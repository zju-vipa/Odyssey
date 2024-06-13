async function makeCookies(bot) {
    let wheatCount = bot.inventory.count(mcData.itemsByName.wheat.id);
    let cocoaPodsCount = bot.inventory.count(mcData.itemsByName.cocoa_beans.id);
    if (wheatCount < 2) {
        bot.chat("Not enough wheat in inventory! plant and collect wheat first!");
        return;
    }
    if (!cocoaPodsCount) {
        bot.chat("Not enough cocoa beans in inventory! collect some first!");
        return;
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
  
    // Make cookies using the crafting table
    await craftItem(bot, "cookie", 1);
    bot.chat("Made cookies.");
}