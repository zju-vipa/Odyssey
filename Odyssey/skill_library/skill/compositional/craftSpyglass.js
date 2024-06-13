async function craftSpyglass(bot) {
    // Smelt all raw copper first
    await smeltAllRawCopper(bot);
    // Check if there are enough copper ingots and amethyst_shard in the inventory
    let copperIngotsCount = bot.inventory.count(mcData.itemsByName.copper_ingot.id);
    let amethystShardCount = bot.inventory.count(mcData.itemsByName.amethyst_shard.id);
    // If not enough copper ingots, mine copper ores and smelt them into copper ingots
    while (copperIngotsCount < 2) {
      await mineCopperOre(bot);
      copperIngotsCount += 1;
    }
    await smeltAllRawcopper(bot);
    // If not enough amethyst_shard, mine 1
    if (amethystShardCount < 1) {
        await mineAmethystCluster(bot);
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
    // Craft a spyglass using the crafting table
    await craftItem(bot, "spyglass", 1);
    bot.chat("Crafted a spyglass.");
}