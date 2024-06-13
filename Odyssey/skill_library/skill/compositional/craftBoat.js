async function craftBoat(bot) {
    // Check if there are enough planks in the inventory
    let planksCount = await getPlanksCount(bot);
    bot.chat(`inventory planks count: ${planksCount}`);
    // If not, craft planks from logs
    while (planksCount < 5) {
      await craftWoodenPlanks(bot);
      planksCount = await getPlanksCount(bot);
      bot.chat(`inventory planks count: ${planksCount}`);
    }
    // check wooden_shovel
    let woodenShovel = bot.inventory.findInventoryItem(mcData.itemsByName.wooden_shovel.id);
    if (!woodenShovel) {
        await craftWoodenShovel(bot);
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
    // Craft a boat using the crafting table
    const plankNames = ["oak_planks", "birch_planks", "spruce_planks", "jungle_planks", "acacia_planks", "dark_oak_planks", "mangrove_planks"];
    let type;
    for (const plankName of plankNames) {
      const plankId = mcData.itemsByName[plankName].id;
      const plankCount = bot.inventory.count(plankId);
      if (plankCount >= 5)
        type = plankName.match(/(\w+)_planks/)[1];
    }
    await craftItem(bot, type + "_boat", 1);
    bot.chat("Crafted a boat.");
  }