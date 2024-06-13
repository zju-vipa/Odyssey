async function feedAnimals(bot, count = 1, type = null) {
    const fedEntities = new Set(); // Set to store entities that have been fed
    for (let i = 0; i < count; i++) {
        let animal = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
            let entity = bot.nearestEntity(entity => {
                // Check if the entity is of the specified type, within 32 blocks, not already fed
                return entity.name === type && 
                       entity.position.distanceTo(bot.entity.position) < 32 &&
                       !fedEntities.has(entity.uuid)
            });
            return entity;
        });
        if (!animal) {
            bot.chat(`Could not find a suitable ${type}.`);
            return;
        }
        fedEntities.add(animal.uuid); // Add the UUID of the fed entity to the Set
        await bot.pathfinder.goto(new GoalBlock(animal.position.x, animal.position.y, animal.position.z));
        await bot.lookAt(animal.position);
        await bot.useOn(animal);
    }
}
