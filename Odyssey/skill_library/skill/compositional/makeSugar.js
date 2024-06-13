async function makeSugar(bot) {
    let sugarCaneCount = bot.inventory.count(mcData.itemsByName.sugar_cane.id);
    if (!sugarCaneCount) {
        bot.chat("Not enough sugar cane in inventory! collect some first!");
        return;
    }
    // Make sugar
    await craftItem(bot, "sugar", 1);
    bot.chat("Made sugar.");
}