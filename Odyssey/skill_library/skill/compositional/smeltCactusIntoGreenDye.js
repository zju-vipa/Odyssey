async function smeltCactusIntoGreenDye(bot) {
    // Check if there is a furnace in the inventory
    const furnaceItem = bot.inventory.findInventoryItem(mcData.itemsByName.furnace.id);
    const cactusCount = bot.inventory.count(mcData.itemsByName.cactus.id)
    const coal = bot.inventory.findInventoryItem(mcData.itemsByName.coal.id)
    // If not, craft a furnace using the available cobblestone
    if (!furnaceItem) {
      await craftFurnace(bot);
    }
    // If not enough cactus, collect some
    if (cactusCount < 5) {
      await collectFiveCactusBlocks(bot);
    }
    // If not enough coal, collect some
    if (!coal) {
      await mineFiveCoalOres(bot);
    }
    // Find a suitable position to place the furnace
    const furnacePosition = await findSuitablePosition(bot);
    if (!furnacePosition) {
      bot.chat("Could not find a suitable position to place the furnace.");
      return;
    }
  
    // Place the furnace at the suitable position
    await placeItem(bot, "furnace", furnacePosition);
  
    // Smelt cactus using the available coal as fuel
    await smeltItem(bot, "cactus", "coal", cactusCount);
    bot.chat("Smelted cactus into green dye.");
  }