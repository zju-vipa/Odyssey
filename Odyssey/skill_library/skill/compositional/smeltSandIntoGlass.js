async function smeltSandIntoGlass(bot) {
    // Check if there is a furnace in the inventory
    const furnaceItem = bot.inventory.findInventoryItem(mcData.itemsByName.furnace.id);
    let sandCount = bot.inventory.count(mcData.itemsByName.sand.id)
    const coal = bot.inventory.findInventoryItem(mcData.itemsByName.coal.id)
    // If not, craft a furnace using the available cobblestone
    if (!furnaceItem) {
      await craftFurnace(bot);
    }
    // If not enough sand, collect some
    if (sandCount < 5) {
      await collectSand(bot);
    }
    // If not enough coal, collect some
    if (!coal) {
      await mineCoalOre(bot);
    }
    // Find a suitable position to place the furnace
    const furnacePosition = await findSuitablePosition(bot);
    if (!furnacePosition) {
      bot.chat("Could not find a suitable position to place the furnace.");
      return;
    }
  
    // Place the furnace at the suitable position
    await placeItem(bot, "furnace", furnacePosition);
  
    // Smelt sand using the available coal as fuel
    sandCount = bot.inventory.count(mcData.itemsByName.sand.id)
    await smeltItem(bot, "sand", "coal", sandCount);
    bot.chat("Smelted sand into glass.");
  }