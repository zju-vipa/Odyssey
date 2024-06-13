# Sculk Vein (feature)
A sculk vein is a feature that consist of several sculk vein blocks. It generates exclusively in the deep dark biome.

## Contents
- 1 Generation
- 2 Data values
	- 2.1 ID
	- 2.2 Config
- 3 History

## Generation
The Sculk vein feature generates on the four sides and lower surface of stone-like block including stone, andesite, diorite, granite, dripstone block, calcite, tuff, and deepslate. It generates only in air and water.

## Data values
### ID
Java Edition:

| Feature type        | Identifier         |
|---------------------|--------------------|
| [No displayed name] | `multiface_growth` |

| Configured feature  | Identifier   |
|---------------------|--------------|
| [No displayed name] | `sculk_vein` |

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


An example

{
  "type": "minecraft:multiface_growth",
  "config": {
    "block": "minecraft:sculk_vein",
    "can_be_placed_on": [
      "minecraft:stone",
      "minecraft:andesite",
      "minecraft:diorite",
      "minecraft:granite",
      "minecraft:dripstone_block",
      "minecraft:calcite",
      "minecraft:tuff",
      "minecraft:deepslate"
    ],
    "can_place_on_ceiling": true,
    "can_place_on_floor": true,
    "can_place_on_wall": true,
    "chance_of_spreading": 1.0,
    "search_range": 20
  }
}




