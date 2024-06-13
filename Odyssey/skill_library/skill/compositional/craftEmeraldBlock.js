async function craftEmeraldBlock(bot) {
    // Check if there are enough emeralds in the inventory
    let emeraldsCount = bot.inventory.count(mcData.itemsByName.emerald.id);
    // If not enough emeralds, mine some
    while (emeraldsCount < 9) {
      await mineEmerald(bot);
      emeraldsCount = bot.inventory.count(mcData.itemsByName.emerald.id);
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
    // Craft an emerald block using the crafting table
    await craftItem(bot, "emerald_block", 1);
    bot.chat("Crafted an emerald block.");
}