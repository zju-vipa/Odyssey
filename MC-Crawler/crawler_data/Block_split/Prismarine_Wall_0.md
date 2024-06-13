# Prismarine Wall
A prismarine wall is a prismarine variant of a wall.

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
Prismarine walls can be mined using any pickaxe. If mined without a pickaxe, they drop nothing.

| Block     | Prismarine Wall       |
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


### Crafting
| Ingredients | Crafting recipe |
|-------------|-----------------|
| Prismarine  | 6               |

### Stonecutting
| Ingredients | Cutting recipe |
|-------------|----------------|
| Prismarine  |                |

## Usage
Main article: Wall § Usage
### Note blocks
Prismarine walls can be placed under note blocks to produce "bass drum" sounds.

## Data values
### ID
Java Edition:

| Name            | Identifier      | Form         | Block tags | Item tags | Translation key                 |
|-----------------|-----------------|--------------|------------|-----------|---------------------------------|
| Prismarine Wall | prismarine_wall | Block & Item | walls      | walls     | block.minecraft.prismarine_wall |

Bedrock Edition:

| Name            | Identifier       | Numeric ID | Form                       | Item ID[i 1]   | Translation key                       |
|-----------------|------------------|------------|----------------------------|----------------|---------------------------------------|
| Prismarine Wall | cobblestone_wall | 139        | Block & Giveable Item[i 2] | Identical[i 3] | tile.cobblestone_wall.prismarine.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


### Block states
Java Edition

| Name        | Default value | Allowed values | Description                                                  |
|-------------|---------------|----------------|--------------------------------------------------------------|
| east        | none          | lownonetall    | How the wall extends from the center post to the east.       |
| north       | none          | lownonetall    | How the wall extends from the center post to the north.      |
| south       | none          | lownonetall    | How the wall extends from the center post to the south.      |
| up          | true          | falsetrue      | When true, the wall has a center post.                       |
| waterlogged | false         | falsetrue      | Whether or not there's water in the same place as this wall. |
| west        | none          | lownonetall    | How the wall extends from the center post to the west.       |

Bedrock Edition

| Name                       | Metadata Bits | Default value | Allowed values                                                                                                                                           | Values forMetadata Bits | Description                                                          |
|----------------------------|---------------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|----------------------------------------------------------------------|
| wall_block_type            | 0x10x20x40x8  | cobblestone   | cobblestonemossy_cobblestonegranitedioriteandesitesandstonebrickstone_brickmossy_stone_bricknether_brickend_brickprismarinered_sandstonered_nether_brick | 012345678910111213      | The type of wall; for example,stone_brickdenotes a stone brick wall. |
| wall_connection_type_east  | Not Supported | none          | noneshorttall                                                                                                                                            | Unsupported             | How the wall extends from the center post to the east.               |
| wall_connection_type_north | Not Supported | none          | noneshorttall                                                                                                                                            | Unsupported             | How the wall extends from the center post to the north.              |
| wall_connection_type_south | Not Supported | none          | noneshorttall                                                                                                                                            | Unsupported             | How the wall extends from the center post to the south.              |
| wall_connection_type_west  | Not Supported | none          | noneshorttall                                                                                                                                            | Unsupported             | How the wall extends from the center post to the west.               |
| wall_post_bit              | Not Supported | true          | falsetrue                                                                                                                                                | Unsupported             | Whether or not the wall has a center post.                           |




