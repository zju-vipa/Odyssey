# Tutorials/Adding a new dimension
This tutorial explains how to add a new custom dimension to a world using a data pack. It assumes you already know how to create a data pack.

pack.mcmeta
## Contents
- 1 Dimension
- 2 Dimension type
- 3 Noise generator
- 4 Noise settings
- 5 Noise router
- 6 Surface rules
- 7 Biome
- 8 See also
- 9 References

## Dimension
The newly created dimension.
The warning screen that shows when opening a world using experimental settings.
Adding a new dimension is as simple as creating one file in the data pack. This first dimension adds a new superflat world using the flat chunk generator.

data/tutorial/dimension/example_world.json
{
  "type": "minecraft:overworld",
  "generator": {
    "type": "minecraft:flat",
    "settings": {
      "biome": "minecraft:plains",
      "layers": [
        {
          "block": "minecraft:stone",
          "height": 64
        }
      ],
      "structure_overrides": []
    }
  }
}

When adding to an existing world, make sure to leave and reopen the world! A warning screen will ask you to confirm using experimental world settings. It means that new versions can break existing world generation data packs without warning. You can click "I know what I'm doing!".

Now you can use /execute in tutorial:example_world run tp @s ~ ~ ~ to teleport yourself to this new dimension.

The settings can be further customized:

- settings:
	- 
	- Flat generation settings

## Dimension type
The example above used "type": "minecraft:overworld". This is a reference to the dimension type of the dimension. Dimensions are made up of two parts:

- Thedimension typecontrols environmental properties. Changes to the dimension type will apply to existing chunks as well.
- Thechunk generatorcontrols the physical blocks and entities that are placed in the world. Changes to the chunk generator will only affect newly generated chunks.

If you want to modify the properties of the dimension, a new file can be created in a dimension_type folder and the dimension file needs to be updated to reference this new dimension type. In this example the  min_y and  height properties been modified, compared to the overworld dimension type. These control the build limit of the dimension.

data/tutorial/dimension_type/example_world.json
{
  "ultrawarm": false,
  "natural": true,
  "piglin_safe": false,
  "respawn_anchor_works": false,
  "bed_works": true,
  "has_raids": true,
  "has_skylight": true,
  "has_ceiling": false,
  "coordinate_scale": 1,
  "ambient_light": 0,
  "logical_height": 256,
  "infiniburn": "#minecraft:infiniburn_overworld",
  "min_y": 0,
  "height": 256,
  "monster_spawn_light_level": {
    "type": "minecraft:uniform",
    "value": {
      "min_inclusive": 0,
      "max_inclusive": 7
    }
  },
  "monster_spawn_block_light_limit": 0
}

data/tutorial/dimension/example_world.json
{
  "type": "tutorial:example_world",
  "generator": {
    // ...
  }
}


Full JSON format of dimension types

 The root object.

 ultrawarm: Whether the dimensions behaves like the nether (water evaporates and sponges dry) or not. Also lets stalactites drip lava and causes lava to spread faster and thinner.
 natural: When false, compasses spin randomly, and using a bed to set the respawn point or sleep, is disabled. When true, nether portals can spawn zombified piglins.
 coordinate_scale: The multiplier applied to coordinates when leaving the dimension. Value between 0.00001 and 30000000.0 (both inclusive)。
 has_skylight: Whether the dimension has skylight or not.
 has_ceiling: Whether the dimension has a bedrock ceiling. Note that this is only a logical ceiling. It is unrelated with whether the dimension really has a block ceiling.
 ambient_light: How much light the dimension has. When set to 0, it completely follows the light level; when set to 1, there is no ambient lighting. Precise effects need testing [needs testing].
 fixed_time: (optional) If this is set to an int, the time of the day is the specified value. To ensure a normal time cycle, leave the attribute undefined (i.e, do not include it).
 monster_spawn_light_level: Value between 0 and 15 (both inclusive). Maximum light required when the monster spawns. The formula of this light is: max( skyLight - 10, blockLight ) during thunderstorms, and max( internalSkyLight, blockLight ) during other weather.
Int provider
 monster_spawn_block_light_limit: Value between 0 and 15 (both inclusive). Maximum block light required when the monster spawns.
 piglin_safe: When false, Piglins and hoglins shake and transform to zombified entities.
 bed_works: When false, the bed blows up when trying to sleep.
 respawn_anchor_works: When false, the respawn anchor blows up when trying to set spawn point.
 has_raids: Whether players with the Bad Omen effect can cause a raid.
 logical_height: The maximum height to which chorus fruits and nether portals can bring players within this dimension. This excludes portals that were already built above the limit as they still connect normally. Cannot be greater than  height.
 min_y: The minimum height in which blocks can exist within this dimension. Must be between -2032 and 2031 and be a multiple of 16 (effectively making 2016 the maximum).
 height: The total height in which blocks can exist within this dimension. Must be between 16 and 4064 and be a multiple of 16. The maximum building height = min_y + height - 1, which cannot be greater than 2031.
 infiniburn: A block tag with #. Fires on these blocks burns infinitely.
 effects: (optional, defaults to minecraft:overworld) Can be "minecraft:overworld", "minecraft:the_nether" and "minecraft:the_end". Determines the dimension effect used for this dimension. Setting to overworld makes the dimension have clouds, sun, stars and moon. Setting to the nether makes the dimension have thick fog blocking that sight, similar to the nether. Setting to the end makes the dimension have dark spotted sky similar to the end, ignoring the sky and fog color.



## Noise generator
A custom dimension using the noise chunk generator that is entirely plains.
To have overworld-like terrain in the custom dimension, the noise generator type can be used.

data/tutorial/dimension/example_world.json
{
  "type": "tutorial:example_world",
  "generator": {
    "type": "minecraft:noise",
    "settings": "minecraft:overworld",
    "biome_source": {
      "type": "minecraft:fixed",
      "biome": "minecraft:plains"
    }
  }
}

## Noise settings
Custom noise settings with calcite as the default block.
The above example reused the minecraft:overworld noise settings, which assume the world stretches from Y=-64 to Y=320. It also includes unnecessary logic for vanilla biomes. To customize the noise settings a file can be created in worldgen/noise_settings. This example changes the base to calcite, disables ore veins, and adds a grass block layer on top of the surface.

Because this file is very large by default, it is best to start from the vanilla files. You have a few options:

- Extract the file from theversion jar
- Download the file directly from a public repository:overworld.json

data/tutorial/worldgen/noise_settings/example_world.json
{
  "sea_level": 63,
  "disable_mob_generation": false,
  "aquifers_enabled": true,
  "ore_veins_enabled": false,
  "legacy_random_source": false,
  "default_block": {
    "Name": "minecraft:calcite"
  },
  "default_fluid": {
    "Name": "minecraft:water",
    "Properties": {
      "level": "0"
    }
  },
  "noise": {
    "min_y": 0,
    "height": 256,
    "size_horizontal": 1,
    "size_vertical": 2
  },
  "noise_router": {
    // ... (keep the same as the vanilla overworld)
  },
  "spawn_target": [],
  "surface_rule": {
    "type": "minecraft:condition",
    "if_true": {
      "type": "minecraft:stone_depth",
      "offset": 0,
      "surface_type": "floor",
      "add_surface_depth": false,
      "secondary_depth_range": 0
    },
    "then_run": {
      "type": "minecraft:block",
      "result_state": {
        "Name": "minecraft:grass_block",
        "Properties": {
          "snowy": "false"
        }
      }
    }
  }
}

data/tutorial/dimension/example_world.json
{
  "type": "tutorial:example_world",
  "generator": {
    "type": "minecraft:noise",
    "settings": "tutorial:example_world",
    "biome_source": {
      "type": "minecraft:fixed",
      "biome": "minecraft:plains"
    }
  }
}


Full noise settings JSON format

: Root object.

 sea_level: The sea level in this dimension. Note that this value only affects world generation. The sea level for mob spawning is a fixed value 63.
 disable_mob_generation: Disables creature spawning upon chunk generation.
 ore_veins_enabled: Whether ore veins generate.
 aquifers_enabled: Whether aquifers generate. If set to false, almost all caves below sea level are filled with water.
 legacy_random_source: Whether to use the old random number generator from before 1.18 for world generation.
 default_block: The default block used for the terrain.
Block state
 default_fluid: The default block used for seas and lakes.
Block state
 spawn_target: (Required, but can be empty) A list of climate parameters to specify the points around which the player tries to spawn. The game selects some horizonal locations that are not more than 2560 blocks away from the origin (0,0), then sample the noise values ("depth" noise and "offset" are always 0), and calculate ((x^2+z^2)^2) / 390625 + (the square of the mininum distance to the ranges in the list). The player spawns near the location where this value is smallest.
：A range.
Noise parameter for biome (See Biome for usages of each parameter in vanilla game)
 noise: Fields for world generation.
 min_y: The minimum Y coordinate where terrain starts generating. Value between -2032 and 2031 (both inclusive). Must be divisible by 16.
 height: The total height where terrain generates. Value between 0 and 4064 (both inclusive). Must be divisible by 16. And min_y + height cannot exceed 2032.
 size_horizontal: Value between 0 and 4 (both inclusive)
 size_vertical: Value between 0 and 4 (both inclusive)
 noise_router: The noise router routes density functions to noise parameters used for world generation.
 surface_rule: The main surface rule to place blocks in the terrain.



## Noise router
In the last step the noise router was left untouched from the vanilla overworld. But this creates a problem at the bottom of the world since this custom dimension starts at Y=0 and the noise router still assumes it starts at Y=-64. This causes holes at the bottom of the world where the void is exposed.

The fix is in final_density in the noise router. Two fixes need to be made. Find the following pieces of code inside the noise settings file and replace it with the fixed versions. The first issue can also be fixed in the initial_density_without_jaggedness part of the noise router on line 74, but this is less critical. The second fix disables noodle caves.

| Before                                                                                                                         | After                                                                                                                       |
|--------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| "argument1": {   "type": "minecraft:y_clamped_gradient",   "from_y": -64,   "to_y": -40,   "from_value": 0,   "to_value": 1 }, | "argument1": {   "type": "minecraft:y_clamped_gradient",   "from_y": 0,   "to_y": 24,   "from_value": 0,   "to_value": 1 }, |
| "argument2": "minecraft:overworld/caves/noodle"                                                                                | "argument2": 1                                                                                                              |

- Before: Large holes at the bottom of the world.
- After: All caves are blocked off with solid blocks.

## Surface rules
A vertical gradient of bedrock at the bottom of the world.
A dirt layer below the grass blocks.
Right now the only surface blocks are calcite and grass blocks. You can add a dirt layer below the grass blocks and a bedrock gradient at the bottom of the world with some more complicated surface rules.

data/tutorial/worldgen/noise_settings/example_world.json
{
  // ...
  "surface_rule": {
    "type": "minecraft:sequence",
    "sequence": [
      {
        "type": "minecraft:condition",
        "if_true": {
          "type": "minecraft:vertical_gradient",
          "random_name": "minecraft:bedrock_floor",
          "true_at_and_below": {
            "above_bottom": 0
          },
          "false_at_and_above": {
            "above_bottom": 5
          }
        },
        "then_run": {
          "type": "minecraft:block",
          "result_state": {
            "Name": "minecraft:bedrock"
          }
        }
      },
      {
        "type": "minecraft:condition",
        "if_true": {
          "type": "minecraft:stone_depth",
          "offset": 0,
          "surface_type": "floor",
          "add_surface_depth": false,
          "secondary_depth_range": 0
        },
        "then_run": {
          "type": "minecraft:block",
          "result_state": {
            "Name": "minecraft:grass_block",
            "Properties": {
              "snowy": "false"
            }
          }
        }
      },
      {
        "type": "minecraft:condition",
        "if_true": {
          "type": "minecraft:stone_depth",
          "offset": 0,
          "surface_type": "floor",
          "add_surface_depth": true,
          "secondary_depth_range": 0
        },
        "then_run": {
          "type": "minecraft:block",
          "result_state": {
            "Name": "minecraft:dirt"
          }
        }
      }
    ]
  }
}

## Biome
A custom biome with modified colors and a few features.
The example dimension is still using the minecraft:plains biome. To change grass color, structures, features, spawning rules, and more you need a custom biome. This example adds the tutorial:plains biome, which modifies the grass and foliage colors.

A few features are added in the 10th decoration step, which is vegetal_decoration. If you want to add ores, they would go in step 7: underground_ores.

data/tutorial/worldgen/biome/plains.json
{
  "temperature": 0.8,
  "downfall": 0.4,
  "has_precipitation": true,
  "effects": {
    "sky_color": 7907327,
    "fog_color": 12638463,
    "water_color": 4159204,
    "water_fog_color": 329011,
    "grass_color": 10073398,
    "foliage_color": 13127730
  },
  "spawners": {},
  "spawn_costs": {},
  "carvers": {},
  "features": [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [
      "minecraft:glow_lichen",
      "minecraft:trees_plains",
      "minecraft:patch_grass_plain",
      "minecraft:patch_sugar_cane"
    ],
    []
  ]
}

data/tutorial/dimension/example_world.json
{
  "type": "tutorial:example_world",
  "generator": {
    "type": "minecraft:noise",
    "settings": "tutorial:example_world",
    "biome_source": {
      "type": "minecraft:fixed",
      "biome": "tutorial:plains"
    }
  }
}

An interactive widget is being loaded. If this does not work for you, please reload the page or check if JavaScript is enabled.
