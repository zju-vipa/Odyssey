# Mossy Stone Brick Slab
A mossy stone brick slab is a mossy stone brick variant of a slab.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
	- 1.4 Stonecutting
- 2 Usage
	- 2.1 Note blocks
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 References

## Obtaining
### Breaking
Mossy stone brick slabs can be mined using any pickaxe.

| Block     | Mossy Stone Brick Slab |
|-----------|------------------------|
| Hardness  | 1.5                    |
| Tool      |                        |
|           | Breakingtime (sec)[A]  |
| Default   | 7.5                    |
| Wooden    | 1.15                   |
| Stone     | 0.6                    |
| Iron      | 0.4                    |
| Diamond   | 0.3                    |
| Netherite | 0.25                   |
| Golden    | 0.2                    |


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


### Natural generation
Mossy stone brick slabs generate as part of ruined portals in the Overworld.

### Crafting
| Ingredients        | Crafting recipe |
|--------------------|-----------------|
| Mossy Stone Bricks | 6               |

### Stonecutting
| Ingredients        | Cutting recipe |
|--------------------|----------------|
| Mossy Stone Bricks | 2              |

## Usage
For information about the placement mechanics of all slabs, see Slab § Usage.

### Note blocks
Mossy stone brick slabs can be placed under note blocks to produce "bass drum" sounds.

## Data values
### ID
Java Edition:

| Name                   | Identifier             | Form         | Block tags            | Item tags | Translation key                        |
|------------------------|------------------------|--------------|-----------------------|-----------|----------------------------------------|
| Mossy Stone Brick Slab | mossy_stone_brick_slab | Block & Item | slabsmineable/pickaxe | slabs     | block.minecraft.mossy_stone_brick_slab |

Bedrock Edition:

| Name                          | Identifier               | Alias ID           | Numeric ID | Form                         | Item ID[i 1]                                             | Translation key                         |
|-------------------------------|--------------------------|--------------------|------------|------------------------------|----------------------------------------------------------|-----------------------------------------|
| Double Mossy Stone Brick Slab | double_stone_block_slab4 | double_stone_slab4 | 423        | Block & Ungiveable Item[i 2] | double_stone_block_slab4Alias ID:real_double_stone_slab4 | —                                       |
| Mossy Stone Brick Slab        | stone_block_slab4        | stone_slab4        | 421        | Block & Giveable Item[i 3]   | stone_block_slab4Alias ID:double_stone_slab4             | tile.stone_slab4.mossy_stone_brick.name |


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

| Name                    | Metadata Bits | Default value     | Allowed values    | Values forMetadata Bits | Description                         |
|-------------------------|---------------|-------------------|-------------------|-------------------------|-------------------------------------|
| minecraft:vertical_half | Not Supported | bottom            | bottomtop         | Unsupported             | Where the slab is within its block. |
| stone_slab_type_4       | 0x10x20x4     | mossy_stone_brick | mossy_stone_brick | 0                       | Mossy Stone Brick Slab              |
|                         |               |                   | smooth_quartz     | 1                       | Smooth Quartz Slab                  |
|                         |               |                   | stone             | 2                       | Stone Slab                          |
|                         |               |                   | cut_sandstone     | 3                       | Cut Sandstone Slab                  |
|                         |               |                   | cut_red_sandstone | 4                       | Cut Red Sandstone Slab              |




