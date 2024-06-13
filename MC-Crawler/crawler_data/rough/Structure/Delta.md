# Delta
A delta is a one-block-deep sheet of constrained lava found among the terrain of basalt deltas biome in the Nether.

## Contents
- 1 Description
- 2 Data values
	- 2.1 ID
	- 2.2 Config
- 3 History
- 4 Issues
- 5 Gallery
	- 5.1 Screenshots
- 6 References

## Description
Deltas are one-block-deep terraced lava lakes, often divided by lines of blackstone. Magma blocks also generate as part of these structures, replacing some of the lava. Deltas tend to be adjacent or surrounded by basalt columns.

## Data values
### ID
Java Edition:

| Feature type        | Identifier      |
|---------------------|-----------------|
| [No displayed name] | `delta_feature` |

| Configured feature  | Identifier |
|---------------------|------------|
| [No displayed name] | `delta`    |

Bedrock Edition:

| Feature             | Identifier      |
|---------------------|-----------------|
| [No displayed name] | `delta_feature` |

### Config
Java Edition:

See also: Custom feature

- 
	- contentsThe block to use on the inside of the delta.
		- 
		- Block state
	- rimThe block to use for the rim of the delta.
		- 
		- Block state
	- sizeThe size of the inside of the delta. Value between 0 and 16 (inclusive).
		- 
		- Int provider
	- rim_sizeThe size of the rim of the delta. Value between 0 and 16 (inclusive).
		- 
		- Int provider


An example

{
  "type": "minecraft:delta_feature",
  "config": {
    "contents": {
      "Name": "minecraft:lava",
      "Properties": {
        "level": "0"
      }
    },
    "rim": {
      "Name": "minecraft:magma_block"
    },
    "rim_size": {
      "type": "minecraft:uniform",
      "value": {
        "max_inclusive": 2,
        "min_inclusive": 0
      }
    },
    "size": {
      "type": "minecraft:uniform",
      "value": {
        "max_inclusive": 7,
        "min_inclusive": 3
      }
    }
  }
}



