async function craftSandstoneSlab(bot) {
    // Check if there are enough sandstones in the inventory
    let cutSandstoneCount = bot.inventory.count(mcData.itemsByName.cut_sandstone.id);
    // If not enough sandstones, collect some
    if (cutSandstoneCount < 3) {
      await craftCutSandstone(bot);
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
    // Craft sandstone_slab using the crafting table
    await craftItem(bot, "sandstone_slab", 1);
    bot.chat("Crafted sandstone slabs.");
  }