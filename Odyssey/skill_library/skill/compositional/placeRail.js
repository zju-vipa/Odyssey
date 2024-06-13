async function placeRail(bot) {
    // Check rail
    const rail = bot.inventory.findInventoryItem(mcData.itemsByName.rail.id);
    if (!rail) {
        bot.chat("No rail found in inventory.");
        return;
    }
    // Place the rail
    const railPosition = bot.entity.position;
    await placeItem(bot, "rail", railPosition);
}