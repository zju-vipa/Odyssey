async function killOneRabbit(bot) {
    // Equip the sword
    await equipSword(bot);
    // Find the nearest rabbit
    const rabbit = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
      const rabbit = bot.nearestEntity(entity => {
        return entity.name === "rabbit" && entity.position.distanceTo(bot.entity.position) < 32;
      });
      return rabbit;
    });
    if (!rabbit) {
      bot.chat("Could not find a rabbit.");
      return;
    }
  
    // Kill the rabbit using the sword
    await killMob(bot, "rabbit", 300);
    bot.chat("Killed a rabbit.");
  
    // Collect the dropped items
    await bot.pathfinder.goto(new GoalBlock(rabbit.position.x, rabbit.position.y, rabbit.position.z));
    bot.chat("Collected dropped items.");
  }