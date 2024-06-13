async function mineCopperOre(bot) {
    const ironPickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.iron_pickaxe.id);
    if (ironPickaxe) {
      await bot.equip(ironPickaxe, "hand");
    } else {
      // Equip the stone pickaxe
      const stonePickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.stone_pickaxe.id);
      if (!stonePickaxe) {
        await craftStonePickaxe(bot);
        const stonePickaxe1 = bot.inventory.findInventoryItem(mcData.itemsByName.stone_pickaxe.id);
        await bot.equip(stonePickaxe1, "hand");
      }
      await bot.equip(stonePickaxe, "hand");
    }
  
    // Find 1 copper_ore block
    const copperOres = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
      const copperOres = bot.findBlocks({
        matching: block => block.name === "copper_ore",
        maxDistance: 32,
        count: 1
      });
      return copperOres.length >= 1 ? copperOres : null;
    });
    if (!copperOres) {
      bot.chat("Could not find enough copper ores.");
      return;
    }
  
    // Mine the 1 copper_ore block
    await mineBlock(bot, "copper_ore", 1);
    bot.chat("1 copper ore mined.");
  }