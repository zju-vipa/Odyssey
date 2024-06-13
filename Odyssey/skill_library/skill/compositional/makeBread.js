async function makeBread(bot) {
    let wheatCount = bot.inventory.count(mcData.itemsByName.wheat.id);
    if (wheatCount < 3) {
        bot.chat("Not enough wheat in inventory! plant and collect wheat first!");
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
  
    // Make a bread using the crafting table
    await craftItem(bot, "bread", 1);
    bot.chat("Made a bread.");
}