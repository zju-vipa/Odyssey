async function killOneCreeper(bot) {
    // Equip the sword
    await equipSword(bot);
    // Find the nearest creeper
    const creeper = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
      const creeper = bot.nearestEntity(entity => {
        return entity.name === "creeper" && entity.position.distanceTo(bot.entity.position) < 32;
      });
      return creeper;
    });
    if (!creeper) {
      bot.chat("Could not find a creeper.");
      return;
    }
  
    // Kill the creeper using the sword
    await killMob(bot, "creeper", 300);
    bot.chat("Killed a creeper.");
  
    // Collect the dropped items
    await bot.pathfinder.goto(new GoalBlock(creeper.position.x, creeper.position.y, creeper.position.z));
    bot.chat("Collected dropped items.");
  }