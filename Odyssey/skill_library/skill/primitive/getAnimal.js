async function getAnimal(bot, type = null, x, y, z) {
    if (typeof type !== "string") {
        throw new Error("[getAnimal] type must be a string");
    }
    if (![x, y, z].every(Number.isFinite)) {
        throw new Error("[getAnimal] x, y and z must be finite numbers");
    }

    const foodByAnimal = {
        sheep: "wheat",
        cow: "wheat",
        chicken: "wheat_seeds",
        pig: "carrot",
    };
    const foodName = foodByAnimal[type];
    if (!foodName) {
        throw new Error(
            `[getAnimal] unsupported animal type: ${type}; expected sheep, cow, chicken or pig`
        );
    }

    const foodData = mcData.itemsByName[foodName];
    const food = foodData
        ? bot.inventory.findInventoryItem(foodData.id)
        : null;
    if (!food) {
        throw new Error(`[getAnimal] ${foodName} is required to lure ${type}`);
    }
    await bot.equip(food, "hand");

    const animal = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
        return bot.nearestEntity((entity) => {
            return (
                entity.name === type &&
                entity.position.distanceTo(bot.entity.position) < 32
            );
        });
    });
    if (!animal) {
        throw new Error(`[getAnimal] could not find a ${type} within 32 blocks`);
    }

    await bot.pathfinder.goto(
        new GoalNear(
            animal.position.x,
            animal.position.y,
            animal.position.z,
            2
        )
    );
    await bot.lookAt(animal.position);
    await goto(bot, x, y, z);

    const target = new Vec3(x, y, z);
    const targetRadius = 4;
    const followWaitTicks = 100;
    for (let waited = 0; waited <= followWaitTicks; waited += 10) {
        if (animal.position.distanceTo(target) <= targetRadius) {
            bot.chat(`Lured ${type} to (${x}, ${y}, ${z}).`);
            return animal;
        }
        if (waited < followWaitTicks) {
            await bot.waitForTicks(10);
        }
    }

    throw new Error(
        `[getAnimal] ${type} did not reach within ${targetRadius} blocks of (${x}, ${y}, ${z})`
    );
}
