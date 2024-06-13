async function craftRails(bot) {
    await smeltAllRawIron(bot);
    // Check iron ingots and sticks
    let ironIngotsCount = bot.inventory.count(mcData.itemsByName.iron_ingot.id);
    let sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);
    // If not enough iron ingots, collect the required items.
    do {
      ironIngotsCount = bot.inventory.count(mcData.itemsByName.iron_ingot.id);
      if (ironIngotsCount >= 6)
       break;
      await mineFiveIronOres(bot);
      bot.chat("Collected iron ores.");
      await smeltAllRawIron(bot);
      bot.chat("Smelted iron ores into iron ingots.");
    } while (ironIngotsCount < 6)
    // If not enough sticks, craft some
    if (!sticksCount) {
        craftSticks(bot);
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
    // Craft rails using the crafting table
    await craftItem(bot, "rail", 1);
    bot.chat("Crafted rails.");
  }