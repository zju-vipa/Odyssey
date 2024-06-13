async function collectPumpkinSeeds(bot) {
    let pumpkin = bot.inventory.findInventoryItem(mcData.itemsByName.pumpkin.id);
    if (!pumpkin) {
        await bot.chat("No pumpkin found in inventory.");
        return;
    }
    await craftItem(bot, "pumpkin_seeds", 1);
}