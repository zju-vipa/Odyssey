async function craftDiamondBoots(bot) {
    // Check if there are enough diamond in the inventory
    let diamondsCount = bot.inventory.count(mcData.itemsByName.diamond.id);
  
    // If not enough diamonds, collect some
    while (diamondsCount < 4) {
      await mineDiamond(bot);
      diamondsCount = bot.inventory.count(mcData.itemsByName.diamond.id);
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
  
    // Craft diamond boots using the crafting table
    await craftItem(bot, "diamond_boots", 1);
    bot.chat("Crafted diamond boots.");
  }