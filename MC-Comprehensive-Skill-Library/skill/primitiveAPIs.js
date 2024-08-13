async function craftItem(bot, count = 1, type, need_crafting_table = true, recursive = true) {
    // return if type is not string
    if (typeof type !== "string") {
        throw new Error("type for craftItem must be a string");
    }
    // return if count is not number
    if (typeof count !== "number") {
        throw new Error("count for craftItem must be a number");
    }
    let original_count = await getTotalCount(bot, type);
    let output_count = 1; // Output count from the recipe
    if (recursive) {
        bot.chat(`Recursively executing craftItem(bot, ${count}, ${type})...`);
        // check pre material
        let pre_item_info = await preItem(type);
        // bot.chat(`pre item info of ${type}: ${JSON.stringify(pre_item_info)}`);
        let [item_array, num, bool] = pre_item_info;
        output_count = num;
        need_crafting_table = bool;
        for (const item of item_array) {
            let [need_count_str, need_type] = item.split(' ');
            let need_count = Math.ceil(count / output_count * parseFloat(need_count_str));
            let inv_count = await getTotalCount(bot, need_type);
            // if not enough
            if (inv_count < need_count) {
                await obtainItem(bot, need_count - inv_count, need_type);
            }
        }
    }
    let craft_times = Math.ceil(count / output_count);
    // specify plank type
    if (type == "plank") {
        const log_names = ["oak_log", "birch_log", "spruce_log", "jungle_log", 
            "acacia_log", "dark_oak_log", "mangrove_log", "crimson_stem", "warped_stem"];
        const plank_names = ["oak_planks", "birch_planks", "spruce_planks", "jungle_planks", 
            "acacia_planks", "dark_oak_planks", "mangrove_planks", "crimson_planks", "warped_planks"];
        let log_in_inventory = log_names.find(logName => bot.inventory.count(mcData.itemsByName[logName].id) > 0);
        const log_index = log_names.indexOf(log_in_inventory);
        const plank_name = plank_names[log_index];
        type = plank_name;
    } 
    // craft
    let item_by_name = mcData.itemsByName[type];
    if (!item_by_name) {
        throw new Error(`No item named ${type}`);
    }
    if (!need_crafting_table) {
        const recipe = bot.recipesFor(item_by_name.id, null, 1, null)[0];
        // bot.chat(`recipe: ${JSON.stringify(recipe)}`);
        try {
            await bot.craft(recipe, craft_times, null);
            bot.chat(`I did the recipe for ${type} ${craft_times} times`);
        } catch (err) {
            bot.chat(`I cannot do the recipe for ${type} ${craft_times} times`);
        }
    } else { // need crafting_table
        let craftingTableBlock = bot.findBlock({matching: mcData.blocksByName.crafting_table.id, maxDistance: 32,});
        if (!craftingTableBlock) {
            // no crafting_table nearby, craft one
            // check crafting_table in inventory
            const craftingTable = bot.inventory.findInventoryItem(mcData.itemsByName.crafting_table.id);
            if (!craftingTable) {
                if (recursive) {
                    await craftItem(bot, 1, "crafting_table", false, true);
                } else {
                    bot.chat("Craft without a crafting table");
                }
            }
            // place crafting_table
            const craftingTablePosition = await findSuitablePosition(bot);
            await placeItem(bot, "crafting_table", craftingTablePosition);
            craftingTableBlock = bot.findBlock({matching: mcData.blocksByName.crafting_table.id, maxDistance: 32,});
        }
        await bot.pathfinder.goto(new GoalLookAtBlock(craftingTableBlock.position, bot.world));
        // craft item
        const recipe = bot.recipesFor(item_by_name.id, null, 1, craftingTableBlock)[0];
        if (recipe) {
            try {
                await bot.craft(recipe, craft_times, craftingTableBlock);
                bot.chat(`I did the recipe for ${type} ${craft_times} times`);
            } catch (err) {
                bot.chat(`I cannot do the recipe for ${type} ${craft_times} times`);
            }
        } else {
            failedCraftFeedback(bot, type, item_by_name, craftingTableBlock);
            _craftItemFailCount++;
            if (_craftItemFailCount > 10) {
                throw new Error(
                    "craftItem failed too many times, check chat log to see what happened"
                );
            }
        }
    }
    let after_count = await getTotalCount(bot, type);
    let craft_count = after_count - original_count;
    if (craft_count >= count) {
        await bot.chat(`SUCCESS: ${craft_count} ${type} crafted.`);
        return true;
    } else {
        await bot.chat(`FAILED: only ${craft_count} ${type} crafted.`);
        return false;
    }
}

async function mineItem(bot, count = 1, type, explore_direction = new Vec3(1, 0, 1), explore_time = 300, recursive = true) {
    if (typeof type !== "string") {
        throw new Error(`type for mineBlock must be a string`);
    }
    if (typeof count !== "number") {
        throw new Error(`count for mineBlock must be a number`);
    }
    // let original_count = await getTotalCount(bot, type);
    if (recursive) {
        bot.chat(`Recursively executing mineItem(bot, ${count}, ${type})...`);
        // get tool_item from pre_tool.json
        let tool_item = await preTool(type);
        let check_tool = false;
        if (tool_item != "none") {
            if (tool_item.endsWith('_pickaxe')) {
                let level = tool_item.slice(0, -8); // extract the part before '_pickaxe'
                res = await equipPickaxeOfLevel(bot, level);
                check_tool = !res;
            } else if (tool_item === "axe" || tool_item === "pickaxe" || tool_item === "sword" || tool_item === "shovel" || tool_item === "hoe") {
                await equipBestTool(bot, tool_item);
            } else if (tool_item === "bucket" || tool_item === "shears") {
                check_tool = true;
            }
        }
        if (check_tool) {
            let tool = bot.inventory.findInventoryItem(mcData.itemsByName[tool_item].id);
                while (!tool) {
                    await craftItem(bot, 1, tool_item);
                    tool = bot.inventory.findInventoryItem(mcData.itemsByName[tool_item].id);
                }
                await bot.equip(tool, "hand");
        }
    }
    // todo: specify explore direction for all items
    if (type == "diamond") explore_direction = new Vec3(0, -1, 0); // dig down for diamond
    // find the block
    let name_list = await mapName(type);
    const blocks = await exploreUntil(bot, explore_direction, explore_time, () => {
        const blocks = bot.findBlocks({
            matching: block => name_list.includes(block.name),
            maxDistance: 32,
            count: count
        });
        return blocks.length >= 1 ? blocks : null;
    });
    if (!blocks) {
        bot.chat(`Could not find ${type}.`);
        return;
    }
    // todo: many-to-one like flint, one-to-many like redstone, not count-to-count
    const targets = [];
    for (let i = 0; i < blocks.length; i++) {
        targets.push(bot.blockAt(blocks[i]));
    }
    await bot.collectBlock.collect(targets, {
        ignoreNoPath: true,
        count: count,
    });

    let inv_count = await getTotalCount(bot, type);
    if (inv_count >= count) {
        await bot.chat(`SUCCESS: ${inv_count} ${type} in inventory.`);
        return true;
    } else {
        await bot.chat(`FAILED: only ${inv_count} ${type} in inventory.`);
        return false;
    }
}

async function smeltItem(bot, count = 1, type, fuel = "coal", recursive = true) {
    // todo: add fuel dynamically; other fuel: wooden material...
    if (typeof type !== "string" || typeof fuel !== "string") {
        throw new Error("type(item_name) or fuel_name for smeltItem must be a string");
    }
    if (typeof count !== "number") {
        throw new Error("count for smeltItem must be a number");
    }
    const type_in_mc = mcData.itemsByName[type];
    const fuel_in_mc = mcData.itemsByName[fuel];
    if (!type_in_mc) throw new Error(`No item named ${type}`);
    if (!fuel_in_mc) throw new Error(`No item named ${fuel}`);

    let original_count = await getTotalCount(bot, type);
    let smelt_item_str = await preSmelt(type);
    if (recursive) {
        bot.chat(`Recursively executing smeltItem(bot, ${count}, ${type})...`);
        // check fuel
        let fuel_item = bot.inventory.findInventoryItem(mcData.itemsByName[fuel].id);
        if (!fuel_item) {
            await obtainItem(bot, 1, fuel);
            fuel_item = bot.inventory.findInventoryItem(mcData.itemsByName[fuel].id);
        }
        // check pre_item
        let inv_count = await getTotalCount(bot, smelt_item_str);
        // bot.chat(`${smelt_item_str} inv_count=${inv_count}`);
        // if not enough
        if (inv_count < count) {
            await obtainItem(bot, count - inv_count, smelt_item_str);
        }
    }
    let furnaceBlock = bot.findBlock({matching: mcData.blocksByName.furnace.id, maxDistance: 32});
    if (!furnaceBlock) {
        if (recursive) {
            // check furnace
            let furnace_item = bot.inventory.findInventoryItem(mcData.itemsByName.furnace.id);
            if (!furnace_item) {
                await craftItem(bot, 1, "furnace");
            }
        } else {
            throw new Error("No furnace nearby");
        }
    }
    // place the furnace near the bot
    const furnacePosition = await findSuitablePosition(bot);
    await placeItem(bot, "furnace", furnacePosition);
    furnaceBlock = bot.findBlock({matching: mcData.blocksByName.furnace.id, maxDistance: 4});
    // bot.chat(`smelt_item=${smelt_item_str}, fuel_item=${fuel}`);
    
    const furnace = await bot.openFurnace(furnaceBlock);
    let item = mcData.itemsByName[smelt_item_str];
    let success_count = 0;
    for (let i = 0; i < count; i++) {
        if (!bot.inventory.findInventoryItem(item.id, null)) {
            bot.chat(`No ${type} to smelt in inventory`);
            break;
        }
        if (furnace.fuelSeconds < 15 && furnace.fuelItem()?.name !== fuel) {
            if (!bot.inventory.findInventoryItem(fuel_in_mc.id, null)) {
                bot.chat(`No ${fuel} as fuel in inventory`);
                break;
            }
            await furnace.putFuel(fuel_in_mc.id, null, 1);
            await bot.waitForTicks(20);
            if (!furnace.fuel && furnace.fuelItem()?.name !== fuel) {
                throw new Error(`${fuel} is not a valid fuel`);
            }
        }
        await furnace.putInput(item.id, null, 1);
        await bot.waitForTicks(12 * 20);
        if (!furnace.outputItem()) {
            throw new Error(`${type} is not a valid input`);
        }
        await furnace.takeOutput();
        success_count++;
    }
    furnace.close();
    if (success_count > 0) bot.chat(`Smelted ${success_count} ${type}.`);
    else {
        bot.chat(
            `Failed to smelt ${type}, please check the fuel and input.`
        );
        _smeltItemFailCount++;
        if (_smeltItemFailCount > 10) {
            throw new Error(
                `smeltItem failed too many times, please check the fuel and input.`
            );
        }
    }
    
    let after_count = await getTotalCount(bot, type);
    let smelt_count = after_count - original_count;
    if (smelt_count >= count) {
        await bot.chat(`SUCCESS: ${count} ${smelt_item_str} smelted into ${type}.`);
        return true;
    } else {
        await bot.chat(`FAILED: only ${count} ${smelt_item_str} smelted into ${type}.`);
        return false;
    }
}

async function placeItem(bot, name, position) {
    // return if name is not string
    if (typeof name !== "string") {
        throw new Error(`name for placeItem must be a string`);
    }
    // return if position is not Vec3
    if (!(position instanceof Vec3)) {
        throw new Error(`position for placeItem must be a Vec3`);
    }
    const itemByName = mcData.itemsByName[name];
    if (!itemByName) {
        throw new Error(`No item named ${name}`);
    }
    const item = bot.inventory.findInventoryItem(itemByName.id);
    if (!item) {
        bot.chat(`No ${name} in inventory`);
        return;
    }
    const item_count = item.count;
    // find a reference block
    const faceVectors = [
        new Vec3(0, 1, 0),
        new Vec3(0, -1, 0),
        new Vec3(1, 0, 0),
        new Vec3(-1, 0, 0),
        new Vec3(0, 0, 1),
        new Vec3(0, 0, -1),
    ];
    let referenceBlock = null;
    let faceVector = null;
    for (const vector of faceVectors) {
        const block = bot.blockAt(position.minus(vector));
        if (block?.name !== "air") {
            referenceBlock = block;
            faceVector = vector;
            bot.chat(`Placing ${name} on ${block.name} at ${block.position}`);
            break;
        }
    }
    if (!referenceBlock) {
        bot.chat(
            `No block to place ${name} on. You cannot place a floating block.`
        );
        _placeItemFailCount++;
        if (_placeItemFailCount > 10) {
            throw new Error(
                `placeItem failed too many times. You cannot place a floating block.`
            );
        }
        return;
    }

    // You must use try catch to placeBlock
    try {
        // You must first go to the block position you want to place
        await bot.pathfinder.goto(new GoalPlaceBlock(position, bot.world, {}));
        // You must equip the item right before calling placeBlock
        await bot.equip(item, "hand");
        await bot.placeBlock(referenceBlock, faceVector);
        bot.chat(`Placed ${name}`);
        bot.save(`${name}_placed`);
    } catch (err) {
        const item = bot.inventory.findInventoryItem(itemByName.id);
        if (item?.count === item_count) {
            bot.chat(
                `Error placing ${name}: ${err.message}, please find another position to place`
            );
            _placeItemFailCount++;
            if (_placeItemFailCount > 10) {
                throw new Error(
                    `placeItem failed too many times, please find another position to place.`
                );
            }
        } else {
            bot.chat(`Placed ${name}`);
            bot.save(`${name}_placed`);
        }
    }
}

// Explore downward for 60 seconds: exploreUntil(bot, new Vec3(0, -1, 0), 60);
async function exploreUntil(
    bot,
    direction,
    maxTime = 60,
    callback = () => {
        return false;
    }
) {
    if (typeof maxTime !== "number") {
        throw new Error("maxTime must be a number");
    }
    if (typeof callback !== "function") {
        throw new Error("callback must be a function");
    }
    const test = callback();
    if (test) {
        bot.chat("Explore success.");
        return Promise.resolve(test);
    }
    if (direction.x === 0 && direction.y === 0 && direction.z === 0) {
        throw new Error("direction cannot be 0, 0, 0");
    }
    if (
        !(
            (direction.x === 0 || direction.x === 1 || direction.x === -1) &&
            (direction.y === 0 || direction.y === 1 || direction.y === -1) &&
            (direction.z === 0 || direction.z === 1 || direction.z === -1)
        )
    ) {
        throw new Error(
            "direction must be a Vec3 only with value of -1, 0 or 1"
        );
    }
    maxTime = Math.min(maxTime, 1200);
    return new Promise((resolve, reject) => {
        const dx = direction.x;
        const dy = direction.y;
        const dz = direction.z;

        let explorationInterval;
        let maxTimeTimeout;

        const cleanUp = () => {
            clearInterval(explorationInterval);
            clearTimeout(maxTimeTimeout);
            bot.pathfinder.setGoal(null);
        };

        const explore = () => {
            const x =
                bot.entity.position.x +
                Math.floor(Math.random() * 20 + 10) * dx;
            const y =
                bot.entity.position.y +
                Math.floor(Math.random() * 20 + 10) * dy;
            const z =
                bot.entity.position.z +
                Math.floor(Math.random() * 20 + 10) * dz;
            let goal = new GoalNear(x, y, z);
            if (dy === 0) {
                goal = new GoalNearXZ(x, z);
            }
            bot.pathfinder.setGoal(goal);

            try {
                const result = callback();
                if (result) {
                    cleanUp();
                    bot.chat("Explore success.");
                    resolve(result);
                }
            } catch (err) {
                cleanUp();
                reject(err);
            }
        };

        explorationInterval = setInterval(explore, 2000);

        maxTimeTimeout = setTimeout(() => {
            cleanUp();
            bot.chat("Max exploration time reached");
            resolve(null);
        }, maxTime * 1000);
    });
}

function failedCraftFeedback(bot, name, item, craftingTable) {
    const recipes = bot.recipesAll(item.id, null, craftingTable);
    if (!recipes.length) {
        throw new Error(`No crafting table nearby`);
    } else {
        const recipes = bot.recipesAll(
            item.id,
            null,
            mcData.blocksByName.crafting_table.id
        );
        // find the recipe with the fewest missing ingredients
        var min = 999;
        var min_recipe = null;
        for (const recipe of recipes) {
            const delta = recipe.delta;
            var missing = 0;
            for (const delta_item of delta) {
                if (delta_item.count < 0) {
                    const inventory_item = bot.inventory.findInventoryItem(
                        mcData.items[delta_item.id].name,
                        null
                    );
                    if (!inventory_item) {
                        missing += -delta_item.count;
                    } else {
                        missing += Math.max(
                            -delta_item.count - inventory_item.count,
                            0
                        );
                    }
                }
            }
            if (missing < min) {
                min = missing;
                min_recipe = recipe;
            }
        }
        const delta = min_recipe.delta;
        let message = "";
        for (const delta_item of delta) {
            if (delta_item.count < 0) {
                const inventory_item = bot.inventory.findInventoryItem(
                    mcData.items[delta_item.id].name,
                    null
                );
                if (!inventory_item) {
                    message += ` ${-delta_item.count} more ${
                        mcData.items[delta_item.id].name
                    }, `;
                } else {
                    if (inventory_item.count < -delta_item.count) {
                        message += `${
                            -delta_item.count - inventory_item.count
                        } more ${mcData.items[delta_item.id].name}`;
                    }
                }
            }
        }
        bot.chat(`I cannot make ${name} because I need: ${message}`);
    }
}
