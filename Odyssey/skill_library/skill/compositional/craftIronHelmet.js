async function craftIronHelmet(bot) {
  // Smelt all raw iron first
  console.log('Craft Iron Helmet: start to smelt all raw iron');
  await smeltAllRawIron(bot);
  console.log('Craft Iron Helmet: smelt all raw iron done');
  // Check if there are enough iron ingots in the inventory
  let ironIngotsCount = bot.inventory.count(mcData.itemsByName.iron_ingot.id);
  // If not enough iron ingots, mine iron ores and smelt them into iron ingots
  while (ironIngotsCount < 5) {
    console.log("Craft Iron Helmet: Not enough iron ingots. Mining an iron ore...");
    await mineIronOre(bot);
    ironIngotsCount += 1;
  }
  console.log('Craft Iron Helmet: start to smelt all raw iron again');
  await smeltAllRawIron(bot);
  console.log('Craft Iron Helmet: smelt all raw iron done again');
  // Check if crafting table is in the inventory
  const craftingTableCount = bot.inventory.count(mcData.itemsByName.crafting_table.id);
  // If not, craft a crafting table
  if (craftingTableCount === 0) {
    console.log("Craft Iron Helmet: No crafting table in inventory. Crafting a crafting table...");
    await craftCraftingTable(bot);
  }
  // Place the crafting table near the bot
  console.log("Craft Iron Helmet: Looking for a suitable position to place the crafting table...");
  const craftingTablePosition = await findSuitablePosition(bot);
  console.log("Craft Iron Helmet: Placing the crafting table at position", craftingTablePosition);
  await placeItem(bot, "crafting_table", craftingTablePosition);
  // Craft an iron helmet using the crafting table
  await craftItem(bot, "iron_helmet", 1);
  bot.chat("Crafted an iron helmet.");
}