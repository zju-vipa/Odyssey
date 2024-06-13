async function collectWaterWithBucket(bot) {
  // check bucket
  let bucket = bot.inventory.findInventoryItem(mcData.itemsByName.bucket.id);
  if (!bucket) {
      await craftBucket(bot);
  }
  // find water
  const waterBlock = bot.findBlock({
    matching: mcData.blocksByName.water.id,
    maxDistance: 32
  });
  if (!waterBlock) {
    bot.chat("No water block found nearby. Exploring...");
    await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
      const foundWaterBlock = bot.findBlock({
        matching: mcData.blocksByName.water.id,
        maxDistance: 32
      });
      return foundWaterBlock;
    });
  }
  await bot.pathfinder.goto(new GoalBlock(waterBlock.position.x, waterBlock.position.y, waterBlock.position.z))
  await bot.equip(bucket, "hand");
  await bot.lookAt(waterBlock.position);
  await bot.activateItem();
  bot.chat("Water collected with bucket.");
}