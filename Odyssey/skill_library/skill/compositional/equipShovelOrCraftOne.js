async function equipShovelOrCraftOne(bot) {
    // Find the best shovel in the bot's inventory
    let diamondShovel = bot.inventory.findInventoryItem(mcData.itemsByName.diamond_shovel.id);
    let ironShovel = bot.inventory.findInventoryItem(mcData.itemsByName.iron_shovel.id);
    let stoneShovel = bot.inventory.findInventoryItem(mcData.itemsByName.stone_shovel.id);
    let woodenShovel = bot.inventory.findInventoryItem(mcData.itemsByName.wooden_shovel.id);
    // Equip the best shovel
    if (diamondShovel) {
        await bot.equip(diamondShovel, "hand");
    } else if (ironShovel) {
        await bot.equip(ironShovel, "hand");
    } else if (stoneShovel) {
        await bot.equip(stoneShovel, "hand");
    } else if (woodenShovel) {
        await bot.equip(woodenShovel, "hand");
    } else {
        await craftWoodenShovel(bot);
        woodenShovel = bot.inventory.findInventoryItem(mcData.itemsByName.wooden_shovel.id);
        await bot.equip(woodenShovel, "hand");
    }
    // bot.chat("shovel equipped.");
  }