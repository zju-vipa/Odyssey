async function collectCarrots(bot) {
    // Use the exploreUntil function to find carrots
    const carrots = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
    const carrots = bot.findBlocks({
        matching: block => block.name === "carrots" && block.getProperties().age === 7,
        maxDistance: 32,
        count: 1
    });
    return carrots.length >= 1 ? carrots : null;
    });
    if (!carrots) {
        bot.chat("Could not find enough carrots.");
        return;
    }
    const block = bot.blockAt(carrots[0]);
    await bot.pathfinder.goto(new GoalBlock(carrots[0].x, carrots[0].y, carrots[0].z));
    await bot.dig(block);
}