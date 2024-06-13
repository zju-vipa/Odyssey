async function craftIronShovel(bot) {
  // Smelt all raw iron first
  await smeltAllRawIron(bot);
  // Check if there are enough iron ingots and sticks in the inventory
  let ironIngotsCount = bot.inventory.count(mcData.itemsByName.iron_ingot.id);
  const sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);
  // If not enough iron ingots or sticks, collect the required items.
  if (sticksCount < 2) {
    await craftSticks(bot);
  }
  if (ironIngotsCount < 1) {
    await mineIronOre(bot);
    await smeltAllRawIron(bot);
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
  // Craft an iron shovel using the crafting table
  await craftItem(bot, "iron_shovel", 1);
  bot.chat("Crafted an iron shovel.");
}