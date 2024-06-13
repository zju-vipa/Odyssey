async function checkNoAdjacentBlock(bot, types, x, y, z) {
    // check adjacent blocks of block at (x, y, z)
    // return true if not all adjacent blocks are within the specified type
    const adjacentVec = [
        new Vec3(1, 0, 0),
        new Vec3(-1, 0, 0),
        new Vec3(0, 0, 1),
        new Vec3(0, 0, -1),
        new Vec3(0, 1, 0),
        new Vec3(0, -1, 0)
    ]
    for (const offset of adjacentVec) {
        const pos = new Vec3(x + offset.x, y + offset.y, z + offset.z);
        const block = bot.blockAt(pos);
        if (!types.includes(block.name)) {
            return true;
        }
    }
    return false;
}