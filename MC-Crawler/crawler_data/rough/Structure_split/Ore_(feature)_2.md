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




