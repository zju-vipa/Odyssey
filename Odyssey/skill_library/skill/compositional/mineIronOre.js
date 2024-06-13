async function mineIronOre(bot) {
    const ironPickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.iron_pickaxe.id);
    if (ironPickaxe) {
      await bot.equip(ironPickaxe, "hand");
    } else {
      // Equip the stone pickaxe
      let stonePickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.stone_pickaxe.id);
      if (!stonePickaxe) {
        await craftStonePickaxe(bot);
        let stonePickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.stone_pickaxe.id);
        await bot.equip(stonePickaxe, "hand");
      } else {
        await bot.equip(stonePickaxe, "hand");
      }
    }
  
    // Find 1 iron_ore block
    const ironOres = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
      const ironOres = bot.findBlocks({
        matching: block => block.name === "iron_ore" || block.name === "deepslate_iron_ore",
        maxDistance: 32,
        count: 1
      });
      return ironOres.length >= 1 ? ironOres : null;
    });
    if (!ironOres) {
      bot.chat("Could not find iron ore.");
      return;
    }
  
    // Mine the 1 iron_ore block
    await mineBlock(bot, "iron_ore", 1);
    bot.chat("1 iron ore mined.");
  }