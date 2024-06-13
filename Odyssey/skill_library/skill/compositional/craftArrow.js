async function craftArrow(bot) {
    // Check if there are enough feather, flint and stick in the inventory
    let feathersCount = bot.inventory.count(mcData.itemsByName.feather.id);
    let flintsCount = bot.inventory.count(mcData.itemsByName.flint.id);
    let sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);

    if (flintsCount < 1) {
        await mineFlint(bot);
    }
    if (sticksCount < 1) {
        await craftSticks(bot);
    }
    while (feathersCount < 1) {
        await killOneChicken(bot);
        feathersCount = bot.inventory.count(mcData.itemsByName.feather.id);
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
  
    // Craft an arrow using the crafting table
    await craftItem(bot, "arrow", 1);
    bot.chat("Crafted an arrow.");
}