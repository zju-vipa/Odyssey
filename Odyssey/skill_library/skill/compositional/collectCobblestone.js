async function collectCobblestone(bot) {
    await equipPickaxeOrCraftOne(bot);
    // Use the exploreUntil function to find cobblestone blocks
    const cobblestoneBlocks = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
      const cobblestoneBlocks = bot.findBlocks({
        matching: block => block.name === "stone",
        maxDistance: 32,
        count: 10
      });
      return cobblestoneBlocks.length >= 10 ? cobblestoneBlocks : null;
    });
    if (!cobblestoneBlocks) {
      bot.chat("Could not find enough stones.");
      return;
    }
    // Mine 10 cobblestone blocks using the mineBlock function
    await mineBlock(bot, "stone", 10);
    bot.chat(`10 cobblestones mined.`);
  }