# Water
Water is a fluid that naturally generates abundantly in the Overworld.

## Contents
- 1 Obtaining
	- 1.1 Natural generation
- 2 Usage
	- 2.1 Appearance
	- 2.2 Swimming
	- 2.3 Spreading
		- 2.3.1 Flow arrangement tables
	- 2.4 Source blocks
	- 2.5 Current
	- 2.6 Light
	- 2.7 Color
		- 2.7.1 Java Edition
		- 2.7.2 Bedrock Edition
	- 2.8 Water and lava
	- 2.9 Interactions with mobs
		- 2.9.1 Direct contact
		- 2.9.2 Drowning
	- 2.10 Slower mining speed
	- 2.11 Explosions
	- 2.12 Hardening concrete powder
	- 2.13 Sponges
	- 2.14 Dripping
	- 2.15 Vertical transport
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
	- 4.3 Fluid states
- 5 Achievements
- 6 Advancements
- 7 History
	- 7.1 Data history
- 8 Issues
- 9 Trivia
- 10 Gallery
	- 10.1 Textures
	- 10.2 Screenshots
- 11 See also
- 12 References
- 13 External links

## Obtaining
Water can be collected by using a bucket on a water source block or a full water cauldron, creating a water bucket.

In Java Edition, water does not have a direct item form, but in Bedrock Edition it may be obtained as an item via inventory editing or add-ons.

### Natural generation
Water naturally generates in the Overworld to form oceans, rivers and springs. The water level is at layer 63 near oceans and rivers, but changes depending on location due to the aquifer system, filling some carvers, noise caves and canyons with water at different levels. Water also generates as small puddles on the floor next to dripstone clusters, and as clay pools on the floor of lush caves.

Water also generates in villages, desert wells, strongholds, woodland mansions, ancient cities and ocean monuments. 

Water never generates in the Nether and instantly disappears if placed there with a water bucket. However, water can exist in the Nether in a cauldron. Water can also be placed in the Nether using commands such as /setblock and /fill. Although it does not naturally generate there, water can be placed and function normally in the End.

In Bedrock Edition, water also generates as part of ocean ruins with loot chests, but only two water blocks generate: 

- One water block generates inside the loot chest, making it awaterloggedloot chest.
- The other water block generates on top of the loot chest.

These water blocks generate even if the ruin is located on the surface.[1] This is not the case in Java Edition; if an underwater ruin generates on the surface, no water generates.[2] This also happens with shipwrecks.

Water spends most of its time as stationary, rather than flowing – regardless of its level, or whether it contains a current downward or to the side. When specifically triggered by a block update, water changes to 'flowing', updates its level, then changes back to stationary. Water springs are generated as flowing, and oceans, and rivers are generated as stationary. This happens before most types of generated structure are created, and the main cause of water "glitches" is that generated structures do not trigger a block update to let water flow into them.

## Usage
### Appearance
Water uses a translucent animated texture that is tinted differently in different biomes. In Java Edition, water in cauldrons is completely opaque.[3]

Unlike other translucent blocks such as ice, stained glass and tinted glass, water shows the opposite sides of its external planes when viewed from within and from outside.[4] However, it applies only to the top plane and four side planes; the bottom face is always unseen from above.[5]

### Swimming
Main article: Swimming
The button for swimming is the same as the button for jumping; non-swimming players and mobs sink slowly in water. Holding the swim button raises the player through the water, and when the surface is reached, the player bobs up and down. The crouch button can be used to sink faster. The sprint button can be used to put the player in "swim mode" when the player is completely submerged in water. When in swim mode, the player is horizontal and one block high. The player has an arm-waving animation when viewed in third person or by other players.

Swimming in water is considerably slower against currents (see Current below), but faster when going with the current.

Most mobs that can stand can also swim any time they are in water, except for iron golems, piglins, hoglins, striders, piglin brutes and undead mobs. This can lead to drowning if the water is falling from above.

Water of any depth prevents any entity, including the player, from sustaining falling damage if they fall into it, regardless of the distance fallen.

Being inside of water also imparts a fog effect, tinted accordingly.

### Spreading
Main article: Fluid § Spread
An image showing water's spreading distance
Water spreads horizontally and downward into nearby air blocks. Water can spread downward infinitely until stopped by a block, and 7 blocks horizontally from a source block on a flat surface. Water spreads at a rate of 1 block every 5 game ticks, or 4 blocks per second.

When spreading horizontally, a weight is assigned to every direction water can flow. For each direction, this weight is initially set to 1000. Then, for every adjacent block it can flow into it tries to find a way down that is reachable in four or fewer blocks from the block it wants to flow to. When found, the flow weight for that direction is set to the shortest path distance to the way down. Finally, water spreads in the directions with the lowest flow weight.

Spreading water extinguishes fire and washes away certain types of items or placed blocks, causing them to drop as items and then carrying them along in the flow until the edge of the spread. Affected items include plants (except trees), snow, torches, carpets, redstone dust and some other redstone components, cobweb, end rods, heads, and flower pots.

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

### Light
In Bedrock Edition, every block of water reduces light by 1 extra level (in addition to the normal fading-out of light). In Java Edition, water does not cause any additional decrease for block light, but diffuses sky light, causing the light to fade with depth. Underwater visibility changes depending on the biome the player is in. The Night Vision and Conduit Power effects increase underwater visibility.

### Color
Water has several colors, depending on the biome.

#### Java Edition
| Biome                                                          | Water color | Water fog color | Block |
|----------------------------------------------------------------|-------------|-----------------|-------|
| Default (biomes not listed below)                              | #3F76E4     | #050533         |       |
| Swamp                                                          | #617B64     | #232317         |       |
| Lukewarm Ocean<br/>Deep Lukewarm Ocean                         | #45ADF2     | #041633         |       |
| Warm Ocean                                                     | #43D5EE     | #041F33         |       |
| Cold Ocean<br/>Deep Cold Ocean<br/>Snowy Taiga<br/>Snowy Beach | #3D57D6     | #050533         |       |
| Frozen River<br/>Frozen Ocean<br/>Deep Frozen Ocean            | #3938C9     | #050533         |       |
| Meadow                                                         | #0E4ECF     | #050533         |       |
| Mangrove Swamp                                                 | #3A7A6A     | #4D7A60         |       |
| Cherry Grove                                                   | #5DB7EF     | #5DB7EF         |       |

#### Bedrock Edition
Biome tints

| Biome                                                                   | Water Surface Color | Water Fog Color | Water Fog Distance | Water Surface Transparency | Block |
|-------------------------------------------------------------------------|---------------------|-----------------|--------------------|----------------------------|-------|
| Default<br/>(biomes not listed below)                                   | #44aff5             | #44aff5         | 15                 | 65%                        |       |
| Sunflower Plains<br/>Plains                                             | #44aff5             | #44aff5         | 60                 | -                          |       |
| Desert                                                                  | #32a598             | #32a598         | 60                 | -                          |       |
| Mountains                                                               | #007BF7             | #007BF7         | -                  | -                          |       |
| Forest                                                                  | #1e97f2             | #1e97f2         | 60                 | -                          |       |
| Flower Forest                                                           | #20a3CC             | #20a3CC         | 60                 | -                          |       |
| Taiga                                                                   | #287082             | #287082         | 60                 | -                          |       |
| Taiga Mountains                                                         | #1e6B82             | #1e6B82         | -                  | -                          |       |
| Swamp                                                                   | #4c6559             | #4c6559         | 30                 | 100%                       |       |
| River                                                                   | #0084ff             | #0084ff         | 60                 | -                          |       |
| Nether Wastes<br/>Warped Forest<br/>Crimson Forest<br/>Soul Sand Valley | #905957             | #905957         | 15                 | -                          |       |
| Basalt Deltas                                                           | #3f76e4             | #423e42         | 15                 | -                          |       |
| The End                                                                 | #62529e             | #62529e         | -                  | -                          |       |
| Frozen River                                                            | #185390             | #185390         | 60                 | -                          |       |
| Snowy Plains<br/>Ice Spikes                                             | #14559b             | #14559b         | -                  | -                          |       |
| Mushroom Fields                                                         | #8a8997             | #8a8997         | -                  | -                          |       |
| Beach                                                                   | #157cab             | #157cab         | 60                 | -                          |       |
| Mountain Edge                                                           | #045cd5             | #045cd5         | -                  | -                          |       |
| Jungle<br/>Bamboo Jungle                                                | #14a2c5             | #14a2c5         | 60<br/>15          | -                          |       |
| Sparse Jungle                                                           | #0D8AE3             | #0D8AE3         | -                  | -                          |       |
| Stony Shore                                                             | #0d67bb             | #0d67bb         | 60                 | -                          |       |
| Snowy Beach                                                             | #1463a5             | #1463a5         | 60                 | -                          |       |
| Birch Forest                                                            | #0677ce             | #0677ce         | 60                 | -                          |       |
| Dark Forest                                                             | #3B6CD1             | #3B6CD1         | 60                 | -                          |       |
| Snowy Taiga                                                             | #205e83             | #205e83         | 60                 | -                          |       |
| Old Growth Pine Taiga<br/>Old Growth Spruce Taiga                       | #2d6d77             | #2d6d77         | 60                 | -                          |       |
| Windswept Forest<br/>Windswept Gravelly Hills                           | #0E63AB             | #0E63AB         | -                  | -                          |       |
| Savanna                                                                 | #2C8B9C             | #2C8B9C         | 60                 | -                          |       |
| Savanna Plateau<br/>Windswept Savanna                                   | #2590a8             | #2590a8         | -                  | -                          |       |
| Badlands                                                                | #4E7f81             | #4E7f81         | 60                 | -                          |       |
| Eroded Badlands<br/>Wooded Badlands                                     | #497f99             | #497f99         | -                  | -                          |       |
| Ocean                                                                   | #1787D4             | #1165b0         | 60                 | -                          |       |
| Deep Ocean                                                              | #1787D4             | #1463a5         | 60                 | -                          |       |
| Warm Ocean                                                              | #02B0E5             | #0289d5         | 60                 | 55%                        |       |
| Lukewarm Ocean                                                          | #0D96DB             | #0a74c4         | 60                 | -                          |       |
| Lukewarm Deep Ocean                                                     | #0D96DB             | #0e72b9         | 60                 | -                          |       |
| Cold Ocean                                                              | #2080C9             | #14559b         | 60                 | -                          |       |
| Cold Deep Ocean                                                         | #2080C9             | #185390         | 60                 | -                          |       |
| Frozen Ocean                                                            | #2570B5             | #174985         | 60                 | -                          |       |
| Frozen Deep Ocean                                                       | #2570B5             | #1a4879         | 60                 | -                          |       |
| Mangrove Swamp                                                          | #3a7a6a             | #4d7a60         | 30                 | -                          |       |

Biome tints from unused biomes

| Biome                                                    | Water Surface Color | Water Fog Color | Water Fog Distance | Water Surface Transparency | Block |
|----------------------------------------------------------|---------------------|-----------------|--------------------|----------------------------|-------|
| Legacy Frozen Ocean                                      | #44aff5             | #44aff5         | -                  | -                          |       |
| Mountains                                                | #007BF7             | #007bf7         | -                  | -                          |       |
| Taiga Mountains                                          | #1e6B82             | #1e6b82         | -                  | -                          |       |
| Swamp Hills                                              | #4c6156             | #4c6156         | 30                 | 100%                       |       |
| Snowy Mountains                                          | #1156a7             | #1156a7         | -                  | -                          |       |
| Mushroom Field Shore                                     | #818193             | #818193         | -                  | -                          |       |
| Desert Hills                                             | #1a7aa1             | #1a7aa1         | -                  | -                          |       |
| Wooded Hills                                             | #056bd1             | #056bd1         | -                  | -                          |       |
| Taiga Hills                                              | #236583             | #236583         | -                  | -                          |       |
| Mountain Edge                                            | #045cd5             | #045cd5         | -                  | -                          |       |
| Jungle Hills<br/>Modified Jungle<br/>Bamboo Jungle Hills | #1B9ED8             | #1B9ED8         | -                  | -                          |       |
| Modified Jungle Edge                                     | #0D8AE3             | #0D8AE3         | -                  | -                          |       |
| Birch Forest Hills                                       | #0a74c4             | #0a74c4         | -                  | -                          |       |
| Snowy Taiga Mountains                                    | #205e83             | #205e83         | 60                 | -                          |       |
| Snowy Taiga Hills                                        | #245b78             | #245b78         | -                  | -                          |       |
| Giant Tree Taiga Hills                                   | #286378             | #286378         | -                  | -                          |       |
| Gravelly Mountains+                                      | #0E63AB             | #0e63ab         | -                  | -                          |       |
| Shattered Savanna Plateau                                | #2590a8             | #2590a8         | -                  | -                          |       |
| Badlands Plateau<br/>Modified Badlands Plateau           | #55809E             | #55809e         | -                  | -                          |       |
| Warm Deep Ocean                                          | #02B0E5             | #0686ca         | 60                 | -                          |       |

### Water and lava
Main article: Fluid § Mixing
Water and lava can produce stone, cobblestone, or obsidian based on how they interact. If water touches a lava source, the lava source turns to obsidian. If both touch each other while flowing, cobblestone is made and no sources are removed, and if lava flows downward onto water, the water turns to stone.

### Interactions with mobs
#### Direct contact
Water damages endermen, snow golems, striders and blazes, at a rate of 1 per half second. If water comes into contact with a shulker or an enderman, the mob teleports away.

#### Drowning
Main article: Damage § Drowning
Players and mobs (except aquatic mobs, undead mobs and iron golems) have a breath meter that lasts 15 seconds. After they run out of breath, they take 2 drowning damage every second until they die, surface, or enter bubble columns.

Dolphins are a special case when it comes to drowning: they take drowning damage when underwater for about 4 minutes, but also take suffocation damage when in air for about 2 minutes.

Each level of the Respiration enchantment adds 15 seconds to the breath meter and grants an x/(x+1) chance (where x is the Respiration level) of not taking damage after that time: 30 seconds and an average 1/second with Respiration I, 45 seconds and an average of 2⁄3 damage/second with Respiration II, and 60 seconds and an average of 1⁄2 damage/second with Respiration III.

If a husk drowns underwater, it starts to shake and eventually becomes a zombie. If a zombie drowns underwater, it starts to shake and eventually transforms into a drowned.

### Slower mining speed
Players with their head underwater require 5 times the normal amount of time to mine blocks while standing on the ground, or 25 times while not on the ground. If a player wears a helmet with the Aqua Affinity enchantment, then underwater mining speed while standing on the ground is the same as on land, and 5 times slower if not standing on the ground.

### Explosions
Water does not prevent explosions from activating. Water has a high blast resistance, causing it to absorb any normal blasts, with the exception of explosions from underwater TNT‌[Minecraft Education  only].

### Hardening concrete powder
When water comes into contact with concrete powder, the powder hardens into solid concrete.

### Sponges
When a dry sponge comes into contact with a water source or flowing block, it becomes a wet sponge, absorbing all water within 3 to 5 blocks in all directions. Kelp and lily pads within the absorbed water blocks are destroyed and drop as items, and seagrass is destroyed without dropping anything. Mobs that take damage out of water are affected as a side-effect. 

Sponges do not absorb water from waterlogged blocks, nor water that comes into contact by flowing back in from outside the area of absorption. For instance, placing a sponge 4 or more blocks from a single water source removes the flowing water in the area of effect, but as the flow from the source resumes it is not affected by the wet sponge.

A sponge instantly absorbs nearby water when it is placed next to water or when water comes into contact with it (by being placed next to the sponge, or by flowing toward it). A sponge absorbs water around itself (water source blocks or flowing water) out to a taxicab distance of 7 in all directions (including up and down), but won't absorb more than 65 blocks of water (water closest to the sponge is absorbed first). The absorption propagates only from water to water and does not "jump over" non-water blocks (including air).

### Dripping
Dripping water.
Water above a non-transparent block (except for stairs, fences, or slabs) produces dripping particles on the underside of that block. If a block of pointed dripstone hangs under any block directly beneath a water source, the drips can slowly fill up a cauldron placed underneath. Without the dripstone, a cauldron does not fill.

### Vertical transport
Bubble columns are created by placing magma blocks or soul sand under water. These can be used to transport mobs or items quickly vertically.

## Data values
### ID
Java Edition:

| Water | Identifier | Form  | Translation key         |
|-------|------------|-------|-------------------------|
| Block | `water`    | Block | `block.minecraft.water` |

| Water         | Identifier      | Fluid tags |
|---------------|-----------------|------------|
| Fluid         | `water`         | `water`    |
| Flowing Fluid | `flowing_water` | `water`    |

Bedrock Edition:

| Water      | Identifier      | Numeric ID | Form                         | Item ID[i 1]   | Translation key           |
|------------|-----------------|------------|------------------------------|----------------|---------------------------|
| Flowing    | `flowing_water` | `8`        | Block & Ungiveable Item[i 2] | Identical[i 3] | `tile.flowing_water.name` |
| Stationary | `water`         | `9`        | Block & Ungiveable Item[i 2] | Identical[i 3] | `tile.water.name`         |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑ a bUnavailable with /give command
3. ↑ a bThe block's direct item form has the same id as the block.

### Block states
See also: Block states

Java Edition:

| Name  | Default value | Allowed values                                                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| level | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | If bit 0x8 is set, this fluid is "falling" and spreads only downward. At this level, the lower bits are essentially ignored, since this block is then at its highest fluid level. This level is equal to the falling water above, equal to 8 plus the level of the non-falling water above it.The lower three bits are the fluid block's level. 0 is the highest fluid level (not necessarily filling the block - this depends on the neighboring fluid blocks above each upper corner of the block). Data values increase as the fluid level of the block drops: 1 is the next highest, 2 lower, on through 7, the lowest fluid level. Along a line on a flat plane, water drops one level per meter. |

Bedrock Edition:
Water and flowing water

| Name         | Metadata Bits                       | Default value | Allowed values                                                                                                                    | Values forMetadata Bits                                                                                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|--------------|-------------------------------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| liquid_depth | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | If bit 0x8 is set, this fluid is "falling" and spreads only downward. At this level, the lower bits are essentially ignored, since this block is then at its highest fluid level. This level is equal to the falling water above, equal to 8 plus the level of the non-falling water above it.The lower three bits are the fluid block's level. 0 is the highest fluid level (not necessarily filling the block - this depends on the neighboring fluid blocks above each upper corner of the block). Data values increase as the fluid level of the block drops: 1 is the next highest, 2 lower, on through 7, the lowest fluid level. Along a line on a flat plane, water drops one level per meter. |



### Fluid states
See also: Block states

Java Edition:
Water

| Name    | Default value | Allowed values     | Description   |
|---------|---------------|--------------------|---------------|
| falling | `false`       | `true`<br/>`false` | Always false. |

Flowing water

| Name    | Default value | Allowed values                                              | Description                                                 |
|---------|---------------|-------------------------------------------------------------|-------------------------------------------------------------|
| falling | `false`       | `true`<br/>`false`                                          | True for falling water, false for water with a block below. |
| level   | `1`           | `1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8` | Height of the water, 8 when the water is falling.           |

