async function collectMelonSeeds(bot) {
    let melonSlice = bot.inventory.findInventoryItem(mcData.itemsByName.melon_slice.id);
    if (!melonSlice) {
        await bot.chat("No melon slice found in inventory.");
        return;
    }
    await craftItem(bot, "melon_seeds", 1);
}