async function mineLapisLazuliOre(bot) {
    // Equip the iron pickaxe or stone pickaxe
    let ironPickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.iron_pickaxe.id);
    let stonePickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.stone_pickaxe.id);
    if (ironPickaxe) {
        await bot.equip(ironPickaxe, "hand");
    } else if (stonePickaxe) {
        await bot.equip(stonePickaxe, "hand");
    } else {
        await craftStonePickaxe(bot);
        stonePickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.stone_pickaxe.id);
        await bot.equip(stonePickaxe, "hand");
    }
  
    // Find 1 lapis_lazuli_ore block
    const lapisOres = await exploreUntil(bot, new Vec3(1, -1, 1), 60, () => {
      const lapisOres = bot.findBlocks({
        matching: block => block.name === "lapis_ore",
        maxDistance: 32,
        count: 1
      });
      return lapisOres.length >= 1 ? lapisOres : null;
    });
    if (!lapisOres) {
      bot.chat("Could not find lapis lazuli ores.");
      return;
    }
  
    // Mine the 1 lapis_lazuli_ore blocks
    await mineBlock(bot, "lapis_ore", 1);
    bot.chat("1 lapis lazuli ores mined.");
  }