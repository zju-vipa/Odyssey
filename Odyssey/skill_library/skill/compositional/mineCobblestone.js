async function mineCobblestone(bot) {
    await equipPickaxeOrCraftOne(bot);
    // Use the exploreUntil function to find cobblestone block
    const cobblestoneBlocks = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
      const cobblestoneBlocks = bot.findBlocks({
        matching: block => block.name === "stone",
        maxDistance: 32,
        count: 1
      });
      return cobblestoneBlocks.length >= 1 ? cobblestoneBlocks : null;
    });
    if (!cobblestoneBlocks) {
      bot.chat("Could not find stone.");
      return;
    }
    // Mine 1 cobblestone block using the mineBlock function
    await mineBlock(bot, "stone", 1);
    bot.chat(`1 cobblestone mined.`);
  }