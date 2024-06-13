async function craftRedstoneBlock(bot) {
    // Check if there are enough redstone in the inventory
    let redstoneCount = bot.inventory.count(mcData.itemsByName.redstone.id);
    // If not enough redstone, mine some
    while (redstoneCount < 9) {
      await mineRedstoneOre(bot);
      redstoneCount = bot.inventory.count(mcData.itemsByName.redstone.id);
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
    // Craft a redstone block using the crafting table
    await craftItem(bot, "redstone_block", 1);
    bot.chat("Crafted a redstone block.");
}