async function collectPotatoes(bot) {
    // Use the exploreUntil function to find potatoes
    const potatoes = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
    const potatoes = bot.findBlocks({
        matching: block => block.name === "potatoes" && block.getProperties().age === 7,
        maxDistance: 32,
        count: 1
    });
    return potatoes.length >= 1 ? potatoes : null;
    });
    if (!potatoes) {
        bot.chat("Could not find enough potatoes.");
        return;
    }
    const block = bot.blockAt(potatoes[0]);
    await bot.pathfinder.goto(new GoalBlock(potatoes[0].x, potatoes[0].y, potatoes[0].z));
    await bot.dig(block);
  }