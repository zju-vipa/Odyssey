async function craftTorches(bot) {
    // check coals and sticks
    let coalsCount = bot.inventory.count(mcData.itemsByName.coal.id);
    let sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);
    if (!coalsCount) {
        await mineFiveCoalOres(bot);
    }
    if (!sticksCount) {
        await craftSticks(bot);
    }
    await craftItem(bot, "torch", 1);
    bot.chat("4 torches crafted.");
  }