async function craftSticks(bot) {
    const requiredPlanks = 2;
    let totalPlanksCount = await getPlanksCount(bot);
    // If not enough planks
    if (totalPlanksCount < requiredPlanks) {
      await craftWoodenPlanks(bot);
      // bot.chat("Planks crafted.");
    }
    await craftItem(bot, "stick", 1);
    bot.chat("4 sticks crafted.");
  }