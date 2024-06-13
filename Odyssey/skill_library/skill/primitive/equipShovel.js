async function equipShovel(bot) {
    // Find the best shovel in the bot's inventory
    const shovel = bot.inventory.findInventoryItem(mcData.itemsByName.diamond_shovel.id)||
                    bot.inventory.findInventoryItem(mcData.itemsByName.iron_shovel.id)   ||
                    bot.inventory.findInventoryItem(mcData.itemsByName.stone_shovel.id)  ||
                    bot.inventory.findInventoryItem(mcData.itemsByName.golden_shovel.id) ||
                    bot.inventory.findInventoryItem(mcData.itemsByName.wooden_shovel.id);
    // Equip the best shovel
    if (shovel) {
        await bot.equip(shovel, "hand");
        bot.chat("Shovel equipped.");
        return true;
    } else {
        bot.chat("No shovel in inventory.");
        return false;
    }
}