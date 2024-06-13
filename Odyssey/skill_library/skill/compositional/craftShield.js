async function craftShield(bot) {
    // Check if there are enough planks and iron_ingots in the inventory
    let ironIngotsCount = bot.inventory.count(mcData.itemsByName.iron_ingot.id);
    let totalPlanksCount = await getPlanksCount(bot);
    // If not, craft some
    while (totalPlanksCount < 6) {
        await craftWoodenPlanks(bot);
        totalPlanksCount += 4;
    }
    // If not, explore to find and mine iron ores
    if (ironIngotsCount < 1) {
      await mineIronOre(bot);
      await smeltAllRawIron(bot);
      ironIngotsCount += 1;
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
  
    // Craft a shield using the crafting table
    await craftItem(bot, "shield", 1);
    bot.chat("Crafted a shield.");
  }