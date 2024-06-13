async function craftGoldenHelmet(bot) {
    // Smelt all raw gold first
    await smeltAllRawGold(bot);
    // Check if there are enough gold ingots in the inventory
    const goldIngotsCount = bot.inventory.count(mcData.itemsByName.gold_ingot.id);
    // If not enough gold ingots, collect the required items.
    if (goldIngotsCount < 5) {
      await mineGoldOre(bot);
      goldIngotsCount += 1;
    }
    await smeltAllRawgold(bot);
    // Check if crafting table is in the inventory
    const craftingTableCount = bot.inventory.count(mcData.itemsByName.crafting_table.id);
    // If not, craft a crafting table
    if (craftingTableCount === 0) {
      await craftCraftingTable(bot);
    }
    // Place the crafting table near the bot
    const craftingTablePosition = await findSuitablePosition(bot);
    await placeItem(bot, "crafting_table", craftingTablePosition);
    // Craft a golden helmet using the crafting table
    await craftItem(bot, "golden_helmet", 1);
    bot.chat("Crafted a golden helmet.");
  }