# Vines
Vines are climbable non-solid vegetation blocks that grow on walls.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Trading
	- 1.4 Post-generation
- 2 Behavior
- 3 Usage
	- 3.1 Crafting ingredient
	- 3.2 Composting
	- 3.3 Color
		- 3.3.1 Biome colors
- 4 Sounds
- 5 Data values
	- 5.1 ID
	- 5.2 Block states
- 6 History
- 7 Issues
- 8 Gallery
	- 8.1 Screenshots
- 9 References
- 10 External links

## Obtaining
### Breaking
Vines can be destroyed with any item, but using shears is the only way to collect them. Shears enchanted with Efficiency are more efficient when used on vines; Efficiency II and above allows vines to be instantly broken.[1] Using an axe on vines can also increase efficiency, but does not allow for collection, even with Silk Touch. If multiple vines exist within the same block space, breaking one of them breaks all of them instead of just the one targeted[2] and results in only a single vine dropping[3]. Shears used by a dispenser cannot break vines.

| Block     | Vines                 |
|-----------|-----------------------|
| Hardness  | 0.2                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 0.3                   |
| Wooden    | 0.15                  |
| Stone     | 0.1                   |
| Iron      | 0.05                  |
| Diamond   | 0.05                  |
| Netherite | 0.05                  |
| Golden    | 0.05                  |
| Shears    | 0.3                   |
| Sword     | 0.2                   |


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


### Natural generation
Vines are naturally generated in jungles, swamps and lush caves. Jungle trees of both sizes have vines on their trunks and canopy edges, and vines grow on the sides of jungle terrain. Vines are also naturally generated on oak trees in swamps and mangrove trees. In Bedrock Edition, vines can also generate on dying oak, spruce, jungle and dark oak trees. 

Vines are found in jungle temples and the allium room in woodland mansions. They can also generate in watchtower walls in pillager outposts.


### Trading
Vines are sold by wandering traders for an emerald.

### Post-generation
Vines generate on 2×2 jungle trees grown from saplings, or mangrove trees grown from propagules.

In Bedrock Edition, vines generate on dying trees, which can sometimes be grown from saplings.

## Behavior
On each block tick, the vine block has a 25% chance to spread in a randomly selected direction. Their spreading can be toggled by the doVinesSpread game rule‌[Java Edition  only]. Vines spread to adjacent blocks under certain conditions:

- Downward:
	- If the block below is air, each side (north, south, east, and west) with vines has a 50% chance to spread downward.
	- If the block below is a block, each side of that block with vines on the ticked block has a 50% chance of gaining vines.

- Upward:
	- If the block above is air and there are fewer than 4 other vine blocks in a 9×9×3 area surrounding the ticked vine block, each side (north, south, east, and west) with vines has a 50% chance to spread upward if that side is backed by a block that vines can be placed on.

- Horizontally:
	- If the current vine block isn't covering the target direction and there are fewer than 4 other vine blocks in a 9×9×3 area surrounding the ticked vine block, then:
		- If the block in the target direction is air, then it tries:

|   |   |
|---|---|
| ↑ | ? |

|  |   |
|--|---|
|  | ? |

If the vine block has vines to the right and that side of the air block is backed by something vines can be placed on, spread to the right side of the air block.

|   |   |
|---|---|
| ? | ↑ |

|   |  |
|---|--|
| ? |  |

If the vine block has vines to the left and that side of the air block is backed by something vines can be placed on, spread to the left side of the air block.

|   |  |
|---|--|
| ↑ |  |

|  |  |
|--|--|
|  |  |

[more information needed]

If the vine block has vines to the right, and that side of the air block is backed by another air block, and the right side of the vine block is backed by something vines can be placed on, spread around the corner.

|  |   |
|--|---|
|  | ↑ |

|  |  |
|--|--|
|  |  |

If the vine block has vines to the left, and that side of the air block is backed by another air block, and the left side of the vine block is backed by something vines can be placed on, spread around the corner.

If the air block in the target direction has something vines could be placed on above it, spread to the top side of the air block.
If the block in the target direction is opaque and fills its whole cube, spread to that side of the ticked vine block.
Vines cannot be grown using bone meal.

Vines do not need light when growing.

## Usage
Vines can be placed on the side of any block that fills its whole cube and blocks entity movement. They can also be placed on the bottom side of a block (although not the bottom side of another vine[4]). However, a vine block without vines on any of the horizontal sides disappears if it gets an update from a neighboring block. Vines attached to the bottom of stairs are completely deleted by any block update.[5]

Several vines can be placed in the same block space, as long as they are facing different directions.

Vines can be climbed by standing next to them and holding the jump key. If there is a solid block behind the vines, the walk forward key can also be used.

Vines cancel a sprint if the player is sprinting, slowing the movement speed.

Vines absorb all fall damage, even without a solid surface nearby. Sneaking on vines causes the player to hang, even if the vines are not adjacent to any surface.

Blocks can replace vines if placed within the same block space. However, item frames and paintings cannot.[6]

### Crafting ingredient
| Name                            | Ingredients        | Crafting recipe |
|---------------------------------|--------------------|-----------------|
| Banner Pattern Bordure Indented | Paper+Vines        |                 |
| Mossy Cobblestone               | Cobblestone+Vines  |                 |
| Mossy Stone Bricks              | Stone Bricks+Vines |                 |

### Composting
Placing vines into a composter has a 50% chance of raising the compost level by 1.

### Color
- In the Inventory, Vines have a Color:#48b518.

##### Biome colors
These values are generated by the biome dyeing algorithm. See biome colors for more information.

| Biome                                                                                                                                                                                                              | Temperature | Downfall                   | Foliage Color | Block |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|----------------------------|---------------|-------|
| (Default values)The VoidRiverWarm OceanLukewarm OceanDeep Lukewarm OceanOceanDeep OceanCold OceanDeep Cold OceanDeep Frozen OceanLush Caves‌[JE  only]The EndEnd HighlandsEnd MidlandsSmall End IslandsEnd Barrens | 0.5         | 0.5                        | #71a74d       |       |
| Lush Caves‌[BE  only]                                                                                                                                                                                              | 0.9         | 0.0                        | #a6a432       |       |
| PlainsBeachSunflower PlainsDripstone Caves‌[JE  only]Deep Dark                                                                                                                                                     | 0.8         | 0.4                        | #77ab2f       |       |
| Dripstone Caves‌[BE  only]                                                                                                                                                                                         | 0.2         | 0.0                        | #70a26c       |       |
| Snowy PlainsIce SpikesSnowy TaigaFrozen OceanFrozen River                                                                                                                                                          | 0.0         | 0.5                        | #60a17b       |       |
|                                                                                                                                                                                                                    |             | Grove                      | -0.2          | 0.8   |
|                                                                                                                                                                                                                    |             | Snowy Slopes               | -0.3          | 0.9   |
|                                                                                                                                                                                                                    |             | Frozen PeaksJagged Peaks   | -0.7          | 0.9   |
| DesertSavanna‌[JE  only]Savanna Plateau‌[JE  only]Windswept SavannaNether WastesWarped ForestCrimson ForestSoul Sand ValleyBasalt Deltas                                                                           | 2.0         | 0.0                        | #aea42a       |       |
|                                                                                                                                                                                                                    |             | Savanna‌[BE  only]         | 1.2           | 0.0   |
|                                                                                                                                                                                                                    |             | Savanna Plateau‌[BE  only] | 1.0           | 0.0   |
| BadlandsWooded BadlandsEroded Badlands                                                                                                                                                                             | 2.0         | 0.0                        | #9e814d[n 1]  |       |
| Swamp                                                                                                                                                                                                              | 0.8         | 0.9                        | #6a7039[n 1]  |       |
| Mangrove Swamp                                                                                                                                                                                                     | 0.8         | 0.9                        | #8db127[n 1]  |       |
| ForestDark ForestFlower Forest                                                                                                                                                                                     | 0.7         | 0.8                        | #59ae30       |       |
| Birch ForestOld Growth Birch Forest                                                                                                                                                                                | 0.6         | 0.6                        | #6ba941       |       |
| Old Growth Pine Taiga                                                                                                                                                                                              | 0.3         | 0.8                        | #68a55f       |       |
| Old Growth Spruce TaigaTaiga                                                                                                                                                                                       | 0.25        | 0.8                        | #68a464       |       |
| Windswept HillsWindswept Gravelly HillsWindswept ForestStony Shore                                                                                                                                                 | 0.2         | 0.3                        | #6da36b       |       |
| JungleBamboo Jungle                                                                                                                                                                                                | 0.95        | 0.9                        | #30bb0b       |       |
| Sparse Jungle                                                                                                                                                                                                      | 0.95        | 0.8                        | #3eb80f       |       |
| Meadow                                                                                                                                                                                                             | 0.5         | 0.8                        | #63a948       |       |
| Cherry Grove                                                                                                                                                                                                       | 0.5         | 0.8                        | #b6db61[n 1]  |       |
| Stony Peaks                                                                                                                                                                                                        | 1.0         | 0.3                        | #82ac1e       |       |
| Snowy Beach                                                                                                                                                                                                        | 0.05        | 0.3                        | #64a278       |       |
| Mushroom Fields                                                                                                                                                                                                    | 0.9         | 1.0                        | #2bbb0f       |       |

Unused biomes in Bedrock Edition.

| Biome                                                                     | Temperature | Downfall                               | Foliage Color | Block |
|---------------------------------------------------------------------------|-------------|----------------------------------------|---------------|-------|
| (Default values)Deep Warm Ocean                                           | 0.5         | 0.5                                    | #71a74d       |       |
| Snowy MountainsLegacy Frozen Ocean                                        | 0.0         | 0.5                                    | #60a17b       |       |
|                                                                           |             | Snowy Taiga HillsSnowy Taiga Mountains | -0.5          | 0.4   |
| Taiga HillsTaiga Mountains                                                | 0.25        | 0.8                                    | #68a464       |       |
| Desert HillsDesert Lakes                                                  | 2.0         | 0.0                                    | #aea42a       |       |
| Badlands PlateauModified Badlands PlateauModified Wooded Badlands Plateau | 2.0         | 0.0                                    | #9e814d[n 1]  |       |
| Shattered Savanna Plateau                                                 | 1.0         | 0.5                                    | #64b216       |       |
| Swamp Hills                                                               | 0.8         | 0.5                                    | #6a7039[n 1]  |       |
| Wooded HillsTall Birch Hills                                              | 0.7         | 0.8                                    | #59ae30       |       |
| Birch Forest Hills                                                        | 0.6         | 0.6                                    | #6ba941       |       |
| Giant Tree Taiga HillsGiant Spruce Taiga Hills                            | 0.3         | 0.8                                    | #68a55f       |       |
| Gravelly Mountains+Mountain Edge                                          | 0.2         | 0.3                                    | #6da36b       |       |
| Jungle HillsModified JungleBamboo Jungle Hills                            | 0.95        | 0.9                                    | #30bb0b       |       |
| Modified Jungle Edge                                                      | 0.95        | 0.8                                    | #3eb80f       |       |
| Mushroom Field Shore                                                      | 0.9         | 1.0                                    | #2bbb0f       |       |


↑ a b c d e f Color is preset


## Data values
### ID
Java Edition:

| Name  | Identifier | Form         | Block tags                       | Translation key      |
|-------|------------|--------------|----------------------------------|----------------------|
| Vines | vine       | Block & Item | climbablelush_plants_replaceable | block.minecraft.vine |

Bedrock Edition:

| Name  | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key |
|-------|------------|------------|----------------------------|----------------|-----------------|
| Vines | vine       | 106        | Block & Giveable Item[i 2] | Identical[i 3] | tile.vine.name  |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


### Block states
See also: Block state

Java Edition:

| Name  | Default value | Allowed values | Description                                          |
|-------|---------------|----------------|------------------------------------------------------|
| east  | false         | falsetrue      | When true, a vine texture is displayed on the east.  |
| north | false         | falsetrue      | When true, a vine texture is displayed on the north. |
| south | false         | falsetrue      | When true, a vine texture is displayed on the south. |
| up    | false         | falsetrue      | When true, a vine texture is displayed on the top.   |
| west  | false         | falsetrue      | When true, a vine texture is displayed on the west.  |

Bedrock Edition:

| Name                | Metadata Bits | Default value | Allowed values         | Values forMetadata Bits | Description                                                                                                                                                                                                                                                           |
|---------------------|---------------|---------------|------------------------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| vine_direction_bits | 0x10x20x40x8  | 0             | 0123456789101112131415 | 0123456789101112131415  | The directions the vine exists, excluding up. Each bit determines one direction:0x1: Vines at the south 0x2: Vines at the west 0x4: Vines at the north 0x8: Vines at the eastNote: Vines gain the ceiling vines if there's a block above, block state doesn't change. |



