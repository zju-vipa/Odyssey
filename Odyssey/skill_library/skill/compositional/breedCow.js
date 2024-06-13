async function breedCow(bot) {
    let wheatCount = bot.inventory.count(mcData.itemsByName.wheat.id);
    let wheat = bot.inventory.findInventoryItem(mcData.itemsByName.wheat.id);
    if (wheatCount <= 2) {
        bot.chat("Not enough wheat for breeding. Need 2 wheat.");
        return;
    }
    await bot.equip(wheat, "hand");
    await feedAnimals(bot, 2, "cow");
}