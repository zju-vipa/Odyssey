# Huge fungus
A huge fungus is a large "tree" feature that generates in the Nether. There are two types of huge fungi: the huge crimson fungus and the huge warped fungus.

## Contents
- 1 Generation
- 2 Blocks and items
- 3 Structure
- 4 Growth
- 5 Data values
	- 5.1 ID
	- 5.2 Config
- 6 History
- 7 Issues
- 8 Gallery
	- 8.1 Screenshots
- 9 See also
- 10 References

## Generation
Huge crimson fungi and huge warped fungi generate only in crimson forests and warped forests, respectively.

## Blocks and items
These items can be obtained from the huge crimson fungus:

- Crimson Stem
- Nether Wart Block
- Shroomlight
- Crimson Planks(created from a crimson stem in the inventory crafting grid)
- Weeping Vines

These items can be obtained from the huge warped fungus:

- Warped Stem
- Warped Wart Block
- Shroomlight
- Warped Planks(created from a warped stem in the inventory crafting grid)

## Structure
The trunks of huge fungi are made of either warped stems or crimson stems depending on the type. Huge fungus trunks can be either thick or thin: thick trunks grow up in a 3×3-plus shape, with stray stems sometimes in the corners, while thin trunks grow straight up as a 1×1 column. To determine the size of huge fungi, a random integer is chosen between 4 and 13 [inclusive]. There is then a 1⁄12 chance of that integer doubling. The resulting value is the height of the trunk. A layer of wart blocks and shroomlights is then spread around the trunk, being able to generate up to 3 blocks out from the trunk, and are the "leaves" of the fungus. There is a 3×3×2 hollow ring that surrounds the lowest block of a fungus where no blocks generate. Both variants have shroomlights generate inside them, replacing both the wart blocks and stems. Huge crimson fungi may also have weeping vines growing replacing the same, or from the underside of wart blocks. In this way huge crimson fungi may grow the weeping vines lower than the stems as well as initially generate replacing the stems, when naturally-generated uniquely along the local ceiling.

## Growth
The smallest a huge fungus structure can be.
When bone meal is used on a fungus that is planted on matching nylium, this has a 40% chance to grow into its huge equivalent (similar to saplings and mushrooms). Crimson and warped fungi grow into crimson and warped huge fungi, respectively. The stem, shroomlight, or nether wart block do not replace blocks.

A fungus does not grow by itself through random ticks, unlike saplings.

Huge fungi grow even with blocks above them,[1] and do not replace any solid blocks when grown; however, they do not grow if blocked by the world height limit, or if situated outside of the world.

Huge fungi can grow up to 27 blocks tall. The maximum space they can take up is 9×27×9 blocks (partially hollow), and the average is 213 blocks of volume.

Nether wart blocks and shroomlight persist when the stem of the huge fungus is removed, unlike how leaves decay when logs of a tree are removed.

## Data values
### ID
Java Edition:

| Feature type        | Identifier    |
|---------------------|---------------|
| [No displayed name] | `huge_fungus` |

| Configured feature  | Identifier               |
|---------------------|--------------------------|
| [No displayed name] | `crimson_fungus`         |
| [No displayed name] | `crimson_fungus_planted` |
| [No displayed name] | `warped_fungus`          |
| [No displayed name] | `warped_fungus_planted`  |

### Config
Main article: Configured feature
Java Edition:

- config
	- hat_stateThe block to use for the hat.
		- 
		- Block state
	- decor_stateThe block to use as decoration.
		- 
		- Block state
	- stem_stateThe block to use for the stem.
		- 
		- Block state
	- valid_base_blockThe block to place this feature on.
		- 
		- Block state
	- planted(optional, defaults to false) Whether this huge fungus is planted. If false, it can't exceed the world ceiling, can replace blocks whose material isplant, and doesn't drop items when replaced by other blocks.
	- replaceable_blocksA block predicate. The predicate must pass to be replaced with this feature.
		- 
		- Block predicate


An example

{
  "type": "minecraft:huge_fungus",
  "config": {
    "decor_state": {
      "Name": "minecraft:shroomlight"
    },
    "hat_state": {
      "Name": "minecraft:warped_wart_block"
    },
    "planted": false,
    "replaceable_blocks": {
      "type": "minecraft:matching_blocks",
      "blocks": [
        "minecraft:warped_fungus",
        "minecraft:crimson_fungus",
        "minecraft:weeping_vines",
        "minecraft:weeping_vines_plant",
        "minecraft:twisting_vines",
        "minecraft:twisting_vines_plant"
      ]
    },
    "stem_state": {
      "Name": "minecraft:warped_stem",
      "Properties": {
        "axis": "y"
      }
    },
    "valid_base_block": {
      "Name": "minecraft:warped_nylium"
    }
  }
}



