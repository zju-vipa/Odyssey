async function craftWoodenPlanks(bot) {
  const logNames = ["oak_log", "birch_log", "spruce_log", "jungle_log", "acacia_log", "dark_oak_log", "mangrove_log"];
  const plankNames = ["oak_planks", "birch_planks", "spruce_planks", "jungle_planks", "acacia_planks", "dark_oak_planks", "mangrove_planks"];
  let logInInventory = logNames.find(logName => bot.inventory.count(mcData.itemsByName[logName].id) > 0);
  console.log('Craft Wooden Planks, before Mine Wood Log bot inventory:', bot.inventory);
  if (!logInInventory) {
    bot.chat("No wooden log in inventory. Mining a wooden log...");
    await mineWoodLog(bot);
  }
  console.log('Craft Wooden Planks, after Mine Wood Log, bot inventory:', bot.inventory);
  logInInventory = logNames.find(logName => bot.inventory.count(mcData.itemsByName[logName].id) > 0);
  const logIndex = logNames.indexOf(logInInventory);
  const plankName = plankNames[logIndex];
  bot.chat(`Crafting 4 ${plankName}...`);
  await craftItem(bot, plankName, 1);
  bot.chat(`4 ${plankName} crafted.`);
}