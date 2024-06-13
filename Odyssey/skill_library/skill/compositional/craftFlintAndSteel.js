async function craftFlintAndSteel(bot) {
    
    // Check if there are enough flints and iron_ingots in the inventory
    let ironIngotsCount = bot.inventory.count(mcData.itemsByName.iron_ingot.id);
    let flintsCount = bot.inventory.count(mcData.itemsByName.flint.id);
    await smeltAllRawIron(bot);
    // If not, explore to find and mine iron ores
    if (ironIngotsCount < 1) {
      await mineIronOre(bot);
      await smeltAllRawIron(bot);
    }
    if (flintsCount < 1) {
        await mineFlint(bot);
        flintsCount += 1;
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
  
    // Craft a flint_and_steel using the crafting table
    await craftItem(bot, "flint_and_steel", 1);
    bot.chat("Crafted a flint_and_steel.");
  }