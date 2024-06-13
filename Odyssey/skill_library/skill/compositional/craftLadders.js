async function craftLadders(bot) {
    // Check required items
    let sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);
    while (sticksCount < 7) {
        await craftSticks(bot);
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
    // Craft ladders using the crafting table
    await craftItem(bot, "ladder", 1);
    bot.chat("Crafted ladders.");
}