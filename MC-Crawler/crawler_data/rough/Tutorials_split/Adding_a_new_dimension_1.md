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

