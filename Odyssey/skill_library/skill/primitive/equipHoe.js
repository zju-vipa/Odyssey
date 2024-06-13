async function equipHoe(bot) {
    // Find the best hoe in the bot's inventory
    const hoe = bot.inventory.findInventoryItem(mcData.itemsByName.diamond_hoe.id)||
                    bot.inventory.findInventoryItem(mcData.itemsByName.iron_hoe.id)   ||
                    bot.inventory.findInventoryItem(mcData.itemsByName.stone_hoe.id)  ||
                    bot.inventory.findInventoryItem(mcData.itemsByName.golden_hoe.id) ||
                    bot.inventory.findInventoryItem(mcData.itemsByName.wooden_hoe.id);
    // Equip the best hoe
    if (hoe) {
        await bot.equip(hoe, "hand");
        bot.chat("Hoe equipped.");
        return true;
    } else {
        bot.chat("No hoe in inventory.");
        return false;
    }
}