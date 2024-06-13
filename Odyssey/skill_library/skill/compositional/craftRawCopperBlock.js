async function craftRawCopperBlock(bot) {
    // Check if there are enough raw copper in the inventory
    let rawCopperCount = bot.inventory.count(mcData.itemsByName.raw_copper.id);
    // If not enough raw copper, mine copper ores and smelt them into raw copper
    while (rawCopperCount < 9) {
      await mineCopperOre(bot);
      rawCopperCount = bot.inventory.count(mcData.itemsByName.raw_copper.id);
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
    // Craft a raw copper block using the crafting table
    await craftItem(bot, "raw_copper_block", 1);
    bot.chat("Crafted a raw copper block.");
}