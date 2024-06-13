async function mineGoldOre(bot) {
    let ironPickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.iron_pickaxe.id);
    if (ironPickaxe) {
      await bot.equip(ironPickaxe, "hand");
    } else {
      await craftIronPickaxe(bot);
      ironPickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.iron_pickaxe.id);
      await bot.equip(ironPickaxe, "hand");
    }
    // Find 1 gold_ore block
    const goldOres = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
      const goldOres = bot.findBlocks({
        matching: block => block.name === "gold_ore",
        maxDistance: 32,
        count: 1
      });
      return goldOres.length >= 1 ? goldOres : null;
    });
    if (!goldOres) {
      bot.chat("Could not find enough gold ores.");
      return;
    }
  
    // Mine the 1 gold_ore block
    await mineBlock(bot, "gold_ore", 1);
    bot.chat("1 gold ore mined.");
  }