#!/usr/bin/env node
"use strict";

const assert = require("node:assert/strict");
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

    plus(other) {
        return new Vec3(this.x + other.x, this.y + other.y, this.z + other.z);
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

function source(...parts) {
    return parts
        .map((part) => fs.readFileSync(part, "utf8"))
        .join("\n\n");
}

const spatial = new Function(
    "Vec3",
    `${source(
        path.join(PRIMITIVE_ROOT, "checkBlockAbove.js"),
        path.join(PRIMITIVE_ROOT, "checkBlocksAround.js"),
        path.join(PRIMITIVE_ROOT, "checkNoAdjacentBlock.js"),
        path.join(PRIMITIVE_ROOT, "findSuitablePosition.js")
    )}\nreturn { checkBlockAbove, checkBlocksAround, findSuitablePosition };`
)(Vec3);

const armorNames = [
    "diamond_chestplate",
    "iron_chestplate",
    "golden_chestplate",
    "chainmail_chestplate",
    "leather_chestplate",
    "diamond_leggings",
    "iron_leggings",
    "golden_leggings",
    "chainmail_leggings",
    "leather_leggings",
    "diamond_helmet",
    "iron_helmet",
    "golden_helmet",
    "chainmail_helmet",
    "leather_helmet",
    "diamond_boots",
    "iron_boots",
    "golden_boots",
    "chainmail_boots",
    "leather_boots",
];
const armorMcData = { itemsByName: {} };
for (const [index, name] of armorNames.entries()) {
    armorMcData.itemsByName[name] = { id: index + 1, name };
}
const { equipArmor } = new Function(
    "mcData",
    `${source(path.join(PRIMITIVE_ROOT, "equipArmor.js"))}\nreturn { equipArmor };`
)(armorMcData);

const { killAnimal } = new Function(
    "equipSword",
    "killMob",
    `${source(path.join(PRIMITIVE_ROOT, "killAnimal.js"))}\nreturn { killAnimal };`
)(
    async () => true,
    async (_bot, type, timeout) => ({ type, timeout, collected: true })
);

const { nextExplorationRandom } = new Function(
    `${source(path.join(CONTROL_ROOT, "exploreUntil.js"))}\n` +
        "return { nextExplorationRandom };"
)();

const tests = [];
function test(name, callback) {
    tests.push({ name, callback });
}

test("spatial primitives keep the public Vec3 contract", async () => {
    const origin = new Vec3(10, 64, -5);
    const bot = {
        blockAt(position) {
            if (position.x === 10 && position.y === 65 && position.z === -5) {
                return { name: "air" };
            }
            if (position.x === 11 && position.y === 64 && position.z === -5) {
                return { name: "water" };
            }
            return { name: "stone" };
        },
    };
    assert.equal(await spatial.checkBlockAbove(bot, "air", origin), true);
    assert.equal(await spatial.checkBlocksAround(bot, "water", origin), true);
    await assert.rejects(
        spatial.checkBlockAbove(bot, "air", { x: 10, y: 64, z: -5 }),
        /Vec3/
    );
});

test("findSuitablePosition preserves water as a public-code target", async () => {
    const bot = {
        entity: { position: new Vec3(0, 64, 0) },
        blockAt(position) {
            if (position.x === 1 && position.y === 64 && position.z === 0) {
                return { name: "water" };
            }
            if (position.x === 1 && position.y === 63 && position.z === 0) {
                return { name: "stone" };
            }
            return { name: "water" };
        },
    };
    assert.deepEqual(
        await spatial.findSuitablePosition(bot),
        new Vec3(1, 64, 0)
    );
});

test("equipArmor preserves gold before chainmail", async () => {
    const byId = new Map(
        [
            "golden_chestplate",
            "chainmail_chestplate",
            "golden_leggings",
            "chainmail_leggings",
            "golden_helmet",
            "chainmail_helmet",
            "golden_boots",
            "chainmail_boots",
        ].map((name) => {
            const item = armorMcData.itemsByName[name];
            return [item.id, item];
        })
    );
    const equipped = [];
    const bot = {
        inventory: {
            findInventoryItem(id) {
                return byId.get(id) || null;
            },
        },
        async equip(item, destination) {
            equipped.push([item.name, destination]);
        },
        chat() {},
    };
    await equipArmor(bot);
    assert.deepEqual(equipped, [
        ["golden_chestplate", "torso"],
        ["golden_leggings", "legs"],
        ["golden_helmet", "head"],
        ["golden_boots", "feet"],
    ]);
});

test("killAnimal delegates target, combat and drop ownership once", async () => {
    const bot = {
        pathfinder: {
            async goto() {
                throw new Error("killAnimal must not perform a second move");
            },
        },
        chat(message) {
            assert.notEqual(message, "Collected dropped items.");
        },
    };
    assert.deepEqual(await killAnimal(bot, "cow"), {
        type: "cow",
        timeout: 300,
        collected: true,
    });
});

test("exploration seed 42 produces a repeatable non-constant sequence", () => {
    const first = { explorationSeed: 42 };
    const second = { explorationSeed: 42 };
    const firstSequence = Array.from({ length: 8 }, () =>
        nextExplorationRandom(first)
    );
    const secondSequence = Array.from({ length: 8 }, () =>
        nextExplorationRandom(second)
    );
    assert.deepEqual(firstSequence, secondSequence);
    assert.deepEqual(firstSequence.slice(0, 3), [
        0.2523451747838408,
        0.08812504541128874,
        0.5772811982315034,
    ]);
    assert.ok(new Set(firstSequence).size > 1);
    assert.ok(firstSequence.every((value) => value >= 0 && value < 1));
});

test("modernized execution profile contains no bot operator", () => {
    const ops = JSON.parse(
        fs.readFileSync(
            path.join(
                ODYSSEY_ROOT,
                "server-profile",
                "modernized",
                "ops.json"
            ),
            "utf8"
        )
    );
    assert.deepEqual(ops, []);
    const compose = fs.readFileSync(
        path.join(ODYSSEY_ROOT, "docker-compose.yml"),
        "utf8"
    );
    assert.match(compose, /server-profile\/modernized\/ops\.json/);
    assert.match(compose, /ENABLE_RCON: "TRUE"/);
    assert.match(compose, /ODYSSEY_RCON_PASSWORD/);
    assert.doesNotMatch(compose, /25575:25575/);
    const bridge = fs.readFileSync(
        path.join(ODYSSEY_ROOT, "odyssey", "env", "bridge.py"),
        "utf8"
    );
    assert.match(bridge, /options\.get\("mode", "soft"\)/);
    assert.match(bridge, /server-host RCON/);
    const mineflayerBridge = fs.readFileSync(
        path.join(
            ODYSSEY_ROOT,
            "odyssey",
            "env",
            "mineflayer",
            "index.js"
        ),
        "utf8"
    );
    assert.match(mineflayerBridge, /requestsHostAdmin/);
    assert.match(mineflayerBridge, /operator_commands_enabled/);
    const skillLoader = fs.readFileSync(
        path.join(
            ODYSSEY_ROOT,
            "odyssey",
            "env",
            "mineflayer",
            "lib",
            "skillLoader.js"
        ),
        "utf8"
    );
    assert.match(skillLoader, /startsWith\("\/"\)/);
    const killMonsters = fs.readFileSync(
        path.join(PRIMITIVE_ROOT, "killMonsters.js"),
        "utf8"
    );
    assert.doesNotMatch(killMonsters, /\/gamemode/);
});

async function main() {
    let passed = 0;
    for (const { name, callback } of tests) {
        try {
            await callback();
            passed += 1;
            console.log(`PASS ${name}`);
        } catch (error) {
            console.error(`FAIL ${name}`);
            console.error(error);
            process.exitCode = 1;
        }
    }
    console.log(`${passed}/${tests.length} primitive policy fixtures passed`);
}

main();
