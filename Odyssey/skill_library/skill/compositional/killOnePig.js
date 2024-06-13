async function killOnePig(bot) {
  // Equip the sword
  await equipSword(bot);
  // Find the nearest pig
  const pig = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
    const pig = bot.nearestEntity(entity => {
      return entity.name === "pig" && entity.position.distanceTo(bot.entity.position) < 32;
    });
    return pig;
  });
  if (!pig) {
    bot.chat("Could not find a pig.");
    return;
  }

  // Kill the pig using the sword
  await killMob(bot, "pig", 300);
  bot.chat("Killed a pig.");

  // Collect the dropped items
  await bot.pathfinder.goto(new GoalBlock(pig.position.x, pig.position.y, pig.position.z));
  bot.chat("Collected dropped items.");
}