# Underwater magma
Underwater magma is a feature found underwater in the Overworld.

## Contents
- 1 Generation
- 2 Data values
	- 2.1 ID
	- 2.2 Config
- 3 History
- 4 References

## Generation
An underwater magma is a feature made entirely of magma blocks. It is up to 3×3×3 in size. It can be found at the underwater floor in any Overworld biome.

## Data values
### ID
Java Edition:

| Feature type        | Identifier         |
|---------------------|--------------------|
| [No displayed name] | `underwater_magma` |

| Configured feature  | Identifier         |
|---------------------|--------------------|
| [No displayed name] | `underwater_magma` |

Bedrock Edition:

| Feature             | Identifier                 |
|---------------------|----------------------------|
| [No displayed name] | `underwater_magma_feature` |

which is used in:

| Feature             | Identifier                                 |
|---------------------|--------------------------------------------|
| [No displayed name] | `underwater_magma_snap_to_surface_feature` |

which is used in:

| Feature             | Identifier                             |
|---------------------|----------------------------------------|
| [No displayed name] | `underwater_magma_underground_feature` |

### Config
Main article: Configured feature
Java Edition:

- config
	- floor_search_rangeValue between 0 and 512 (inclusive).
	- placement_radius_around_floorValue between 0 and 64 (inclusive).
	- placement_probability_per_valid_positionValue between 0.0 and 1.0 (inclusive).


An example

{
  "type": "minecraft:underwater_magma",
  "config": {
    "floor_search_range": 5,
    "placement_probability_per_valid_position": 0.5,
    "placement_radius_around_floor": 1
  }
}



