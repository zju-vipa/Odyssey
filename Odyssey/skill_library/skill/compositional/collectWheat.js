async function collectWheat(bot, pos = None) {
    if (pos) {
        await bot.pathfinder.goto(new GoalBlock(pos.x, pos.y, pos.z));
    }
    // Use the exploreUntil function to find wheat
    const ripe_wheat = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
        const wheat = bot.findBlocks({
            matching: block => block.name === "wheat" && block.getProperties().age === 7,
            maxDistance: 32,
            count: 1
        });
        return wheat.length >= 1 ? wheat : null;
    });
    if (!ripe_wheat) {
        bot.chat("Could not find ripe wheat. Plant seeds or wait for seeds to ripen first!");
        return;
    }
    const block = bot.blockAt(ripe_wheat[0]);
    // const blockProperties = block.getProperties();
    // bot.chat(`${blockProperties.age}`);
    // bot.chat(JSON.stringify(blockProperties));
    await bot.pathfinder.goto(new GoalBlock(ripe_wheat[0].x, ripe_wheat[0].y, ripe_wheat[0].z));
    await bot.dig(block);
  }