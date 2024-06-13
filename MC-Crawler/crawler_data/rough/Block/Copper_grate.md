# Copper Grate
Copper grates are a variant of copper blocks that have perforations that can be seen through.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Crafting
	- 1.3 Stonecutting
- 2 Usage
	- 2.1 Oxidation
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
- 5 Achievements
- 6 Advancements
- 7 History
- 8 Issues
- 9 Trivia
- 10 Gallery
	- 10.1 Screenshots
- 11 References

## Obtaining
### Breaking
Copper grates can be mined only with a stone pickaxe or greater. If a copper grate is mined without the use of a pickaxe, it drops nothing.

| Block     | Copper GrateExposed Copper GrateWeathered Copper GrateOxidized Copper Grate |
|-----------|-----------------------------------------------------------------------------|
| Hardness  | 3                                                                           |
| Tool      |                                                                             |
|           | Breakingtime (sec)[A]                                                       |
| Default   | 15                                                                          |
| Wooden    | 7.5                                                                         |
| Stone     | 1.15                                                                        |
| Iron      | 0.75                                                                        |
| Diamond   | 0.6                                                                         |
| Netherite | 0.5                                                                         |
| Golden    | 1.25                                                                        |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Crafting
| Name                                         | Ingredients                                                         | Crafting recipe |
|----------------------------------------------|---------------------------------------------------------------------|-----------------|
| UnwaxedCopper Grateor<br/>Waxed Copper Grate | Matching UnwaxedBlock of Copperor<br/>MatchingWaxed Block of Copper | 44444444        |
| Waxed Copper Grate                           | Matching UnwaxedCopper Grate+<br/>Honeycomb                         |                 |

### Stonecutting
| Ingredients                                                         | Cutting recipe |
|---------------------------------------------------------------------|----------------|
| Matching UnwaxedBlock of Copperor<br/>MatchingWaxed Block of Copper | 44444444       |

## Usage
Copper grates are decorative semi-transparent blocks that can oxidize. Copper grates do not conduct redstone, and mobs cannot spawn on top of them. They can also be waterlogged.

Copper grates adjacent to other copper grates are invisible when viewed through a copper grate that is identical in states of oxidation and wax.

### Oxidation
Main article: Oxidation
Non-waxed copper grates have four stages of oxidation (including the initial normal state). Lightning bolts and axes can remove the oxidation on copper grates. Using a honeycomb on a copper grate prevents it from oxidizing.

As the block begins to oxidize (exposed), it gets discolored and green spots begin to appear. As the oxidation continues (weathered), the block is a green color with brown spots. In the last stage (oxidized), the block is teal with several green spots.

## Data values
### ID
Java Edition:

| Name                         | Identifier                     | Form         | Block tags                                | Translation key                                |
|------------------------------|--------------------------------|--------------|-------------------------------------------|------------------------------------------------|
| Copper Grate                 | `copper_grate`                 | Block & Item | `mineable/pickaxe`<br/>`needs_stone_tool` | `block.minecraft.copper_grate`                 |
| Exposed Copper Grate         | `exposed_copper_grate`         | Block & Item | `mineable/pickaxe`<br/>`needs_stone_tool` | `block.minecraft.exposed_copper_grate`         |
| Weathered Copper Grate       | `weathered_copper_grate`       | Block & Item | `mineable/pickaxe`<br/>`needs_stone_tool` | `block.minecraft.weathered_copper_grate`       |
| Oxidized Copper Grate        | `oxidized_copper_grate`        | Block & Item | `mineable/pickaxe`<br/>`needs_stone_tool` | `block.minecraft.oxidized_copper_grate`        |
| Waxed Copper Grate           | `waxed_copper_grate`           | Block & Item | `mineable/pickaxe`<br/>`needs_stone_tool` | `block.minecraft.waxed_copper_grate`           |
| Waxed Exposed Copper Grate   | `waxed_exposed_copper_grate`   | Block & Item | `mineable/pickaxe`<br/>`needs_stone_tool` | `block.minecraft.waxed_exposed_copper_grate`   |
| Waxed Weathered Copper Grate | `waxed_weathered_copper_grate` | Block & Item | `mineable/pickaxe`<br/>`needs_stone_tool` | `block.minecraft.waxed_weathered_copper_grate` |
| Waxed Oxidized Copper Grate  | `waxed_oxidized_copper_grate`  | Block & Item | `mineable/pickaxe`<br/>`needs_stone_tool` | `block.minecraft.waxed_oxidized_copper_grate`  |

Bedrock Edition:

| Name                         | Identifier                     | Numeric ID | Form                       | Item ID[i 1]   | Translation key                          |
|------------------------------|--------------------------------|------------|----------------------------|----------------|------------------------------------------|
| Copper Grate                 | `copper_grate`                 | `-768`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.copper_grate.name`                 |
| Exposed Copper Grate         | `exposed_copper_grate`         | `-769`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.exposed_copper_grate.name`         |
| Weathered Copper Grate       | `weathered_copper_grate`       | `-770`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.weathered_copper_grate.name`       |
| Oxidized Copper Grate        | `oxidized_copper_grate`        | `-771`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.oxidized_copper_grate.name`        |
| Waxed Copper Grate           | `waxed_copper_grate`           | `-772`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.waxed_copper_grate.name`           |
| Waxed Exposed Copper Grate   | `waxed_exposed_copper_grate`   | `-773`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.waxed_exposed_copper_grate.name`   |
| Waxed Weathered Copper Grate | `waxed_weathered_copper_grate` | `-774`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.waxed_weathered_copper_grate.name` |
| Waxed Oxidized Copper Grate  | `waxed_oxidized_copper_grate`  | `-775`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.waxed_oxidized_copper_grate.name`  |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑ a b c d e f g hAvailable with /give command.
3. ↑ a b c d e f g hThe block's direct item form has the same id as the block.

