function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function constructRec(bot, start_pos=new Vec3(0, 0, 0), end_pos=new Vec3(0, 0, 0), block_type, mode="place") {
    if (mode == "command") {
        await bot.chat(`/fill ${start_pos.x} ${start_pos.y} ${start_pos.z} ${end_pos.x} ${end_pos.y} ${end_pos.z} ${block_type}`);
    } else if (mode == "place") {
        // Get the min and max coordinates for each axis
        const minX = Math.min(start_pos.x, end_pos.x);
        const maxX = Math.max(start_pos.x, end_pos.x);
        const minY = Math.min(start_pos.y, end_pos.y);
        const maxY = Math.max(start_pos.y, end_pos.y);
        const minZ = Math.min(start_pos.z, end_pos.z);
        const maxZ = Math.max(start_pos.z, end_pos.z);
        
        // Iterate over all positions within the rectangular prism
        for (let x = minX; x <= maxX; x++) {
            for (let y = minY; y <= maxY; y++) {
                for (let z = minZ; z <= maxZ; z++) {
                    const pos = new Vec3(x, y, z);
                    await placeItem(bot, block_type, pos);
                    await sleep(2000); // Sleep for 2000ms between each placement
                    console.log('Slept for 2 second');
                }
            }
        }
    }
    await bot.chat(`Construction completed.`);
}
