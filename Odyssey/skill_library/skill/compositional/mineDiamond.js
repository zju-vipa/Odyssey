async function mineDiamond(bot) {
    let ironPickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.iron_pickaxe.id);
    if (!ironPickaxe) {
      await craftIronPickaxe(bot);
      ironPickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.iron_pickaxe.id);
    }
    await bot.equip(ironPickaxe, "hand");
    const oreNames = ["diamond_ore", "deepslate_diamond_ore"];
    let y = bot.entity.position.y;
    let direction;
    if (y > 16) {
      direction = new Vec3(0, -1, 0);
    } else {
      direction = new Vec3(1, 0, 0);
    }
    // Find diamond_ore or deepslate_diamond_ore
    const oreBlock = await exploreUntil(bot, direction, 60, () => {
      return bot.findBlock({
        matching: block => oreNames.includes(block.name),
        maxDistance: 32
      });
    });
    // bot.chat(`${oreBlock}`);
    if (!oreBlock) {
      bot.chat("Could not find a diamond ore.");
      return;
    }
    await mineBlock(bot, oreBlock.name, 1);
    bot.chat("1 diamond mined.");
  }