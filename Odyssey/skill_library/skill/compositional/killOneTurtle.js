async function killOneTurtle(bot) {
    // Equip the sword
    await equipSword(bot);
    // Find the nearest turtle
    const turtle = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
      const turtle = bot.nearestEntity(entity => {
        return entity.name === "turtle" && entity.position.distanceTo(bot.entity.position) < 32;
      });
      return turtle;
    });
    if (!turtle) {
      bot.chat("Could not find a turtle.");
      return;
    }
  
    // Kill the turtle using the sword
    await killMob(bot, "turtle", 300);
    bot.chat("Killed a turtle.");
  
    // Collect the dropped items
    await bot.pathfinder.goto(new GoalBlock(turtle.position.x, turtle.position.y, turtle.position.z));
    bot.chat("Collected dropped items.");
  }