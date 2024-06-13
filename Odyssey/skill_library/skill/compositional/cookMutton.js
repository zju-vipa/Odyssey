async function cookMutton(bot) {
    // Check if there is a furnace and some coals and mutton in the inventory
    const furnaceItem = bot.inventory.findInventoryItem(mcData.itemsByName.furnace.id);
    const coal = bot.inventory.findInventoryItem(mcData.itemsByName.coal.id);
    const mutton = bot.inventory.findInventoryItem(mcData.itemsByName.mutton.id);
    // If not, craft a furnace using the available cobblestone
    if (!mutton)
        await bot.chat("No mutton in inventory! Kill one sheep first!");
        // await killOneSheep(bot); // not allowed for farming tasks
    if (!furnaceItem) 
        await craftFurnace(bot);
    if (!coal)
        await mineCoalOre(bot); 
    await cookFood(bot, "mutton");
}