async function collectItem(bot, count = 1, type, func, tool, recursive = true) {
    let original_count = await getTotalCount(bot, type);
    let inv_count = original_count;
    bot.chat(`Recursively executing collectItem(bot, ${count}, ${type}, ${func}, ${tool})...`);
    while (inv_count - original_count < count) {
        await equipBestTool(bot, tool);
        if (func == "kill") {
            let mob_list = await preCollect(type);
            bot.chat(`${JSON.stringify(mob_list)}`);
            // find entity first
            const mob = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
                const mob = bot.nearestEntity(entity => {
                    return mob_list.includes(entity.name) && entity.position.distanceTo(bot.entity.position) < 32;
                });
                return mob;
            });
            if (!mob) {
                bot.chat("Could not find a mob.");
                return false;
            }
            // kill the mob using the sword
            await equipBestTool(bot, tool);
            await killMob(bot, mob.name, 300);
            // collect the dropped items
            await bot.pathfinder.goto(new GoalBlock(mob.position.x, mob.position.y, mob.position.z));
            bot.chat("Collected dropped items.");
        } else if (func == "collect_mine") {
            // find block first
        }
        inv_count = await getTotalCount(bot, type);
    }
    return true;
}