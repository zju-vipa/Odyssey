async function respawnAndClear(bot) {
    await bot.chat("/tp @a ~100 256 ~100");
    await bot.chat("/clear @a");
    await bot.chat("/gamemode survival");
    await bot.chat("/difficulty peaceful");
    await bot.chat("Teleported to new location and reset inventory.");
}