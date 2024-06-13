async function takeAndMoveMinecart(bot) {
    // find minecart
    let minecart = await exploreUntil(bot, new Vec3(1, 0, 1), 60, () => {
        let minecart = bot.nearestEntity(entity => {
          return entity.name === "minecart" && entity.position.distanceTo(bot.entity.position) < 32;
        });
        return minecart;
      });
      if (!minecart) {
        bot.chat("Could not find a minecart.");
        return;
      }
    await bot.pathfinder.goto(new GoalBlock(minecart.position.x, minecart.position.y, minecart.position.z));
    bot.chat(`${minecart.position}`);
    await bot.activateEntity(minecart);
    // move the minecart along the rails
    let lastPosition = bot.entity.position.clone();
    // todo: check where the bot is looking at
    do {
        let forward = minecart.velocity.z > 0 ? 1 : -1;
        let left = minecart.velocity.x > 0 ? 1 : -1;
        bot.chat(`minecart.velocity: ${minecart.velocity}, next direction: (x, z) = (${left}, ${forward})`);
        await bot.moveVehicle(left, forward);

        // check if the position has changed
        if (lastPosition.equals(bot.entity.position)) {
            break; // exit the loop if the position has not changed
        }
        lastPosition = bot.entity.position.clone();
    } while (true)

    // dismount from the minecart
    await bot.dismount();
}