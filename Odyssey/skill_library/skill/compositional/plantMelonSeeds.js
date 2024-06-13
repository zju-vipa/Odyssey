async function plantMelonSeeds(bot) {
  // check seeds
  const seeds = bot.inventory.findInventoryItem(mcData.itemsByName.melon_seeds.id);
  if (!seeds) {
    bot.chat("No melon seeds found in inventory, collect melon seeds first!");
  }
  await plantSeeds(bot, "melon_seeds");
  return bot.entity.position;
}