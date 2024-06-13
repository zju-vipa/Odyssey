#### Flow arrangement tables
|   |   |   |   |   |   |   | 7 |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   | 7 | 6 | 7 |   |   |   |   |   |   |
|   |   |   |   |   | 7 | 6 | 5 | 6 | 7 |   |   |   |   |   |
|   |   |   |   | 7 | 6 | 5 | 4 | 5 | 6 | 7 |   |   |   |   |
|   |   |   | 7 | 6 | 5 | 4 | 3 | 4 | 5 | 6 | 7 |   |   |   |
|   |   | 7 | 6 | 5 | 4 | 3 | 2 | 3 | 4 | 5 | 6 | 7 |   |   |
|   | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |   |
| 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|   | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |   |
|   |   | 7 | 6 | 5 | 4 | 3 | 2 | 3 | 4 | 5 | 6 | 7 |   |   |
|   |   |   | 7 | 6 | 5 | 4 | 3 | 4 | 5 | 6 | 7 |   |   |   |
|   |   |   |   | 7 | 6 | 5 | 4 | 5 | 6 | 7 |   |   |   |   |
|   |   |   |   |   | 7 | 6 | 5 | 6 | 7 |   |   |   |   |   |
|   |   |   |   |   |   | 7 | 6 | 7 |   |   |   |   |   |   |
|   |   |   |   |   |   |   | 7 |   |   |   |   |   |   |   |

| Range |        | Height in blocks |
|-------|--------|------------------|
| 1     | block  | 1                |
| 2     | blocks | 0.75-1           |
| 3     | blocks | 0.625-0.75       |
| 4     | blocks | 0.5-0.625        |
| 5     | blocks | 0.375-0.5        |
| 6     | blocks | 0.25-0.375       |
| 7     | blocks | 0.125-0.25       |

### Source blocks


This section is about the behavior and creation of source units of water.  For the removed block that created water sources, see Water Spawner.
A water source block is created from a flowing block that is horizontally adjacent to two or more other source blocks, and sitting on top of a solid block or another water source block. This allows water spawners to exist, in which a new source block immediately forms in the space left by removing a source block with a bucket. Pools of still water can be created by placing water source blocks in a confined area.

Water spawners can be constructed by arranging for two source blocks to flow into a third block. Each of the examples below require two source blocks, each on opposite ends of the hole, to create a renewable water source block in between.

While water source blocks only generate adjacent to solid blocks, they do not require a solid block to support them. Removing all adjacent blocks to a water source block only causes it to remain floating in the air.

In Java Edition, the formation of new water sources blocks can be disabled when the game rule waterSourceConversion is set to false.

- 2×2 water spawner (every corner is renewable)
- 3×1 water spawner (middle water block is renewable)
- L-shaped water spawner (corner water block is renewable)

A dispenser loaded with a filled bucket places a water source block in an empty block in front of it when activated. A dispenser loaded with an empty bucket and a water source right in front of it sucks the source into the bucket when activated.

In snowy biomes, water source blocks have a chance to turn into ice if directly under the sky. Ice blocks under brighter light levels melt back into water source blocks (except in the Nether). Ice reverts to water when broken, but only if there is a solid block under it.

### Current
The current in a water block determines both the direction it appears to flow and the direction an entity such as a player or boat is pushed from that block.

Water with a current pushes players and mobs at a speed of about 1.39 meters per second, or 25 blocks every 18 seconds. Players that are in creative flying mode don’t get pushed.‌[Java Edition  only][6]

The horizontal current in a water block is based on a vector sum of the flows to and from that block from its four horizontal neighbors. For example, if a block receives water from the north and sends it both south and east, but borders a solid block on its west edge, then a south-southeast current exits from that block, because 2 southward flows (in and out) are combined with 1 eastward flow (out). Thus, 16 horizontal directions are possible. If a branch in a channel is 2 blocks wide at its entrance, then entities float into it rather than continuing in a straight line.

Water blocks can create a downward current. A downward current in a water block is caused by the block below it. Most blocks that do not have a solid upper face cause downward current on above water blocks. Also, ice and falling water blocks (blocks created by spreading downward) cause downward current on the water block above. Falling water blocks have a downward current by default.

