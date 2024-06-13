async function craftCampfire(bot) {
    // check required items
    let logsCount = await getLogsCount(bot);
    let sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);
    let coalCount = bot.inventory.count(mcData.itemsByName.coal.id);
    if (sticksCount < 3) {
        await craftSticks(bot);
    }
    while (logsCount < 3) {
        await mineWoodLog(bot);
    }
    if (coalCount < 1) {
        await mineCoalOre(bot);
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
    // Craft a campfire using the crafting table
    await craftItem(bot, "campfire", 1);
    bot.chat("Crafted a campfire.");
}