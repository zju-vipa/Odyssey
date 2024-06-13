async function goto(bot, x, y, z) {
    let pos_x = bot.entity.positon.x;
    let pos_y = bot.entity.positon.y;
    let pos_z = bot.entity.positon.z;
    while (Math.abs(pos_x - x) > 2 && Math.abs(pos_y - y) > 2 && Math.abs(pos_z - z) > 2) {
        pos_x = bot.entity.positon.x;
        pos_y = bot.entity.positon.y;
        pos_z = bot.entity.positon.z;
        await bot.pathfinder.goto(new GoalBlock(x, y, z));
    }
}