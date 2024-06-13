async function equipSwordOrCraftOne(bot) {
    // Find the best sword in the bot's inventory
    let diamondSword = bot.inventory.findInventoryItem(mcData.itemsByName.diamond_sword.id);
    let ironSword = bot.inventory.findInventoryItem(mcData.itemsByName.iron_sword.id);
    let stoneSword = bot.inventory.findInventoryItem(mcData.itemsByName.stone_sword.id);
    let woodenSword = bot.inventory.findInventoryItem(mcData.itemsByName.wooden_sword.id);
    // Equip the best sword
    if (diamondSword) {
        await bot.equip(diamondSword, "hand");
    } else if (ironSword) {
        await bot.equip(ironSword, "hand");
    } else if (stoneSword) {
        await bot.equip(stoneSword, "hand");
    } else if (woodenSword) {
        await bot.equip(woodenSword, "hand");
    } else {
        await craftWoodenSword(bot);
        woodenSword = bot.inventory.findInventoryItem(mcData.itemsByName.wooden_sword.id);
        await bot.equip(woodenSword, "hand");
    }
    bot.chat("Sword equipped.");
  }