async function equipPickaxeOrCraftOne(bot) {
    // Find the best pickaxe in the bot's inventory
    let diamondPickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.diamond_pickaxe.id);
    let ironPickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.iron_pickaxe.id);
    let stonePickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.stone_pickaxe.id);
    let woodenPickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.wooden_pickaxe.id);
    // Equip the best pickaxe
    if (diamondPickaxe) {
        await bot.equip(diamondPickaxe, "hand");
    } else if (ironPickaxe) {
        await bot.equip(ironPickaxe, "hand");
    } else if (stonePickaxe) {
        await bot.equip(stonePickaxe, "hand");
    } else if (woodenPickaxe) {
        await bot.equip(woodenPickaxe, "hand");
    } else {
        await craftWoodenPickaxe(bot);
        woodenPickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.wooden_pickaxe.id);
        await bot.equip(woodenPickaxe, "hand");
    }
    // bot.chat("pickaxe equipped.");
  }