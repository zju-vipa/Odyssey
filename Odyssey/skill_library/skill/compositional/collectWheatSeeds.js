async function collectWheatSeeds(bot) {
    // Check seeds
    let seedsCount = bot.inventory.count(mcData.itemsByName.wheat_seeds.id);
    let newSeedsCount = seedsCount;
    // Use the exploreUntil function to find grass
    do {
        const grasses = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
        const grasses = bot.findBlocks({
            matching: block => block.name === "grass",
            maxDistance: 32,
            count: 10
        });
        return grasses.length >= 10 ? grasses : null;
        });
        if (!grasses) {
            bot.chat("Could not find enough grass.");
            return;
        }
        // Mine 10 grass using the dig function (The mineBlock function is not applicable for collecting plants or crops)
        for (const grass of grasses) {
            const block = bot.blockAt(grass);
            await bot.pathfinder.goto(new GoalBlock(grass.x, grass.y, grass.z));
            await bot.dig(block);
            await bot.pathfinder.goto(new GoalBlock(grass.x, grass.y, grass.z));
        }
        // Check seeds
        newSeedsCount = bot.inventory.count(mcData.itemsByName.wheat_seeds.id);
    } while (newSeedsCount == seedsCount)
    await bot.chat(`${newSeedsCount-seedsCount} wheat seeds collected.`)
  }