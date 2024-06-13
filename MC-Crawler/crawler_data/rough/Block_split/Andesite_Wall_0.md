# Andesite Wall
An andesite wall is an andesite variant of a wall.

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
- 7 Gallery
	- 7.1 Screenshots
- 8 References

## Obtaining
### Breaking
Andesite walls can be mined using any pickaxe. If mined without a pickaxe, they drop nothing.

| Block     | Andesite Wall         |
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
| Andesite    | 6               |

### Stonecutting
| Ingredients | Cutting recipe |
|-------------|----------------|
| Andesite    |                |

## Usage
For information about the placement mechanics of all walls, see Wall § Usage.

### Note blocks
Andesite walls can be placed under note blocks to produce "bass drum" sounds.

## Data values
### ID
Java Edition:

| Name          | Identifier      | Form         | Block tags | Item tags | Translation key                 |
|---------------|-----------------|--------------|------------|-----------|---------------------------------|
| Andesite Wall | `andesite_wall` | Block & Item | `walls`    | `walls`   | `block.minecraft.andesite_wall` |

Bedrock Edition:

| Name          | Identifier         | Numeric ID | Form                       | Item ID[i 1]   | Translation key                       |
|---------------|--------------------|------------|----------------------------|----------------|---------------------------------------|
| Andesite Wall | `cobblestone_wall` | `139`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.cobblestone_wall.andesite.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
Java Edition

| Name        | Default value | Allowed values              | Description                                                  |
|-------------|---------------|-----------------------------|--------------------------------------------------------------|
| east        | `none`        | `low`<br/>`none`<br/>`tall` | How the wall extends from the center post to the east.       |
| north       | `none`        | `low`<br/>`none`<br/>`tall` | How the wall extends from the center post to the north.      |
| south       | `none`        | `low`<br/>`none`<br/>`tall` | How the wall extends from the center post to the south.      |
| up          | `true`        | `false`<br/>`true`          | When true, the wall has a center post.                       |
| waterlogged | `false`       | `false`<br/>`true`          | Whether or not there's water in the same place as this wall. |
| west        | `none`        | `low`<br/>`none`<br/>`tall` | How the wall extends from the center post to the west.       |

Bedrock Edition

| Name                       | Metadata Bits                       | Default value | Allowed values                                                                                                                                                                                                                                        | Values forMetadata Bits                                                                                         | Description                                                            |
|----------------------------|-------------------------------------|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| wall_block_type            | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8` | `cobblestone` | `cobblestone`<br/>`mossy_cobblestone`<br/>`granite`<br/>`diorite`<br/>`andesite`<br/>`sandstone`<br/>`brick`<br/>`stone_brick`<br/>`mossy_stone_brick`<br/>`nether_brick`<br/>`end_brick`<br/>`prismarine`<br/>`red_sandstone`<br/>`red_nether_brick` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13` | The type of wall; for example,`stone_brick`denotes a stone brick wall. |
| wall_connection_type_east  | Not Supported                       | `none`        | `none`<br/>`short`<br/>`tall`                                                                                                                                                                                                                         | `Unsupported`                                                                                                   | How the wall extends from the center post to the east.                 |
| wall_connection_type_north | Not Supported                       | `none`        | `none`<br/>`short`<br/>`tall`                                                                                                                                                                                                                         | `Unsupported`                                                                                                   | How the wall extends from the center post to the north.                |
| wall_connection_type_south | Not Supported                       | `none`        | `none`<br/>`short`<br/>`tall`                                                                                                                                                                                                                         | `Unsupported`                                                                                                   | How the wall extends from the center post to the south.                |
| wall_connection_type_west  | Not Supported                       | `none`        | `none`<br/>`short`<br/>`tall`                                                                                                                                                                                                                         | `Unsupported`                                                                                                   | How the wall extends from the center post to the west.                 |
| wall_post_bit              | Not Supported                       | `true`        | `false`<br/>`true`                                                                                                                                                                                                                                    | `Unsupported`                                                                                                   | Whether or not the wall has a center post.                             |




