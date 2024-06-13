# Smooth Stone Slab
A smooth stone slab is a smooth stone variant of a slab.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
	- 1.4 Stonecutting
- 2 Usage
	- 2.1 Crafting ingredient
	- 2.2 Note blocks
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 Gallery
	- 7.1 Screenshots
- 8 References

## Obtaining
### Breaking
Smooth stone slabs can be mined using any pickaxe.

| Block     | Smooth Stone Slab     |
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
Smooth stone slabs generate as part of strongholds and plains, savanna, taiga, and snowy tundra villages.

### Crafting
| Ingredients  | Crafting recipe |
|--------------|-----------------|
| Smooth Stone | 6               |

### Stonecutting
| Ingredients  | Cutting recipe |
|--------------|----------------|
| Smooth Stone | 2              |

## Usage
For information about the placement mechanics of all slabs, see Slab § Usage.

### Crafting ingredient
| Name        | Ingredients             | Crafting recipe |
|-------------|-------------------------|-----------------|
| Armor Stand | Stick+Smooth Stone Slab |                 |

### Note blocks
Smooth stone slabs can be placed under note blocks to produce "bass drum" sounds.

## Data values
### ID
Java Edition:

| Name              | Identifier        | Form         | Block tags            | Item tags | Translation key                   |
|-------------------|-------------------|--------------|-----------------------|-----------|-----------------------------------|
| Smooth Stone Slab | smooth_stone_slab | Block & Item | slabsmineable/pickaxe | slabs     | block.minecraft.smooth_stone_slab |

Bedrock Edition:

| Name                     | Identifier              | Alias ID          | Numeric ID | Form                         | Item ID[i 1]                                           | Translation key                   |
|--------------------------|-------------------------|-------------------|------------|------------------------------|--------------------------------------------------------|-----------------------------------|
| Double Smooth Stone Slab | double_stone_block_slab | double_stone_slab | 43         | Block & Ungiveable Item[i 2] | double_stone_block_slabAlias ID:real_double_stone_slab | tile.double_stone_slab.stone.name |
| Smooth Stone Slab        | stone_block_slab        | stone_slab        | 44         | Block & Giveable Item[i 3]   | stone_block_slabAlias ID:double_stone_slab             | tile.stone_slab.stone.name        |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Unavailable with /give command

↑ Available with /give command.


### Block states
See also: Block states

Java Edition:

| Name        | Default value | Allowed values | Description                                                  |
|-------------|---------------|----------------|--------------------------------------------------------------|
| type        | bottom        | bottomtop      | Where the slab is within its block.                          |
|             |               | double         | The block is a double slab.                                  |
| waterlogged | false         | falsetrue      | Whether or not there's water in the same place as this slab. |

Bedrock Edition:

| Name                    | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                         |
|-------------------------|---------------|---------------|----------------|-------------------------|-------------------------------------|
| minecraft:vertical_half | Not Supported | bottom        | bottomtop      | Unsupported             | Where the slab is within its block. |
| stone_slab_type         | 0x10x20x4     | smooth_stone  | smooth_stone   | 0                       | Smooth Stone Slab                   |
|                         |               |               | sandstone      | 1                       | Sandstone Slab                      |
|                         |               |               | wood           | 2                       | Petrified Oak Slab                  |
|                         |               |               | cobblestone    | 3                       | Cobblestone Slab                    |
|                         |               |               | brick          | 4                       | Brick Slab                          |
|                         |               |               | stone_brick    | 5                       | Stone Brick Slab                    |
|                         |               |               | quartz         | 6                       | Quartz Slab                         |
|                         |               |               | nether_brick   | 7                       | Nether Brick Slab                   |



