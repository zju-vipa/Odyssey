async function killOneHorse(bot) {
    // Equip the sword
    await equipSword(bot);
    // Find the nearest horse
    const horse = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
      const horse = bot.nearestEntity(entity => {
        return entity.name === "horse" && entity.position.distanceTo(bot.entity.position) < 32;
      });
      return horse;
    });
    if (!horse) {
      bot.chat("Could not find a horse.");
      return;
    }
  
    // Kill the horse using the sword
    await killMob(bot, "horse", 300);
    bot.chat("Killed a horse.");
  
    // Collect the dropped items
    await bot.pathfinder.goto(new GoalBlock(horse.position.x, horse.position.y, horse.position.z));
    bot.chat("Collected dropped items.");
  }