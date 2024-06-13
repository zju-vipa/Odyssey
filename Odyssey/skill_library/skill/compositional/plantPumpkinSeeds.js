async function plantPumpkinSeeds(bot) {
  // check seeds
  const seeds = bot.inventory.findInventoryItem(mcData.itemsByName.pumpkin_seeds.id);
  if (!seeds) {
    await bot.chat("No pumpkin seeds found in inventory, collect pumpkin seeds first!");
  }
  await plantSeeds(bot, "pumpkin_seeds");
  return bot.entity.position;
}