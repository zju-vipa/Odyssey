# Small island
A small island (aka. end island) is roughly a hemispherical cluster of end stone blocks found within its respective biome.

## Contents
- 1 Generation
- 2 Data values
	- 2.1 ID
	- 2.2 Config
- 3 History
- 4 Issues

## Generation
Small islands are generated from Y=55 to Y=70 around outer islands. The probability that a small island tries to generate in each chunk is 1⁄14. It generates successfully when in small end islands biome‌[Java Edition  only] or at a chunk where the noise value fits‌[Bedrock Edition  only]. In Java Edition, if it tries generate a small island in a chunk, there's an 1⁄4 probability to try to generate another small island in this chunk. The two islands often overlap with each other.In Bedrock Edition, if the the chunk's noise value fits, there's also a probability of 1⁄4 to re-generate another island, but at the exactly same position, which makes the two islands look like a sinlge island. 

It also generates when an end gateway spawns on the outer island if the chunk does not provide any End stone.

## Data values
### ID
Java Edition:

| Feature type        | Identifier   |
|---------------------|--------------|
| [No displayed name] | `end_island` |

| Configured feature  | Identifier   |
|---------------------|--------------|
| [No displayed name] | `end_island` |

Bedrock Edition:

| Feature             | Identifier |
|---------------------|------------|
| [No displayed name] | `[No ID]`  |

### Config
Main article: Configured feature
Java Edition:

- config: Empty


An example

{
  "type": "minecraft:end_island",
  "config": {}
}



