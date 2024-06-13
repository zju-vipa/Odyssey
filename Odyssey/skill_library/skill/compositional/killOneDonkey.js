async function killOneDonkey(bot) {
    // Equip the sword
    await equipSword(bot);
    // Find the nearest Donkey
    const Donkey = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
      const Donkey = bot.nearestEntity(entity => {
        return entity.name === "donkey" && entity.position.distanceTo(bot.entity.position) < 32;
      });
      return Donkey;
    });
    if (!Donkey) {
      bot.chat("Could not find a donkey.");
      return;
    }
  
    // Kill the Donkey using the sword
    await killMob(bot, "donkey", 300);
    bot.chat("Killed a donkey.");
  
    // Collect the dropped items
    await bot.pathfinder.goto(new GoalBlock(Donkey.position.x, Donkey.position.y, Donkey.position.z));
    bot.chat("Collected dropped items.");
  }