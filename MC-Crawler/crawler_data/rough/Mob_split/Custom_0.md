# Custom
Custom is a world type that allows users to change the generation of the Overworld, Nether, and End dimensions as well as the ability to create custom dimensions. It is edited using a JSON file that is imported on the world creation screen.

## Contents
- 1 Access
- 2 JSON format
	- 2.1 Generator types
- 3 Defaults
	- 3.1 Noise generator preset defaults
		- 3.1.1 Structure defaults
	- 3.2 Biome parameter defaults
	- 3.3 Type defaults
- 4 Examples
	- 4.1 Default settings
		- 4.1.1 Expanded default settings
	- 4.2 Custom superflat dimension
- 5 History
- 6 Issues
- 7 Gallery
	- 7.1 Screenshots
- 8 External links
- 9 See also
- 10 Notes
- 11 References

## Access
To customize a world by using a JSON file, it needs to be imported before world creation: 

- in the world creation menu, go to "More World Options..." and select the "Import Settings" option. Then, select a world generationJSONfile. A warning appears saying that custom worlds are experimental. Click "Yes" to continue.
- then, in the world creation menu, the "World Type" button becomes gray and displays text: "World Type: Custom", so that the user is not able to change the world type anymore for the world being created.

The only way to access added dimensions is through commands, such as /execute in <dimension name> run tp @s ~ ~ ~, which teleports the player to the specified dimension (see § JSON format).

## JSON format
Main articles: Custom dimension and Custom world generation

  

This section needs expansion. 
You can help by expanding it.Instructions:  explanations on each component of the JSON file. Useful sources: [1], [2]


Custom generation files take the following format:

- The root tag.
	- bonus_chest: Whether the world has a bonus chest or not (equivalent to the "Bonus chest" option).
	- generate_features: Whether structures should be generated or not (equivalent to the "Generate structures" option).
	- seed: The numerical seed of the world.
	- legacy_custom_options: The custom world preset that was used to generate the world when it was anold customizedworld. Exists only for old customized worlds.
	- dimensions: A list of the dimensions in this world where the key is theresource locationof the dimension.
		- A dimension. The dimensionsminecraft:overworld,minecraft:the_netherandminecraft:the_endare required for a well functioning world. Any other resource location is allowed for custom dimensions.
			- generator: Generation settings used for that dimension.
				- type: The ID of the generator. Can beminecraft:flatfor a superflat dimension,minecraft:noisefor noise generation, orminecraft:debugfor adebugdimension.
				- Other compounds (see below)
			- type: The resource location of a dimension type file in a data pack, or one of the four default dimension types (minecraft:overworld,minecraft:the_nether,minecraft:the_end,minecraft:overworld_caves).

### Generator types
- 
	- type: The ID of the genarator. One ofnoise,flat, ordebug.If  type is minecraft:noise, additional fields are as follows:
	- settings:noise settings(referenced byID orinlined) — Settings for the noise generator.
	- biome_source: Settings dictating which biomes and biome shapes.
		- type: The type of biome generation. One ofmulti_noise,fixed,checkerboard, orthe_end.If type is multi_noise(3D biome generation used in the nether, and in the overworld in snapshot 21w37a and after.) , additional fields are as follows:
		- preset: (mutually exclusive withbiomes) An ID or an object of amulti-noise biome source parameter list.
		- biomes: (mutually exclusive withpreset) (Cannot be empty) A parameter list of biomes, including their IDs and target noise parameters.
			- : A biome and its properties.
				- biome:biome(referenced byID) — The biome to place at the given parameters. A single id may be repeated several times with different parameters.
				- parameters: Represent optimal intervals for where the biome should be placed. These values do not affect the generation of terrain within biomes, instead, they only affect where the game chooses to place biomes. Thinking of a six-dimensional space, in the space these intervals are defined for biomes. If the six parameters at a location based on the noise router innoise settingsfall into an interval, the corresponding biome is generated here. If the six parameters at a location do not fall into a defined biome interval in this list, it uses the closest biome interval to the 6D parameter point, in order to form a transition between biomes. Parameter combinations should be unique in the biomes list.
					- 
					- Noise parameter for biome (SeeBiomefor usages of each parameter in vanilla game)
		- biome: The ID of the single biome to generate.If type is checkerboard(A biome generation in which biomes are square (or close to square) and repeat along the diagonals) , additional fields are as follows:
		- biomes:biome(referenced byID), or biome#tagorlist (containingIDs) Biomes that repeat along the diagonals.
		- scale: (optional, defaults to 2) Value between 0 and 62 (both inclusive). Determines the size of the squares on an exponential scale.
	- settings: Superflat settings.
		- 
		- Flat generation settings



## Defaults
Moved to Custom world generation#Noise settings

### Noise generator preset defaults
These are the settings used by the 6 presets available for the minecraft:noise generator.

| Property     |                |                          | minecraft:overworld | minecraft:amplified | minecraft:nether       | minecraft:caves   | minecraft:end         | minecraft:floating_islands |
|--------------|----------------|--------------------------|---------------------|---------------------|------------------------|-------------------|-----------------------|----------------------------|
|              |                | `bedrock_roof_position`  |                     | -10                 |                        | 0                 |                       | -10                        |
|              |                | `bedrock_floor_position` |                     | 0                   |                        | 0                 |                       | -10                        |
|              |                | `sea_level`              |                     | 63                  |                        | 32                |                       | 0                          |
|              |                | `disable_mob_generation` |                     | false               |                        | false             | true                  | false                      |
|              |                | `default_block`          |                     | `minecraft:stone`   | `minecraft:netherrack` | `minecraft:stone` | `minecraft:end_stone` | `minecraft:stone`          |
|              |                | `default_fluid`          |                     | `minecraft:water`   | `minecraft:lava`       | `minecraft:water` | `minecraft:air`       | `minecraft:water`          |
| `structures` | `stronghold`   | `distance`               |                     | 32                  |                        | Tag not included  |                       | Tag not included           |
|              |                | `count`                  |                     | 1                   |                        |                   |                       |                            |
|              |                | `spread`                 |                     | 3                   |                        |                   |                       |                            |
|              |                | `structures`             |                     |                     |                        |                   |                       | See below                  |
| `noise`      | `top_slide`    | `target`                 |                     | -10                 |                        | 120               |                       | -3000                      |
|              |                | `size`                   |                     | 3                   |                        | 3                 |                       | 64                         |
|              |                | `offset`                 |                     | 0                   |                        | 0                 |                       | -46                        |
|              | `bottom_slide` | `target`                 |                     | -30                 |                        | 320               |                       | -30                        |
|              |                | `size`                   |                     | 0                   |                        | 4                 |                       | 7                          |
|              |                | `offset`                 |                     | 0                   |                        | -1                |                       | 1                          |
|              | `sampling`     | `xz_scale`               |                     | 0.9999999814507745  |                        | 1                 |                       | 2                          |
|              |                | `xz_factor`              |                     | 80                  |                        | 80                |                       | 80                         |
|              |                | `y_scale`                |                     | 0.9999999814507745  |                        | 3                 |                       | 1                          |
|              |                | `y_factor`               |                     | 160                 |                        | 60                |                       | 160                        |
|              |                | `size_vertical`          |                     | 2                   |                        | 2                 |                       | 1                          |
|              |                | `size_horizontal`        |                     | 1                   |                        | 1                 |                       | 2                          |
|              |                | `height`                 |                     | 256                 |                        | 128               |                       | 128                        |
|              |                | `density_factor`         |                     | 1                   |                        | 0                 |                       | 0                          |
|              |                | `density_offset`         |                     | -0.46875            |                        | 0.019921875       |                       | 0                          |
|              |                | `random_density_offset`  |                     | true                |                        | false             |                       | false                      |
|              |                | `simplex_surface_noise`  |                     | true                |                        | false             |                       | true                       |
|              |                | `island_noise_override`  |                     | false               |                        | false             | true                  | false                      |
|              |                | `amplified`              | false               | true                |                        | false             |                       | false                      |

