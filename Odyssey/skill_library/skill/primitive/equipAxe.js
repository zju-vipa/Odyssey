async function equipAxe(bot) {
    // Find the best axe in the bot's inventory
    const axe = bot.inventory.findInventoryItem(mcData.itemsByName.diamond_axe.id)||
                    bot.inventory.findInventoryItem(mcData.itemsByName.iron_axe.id)   ||
                    bot.inventory.findInventoryItem(mcData.itemsByName.stone_axe.id)  ||
                    bot.inventory.findInventoryItem(mcData.itemsByName.golden_axe.id) ||
                    bot.inventory.findInventoryItem(mcData.itemsByName.wooden_axe.id);
    // Equip the best axe
    if (axe) {
        await bot.equip(axe, "hand");
        bot.chat("Axe equipped.");
        return true;
    } else {
        bot.chat("No axe in inventory.");
        return false;
    }
}