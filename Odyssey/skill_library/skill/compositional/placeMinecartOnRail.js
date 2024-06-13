async function placeMinecartOnRail(bot) {
    // check minecart
    const minecart = bot.inventory.findInventoryItem(mcData.itemsByName.minecart.id);
    if (!minecart) {
        bot.chat("No minecart found in inventory.");
        return;
    }
    // find rail
    const rail = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
        const rails = bot.findBlocks({
          matching: block => block.name === "rail",
          maxDistance: 32,
          count: 1
        });
        return rails.length >= 1 ? rails[0] : null;
      });
      if (!rail) {
        bot.chat("Could not find rail.");
        return;
      }
    // place the minecart
    // bot.chat(`found rail at ${rail}`);
    bot.chat(`/summon minecraft:minecart ${rail.x} ${rail.y} ${rail.z}`)
    bot.chat(`/clear @s minecraft:minecart 1`);
}