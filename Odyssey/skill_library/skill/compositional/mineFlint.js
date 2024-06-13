async function mineFlint(bot) {
    let ironShovel = bot.inventory.findInventoryItem(mcData.itemsByName.iron_shovel.id);
    let stoneShovel = bot.inventory.findInventoryItem(mcData.itemsByName.stone_shovel.id);
    let woodenShovel = bot.inventory.findInventoryItem(mcData.itemsByName.wooden_shovel.id);
    const flintsCount = bot.inventory.count(mcData.itemsByName.flint.id);
    let newFlintsCount = bot.inventory.count(mcData.itemsByName.flint.id);
    if (ironShovel) {
        await bot.equip(ironShovel, "hand");
    } else if (stoneShovel) {
        await bot.equip(stoneShovel, "hand");
    } else if (woodenShovel) {
        await bot.equip(woodenShovel, "hand");
    } else {
        await craftWoodenShovel(bot);
        woodenShovel = bot.inventory.findInventoryItem(mcData.itemsByName.wooden_shovel.id);
        await bot.equip(woodenShovel, "hand");
    }
    // find gravel
    await exploreUntil(bot, new Vec3(0, -1, 0), 60, () => {
      const foundGravel = bot.findBlock({
        matching: mcData.blocksByName.gravel.id,
        maxDistance: 32
      });
      return foundGravel;
    });
    // mine gravel until flint count increase 1
    while (newFlintsCount == flintsCount) {
        await mineBlock(bot, "gravel", 1);
        newFlintsCount = bot.inventory.count(mcData.itemsByName.flint.id);
    }
    bot.chat("1 flint mined.");
  }