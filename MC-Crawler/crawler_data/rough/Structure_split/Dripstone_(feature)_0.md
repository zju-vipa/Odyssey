# Dripstone (feature)
Dripstone features can be found commonly in dripstone caves biomes. There are three types of dripstone feature: large dripstone, dripstone cluster and pointed dripstone (also known as small dripstone).

## Contents
- 1 Description
- 2 Data values
	- 2.1 ID
	- 2.2 Config
- 3 History
- 4 Issues
- 5 Trivia
- 6 Gallery
	- 6.1 Screenshots
- 7 References

## Description
Dripstone features generate inside large hollows in the dripstone caves biome. They can generate in water.

There are three types of dripstone feature:

- The first type is the "large dripstone", which takes the form of either a separated stalagmite and stalactite, or a stalagnate, and is composed ofdripstone blocks. Stalagnates generate around two positions selected on the floor and ceiling of a cave, which may potentially be separated by several blocks horizontally. The maximum possible size of a large dripstone varies depending on the available space.

- The second type is the "dripstone cluster", a patch of dripstone blocks replacing a section of a cave’s walls, floor and ceiling. Somepointed dripstoneblocks will generate hanging from the ceiling and growing on the floor in these patches, attached to the dripstone blocks, forming detailed speleothem growths.Waterpuddles can also occasionally be found on the floor patches.

- The third type is the "pointed dripstone", which is similar to the dripstone cluster, but only has a single stalagmite or stalactite.

When these types overlap, it results in pointed dripstone generating on the large columns of dripstone blocks.

## Data values
### ID
Java Edition:

| Feature type        | Identifier          |
|---------------------|---------------------|
| [No displayed name] | `large_dripstone`   |
| [No displayed name] | `dripstone_cluster` |
| [No displayed name] | `pointed_dripstone` |

| Configured feature  | Identifier          |
|---------------------|---------------------|
| [No displayed name] | `large_dripstone`   |
| [No displayed name] | `dripstone_cluster` |
| [No displayed name] | `pointed_dripstone` |

Bedrock Edition:

| Feature             | Identifier                  |
|---------------------|-----------------------------|
| [No displayed name] | `dripstone_cluster_feature` |
| [No displayed name] | `large_dripstone_feature`   |

| Feature             | Identifier                  |
|---------------------|-----------------------------|
| [No displayed name] | `pointed_dripstone_feature` |

which is used in:

| Feature             | Identifier                                |
|---------------------|-------------------------------------------|
| [No displayed name] | `small_dripstone_snap_to_surface_feature` |

which is used in:

| Feature             | Identifier                |
|---------------------|---------------------------|
| [No displayed name] | `small_dripstone_feature` |

### Config
Main article: Configured feature
Java Edition:

If type is dripstone_cluster:

- config
	- floor_to_ceiling_search_rangeFor how many blocks the feature searches for the floor or ceiling. Value between 1 and 512 (inclusive).
	- heightThe height of the cluster. Value between 1 and 128 (inclusive).
		- 
		- Int provider
	- radiusThe radius of the cluster. Value between 1 and 128 (inclusive).
		- 
		- Int provider
	- max_stalagmite_stalactite_height_diffThe maximum height difference between stalagmites and stalactites. Value between 0 and 64 (inclusive).
	- height_deviationThe height deviation. Value between 1 and 64 (inclusive).
	- dripstone_block_layer_thicknessThe dripstone block layer's thickness. Value between 0 and 128 (inclusive).
		- 
		- Int provider
	- densityValue between 0.0 and 2.0 (inclusive).
		- 
		- Float provider
	- wetnessValue between 0.0 and 2.0 (inclusive).
		- 
		- Float provider
	- chance_of_dripstone_column_at_max_distance_from_centerValue between 0.0 and 1.0 (inclusive).
	- max_distance_from_edge_affecting_chance_of_dripstone_columnValue between 1 and 64 (inclusive).
	- max_distance_from_center_affecting_height_biasValue between 1 and 64 (inclusive).


An example

{
  "type": "minecraft:dripstone_cluster",
  "config": {
    "chance_of_dripstone_column_at_max_distance_from_center": 0.1,
    "density": {
      "type": "minecraft:uniform",
      "value": {
        "max_exclusive": 0.7,
        "min_inclusive": 0.3
      }
    },
    "dripstone_block_layer_thickness": {
      "type": "minecraft:uniform",
      "value": {
        "max_inclusive": 4,
        "min_inclusive": 2
      }
    },
    "floor_to_ceiling_search_range": 12,
    "height": {
      "type": "minecraft:uniform",
      "value": {
        "max_inclusive": 6,
        "min_inclusive": 3
      }
    },
    "height_deviation": 3,
    "max_distance_from_center_affecting_height_bias": 8,
    "max_distance_from_edge_affecting_chance_of_dripstone_column": 3,
    "max_stalagmite_stalactite_height_diff": 1,
    "radius": {
      "type": "minecraft:uniform",
      "value": {
        "max_inclusive": 8,
        "min_inclusive": 2
      }
    },
    "wetness": {
      "type": "minecraft:clamped_normal",
      "value": {
        "deviation": 0.3,
        "max": 0.9,
        "mean": 0.1,
        "min": 0.1
      }
    }
  }
}



If type is large_dripstone:

- config
	- floor_to_ceiling_search_range(optional, defaults to 30) The search range from start point to cave floor or ceiling (rather than from floor to ceiling). Value between 1 and 512 (inclusive).
	- column_radiusUsed to provide a min and max value for radius. Note that this int provider doesn't provide a single int, but provides the min and max value of the specified distribution. Value between 1 and 60 (inclusive). Seethe graph for details.
		- 
		- Int provider
	- height_scaleHigher value leads to higher height. Value between 0.0 and 20.0 (inclusive).
		- 
		- Float provider
	- max_column_radius_to_cave_height_ratioThe ratio of the max radius to the height of the cave. Value between 0.0 and 1.0 (inclusive).
	- stalactite_bluntnessTruncate the tip of stalactite. Higher value leads to lower height. Value between 0.1 and 10.0 (inclusive).
		- 
		- Float provider
	- stalagmite_bluntnessTruncate the tip of stalagmite. Higher value leads to lower height. Value between 0.1 and 10.0 (inclusive).
		- 
		- Float provider
	- wind_speedLarger value results in larger inclination. Value between 0.0 and 2.0 (inclusive).
		- 
		- Float provider
	- min_radius_for_windThe min column radius to used for the wind. Value between 0 and 100.
	- min_bluntness_for_windThe min value of the bluntnesses to used for the wind. Value between 0.0 and 5.0 (inclusive).


An example

{
  "type": "minecraft:large_dripstone",
  "config": {
    "column_radius": {
      "type": "minecraft:uniform",
      "value": {
        "max_inclusive": 19,
        "min_inclusive": 3
      }
    },
    "floor_to_ceiling_search_range": 30,
    "height_scale": {
      "type": "minecraft:uniform",
      "value": {
        "max_exclusive": 2.0,
        "min_inclusive": 0.4
      }
    },
    "max_column_radius_to_cave_height_ratio": 0.33,
    "min_bluntness_for_wind": 0.6,
    "min_radius_for_wind": 4,
    "stalactite_bluntness": {
      "type": "minecraft:uniform",
      "value": {
        "max_exclusive": 0.9,
        "min_inclusive": 0.3
      }
    },
    "stalagmite_bluntness": {
      "type": "minecraft:uniform",
      "value": {
        "max_exclusive": 1.0,
        "min_inclusive": 0.4
      }
    },
    "wind_speed": {
      "type": "minecraft:uniform",
      "value": {
        "max_exclusive": 0.3,
        "min_inclusive": 0.0
      }
    }
  }
}



If type is pointed_dripstone:

- config
	- chance_of_taller_dripstone(optional, defaults to 0.2) Value between 0.0 and 1.0 (inclusive). Probability for double-block dripstone.
	- chance_of_directional_spread(optional, defaults to 0.7) Value between 0.0 and 1.0 (inclusive). Probability that the dripstone spreads in a horizontal direction.
	- chance_of_spread_radius2(optional, defaults to 0.5) Value between 0.0 and 1.0 (inclusive). Probability of horizontal spread by two blocks.
	- chance_of_spread_radius3(optional, defaults to 0.5) Value between 0.0 and 1.0 (inclusive). After the spread by two blocks, probability of spreading the third block.


An example

{
  "type": "minecraft:pointed_dripstone",
  "config": {
    "chance_of_directional_spread": 0.7,
    "chance_of_spread_radius2": 0.5,
    "chance_of_spread_radius3": 0.5,
    "chance_of_taller_dripstone": 0.2
  }
}




