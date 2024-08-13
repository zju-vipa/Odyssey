async function equipBestTool(bot, type) {
    // used to equip the highest level of tools in inventory
    if (type == "sword") {
        // find the best sword in the bot's inventory
        const Sword =   bot.inventory.findInventoryItem(mcData.itemsByName.diamond_sword.id)||
                        bot.inventory.findInventoryItem(mcData.itemsByName.iron_sword.id)   ||
                        bot.inventory.findInventoryItem(mcData.itemsByName.stone_sword.id)  ||
                        bot.inventory.findInventoryItem(mcData.itemsByName.golden_sword.id) ||
                        bot.inventory.findInventoryItem(mcData.itemsByName.wooden_sword.id);
        // equip the best sword
        if (Sword) {
            await bot.equip(Sword, "hand");
            bot.chat("Sword equipped.");
            return true;
        } else {
            bot.chat("No sword in inventory.");
            return false;
        }
    } else if (type == "pickaxe") {
        // find the best pickaxe in the bot's inventory
        const pickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.diamond_pickaxe.id)||
                        bot.inventory.findInventoryItem(mcData.itemsByName.iron_pickaxe.id)   ||
                        bot.inventory.findInventoryItem(mcData.itemsByName.stone_pickaxe.id)  ||
                        bot.inventory.findInventoryItem(mcData.itemsByName.golden_pickaxe.id) ||
                        bot.inventory.findInventoryItem(mcData.itemsByName.wooden_pickaxe.id);
        // equip the best pickaxe
        if (pickaxe) {
            await bot.equip(pickaxe, "hand");
            bot.chat("Pickaxe equipped.");
            return true;
        } else {
            bot.chat("No pickaxe in inventory.");
            return false;
        }
    } else if (type == "axe") {
        // find the best axe in the bot's inventory
        const axe = bot.inventory.findInventoryItem(mcData.itemsByName.diamond_axe.id)||
                    bot.inventory.findInventoryItem(mcData.itemsByName.iron_axe.id)   ||
                    bot.inventory.findInventoryItem(mcData.itemsByName.stone_axe.id)  ||
                    bot.inventory.findInventoryItem(mcData.itemsByName.golden_axe.id) ||
                    bot.inventory.findInventoryItem(mcData.itemsByName.wooden_axe.id);
        // equip the best axe
        if (axe) {
            await bot.equip(axe, "hand");
            bot.chat("Axe equipped.");
            return true;
        } else {
            bot.chat("No axe in inventory.");
            return false;
        }
    } else if (type == "hoe") {
        // find the best hoe in the bot's inventory
        const hoe = bot.inventory.findInventoryItem(mcData.itemsByName.diamond_hoe.id)||
                    bot.inventory.findInventoryItem(mcData.itemsByName.iron_hoe.id)   ||
                    bot.inventory.findInventoryItem(mcData.itemsByName.stone_hoe.id)  ||
                    bot.inventory.findInventoryItem(mcData.itemsByName.golden_hoe.id) ||
                    bot.inventory.findInventoryItem(mcData.itemsByName.wooden_hoe.id);
        // equip the best hoe
        if (hoe) {
            await bot.equip(hoe, "hand");
            bot.chat("Hoe equipped.");
            return true;
        } else {
            bot.chat("No hoe in inventory.");
            return false;
        }
    } else if (type == "shovel") {
        // find the best shovel in the bot's inventory
        const shovel =  bot.inventory.findInventoryItem(mcData.itemsByName.diamond_shovel.id)||
                        bot.inventory.findInventoryItem(mcData.itemsByName.iron_shovel.id)   ||
                        bot.inventory.findInventoryItem(mcData.itemsByName.stone_shovel.id)  ||
                        bot.inventory.findInventoryItem(mcData.itemsByName.golden_shovel.id) ||
                        bot.inventory.findInventoryItem(mcData.itemsByName.wooden_shovel.id);
        // equip the best shovel
        if (shovel) {
            await bot.equip(shovel, "hand");
            bot.chat("Shovel equipped.");
            return true;
        } else {
            bot.chat("No shovel in inventory.");
            return false;
        }
    } else if (type == "helmet") {
        // find the best helmet in the bot's inventory
        const Helmet =  bot.inventory.findInventoryItem(mcData.itemsByName.diamond_helmet.id)     ||
                        bot.inventory.findInventoryItem(mcData.itemsByName.iron_helmet.id)        ||
                        bot.inventory.findInventoryItem(mcData.itemsByName.golden_helmet.id)      ||
                        bot.inventory.findInventoryItem(mcData.itemsByName.chainmail_helmet.id)   ||
                        bot.inventory.findInventoryItem(mcData.itemsByName.leather_helmet.id);
        if (Helmet) {
            await bot.equip(Helmet, "head");
            return true;
        } else {
            await bot.chat("No helmet found in inventory.");
            return false;
        }
    } else if (type == "chestplate") {
        // find the best chestplate in the bot's inventory
        const Chestplate =  bot.inventory.findInventoryItem(mcData.itemsByName.diamond_chestplate.id)   ||
                            bot.inventory.findInventoryItem(mcData.itemsByName.iron_chestplate.id)      ||
                            bot.inventory.findInventoryItem(mcData.itemsByName.golden_chestplate.id)    ||
                            bot.inventory.findInventoryItem(mcData.itemsByName.chainmail_chestplate.id) ||
                            bot.inventory.findInventoryItem(mcData.itemsByName.leather_chestplate.id);
        if (Chestplate) {
            await bot.equip(Chestplate, "torso");
            return true;
        } else {
            await bot.chat("No chestplate found in inventory.");
            return false;
        }
    } else if (type == "leggings") {
        // find the best leggings in the bot's inventory
        const Leggings =    bot.inventory.findInventoryItem(mcData.itemsByName.diamond_leggings.id)     ||
                            bot.inventory.findInventoryItem(mcData.itemsByName.iron_leggings.id)        ||
                            bot.inventory.findInventoryItem(mcData.itemsByName.golden_leggings.id)      ||
                            bot.inventory.findInventoryItem(mcData.itemsByName.chainmail_leggings.id)   ||
                            bot.inventory.findInventoryItem(mcData.itemsByName.leather_leggings.id);
        if (Leggings) {
            await bot.equip(Leggings, "legs");
            return true;
        } else {
            await bot.chat("No leggings found in inventory.");
            return false;
        }
    } else if (type == "boots") {
        // find the best boots in the bot's inventory
        const Boots =   bot.inventory.findInventoryItem(mcData.itemsByName.diamond_boots.id)     ||
                        bot.inventory.findInventoryItem(mcData.itemsByName.iron_boots.id)        ||
                        bot.inventory.findInventoryItem(mcData.itemsByName.golden_boots.id)      ||
                        bot.inventory.findInventoryItem(mcData.itemsByName.chainmail_boots.id)   ||
                        bot.inventory.findInventoryItem(mcData.itemsByName.leather_boots.id);
        if (Boots) {
            await bot.equip(Boots, "feet");
            return true;
        } else {
            await bot.chat("No boots found in inventory.");
            return false;
        }
    } else if (type == "shears") {
        const Shears = bot.inventory.findInventoryItem(mcData.itemsByName.shears.id)
        if (Shears) {
            await bot.equip(Shears, "hand");
            return true;
        } else {
            await bot.chat("No shears found in inventory.");
            return false;
        }
    } else if (type == "bucket") {
        const Bucket = bot.inventory.findInventoryItem(mcData.itemsByName.bucket.id)
        if (Bucket) {
            await bot.equip(Bucket, "hand");
            return true;
        } else {
            await bot.chat("No bucket found in inventory.");
            return false;
        }
    } else if (type == "fishing_rod") {
        const Fishing_rod = bot.inventory.findInventoryItem(mcData.itemsByName.fishing_rod.id)
        if (Fishing_rod) {
            await bot.equip(Fishing_rod, "hand");
            return true;
        } else {
            await bot.chat("No fishing_rod found in inventory.");
            return false;
        }
    }
    else {
        bot.chat("Invalid type of equipment.");
        return false;
    }
}

async function equipPickaxeOfLevel(bot, level) {
    // used for equipping a pickaxe of at least 'level'
    const diamond_pickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.diamond_pickaxe.id);
    const iron_pickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.iron_pickaxe.id);
    const stone_pickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.stone_pickaxe.id);
    const golden_pickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.golden_pickaxe.id);
    const wooden_pickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.wooden_pickaxe.id);
    const pickaxe_list = [diamond_pickaxe, iron_pickaxe, stone_pickaxe, golden_pickaxe, wooden_pickaxe];
    const index = ["diamond", "iron", "stone", "golden", "wooden"].indexOf(level);
    if (index === -1) {
        bot.chat("Invalid level");
        return false;
    }
    for (let i = 0; i <= index; i++) {
        let pickaxe = pickaxe_list[i];
        if (pickaxe) {
            await bot.equip(pickaxe, "hand");
            return true;
        }
    }
    return false;
}