async function craftFishingRod(bot) {
    // Check if there are enough sticks and strings in the inventory
    let sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);
    let stringsCount = bot.inventory.count(mcData.itemsByName.string.id);
    if (sticksCount < 3) {
      await craftSticks(bot);
    }
    if (stringsCount < 2) {
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
  
    // Craft a fishing_rod using the crafting table
    await craftItem(bot, "fishing_rod", 1);
    bot.chat("Crafted a fishing rod.");
  }