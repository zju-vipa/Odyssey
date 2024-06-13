# Basalt columns
Basalt columns are vertical clusters of basalt blocks found within basalt delta biomes. They may also contain lava and magma in the many gaps between the towers.

## Contents
- 1 Generation
- 2 Data values
	- 2.1 ID
	- 2.2 Config
- 3 History
- 4 Issues
- 5 Gallery
	- 5.1 Screenshots

## Generation
An example of basalt columns in the air and on the ground.
Basalt columns generate in basalt deltas.

## Data values
### ID
Java Edition:

| Feature type        | Identifier       |
|---------------------|------------------|
| [No displayed name] | `basalt_columns` |

| Configured feature  | Identifier             |
|---------------------|------------------------|
| [No displayed name] | `large_basalt_columns` |
| [No displayed name] | `small_basalt_columns` |

Bedrock Edition:

| Feature             | Identifier               |
|---------------------|--------------------------|
| [No displayed name] | `basalt_columns_feature` |

### Config
Main article: Configured feature
Java Edition:

- config
	- reachThe max radius of a column in this column cluster. Value between 0 and 3 (inclusive).
		- 
		- Int provider
	- heightThe max height isheight + 1. Value between 1 and 10 (inclusive).
		- 
		- Int provider


An example

{
  "type": "minecraft:basalt_columns",
  "config": {
    "height": {
      "type": "minecraft:uniform",
      "value": {
        "max_inclusive": 4,
        "min_inclusive": 1
      }
    },
    "reach": 1
  }
}




