async function collectSugarCane(bot) {
    // Find sugar cane plants using the exploreUntil function
    const sugarCanePlants = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
      const sugarCanePlants = bot.findBlocks({
        matching: block => block.name === "sugar_cane",
        maxDistance: 32,
        count: 1
      });
      return sugarCanePlants.length >= 1 ? sugarCanePlants : null;
    });
    if (!sugarCanePlants) {
      bot.chat("Could not find sugar cane plants.");
      return;
    }
    for (const sugarCanePlant of sugarCanePlants) {
      const block = bot.blockAt(sugarCanePlant);
      await bot.dig(block);
      await bot.pathfinder.goto(new GoalBlock(sugarCanePlant.x, sugarCanePlant.y, sugarCanePlant.z));
    }
    bot.chat("sugar cane collected.");
}