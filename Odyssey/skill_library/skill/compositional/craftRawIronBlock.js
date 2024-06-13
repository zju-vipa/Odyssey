async function craftRawIronBlock(bot) {
    // Check if there are enough raw iron in the inventory
    let rawIronCount = bot.inventory.count(mcData.itemsByName.raw_iron.id);
    // If not enough raw iron, mine iron ores and smelt them into raw iron
    while (rawIronCount < 9) {
      await mineIronOre(bot);
      rawIronCount = bot.inventory.count(mcData.itemsByName.raw_iron.id);
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
    // Craft a raw iron block using the crafting table
    await craftItem(bot, "raw_iron_block", 1);
    bot.chat("Crafted a raw iron block.");
}