async function checkNearbyBlock(bot, types, x, y, z, r) {
    // check blocks in a radius around the block at (x, y, z)
    // return true if any block within the radius matches the specified types
    const minX = x - r;
    const maxX = x + r;
    const minZ = z - r;
    const maxZ = z + r;
    for (let i = minX; i <= maxX; i++) {
        for (let j = minZ; j <= maxZ; j++) {
            const pos = new Vec3(i, y, j);
            const block = bot.blockAt(pos);
            if (types.includes(block.name)) {
                return true;
            }
        }
    }
    return false;
}
