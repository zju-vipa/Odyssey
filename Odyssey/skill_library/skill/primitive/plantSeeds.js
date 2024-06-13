async function plantSeeds(bot, type = null) {
    // check seeds
    const seeds = bot.inventory.findInventoryItem(mcData.itemsByName[type].id);
    await bot.equip(seeds, "hand");
    // find one farmland
    const farmland = bot.findBlocks({
        matching: block => block.name === "farmland",
        maxDistance: 32,
        count: 10
    });
    if (!farmland) {
        await bot.chat("No farmland nearby, return to my fields first!");
        return;
    }
    // plant seed
    for (const pos of farmland) {
        if (await checkBlockAbove(bot, "air", pos)) {
            const block = await bot.blockAt(pos);
            await bot.pathfinder.goto(new GoalBlock(pos.x, pos.y, pos.z));
            await bot.placeBlock(block, new Vec3(0, 1, 0));
        }
    }
}