async function collectCocoaBeans(bot) {
  // Find bamboo plants using the exploreUntil function
  const cocoaPods = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
    const cocoaPods = bot.findBlocks({
      matching: block => block.name === "cocoa",
      maxDistance: 32,
      count: 1
    });
    return cocoaPods.length >= 1 ? cocoaPods : null;
  });
  // equip axe if there is one
  await equipAxe(bot);
  if (!cocoaPods) {
    bot.chat("Could not find cocoaPods.");
    return;
  }
  for (const cocoa of cocoaPods) {
    const block = bot.blockAt(cocoa);
    await bot.dig(block);
    await bot.pathfinder.goto(new GoalBlock(cocoa.x, cocoa.y, cocoa.z));
  }
  bot.chat("cocoa beans collected.")
}