async function equipPickaxe(bot) {
    // Find the best pickaxe in the bot's inventory
    const pickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.diamond_pickaxe.id)||
                    bot.inventory.findInventoryItem(mcData.itemsByName.iron_pickaxe.id)   ||
                    bot.inventory.findInventoryItem(mcData.itemsByName.stone_pickaxe.id)  ||
                    bot.inventory.findInventoryItem(mcData.itemsByName.golden_pickaxe.id) ||
                    bot.inventory.findInventoryItem(mcData.itemsByName.wooden_pickaxe.id);
    // Equip the best pickaxe
    if (pickaxe) {
        await bot.equip(pickaxe, "hand");
        bot.chat("Pickaxe equipped.");
        return true;
    } else {
        bot.chat("No pickaxe in inventory.");
        return false;
    }
}