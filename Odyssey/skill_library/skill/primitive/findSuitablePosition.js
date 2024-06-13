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