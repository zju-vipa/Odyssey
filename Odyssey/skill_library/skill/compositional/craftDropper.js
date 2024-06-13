async function craftDropper(bot) {
    // check redstone and cobblestones
    let redstoneCount = bot.inventory.count(mcData.itemsByName.redstone.id);
    let cobblestonesCount = bot.inventory.count(mcData.itemsByName.cobblestone.id);
    if (!redstoneCount) {
        await mineRedstoneOre(bot);
    }
    if (cobblestonesCount < 7) {
        await collectCobblestone(bot);
        cobblestonesCount = bot.inventory.count(mcData.itemsByName.cobblestone.id);
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
    await craftItem(bot, "dropper", 1);
    bot.chat("Crafted a dropper.");
  }