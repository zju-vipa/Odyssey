async function hoeFarmland(bot) {
    if (await equipHoe(bot)) {
        // find water
        const water = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
            const water = bot.findBlocks({
                matching: block => block.name === "water",
                maxDistance: 2,
                count: 1
            });
            return water.length >= 1 ? water : null;
        });
        if (!water) {
            bot.chat("No water nearby.");
            return;
        }
        // find dirt or grass_block near water
        const dirtNearWater = bot.findBlocks({
            matching: block => (block.name === "dirt" ||  block.name === "grass_block"),
            maxDistance: 8,
            count: 60
        });
        // hoe a farmland
        for (pos of dirtNearWater) {   
            await equipHoe(bot);
            const farmland = await bot.blockAt(pos);
            // if there's air above this block and water near this block
            if (await checkBlockAbove(bot, "air", pos) && await checkBlocksAround(bot, "water", pos)) {
                await bot.lookAt(pos);
                await bot.activateBlock(farmland);
                bot.chat(`hoed block at ${pos}`);
            }
        }
    } else {
        bot.chat("No hoe in inventory. Craft a hoe first!");
        return;
    }
}