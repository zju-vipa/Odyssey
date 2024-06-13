async function collectPumpkin(bot) {
    await equipAxe(bot);
    // Use the exploreUntil function to find pumpkin blocks
    const pumpkinBlocks = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
      const pumpkinBlocks = bot.findBlocks({
        matching: block => block.name === "pumpkin",
        maxDistance: 32,
        count: 1
      });
      return pumpkinBlocks.length >= 1 ? pumpkinBlocks : null;
    });
    if (!pumpkinBlocks) {
      bot.chat("Could not find enough pumpkin.");
      return;
    }
    // Mine 1 pumpkin block using the mineBlock function
    await mineBlock(bot, "pumpkin", 1);
    bot.chat("1 pumpkin collected.");
  }