async function killOneBat(bot) {
    // Equip the sword
    await equipSword(bot);
    // Find the nearest bat
    const bat = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
      const bat = bot.nearestEntity(entity => {
        return entity.name === "bat" && entity.position.distanceTo(bot.entity.position) < 32;
      });
      return bat;
    });
    if (!bat) {
      bot.chat("Could not find a bat.");
      return;
    }
  
    // Kill the bat using the sword
    await killMob(bot, "bat", 300);
    bot.chat("Killed a bat.");
  
    // Collect the dropped items
    await bot.pathfinder.goto(new GoalBlock(bat.position.x, bat.position.y, bat.position.z));
    bot.chat("Collected dropped items.");
  }