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



