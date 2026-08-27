async function craftCraftingTable(bot) {
  const logNames = ["oak_log", "birch_log", "spruce_log", "jungle_log", "acacia_log", "dark_oak_log", "mangrove_log"];
  let planksCount = await getPlanksCount(bot);

  if (planksCount < 4) {
    const logInInventory = logNames.find(
      logName => bot.inventory.count(mcData.itemsByName[logName].id) > 0
    );
    if (!logInInventory) {
      bot.chat("No wooden log in inventory. Mining a wooden log...");
      await mineWoodLog(bot);
    }
    await craftWoodenPlanks(bot);
    planksCount = await getPlanksCount(bot);
  }

  if (planksCount < 4) {
    throw new Error("Not enough wooden planks to craft a crafting table");
  }

  await craftItem(bot, "crafting_table", 1);
  bot.chat("Crafted a crafting table.");
}
