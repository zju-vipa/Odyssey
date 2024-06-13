async function craftIronNugget(bot) {
    // Smelt all raw iron first
    await smeltAllRawIron(bot);
    // Check if there are enough iron ingots in the inventory
    let ironIngotsCount = bot.inventory.count(mcData.itemsByName.iron_ingot.id);
    // If not enough iron ingots, mine iron ores and smelt them into iron ingots
    if (ironIngotsCount < 1) {
      await mineIronOre(bot);
    }
    await smeltAllRawIron(bot);
    
    await craftItem(bot, "iron_nugget", 1);
    bot.chat("Crafted iron nuggets.");
  }