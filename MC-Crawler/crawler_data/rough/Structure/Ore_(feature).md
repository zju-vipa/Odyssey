# Ore (feature)
An ore[1][2][3] is a feature consisting of a natural deposit of ores or other blocks in the ground.

## Contents
- 1 Generation
- 2 List
	- 2.1 Overworld
	- 2.2 The Nether
- 3 Data values
	- 3.1 ID
	- 3.2 Config
- 4 History
- 5 Gallery
	- 5.1 Renders
	- 5.2 Screenshots
- 6 References

## Generation
The ore feature has two types: ore blobs and scatter ores.

An ore blob is an ellipsoidal cluster of blocks. In the overworld, underground deposits of dirt and gravel are generated in this form, followed by the more precious ores, like coal, copper, iron, gold, redstone, diamond, emerald (in mountains biomes) and lapis lazuli. They can form only in stone, deepslate, andesite, diorite, granite and tuff‌[JE  only] (also in their polished variants in Bedrock Edition, replacing parts of structures). Two or more ores can form next to each other and appear as an ore made of more than one material.

Each ore blob has a spawn size. The maximum number of generated blocks in a blob each spawn size corresponds to is shown in the table below[4]:

| Spawn size | Max number of blocks |
|------------|----------------------|
| 0          | 0                    |
| 1          | 0                    |
| 2          | 0                    |
| 3          | 4                    |
| 4          | 5                    |
| 5          | 8                    |
| 6          | 9                    |
| 7          | 10                   |
| 8          | 10                   |
| 9          | 13                   |
| 10         | 16                   |
| 11         | 17                   |
| 12         | 23                   |
| 13         | 24                   |
| 14         | 24                   |
| 15         | 29                   |
| 16         | 32                   |
| 17         | 37                   |
| 18         | 46                   |
| 19         | 52                   |
| 20         | 52                   |
| 21         | 60                   |
| 22         | 68                   |
| 23         | 68                   |
| 24         | 74                   |
| 25         | 82                   |
| 26         | 94                   |
| 27         | 104                  |
| 28         | 106                  |
| 29         | 120                  |
| 30         | 128                  |
| 31         | 135                  |
| 32         | 149                  |
| 33         | 160                  |
| 34         | 180                  |
| 35         | 190                  |
| 36         | 204                  |
| 37         | 212                  |
| 38         | 228                  |
| 39         | 246                  |
| 40         | 262                  |
| 41         | 276                  |
| 42         | 292                  |
| 43         | 308                  |
| 44         | 324                  |
| 45         | 344                  |
| 46         | 360                  |
| 47         | 381                  |
| 48         | 403                  |
| 49         | 429                  |
| 50         | 452                  |
| 51         | 480                  |
| 52         | 500                  |
| 53         | 530                  |
| 54         | 558                  |
| 55         | 584                  |
| 56         | 616                  |
| 57         | 634                  |
| 58         | 664                  |
| 59         | 694                  |
| 60         | 730                  |
| 61         | 760                  |
| 62         | 790                  |
| 63         | 826                  |
| 64         | 864                  |

A scatter ore is a slightly dispersed cluster of blocks. Currently only ancient debris is generated in this form. Scatter ores also have a spawn size value. The maximum number of generated blocks in a scatter ore is just the spawn size.

There was also a deprecated ore type, which generates only one block in each generation attempt. It was used by emerald ore before 1.18.

## List
| Dimension  | Block                                                                                                                                                                                                                                                                                                                                                                                                                               | Can replace                                                                                                         |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Overworld  | Andesite Clay (Only in lush caves) Coal Ore Copper Ore Diamond Ore Diorite Dirt Emerald Ore (Only in mountains and windswept hills biomes) Gold Ore Granite Gravel Infested Stone (Only in mountains and windswept hills biomes) Iron Ore Lapis Lazuli Ore Redstone Ore Tuff                                                                                                                                                        | Andesite Diorite Granite Polished Andesite‌[BE  only] Polished Diorite‌[BE  only] Polished Granite‌[BE  only] Stone |
|            | Andesite‌[JE  only] Clay‌[JE  only] (Only in lush caves) Deepslate Coal Ore Deepslate Copper Ore Deepslate Diamond Ore Diorite‌[JE  only] Dirt‌[JE  only] Deepslate Emerald Ore (Only in mountain biomes and windswept hills biomes) Deepslate Gold Ore Granite‌[JE  only] Gravel Infested Deepslate (Only in mountain biomes and windswept hills biomes) Deepslate Iron Ore Deepslate Lapis Lazuli Ore Deepslate Redstone Ore Tuff | Deepslate Tuff‌[JE  only]                                                                                           |
| The Nether | Ancient Debris<br/>                                                                                                                                                                                                                                                                                                                                                                                                                 | Basalt‌[JE  only] Blackstone‌[JE  only] Netherrack                                                                  |
|            | Blackstone Gravel Nether Gold Ore Nether Quartz Ore Soul Sand                                                                                                                                                                                                                                                                                                                                                                       | Netherrack<br/>                                                                                                     |
|            | Magma Block                                                                                                                                                                                                                                                                                                                                                                                                                         | Netherrack<br/>Blackstone‌[BE  only]<br/>                                                                           |

### Overworld
| Blocks                                          | Spawn size                        | Spawn tries per chunk          | Minimum height                  | Maximum height                  | Ore concentrate[note 1] | Skipped when air exposed[note 2] | Biomes                                                                                                                                                                                                                                                     |
|-------------------------------------------------|-----------------------------------|--------------------------------|---------------------------------|---------------------------------|-------------------------|----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Dirt                                            | 33                                | 7                              | 0                               | 160                             | Uniform                 | 0                                | All                                                                                                                                                                                                                                                        |
| Clay                                            | 33                                | 46                             | -64                             | 256                             | Uniform                 | 0                                | Lush Caves                                                                                                                                                                                                                                                 |
| Gravel                                          | 33                                | 14                             | -64                             | 320                             | Uniform                 | 0                                | All                                                                                                                                                                                                                                                        |
| Granite                                         | 64                                | 2                              | 0                               | 60                              | Uniform                 | 0                                | All                                                                                                                                                                                                                                                        |
|                                                 |                                   | $\frac{1}{6}$                  | 64                              | 128                             |                         |                                  |                                                                                                                                                                                                                                                            |
| Diorite                                         | 64                                | 2                              | 0                               | 60                              | Uniform                 | 0                                | All                                                                                                                                                                                                                                                        |
|                                                 |                                   | $\frac{1}{6}$                  | 64                              | 128                             |                         |                                  |                                                                                                                                                                                                                                                            |
| Andesite                                        | 64                                | 2                              | 0                               | 60                              | Uniform                 | 0                                | All                                                                                                                                                                                                                                                        |
|                                                 |                                   | $\frac{1}{6}$                  | 64                              | 128                             |                         |                                  |                                                                                                                                                                                                                                                            |
| Tuff                                            | 64                                | 2                              | -64                             | 0                               | Uniform                 | 0                                | All                                                                                                                                                                                                                                                        |
| Coal Ore<br/>Deepslate Coal Ore                 | 17                                | 20                             | 0                               | 192                             | Triangle                | 0.5                              | All                                                                                                                                                                                                                                                        |
|                                                 |                                   | 30                             | 136                             | 320                             | Uniform                 | 0                                |                                                                                                                                                                                                                                                            |
|                                                 |                                   | 0‌[JE  only]<br/>20‌[BE  only] | 128                             | 156                             | Uniform                 | 0                                | Grove<br/>Cherry Grove<br/>Jagged Peaks<br/>Meadow<br/>Frozen Peaks<br/>Stony Peaks<br/>Snowy Slopes                                                                                                                                                       |
| Iron Ore<br/>Deepslate Iron Ore                 | 4                                 | 10                             | -64                             | 72                              | Uniform                 | 0                                | All                                                                                                                                                                                                                                                        |
|                                                 | 9‌[JE  only]<br/>10‌[BE  only][5] | 10                             | -24                             | 56                              | Triangle                | 0                                |                                                                                                                                                                                                                                                            |
|                                                 |                                   | 90                             | 80                              | 384                             | Triangle                | 0                                |                                                                                                                                                                                                                                                            |
| Copper Ore<br/>Deepslate Copper Ore             | 10                                | 16                             | -16                             | 112                             | Triangle                | 0                                | Other                                                                                                                                                                                                                                                      |
|                                                 | 20                                |                                |                                 |                                 |                         |                                  | Dripstone Caves                                                                                                                                                                                                                                            |
| Redstone Ore<br/>Deepslate Redstone Ore         | 8                                 | 4                              | -64                             | 15                              | Uniform                 | 0                                | All                                                                                                                                                                                                                                                        |
|                                                 |                                   | 8                              | -64                             | -32                             | Triangle                |                                  |                                                                                                                                                                                                                                                            |
| Lapis Lazuli Ore<br/>Deepslate Lapis Lazuli Ore | 7                                 | 2                              | -32                             | 32                              | Triangle                | 0                                | All                                                                                                                                                                                                                                                        |
|                                                 |                                   | 4                              | -64                             | 64                              | Uniform                 | 1                                |                                                                                                                                                                                                                                                            |
| Gold Ore<br/>Deepslate Gold Ore                 | 9                                 | 4                              | -64                             | 32                              | Triangle                | 0.5                              | All                                                                                                                                                                                                                                                        |
|                                                 |                                   | $\frac{1}{2}$                  | -64                             | -48                             | Uniform                 | 0.5                              | All                                                                                                                                                                                                                                                        |
|                                                 |                                   | 50                             | 32                              | 256                             | Uniform                 | 0                                | Badlands<br/>Eroded Badlands<br/>Wooded Badlands<br/>Badlands Plateau‌[BE  only](Unused)<br/>Modified Badlands Plateau‌[BE  only](Unused)<br/>Modified Wooded Badlands Plateau‌[BE  only](Unused)                                                          |
| Diamond Ore<br/>Deepslate Diamond Ore           | 4                                 | 7                              | -64                             | 16                              | Triangle                | 0.5                              | All                                                                                                                                                                                                                                                        |
|                                                 | 8                                 | 4                              |                                 |                                 |                         | 1                                |                                                                                                                                                                                                                                                            |
|                                                 | 12                                | $\frac{1}{9}$                  |                                 |                                 |                         | 0.7                              |                                                                                                                                                                                                                                                            |
|                                                 | 8                                 | 2                              | -64                             | -4                              | Uniform                 | 0.5                              |                                                                                                                                                                                                                                                            |
| Emerald Ore<br/>Deepslate Emerald Ore           | 3                                 | 100                            | -16                             | 480                             | Triangle                | 0                                | Windswept Hills<br/>Grove<br/>Cherry Grove<br/>Jagged Peaks<br/>Meadow<br/>Frozen Peaks<br/>Stony Peaks<br/>Windswept Forest<br/>Snowy Slopes<br/>Windswept Gravelly Hills<br/>Mountain Edge‌[BE  only](Unused)<br/>Gravelly Mountains+‌[BE  only](Unused) |
| Infested Stone<br/>Infested Deepslate           | 9‌[JE  only]<br/>8‌[BE  only]     | 14                             | -64‌[JE  only]<br/>0‌[BE  only] | 63‌[JE  only]<br/>64‌[BE  only] | Uniform                 | 0                                | Windswept Hills<br/>Grove<br/>Cherry Grove<br/>Jagged Peaks<br/>Meadow<br/>Frozen Peaks<br/>Stony Peaks<br/>Windswept Forest<br/>Snowy Slopes<br/>Windswept Gravelly Hills<br/>Mountain Edge‌[BE  only](Unused)<br/>Gravelly Mountains+‌[BE  only](Unused) |

### The Nether
| Blocks            | Spawn size                      | Spawn tries per chunk           | Minimum height                  | Maximum height                  | Ore concentrate[note 1]                    | Skipped when air exposed[note 2] | Biomes                                                          |
|-------------------|---------------------------------|---------------------------------|---------------------------------|---------------------------------|--------------------------------------------|----------------------------------|-----------------------------------------------------------------|
| Magma Block       | 33‌[JE  only]<br/>28‌[BE  only] | 4‌[JE  only]<br/>9‌[BE  only]   | 27‌[JE  only]<br/>23‌[BE  only] | 36                              | Uniform                                    | 0                                | All                                                             |
| Nether Quartz Ore | 14                              | 16                              | 10                              | 117                             | Uniform                                    | 0                                | Others                                                          |
|                   |                                 | 32‌[JE  only]<br/>16‌[BE  only] |                                 |                                 |                                            |                                  | Basalt Deltas                                                   |
| Nether Gold Ore   | 10                              | 10                              | 10                              | 117                             | Uniform                                    | 0                                | Others                                                          |
|                   |                                 | 20‌[JE  only]<br/>10‌[BE  only] |                                 |                                 |                                            |                                  | Basalt Deltas                                                   |
| Ancient Debris    | 3                               | 1‌[JE  only]<br/>2‌[BE  only]   | 8                               | 24‌[JE  only]<br/>23‌[BE  only] | Triangle‌[JE  only]<br/>Uniform‌[BE  only] | 1                                | All                                                             |
|                   | 2                               | 1‌[JE  only]<br/>3‌[BE  only]   | 8                               | 119                             | Uniform                                    |                                  |                                                                 |
| Soul Sand         | 12                              | 12                              | 0                               | 31‌[JE  only]<br/>32‌[BE  only] | Uniform                                    | 0                                | Soul Sand Valley                                                |
| Gravel            | 33                              | 2                               | 5                               | 41‌[JE  only]<br/>36‌[BE  only] | Uniform                                    | 0                                | Nether Wastes<br/>Crimson Forest Warped Forest Soul Sand Valley |
| Blackstone        | 33                              | 2                               | 5                               | 31‌[JE  only]<br/>36‌[BE  only] | Uniform                                    | 0                                | Nether Wastes<br/>Crimson Forest Warped Forest Soul Sand Valley |

1. ↑ a bOres generate using either uniform distribution, or triangle distribution. Uniform distribution have all ores spread in same frequency at any height, while triangle generate more frequent in center height.
2. ↑ a bWhen an ore block is about to be placed, if it is exposed to air then it has this chance of being skipped instead.

## Data values
### ID
Java Edition:

| Feature type        | Identifier      |
|---------------------|-----------------|
| [No displayed name] | `ore`           |
| [No displayed name] | `scattered_ore` |

| Configured feature  | Identifier                 |
|---------------------|----------------------------|
| [No displayed name] | `ore_ancient_debris_large` |
| [No displayed name] | `ore_ancient_debris_small` |
| [No displayed name] | `ore_andesite`             |
| [No displayed name] | `ore_blackstone`           |
| [No displayed name] | `ore_clay`                 |
| [No displayed name] | `ore_coal`                 |
| [No displayed name] | `ore_coal_buried`          |
| [No displayed name] | `ore_copper_large`         |
| [No displayed name] | `ore_copper_small`         |
| [No displayed name] | `ore_diamond_buried`       |
| [No displayed name] | `ore_diamond_large`        |
| [No displayed name] | `ore_diamond_small`        |
| [No displayed name] | `ore_diorite`              |
| [No displayed name] | `ore_dirt`                 |
| [No displayed name] | `ore_emerald`              |
| [No displayed name] | `ore_gold`                 |
| [No displayed name] | `ore_gold_buried`          |
| [No displayed name] | `ore_granite`              |
| [No displayed name] | `ore_gravel`               |
| [No displayed name] | `ore_gravel_nether`        |
| [No displayed name] | `ore_infested`             |
| [No displayed name] | `ore_iron`                 |
| [No displayed name] | `ore_iron_small`           |
| [No displayed name] | `ore_lapis`                |
| [No displayed name] | `ore_lapis_buried`         |
| [No displayed name] | `ore_magma`                |
| [No displayed name] | `ore_nether_gold`          |
| [No displayed name] | `ore_quartz`               |
| [No displayed name] | `ore_redstone`             |
| [No displayed name] | `ore_soul_sand`            |
| [No displayed name] | `ore_tuff`                 |

Bedrock Edition:

| Feature             | Identifier                             |
|---------------------|----------------------------------------|
| [No displayed name] | `andesite_feature`                     |
| [No displayed name] | `clay_ore_feature`                     |
| [No displayed name] | `coal_ore_feature`                     |
| [No displayed name] | `coal_ore_upper_feature`               |
| [No displayed name] | `copper_ore_feature`                   |
| [No displayed name] | `deepslate_feature`                    |
| [No displayed name] | `diamond_ore_buried_feature`           |
| [No displayed name] | `diamond_ore_feature`                  |
| [No displayed name] | `diamond_ore_large_feature`            |
| [No displayed name] | `diorite_feature`                      |
| [No displayed name] | `dirt_feature`                         |
| [No displayed name] | `dripstone_caves_copper_ore_feature`   |
| [No displayed name] | `emerald_ore_feature`                  |
| [No displayed name] | `gold_ore_extra_feature`               |
| [No displayed name] | `gold_ore_feature`                     |
| [No displayed name] | `gold_ore_lower_feature`               |
| [No displayed name] | `granite_feature`                      |
| [No displayed name] | `gravel_ore_feature`                   |
| [No displayed name] | `iron_ore_feature`                     |
| [No displayed name] | `iron_ore_small_feature`               |
| [No displayed name] | `lapis_ore_buried_feature`             |
| [No displayed name] | `lapis_ore_feature`                    |
| [No displayed name] | `nether_soul_sand_underground_feature` |
| [No displayed name] | `redstone_ore_feature`                 |
| [No displayed name] | `silverfish_feature`                   |
| [No displayed name] | `tuff_feature`                         |
| [No displayed name] | `nether_gold_ore_feature`              |
| [No displayed name] | `nether_gravel_underground_feature`    |
| [No displayed name] | `nether_quartz_ore_feature`            |
| [No displayed name] | `nether_magma_feature`                 |
| [No displayed name] | `blackstone_feature`                   |
| [No displayed name] | `nether_netherite_deep_feature`        |
| [No displayed name] | `nether_netherite_tall_feature`        |

### Config
Main article: Configured feature
Java Edition:

- config
	- sizeValue between 0 and 64 (inclusive). Determine the volume size of the ore. See alsoOre_(feature).
	- discard_chance_on_air_exposureValue between 0 and 1 (inclusive). The chance for an ore block to be discarded when it is exposed to air. Setting this to 1 makes the ore completely hidden.
	- targets(Required, but can be empty) A list of targets.
		- A target.
			- targetRule test. The blocks to replace.
				- 
				- A rule test
			- stateThe block to use.
				- 
				- Block state


An example

{
  "type": "minecraft:ore",
  "config": {
    "discard_chance_on_air_exposure": 0.5,
    "size": 4,
    "targets": [
      {
        "state": {
          "Name": "minecraft:diamond_ore"
        },
        "target": {
          "predicate_type": "minecraft:tag_match",
          "tag": "minecraft:stone_ore_replaceables"
        }
      },
      {
        "state": {
          "Name": "minecraft:deepslate_diamond_ore"
        },
        "target": {
          "predicate_type": "minecraft:tag_match",
          "tag": "minecraft:deepslate_ore_replaceables"
        }
      }
    ]
  }
}



