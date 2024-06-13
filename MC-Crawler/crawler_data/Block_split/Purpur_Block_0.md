# Purpur Block
Purpur blocks are decorative blocks that are naturally generated in end cities and end ships.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
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
- 7 Trivia
- 8 See also
- 9 External links

## Obtaining
### Breaking
Purpur blocks can be mined using any pickaxe. If mined without a pickaxe, it drops nothing.

| Block     | Purpur Block          |
|-----------|-----------------------|
| Hardness  | 1.5                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 7.5                   |
| Wooden    | 1.15                  |
| Stone     | 0.6                   |
| Iron      | 0.4                   |
| Diamond   | 0.3                   |
| Netherite | 0.25                  |
| Golden    | 0.2                   |


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


### Natural generation
Purpur blocks can be found naturally as part of the structure of end cities and end ships.

### Crafting
| Ingredients         | Crafting recipe |
|---------------------|-----------------|
| Popped Chorus Fruit | 4               |

## Usage
Purpur blocks are primarily decorative blocks, similar to other brick-type blocks. They can also be used to craft different variants of the block. 

### Crafting ingredient
| Name                               | Ingredients                           | Crafting recipe | Description              |
|------------------------------------|---------------------------------------|-----------------|--------------------------|
| Purpur Slab                        | Purpur Block                          | 6               | ‌[Java Edition  only]    |
| Purpur Slab                        | Purpur Block                          | 6               | ‌[Bedrock Edition  only] |
| Purpur Stairs                      | Purpur Block                          | 4               |                          |
| Spire Armor Trim Smithing Template | Diamond+Spire Armor Trim+Purpur Block | 2               |                          |

### Stonecutting
| Name                                      | Ingredients  | Cutting recipe |
|-------------------------------------------|--------------|----------------|
| Purpur SlaborPurpur StairsorPurpur Pillar | Purpur Block | 2              |

### Note Blocks
Purpur blocks can be placed under note blocks to produce "bass drum" sound.

## Data values
### ID
Java Edition:

| Name         | Identifier   | Form         | Block tags       | Translation key              |
|--------------|--------------|--------------|------------------|------------------------------|
| Purpur Block | purpur_block | Block & Item | mineable/pickaxe | block.minecraft.purpur_block |

Bedrock Edition:

| Name         | Identifier   | Numeric ID | Form                       | Item ID[i 1]   | Translation key                |
|--------------|--------------|------------|----------------------------|----------------|--------------------------------|
| Purpur Block | purpur_block | 201        | Block & Giveable Item[i 2] | Identical[i 3] | tile.purpur_block.default.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


### Block states
See also: Block states

Bedrock Edition:

| Name        | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                               |
|-------------|---------------|---------------|----------------|-------------------------|-------------------------------------------|
| chisel_type | 0x10x2        | default       | default        | 0                       | Purpur Block                              |
|             |               |               | chiseled       | 1                       | Chiseled Purpur(Unused)                   |
|             |               |               | lines          | 2                       | Purpur Pillar                             |
|             |               |               | smooth         | 3                       | Smooth Purpur(Unused)                     |
| pillar_axis | 0x40x8        | y             | x              | 1                       | The purpur block is oriented east–west.   |
|             |               |               | y              | 0                       | The purpur block is oriented vertically.  |
|             |               |               | z              | 2                       | The purpur block is oriented north–south. |



## See also
- Chorus fruit farming– means to produce materials for purpur blocks in mass numbers


