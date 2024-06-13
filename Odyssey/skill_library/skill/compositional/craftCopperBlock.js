async function craftCopperBlock(bot) {
    // Smelt all raw copper first
    await smeltAllRawCopper(bot);
    // Check if there are enough copper ingots in the inventory
    let copperIngotsCount = bot.inventory.count(mcData.itemsByName.copper_ingot.id);
    // If not enough copper ingots, mine copper ores and smelt them into copper ingots
    while (copperIngotsCount < 9) {
      await mineCopperOre(bot);
      copperIngotsCount += 1;
    }
    await smeltAllRawCopper(bot);
    // Check if crafting table is in the inventory
    const craftingTableCount = bot.inventory.count(mcData.itemsByName.crafting_table.id);
    // If not, craft a crafting table
    if (craftingTableCount === 0) {
      await craftCraftingTable(bot);
    }
    // Place the crafting table near the bot
    const craftingTablePosition = await findSuitablePosition(bot);
    await placeItem(bot, "crafting_table", craftingTablePosition);
    // Craft a copper block using the crafting table
    await craftItem(bot, "copper_block", 1);
    bot.chat("Crafted a copper block.");
}