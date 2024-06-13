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

