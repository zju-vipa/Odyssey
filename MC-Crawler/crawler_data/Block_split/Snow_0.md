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

