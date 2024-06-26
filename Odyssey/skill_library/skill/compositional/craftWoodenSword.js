async function craftWoodenSword(bot) {
    const sticksCount = bot.inventory.count(mcData.itemsByName.stick.id);
    // Check if there are enough planks and sticks in the inventory
    if (sticksCount < 1) {
      await craftSticks(bot);
    }
    let totalPlanksCount = await getPlanksCount(bot);
    if (totalPlanksCount < 2) {
      await craftWoodenPlanks(bot);
    }

    // Check if crafting table is in the inventory
    const craftingTableCount = bot.inventory.count(mcData.itemsByName.crafting_table.id);
    // If not, craft a crafting table
    if (craftingTableCount === 0) {
      await craftCraftingTable(bot);
    }
    // Place the crafting table near the bot
    const craftingTablePosition = await findSuitablePosition(bot);
    await placeItem(bot, "crafting_table", craftingTablePosition);
  
    // Craft a wooden sword using the crafting table
    await craftItem(bot, "wooden_sword", 1);
    bot.chat("Crafted a wooden sword.");
  }