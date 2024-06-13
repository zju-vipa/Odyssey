async function killOneChicken(bot) {
    // Equip the sword
    await equipSword(bot);
    // Find the nearest chicken
    const chicken = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
      const chicken = bot.nearestEntity(entity => {
        return entity.name === "chicken" && entity.position.distanceTo(bot.entity.position) < 32;
      });
      return chicken;
    });
    if (!chicken) {
      bot.chat("Could not find a chicken.");
      return;
    }
  
    // Kill the chicken using the sword
    await killMob(bot, "chicken", 300);
    bot.chat("Killed a chicken.");
  
    // Collect the dropped items
    await bot.pathfinder.goto(new GoalBlock(chicken.position.x, chicken.position.y, chicken.position.z));
    bot.chat("Collected dropped items.");
  }