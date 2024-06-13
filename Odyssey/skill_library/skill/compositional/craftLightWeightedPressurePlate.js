async function craftLightWeightedPressurePlate(bot) {
    // Smelt all raw gold first
    await smeltAllRawGold(bot);
    // Check if there are enough gold ingots in the inventory
    let goldIngotsCount = bot.inventory.count(mcData.itemsByName.gold_ingot.id);
    // If not enough gold ingots, mine gold ores and smelt them into gold ingots
    while (goldIngotsCount < 2) {
      await mineGoldOre(bot);
      goldIngotsCount += 1;
    }
    await smeltAllRawgold(bot);

    await craftItem(bot, "light_weighted_pressure_plate", 1);
    bot.chat("Crafted a light_weighted_pressure_plate.");
  }