async function craftIronTrapdoor(bot) {
    // Smelt all raw iron first
    await smeltAllRawIron(bot);
    // Check if there are enough iron ingots in the inventory
    let ironIngotsCount = bot.inventory.count(mcData.itemsByName.iron_ingot.id);
    // If not enough iron ingots, mine iron ores and smelt them into iron ingots
    while (ironIngotsCount < 4) {
      await mineIronOre(bot);
      ironIngotsCount += 1;
    }
    await smeltAllRawIron(bot);

    await craftItem(bot, "iron_trapdoor", 1);
    bot.chat("Crafted an iron trapdoor.");
  }