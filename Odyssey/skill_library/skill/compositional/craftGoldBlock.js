async function craftGoldBlock(bot) {
    // Smelt all raw gold first
    await smeltAllRawGold(bot);
    // Check if there are enough gold ingots in the inventory
    let goldIngotsCount = bot.inventory.count(mcData.itemsByName.gold_ingot.id);
    // If not enough gold ingots, mine gold ores and smelt them into gold ingots
    while (goldIngotsCount < 9) {
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
    // Craft a gold block using the crafting table
    await craftItem(bot, "gold_block", 1);
    bot.chat("Crafted a gold block.");
}