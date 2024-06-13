async function craftScaffolding(bot) {
    // Check if there are enough bamboos and strings in the inventory
    let bamboosCount = bot.inventory.count(mcData.itemsByName.bamboo.id);
    let stringsCount = bot.inventory.count(mcData.itemsByName.string.id);
    if (bamboosCount < 6) {
      await collectBamboo(bot);
    }
    if (stringsCount < 1) {
        await bot.chat("Not enough strings in inventory, try killing some spiders first!");
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
  
    // Craft a scaffolding using the crafting table
    await craftItem(bot, "scaffolding", 1);
    bot.chat("Crafted a scaffolding.");
  }