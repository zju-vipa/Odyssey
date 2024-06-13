async function mineAmethystCluster(bot) {
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
    
    await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
      const foundAmethystCluster = bot.findBlock({
        matching: mcData.blocksByName.amethyst_cluster_ore.id,
        maxDistance: 32
      });
      return foundAmethystCluster;
    });
    await mineBlock(bot, "amethyst_cluster", 1);
    bot.chat("1 amethyst_cluster mined.");
  }