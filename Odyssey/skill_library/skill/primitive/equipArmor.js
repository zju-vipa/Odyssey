async function equipArmor(bot) {
    // Find the chestplate, leggings, helmet and boots in the inventory
    const Chestplate =  bot.inventory.findInventoryItem(mcData.itemsByName.diamond_chestplate.id)   ||
                        bot.inventory.findInventoryItem(mcData.itemsByName.iron_chestplate.id)      ||
                        bot.inventory.findInventoryItem(mcData.itemsByName.golden_chestplate.id)    ||
                        bot.inventory.findInventoryItem(mcData.itemsByName.chainmail_chestplate.id) ||
                        bot.inventory.findInventoryItem(mcData.itemsByName.leather_chestplate.id);
    const Leggings =    bot.inventory.findInventoryItem(mcData.itemsByName.diamond_leggings.id)     ||
                        bot.inventory.findInventoryItem(mcData.itemsByName.iron_leggings.id)        ||
                        bot.inventory.findInventoryItem(mcData.itemsByName.golden_leggings.id)      ||
                        bot.inventory.findInventoryItem(mcData.itemsByName.chainmail_leggings.id)   ||
                        bot.inventory.findInventoryItem(mcData.itemsByName.leather_leggings.id);
    const Helmet =  bot.inventory.findInventoryItem(mcData.itemsByName.diamond_helmet.id)     ||
                    bot.inventory.findInventoryItem(mcData.itemsByName.iron_helmet.id)        ||
                    bot.inventory.findInventoryItem(mcData.itemsByName.golden_helmet.id)      ||
                    bot.inventory.findInventoryItem(mcData.itemsByName.chainmail_helmet.id)   ||
                    bot.inventory.findInventoryItem(mcData.itemsByName.leather_helmet.id);
    const Boots =   bot.inventory.findInventoryItem(mcData.itemsByName.diamond_boots.id)     ||
                    bot.inventory.findInventoryItem(mcData.itemsByName.iron_boots.id)        ||
                    bot.inventory.findInventoryItem(mcData.itemsByName.golden_boots.id)      ||
                    bot.inventory.findInventoryItem(mcData.itemsByName.chainmail_boots.id)   ||
                    bot.inventory.findInventoryItem(mcData.itemsByName.leather_boots.id);
  
    // Equip the chestplate, leggings, helmet and boots in the appropriate slots
    if (Chestplate) {
        await bot.equip(Chestplate, "torso");
    } else {
        await bot.chat("No chestplate found in inventory.");
    }
    if (Leggings) {
        await bot.equip(Leggings, "legs");
    } else {
        await bot.chat("No leggings found in inventory.");
    }
    if (Helmet) {
        await bot.equip(Helmet, "head");
    } else {
        await bot.chat("No helmet found in inventory.");
    }
    if (Boots) {
        await bot.equip(Boots, "feet");
    } else {
        await bot.chat("No boots found in inventory.");
    }
  }