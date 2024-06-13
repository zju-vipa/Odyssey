async function collectFlowers(bot) {
    const flowerNames = ["dandelion", "poppy", "blue_orchid", "allium", "azure_bluet", 
                     "red_tulip", "orange_tulip", "white_tulip", "pink_tulip",
                     "oxeye_daisy", "cornflower", "lily_of_the_valley", "wither_rose", "torchflower", 
                     "sunflower", "lilac", "rose_bush", "peony", "pitcher_plant"];
    // Find 10 flowers
    const flowers = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
        const flowers = bot.findBlocks({
          matching: block => flowerNames.includes(block.name),
          maxDistance: 32,
          count: 10
        });
        return flowers.length >= 1 ? flowers : null;
      });
    if (!flowers) {
        bot.chat("Could not find flowers.");
        return;
    }
    for (const flower of flowers) {
        const block = bot.blockAt(flower);
        await bot.dig(block);
    }
    await bot.chat("Collected flowers.")
}