async function checkBlockAbove(bot, type, position) {
    // check block above the block at position
    // return true if the above block match the specified type
    // return if position is not Vec3
    if (!(position instanceof Vec3)) {
        throw new Error(`position must be a Vec3`);
    }
    const pos = position.plus(new Vec3(0, 1, 0));
    const block = bot.blockAt(pos);
    if (type == block.name) {
        // bot.chat(`block at ${pos} is ${type}.`);
        return true;
        
    }
    return false;
}