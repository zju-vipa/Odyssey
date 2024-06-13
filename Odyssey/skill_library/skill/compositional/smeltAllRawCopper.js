async function smeltAllRawCopper(bot) {
  // Check if there is a furnace and some coals in the inventory
  const furnaceItem = bot.inventory.findInventoryItem(mcData.itemsByName.furnace.id);
  const coal = bot.inventory.findInventoryItem(mcData.itemsByName.coal.id);
  let rawCopperCount = bot.inventory.count(mcData.itemsByName.raw_copper.id)
  // check raw copper
  if (!rawCopperCount) {
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

  // Smelt all raw copper using the available coal as fuel
  await smeltItem(bot, "raw_copper", "coal", rawCopperCount);
  bot.chat("Raw copper smelted.");
}