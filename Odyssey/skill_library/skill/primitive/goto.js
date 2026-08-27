async function goto(bot, x, y, z, timeout = 30000) {
    const coordinates = [x, y, z];
    if (!coordinates.every(Number.isFinite)) {
        throw new Error("[goto] x, y and z must be finite numbers");
    }
    if (!Number.isFinite(timeout) || timeout <= 0) {
        throw new Error("[goto] timeout must be a positive finite number");
    }

    // GoalNear floors its coordinates to Minecraft's block grid.  Use that
    // same coordinate system for both the early return and the postcondition.
    const target = new Vec3(Math.floor(x), Math.floor(y), Math.floor(z));
    const tolerance = 2;
    const distanceToTarget = () => {
        const position = bot.entity?.position;
        if (
            !position ||
            ![position.x, position.y, position.z].every(Number.isFinite)
        ) {
            throw new Error("[goto] bot position must be finite");
        }
        const blockPosition = new Vec3(
            Math.floor(position.x),
            Math.floor(position.y),
            Math.floor(position.z)
        );
        return blockPosition.distanceTo(target);
    };

    if (distanceToTarget() <= tolerance) {
        return true;
    }

    let timeoutHandle;
    try {
        await Promise.race([
            bot.pathfinder.goto(new GoalNear(x, y, z, tolerance)),
            new Promise((_, reject) => {
                timeoutHandle = setTimeout(() => {
                    reject(
                        new Error(
                            `[goto] timed out after ${timeout}ms while moving to (${x}, ${y}, ${z})`
                        )
                    );
                }, timeout);
            }),
        ]);
    } catch (error) {
        bot.pathfinder.setGoal?.(null);
        if (error.message?.startsWith("[goto]")) {
            throw error;
        }
        throw new Error(
            `[goto] pathfinder failed while moving to (${x}, ${y}, ${z}): ${error.message}`
        );
    } finally {
        clearTimeout(timeoutHandle);
    }

    const finalDistance = distanceToTarget();
    if (finalDistance > tolerance) {
        throw new Error(
            `[goto] pathfinder stopped at block-grid distance ${finalDistance.toFixed(2)} from (${x}, ${y}, ${z})`
        );
    }
    return true;
}
