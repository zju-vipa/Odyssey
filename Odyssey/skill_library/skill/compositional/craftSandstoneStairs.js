async function craftSandstoneStairs(bot) {
    // Check if there are enough sandstones in the inventory
    let sandstoneCount = bot.inventory.count(mcData.itemsByName.sandstone.id);
    // If not enough sandstones, collect some
    if (sandstoneCount < 6) {
      await collectSandstone(bot);
      sandstoneCount = bot.inventory.count(mcData.itemsByName.sandstone.id);
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
    // Craft sandstone_stairs using the crafting table
    await craftItem(bot, "sandstone_stairs", 1);
    bot.chat("Crafted sandstone stairs.");
  }