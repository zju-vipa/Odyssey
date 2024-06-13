async function killMonsters(bot, type = null, count = 1) {
  await bot.chat("/gamemode survival");
  isAlive = true;
  // Listen for bot's death
  bot.on('death', () => {
    bot.chat("I lost the combat.");
    isAlive = false;
    return false;
  });
  await equipSword(bot);
  await equipArmor(bot);
  for (i = 0; i < count; i++) {
    if (!isAlive) {
      return false;
    }
    // Find the nearest monster
    const monster = bot.nearestEntity(entity => {
      return entity.name === type && entity.position.distanceTo(bot.entity.position) < 32;
    });
    // Kill the animal using the sword
    await killMob(bot, type, 300);
    await bot.chat(`Killed a ${type}.`);
  
    // Collect the dropped items
    await bot.pathfinder.goto(new GoalBlock(monster.position.x, monster.position.y, monster.position.z));
    await bot.chat("Collected dropped items.");
    await bot.chat(`Killed a ${type}.`);
  }
  await bot.chat("I won the combat.");
  await bot.chat("/gamemode survival");
  return true;
}