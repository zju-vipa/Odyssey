async function breedChicken(bot) {
    let wheatSeedsCount = bot.inventory.count(mcData.itemsByName.wheat_seeds.id);
    let wheatSeed = bot.inventory.findInventoryItem(mcData.itemsByName.wheat_seeds.id);
    if (wheatSeedsCount <= 2) {
        bot.chat("Not enough wheat seeds for breeding. Need 2 wheat seeds.");
        return;
    }
    await bot.equip(wheatSeed, "hand");
    await feedAnimals(bot, 2, "chicken");
}