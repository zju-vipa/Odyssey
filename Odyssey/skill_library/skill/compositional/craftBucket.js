async function craftBucket(bot) {
  // Check if there are enough iron ingots in the inventory
  const ironIngotsCount = bot.inventory.count(mcData.itemsByName.iron_ingot.id);

  // If not enough iron ingots, mine iron ores and smelt them into iron ingots
  if (ironIngotsCount < 3) {
    await mineFiveIronOres(bot);
    bot.chat("Collected iron ores.");
    await smeltFiveRawIron(bot);
    bot.chat("Smelted iron ores into iron ingots.");
  }
  // Check if crafting table is in the inventory
  const craftingTableCount = bot.inventory.count(mcData.itemsByName.crafting_table.id);
  // If not, craft a crafting table
  if (craftingTableCount === 0) {
    await craftCraftingTable(bot);
  }
  // Place the crafting table near the bot
  const craftingTablePosition = await findSuitablePosition(bot);
  await placeItem(bot, "crafting_table", craftingTablePosition);

  // Craft a bucket using the crafting table
  await craftItem(bot, "bucket", 1);
  bot.chat("Crafted a bucket.");
}