async function collectSandstone(bot) {
    await equipPickaxeOrCraftOne(bot);
    // Use the exploreUntil function to find sandstone blocks
    const sandstoneBlocks = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
      const sandstoneBlocks = bot.findBlocks({
        matching: block => block.name === "sandstone",
        maxDistance: 32,
        count: 10
      });
      return sandstoneBlocks.length >= 10 ? sandstoneBlocks : null;
    });
    if (!sandstoneBlocks) {
      bot.chat("Could not find enough stones.");
      return;
    }
    // Mine 10 sandstone blocks using the mineBlock function
    await mineBlock(bot, "sandstone", 10);
    bot.chat(`10 sandstones mined.`);
  }