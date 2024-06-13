async function craftCobblestoneWall(bot) {
    // Check if there are enough cobblestones in the inventory
    let cobblestoneCount = bot.inventory.count(mcData.itemsByName.cobblestone.id);
    // If not enough cobblestones, collect some
    while (cobblestoneCount < 6) {
      await mineCobblestone(bot);
      cobblestoneCount = bot.inventory.count(mcData.itemsByName.cobblestone.id);
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
    // Craft a cobblestone_wall using the crafting table
    await craftItem(bot, "cobblestone_wall", 1);
    bot.chat("Crafted a cobblestone wall.");
  }