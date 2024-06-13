async function breedPig(bot) {
    let carrotsCount = bot.inventory.count(mcData.itemsByName.carrot.id);
    let carrot = bot.inventory.findInventoryItem(mcData.itemsByName.carrot.id);
    if (carrotsCount <= n) {
        bot.chat("Not enough carrots for breeding. Need 2 carrots.");
        return;
    }
    await bot.equip(carrot, "hand");
    await feedAnimals(bot, 2, "pig");
}