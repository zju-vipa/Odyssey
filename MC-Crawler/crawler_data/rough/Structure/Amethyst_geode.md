# Amethyst geode
An amethyst geode is a feature found in the underground of the Overworld. Amethyst geodes contain smooth basalt, calcite, and are the main source of amethyst shards and blocks.

## Contents
- 1 Generation
- 2 Structure
- 3 Data values
	- 3.1 ID
	- 3.2 Config
- 4 History
- 5 Issues
- 6 Gallery
	- 6.1 Screenshots
	- 6.2 Concept artwork
	- 6.3 In other media
- 7 References

## Generation
Amethyst geodes generate between Y=-58 and Y=30. Each chunk has a 1⁄24 chance to attempt to generate a geode.

## Structure
The inside of a cracked amethyst geode.
Amethyst geodes consist of three layers: an outer layer of smooth basalt, a middle layer of calcite, and a hollow layer of primarily amethyst blocks, with 8.3% replaced by budding amethyst blocks instead. Amethyst crystals generate within the structure on budding amethyst. Geodes have a 95% chance of generating with a crack, exposing its inside. Caves, aquifers and canyons may be overridden by geodes,[1] and as such are often obstructed by them.

## Data values
### ID
Java Edition:

| Feature type        | Identifier |
|---------------------|------------|
| [No displayed name] | `geode`    |

| Configured feature  | Identifier       |
|---------------------|------------------|
| [No displayed name] | `amethyst_geode` |

Bedrock Edition:

| Feature             | Identifier               |
|---------------------|--------------------------|
| [No displayed name] | `amethyst_geode_feature` |

### Config
Main article: Configured feature
Java Edition:

- config
	- blocksThe blocks to use.
		- filling_providerThe block used for filling.
			- 
			- Block state provider
		- inner_layer_providerThe block of the inner layer.
			- 
			- Block state provider
		- alternate_inner_layer_providerThe alternate block of the inner layer.
			- 
			- Block state provider
		- middle_layer_providerThe block of the middle layer.
			- 
			- Block state provider
		- outer_layer_providerThe block of the outer layer.
			- 
			- Block state provider
		- inner_placements(Cannot be empty) The blocks to place in the geode.
			- A block state.
				- 
				- Block state
		- cannot_replaceA block tag with#listing which blocks not to replace.
		- invalid_blocksA block tag with#listing invalid blocks. Due toMC-264886, any value is treated as#minecraft:geode_invalid_blocks. Additionally, air is an invalid block.
	- layersThe max radius of each layer. Higher value results in higher max radius of each layer.
		- filling(optional, defaults to 1.7) Value between 0.01 and 50 (inclusive).
		- inner_layer(optional, defaults to 2.2) Value between 0.01 and 50 (inclusive).
		- middle_layer(optional, defaults to 3.2) Value between 0.01 and 50 (inclusive).
		- outer_layer(optional, defaults to 4.2) Value between 0.01 and 50 (inclusive).
	- crackThe configuration of the crack on the geode.
		- generate_crack_chance(optional, defaults to 1.0) The probability for generating crack. Value between 0.0 and 1.0 (inclusive).
		- base_crack_size(optional, defaults to 2) Value between 0.0 and 5.0 (inclusive).
		- crack_point_offset(optional, defaults to 2) Value between 0 and 10 (inclusive).
	- noise_multiplier(optional, defaults to 0.05) Value between 0.0 and 1.0 (inclusive).
	- use_potential_placements_chance(optional, defaults to 0.35) The probability for placing the inner placement on a block of inner layer. Value between 0 and 1 (inclusive).
	- use_alternate_layer0_chance(optional, defaults to 0.0) The probability of the alternate blocks on inner layer. Value between 0 and 1 (inclusive).
	- placements_require_layer0_alternate(optional, defaults to true) Whether the inner placements are only allowed on the alternate inner blocks.
	- outer_wall_distance(optional, defaults to a uniform int between 4 and 5) The offset on each coordinate of the center from the feature start. Value between 1 and 20 (inclusive).
		- 
		- Int provider
	- distribution_points(optional, defaults to a uniform int between 3 and 4) Value between 1 and 20 (inclusive).
		- 
		- Int provider
	- invalid_blocks_thresholdCheckdistribution_pointstimes near the center of the geode, and if the number of invalid blocks found exceeds this number, the feature will not be generated.
	- point_offset(optional, defaults to a uniform int between 1 and 2) Value between 1 and 10.
		- 
		- Int provider
	- min_gen_offset(optional, defaults to -16) The minimum Chebyshev distance between the block and the center.
	- max_gen_offset(optional, defaults to 16) The maximum Chebyshev distance between the block and the center.


An example

{
  "type": "minecraft:geode",
  "config": {
    "blocks": {
      "alternate_inner_layer_provider": {
        "type": "minecraft:simple_state_provider",
        "state": {
          "Name": "minecraft:budding_amethyst"
        }
      },
      "cannot_replace": "#minecraft:features_cannot_replace",
      "filling_provider": {
        "type": "minecraft:simple_state_provider",
        "state": {
          "Name": "minecraft:air"
        }
      },
      "inner_layer_provider": {
        "type": "minecraft:simple_state_provider",
        "state": {
          "Name": "minecraft:amethyst_block"
        }
      },
      "inner_placements": [
        {
          "Name": "minecraft:small_amethyst_bud",
          "Properties": {
            "facing": "up",
            "waterlogged": "false"
          }
        },
        {
          "Name": "minecraft:medium_amethyst_bud",
          "Properties": {
            "facing": "up",
            "waterlogged": "false"
          }
        },
        {
          "Name": "minecraft:large_amethyst_bud",
          "Properties": {
            "facing": "up",
            "waterlogged": "false"
          }
        },
        {
          "Name": "minecraft:amethyst_cluster",
          "Properties": {
            "facing": "up",
            "waterlogged": "false"
          }
        }
      ],
      "invalid_blocks": "#minecraft:geode_invalid_blocks",
      "middle_layer_provider": {
        "type": "minecraft:simple_state_provider",
        "state": {
          "Name": "minecraft:calcite"
        }
      },
      "outer_layer_provider": {
        "type": "minecraft:simple_state_provider",
        "state": {
          "Name": "minecraft:smooth_basalt"
        }
      }
    },
    "crack": {
      "base_crack_size": 2.0,
      "crack_point_offset": 2,
      "generate_crack_chance": 0.95
    },
    "distribution_points": {
      "type": "minecraft:uniform",
      "value": {
        "max_inclusive": 4,
        "min_inclusive": 3
      }
    },
    "invalid_blocks_threshold": 1,
    "layers": {
      "filling": 1.7,
      "inner_layer": 2.2,
      "middle_layer": 3.2,
      "outer_layer": 4.2
    },
    "max_gen_offset": 16,
    "min_gen_offset": -16,
    "noise_multiplier": 0.05,
    "outer_wall_distance": {
      "type": "minecraft:uniform",
      "value": {
        "max_inclusive": 6,
        "min_inclusive": 4
      }
    },
    "placements_require_layer0_alternate": true,
    "point_offset": {
      "type": "minecraft:uniform",
      "value": {
        "max_inclusive": 2,
        "min_inclusive": 1
      }
    },
    "use_alternate_layer0_chance": 0.083,
    "use_potential_placements_chance": 0.35
  }
}



