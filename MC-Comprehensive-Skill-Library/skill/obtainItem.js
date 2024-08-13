async function obtainItem(bot, count = 1, type) {
    let res = false;
    bot.chat(`Recursively executing obtainItem(bot, ${count}, ${type})...`);
    while (!res) {
        let func_name = await getFunc(type);
        if (func_name == "craft") {
            res =await craftItem(bot, count, type);
        } else if (func_name == "mine") {
            // specify mine or collect: mine_until?
            res = await mineItem(bot, count, type);
        } else if (func_name == "smelt") {
            res = await smeltItem(bot, count, type);
        } else if (func_name == "kill") {
            res =await collectItem(bot, count, type, "kill", "sword");
        } else if (func_name == "collect_mine") {
            res =await collectItem(bot, count, type, "collect_mine");
        }
    }
    return res;
}