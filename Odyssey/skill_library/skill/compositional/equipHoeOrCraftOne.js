async function equipHoeOrCraftOne(bot) {
    // Find the best hoe in the bot's inventory
    let diamondHoe = bot.inventory.findInventoryItem(mcData.itemsByName.diamond_hoe.id);
    let ironHoe = bot.inventory.findInventoryItem(mcData.itemsByName.iron_hoe.id);
    let stoneHoe = bot.inventory.findInventoryItem(mcData.itemsByName.stone_hoe.id);
    let woodenHoe = bot.inventory.findInventoryItem(mcData.itemsByName.wooden_hoe.id);
    // Equip the best hoe
    if (diamondHoe) {
        await bot.equip(diamondHoe, "hand");
    } else if (ironHoe) {
        await bot.equip(ironHoe, "hand");
    } else if (stoneHoe) {
        await bot.equip(stoneHoe, "hand");
    } else if (woodenHoe) {
        await bot.equip(woodenHoe, "hand");
    } else {
        await craftWoodenHoe(bot);
        woodenHoe = bot.inventory.findInventoryItem(mcData.itemsByName.wooden_hoe.id);
        await bot.equip(woodenHoe, "hand");
    }
    // bot.chat("hoe equipped.");
  }