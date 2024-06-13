async function collectSand(bot) {
  await equipShovelOrCraftOne(bot);
  // Use the exploreUntil function to find sand blocks
  const sandBlocks = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
    const sandBlocks = bot.findBlocks({
      matching: block => block.name === "sand",
      maxDistance: 32,
      count: 10
    });
    return sandBlocks.length >= 10 ? sandBlocks : null;
  });
  if (!sandBlocks) {
    bot.chat("Could not find enough sand.");
    return;
  }
  // Mine 10 sand blocks using the mineBlock function
  await mineBlock(bot, "sand", 10);
  bot.chat("10 sand mined.");
}