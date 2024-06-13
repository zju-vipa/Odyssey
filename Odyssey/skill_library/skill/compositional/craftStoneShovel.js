async function craftStoneShovel(bot) {
    // Check if there are enough cobblestone and sticks in the inventory
    let cobblestoneCount = bot.inventory.count(mcData.itemsByName.cobblestone.id);
    const sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);
    // If not enough cobblestone or sticks, collect the required items
    if (sticksCount < 2) {
      await craftSticks(bot);
      bot.chat("Crafted sticks.");
    }
    if (cobblestoneCount < 1) {
      await mineCobblestone(bot);
    }
    // Check if crafting table is in the inventory
    const craftingTableCount = bot.inventory.count(
      mcData.itemsByName.crafting_table.id
    );
    // If not, craft a crafting table
    if (craftingTableCount === 0) {
      await craftCraftingTable(bot);
    }
    // Place the crafting table near the bot
    const craftingTablePosition = await findSuitablePosition(bot);
    await placeItem(bot, "crafting_table", craftingTablePosition);
    // Craft a stone shovel using the crafting table
    await craftItem(bot, "stone_shovel", 1);
    bot.chat("Crafted a stone shovel.");
  }