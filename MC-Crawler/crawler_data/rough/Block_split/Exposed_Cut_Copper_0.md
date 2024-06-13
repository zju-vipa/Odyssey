# Cut Copper
Cut copper is an oxidizing metal block crafted from blocks of copper. Like other copper blocks, cut copper can be waxed to prevent oxidation.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
	- 1.4 Stonecutting
	- 1.5 Waxing
	- 1.6 Scraping
	- 1.7 Lightning strike
- 2 Usage
	- 2.1 Crafting ingredient
	- 2.2 Stonecutting
	- 2.3 Oxidation
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
- 5 Achievements
- 6 Advancements
- 7 History
- 8 Gallery
	- 8.1 Screenshots
- 9 Issues

## Obtaining
### Breaking
Cut copper can be mined only with a stone pickaxe or better. If cut copper is mined without the use of a pickaxe, it drops nothing.

| Block     | Cut Copper            |
|-----------|-----------------------|
| Hardness  | 3                     |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 15                    |
| Wooden    | 7.5                   |
| Stone     | 1.15                  |
| Iron      | 0.75                  |
| Diamond   | 0.6                   |
| Netherite | 0.5                   |
| Golden    | 1.25                  |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Natural generation

  

This section describes an experimental feature in Java Edition and Bedrock Edition. 
This feature is not enabled in-game by default and requires enabling the "Update 1.21" experimental data pack in Java Edition or the "Update 1.21" setting in the "Experiments" section in Bedrock Edition.


Waxed oxidized cut copper generates naturally in trial chambers.

### Crafting
| Name                                     | Ingredients                                                         | Crafting recipe |
|------------------------------------------|---------------------------------------------------------------------|-----------------|
| UnwaxedCut Copperor<br/>Waxed Cut Copper | Matching UnwaxedBlock of Copperor<br/>MatchingWaxed Block of Copper | 44444444        |
| Waxed Cut Copper                         | Matching UnwaxedCut Copper+<br/>Honeycomb                           |                 |

### Stonecutting
| Ingredients                                                         | Cutting recipe |
|---------------------------------------------------------------------|----------------|
| Matching UnwaxedBlock of Copperor<br/>MatchingWaxed Block of Copper | 44444444       |

### Waxing
Cut copper can be turned into the respective waxed cut copper by using a honeycomb item on them. Waxed cut copper does not oxidize and are identical to the non-waxed version.

### Scraping
Using an axe on waxed cut copper turns it into the respective non-waxed cut copper. In addition, using an axe on exposed, weathered, or oxidized cut copper reverts it one stage to regular, exposed, or weathered cut copper respectively.

### Lightning strike
Non-waxed cut copper is completely deoxidized when struck by lightning, and other non-waxed cut copper nearby is deoxidized randomly.

## Usage
### Crafting ingredient
| Name                                                   | Ingredients                                               | Crafting recipe |
|--------------------------------------------------------|-----------------------------------------------------------|-----------------|
| UnwaxedCut Copper Slabor<br/>Waxed Cut Copper Slab     | Matching UnwaxedCut Copperor<br/>MatchingWaxed Cut Copper | 66666666        |
| UnwaxedCut Copper Stairsor<br/>Waxed Cut Copper Stairs | Matching UnwaxedCut Copperor<br/>MatchingWaxed Cut Copper | 44444444        |

### Stonecutting
| Name                                                   | Ingredients                                               | Cutting recipe | Description                      |
|--------------------------------------------------------|-----------------------------------------------------------|----------------|----------------------------------|
| UnwaxedCut Copper Slabor<br/>Waxed Cut Copper Slab     | Matching UnwaxedCut Copperor<br/>MatchingWaxed Cut Copper | 22222222       |                                  |
| UnwaxedCut Copper Stairsor<br/>Waxed Cut Copper Stairs | Matching UnwaxedCut Copperor<br/>MatchingWaxed Cut Copper |                |                                  |
| UnwaxedChiseled Copperor<br/>Waxed Chiseled Copper     | Matching UnwaxedCut Copperor<br/>MatchingWaxed Cut Copper |                | ‌[upcoming: JE 1.21 & BE 1.21.0] |

### Oxidation
Main article: Oxidation
Non-waxed cut copper has four stages of oxidation (including the initial normal state). Lightning bolts and axes can remove the oxidation on cut copper. 

As the block begins to oxidize (exposed), it gets discolored and green spots begin to appear. As the oxidation continues (weathered), the block is a green color with brown spots. In the last stage (oxidized), the block is teal with several green spots.

## Data values
### ID
Java Edition:

| Name                       | Identifier                   | Form         | Translation key                              |
|----------------------------|------------------------------|--------------|----------------------------------------------|
| Cut Copper                 | `cut_copper`                 | Block & Item | `block.minecraft.cut_copper`                 |
| Exposed Cut Copper         | `exposed_cut_copper`         | Block & Item | `block.minecraft.exposed_cut_copper`         |
| Weathered Cut Copper       | `weathered_cut_copper`       | Block & Item | `block.minecraft.weathered_cut_copper`       |
| Oxidized Cut Copper        | `oxidized_cut_copper`        | Block & Item | `block.minecraft.oxidized_cut_copper`        |
| Waxed Cut Copper           | `waxed_cut_copper`           | Block & Item | `block.minecraft.waxed_cut_copper`           |
| Waxed Exposed Cut Copper   | `waxed_exposed_cut_copper`   | Block & Item | `block.minecraft.waxed_exposed_cut_copper`   |
| Waxed Weathered Cut Copper | `waxed_weathered_cut_copper` | Block & Item | `block.minecraft.waxed_weathered_cut_copper` |
| Waxed Oxidized Cut Copper  | `waxed_oxidized_cut_copper`  | Block & Item | `block.minecraft.waxed_oxidized_cut_copper`  |

Bedrock Edition:

| Name                       | Identifier                   | Numeric ID | Form                       | Item ID[i 1]   | Translation key                        |
|----------------------------|------------------------------|------------|----------------------------|----------------|----------------------------------------|
| Cut Copper                 | `cut_copper`                 | `602`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.cut_copper.name`                 |
| Exposed Cut Copper         | `exposed_cut_copper`         | `603`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.exposed_cut_copper.name`         |
| Weathered Cut Copper       | `weathered_cut_copper`       | `604`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.weathered_cut_copper.name`       |
| Oxidized Cut Copper        | `oxidized_cut_copper`        | `605`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.oxidized_cut_copper.name`        |
| Waxed Cut Copper           | `waxed_cut_copper`           | `606`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.waxed_cut_copper.name`           |
| Waxed Exposed Cut Copper   | `waxed_exposed_cut_copper`   | `607`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.waxed_exposed_cut_copper.name`   |
| Waxed Weathered Cut Copper | `waxed_weathered_cut_copper` | `608`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.waxed_weathered_cut_copper.name` |
| Waxed Oxidized Cut Copper  | `waxed_oxidized_cut_copper`  | `702`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.waxed_oxidized_cut_copper.name`  |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑ a b c d e f g hAvailable with /give command.
3. ↑ a b c d e f g hThe block's direct item form has the same id as the block.


