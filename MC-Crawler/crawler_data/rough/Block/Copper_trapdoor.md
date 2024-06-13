# Copper Trapdoor
A copper trapdoor is a type of trapdoor made from copper that can be opened and closed by the player without redstone.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
- 2 Usage
	- 2.1 Barrier
	- 2.2 Redstone component
	- 2.3 Oxidation
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
		- 3.2.1 Waxing
		- 3.2.2 Opening
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 Achievements
- 6 Advancements
- 7 History
- 8 Gallery
	- 8.1 Screenshots
- 9 Issues

## Obtaining
### Breaking
Copper trapdoors can be mined only with a stone pickaxe or better. If a copper trapdoor is mined without the use of a pickaxe, it drops nothing.

| Block     | Copper Trapdoor       |
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
Copper trapdoors generate naturally in trial chambers.

### Crafting
| Name                                               | Ingredients                                                         | Crafting recipe |
|----------------------------------------------------|---------------------------------------------------------------------|-----------------|
| UnwaxedCopper Trapdooror<br/>Waxed Copper Trapdoor | Matching UnwaxedBlock of Copperor<br/>MatchingWaxed Block of Copper | 22222222        |
| Waxed Copper Trapdoor                              | Matching UnwaxedCopper Trapdoor+<br/>Honeycomb                      |                 |

## Usage
Main articles: Trapdoor § Usage and Tutorials/Trapdoor uses
Copper trapdoors can be opened and closed by players or a redstone pulse. Copper trapdoors are also affected by the wind burst of thrown wind charges, causing them to open if closed, or vice versa.

### Barrier
A copper trapdoor can be opened or closed by pressing the Use Item/Place Block control.

### Redstone component
Copper trapdoors can be controlled with redstone power. When activated, the copper trapdoor immediately opens. When deactivated, it immediately closes.

An activated copper trapdoor can still be closed by a player, and does not re-open until it receives a new activation signal (if a trapdoor has been closed "by hand", it still needs to be deactivated and then reactivated to open by redstone). 

### Oxidation
Main article: Oxidation
Non-waxed copper trapdoors have four stages of oxidation (including the initial normal state). Lightning bolts and axes can remove the oxidation on copper trapdoors. They can be waxed with honeycomb to prevent oxidation from progressing.

As the block begins to oxidize (exposed), it gets discolored and green spots begin to appear. As the oxidation continues (weathered), the block is a green color with brown spots. In the last stage (oxidized), the block is teal with several green spots.

## Data values
### ID
Java Edition:

| Name                            | Identifier                        | Form         | Block tags                                | Translation key                                   |
|---------------------------------|-----------------------------------|--------------|-------------------------------------------|---------------------------------------------------|
| Copper Trapdoor                 | `copper_trapdoor`                 | Block & Item | `mineable/pickaxe`<br/>`needs_stone_tool` | `block.minecraft.copper_trapdoor`                 |
| Exposed Copper Trapdoor         | `exposed_copper_trapdoor`         | Block & Item | `mineable/pickaxe`<br/>`needs_stone_tool` | `block.minecraft.exposed_copper_trapdoor`         |
| Weathered Copper Trapdoor       | `weathered_copper_trapdoor`       | Block & Item | `mineable/pickaxe`<br/>`needs_stone_tool` | `block.minecraft.weathered_copper_trapdoor`       |
| Oxidized Copper Trapdoor        | `oxidized_copper_trapdoor`        | Block & Item | `mineable/pickaxe`<br/>`needs_stone_tool` | `block.minecraft.oxidized_copper_trapdoor`        |
| Waxed Copper Trapdoor           | `waxed_copper_trapdoor`           | Block & Item | `mineable/pickaxe`<br/>`needs_stone_tool` | `block.minecraft.waxed_copper_trapdoor`           |
| Waxed Exposed Copper Trapdoor   | `waxed_exposed_copper_trapdoor`   | Block & Item | `mineable/pickaxe`<br/>`needs_stone_tool` | `block.minecraft.waxed_exposed_copper_trapdoor`   |
| Waxed Weathered Copper Trapdoor | `waxed_weathered_copper_trapdoor` | Block & Item | `mineable/pickaxe`<br/>`needs_stone_tool` | `block.minecraft.waxed_weathered_copper_trapdoor` |
| Waxed Oxidized Copper Trapdoor  | `waxed_oxidized_copper_trapdoor`  | Block & Item | `mineable/pickaxe`<br/>`needs_stone_tool` | `block.minecraft.waxed_oxidized_copper_trapdoor`  |

Bedrock Edition:

| Name                            | Identifier                        | Numeric ID | Form                       | Item ID[i 1]   | Block tags  | Translation key                             |
|---------------------------------|-----------------------------------|------------|----------------------------|----------------|-------------|---------------------------------------------|
| Copper Trapdoor                 | `copper_trapdoor`                 | `-792`     | Block & Giveable Item[i 2] | Identical[i 3] | `trapdoors` | `tile.copper_trapdoor.name`                 |
| Exposed Copper Trapdoor         | `exposed_copper_trapdoor`         | `-793`     | Block & Giveable Item[i 2] | Identical[i 3] | `trapdoors` | `tile.exposed_copper_trapdoor.name`         |
| Weathered Copper Trapdoor       | `weathered_copper_trapdoor`       | `-794`     | Block & Giveable Item[i 2] | Identical[i 3] | `trapdoors` | `tile.weathered_copper_trapdoor.name`       |
| Oxidized Copper Trapdoor        | `oxidized_copper_trapdoor`        | `-795`     | Block & Giveable Item[i 2] | Identical[i 3] | `trapdoors` | `tile.oxidized_copper_trapdoor.name`        |
| Waxed Copper Trapdoor           | `waxed_copper_trapdoor`           | `-796`     | Block & Giveable Item[i 2] | Identical[i 3] | `trapdoors` | `tile.waxed_copper_trapdoor.name`           |
| Waxed Exposed Copper Trapdoor   | `waxed_exposed_copper_trapdoor`   | `-797`     | Block & Giveable Item[i 2] | Identical[i 3] | `trapdoors` | `tile.waxed_exposed_copper_trapdoor.name`   |
| Waxed Weathered Copper Trapdoor | `waxed_weathered_copper_trapdoor` | `-798`     | Block & Giveable Item[i 2] | Identical[i 3] | `trapdoors` | `tile.waxed_weathered_copper_trapdoor.name` |
| Waxed Oxidized Copper Trapdoor  | `waxed_oxidized_copper_trapdoor`  | `-799`     | Block & Giveable Item[i 2] | Identical[i 3] | `trapdoors` | `tile.waxed_oxidized_copper_trapdoor.name`  |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑ a b c d e f g hAvailable with /give command.
3. ↑ a b c d e f g hThe block's direct item form has the same id as the block.

### Block states
Main article: Trapdoor § Block states
