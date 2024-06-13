async function cookPorkchop(bot) {
  // Check if there is a furnace and some coals and porks in the inventory
  const furnaceItem = bot.inventory.findInventoryItem(mcData.itemsByName.furnace.id);
  const coal = bot.inventory.findInventoryItem(mcData.itemsByName.coal.id);
  const pork = bot.inventory.findInventoryItem(mcData.itemsByName.porkchop.id);
  // If not, craft a furnace using the available cobblestone
  if (!pork)
    await bot.chat("No pork in inventory! Kill one pig first!");
    // await killOnePig(bot); // not allowed for farming tasks
  if (!furnaceItem) 
    await craftFurnace(bot);
  if (!coal)
    await mineCoalOre(bot); 
  await cookFood(bot, "porkchop");
}