# Huge mushroom
Huge mushrooms are tree-like features that consist of mushroom blocks. They can be found naturally in swamp‌[BE  only], dark forest, and mushroom fields biomes, or grown from a small mushroom by applying bone meal on it – small mushrooms do not turn into huge mushrooms naturally.

## Contents
- 1 Generation
- 2 Growth
- 3 Construction
	- 3.1 Huge brown mushrooms
	- 3.2 Huge red mushrooms
- 4 Data values
	- 4.1 ID
	- 4.2 Config
- 5 History
- 6 Trivia
- 7 Gallery
	- 7.1 Screenshots
- 8 References

## Generation
Huge mushrooms naturally generate in swamp‌[BE  only], dark forest, and mushroom fields biomes.

## Growth
Huge mushrooms have a 40% chance to be grown by applying bone meal to a small red or brown mushroom that is planted on dirt, coarse dirt, grass blocks, rooted dirt or moss blocks with a sky and block light level of 12 or less, or on podzol, mycelium or nylium at any light level. The volume the huge mushroom would generate in must be free of solid blocks, and a minimum of 5 blocks above the mushroom, although 7 blocks allows most to spawn. 13 blocks are required for all huge mushrooms to generate. Extra tall huge mushrooms have a ~5% chance of growing.

A huge mushroom does not grow above the height limit.

Any small mushroom placed does not grow into a huge mushroom naturally; bone meal must be applied.

## Construction
Main article: /Structure
A huge mushroom's height is normally between 5 and 7 blocks inclusive, but have a 1⁄12 chance to generate twice as high (minus 1 block), meaning they can be 9, 11, or 13 blocks tall.[1]

A huge brown mushroom
A huge red mushroom
To grow, the block under the huge mushroom's stem must be dirt, podzol, or mycelium. Light level does not matter if placed on podzol or mycelium, but if placed on dirt, coarse dirt or grass blocks both skylight and blocklight must be 12 or less. Each type of mushroom also has its own space requirements, which are described below.

### Huge brown mushrooms
Huge brown mushrooms consist of a single stalk in the center, with a 7×7 canopy of brown mushroom blocks at the top with the corners missing. 

For the mushroom to grow, the lowest four blocks of the stem (i.e. the three blocks above the small mushroom being grown) must be air or leaves, and a 7×7×(height−3) region above must similarly be clear of anything except air or leaves. Due to the space requirement matching the size of the canopy at the top, it is possible for a huge brown mushroom to grow with its canopy directly touching a mushroom next to it.

### Huge red mushrooms
Huge red mushrooms, like their brown counterparts, have a single stalk in the center, but a different canopy, composed of five 3×3 slabs of red mushroom blocks arranged above and around the stalk, forming a 'dome'. Unlike brown mushrooms, red mushrooms only check the blocks directly above the small mushroom, and do not require the rest of the dome to be clear of other blocks. Blocks that mobs can't suffocate in, such as slabs, end portal frame and end portal, are replaced; full blocks remain unchanged.

## Data values
### ID
Java Edition:

| Feature type        | Identifier            |
|---------------------|-----------------------|
| [No displayed name] | `huge_red_mushroom`   |
| [No displayed name] | `huge_brown_mushroom` |

| Configured feature  | Identifier            |
|---------------------|-----------------------|
| [No displayed name] | `huge_red_mushroom`   |
| [No displayed name] | `huge_brown_mushroom` |

which are used in:

| Configured feature  | Identifier                   |
|---------------------|------------------------------|
| [No displayed name] | `mushroom_island_vegetation` |
| [No displayed name] | `dark_forest_vegetation`     |

Bedrock Edition:

| Feature             | Identifier                    |
|---------------------|-------------------------------|
| [No displayed name] | `huge_red_mushroom_feature`   |
| [No displayed name] | `huge_brown_mushroom_feature` |

which are used in:

| Feature             | Identifier              |
|---------------------|-------------------------|
| [No displayed name] | `huge_mushroom_feature` |

which is used in:

| Feature             | Identifier                                       |
|---------------------|--------------------------------------------------|
| [No displayed name] | `minecraft:legacy:forest_foliage_feature`        |
| [No displayed name] | `minecraft:legacy:flower_forest_foliage_feature` |
| [No displayed name] | `minecraft:legacy:roofed_forest_foliage_feature` |
| [No displayed name] | `minecraft:legacy:swamp_foliage_feature`         |

### Config
Main article: Configured feature
Java Edition:

- config
	- cap_providerThe block to use for the cap.
		- 
		- Block state provider
	- stem_providerThe block to use for the stem.
		- 
		- Block state provider
	- foliage_radius(optional，defaults to 2) The size of the cap.


An example

{
  "type": "minecraft:huge_red_mushroom",
  "config": {
    "cap_provider": {
      "type": "minecraft:simple_state_provider",
      "state": {
        "Name": "minecraft:red_mushroom_block",
        "Properties": {
          "down": "false",
          "east": "true",
          "north": "true",
          "south": "true",
          "up": "true",
          "west": "true"
        }
      }
    },
    "foliage_radius": 2,
    "stem_provider": {
      "type": "minecraft:simple_state_provider",
      "state": {
        "Name": "minecraft:mushroom_stem",
        "Properties": {
          "down": "false",
          "east": "true",
          "north": "true",
          "south": "true",
          "up": "false",
          "west": "true"
        }
      }
    }
  }
}



