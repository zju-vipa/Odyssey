async function placeWater(bot) {
    // Check water
    const waterBucket = bot.inventory.findInventoryItem(mcData.itemsByName.water_bucket.id);
    if (!waterBucket) {
        bot.chat("No water_bucket found in inventory.");
        return;
    }
    // Place the water
    const waterPosition = bot.entity.position;
    await bot.equip(waterBucket, "hand");
    await bot.lookAt(waterPosition);
    await bot.activateItem();
    bot.chat("water placed.");
}