async function craftClock(bot) {
    // Smelt all raw gold first
    await smeltAllRawGold(bot);
    // Check if there are enough gold ingots and redstone in the inventory
    let goldIngotsCount = bot.inventory.count(mcData.itemsByName.gold_ingot.id);
    let redstoneCount = bot.inventory.count(mcData.itemsByName.redstone.id);
    // If not enough gold ingots, mine gold ores and smelt them into gold ingots
    while (goldIngotsCount < 4) {
      await mineGoldOre(bot);
      goldIngotsCount += 1;
    }
    await smeltAllRawgold(bot);
    // If not enough redstone, mine 1
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
    // Craft a clock using the crafting table
    await craftItem(bot, "clock", 1);
    bot.chat("Crafted a clock.");
}