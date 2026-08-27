async function eatFood(bot, type = null) {
    if (bot.food >= 20) {
        bot.chat("Cannot eat as I'm full.");
        return false;
    }
    const foodType = mcData.itemsByName[type];
    if (!foodType) {
        bot.chat(`No item named ${type}.`);
        return false;
    }
    const food = bot.inventory.findInventoryItem(foodType.id);
    if (!food) {
        bot.chat(`No ${type} found in inventory.`);
        return false;
    }
    await bot.equip(food, "hand");
    await bot.consume();
    return true;
}
