async function killOneMule(bot) {
    // Equip the sword
    await equipSword(bot);
    // Find the nearest ule
    const ule = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
      const ule = bot.nearestEntity(entity => {
        return entity.name === "mule" && entity.position.distanceTo(bot.entity.position) < 32;
      });
      return ule;
    });
    if (!ule) {
      bot.chat("Could not find a mule.");
      return;
    }
  
    // Kill the mule using the sword
    await killMob(bot, "mule", 300);
    bot.chat("Killed a mule.");
  
    // Collect the dropped items
    await bot.pathfinder.goto(new GoalBlock(ule.position.x, ule.position.y, ule.position.z));
    bot.chat("Collected dropped items.");
  }