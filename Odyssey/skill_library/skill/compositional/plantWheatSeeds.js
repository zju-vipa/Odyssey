async function plantWheatSeeds(bot) {
  // check seeds
  const seeds = bot.inventory.findInventoryItem(mcData.itemsByName.wheat_seeds.id);
  if (!seeds) {
    // await bot.chat("No wheat seeds found in inventory, collect wheat seeds first!");
    await collectWheatSeeds(bot);
  }
  await plantSeeds(bot, "wheat_seeds");
  return bot.entity.position;
}