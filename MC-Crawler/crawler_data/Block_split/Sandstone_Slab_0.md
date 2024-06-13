# Sandstone Slab
A sandstone slab is a sandstone variant of a slab.

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
- 7 References

## Obtaining
### Breaking
Sandstone slabs can be mined using any pickaxe.

| Block     | Sandstone Slab        |
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
Sandstone slabs generate as part of desert pyramids, desert villages and desert wells.

### Crafting
| Ingredients                   | Crafting recipe |
|-------------------------------|-----------------|
| SandstoneorChiseled Sandstone | 6               |

### Stonecutting
| Ingredients | Cutting recipe |
|-------------|----------------|
| Sandstone   | 2              |

## Usage
For information about the placement mechanics of all slabs, see Slab § Usage.

### Crafting ingredient
| Name               | Ingredients    | Crafting recipe |
|--------------------|----------------|-----------------|
| Chiseled Sandstone | Sandstone Slab |                 |

### Note blocks
Sandstone slabs can be placed under note blocks to produce "bass drum" sounds.

## Data values
### ID
Java Edition:

| Name           | Identifier     | Form         | Block tags            | Item tags | Translation key                |
|----------------|----------------|--------------|-----------------------|-----------|--------------------------------|
| Sandstone Slab | sandstone_slab | Block & Item | slabsmineable/pickaxe | slabs     | block.minecraft.sandstone_slab |

Bedrock Edition:

| Name                  | Identifier              | Alias ID          | Numeric ID | Form                         | Item ID[i 1]                                           | Translation key                  |
|-----------------------|-------------------------|-------------------|------------|------------------------------|--------------------------------------------------------|----------------------------------|
| Double Sandstone Slab | double_stone_block_slab | double_stone_slab | 43         | Block & Ungiveable Item[i 2] | double_stone_block_slabAlias ID:real_double_stone_slab | tile.double_stone_slab.sand.name |
| Sandstone Slab        | stone_block_slab        | stone_slab        | 44         | Block & Giveable Item[i 3]   | stone_block_slabAlias ID:double_stone_slab             | tile.stone_slab.sand.name        |


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




