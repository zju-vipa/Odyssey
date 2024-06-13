async function craftRawGoldBlock(bot) {
    // Check if there are enough raw gold in the inventory
    let rawGoldCount = bot.inventory.count(mcData.itemsByName.raw_gold.id);
    // If not enough raw gold, mine gold ores and smelt them into raw gold
    while (rawGoldCount < 9) {
      await mineGoldOre(bot);
      rawGoldCount = bot.inventory.count(mcData.itemsByName.raw_gold.id);
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
    // Craft a raw gold block using the crafting table
    await craftItem(bot, "raw_gold_block", 1);
    bot.chat("Crafted a raw gold block.");
}