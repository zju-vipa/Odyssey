async function craftCutSandstone(bot) {
    let sandstoneCount = bot.inventory.count(mcData.itemsByName.sandstone.id);
    if (sandstoneCount < 4) {
        await collectSandstone(bot);
    }
    await craftItem(bot, "cut_sandstone", 1);
    bot.chat("Crafted cut sandstones.");
}