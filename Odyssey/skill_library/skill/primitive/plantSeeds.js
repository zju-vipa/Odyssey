async function plantSeeds(bot, type = null) {
    const seedType = mcData.itemsByName[type];
    if (!seedType) {
        bot.chat(`No item named ${type}.`);
        return 0;
    }
    const seeds = bot.inventory.findInventoryItem(seedType.id);
    if (!seeds) {
        bot.chat(`No ${type} found in inventory.`);
        return 0;
    }
    await bot.equip(seeds, "hand");
    const farmland = bot.findBlocks({
        matching: block => block.name === "farmland",
        maxDistance: 32,
        count: 10
    });
    if (!farmland || farmland.length === 0) {
        await bot.chat("No farmland nearby, return to my fields first!");
        return 0;
    }
    let plantedCount = 0;
    for (const pos of farmland) {
        if (await checkBlockAbove(bot, "air", pos)) {
            const block = await bot.blockAt(pos);
            await bot.pathfinder.goto(new GoalBlock(pos.x, pos.y, pos.z));
            await bot.placeBlock(block, new Vec3(0, 1, 0));
            plantedCount++;
        }
    }
    return plantedCount;
}
