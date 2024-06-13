async function summonMob(bot, n = 1, r = 8, type = null) {
    // let n = 1;              number of monsters
    // let r = 8;              env size
    // let type = "zombie";    type of monsters
    // set to creative to prevent immediate monster attacks
    bot.chat("/gamemode creative")
    bot.chat("Summoning mob...")
    function getRandomNumber(r) {
        const sign = Math.random() < 0.5 ? -1 : 1;
        const randomValue = Math.random() * r;
        return sign * (randomValue + r);
    }
    for (let i = 0; i < n; i++) {
        let x = getRandomNumber(r);
        let z = getRandomNumber(r);
        await bot.chat(`/summon minecraft:${type} ~${x} ~1 ~${z}`);
    }
    bot.chat("Mobs summoned.")
}