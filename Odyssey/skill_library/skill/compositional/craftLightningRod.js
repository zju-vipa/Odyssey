async function craftLightningRod(bot) {
    // Smelt all raw copper first
    await smeltAllRawCopper(bot);
    // Check if there are enough copper ingots in the inventory
    let copperIngotsCount = bot.inventory.count(mcData.itemsByName.copper_ingot.id);
    // If not enough copper ingots, mine copper ores and smelt them into copper ingots
    while (copperIngotsCount < 3) {
      await mineCopperOre(bot);
      copperIngotsCount += 1;
    }
    await smeltAllRawCopper(bot);
    // Check if crafting table is in the inventory
    const craftingTableCount = bot.inventory.count(mcData.itemsByName.crafting_table.id);
    // If not, craft a crafting table
    if (craftingTableCount === 0) {
      await craftCraftingTable(bot);
    }
    // Place the crafting table near the bot
    const craftingTablePosition = await findSuitablePosition(bot);
    await placeItem(bot, "crafting_table", craftingTablePosition);
    // Craft a lightning rod using the crafting table
    await craftItem(bot, "lightning_rod", 1);
    bot.chat("Crafted a lightning rod.");
  }