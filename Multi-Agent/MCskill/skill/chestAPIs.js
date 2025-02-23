async function getItemFromChest(bot, chest_position, items_to_get) {
    if (!(chest_position instanceof Vec3)) {
        // find the nearest chest
        const directions = [
            new Vec3(1, 0, 0),   // East
            new Vec3(-1, 0, 0),  // West
            new Vec3(0, 0, 1),   // North
            new Vec3(0, 0, -1),  // South
            new Vec3(1, 0, 1),   // Northeast
            new Vec3(-1, 0, -1), // Southwest
            new Vec3(1, 0, -1),  // Southeast
            new Vec3(-1, 0, 1)   // Northwest
        ];
        // randomly pick a direction from the list
        explore_direction = directions[Math.floor(Math.random() * directions.length)];
        explore_time = 300;
        const chest_block = await exploreUntil(bot, explore_direction, explore_time, () => {
            const chest_block = bot.findBlocks({
                matching: block => block.name == "chest",
                maxDistance: 32,
                count: 1
            });
            return chest_block.length >= 1 ? chest_block : null;
        });
        if (!chest_block) {
            bot.chat(`Could not find the chest.`);
            return;
        } else {
            chest_position = chest_block[0];
            // bot.chat(`${JSON.stringify(chest_position)}`);
        }
    }
    await moveToChest(bot, chest_position);
    const chestBlock = bot.blockAt(chest_position);
    const chest = await bot.openContainer(chestBlock);
    for (const name in items_to_get) {
        const itemByName = mcData.itemsByName[name];
        if (!itemByName) {
            bot.chat(`No item named ${name}`);
            continue;
        }

        const item = chest.findContainerItem(itemByName.id);
        if (!item) {
            bot.chat(`I don't see ${name} in this chest`);
            continue;
        }
        try {
            await chest.withdraw(item.type, null, items_to_get[name]);
        } catch (err) {
            bot.chat(`Not enough ${name} in chest.`);
        }
    }
    await closeChest(bot, chestBlock);
}

async function depositItemIntoChest(bot, chest_position, items_to_deposit) {
    if (!(chest_position instanceof Vec3)) {
        // find the nearest chest
        const directions = [
            new Vec3(1, 0, 0),   // East
            new Vec3(-1, 0, 0),  // West
            new Vec3(0, 0, 1),   // North
            new Vec3(0, 0, -1),  // South
            new Vec3(1, 0, 1),   // Northeast
            new Vec3(-1, 0, -1), // Southwest
            new Vec3(1, 0, -1),  // Southeast
            new Vec3(-1, 0, 1)   // Northwest
        ];
        // randomly pick a direction from the list
        explore_direction = directions[Math.floor(Math.random() * directions.length)];
        explore_time = 300;
        const chest_block = await exploreUntil(bot, explore_direction, explore_time, () => {
            const chest_block = bot.findBlocks({
                matching: block => block.name == "chest",
                maxDistance: 32,
                count: 1
            });
            return chest_block.length >= 1 ? chest_block : null;
        });
        if (!chest_block) {
            bot.chat(`Could not find the chest.`);
            return;
        } else {
            chest_position = chest_block[0];
            // bot.chat(`${JSON.stringify(chest_position)}`);
        }
    }
    await moveToChest(bot, chest_position);
    const chestBlock = bot.blockAt(chest_position);
    const chest = await bot.openContainer(chestBlock);
    for (const name in items_to_deposit) {
        const itemByName = mcData.itemsByName[name];
        if (!itemByName) {
            bot.chat(`No item named ${name}`);
            continue;
        }
        const item = bot.inventory.findInventoryItem(itemByName.id);
        if (!item) {
            bot.chat(`No ${name} in inventory`);
            continue;
        }
        try {
            await chest.deposit(item.type, null, items_to_deposit[name]);
        } catch (err) {
            bot.chat(`Not enough ${name} in inventory.`);
        }
    }
    await closeChest(bot, chestBlock);
}

async function checkItemInsideChest(bot, chest_position) {
    // return if chest_position is not Vec3
    if (!(chest_position instanceof Vec3)) {
        throw new Error(
            "chest_position for checkItemInsideChest must be a Vec3"
        );
    }
    await moveToChest(bot, chest_position);
    const chestBlock = bot.blockAt(chest_position);
    await bot.openContainer(chestBlock);
    await closeChest(bot, chestBlock);
}

async function moveToChest(bot, chest_position) {
    if (!(chest_position instanceof Vec3)) {
        throw new Error(
            "chest_position for moveToChest must be a Vec3"
        );
    }
    if (chest_position.distanceTo(bot.entity.position) > 32) {
        bot.chat(
            `/tp ${chest_position.x} ${chest_position.y} ${chest_position.z}`
        );
        await bot.waitForTicks(20);
    }
    const chestBlock = bot.blockAt(chest_position);
    if (chestBlock.name !== "chest") {
        bot.emit("removeChest", chest_position);
        throw new Error(
            `No chest at ${chest_position}, it is ${chestBlock.name}`
        );
    }
    await bot.pathfinder.goto(
        new GoalLookAtBlock(chestBlock.position, bot.world, {})
    );
    return chestBlock;
}

async function listItemsInChest(bot, chestBlock) {
    const chest = await bot.openContainer(chestBlock);
    const items = chest.containerItems();
    if (items.length > 0) {
        const itemNames = items.reduce((acc, obj) => {
            if (acc[obj.name]) {
                acc[obj.name] += obj.count;
            } else {
                acc[obj.name] = obj.count;
            }
            return acc;
        }, {});
        bot.emit("closeChest", itemNames, chestBlock.position);
    } else {
        bot.emit("closeChest", {}, chestBlock.position);
    }
    return chest;
}

async function closeChest(bot, chestBlock) {
    try {
        const chest = await listItemsInChest(bot, chestBlock);
        await chest.close();
    } catch (err) {
        await bot.closeWindow(chestBlock);
    }
}

function itemByName(items, name) {
    for (let i = 0; i < items.length; ++i) {
        const item = items[i];
        if (item && item.name === name) return item;
    }
    return null;
}

async function goto(bot, position) {
    await bot.pathfinder.goto(position);
}