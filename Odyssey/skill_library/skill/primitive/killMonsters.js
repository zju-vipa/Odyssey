async function killMonsters(bot, type = null, count = 1) {
  if (typeof type !== "string" || type.length === 0) {
    throw new Error("type for killMonsters must be a non-empty string");
  }
  if (!Number.isInteger(count) || count < 1) {
    throw new Error("count for killMonsters must be a positive integer");
  }
  let isAlive = true;
  const onDeath = () => {
    bot.chat("I lost the combat.");
    isAlive = false;
  };
  bot.on("death", onDeath);
  try {
    if (!await equipSword(bot)) {
      return false;
    }
    await equipArmor(bot);
    for (let i = 0; i < count; i++) {
      if (!isAlive) {
        return false;
      }
      const result = await killMob(bot, type, 300);
      if (!result) {
        bot.chat(`Could not find a ${type} to kill.`);
        return false;
      }
    }
    if (!isAlive) {
      return false;
    }
    await bot.chat("I won the combat.");
    return true;
  } finally {
    bot.removeListener("death", onDeath);
  }
}
