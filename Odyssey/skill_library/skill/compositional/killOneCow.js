async function killOneCow(bot) {
    // Equip the sword
    await equipSword(bot);
    // Find the nearest cow
    const cow = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
      const cow = bot.nearestEntity(entity => {
        return entity.name === "cow" && entity.position.distanceTo(bot.entity.position) < 32;
      });
      return cow;
    });
    if (!cow) {
      bot.chat("Could not find a cow.");
      return;
    }
  
    // Kill the cow using the sword
    await killMob(bot, "cow", 300);
    bot.chat("Killed a cow.");
  
    // Collect the dropped items
    await bot.pathfinder.goto(new GoalBlock(cow.position.x, cow.position.y, cow.position.z));
    bot.chat("Collected dropped items.");
  }