# Basalt
Basalt is an igneous rock found in the Nether.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Post-generation
- 2 Usage
	- 2.1 Crafting
	- 2.2 Stonecutting
	- 2.3 Smelting ingredient
	- 2.4 Note blocks
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 Trivia
- 8 Gallery
- 9 References
- 10 External links

## Obtaining
### Breaking
Basalt drops as an item if mined by any pickaxe. If mined by any other tool, it drops nothing.

| Block     | Basalt                |
|-----------|-----------------------|
| Hardness  | 1.25                  |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 6.25                  |
| Wooden    | 0.95                  |
| Stone     | 0.5                   |
| Iron      | 0.35                  |
| Diamond   | 0.25                  |
| Netherite | 0.25                  |
| Golden    | 0.2                   |


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


### Natural generation
Basalt generates naturally as basalt pillars, which are found in the soul sand valley biome. They also generate in the basalt deltas biome as regular terrain and as part of basalt columns. In Java Edition, they also generate in blobs, which attempt to replace netherrack 75 times per chunk in blobs of radius 3—7, from levels 0 to 127, in basalt deltas biome.

Basalt can also be found naturally as part of bastion remnants.


### Post-generation
A simple basalt generator.
Basalt can also be made by lava flowing into a space that is on top of soul soil and adjacent to blue ice. The flowing lava is then replaced with basalt.

## Usage
Basalt's only current use is as building material. Like logs and quartz pillars, basalt points perpendicular to whatever block face they are placed on.

### Crafting
| Name            | Ingredients | Crafting recipe |
|-----------------|-------------|-----------------|
| Polished Basalt | Basalt      | 4               |

### Stonecutting
| Name            | Ingredients | Cutting recipe |
|-----------------|-------------|----------------|
| Polished Basalt | Basalt      |                |

### Smelting ingredient
| Name          | Ingredients    | Smelting recipe |
|---------------|----------------|-----------------|
| Smooth Basalt | Basalt+Anyfuel | 0.1             |

### Note blocks
Basalt can be placed under note blocks to produce "bass drum" sound.

## Data values
### ID
Java Edition:

| Name   | Identifier | Form         | Block tags                        | Translation key        |
|--------|------------|--------------|-----------------------------------|------------------------|
| Basalt | basalt     | Block & Item | base_stone_nethermineable/pickaxe | block.minecraft.basalt |

Bedrock Edition:

| Name   | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key  |
|--------|------------|------------|----------------------------|----------------|------------------|
| Basalt | basalt     | 489        | Block & Giveable Item[i 2] | Identical[i 3] | tile.basalt.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


### Block states
See also: Block states

Java Edition:

| Name | Default value | Allowed values | Description                         |
|------|---------------|----------------|-------------------------------------|
| axis | y             | x              | The basalt is oriented east–west.   |
|      |               | y              | The basalt is oriented vertically.  |
|      |               | z              | The basalt is oriented north–south. |

Bedrock Edition:

| Name        | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                         |
|-------------|---------------|---------------|----------------|-------------------------|-------------------------------------|
| pillar_axis | 0x10x2        | y             | x              | 1                       | The basalt is oriented east–west.   |
|             |               |               | y              | 0                       | The basalt is oriented vertically.  |
|             |               |               | z              | 2                       | The basalt is oriented north–south. |




