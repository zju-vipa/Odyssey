# Copper Bulb
A copper bulb is a light-emitting block. It toggles on or off when it receives a redstone pulse, and does not need continuous power to emit light. Its light level depends on its state of oxidation.

Waxed copper bulbs do not oxidize, but otherwise function identically.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
- 2 Usage
	- 2.1 Oxidation
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
		- 3.2.1 Waxing
		- 3.2.2 Toggling
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 Achievements
- 6 Advancements
- 7 History
- 8 Issues
- 9 Gallery
	- 9.1 Renders
		- 9.1.1 Powered
		- 9.1.2 Unpowered
	- 9.2 Screenshots
- 10 References

## Obtaining
### Breaking
Copper bulbs can be mined only with a stone pickaxe or better. If a copper bulb is mined without the use of a valid pickaxe, it drops nothing.

| Block     | Copper BulbExposed Copper BulbWeathered Copper BulbOxidized Copper Bulb |
|-----------|-------------------------------------------------------------------------|
| Hardness  | 3                                                                       |
| Tool      |                                                                         |
|           | Breakingtime (sec)[A]                                                   |
| Default   | 15                                                                      |
| Wooden    | 7.5                                                                     |
| Stone     | 1.15                                                                    |
| Iron      | 0.75                                                                    |
| Diamond   | 0.6                                                                     |
| Netherite | 0.5                                                                     |
| Golden    | 1.25                                                                    |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Natural generation
Lit, unwaxed copper bulbs in random states of oxidation are generated in trial chambers.

### Crafting
| Name                                       | Ingredients                                                                                           | Crafting recipe |
|--------------------------------------------|-------------------------------------------------------------------------------------------------------|-----------------|
| UnwaxedCopper Bulbor<br/>Waxed Copper Bulb | Matching UnwaxedBlock of Copperor<br/>MatchingWaxed Block of Copper+<br/>Blaze Rod+<br/>Redstone Dust | 44444444        |
| Waxed Copper Bulb                          | Matching UnwaxedCopper Bulb+<br/>Honeycomb                                                            |                 |

## Usage
Copper bulbs can be activated to emit light, with the light level emitted decreasing for each stage of oxidation.
When the copper bulb receives a redstone pulse, it immediately toggles between its lit and unlit states.

A comparator can read the state of a copper bulb, and it emits a signal strength of 15 if the bulb is lit, regardless of oxidation. If the bulb is unlit, the comparator does not emit any power, allowing this comparator and copper bulb combination to act as a compact T flip-flop.

While the copper bulb is receiving redstone power (either to toggle the bulb on or off) a red dot appears in the center of the block. An observer can detect this, and emits a signal when a copper bulb becomes powered or unpowered. 

### Oxidation
Main article: Oxidation
Non-waxed copper bulbs have four stages of oxidation (including the initial normal state). Lightning bolts and axes can remove the oxidation on copper bulbs. They can be waxed with honeycomb to prevent oxidation from progressing.

As the block begins to oxidize (exposed), it gets discolored and green spots begin to appear. As the oxidation continues (weathered), the block is a green color with brown spots. In the last stage (oxidized), the block is teal with several green spots.

The light level emitted by copper bulbs also changes depending on the stage of oxidation.

| Oxidation level | Light level |
|-----------------|-------------|
| Normal          | 15          |
| Exposed         | 12          |
| Weathered       | 8           |
| Oxidized        | 4           |

## Data values
### ID
Java Edition:

| Name                        | Identifier                    | Form         | Block tags                                | Translation key                               |
|-----------------------------|-------------------------------|--------------|-------------------------------------------|-----------------------------------------------|
| Copper Bulb                 | `copper_bulb`                 | Block & Item | `mineable/pickaxe`<br/>`needs_stone_tool` | `block.minecraft.copper_bulb`                 |
| Exposed Copper Bulb         | `exposed_copper_bulb`         | Block & Item | `mineable/pickaxe`<br/>`needs_stone_tool` | `block.minecraft.exposed_copper_bulb`         |
| Weathered Copper Bulb       | `weathered_copper_bulb`       | Block & Item | `mineable/pickaxe`<br/>`needs_stone_tool` | `block.minecraft.weathered_copper_bulb`       |
| Oxidized Copper Bulb        | `oxidized_copper_bulb`        | Block & Item | `mineable/pickaxe`<br/>`needs_stone_tool` | `block.minecraft.oxidized_copper_bulb`        |
| Waxed Copper Bulb           | `waxed_copper_bulb`           | Block & Item | `mineable/pickaxe`<br/>`needs_stone_tool` | `block.minecraft.waxed_copper_bulb`           |
| Waxed Exposed Copper Bulb   | `waxed_exposed_copper_bulb`   | Block & Item | `mineable/pickaxe`<br/>`needs_stone_tool` | `block.minecraft.waxed_exposed_copper_bulb`   |
| Waxed Weathered Copper Bulb | `waxed_weathered_copper_bulb` | Block & Item | `mineable/pickaxe`<br/>`needs_stone_tool` | `block.minecraft.waxed_weathered_copper_bulb` |
| Waxed Oxidized Copper Bulb  | `waxed_oxidized_copper_bulb`  | Block & Item | `mineable/pickaxe`<br/>`needs_stone_tool` | `block.minecraft.waxed_oxidized_copper_bulb`  |

Bedrock Edition:

| Name                        | Identifier                    | Numeric ID | Form                       | Item ID[i 1]   | Translation key                         |
|-----------------------------|-------------------------------|------------|----------------------------|----------------|-----------------------------------------|
| Copper Bulb                 | `copper_bulb`                 | `-776`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.copper_bulb.name`                 |
| Exposed Copper Bulb         | `exposed_copper_bulb`         | `-777`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.exposed_copper_bulb.name`         |
| Weathered Copper Bulb       | `weathered_copper_bulb`       | `-778`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.weathered_copper_bulb.name`       |
| Oxidized Copper Bulb        | `oxidized_copper_bulb`        | `-779`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.oxidized_copper_bulb.name`        |
| Waxed Copper Bulb           | `waxed_copper_bulb`           | `-780`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.waxed_copper_bulb.name`           |
| Waxed Exposed Copper Bulb   | `waxed_exposed_copper_bulb`   | `-781`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.waxed_exposed_copper_bulb.name`   |
| Waxed Weathered Copper Bulb | `waxed_weathered_copper_bulb` | `-782`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.waxed_weathered_copper_bulb.name` |
| Waxed Oxidized Copper Bulb  | `waxed_oxidized_copper_bulb`  | `-783`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.waxed_oxidized_copper_bulb.name`  |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑ a b c d e f g hAvailable with /give command.
3. ↑ a b c d e f g hThe block's direct item form has the same id as the block.

### Block states
See also: Block states

Java Edition:

| Name    | Default value | Allowed values     | Description                         |
|---------|---------------|--------------------|-------------------------------------|
| lit     | `false`       | `false`<br/>`true` | Whether the copper bulb is lit.     |
| powered | `false`       | `false`<br/>`true` | Whether the copper bulb is powered. |

Bedrock Edition:

| Name        | Metadata Bits | Default value | Allowed values     | Values forMetadata Bits | Description                         |
|-------------|---------------|---------------|--------------------|-------------------------|-------------------------------------|
| lit         | Not Supported | `false`       | `false`<br/>`true` | `Unsupported`           | Whether the copper bulb is lit.     |
| powered_bit | Not Supported | `false`       | `false`<br/>`true` | `Unsupported`           | Whether the copper bulb is powered. |



