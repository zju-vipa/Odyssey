async function equipSword(bot) {
    // Find the best sword in the bot's inventory
    const Sword =   bot.inventory.findInventoryItem(mcData.itemsByName.diamond_sword.id)||
                    bot.inventory.findInventoryItem(mcData.itemsByName.iron_sword.id)   ||
                    bot.inventory.findInventoryItem(mcData.itemsByName.stone_sword.id)  ||
                    bot.inventory.findInventoryItem(mcData.itemsByName.golden_sword.id) ||
                    bot.inventory.findInventoryItem(mcData.itemsByName.wooden_sword.id);
    // Equip the best sword
    if (Sword) {
        await bot.equip(Sword, "hand");
        bot.chat("Sword equipped.");
        return true;
    } else {
        bot.chat("No sword in inventory.");
        return false;
    }
}