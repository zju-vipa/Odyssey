async function collectMelon(bot) {
    await equipAxe(bot);
    // Use the exploreUntil function to find melon blocks
    const melonBlocks = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
      const melonBlocks = bot.findBlocks({
        matching: block => block.name === "melon",
        maxDistance: 32,
        count: 1
      });
      return melonBlocks.length >= 1 ? melonBlocks : null;
    });
    if (!melonBlocks) {
      bot.chat("Could not find enough melon.");
      return;
    }
    // Mine 1 melon block using the mineBlock function
    await mineBlock(bot, "melon", 1);
    bot.chat("1 melon collected.");
  }