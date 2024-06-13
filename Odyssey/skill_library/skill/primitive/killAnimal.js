async function killAnimal(bot, type = null) {
    // Equip the sword
    await equipSword(bot);
    // Find the nearest animal
    const animal = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
      const animal = bot.nearestEntity(entity => {
        return entity.name === type && entity.position.distanceTo(bot.entity.position) < 32;
      });
      return animal;
    });
    if (!animal) {
      bot.chat(`Could not find a ${type}.`);
      return;
    }
  
    // Kill the animal using the sword
    await killMob(bot, type, 300);
    bot.chat(`Killed a ${type}.`);
  
    // Collect the dropped items
    await bot.pathfinder.goto(new GoalBlock(animal.position.x, animal.position.y, animal.position.z));
    bot.chat("Collected dropped items.");
  }