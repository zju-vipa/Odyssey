async function feedAnimals(bot, count = 1, type = null) {
    const foodByAnimal = {
        cow: "wheat",
        sheep: "wheat",
        pig: "carrot",
        chicken: "wheat_seeds",
    };
    if (!Number.isInteger(count) || count < 1) {
        throw new Error("count for feedAnimals must be a positive integer");
    }
    const foodName = foodByAnimal[type];
    if (!foodName) {
        bot.chat(`Unsupported animal type for feeding: ${type}`);
        return 0;
    }
    const foodType = mcData.itemsByName[foodName];
    const fedEntities = new Set();
    let fedCount = 0;
    for (let i = 0; i < count; i++) {
        const food = bot.inventory.findInventoryItem(foodType.id);
        if (!food) {
            bot.chat(`No ${foodName} found in inventory to feed ${type}.`);
            return fedCount;
        }
        await bot.equip(food, "hand");
        let animal = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
            let entity = bot.nearestEntity(entity => {
                const entityKey = entity.uuid ?? entity.id ?? entity;
                return entity.name === type &&
                       entity.position.distanceTo(bot.entity.position) < 32 &&
                       !fedEntities.has(entityKey);
            });
            return entity;
        });
        if (!animal) {
            bot.chat(`Could not find a suitable ${type}.`);
            return fedCount;
        }
        await bot.pathfinder.goto(new GoalBlock(animal.position.x, animal.position.y, animal.position.z));
        await bot.lookAt(animal.position);
        await bot.useOn(animal);
        fedEntities.add(animal.uuid ?? animal.id ?? animal);
        fedCount++;
    }
    return fedCount;
}
