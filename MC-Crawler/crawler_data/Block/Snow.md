# Snow
Snow, known as top snow in Bedrock Edition, is a ground cover block found on the surface in snowy biomes, and can be replenished during snowfall.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
	- 1.4 Post-generation
		- 1.4.1 Weather
		- 1.4.2 Snow golems
- 2 Usage
	- 2.1 Cover
	- 2.2 Melting
	- 2.3 Foxes
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 Trivia
- 8 Gallery
	- 8.1 Screenshots
- 9 See also
- 10 Notes
- 11 References

## Obtaining
### Breaking
In Java Edition, destroying snow with a non-Silk-Touch shovel yields one snowball per layer. Explosions by TNT or creepers also cause snow to yield a snowball. Snow drops one item of itself per layer when mined using a shovel enchanted with Silk Touch, except for 8 layers of snow, which drops a snow block.[1] Any other tool, even if enchanted with Silk Touch, destroys the snow and drops nothing. 

In Bedrock Edition, destroying top snow with a shovel yields 1-4 snowballs. The number of snowballs dropped is as follows: 1 snowball for 1-3 layers, 2 snowballs for snow 4-5 layers, 3 snowballs for 6-7 layers, and 4 snowballs for 8 layers. Unlike Java Edition, shovels enchanted with Silk Touch cause top snow to drop snowballs.[2] Top snow can also be removed by using a shovel on it if there is no block directly above the snow layer, yielding 1-4 snowballs. One snowball is dropped — regardless of the number of layers — if top snow falls into an invalid block space after its support block is destroyed. 

| Block     | Snow                  |
|-----------|-----------------------|
| Hardness  | 0.1                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 0.5                   |
| Wooden    | 0.1                   |
| Stone     | 0.05                  |
| Iron      | 0.05                  |
| Diamond   | 0.05                  |
| Netherite | 0.05                  |
| Golden    | 0.05                  |


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


### Natural generation
Snow naturally generates in snowy biomes, cold biomes, and other biomes depending on the elevation and temperature. Only blocks with direct access to the sky can generate snow layers naturally (with the exception of some buildings in snowy villages, which generate extra snow in areas inaccessible to the sky).[3]

Top snow generates where there is sky access atop buildings in snowy taiga villages.‌[Bedrock Edition  only]

Snow generates as piles and in multiple layers as part of many snowy plains village structures.

By default, snow generates exclusively in single layers in Java Edition. Top snow can generate in multiple layers in Bedrock Edition.

Snow also generates in ancient cities.


### Crafting
| Ingredients | Crafting recipe |
|-------------|-----------------|
| Snow Block  | 6               |

### Post-generation
#### Weather
In snowy biomes or in cold biomes at higher altitudes, the weather can produce snow instead of rain. In snowy weather, snow generates on random blocks with a complete solid top surface at integer y-values, with a block light level of 9 or less, with the exception of ice and packed ice. The rate at which snow forms is affected by the game rule randomTickSpeed.

Below are the altitudes at which rain ends and snow begins, depending on the biome. The exact height of the snow line is randomized. In taiga, for example, the lowest possible snow layer forms at y level 153, and the lowest height where snow forms at all locations is y=168, with snow lines ranging between y levels 153 and 168 across different locations.

| Biome                                                                                                  | Layer                      |
|--------------------------------------------------------------------------------------------------------|----------------------------|
| All snowy biomes                                                                                       | y -64 (All altitudes)      |
| Windswept Gravelly Hills Windswept Hills Windswept Forest Stony Shore[4] Dripstone Caves‌[BE  only][5] | y 113–128                  |
| Taiga Old Growth Spruce Taiga                                                                          | y 153–168                  |
| Old Growth Pine Taiga Meadow‌[BE  only][needs testing] Cherry Grove‌[BE  only][needs testing]          | y 193–208                  |
| All others except Dry/Hot Biomes                                                                       | Above y 320 (not possible) |
| Frozen Ocean Deep Frozen Ocean                                                                         | Depends on location        |

In Bedrock Edition, anywhere from 1-12 layers of top snow can build up during snowfall, depending on the biome. In Java Edition, snowfall creates one layer of snow by default, and the number of layers that can accumulate can be altered by the game rule snowAccumulationHeight: the default value being 1, while setting it to 0 makes no snow form at all, and setting it to 8 or above lets snow form up to the level of a full block.

Snow layers do not generate if the game rule doWeatherCycle has been set to false.‌[Bedrock Edition  only]

#### Snow golems
See also: Tutorials/Snow farming

Snow golems generate a trail of snow in snowy, cold, and some medium biomes, or any non-dry biome in Bedrock Edition.

## Usage
Various thicknesses of snow.
Snow can be placed only on a solid block that is not ice. In Java Edition, snow breaks if its support block is removed. In Bedrock Edition, snow is affected by gravity and falls if it becomes unsupported, and breaks if it falls onto an unsuitable block. A player can jump up 1 block and 3 snow layers.

### Cover
Snow covered grass block, mycelium or podzol.
If the snow is on a grass block (or mycelium or podzol in Java Edition[6]) the ground cover turns white on the top and around the sides. Snow does not damage tilled and hydrated field areas – it cannot be placed on farmland. A gravity-affected block like sand or gravel does not fall if snow covers the block below it, but the gravity-affected block does replace a snow layer when falling onto it. The texture of the grass block changes to snowy when a single layer of snow is placed on top.[7][8] Thicker layers of snow causes the grass block to revert to plain dirt when the block receives a random tick, similar to regular grass when covered by an opaque block. A plain dirt block with a single layer of snow on top gains a snowy texture if grass spreads to it.

Snow layers will kill nylium if they are placed atop it, reverting it to netherrack.[9]

In Bedrock Edition, if leaves are topped with a layer of snow, particles of snow appear to fall through the leaves from the snow layer.

In Bedrock Edition, snow layers can occupy the same space as one-block flowers, mushrooms, and one-block ferns and short grass, (however two-block tall plants do not work)[10] and can be layered and mined normally. Placing snow on already-existing plant blocks causes snow to appear around them, but placing plants into an area where there is snow removes the snow.[11]

### Melting
Powered redstone lamps melting nearby snow.
Snow melts if there is a heat block,‌[BE & edu  only] or block light level of 12 or more. In Bedrock Edition, it also melts in dry biomes, regardless of block light or daylight level. If there are multiple layers, layers melt gradually in Bedrock Edition, but they melt all at once in Java.

Some light sources can melt snow but many cannot. The melt radius is taxicab distance.

| Item                      | Melt radius |
|---------------------------|-------------|
| Beacon                    | 3           |
| Campfire                  | 3           |
| Soul Campfire             | -           |
| Conduit                   | 3           |
| Glow Lichen               | -           |
| Glowstone                 | 3           |
| Jack o'Lantern            | 3           |
| Lantern                   | 3           |
| Soul Lantern              | -           |
| Lava                      | 3           |
| Redstone Lamp             | 3           |
| Respawn Anchor1/4 Charge  | -           |
| Respawn Anchor 2/4 Charge | -           |
| Respawn Anchor 3/4 Charge | -           |
| Respawn Anchor 4/4 Charge | 3           |
| 1Sea Pickle               | -           |
| 2 Sea Pickles             | -           |
| 3 Sea Pickles             | -           |
| 4 Sea Pickles             | 3           |
| Shroomlight               | 3           |
| Froglight                 | 3           |
| End Rod                   | 2           |
| Torch                     | 2           |
| Soul Torch                | -           |
| Redstone Torch            | -           |
| Ender Chest               | -           |
| Furnace                   | 1           |
| Blast Furnace             | 1           |
| Smoker                    | 1           |
| Crying Obsidian           | -           |
| Magma Block               | -           |
| Brewing Stand             | -           |
| Brown Mushroom            | -           |
| Dragon Egg                | -           |
| Redstone Ore              | -           |
| End Portal Frame          | -           |
| Fire                      | 3           |
| Soul Fire                 | -           |
| Nether Portal             | -           |
| Sea Lantern               | 3           |

### Foxes
When a fox gets stuck in the snow after missing an attack on prey, it emits particles as it emerges from the snow.

## Data values
### ID
Java Edition:

| Name | Identifier | Form         | Block tags                                  | Translation key      |
|------|------------|--------------|---------------------------------------------|----------------------|
| Snow | snow       | Block & Item | inside_step_sound_blockssnowmineable/shovel | block.minecraft.snow |

Bedrock Edition:

| Name     | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key      |
|----------|------------|------------|----------------------------|----------------|----------------------|
| Top Snow | snow_layer | 78         | Block & Giveable Item[i 2] | Identical[i 3] | tile.snow_layer.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


### Block states
See also: Block states

Java Edition:

| Name   | Default value | Allowed values | Description                                                                                                                                     |
|--------|---------------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| layers | 1             | 12345678       | The number of layers thick.Each layer adds two pixels to the block height, and each layer after the first adds two pixels to the collision box. |

Bedrock Edition:

| Name        | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                           |
|-------------|---------------|---------------|----------------|-------------------------|-------------------------------------------------------|
| height      | 0x10x20x4     | 0             | 01234567       | 01234567                | The number of layers in addition to the bottom layer. |
| covered_bit | 0x8           | false         | truefalse      | 01                      | True if the snow is covering a plant.                 |



## See also
- Snowlogging

## Notes


