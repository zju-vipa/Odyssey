async function collectLavaWithBucket(bot) {
    // check bucket
    let bucket = bot.inventory.findInventoryItem(mcData.itemsByName.bucket.id);
    if (!bucket) {
        await craftBucket(bot);
    }
    // find lava
    const lavaBlock = bot.findBlock({
        matching: mcData.blocksByName.lava.id,
        maxDistance: 32
    });
    if (!lavaBlock) {
        bot.chat("No lava block found nearby. Exploring...");
        await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
        const foundlavaBlock = bot.findBlock({
            matching: mcData.blocksByName.lava.id,
            maxDistance: 32
        });
        return foundlavaBlock;
        });
    }

    await bot.equip(bucket, "hand");
    await bot.lookAt(lavaBlock.position);
    await bot.activateItem();
    bot.chat("lava collected with bucket.");
}