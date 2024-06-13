async function craftShears(bot) {
    // Check iron ingots
    let ironIngotsCount = bot.inventory.count(mcData.itemsByName.iron_ingot.id);
    // If not enough iron ingots, collect the required items.
    if (ironIngotsCount < 2) {
      await mineFiveIronOres(bot);
      bot.chat("Collected iron ores.");
      await smeltAllRawIron(bot);
      bot.chat("Smelted iron ores into iron ingots.");
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
    // Craft a pair of shears using the crafting table
    await craftItem(bot, "shears", 1);
    bot.chat("Crafted a pair of shears.");
  }