async function catchFish(bot) {
    // Check if the bot has a fishing rod in its inventory
    let fishingRod = bot.inventory.findInventoryItem(mcData.itemsByName.fishing_rod.id);
    if (!fishingRod) {
        await craftFishingRod(bot);
        fishingRod = bot.inventory.findInventoryItem(mcData.itemsByName.fishing_rod.id);
    }
    // Find a nearby water block
    let waterBlock;
    while (!waterBlock) {
        waterBlock = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
            const foundWaterBlock = bot.findBlock({
                matching: mcData.blocksByName.water.id,
                maxDistance: 32
            });
            return foundWaterBlock;
        });
        if (!waterBlock) {
            bot.chat("No path to the water block. Trying to find another water block...");
        }
    }
    // Move to a block adjacent to the water block
    const adjacentBlock = waterBlock.position.offset(0, 1, 0);
    await bot.pathfinder.goto(new GoalBlock(adjacentBlock.x, adjacentBlock.y, adjacentBlock.z));

    // Look at the water block
    await bot.lookAt(waterBlock.position);

    // Equip the fishing rod
    await bot.equip(fishingRod, "hand");
    await bot.fish();
}