# Smooth Quartz Block
A smooth quartz block is a mineral block used only for decoration. It is made by smelting blocks of quartz.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Smelting
- 2 Usage
	- 2.1 Crafting ingredient
	- 2.2 Stonecutting
	- 2.3 Note Blocks
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 Gallery

## Obtaining
### Breaking
Smooth quartz blocks can be mined using any pickaxe. If mined without a pickaxe, it drops nothing.

| Block     | Smooth Quartz Block   |
|-----------|-----------------------|
| Hardness  | 2                     |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 10                    |
| Wooden    | 1.5                   |
| Stone     | 0.75                  |
| Iron      | 0.5                   |
| Diamond   | 0.4                   |
| Netherite | 0.35                  |
| Golden    | 0.25                  |


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


### Natural generation
2 smooth quartz blocks generate naturally as part of each bridge bastion remnant.

### Smelting
| Name                | Ingredients             | Smelting recipe |
|---------------------|-------------------------|-----------------|
| Smooth Quartz Block | Block of Quartz+Anyfuel | 0.1             |

## Usage
### Crafting ingredient
| Name                 | Ingredients         | Crafting recipe |
|----------------------|---------------------|-----------------|
| Smooth Quartz Slab   | Smooth Quartz Block | 6               |
| Smooth Quartz Stairs | Smooth Quartz Block | 4               |

### Stonecutting
| Ingredients         | Cutting recipe |
|---------------------|----------------|
| Smooth Quartz Block | 2              |

### Note Blocks
Smooth quartz blocks can be placed under note blocks to produce "bass drum" sounds.

## Data values
### ID
Java Edition:

| Name                | Identifier    | Form         | Translation key               |
|---------------------|---------------|--------------|-------------------------------|
| Smooth Quartz Block | smooth_quartz | Block & Item | block.minecraft.smooth_quartz |

Bedrock Edition:

| Name                | Identifier   | Numeric ID | Form                       | Item ID[i 1]   | Translation key               |
|---------------------|--------------|------------|----------------------------|----------------|-------------------------------|
| Smooth Quartz Block | quartz_block | 155        | Block & Giveable Item[i 2] | Identical[i 3] | tile.quartz_block.smooth.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


### Block states
See also: Block states

Bedrock Edition:

| Name        | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                               |
|-------------|---------------|---------------|----------------|-------------------------|-------------------------------------------|
| chisel_type | 0x10x2        | default       | default        | 0                       | Block of Quartz                           |
|             |               |               | chiseled       | 1                       | Chiseled Quartz Block                     |
|             |               |               | lines          | 2                       | Pillar Quartz Block                       |
|             |               |               | smooth         | 3                       | Smooth Quartz Block                       |
| pillar_axis | 0x40x8        | y             | x              | 1                       | The quartz block is oriented east–west.   |
|             |               |               | y              | 0                       | The quartz block is oriented vertically.  |
|             |               |               | z              | 2                       | The quartz block is oriented north–south. |

