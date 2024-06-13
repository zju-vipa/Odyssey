async function craftHeavyWeightedPressurePlate(bot) {
    // Smelt all raw iron first
    await smeltAllRawIron(bot);
    // Check if there are enough iron ingots in the inventory
    let ironIngotsCount = bot.inventory.count(mcData.itemsByName.iron_ingot.id);
    // If not enough iron ingots, mine iron ores and smelt them into iron ingots
    while (ironIngotsCount < 2) {
      await mineIronOre(bot);
      ironIngotsCount += 1;
    }
    await smeltAllRawIron(bot);

    await craftItem(bot, "heavy_weighted_pressure_plate", 1);
    bot.chat("Crafted a heavy_weighted_pressure_plate.");
  }