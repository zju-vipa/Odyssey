async function combatEnv(bot, h = 10, r = 20, y = 150) {
    // let h = 10;    env height
    // let r = 20;    env size
    // let y = 150;   env position y
    if (y + h >= 320) {
        await bot.chat("upper bound exceeded.");
        return;
    } else if (y <= -64) {
        await bot.chat("lower bound exceeded.");
        return;
    } else if ((2*r + 1) * (2*r + 1) * (h + 1) >= 32768) {
        await bot.chat("Too many blocks."); // fill max 32768
        return;
    }
    // kill potential mobs and set difficulty to easy for summoning
    await bot.chat("/difficulty peaceful")
    await bot.chat("/difficulty easy")
    // env set
    await bot.chat(`/fill ~${-r} ${y} ~${-r} ~${r} ${y+h} ~${r} minecraft:sea_lantern`);
    await bot.chat(`/fill ~${-(r-1)} ${y+1} ~${-(r-1)} ~${r-1} ${y+h-1} ~${r-1} minecraft:air`);
    await bot.chat(`/tp @p ~ ${y+1} ~`);
}