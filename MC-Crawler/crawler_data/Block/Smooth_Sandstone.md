# Smooth Sandstone
Smooth sandstone is a variant of sandstone, obtained by smelting.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Smelting
- 2 Usage
	- 2.1 Crafting ingredient
	- 2.2 Stonecutting
	- 2.3 Note blocks
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
	- 5.1 Data history
- 6 Issues
- 7 References

## Obtaining
### Breaking
Smooth sandstone can be mined with any pickaxe. If mined without a pickaxe, the block drops nothing.

| Block     | Smooth Sandstone      |
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
Smooth sandstone generates in desert villages. 

### Smelting
| Ingredients       | Smelting recipe |
|-------------------|-----------------|
| Sandstone+Anyfuel | 0.1             |

## Usage
Unlike sand, smooth sandstone is never affected by gravity.

### Crafting ingredient
| Name                    | Ingredients      | Crafting recipe |
|-------------------------|------------------|-----------------|
| Smooth Sandstone Slab   | Smooth Sandstone | 6               |
| Smooth Sandstone Stairs | Smooth Sandstone | 4               |

### Stonecutting
| Ingredients      | Cutting recipe |
|------------------|----------------|
| Smooth Sandstone | 2              |

### Note blocks
Smooth sandstone can be placed under note blocks to produce "bass drum" sounds.

## Data values
### ID
Java Edition:

| Name             | Identifier       | Form         | Translation key                  |
|------------------|------------------|--------------|----------------------------------|
| Smooth Sandstone | smooth_sandstone | Block & Item | block.minecraft.smooth_sandstone |

Bedrock Edition:

| Name             | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key            |
|------------------|------------|------------|----------------------------|----------------|----------------------------|
| Smooth Sandstone | sandstone  | 24         | Block & Giveable Item[i 2] | Identical[i 3] | tile.sandstone.smooth.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


### Block states
See also: Block states

In Bedrock Edition, smooth sandstone use the following block states:

Bedrock Edition:

| Name            | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description        |
|-----------------|---------------|---------------|----------------|-------------------------|--------------------|
| sand_stone_type | 0x10x2        | default       | default        | 0                       | Sandstone          |
|                 |               |               | heiroglyphs    | 1                       | Chiseled Sandstone |
|                 |               |               | cut            | 2                       | Cut Sandstone      |
|                 |               |               | smooth         | 3                       | Smooth Sandstone   |



