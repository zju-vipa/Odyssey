async function craftCraftingTable(bot) {
  // check log or planks
  const logNames = ["oak_log", "birch_log", "spruce_log", "jungle_log", "acacia_log", "dark_oak_log", "mangrove_log"];
  const planksCount = await getPlanksCount(bot);
  if (planksCount >= 4) {
    // Craft a crafting table using planks
    await craftItem(bot, "crafting_table", 1);
    bot.chat("Crafted a crafting table.");
  }
  // If no enough planks
  const logInInventory = logNames.find(logName => bot.inventory.count(mcData.itemsByName[logName].id) > 0);
  // If no logs, mine logs first
  if (!logInInventory) {
    bot.chat("No wooden log in inventory. Mining a wooden log...");
    await mineWoodLog(bot);
    await craftWoodenPlanks(bot);
  }

  // Craft a crafting table using planks
  await craftItem(bot, "crafting_table", 1);
  bot.chat("Crafted a crafting table.");
}