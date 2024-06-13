# Glow Lichen (feature)
A glow lichen is a feature that consist of several glow lichen blocks.

## Contents
- 1 Generation
- 2 Data values
	- 2.1 ID
	- 2.2 Config
- 3 History

## Generation
Glow lichen feature can be found in all the Overworld biomes. It generates on the four sides and lower surface of stone-like block including stone, andesite, diorite, granite, dripstone block, calcite, tuff, and deepslate. It generates only in air and water.

## Data values
### ID
Java Edition:

| Feature type        | Identifier         |
|---------------------|--------------------|
| [No displayed name] | `multiface_growth` |

| Configured feature  | Identifier    |
|---------------------|---------------|
| [No displayed name] | `glow_lichen` |

Bedrock Edition:

| Feature             | Identifier            |
|---------------------|-----------------------|
| [No displayed name] | `glow_lichen_feature` |

which is used in:

| Feature             | Identifier                        |
|---------------------|-----------------------------------|
| [No displayed name] | `underground_glow_lichen_feature` |

### Config
Main article: Configured feature
Java Edition:

- config
	- block(optional, defaults toglow_lichen) The block to place, currently must beglow_lichenorsculk_vein.
	- search_range(optional, defaults to 10) Value between 1 and 64 (inclusive).
	- chance_of_spreading(optional, defaults to 0.5) Value between 0.0 and 1.0 (inclusive).
	- can_place_on_floor(optional, defaults to false).
	- can_place_on_ceiling(optional, defaults to false).
	- can_place_on_wall(optional, defaults to false).
	- can_be_placed_onCan be a block ID or a block tag, or a list of block IDs.

