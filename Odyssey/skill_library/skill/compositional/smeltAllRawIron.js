async function smeltAllRawIron(bot) {
  // Check if there is a furnace and some coals in the inventory
  const furnaceItem = bot.inventory.findInventoryItem(mcData.itemsByName.furnace.id);
  const coal = bot.inventory.findInventoryItem(mcData.itemsByName.coal.id);
  let rawIronCount = bot.inventory.count(mcData.itemsByName.raw_iron.id)
  // check raw iron
  if (!rawIronCount) {
    return;
  }
  if (!coal)
    await mineCoalOre(bot);
  // If not, craft a furnace using the available cobblestone
  if (!furnaceItem) {
    await craftFurnace(bot);
  }
  // Place the furnace near the bot
  const furnacePosition = await findSuitablePosition(bot);
  await placeItem(bot, "furnace", furnacePosition);
  
  // Smelt all raw iron using the available coal as fuel
  await smeltItem(bot, "raw_iron", "coal", rawIronCount);
  bot.chat("Raw iron smelted.");
}