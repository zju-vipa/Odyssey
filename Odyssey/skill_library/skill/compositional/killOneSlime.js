async function killOneSlime(bot) {
    // Equip the sword
    await equipSword(bot);
    // Find the nearest slime
    const slime = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
      const slime = bot.nearestEntity(entity => {
        return entity.name === "slime" && entity.position.distanceTo(bot.entity.position) < 32;
      });
      return slime;
    });
    if (!slime) {
      bot.chat("Could not find a slime.");
      return;
    }
  
    // Kill the slime using the sword
    await killMob(bot, "slime", 300);
    bot.chat("Killed a slime.");
  
    // Collect the dropped items
    await bot.pathfinder.goto(new GoalBlock(slime.position.x, slime.position.y, slime.position.z));
    bot.chat("Collected dropped items.");
  }