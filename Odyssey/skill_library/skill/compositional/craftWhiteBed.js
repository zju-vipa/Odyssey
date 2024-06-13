async function craftWhiteBed(bot) {
    // Check if there are enough planks and wools in the inventory
    let planksCount = await getPlanksCount(bot);
    let woolsCount = bot.inventory.count(mcData.itemsByName.white_wool.id);
    // If not, craft planks from logs
    if (planksCount < 3) {
        await craftWoodenPlanks(bot);
    }
    while (woolsCount < 3) {
        await killOneSheep(bot);
        woolsCount = bot.inventory.count(mcData.itemsByName.white_wool.id);
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
    // Craft a bed using the crafting table
    await craftItem(bot, "white_bed", 1);
    bot.chat("Crafted a white bed.");
  }