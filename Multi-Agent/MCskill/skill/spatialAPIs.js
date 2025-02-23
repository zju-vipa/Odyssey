async function findSuitablePosition(bot) {
  const offsets = [
      new Vec3(1, 0, 0),
      new Vec3(-1, 0, 0),
      new Vec3(0, 0, 1),
      new Vec3(0, 0, -1),
      new Vec3(1, 0, 1),
      new Vec3(-1, 0, 1),
      new Vec3(-1, 0, 1),
      new Vec3(-1, 0, -1),
      new Vec3(1, 1, 0),
      new Vec3(-1, 1, 0),
      new Vec3(0, 1, 1),
      new Vec3(0, 1, -1),
      new Vec3(1, 1, 1),
      new Vec3(-1, 1, 1),
      new Vec3(-1, 1, 1),
      new Vec3(-1, 1, -1),
      new Vec3(1, -1, 0),
      new Vec3(-1, -1, 0),
      new Vec3(0, -1, 1),
      new Vec3(0, -1, -1),
      new Vec3(1, -1, 1),
      new Vec3(-1, -1, 1),
      new Vec3(-1, -1, 1),
      new Vec3(-1, -1, -1),
      new Vec3(0, 2, 0)
  ]
  for (const offset of offsets) {
      const pos = bot.entity.position.offset(offset.x, offset.y, offset.z);
      const block = bot.blockAt(pos);
      const ref = await checkNoAdjacentBlock(bot, ["air", "water"], pos.x, pos.y, pos.z);
      // bot.chat(`offset: ${offset}; block name: ${block.name}; ref block: ${ref}`);
      if ((block.name == "air" || block.name == "water") && ref) {
        return pos;
    }
  }
  return null;
}

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

async function checkAdjacentBlock(bot, types, x, y, z) {
  // check blocks adjacent to the block at (x, y, z)
  // return true if any of the adjacent blocks match the specified types
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
      if (types.includes(block.name)) {
          return true;
      }
  }
  return false;
}

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
