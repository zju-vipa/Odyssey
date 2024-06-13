async function craftLantern(bot) {
    // Check if there are enough torch and iron nuggets in the inventory
    let torchCount = bot.inventory.count(mcData.itemsByName.torch.id);
    const ironNuggetsCount = bot.inventory.count(mcData.itemsByName.iron_nugget.id);
    // If not enough torch or iron nuggets, collect the required items
    if (ironNuggetsCount < 8) {
      await craftIronNuggets(bot);
    }
    if (torchCount < 1) {
      await craftTorch(bot);
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
    // Craft a lantern using the crafting table
    await craftItem(bot, "lantern", 1);
    bot.chat("Crafted a lantern.");
  }