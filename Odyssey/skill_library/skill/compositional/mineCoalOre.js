async function mineCoalOre(bot) {
  await equipPickaxe(bot);
  // Find coal_ore block
  const coalOres = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
    const coalOres = bot.findBlocks({
      matching: block => block.name === "coal_ore",
      maxDistance: 32,
      count: 1
    });
    return coalOres.length >= 1 ? coalOres : null;
  });
  if (!coalOres) {
    bot.chat("Could not find coal ore.");
    return;
  }
  // Mine the coal_ore block
  await mineBlock(bot, "coal_ore", 1);
  bot.chat("1 coal ore mined.");
}