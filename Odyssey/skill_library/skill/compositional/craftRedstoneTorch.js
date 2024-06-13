async function craftRedstoneTorch(bot) {
    // check redstone and sticks
    let redstoneCount = bot.inventory.count(mcData.itemsByName.redstone.id);
    let sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);
    if (!redstoneCount) {
        await mineRedstoneOre(bot);
    }
    if (!sticksCount) {
        await craftSticks(bot);
    }
    await craftItem(bot, "redstone_torch", 1);
    bot.chat("Crafted redstone torch.");
  }