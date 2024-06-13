async function mineEmerald(bot) {
    let diamondPickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.diamond_pickaxe.id);
    let ironPickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.iron_pickaxe.id);
    if (diamondPickaxe) {
        await bot.equip(diamondPickaxe, "hand");
    } else if (ironPickaxe) {
        await bot.equip(ironPickaxe, "hand");
    } else {
      await craftIronPickaxe(bot);
      ironPickaxe = bot.inventory.findInventoryItem(mcData.itemsByName.iron_pickaxe.id);
      await bot.equip(ironPickaxe, "hand");
    }
    const oreNames = ["emerald_ore", "deepslate_emerald_ore"];
    let y = bot.entity.position.y;
    let direction;
    if (y > 16) {
      direction = new Vec3(0, -1, 0);
    } else {
      direction = new Vec3(1, 0, 0);
    }
    // Find emerald_ore or deepslate_emerald_ore
    const oreBlock = await exploreUntil(bot, direction, 60, () => {
      return bot.findBlock({
        matching: block => oreNames.includes(block.name),
        maxDistance: 32
      });
    });
    // bot.chat(`${oreBlock}`);
    if (!oreBlock) {
      bot.chat("Could not find a emerald ore.");
      return;
    }
    await mineBlock(bot, oreBlock.name, 1);
    bot.chat("1 emerald mined.");
  }