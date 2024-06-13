async function cookChicken(bot) {
    // Check if there is a furnace and some coals and chicken in the inventory
    const furnaceItem = bot.inventory.findInventoryItem(mcData.itemsByName.furnace.id);
    const coal = bot.inventory.findInventoryItem(mcData.itemsByName.coal.id);
    const chicken = bot.inventory.findInventoryItem(mcData.itemsByName.chicken.id);
    // If not, craft a furnace using the available cobblestone
    if (!chicken)
        await bot.chat("No chicken in inventory! Kill one chicken first!");
        // await killOneChicken(bot); // not allowed for farming tasks
    if (!furnaceItem) 
        await craftFurnace(bot);
    if (!coal)
        await mineCoalOre(bot); 
    await cookFood(bot, "chicken");
}