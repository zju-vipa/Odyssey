async function craftPiston(bot) {
    const redstoneCount = bot.inventory.count(mcData.itemsByName.redstone.id);
    const ironIngotCount = bot.inventory.count(mcData.itemsByName.iron_ingot.id);
    let cobblestoneCount = bot.inventory.count(mcData.itemsByName.cobblestone.id);
    let totalPlanksCount = await getPlanksCount(bot);
    if (redstoneCount < 1) {
        await mineRedstoneOre(bot);
    }
    if (ironIngotCount < 1) {
        await mineIronOre(bot);
        await smeltAllRawIron(bot);
    }
    while (cobblestoneCount < 4) {
        await mineCobblestone(bot);
        cobblestoneCount = bot.inventory.count(mcData.itemsByName.cobblestone.id);
    }
    if (totalPlanksCount < 3) {
        await craftWoodenPlanks(bot);
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
  
    // Craft a piston using the crafting table
    await craftItem(bot, "piston", 1);
    bot.chat("Crafted a piston.");
  }