async function smeltFiveRawIron(bot) {
  // Check if there is a furnace and some coals in the inventory
  const furnaceItem = bot.inventory.findInventoryItem(mcData.itemsByName.furnace.id);
  const coal = bot.inventory.findInventoryItem(mcData.itemsByName.coal.id);
  // If not, craft a furnace using the available cobblestone
  if (!furnaceItem) {
    await craftFurnace(bot);
  }

  // Place the furnace near the bot
  const furnacePosition = await findSuitablePosition(bot);
  await placeItem(bot, "furnace", furnacePosition);
  if (!coal)
    await mineFiveCoalOres(bot);
  // Smelt 5 raw iron using the available coal as fuel
  await smeltItem(bot, "raw_iron", "coal", 5);
  bot.chat("5 raw iron smelted.");
}