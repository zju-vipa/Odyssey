#!/usr/bin/env node
"use strict";

const assert = require("node:assert/strict");
const { EventEmitter } = require("node:events");
const fs = require("node:fs");
const path = require("node:path");

const ODYSSEY_ROOT = path.resolve(__dirname, "..");
const PRIMITIVE_ROOT = path.join(
    ODYSSEY_ROOT,
    "skill_library",
    "skill",
    "primitive"
);
const CONTROL_ROOT = path.join(ODYSSEY_ROOT, "odyssey", "control_primitives");

class Vec3 {
    constructor(x, y, z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    offset(x, y, z) {
        return new Vec3(this.x + x, this.y + y, this.z + z);
    }

    distanceTo(other) {
        return Math.hypot(
            this.x - other.x,
            this.y - other.y,
            this.z - other.z
        );
    }
}

class GoalBlock {
    constructor(x, y, z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }
}

class GoalLookAtBlock {
    constructor(position) {
        this.position = position;
    }
}

const mcData = {
    itemsByName: {
        wheat: { id: 1 },
        carrot: { id: 2 },
        wheat_seeds: { id: 3 },
        furnace: { id: 4 },
        coal: { id: 5 },
        beef: { id: 6 },
        bread: { id: 7 },
        torch: { id: 8 },
    },
};

function readSource(...parts) {
    return parts.map((part) => fs.readFileSync(part, "utf8")).join("\n\n");
}

function primitiveSource(name) {
    return readSource(path.join(PRIMITIVE_ROOT, `${name}.js`));
}

function controlSource(name) {
    return readSource(path.join(CONTROL_ROOT, `${name}.js`));
}

const tests = [];
function test(name, callback) {
    tests.push({ name, callback });
}

test("combat plugins are exact-locked and loaded by the bridge", () => {
    const packageJson = JSON.parse(
        fs.readFileSync(
            path.join(
                ODYSSEY_ROOT,
                "odyssey",
                "env",
                "mineflayer",
                "package.json"
            ),
            "utf8"
        )
    );
    assert.equal(packageJson.dependencies["mineflayer-pvp"], "1.3.2");
    assert.equal(packageJson.dependencies.minecrafthawkeye, "1.3.8");
    const bridge = fs.readFileSync(
        path.join(
            ODYSSEY_ROOT,
            "odyssey",
            "env",
            "mineflayer",
            "index.js"
        ),
        "utf8"
    );
    assert.match(bridge, /bot\.loadPlugin\(pvp\)/);
    assert.match(bridge, /bot\.loadPlugin\(hawkEye\)/);
    assert.equal(typeof require("mineflayer-pvp").plugin, "function");
    const hawkEyeModule = require("minecrafthawkeye");
    assert.equal(typeof (hawkEyeModule.default || hawkEyeModule), "function");
});

test("getItemFromChest uses containerItems and withdraw", async () => {
    const { getItemFromChest } = new Function(
        "Vec3",
        "GoalLookAtBlock",
        "mcData",
        `${controlSource("useChest")}\nreturn { getItemFromChest };`
    )(Vec3, GoalLookAtBlock, mcData);
    const position = new Vec3(1, 64, 1);
    const withdrawn = [];
    const container = {
        containerItems() {
            return [{ name: "torch", type: 8, count: 3 }];
        },
        async withdraw(type, metadata, count) {
            withdrawn.push({ type, metadata, count });
        },
        async close() {},
    };
    const bot = {
        entity: { position: new Vec3(0, 64, 0) },
        world: {},
        pathfinder: { async goto() {} },
        blockAt() {
            return { name: "chest", position };
        },
        async openContainer() {
            return container;
        },
        chat() {},
    };
    await getItemFromChest(bot, position, { torch: 2 });
    assert.deepEqual(withdrawn, [{ type: 8, metadata: null, count: 2 }]);
});

test("feedAnimals equips the animal-specific food before useOn", async () => {
    const animal = {
        uuid: "cow-1",
        name: "cow",
        position: new Vec3(2, 64, 0),
    };
    const equipped = [];
    const used = [];
    const { feedAnimals } = new Function(
        "mcData",
        "Vec3",
        "GoalBlock",
        "exploreUntil",
        `${primitiveSource("feedAnimals")}\nreturn { feedAnimals };`
    )(
        mcData,
        Vec3,
        GoalBlock,
        async (_bot, _direction, _seconds, callback) => callback()
    );
    const bot = {
        entity: { position: new Vec3(0, 64, 0) },
        inventory: {
            findInventoryItem(id) {
                return id === mcData.itemsByName.wheat.id
                    ? { id, name: "wheat" }
                    : null;
            },
        },
        nearestEntity(predicate) {
            return predicate(animal) ? animal : null;
        },
        pathfinder: { async goto() {} },
        async equip(item, destination) {
            equipped.push([item.name, destination]);
        },
        async lookAt() {},
        async useOn(entity) {
            used.push(entity.uuid);
        },
        chat() {},
    };
    assert.equal(await feedAnimals(bot, 1, "cow"), 1);
    assert.deepEqual(equipped, [["wheat", "hand"]]);
    assert.deepEqual(used, ["cow-1"]);
});

test("cookFood stops on missing coal and returns the real smelt count", async () => {
    const calls = [];
    let inventory = new Map([
        [mcData.itemsByName.furnace.id, { name: "furnace" }],
        [mcData.itemsByName.beef.id, { name: "beef" }],
    ]);
    const { cookFood } = new Function(
        "mcData",
        "findSuitablePosition",
        "placeItem",
        "smeltItem",
        `${primitiveSource("cookFood")}\nreturn { cookFood };`
    )(
        mcData,
        async () => {
            calls.push("position");
            return new Vec3(1, 64, 0);
        },
        async () => calls.push("place"),
        async (_bot, _type, _fuel, count) => {
            calls.push("smelt");
            return count;
        }
    );
    const messages = [];
    const bot = {
        inventory: { findInventoryItem: (id) => inventory.get(id) || null },
        chat(message) {
            messages.push(message);
        },
    };
    assert.equal(await cookFood(bot, "beef", 2), 0);
    assert.deepEqual(calls, []);
    assert.ok(messages.includes("No coal found in inventory."));

    inventory.set(mcData.itemsByName.coal.id, { name: "coal" });
    messages.length = 0;
    assert.equal(await cookFood(bot, "beef", 2), 2);
    assert.deepEqual(calls, ["position", "place", "smelt"]);
    assert.doesNotMatch(messages.join("\n"), /^1 beef cooked\.$/m);
});

test("killMonsters has local state, handles missing targets and removes death listener", async () => {
    let killResult = { entity: { name: "zombie" }, droppedItem: null };
    let killCalls = 0;
    const { killMonsters } = new Function(
        "equipSword",
        "equipArmor",
        "killMob",
        `${primitiveSource("killMonsters")}\nreturn { killMonsters };`
    )(
        async () => true,
        async () => true,
        async () => {
            killCalls++;
            return killResult;
        }
    );
    const bot = new EventEmitter();
    bot.chat = () => {};
    assert.equal(await killMonsters(bot, "zombie", 2), true);
    assert.equal(killCalls, 2);
    assert.equal(bot.listenerCount("death"), 0);

    killResult = null;
    assert.equal(await killMonsters(bot, "zombie", 1), false);
    assert.equal(bot.listenerCount("death"), 0);
});

test("plantSeeds exits cleanly for missing seed and empty farmland", async () => {
    const { plantSeeds } = new Function(
        "mcData",
        "Vec3",
        "GoalBlock",
        "checkBlockAbove",
        `${primitiveSource("plantSeeds")}\nreturn { plantSeeds };`
    )(mcData, Vec3, GoalBlock, async () => true);
    let equipped = false;
    const messages = [];
    const bot = {
        inventory: { findInventoryItem: () => null },
        async equip() {
            equipped = true;
        },
        findBlocks: () => [],
        chat(message) {
            messages.push(message);
        },
    };
    assert.equal(await plantSeeds(bot, "wheat_seeds"), 0);
    assert.equal(equipped, false);
    assert.ok(messages.includes("No wheat_seeds found in inventory."));

    bot.inventory.findInventoryItem = () => ({ name: "wheat_seeds" });
    assert.equal(await plantSeeds(bot, "wheat_seeds"), 0);
    assert.equal(equipped, true);
    assert.ok(
        messages.includes("No farmland nearby, return to my fields first!")
    );
});

test("eatFood rejects a missing item before equip and consumes a present item", async () => {
    const { eatFood } = new Function(
        "mcData",
        `${primitiveSource("eatFood")}\nreturn { eatFood };`
    )(mcData);
    let food = null;
    let equipped = 0;
    let consumed = 0;
    const bot = {
        food: 10,
        inventory: { findInventoryItem: () => food },
        chat() {},
        async equip() {
            equipped++;
        },
        async consume() {
            consumed++;
        },
    };
    assert.equal(await eatFood(bot, "bread"), false);
    assert.equal(equipped, 0);
    food = { name: "bread" };
    assert.equal(await eatFood(bot, "bread"), true);
    assert.equal(equipped, 1);
    assert.equal(consumed, 1);
});

test("findSuitablePosition scans 25 unique symmetric offsets", async () => {
    const { findSuitablePosition } = new Function(
        "Vec3",
        "checkNoAdjacentBlock",
        `${primitiveSource("findSuitablePosition")}\n` +
            "return { findSuitablePosition };"
    )(Vec3, async () => false);
    const visited = [];
    const bot = {
        entity: { position: new Vec3(0, 64, 0) },
        blockAt(position) {
            visited.push(`${position.x},${position.y},${position.z}`);
            return { name: "stone" };
        },
    };
    assert.equal(await findSuitablePosition(bot), null);
    assert.equal(visited.length, 25);
    assert.equal(new Set(visited).size, 25);
    for (const y of [63, 64, 65]) {
        for (const [x, z] of [
            [1, 1],
            [-1, 1],
            [1, -1],
            [-1, -1],
        ]) {
            assert.ok(visited.includes(`${x},${y},${z}`));
        }
    }
});

async function main() {
    let passed = 0;
    for (const { name, callback } of tests) {
        try {
            await callback();
            passed++;
            console.log(`PASS ${name}`);
        } catch (error) {
            console.error(`FAIL ${name}`);
            console.error(error);
            process.exitCode = 1;
        }
    }
    console.log(`${passed}/${tests.length} primitive contract fixtures passed`);
}

main();
