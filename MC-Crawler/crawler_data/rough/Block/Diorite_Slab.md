# Diorite Slab
A diorite slab is a diorite variant of a slab.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Crafting
	- 1.3 Stonecutting
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
Diorite slabs can be mined using any pickaxe.

| Block     | Diorite Slab          |
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

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Crafting
| Ingredients | Crafting recipe |
|-------------|-----------------|
| Diorite     | 6               |

### Stonecutting
| Ingredients | Cutting recipe |
|-------------|----------------|
| Diorite     | 2              |

## Usage
For information about the placement mechanics of all slabs, see Slab § Usage.

### Note blocks
Diorite slabs can be placed under note blocks to produce "bass drum" sounds.

## Data values
### ID
Java Edition:

| Name         | Identifier     | Form         | Block tags                     | Item tags | Translation key                |
|--------------|----------------|--------------|--------------------------------|-----------|--------------------------------|
| Diorite Slab | `diorite_slab` | Block & Item | `slabs`<br/>`mineable/pickaxe` | `slabs`   | `block.minecraft.diorite_slab` |

Bedrock Edition:

| Name                | Identifier                 | Alias ID             | Numeric ID | Form                         | Item ID[i 1]                                                      | Translation key                 |
|---------------------|----------------------------|----------------------|------------|------------------------------|-------------------------------------------------------------------|---------------------------------|
| Double Diorite Slab | `double_stone_block_slab3` | `double_stone_slab3` | `422`      | Block & Ungiveable Item[i 2] | `double_stone_block_slab3`<br/>Alias ID:`real_double_stone_slab3` | —                               |
| Diorite Slab        | `stone_block_slab3`        | `stone_slab3`        | `417`      | Block & Giveable Item[i 3]   | `stone_block_slab3`<br/>Alias ID:`double_stone_slab3`             | `tile.stone_slab3.diorite.name` |

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

| Name                    | Metadata Bits             | Default value     | Allowed values         | Values forMetadata Bits | Description                         |
|-------------------------|---------------------------|-------------------|------------------------|-------------------------|-------------------------------------|
| minecraft:vertical_half | Not Supported             | `bottom`          | `bottom`<br/>`top`     | `Unsupported`           | Where the slab is within its block. |
| stone_slab_type_3       | `0x1`<br/>`0x2`<br/>`0x4` | `end_stone_brick` | `end_stone_brick`      | `0`                     | End Stone Brick Slab                |
|                         |                           |                   | `smooth_red_sandstone` | `1`                     | Smooth Red Sandstone Slab           |
|                         |                           |                   | `polished_andesite`    | `2`                     | Polished Andesite Slab              |
|                         |                           |                   | `andesite`             | `3`                     | Andesite Slab                       |
|                         |                           |                   | `diorite`              | `4`                     | Diorite Slab                        |
|                         |                           |                   | `polished_diorite`     | `5`                     | Polished Diorite Slab               |
|                         |                           |                   | `granite`              | `6`                     | Granite Slab                        |
|                         |                           |                   | `polished_granite`     | `7`                     | Polished Granite Slab               |



