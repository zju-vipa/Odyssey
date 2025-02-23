async function setGamemode(bot, mode) {
    // mode = 'survival' or 'creative' or 'spectator' or 'adventure'
    bot.chat(`/gamemode ${mode}`);
}

async function setDifficulty(bot, difficulty) {
    // difficulty = 'peaceful' or 'easy' or 'normal' or 'hard'
    bot.chat(`/difficulty ${difficulty}`);
}

async function setWeather(bot, weather) {
    // weather = 'clear' or 'rain' or 'thunder'
    bot.chat(`/weather ${weather}`);
}

async function setTime(bot, time) {
    // time = 'day' or 'night' or any number representing the time of day
    bot.chat(`/time set ${time}`);
}

async function clear(bot) {
    bot.chat(`/clear @s`);
}

async function initialInventory(bot, item_dict) {
    await setGamemode(bot, 'creative') // To avoid immediate attack from mobs
    // Iterate over the item dictionary and give each item to the bot
    for (const [item, count] of Object.entries(item_dict)) {
        const command = `/give @s ${item} ${count}`;
        bot.chat(command);
        await new Promise(resolve => setTimeout(resolve, 500)); // Add a small delay to avoid spamming commands
    }
}

async function giveItemToPlayer(bot, target, type, count) {
    // target is a string, i.e. game ID of the player
    // @a = all players, @p = the nearest player (including self), @s = self
    if (typeof target !== "string") {
        throw new Error("target for /give must be a string");
    }
    if (typeof type !== "string") {
        throw new Error("item type for /give must be a string");
    }
    if (typeof count !== "number") {
        throw new Error("count for /give must be a number");
    }
    let inv_count = await getTotalCount(bot, type);
    if (inv_count < count) {
        bot.chat(`Not enough ${type} to give, need ${count} but only ${inv_count} in my inventory.`);
        return;
    }
    bot.chat(`/clear @s ${type} ${count}`);
    bot.chat(`/give ${target} ${type} ${count}`);
}

async function respawnAndClear(bot) {
    await bot.chat("/tp @a ~100 256 ~100");
    await bot.chat("/clear @a");
    await bot.chat("/gamemode survival");
    await bot.chat("/difficulty peaceful");
    await bot.chat("Teleported to new location and reset inventory.");
}