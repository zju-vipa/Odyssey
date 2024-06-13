async function craftGoldenShovel(bot) {
    // Smelt all raw gold first
    await smeltAllRawGold(bot);
    // Check if there are enough gold ingots and sticks in the inventory
    const goldIngotsCount = bot.inventory.count(mcData.itemsByName.gold_ingot.id);
    const sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);
    // If not enough gold ingots or sticks, collect the required items.
    if (goldIngotsCount < 1) {
      await mineGoldOre(bot);
      goldIngotsCount += 1;
    }
    await smeltAllRawgold(bot);
    if (sticksCount < 2) {
      await craftSticks(bot);
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
    // Craft a golden shovel using the crafting table
    await craftItem(bot, "golden_shovel", 1);
    bot.chat("Crafted a golden shovel.");
  }