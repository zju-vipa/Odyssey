async function killOneSkeleton(bot) {
    // Equip the sword
    await equipSword(bot);
    // Find the nearest skeleton
    const skeleton = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
      const skeleton = bot.nearestEntity(entity => {
        return entity.name === "skeleton" && entity.position.distanceTo(bot.entity.position) < 32;
      });
      return skeleton;
    });
    if (!skeleton) {
      bot.chat("Could not find a skeleton.");
      return;
    }
  
    // Kill the skeleton using the sword
    await killMob(bot, "skeleton", 300);
    bot.chat("Killed a skeleton.");
  
    // Collect the dropped items
    await bot.pathfinder.goto(new GoalBlock(skeleton.position.x, skeleton.position.y, skeleton.position.z));
    bot.chat("Collected dropped items.");
  }