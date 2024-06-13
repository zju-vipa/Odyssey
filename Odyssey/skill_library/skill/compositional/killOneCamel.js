async function killOneCamel(bot) {
    // Equip the sword
    await equipSword(bot);
    // Find the nearest camel
    const camel = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
      const camel = bot.nearestEntity(entity => {
        return entity.name === "camel" && entity.position.distanceTo(bot.entity.position) < 32;
      });
      return camel;
    });
    if (!camel) {
      bot.chat("Could not find a camel.");
      return;
    }
  
    // Kill the camel using the sword
    await killMob(bot, "camel", 300);
    bot.chat("Killed a camel.");
  
    // Collect the dropped items
    await bot.pathfinder.goto(new GoalBlock(camel.position.x, camel.position.y, camel.position.z));
    bot.chat("Collected dropped items.");
  }