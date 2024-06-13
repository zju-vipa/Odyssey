async function getAnimal(bot, type = null, x, y, z) {
    // let type = "sheep"   type of animals
    // (x,y,z)   dest pos
    let wheatSeedsCount = bot.inventory.count(mcData.itemsByName.wheat_seeds.id);
    let wheatCount = bot.inventory.count(mcData.itemsByName.wheat.id);
    let carrotsCount = bot.inventory.count(mcData.itemsByName.carrot.id);
    let wheatSeed = bot.inventory.findInventoryItem(mcData.itemsByName.wheat_seeds.id);
    let wheat = bot.inventory.findInventoryItem(mcData.itemsByName.wheat.id);
    let carrot = bot.inventory.findInventoryItem(mcData.itemsByName.carrot.id);
    if (type = "sheep" || "cow") {
        if (wheatCount <= 1) {
            bot.chat("Not enough wheat.");
            return;
        }
        await bot.equip(wheat, "hand");
    } else if (type = "chichken") {
        if (wheatSeedsCount <= 1) {
            bot.chat("Not enough wheat seeds.");
            return;
        }
        await bot.equip(wheatSeed, "hand");
    } else if (type = "pig") {
        if (carrotsCount <= 1) {
            bot.chat("Not enough carrots.");
            return;
        }
        await bot.equip(carrot, "hand");
    } else {
        bot.chat("undefined type.");
        return;
    }
    
    let animal = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
        let entity = bot.nearestEntity(entity => {
            return entity.name === type && entity.position.distanceTo(bot.entity.position) < 32;
        });
        return entity;
    });
    if (!animal) {
        bot.chat(`Could not find a ${type}.`);
        return;
    }
    await bot.pathfinder.goto(new GoalBlock(x, y, z));
}