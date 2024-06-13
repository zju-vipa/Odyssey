async function placeChest(bot) {
    // Check chest
    const chest = bot.inventory.findInventoryItem(mcData.itemsByName.chest.id);
    if (!chest) {
        await craftChest(bot);
    }
    // Place the chest
    const chestPosition = await findSuitablePosition(bot);
    await placeItem(bot, "chest", chestPosition);
    return chestPosition;
}