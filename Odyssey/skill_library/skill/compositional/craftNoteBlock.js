async function craftNoteBlock(bot) {
    const redstoneCount = bot.inventory.count(mcData.itemsByName.redstone.id);
    let totalPlanksCount = await getPlanksCount(bot);
    while (totalPlanksCount < 8) {
      await craftWoodenPlanks(bot);
    }
    if (redstoneCount < 1) {
        await mineRedstoneOre(bot);
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
  
    // Craft a note block using the crafting table
    await craftItem(bot, "note_block", 1);
    bot.chat("Crafted a note block.");
  }