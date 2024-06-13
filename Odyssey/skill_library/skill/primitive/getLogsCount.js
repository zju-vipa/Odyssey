async function getLogsCount(bot) {
    const logNames = ["oak_log", "birch_log", "spruce_log", "jungle_log", "acacia_log", "dark_oak_log", "mangrove_log"];
    let totalLogCount = 0;
    for (const logName of logNames) {
      const logId = mcData.itemsByName[logName].id;
      const logCount = bot.inventory.count(logId);
      totalLogCount += logCount;
    }
    return totalLogCount;
}