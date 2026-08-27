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

class Vec3 {
    constructor(x, y, z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    distanceTo(other) {
        return Math.hypot(
            this.x - other.x,
            this.y - other.y,
            this.z - other.z
        );
    }
}

class GoalNear {
    constructor(x, y, z, range) {
        // Match mineflayer-pathfinder's GoalNear coordinate contract.
        this.x = Math.floor(x);
        this.y = Math.floor(y);
        this.z = Math.floor(z);
        this.range = range;
    }
}

const mcData = {
    itemsByName: {
        wheat: { id: 1 },
        wheat_seeds: { id: 2 },
        carrot: { id: 3 },
    },
};

let exploreHandler = async (_bot, _direction, _maxTime, callback) =>
    callback();

async function exploreUntil(...args) {
    return exploreHandler(...args);
}

function loadPrimitives() {
    const source = ["goto.js", "getAnimal.js"]
        .map((name) =>
            fs.readFileSync(path.join(PRIMITIVE_ROOT, name), "utf8")
        )
        .join("\n\n");
    return new Function(
        "Vec3",
        "GoalNear",
        "exploreUntil",
        "mcData",
        `${source}\nreturn { goto, getAnimal };`
    )(Vec3, GoalNear, exploreUntil, mcData);
}

const { goto, getAnimal } = loadPrimitives();

function makeBot({ animal = null, foodName = null, followAnimal = true } = {}) {
    const chats = [];
    const equips = [];
    const pathCalls = [];
    const cancelledGoals = [];
    const food = foodName
        ? { name: foodName, type: mcData.itemsByName[foodName].id }
        : null;
    const bot = {
        entity: { position: new Vec3(0, 64, 0) },
        inventory: {
            findInventoryItem(id) {
                return food?.type === id ? food : null;
            },
        },
        pathfinder: {
            async goto(goal) {
                pathCalls.push(goal);
                bot.entity.position = new Vec3(goal.x, goal.y, goal.z);
                if (animal && followAnimal && pathCalls.length > 1) {
                    animal.position = new Vec3(goal.x + 1, goal.y, goal.z);
                }
            },
            setGoal(goal) {
                cancelledGoals.push(goal);
            },
        },
        nearestEntity(predicate) {
            return animal && predicate(animal) ? animal : null;
        },
        async equip(item, destination) {
            equips.push({ item, destination });
        },
        async lookAt() {},
        async waitForTicks() {},
        chat(message) {
            chats.push(message);
        },
        _fixture: { chats, equips, pathCalls, cancelledGoals },
    };
    return bot;
}

const tests = [];

function test(name, callback) {
    tests.push({ name, callback });
}

test("goto returns without pathfinding when already within two blocks", async () => {
    const bot = makeBot();
    assert.equal(await goto(bot, 1, 64, 0), true);
    assert.equal(bot._fixture.pathCalls.length, 0);
});

test("goto uses GoalNear and verifies the final position", async () => {
    const bot = makeBot();
    assert.equal(await goto(bot, 8, 64, 3), true);
    assert.equal(bot._fixture.pathCalls.length, 1);
    assert.deepEqual(bot.entity.position, new Vec3(8, 64, 3));
    assert.equal(bot._fixture.pathCalls[0].range, 2);
});

test("goto evaluates fractional targets on GoalNear's block grid", async () => {
    const bot = makeBot();
    bot.entity.position = new Vec3(
        39.48792155165041,
        64,
        -68.32084320891104
    );
    bot.pathfinder.goto = async (goal) => {
        bot._fixture.pathCalls.push(goal);
        bot.entity.position = new Vec3(
            43.34198871358728,
            64,
            -68.5037593273642
        );
    };

    assert.equal(
        await goto(bot, 45.48792155165041, 64, -68.32084320891104),
        true
    );
    assert.deepEqual(
        bot._fixture.pathCalls[0],
        new GoalNear(45.48792155165041, 64, -68.32084320891104, 2)
    );
});

test("goto rejects non-finite coordinates", async () => {
    const bot = makeBot();
    await assert.rejects(
        goto(bot, Number.NaN, 64, 0),
        /must be finite numbers/
    );
});

test("goto cancels pathfinding after its timeout", async () => {
    const bot = makeBot();
    bot.pathfinder.goto = async () => new Promise(() => {});
    await assert.rejects(goto(bot, 8, 64, 0, 5), /timed out after 5ms/);
    assert.deepEqual(bot._fixture.cancelledGoals, [null]);
});

test("goto rejects a pathfinder result that is still too far away", async () => {
    const bot = makeBot();
    bot.pathfinder.goto = async (goal) => {
        bot._fixture.pathCalls.push(goal);
    };
    await assert.rejects(goto(bot, 8, 64, 0), /pathfinder stopped/);
});

for (const [type, foodName] of [
    ["sheep", "wheat"],
    ["cow", "wheat"],
    ["chicken", "wheat_seeds"],
    ["pig", "carrot"],
]) {
    test(`getAnimal lures ${type} with ${foodName}`, async () => {
        const animal = {
            name: type,
            position: new Vec3(3, 64, 0),
        };
        const bot = makeBot({ animal, foodName });
        exploreHandler = async (_bot, _direction, _maxTime, callback) =>
            callback();

        const result = await getAnimal(bot, type, 10, 64, 0);

        assert.equal(result, animal);
        assert.equal(bot._fixture.equips.length, 1);
        assert.equal(bot._fixture.equips[0].item.name, foodName);
        assert.equal(bot._fixture.equips[0].destination, "hand");
        assert.equal(bot._fixture.pathCalls.length, 2);
        assert.ok(animal.position.distanceTo(new Vec3(10, 64, 0)) <= 4);
    });
}

test("getAnimal rejects an unsupported animal type", async () => {
    const bot = makeBot({ foodName: "carrot" });
    await assert.rejects(
        getAnimal(bot, "rabbit", 10, 64, 0),
        /unsupported animal type/
    );
});

test("getAnimal rejects a missing lure item", async () => {
    const bot = makeBot();
    await assert.rejects(
        getAnimal(bot, "cow", 10, 64, 0),
        /wheat is required/
    );
});

test("getAnimal rejects when exploration finds no animal", async () => {
    const bot = makeBot({ foodName: "wheat" });
    exploreHandler = async () => null;
    await assert.rejects(
        getAnimal(bot, "cow", 10, 64, 0),
        /could not find a cow/
    );
});

test("getAnimal rejects when the animal does not reach the target", async () => {
    const animal = { name: "cow", position: new Vec3(3, 64, 0) };
    const bot = makeBot({ animal, foodName: "wheat", followAnimal: false });
    exploreHandler = async (_bot, _direction, _maxTime, callback) => callback();
    await assert.rejects(
        getAnimal(bot, "cow", 20, 64, 0),
        /did not reach within 4 blocks/
    );
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
    console.log(`${passed}/${tests.length} primitive offline fixtures passed`);
}

main();
