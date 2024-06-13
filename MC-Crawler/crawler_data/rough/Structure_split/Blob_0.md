# Blob
A blob is a feature consisting of basalt or blackstone blocks, which replaces netherrack blocks during world generation.

## Contents
- 1 Types
- 2 Data values
	- 2.1 ID
	- 2.2 Config
- 3 History
- 4 Gallery
	- 4.1 Screenshots

## Types
| Blocks     | Radius | Spawn tries per chunk | Minimum height | Maximum height | Ore concentrate[note 1] | Biomes        |
|------------|--------|-----------------------|----------------|----------------|-------------------------|---------------|
| Blackstone | 3—7    | 25                    | 0              | 127            | Uniform                 | Basalt Deltas |
| Basalt     | 3—7    | 75                    | 0              | 127            | Uniform                 | Basalt Deltas |

1. ↑Blobs generate using either uniform distribution, or triangle distribution. Uniform distribution have all ores spread in same frequency at any height, while triangle generate more frequent in center height.

## Data values
### ID
| Feature type        | Identifier                 |
|---------------------|----------------------------|
| [No displayed name] | `netherrack_replace_blobs` |

| Configured feature  | Identifier         |
|---------------------|--------------------|
| [No displayed name] | `blackstone_blobs` |
| [No displayed name] | `basalt_blobs`     |

### Config
Main article: Configured feature
Java Edition:

- config
	- stateThe block to use.
		- 
		- Block state
	- targetThe block to replace.
		- 
		- Block state
	- radiusValue between 0 and 12 (inclusive).
		- 
		- Int provider


An example

{
  "type": "minecraft:netherrack_replace_blobs",
  "config": {
    "radius": {
      "type": "minecraft:uniform",
      "value": {
        "max_inclusive": 7,
        "min_inclusive": 3
      }
    },
    "state": {
      "Name": "minecraft:basalt",
      "Properties": {
        "axis": "y"
      }
    },
    "target": {
      "Name": "minecraft:netherrack"
    }
  }
}




