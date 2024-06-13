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

#### Structure defaults
These are the default values for all namespaced structures. Every preset uses the same values for all of these structures, with the exception of minecraft:ruined_portal.

| Structure       |                     | Spacing | Separation | Salt      |
|-----------------|---------------------|---------|------------|-----------|
|                 | `village`           | 32      | 8          | 10387312  |
|                 | `desert_pyramid`    | 32      | 8          | 14357617  |
|                 | `igloo`             | 32      | 8          | 14357618  |
|                 | `jungle_pyramid`    | 32      | 8          | 14357619  |
|                 | `swamp_hut`         | 32      | 8          | 14357620  |
|                 | `pillager_outpost`  | 32      | 8          | 165745296 |
|                 | `stronghold`*       | 1       | 0          | 0         |
|                 | `monument`          | 32      | 5          | 10387313  |
|                 | `endcity`           | 20      | 11         | 10387313  |
|                 | `mansion`           | 80      | 20         | 10387319  |
|                 | `buried_treasure`** | 1       | 0          | 0         |
|                 | `mineshaft`**       | 1       | 0          | 0         |
| `ruined_portal` | `nether`and`caves`  | 25      | 10         | 34222645  |
|                 | All other presets   | 40      | 15         | 34222645  |
|                 | `shipwreck`         | 24      | 4          | 165745295 |
|                 | `ocean_ruin`        | 20      | 8          | 14357621  |
|                 | `bastion_remnant`   | 27      | 4          | 30084232  |
|                 | `fortress`          | 27      | 4          | 30084232  |
|                 | `nether_fossil`     | 2       | 1          | 14357921  |

*Placeholder values, have no effect

**Salt values aren't used for theses structures; changing them produces no effect

### Biome parameter defaults

  

This section needs to be updated. 
Please update this section to reflect recent updates or newly available information.Reason: Altitude was removed since and Continentalness, Erosion and Depth were added. Values might also not be up to date.


These are the default values used for each biome in the multi_noise biome_source. Interestingly, although only the values for nether biomes are accessible through a preset, several overworld biomes have default values as well.

| Biome                 | Temperature | Humidity | Altitude | Weirdness | Offset |
|-----------------------|-------------|----------|----------|-----------|--------|
| `badlands`            | -0.25       | -0.5     | 0.5      | 0.2       | 1      |
| `badlands_plateau`    | -0.25       | -0.5     | 0.65     | 0.2       | 1      |
| `bamboo_jungle`       | 0.5         | 0.5      | 0        | 0.2       | 1      |
| `bamboo_jungle_hills` | 0.5         | 0.5      | 0.25     | 0.2       | 1      |
| `basalt_deltas`       | -0.5        | 0        | 0        | 0         | 0.175  |
| `beach`               | 0           | 0        | -0.1     | 0         | 0.9935 |
| `birch_forest`        | -0.1        | 0.2      | 0        | 0         | 1      |
| `birch_forest_hills`  | -0.1        | 0.2      | 0.25     | 0         | 1      |
| `crimson_forest`      | 0.4         | 0        | 0        | 0         | 0      |
| `desert`              | 0.5         | -0.5     | 0        | 0         | 1      |
| `jungle`              | 0.5         | 0.5      | 0        | 0         | 1      |
| `nether_wastes`       | 0           | 0        | 0        | 0         | 0      |
| `ocean`               | 0           | 0        | -0.5     | 0         | 1      |
| `plains`              | 0           | 0        | 0        | 0         | 1      |
| `snowy_tundra`        | -0.5        | -0.5     | 0        | 0         | 1      |
| `soul_sand_valley`    | 0           | -0.5     | 0        | 0         | 0      |
| `warm_ocean`          | 0           | 0        | -0.25    | 0         | 1      |
| `warped_forest`       | 0           | 0.5      | 0        | 0         | 0.375  |

### Type defaults
These are the settings used by the 3 dimensions present in Vanilla and the additional Overworld Caves settings provided by Minecraft.

| Property               | Overworld            | The Nether        | The End        | Overworld Caves      |
|------------------------|----------------------|-------------------|----------------|----------------------|
| `ultrawarm`            | false                | true              | false          | false                |
| `natural`              | true                 | false             | false          | true                 |
| `coordinate_scale`     | 1.0                  | 8.0               | 1.0            | 1.0                  |
| `piglin_safe`          | false                | true              | false          | false                |
| `respawn_anchor_works` | false                | true              | false          | false                |
| `bed_works`            | true                 | false             | false          | true                 |
| `has_raids`            | true                 | false             | true           | true                 |
| `has_skylight`         | true                 | false             | false          | true                 |
| `has_ceiling`          | false                | true              | false          | true                 |
| `fixed_time`           | N/A                  | 18000             | 6000           | N/A                  |
| `ambient_light`        | 0.0                  | 0.1               | 0.0            | 0.0                  |
| `logical_height`       | 256                  | 128               | 256            | 256                  |
| `infiniburn`           | infiniburn_overworld | infiniburn_nether | infiniburn_end | infiniburn_overworld |
| `effects`              | overworld            | the_nether        | the_end        | overworld            |

## Examples

  

This section needs expansion. 
You can help by expanding it.Instructions: more examples and the actual info for what the default generator uses. Check that the Expanded default settings listed below still works in 1.19.3.


### Default settings
This one will change to 1.19.3-typed later.

The following is the settings for an exported default Minecraft world.


Collapsed JSON content
{
  "bonus_chest": false,
  "dimensions": {
    "minecraft:overworld": {
      "type": "minecraft:overworld",
      "generator": {
        "biome_source": {
          "seed": 0,
          "large_biomes": false,
          "type": "minecraft:vanilla_layered"
        },
        "seed": 0,
        "settings": "minecraft:overworld",
        "type": "minecraft:noise"
      }
    },
    "minecraft:the_nether": {
      "type": "minecraft:the_nether",
      "generator": {
        "biome_source": {
          "seed": 0,
          "preset": "minecraft:nether",
          "type": "minecraft:multi_noise"
        },
        "seed": 0,
        "settings": "minecraft:nether",
        "type": "minecraft:noise"
      }
    },
    "minecraft:the_end": {
      "type": "minecraft:the_end",
      "generator": {
        "biome_source": {
          "seed": 0,
          "type": "minecraft:the_end"
        },
        "seed": 0,
        "settings": "minecraft:end",
        "type": "minecraft:noise"
      }
    }
  },
  "seed": 0,
  "generate_features": true
}



#### Expanded default settings

This file contains the same settings used to produce a default world, but with all of the presets expanded to their default values. Note that there is a bug that makes it impossible to create the ender dragon fight without using the dimension type preset minecraft:the_end, as the flag that creates the fight is hardcoded and not accessible through JSON. However, it is otherwise identical to the default world.

Collapsed JSON content
{
  "bonus_chest": false,
  "dimensions": {
    "minecraft:overworld": {
      "type": {
		"logical_height": 256,
		"infiniburn": "minecraft:infiniburn_overworld",
		"effects": "minecraft:overworld",
		"ambient_light": 0.0,
		"respawn_anchor_works": false,
		"has_raids": true,
		"min_y": 0,
		"height": 256,
		"natural": true,
		"coordinate_scale": 1.0,
		"piglin_safe": false,
		"bed_works": true,
		"has_skylight": true,
		"has_ceiling": false,
		"ultrawarm": false
      },
      "generator": {
        "biome_source": {
          "seed": 0,
          "large_biomes": false,
          "type": "minecraft:vanilla_layered"
        },
        "seed": 0,
        "settings": {
		  "noise_caves_enabled": false,
		  "deepslate_enabled": false,
		  "ore_veins_enabled": false,
		  "noodle_caves_enabled": false,
		  "min_surface_level": 0,
		  "disable_mob_generation": false,
		  "aquifers_enabled": false,
		  "default_fluid": {
			"Properties": {
			  "level": "0"
			},
			"Name": "minecraft:water"
		  },
		  "bedrock_roof_position": -2147483648,
		  "bedrock_floor_position": 0,
		  "sea_level": 63,
		  "structures": {
			"stronghold": {
			  "distance": 32,
			  "spread": 3,
			  "count": 128
			},
			"structures": {
			  "minecraft:pillager_outpost": {
				"spacing": 32,
				"separation": 8,
				"salt": 165745296
			  },
			  "minecraft:village": {
				"spacing": 32,
				"separation": 8,
				"salt": 10387312
			  },
			  "minecraft:fortress": {
				"spacing": 27,
				"separation": 4,
				"salt": 30084232
			  },
			  "minecraft:desert_pyramid": {
				"spacing": 32,
				"separation": 8,
				"salt": 14357617
			  },
			  "minecraft:bastion_remnant": {
				"spacing": 27,
				"separation": 4,
				"salt": 30084232
			  },
			  "minecraft:stronghold": {
				"spacing": 1,
				"separation": 0,
				"salt": 0
			  },
			  "minecraft:monument": {
				"spacing": 32,
				"separation": 5,
				"salt": 10387313
			  },
			  "minecraft:swamp_hut": {
				"spacing": 32,
				"separation": 8,
				"salt": 14357620
			  },
			  "minecraft:endcity": {
				"spacing": 20,
				"separation": 11,
				"salt": 10387313
			  },
			  "minecraft:mineshaft": {
				"spacing": 1,
				"separation": 0,
				"salt": 0
			  },
			  "minecraft:igloo": {
				"spacing": 32,
				"separation": 8,
				"salt": 14357618
			  },
			  "minecraft:mansion": {
				"spacing": 80,
				"separation": 20,
				"salt": 10387319
			  },
			  "minecraft:buried_treasure": {
				"spacing": 1,
				"separation": 0,
				"salt": 0
			  },
			  "minecraft:ocean_ruin": {
				"spacing": 20,
				"separation": 8,
				"salt": 14357621
			  },
			  "minecraft:jungle_pyramid": {
				"spacing": 32,
				"separation": 8,
				"salt": 14357619
			  },
			  "minecraft:ruined_portal": {
				"spacing": 40,
				"separation": 15,
				"salt": 34222645
			  },
			  "minecraft:shipwreck": {
				"spacing": 24,
				"separation": 4,
				"salt": 165745295
			  },
			  "minecraft:nether_fossil": {
				"spacing": 2,
				"separation": 1,
				"salt": 14357921
			  }
			}
		  },
		  "noise": {
			"simplex_surface_noise": true,
			"random_density_offset": true,
			"size_vertical": 2,
			"density_factor": 1.0,
			"density_offset": -0.46875,
			"top_slide": {
			  "target": -10,
			  "size": 3,
			  "offset": 0
			},
			"bottom_slide": {
			  "target": 15,
			  "size": 3,
			  "offset": 0
			},
			"size_horizontal": 1,
			"min_y": 0,
			"height": 256,
			"sampling": {
			  "xz_scale": 0.9999999814507745,
			  "y_scale": 0.9999999814507745,
			  "xz_factor": 80.0,
			  "y_factor": 160.0
			}
		  },
		  "default_block": {
			"Name": "minecraft:stone"
		  }
		},
        "type": "minecraft:noise"
      }
    },
    "minecraft:the_nether": {
      "type": {
		"logical_height": 128,
		"infiniburn": "minecraft:infiniburn_nether",
		"effects": "minecraft:the_nether",
		"ambient_light": 0.1,
		"respawn_anchor_works": true,
		"has_raids": false,
		"min_y": 0,
		"height": 256,
		"natural": false,
		"coordinate_scale": 8.0,
		"piglin_safe": true,
		"bed_works": false,
		"fixed_time": 18000,
		"has_skylight": false,
		"has_ceiling": true,
		"ultrawarm": true
	  },
	  "generator": {
		"biome_source": {
		  "humidity_noise": {
			"firstOctave": -7,
			"amplitudes": [
			  1.0,
			  1.0
			]
		  },
		  "altitude_noise": {
			"firstOctave": -7,
			"amplitudes": [
			  1.0,
			  1.0
			]
		  },
		  "weirdness_noise": {
			"firstOctave": -7,
			"amplitudes": [
			  1.0,
			  1.0
			]
		  },
		  "seed": 0,
		  "biomes": [
			{
			  "parameters": {
				"altitude": 0.0,
				"weirdness": 0.0,
				"offset": 0.0,
				"temperature": 0.0,
				"humidity": 0.0
			  },
			  "biome": "minecraft:nether_wastes"
			},
			{
			  "parameters": {
				"altitude": 0.0,
				"weirdness": 0.0,
				"offset": 0.0,
				"temperature": 0.0,
				"humidity": -0.5
			  },
			  "biome": "minecraft:soul_sand_valley"
			},
			{
			  "parameters": {
				"altitude": 0.0,
				"weirdness": 0.0,
				"offset": 0.0,
				"temperature": 0.4,
				"humidity": 0.0
			  },
			  "biome": "minecraft:crimson_forest"
			},
			{
			  "parameters": {
				"altitude": 0.0,
				"weirdness": 0.0,
				"offset": 0.375,
				"temperature": 0.0,
				"humidity": 0.5
			  },
			  "biome": "minecraft:warped_forest"
			},
			{
			  "parameters": {
				"altitude": 0.0,
				"weirdness": 0.0,
				"offset": 0.175,
				"temperature": -0.5,
				"humidity": 0.0
			  },
			  "biome": "minecraft:basalt_deltas"
			}
		  ],
		  "temperature_noise": {
			"firstOctave": -7,
			"amplitudes": [
			  1.0,
			  1.0
			]
		  },
		  "type": "minecraft:multi_noise"
		},
        "seed": 0,
        "settings": {
		  "noise_caves_enabled": false,
		  "deepslate_enabled": false,
		  "ore_veins_enabled": false,
		  "noodle_caves_enabled": false,
		  "min_surface_level": 0,
		  "disable_mob_generation": false,
		  "aquifers_enabled": false,
		  "bedrock_roof_position": 0,
		  "bedrock_floor_position": 0,
		  "sea_level": 32,
		  "structures": {
			"structures": {
			  "minecraft:pillager_outpost": {
				"spacing": 32,
				"separation": 8,
				"salt": 165745296
			  },
			  "minecraft:village": {
				"spacing": 32,
				"separation": 8,
				"salt": 10387312
			  },
			  "minecraft:fortress": {
				"spacing": 27,
				"separation": 4,
				"salt": 30084232
			  },
			  "minecraft:desert_pyramid": {
				"spacing": 32,
				"separation": 8,
				"salt": 14357617
			  },
			  "minecraft:bastion_remnant": {
				"spacing": 27,
				"separation": 4,
				"salt": 30084232
			  },
			  "minecraft:stronghold": {
				"spacing": 1,
				"separation": 0,
				"salt": 0
			  },
			  "minecraft:monument": {
				"spacing": 32,
				"separation": 5,
				"salt": 10387313
			  },
			  "minecraft:swamp_hut": {
				"spacing": 32,
				"separation": 8,
				"salt": 14357620
			  },
			  "minecraft:endcity": {
				"spacing": 20,
				"separation": 11,
				"salt": 10387313
			  },
			  "minecraft:mineshaft": {
				"spacing": 1,
				"separation": 0,
				"salt": 0
			  },
			  "minecraft:igloo": {
				"spacing": 32,
				"separation": 8,
				"salt": 14357618
			  },
			  "minecraft:mansion": {
				"spacing": 80,
				"separation": 20,
				"salt": 10387319
			  },
			  "minecraft:buried_treasure": {
				"spacing": 1,
				"separation": 0,
				"salt": 0
			  },
			  "minecraft:ocean_ruin": {
				"spacing": 20,
				"separation": 8,
				"salt": 14357621
			  },
			  "minecraft:jungle_pyramid": {
				"spacing": 32,
				"separation": 8,
				"salt": 14357619
			  },
			  "minecraft:ruined_portal": {
				"spacing": 25,
				"separation": 10,
				"salt": 34222645
			  },
			  "minecraft:shipwreck": {
				"spacing": 24,
				"separation": 4,
				"salt": 165745295
			  },
			  "minecraft:nether_fossil": {
				"spacing": 2,
				"separation": 1,
				"salt": 14357921
			  }
			}
		  },
		  "noise": {
			"density_factor": 0.0,
			"density_offset": 0.019921875,
			"simplex_surface_noise": false,
			"bottom_slide": {
			  "target": 320,
			  "size": 4,
			  "offset": -1
			},
			"size_horizontal": 1,
			"size_vertical": 2,
			"height": 128,
			"sampling": {
			  "xz_scale": 1.0,
			  "y_scale": 3.0,
			  "xz_factor": 80.0,
			  "y_factor": 60.0
			},
			"top_slide": {
			  "target": 120,
			  "size": 3,
			  "offset": 0
			}
		  },
		  "default_block": {
			"Name": "minecraft:netherrack"
		  },
		  "default_fluid": {
			"Properties": {
			  "level": "0"
			},
			"Name": "minecraft:lava"
		  }
		},
        "type": "minecraft:noise"
      }
    },
    "minecraft:the_end": {
	  "type": {
		"logical_height": 256,
		"infiniburn": "minecraft:infiniburn_end",
		"effects": "minecraft:the_end",
		"ambient_light": 0.0,
		"respawn_anchor_works": false,
		"has_raids": true,
		"min_y": 0,
		"height": 256,
		"natural": false,
		"coordinate_scale": 1.0,
		"piglin_safe": false,
		"bed_works": false,
		"fixed_time": 6000,
		"has_skylight": false,
		"has_ceiling": false,
		"ultrawarm": false
	  },
      "generator": {
        "biome_source": {
          "seed": 0,
          "type": "minecraft:the_end"
        },
        "seed": 0,
        "settings": {
		  "noise_caves_enabled": false,
		  "deepslate_enabled": false,
		  "ore_veins_enabled": false,
		  "noodle_caves_enabled": false,
		  "min_surface_level": 0,
		  "disable_mob_generation": true,
		  "aquifers_enabled": false,
		  "bedrock_roof_position": -2147483648,
		  "bedrock_floor_position": -2147483648,
		  "sea_level": 0,
		  "structures": {
			"structures": {
			  "minecraft:pillager_outpost": {
				"spacing": 32,
				"separation": 8,
				"salt": 165745296
			  },
			  "minecraft:village": {
				"spacing": 32,
				"separation": 8,
				"salt": 10387312
			  },
			  "minecraft:fortress": {
				"spacing": 27,
				"separation": 4,
				"salt": 30084232
			  },
			  "minecraft:desert_pyramid": {
				"spacing": 32,
				"separation": 8,
				"salt": 14357617
			  },
			  "minecraft:bastion_remnant": {
				"spacing": 27,
				"separation": 4,
				"salt": 30084232
			  },
			  "minecraft:stronghold": {
				"spacing": 1,
				"separation": 0,
				"salt": 0
			  },
			  "minecraft:monument": {
				"spacing": 32,
				"separation": 5,
				"salt": 10387313
			  },
			  "minecraft:swamp_hut": {
				"spacing": 32,
				"separation": 8,
				"salt": 14357620
			  },
			  "minecraft:endcity": {
				"spacing": 20,
				"separation": 11,
				"salt": 10387313
			  },
			  "minecraft:mineshaft": {
				"spacing": 1,
				"separation": 0,
				"salt": 0
			  },
			  "minecraft:igloo": {
				"spacing": 32,
				"separation": 8,
				"salt": 14357618
			  },
			  "minecraft:mansion": {
				"spacing": 80,
				"separation": 20,
				"salt": 10387319
			  },
			  "minecraft:buried_treasure": {
				"spacing": 1,
				"separation": 0,
				"salt": 0
			  },
			  "minecraft:ocean_ruin": {
				"spacing": 20,
				"separation": 8,
				"salt": 14357621
			  },
			  "minecraft:jungle_pyramid": {
				"spacing": 32,
				"separation": 8,
				"salt": 14357619
			  },
			  "minecraft:ruined_portal": {
				"spacing": 40,
				"separation": 15,
				"salt": 34222645
			  },
			  "minecraft:shipwreck": {
				"spacing": 24,
				"separation": 4,
				"salt": 165745295
			  },
			  "minecraft:nether_fossil": {
				"spacing": 2,
				"separation": 1,
				"salt": 14357921
			  }
			}
		  },
		  "noise": {
			"island_noise_override": true,
			"density_factor": 0.0,
			"density_offset": 0.0,
			"simplex_surface_noise": true,
			"bottom_slide": {
			  "target": -30,
			  "size": 7,
			  "offset": 1
			},
			"size_horizontal": 2,
			"size_vertical": 1,
			"height": 128,
			"sampling": {
			  "xz_scale": 2.0,
			  "y_scale": 1.0,
			  "xz_factor": 80.0,
			  "y_factor": 160.0
			},
			"top_slide": {
			  "target": -3000,
			  "size": 64,
			  "offset": -46
			}
		  },
		  "default_block": {
			"Name": "minecraft:end_stone"
		  },
		  "default_fluid": {
			"Name": "minecraft:air"
		  }
		},
        "type": "minecraft:noise"
      }
    }
  },
  "seed": 0,
  "generate_features": true
}



### Custom superflat dimension
An overview of a world made with the adjacent settings.
This dimension is a Superflat world with a layer of grass on four layers of coarse dirt on top of five layers of basalt. The entire world is full of village houses as spacing is set to 3 (default: 32) and separation is set to 1 (default: 8). The world starts by default at time 1000.


Collapsed dimension object data
{
  "generator": {
    "settings": {
      "structures": {
        "structures": {
          "minecraft:village": {
            "spacing": 3,
            "separation": 1,
            "salt": 10387312
          }
        }
      },
      "layers": [
        {
          "height": 5,
          "block": "minecraft:basalt"
        },
        {
          "height": 4,
          "block": "minecraft:coarse_dirt"
        },
        {
          "height": 1,
          "block": "minecraft:grass_block"
        }
      ],
      "biome": "minecraft:plains"
    },
    "type": "minecraft:flat"
  },
  "type": {
    "ultrawarm": false,
    "natural": true,
	"coordinate_scale": 1.0,
    "ambient_light": 0.5,
    "fixed_time": 1000,
    "has_skylight": true,
    "has_ceiling": false
  }
}



## Notes


