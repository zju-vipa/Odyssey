async function collectBeetroots(bot) {
    // Use the exploreUntil function to find beetroots
    const beetroots = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
    const beetroots = bot.findBlocks({
        matching: block => block.name === "beetroots" && block.getProperties().age === 3,
        maxDistance: 32,
        count: 1
    });
    return beetroots.length >= 1 ? beetroots : null;
    });
    if (!beetroots) {
        bot.chat("Could not find enough beetroots.");
        return;
    }
    const block = bot.blockAt(beetroots[0]);
    await bot.pathfinder.goto(new GoalBlock(beetroots[0].x, beetroots[0].y, beetroots[0].z));
    await bot.dig(block);
}