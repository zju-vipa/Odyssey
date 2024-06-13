async function getPlanksCount(bot) {
    const plankNames = ["oak_planks", "birch_planks", "spruce_planks", "jungle_planks", "acacia_planks", "dark_oak_planks", "mangrove_planks"];
    let totalPlanksCount = 0;
    for (const plankName of plankNames) {
      const plankId = mcData.itemsByName[plankName].id;
      const plankCount = bot.inventory.count(plankId);
      totalPlanksCount += plankCount;
    }
    return totalPlanksCount;
}