# Freeze top layer
A freeze top layer is a feature found throughout the Overworld.

## Contents
- 1 Generation
- 2 Data values
	- 2.1 ID
	- 2.2 Config
- 3 History

## Generation
Freeze top layer is a feature that is used to add snow and ice to mountains and cold biomes.

Freeze top layer tries to generate in all chunks in Overworld. In each chunk, it tries at each block column to generate snow or ice on the terrain surface if the temperature there is cold enough (below 0.15) and the block light level is less than 10. If the surface is water, an ice block replaces the water. And a snow tries to generate on the surface if it can attach on the surface's block.

## Data values
### ID
Java Edition:

| Feature type        | Identifier         |
|---------------------|--------------------|
| [No displayed name] | `freeze_top_layer` |

| Configured feature  | Identifier         |
|---------------------|--------------------|
| [No displayed name] | `freeze_top_layer` |

Bedrock Edition:

In Bedrock Edition, it is not a feature technically. The game simply iterates through each horizonal coordinate after the chunk generation to generate ice and snow.

### Config
Main article: Configured feature
Java Edition:

- config: Empty


An example

{
  "type": "minecraft:freeze_top_layer",
  "config": {}
}




