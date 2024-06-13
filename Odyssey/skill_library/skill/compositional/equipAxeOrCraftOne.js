async function equipAxeOrCraftOne(bot) {
    // Find the best axe in the bot's inventory
    let diamondAxe = bot.inventory.findInventoryItem(mcData.itemsByName.diamond_axe.id);
    let ironAxe = bot.inventory.findInventoryItem(mcData.itemsByName.iron_axe.id);
    let stoneAxe = bot.inventory.findInventoryItem(mcData.itemsByName.stone_axe.id);
    let woodenAxe = bot.inventory.findInventoryItem(mcData.itemsByName.wooden_axe.id);
    // Equip the best axe
    if (diamondAxe) {
        await bot.equip(diamondAxe, "hand");
    } else if (ironAxe) {
        await bot.equip(ironAxe, "hand");
    } else if (stoneAxe) {
        await bot.equip(stoneAxe, "hand");
    } else if (woodenAxe) {
        await bot.equip(woodenAxe, "hand");
    } else {
        await craftWoodenAxe(bot);
        woodenAxe = bot.inventory.findInventoryItem(mcData.itemsByName.wooden_axe.id);
        await bot.equip(woodenAxe, "hand");
    }
    // bot.chat("axe equipped.");
  }