async function craftBowl(bot) {
    // Check if there are enough planks in the inventory
    let planksCount = await getPlanksCount(bot);
    // If not enough planks, collect some
    if (planksCount < 3) {
      await craftWoodenPlanks(bot);
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
    // Craft a bowl using the crafting table
    await craftItem(bot, "bowl", 1);
    bot.chat("Crafted a bowl.");
  }