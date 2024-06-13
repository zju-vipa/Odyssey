# Mossy Cobblestone Slab
A mossy cobblestone slab is a mossy cobblestone variant of a slab.

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
Mossy cobblestone slabs can be mined using any pickaxe.

| Block     | Mossy Cobblestone Slab |
|-----------|------------------------|
| Hardness  | 2                      |
| Tool      |                        |
|           | Breakingtime (sec)[A]  |
| Default   | 10                     |
| Wooden    | 1.5                    |
| Stone     | 0.75                   |
| Iron      | 0.5                    |
| Diamond   | 0.4                    |
| Netherite | 0.35                   |
| Golden    | 0.25                   |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Natural generation
Mossy cobblestone slabs generate as part of pillager outposts.

### Crafting
| Ingredients       | Crafting recipe |
|-------------------|-----------------|
| Mossy Cobblestone | 6               |

### Stonecutting
| Ingredients       | Cutting recipe |
|-------------------|----------------|
| Mossy Cobblestone | 2              |

## Usage
For information about the placement mechanics of all slabs, see Slab § Usage.

### Note blocks
Mossy cobblestone slabs can be placed under note blocks to produce "bass drum" sounds.

## Data values
### ID
Java Edition:

| Name                   | Identifier               | Form         | Block tags                     | Item tags | Translation key                          |
|------------------------|--------------------------|--------------|--------------------------------|-----------|------------------------------------------|
| Mossy Cobblestone Slab | `mossy_cobblestone_slab` | Block & Item | `slabs`<br/>`mineable/pickaxe` | `slabs`   | `block.minecraft.mossy_cobblestone_slab` |

Bedrock Edition:

| Name                          | Identifier                 | Alias ID             | Numeric ID | Form                         | Item ID[i 1]                                                      | Translation key                           |
|-------------------------------|----------------------------|----------------------|------------|------------------------------|-------------------------------------------------------------------|-------------------------------------------|
| Double Mossy Cobblestone Slab | `double_stone_block_slab2` | `double_stone_slab2` | `181`      | Block & Ungiveable Item[i 2] | `double_stone_block_slab2`<br/>Alias ID:`real_double_stone_slab2` | —                                         |
| Mossy Cobblestone Slab        | `stone_block_slab2`        | `stone_slab2`        | `182`      | Block & Giveable Item[i 3]   | `stone_block_slab2`<br/>Alias ID:`double_stone_slab2`             | `tile.stone_slab2.mossy_cobblestone.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Unavailable with /give command
3. ↑Available with /give command.

### Block states
See also: Block states

Java Edition:

| Name        | Default value | Allowed values     | Description                                                  |
|-------------|---------------|--------------------|--------------------------------------------------------------|
| type        | `bottom`      | `bottom`<br/>`top` | Where the slab is within its block.                          |
|             |               | `double`           | The block is a double slab.                                  |
| waterlogged | `false`       | `false`<br/>`true` | Whether or not there's water in the same place as this slab. |

Bedrock Edition:

| Name                    | Metadata Bits             | Default value   | Allowed values      | Values forMetadata Bits | Description                         |
|-------------------------|---------------------------|-----------------|---------------------|-------------------------|-------------------------------------|
| minecraft:vertical_half | Not Supported             | `bottom`        | `bottom`<br/>`top`  | `Unsupported`           | Where the slab is within its block. |
| stone_slab_type_2       | `0x1`<br/>`0x2`<br/>`0x4` | `red_sandstone` | `red_sandstone`     | `0`                     | Red Sandstone Slab                  |
|                         |                           |                 | `purpur`            | `1`                     | Purpur Slab                         |
|                         |                           |                 | `prismarine_rough`  | `2`                     | Prismarine Slab                     |
|                         |                           |                 | `prismarine_dark`   | `3`                     | Dark Prismarine Slab                |
|                         |                           |                 | `prismarine_brick`  | `4`                     | Prismarine Brick Slab               |
|                         |                           |                 | `mossy_cobblestone` | `5`                     | Mossy Cobblestone Slab              |
|                         |                           |                 | `smooth_sandstone`  | `6`                     | Smooth Sandstone Slab               |
|                         |                           |                 | `red_nether_brick`  | `7`                     | Red Nether Brick Slab               |




