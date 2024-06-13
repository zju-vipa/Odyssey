async function checkBlocksAround(bot, type, position) {
    // check blocks around the block at position
    // return true if any of the around blocks match the specified type
    // return if position is not Vec3
    if (!(position instanceof Vec3)) {
        throw new Error(`position must be a Vec3`);
    }
    const adjacentVec = [
        new Vec3(1, 0, 0),
        new Vec3(-1, 0, 0),
        new Vec3(0, 0, 1),
        new Vec3(0, 0, -1)
    ]
    for (const offset of adjacentVec) {
        const pos = position.plus(offset);
        const block = bot.blockAt(pos);
        if (type == block.name) {
            // bot.chat(`block at ${position} is arounded by ${type}.`);
            return true;
        }
    }
    return false;
}