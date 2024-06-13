async function killOneSheep(bot) {
    // Equip the sword
    await equipSword(bot);
    // Find the nearest sheep
    const sheep = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
      const sheep = bot.nearestEntity(entity => {
        return entity.name === "sheep" && entity.position.distanceTo(bot.entity.position) < 32;
      });
      return sheep;
    });
    if (!sheep) {
      bot.chat("Could not find a sheep.");
      return;
    }
  
    // Kill the sheep using the sword
    await killMob(bot, "sheep", 300);
    bot.chat("Killed a sheep.");
  
    // Collect the dropped items
    await bot.pathfinder.goto(new GoalBlock(sheep.position.x, sheep.position.y, sheep.position.z));
    bot.chat("Collected dropped items.");
  }