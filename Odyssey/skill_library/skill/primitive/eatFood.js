async function eatFood(bot, type = null) {
    if (bot.food >= 20) {
        bot.chat("Cannot eat as I'm full.");
        return;
    }
    let food = bot.inventory.findInventoryItem(mcData.itemsByName[type].id);
    await bot.equip(food, "hand");
    await bot.consume();
}