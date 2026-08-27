async function cookFood(bot, type = null, count = 1) {
    if (!Number.isInteger(count) || count < 1) {
      throw new Error("count for cookFood must be a positive integer");
    }
    const foodType = mcData.itemsByName[type];
    if (!foodType) {
      bot.chat(`No item named ${type}.`);
      return 0;
    }
    const furnaceItem = bot.inventory.findInventoryItem(mcData.itemsByName.furnace.id);
    const coal = bot.inventory.findInventoryItem(mcData.itemsByName.coal.id);
    const food = bot.inventory.findInventoryItem(foodType.id);
    if (!food) {
      await bot.chat(`No ${type} found in inventory.`);
      return 0;
    }
    if (!furnaceItem) {
      await bot.chat(`No furnace found in inventory.`);
      return 0;
    }
    if (!coal) {
      await bot.chat(`No coal found in inventory.`);
      return 0;
    }
    const furnacePosition = await findSuitablePosition(bot);
    if (!furnacePosition) {
      await bot.chat("No suitable position found for a furnace.");
      return 0;
    }
    await placeItem(bot, "furnace", furnacePosition);
    return await smeltItem(bot, type, "coal", count);
}
