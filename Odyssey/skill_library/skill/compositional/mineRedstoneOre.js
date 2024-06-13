async function mineRedstoneOre(bot) {
    let ironPickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.iron_pickaxe.id);
    if (ironPickaxe) {
      await bot.equip(ironPickaxe, "hand");
    } else {
      await craftIronPickaxe(bot);
      ironPickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.iron_pickaxe.id);
      await bot.equip(ironPickaxe, "hand");
    }
    // Find 1 redstone_ore block
    const redstoneOres = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
      const redstoneOres = bot.findBlocks({
        matching: block => block.name === "redstone_ore",
        maxDistance: 32,
        count: 1
      });
      return redstoneOres.length >= 1 ? redstoneOres : null;
    });
    if (!redstoneOres) {
      bot.chat("Could not find enough redstone ores.");
      return;
    }
  
    // Mine the 1 redstone_ore block
    await mineBlock(bot, "redstone_ore", 1);
    bot.chat("1 redstone ore mined.");
  }