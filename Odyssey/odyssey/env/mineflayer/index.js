const fs = require("fs");
const express = require("express");
const mineflayer = require("mineflayer");
const { plugin: pvp } = require("mineflayer-pvp");
const hawkEyeModule = require("minecrafthawkeye");
const bridgePackage = require("./package.json");

const skills = require("./lib/skillLoader");
const { initCounter, getNextTime } = require("./lib/utils");
const obs = require("./lib/observation/base");
const OnChat = require("./lib/observation/onChat");
const OnError = require("./lib/observation/onError");
const { Voxels, BlockRecords } = require("./lib/observation/voxels");
const Status = require("./lib/observation/status");
const Inventory = require("./lib/observation/inventory");
const OnSave = require("./lib/observation/onSave");
const Chests = require("./lib/observation/chests");
let activeBot = null;
let pendingStartResponse = null;
const bridgeStartedAt = Date.now();

const app = express();

app.use(express.json({ limit: "50mb" }));
app.use(express.urlencoded({ limit: "50mb", extended: false }));

const STARTUP_CHUNK_TIMEOUT_MS = 10000;
const STARTUP_PHYSICS_PROBE_MS = 500;
const DEFAULT_MINECRAFT_VERSION = process.env.MC_VERSION || "1.19.4";
const DEFAULT_EXPLORATION_SEED = 42;
const LEGACY_BOT_ADMIN_COMMANDS =
    process.env.ODYSSEY_ALLOW_LEGACY_BOT_ADMIN_COMMANDS === "true";
const hawkEye = hawkEyeModule.default || hawkEyeModule;

function delay(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms));
}

function waitForBotEvent(bot, eventName, timeoutMs) {
    return new Promise((resolve, reject) => {
        const timeout = setTimeout(() => {
            bot.removeListener(eventName, onEvent);
            reject(
                new Error(
                    `[startup-guard] Timed out waiting for ${eventName}`
                )
            );
        }, timeoutMs);
        function onEvent(...args) {
            clearTimeout(timeout);
            resolve(args);
        }
        bot.once(eventName, onEvent);
    });
}

function isFiniteVector(vector) {
    return (
        vector &&
        Number.isFinite(vector.x) &&
        Number.isFinite(vector.y) &&
        Number.isFinite(vector.z)
    );
}

function formatVector(vector) {
    if (!vector) return "(missing)";
    return `(${vector.x}, ${vector.y}, ${vector.z})`;
}

function dependencyVersion(name) {
    try {
        return require(`${name}/package.json`).version;
    } catch (_error) {
        return null;
    }
}

function inventorySnapshot(bot = activeBot) {
    if (!bot?.inventory) return {};
    return bot.inventory.items().reduce((inventory, item) => {
        inventory[item.name] = (inventory[item.name] || 0) + item.count;
        return inventory;
    }, {});
}

function bridgeVersionSnapshot() {
    return {
        bridge: bridgePackage.version,
        node: process.version,
        mineflayer: dependencyVersion("mineflayer"),
        minecraft_data: dependencyVersion("minecraft-data"),
        pathfinder: dependencyVersion("mineflayer-pathfinder"),
        tool: dependencyVersion("mineflayer-tool"),
        collectblock: require("./mineflayer-collectblock/package.json").version,
        target_minecraft: DEFAULT_MINECRAFT_VERSION,
    };
}

function botSnapshot() {
    const bot = activeBot;
    const position = bot?.entity?.position;
    return {
        connected: Boolean(bot?.entity && bot?._client?.state === "play"),
        username: bot?.username || null,
        minecraft_version: bot?.version || null,
        position: position
            ? { x: position.x, y: position.y, z: position.z }
            : null,
        position_finite: position ? isFiniteVector(position) : null,
        inventory: inventorySnapshot(),
        exploration_seed: Number.isInteger(bot?.explorationSeed)
            ? bot.explorationSeed
            : null,
        exploration_rng_state: Number.isInteger(bot?.explorationRngState)
            ? bot.explorationRngState
            : null,
        operator_commands_enabled: LEGACY_BOT_ADMIN_COMMANDS,
        combat_plugins: {
            pvp: Boolean(bot?.pvp),
            hawkeye: Boolean(bot?.hawkEye),
        },
    };
}

app.get("/health", (_req, res) => {
    const currentBot = botSnapshot();
    res.json({
        status:
            currentBot.position_finite === false ? "degraded" : "ok",
        service: bridgePackage.name,
        uptime_ms: Date.now() - bridgeStartedAt,
        versions: bridgeVersionSnapshot(),
        bot: currentBot,
    });
});

app.get("/version", (_req, res) => {
    res.json({
        service: bridgePackage.name,
        versions: bridgeVersionSnapshot(),
    });
});

function localCollisionBlocksLoaded(bot) {
    if (!bot.entity || !isFiniteVector(bot.entity.position)) return false;

    // prismarine-physics can inspect neighboring blocks while resolving a
    // collision. Checking the feet and the block below in a 3x3 area also
    // covers a player standing on a chunk boundary.
    for (const yOffset of [-1, 0]) {
        for (const xOffset of [-1, 0, 1]) {
            for (const zOffset of [-1, 0, 1]) {
                const position = bot.entity.position.offset(
                    xOffset,
                    yOffset,
                    zOffset
                );
                if (bot.blockAt(position, false) === null) return false;
            }
        }
    }
    return true;
}

async function waitForLocalCollisionBlocks(bot, timeoutMs) {
    const deadline = Date.now() + timeoutMs;
    while (Date.now() < deadline) {
        if (localCollisionBlocksLoaded(bot)) return;
        await delay(50);
    }
    throw new Error(
        `[startup-guard] Timed out waiting for collision blocks at ${formatVector(
            bot.entity?.position
        )}`
    );
}

function installFiniteMotionGuard(bot) {
    let lastFinitePosition = null;
    let lastFiniteVelocity = null;
    let startupFault = null;

    function rememberFiniteState() {
        if (
            bot.entity &&
            isFiniteVector(bot.entity.position) &&
            isFiniteVector(bot.entity.velocity)
        ) {
            lastFinitePosition = bot.entity.position.clone();
            lastFiniteVelocity = bot.entity.velocity.clone();
        }
    }

    function recordFault(source, position, velocity) {
        if (startupFault) return;
        startupFault = new Error(
            `[startup-guard] Non-finite motion from ${source}: ` +
                `position=${formatVector(position)}, ` +
                `velocity=${formatVector(velocity)}`
        );
        console.error(startupFault.message);
    }

    // This event runs after physics simulation and before Mineflayer writes
    // the movement packet. Restore the last valid state so a NaN packet never
    // reaches the Minecraft server.
    bot.on("physicsTick", () => {
        if (
            isFiniteVector(bot.entity?.position) &&
            isFiniteVector(bot.entity?.velocity)
        ) {
            rememberFiniteState();
            return;
        }

        recordFault("physicsTick", bot.entity?.position, bot.entity?.velocity);
        bot.physicsEnabled = false;
        bot.clearControlStates();
        if (lastFinitePosition) {
            bot.entity.position.set(
                lastFinitePosition.x,
                lastFinitePosition.y,
                lastFinitePosition.z
            );
        }
        if (lastFiniteVelocity) {
            bot.entity.velocity.set(
                lastFiniteVelocity.x,
                lastFiniteVelocity.y,
                lastFiniteVelocity.z
            );
        }
    });

    // A final protocol-boundary check also covers movement packets emitted by
    // teleport handling rather than a normal physics tick.
    const writePacket = bot._client.write.bind(bot._client);
    bot._client.write = (name, packet) => {
        if (
            ["position", "position_look"].includes(name) &&
            packet &&
            ![packet.x, packet.y, packet.z].every(Number.isFinite)
        ) {
            recordFault(`outgoing ${name}`, packet, bot.entity?.velocity);
            bot.physicsEnabled = false;
            return;
        }
        return writePacket(name, packet);
    };

    return {
        rememberFiniteState,
        getStartupFault: () => startupFault,
    };
}

app.post("/start", (req, res) => {
    const explorationSeed = req.body.seed ?? DEFAULT_EXPLORATION_SEED;
    if (!Number.isInteger(explorationSeed)) {
        res.status(400).json({
            error: "seed must be an integer",
        });
        return;
    }
    const inventory = req.body.inventory;
    const equipment = req.body.equipment;
    const hasInventoryInjection =
        inventory !== undefined &&
        inventory !== null &&
        (typeof inventory !== "object" || Object.keys(inventory).length > 0);
    const hasEquipmentInjection = Array.isArray(equipment)
        ? equipment.some(Boolean)
        : equipment !== undefined && equipment !== null;
    const requestsHostAdmin =
        req.body.reset === "hard" ||
        hasInventoryInjection ||
        hasEquipmentInjection ||
        Boolean(req.body.position) ||
        Boolean(req.body.spread);
    if (!LEGACY_BOT_ADMIN_COMMANDS && requestsHostAdmin) {
        res.status(403).json({
            error:
                "World preparation is host-admin only in the modernized profile. " +
                "Use the RCON host harness, then start the execution bot with reset=soft.",
        });
        return;
    }
    if (pendingStartResponse && !pendingStartResponse.headersSent) {
        pendingStartResponse.status(409).json({
            error: "Start request superseded by a newer request",
        });
    }
    pendingStartResponse = res;

    const previousBot = activeBot;
    if (previousBot) {
        activeBot = null;
        closeBot(previousBot, "Restarting bot");
    }
    console.log(req.body);
    const bot = mineflayer.createBot({
        host: req.body.host, // minecraft server ip
        port: req.body.port, // minecraft server port
        username: req.body.username,
        // E0 uses a pinned server protocol. Mineflayer auto-detection can
        // misidentify the 1.19.4 status response with this dependency set.
        version: req.body.version || DEFAULT_MINECRAFT_VERSION,
        disableChatSigning: true,
        checkTimeoutInterval: 60 * 60 * 1000,
        // A restored player can arrive before its surrounding chunks. Starting
        // old prismarine-physics at that point can turn x/z into NaN.
        physicsEnabled: false,
    });
    activeBot = bot;
    const motionGuard = installFiniteMotionGuard(bot);
    bot.once("error", onConnectionFailed);

    // Event subscriptions
    bot.waitTicks = req.body.waitTicks;
    bot.explorationSeed = explorationSeed >>> 0;
    bot.explorationRngState = bot.explorationSeed;
    bot.allowAdminCommands = LEGACY_BOT_ADMIN_COMMANDS;
    bot.globalTickCounter = 0;
    bot.stuckTickCounter = 0;
    bot.stuckPosList = [];
    bot.iron_pickaxe = false;

    bot.on("kicked", onDisconnect);

    // mounting will cause physicsTick to stop
    bot.on("mount", () => {
        bot.dismount();
    });

    bot.once("spawn", async () => {
        try {
            let itemTicks = 1;
            if (req.body.reset === "hard") {
                bot.chat("/clear @s");
                const respawned = waitForBotEvent(
                    bot,
                    "spawn",
                    STARTUP_CHUNK_TIMEOUT_MS
                );
                bot.chat("/kill @s");
                try {
                    await respawned;
                } catch (error) {
                    throw new Error(
                        "[startup-guard] Hard reset did not respawn the bot; " +
                            "verify that the offline-mode bot UUID is an operator",
                        { cause: error }
                    );
                }
                const inventory = req.body.inventory ? req.body.inventory : {};
                const equipment = req.body.equipment
                    ? req.body.equipment
                    : [null, null, null, null, null, null];
                for (let key in inventory) {
                    bot.chat(`/give @s minecraft:${key} ${inventory[key]}`);
                    itemTicks += 1;
                }
                const equipmentNames = [
                    "armor.head",
                    "armor.chest",
                    "armor.legs",
                    "armor.feet",
                    "weapon.mainhand",
                    "weapon.offhand",
                ];
                for (let i = 0; i < 6; i++) {
                    if (i === 4) continue;
                    if (equipment[i]) {
                        bot.chat(
                            `/item replace entity @s ${equipmentNames[i]} with minecraft:${equipment[i]}`
                        );
                        itemTicks += 1;
                    }
                }
            }

            if (req.body.position) {
                const teleported = waitForBotEvent(
                    bot,
                    "forcedMove",
                    STARTUP_CHUNK_TIMEOUT_MS
                );
                bot.chat(
                    `/tp @s ${req.body.position.x} ${req.body.position.y} ${req.body.position.z}`
                );
                await teleported;
            }

            // if iron_pickaxe is in bot's inventory
            if (
                bot.inventory
                    .items()
                    .find((item) => item.name === "iron_pickaxe")
            ) {
                bot.iron_pickaxe = true;
            }

            const { pathfinder } = require("mineflayer-pathfinder");
            const tool = require("mineflayer-tool").plugin;
            const collectBlock = require("./mineflayer-collectblock").plugin;
            bot.loadPlugin(pathfinder);
            bot.loadPlugin(tool);
            bot.loadPlugin(collectBlock);
            bot.loadPlugin(pvp);
            bot.loadPlugin(hawkEye);

            // bot.collectBlock.movements.digCost = 0;
            // bot.collectBlock.movements.placeCost = 0;

            obs.inject(bot, [
                OnChat,
                OnError,
                Voxels,
                Status,
                Inventory,
                OnSave,
                Chests,
                BlockRecords,
            ]);
            skills.inject(bot);

            if (req.body.spread) {
                const spreadComplete = waitForBotEvent(
                    bot,
                    "forcedMove",
                    STARTUP_CHUNK_TIMEOUT_MS
                );
                bot.chat(`/spreadplayers ~ ~ 0 300 under 80 false @s`);
                await spreadComplete;
            }

            await waitForLocalCollisionBlocks(bot, STARTUP_CHUNK_TIMEOUT_MS);
            motionGuard.rememberFiniteState();
            console.log(
                `[startup-guard] Collision blocks ready at ${formatVector(
                    bot.entity.position
                )}; enabling physics`
            );
            bot.physicsEnabled = true;
            await delay(STARTUP_PHYSICS_PROBE_MS);
            if (motionGuard.getStartupFault()) {
                throw motionGuard.getStartupFault();
            }
            bot.removeListener("error", onConnectionFailed);

            await bot.waitForTicks(bot.waitTicks * itemTicks);
            res.json(bot.observe());
            if (pendingStartResponse === res) pendingStartResponse = null;

            initCounter(bot);
            if (LEGACY_BOT_ADMIN_COMMANDS) {
                bot.chat("/gamerule keepInventory true");
                bot.chat("/gamerule doDaylightCycle false");
            }
        } catch (error) {
            onConnectionFailed(error);
        }
    });

    function onConnectionFailed(e) {
        console.error(e);
        if (activeBot === bot) activeBot = null;
        closeBot(bot, "Bot startup failed");
        if (!res.headersSent) {
            res.status(400).json({ error: e.message || String(e) });
        }
        if (pendingStartResponse === res) pendingStartResponse = null;
    }
    function onDisconnect(message) {
        if (activeBot === bot) activeBot = null;
        closeBot(bot, message);
        if (!res.headersSent) {
            res.status(400).json({
                error: `Bot disconnected during startup: ${String(message)}`,
            });
        }
        if (pendingStartResponse === res) pendingStartResponse = null;
    }
});

app.post("/step", async (req, res) => {
    const bot = activeBot;
    if (!bot) {
        res.status(409).json({ error: "Bot not spawned" });
        return;
    }

    // import useful package
    let response_sent = false;
    let stepListenerAttached = false;
    function cleanupStepListeners() {
        if (stepListenerAttached) {
            process.off("uncaughtException", otherError);
            stepListenerAttached = false;
        }
        bot.removeListener("physicsTick", onTick);
    }
    function otherError(err) {
        if (response_sent) return;
        console.log("Uncaught Error");
        const formattedError = handleError(err);
        bot.emit("error", formattedError);
        Promise.race([bot.waitForTicks(bot.waitTicks), delay(1000)])
            .then(() => {
                if (!response_sent && !res.headersSent) {
                    response_sent = true;
                    res.json(bot.observe());
                }
            })
            .catch(() => {
                if (!response_sent && !res.headersSent) {
                    response_sent = true;
                    res.status(500).json({ error: formattedError });
                }
            });
    }

    res.once("finish", cleanupStepListeners);
    res.once("close", cleanupStepListeners);

    process.on("uncaughtException", otherError);
    stepListenerAttached = true;

    const mcData = require("minecraft-data")(bot.version);
    mcData.itemsByName["leather_cap"] = mcData.itemsByName["leather_helmet"];
    mcData.itemsByName["leather_tunic"] =
        mcData.itemsByName["leather_chestplate"];
    mcData.itemsByName["leather_pants"] =
        mcData.itemsByName["leather_leggings"];
    mcData.itemsByName["leather_boots"] = mcData.itemsByName["leather_boots"];
    mcData.itemsByName["lapis_lazuli_ore"] = mcData.itemsByName["lapis_ore"];
    mcData.blocksByName["lapis_lazuli_ore"] = mcData.blocksByName["lapis_ore"];
    const {
        Movements,
        goals: {
            Goal,
            GoalBlock,
            GoalNear,
            GoalXZ,
            GoalNearXZ,
            GoalY,
            GoalGetToBlock,
            GoalLookAtBlock,
            GoalBreakBlock,
            GoalCompositeAny,
            GoalCompositeAll,
            GoalInvert,
            GoalFollow,
            GoalPlaceBlock,
        },
        pathfinder,
        Move,
        ComputedPath,
        PartiallyComputedPath,
        XZCoordinates,
        XYZCoordinates,
        SafeBlock,
        GoalPlaceBlockOptions,
    } = require("mineflayer-pathfinder");
    const { Vec3 } = require("vec3");

    // Set up pathfinder
    const movements = new Movements(bot, mcData);
    bot.pathfinder.setMovements(movements);

    bot.globalTickCounter = 0;
    bot.stuckTickCounter = 0;
    bot.stuckPosList = [];

    function onTick() {
        bot.globalTickCounter++;
        if (bot.pathfinder.isMoving()) {
            bot.stuckTickCounter++;
            if (bot.stuckTickCounter >= 100) {
                onStuck(1.5);
                bot.stuckTickCounter = 0;
            }
        }
    }

    bot.on("physicsTick", onTick);

    // initialize fail count
    let _craftItemFailCount = 0;
    let _killMobFailCount = 0;
    let _mineBlockFailCount = 0;
    let _placeItemFailCount = 0;
    let _smeltItemFailCount = 0;

    // Retrieve array form post bod
    const code = req.body.code;
    const programs = req.body.programs;
    bot.cumulativeObs = [];
    await bot.waitForTicks(bot.waitTicks);
    const r = await evaluateCode(code, programs);
    process.off("uncaughtException", otherError);
    stepListenerAttached = false;
    if (r !== "success") {
        bot.emit("error", handleError(r));
    }
    await returnItems();
    // wait for last message
    await bot.waitForTicks(bot.waitTicks);
    if (!response_sent) {
        response_sent = true;
        res.json(bot.observe());
    }
    bot.removeListener("physicsTick", onTick);

    async function evaluateCode(code, programs) {
        // Echo the code produced for players to see it. Don't echo when the bot code is already producing dialog or it will double echo
        try {
            await eval("(async () => {" + programs + "\n" + code + "})()");
            return "success";
        } catch (err) {
            return err;
        }
    }

    function onStuck(posThreshold) {
        const currentPos = bot.entity.position;
        bot.stuckPosList.push(currentPos);

        // Check if the list is full
        if (bot.stuckPosList.length === 5) {
            const oldestPos = bot.stuckPosList[0];
            const posDifference = currentPos.distanceTo(oldestPos);

            if (posDifference < posThreshold) {
                teleportBot(); // execute the function
            }

            // Remove the oldest time from the list
            bot.stuckPosList.shift();
        }
    }

    function teleportBot() {
        if (!LEGACY_BOT_ADMIN_COMMANDS) {
            bot.pathfinder.setGoal(null);
            bot.chat(
                "Pathfinder stopped after detecting a stuck position; " +
                    "host-admin teleport is disabled."
            );
            return;
        }
        const blocks = bot.findBlocks({
            matching: (block) => {
                return block.type === 0;
            },
            maxDistance: 1,
            count: 27,
        });

        if (blocks) {
            // console.log(blocks.length);
            const randomIndex = Math.floor(Math.random() * blocks.length);
            const block = blocks[randomIndex];
            bot.chat(`/tp @s ${block.x} ${block.y} ${block.z}`);
        } else {
            bot.chat("/tp @s ~ ~1.25 ~");
        }
    }

    function returnItems() {
        if (!LEGACY_BOT_ADMIN_COMMANDS) return;
        bot.chat("/gamerule doTileDrops false");
        const crafting_table = bot.findBlock({
            matching: mcData.blocksByName.crafting_table.id,
            maxDistance: 128,
        });
        if (crafting_table) {
            bot.chat(
                `/setblock ${crafting_table.position.x} ${crafting_table.position.y} ${crafting_table.position.z} air destroy`
            );
            bot.chat("/give @s crafting_table");
        }
        const furnace = bot.findBlock({
            matching: mcData.blocksByName.furnace.id,
            maxDistance: 128,
        });
        if (furnace) {
            bot.chat(
                `/setblock ${furnace.position.x} ${furnace.position.y} ${furnace.position.z} air destroy`
            );
            bot.chat("/give @s furnace");
        }
        if (bot.inventoryUsed() >= 32) {
            // if chest is not in bot's inventory
            if (!bot.inventory.items().find((item) => item.name === "chest")) {
                bot.chat("/give @s chest");
            }
        }
        // if iron_pickaxe not in bot's inventory and bot.iron_pickaxe
        if (
            bot.iron_pickaxe &&
            !bot.inventory.items().find((item) => item.name === "iron_pickaxe")
        ) {
            bot.chat("/give @s iron_pickaxe");
        }
        bot.chat("/gamerule doTileDrops true");
    }

    function handleError(err) {
        let stack = err.stack;
        if (!stack) {
            return err;
        }
        console.log(stack);
        const final_line = stack.split("\n")[1];
        const regex = /<anonymous>:(\d+):\d+\)/;

        const programs_length = programs.split("\n").length;
        let match_line = null;
        for (const line of stack.split("\n")) {
            const match = regex.exec(line);
            if (match) {
                const line_num = parseInt(match[1]);
                if (line_num >= programs_length) {
                    match_line = line_num - programs_length;
                    break;
                }
            }
        }
        if (!match_line) {
            return err.message;
        }
        let f_line = final_line.match(
            /\((?<file>.*):(?<line>\d+):(?<pos>\d+)\)/
        );
        if (f_line && f_line.groups && fs.existsSync(f_line.groups.file)) {
            const { file, line, pos } = f_line.groups;
            const f = fs.readFileSync(file, "utf8").split("\n");
            // let filename = file.match(/(?<=node_modules\\)(.*)/)[1];
            let source = file + `:${line}\n${f[line - 1].trim()}\n `;

            const code_source =
                "at " +
                code.split("\n")[match_line - 1].trim() +
                " in your code";
            return source + err.message + "\n" + code_source;
        } else if (
            f_line &&
            f_line.groups &&
            f_line.groups.file.includes("<anonymous>")
        ) {
            const { file, line, pos } = f_line.groups;
            let source =
                "Your code" +
                `:${match_line}\n${code.split("\n")[match_line - 1].trim()}\n `;
            let code_source = "";
            if (line < programs_length) {
                source =
                    "In your program code: " +
                    programs.split("\n")[line - 1].trim() +
                    "\n";
                code_source = `at line ${match_line}:${code
                    .split("\n")
                    [match_line - 1].trim()} in your code`;
            }
            return source + err.message + "\n" + code_source;
        }
        return err.message;
    }
});

app.post("/stop", (req, res) => {
    const bot = activeBot;
    if (!bot) {
        res.status(409).json({ error: "Bot not spawned" });
        return;
    }
    activeBot = null;
    closeBot(bot, "Bot stopped");
    res.json({
        message: "Bot stopped",
    });
});

app.post("/pause", (req, res) => {
    if (!LEGACY_BOT_ADMIN_COMMANDS) {
        res.status(403).json({
            error: "Server pause is disabled in the modernized non-OP profile",
        });
        return;
    }
    const bot = activeBot;
    if (!bot) {
        res.status(400).json({ error: "Bot not spawned" });
        return;
    }
    bot.chat("/pause");
    bot.waitForTicks(bot.waitTicks).then(() => {
        res.json({ message: "Success" });
    });
});

function closeBot(bot, message) {
    if (!bot) return;
    if (bot.viewer) bot.viewer.close();
    if (bot._client?.state !== "disconnected") bot.end();
    if (message) console.log(message);
}

// Server listening to PORT 3000

const DEFAULT_PORT = 3000;
const PORT = process.argv[2] || DEFAULT_PORT;
app.listen(PORT, () => {
    console.log(`Server started on port ${PORT}`);
});
