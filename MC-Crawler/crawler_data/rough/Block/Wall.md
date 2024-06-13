# Wall
A wall is a decorative block. Like fences, they can be used to create boundaries, because players and most mobs cannot climb or jump over them.

## Contents
- 1 Variants
- 2 Obtaining
	- 2.1 Crafting
	- 2.2 Stonecutting
- 3 Usage
	- 3.1 Note Blocks
- 4 Block states
- 5 History
- 6 Issues
- 7 Trivia
- 8 Gallery
	- 8.1 Screenshots
	- 8.2 Concept artwork
- 9 See also
- 10 References

## Variants
There are 22 (25‌[upcoming: JE 1.21 & BE 1.21.0]) variants of walls:

- Cobblestone Wall
- Mossy Cobblestone Wall
- Stone Brick Wall
- Mossy Stone Brick Wall
- Granite Wall
- Diorite Wall
- Andesite Wall
- Cobbled Deepslate Wall
- Polished Deepslate Wall
- Deepslate Brick Wall
- Deepslate Tile Wall
- Tuff Wall‌[upcoming: JE 1.21 & BE 1.21.0]
- Polished Tuff Wall‌[upcoming: JE 1.21 & BE 1.21.0]
- Tuff Brick Wall‌[upcoming: JE 1.21 & BE 1.21.0]
- Brick Wall
- Mud Brick Wall
- Sandstone Wall
- Red Sandstone Wall
- Prismarine Wall
- Nether Brick Wall
- Red Nether Brick Wall
- Blackstone Wall
- Polished Blackstone Wall
- Polished Blackstone Brick Wall
- End Stone Brick Wall

## Obtaining
### Crafting
All walls have the same crafting recipe shape, with six blocks of the same type resulting in six walls of the same type.

| Ingredients           | Crafting recipe           |
|-----------------------|---------------------------|
| Stone or brick blocks | 6666666666666666666666666 |

### Stonecutting
All walls can be obtained by stonecutting. As with crafting, each used block results in one crafted wall.

| Ingredients          | Cutting recipe |
|----------------------|----------------|
| Stone or brick block |                |

## Usage
Due to the wall's hitboxes being 1.5 blocks tall for mobs, this rabbit could be seen "floating".
Walls are one and a half blocks tall for player or mob collisions, and one block tall for all other purposes, similar to fences. This prevents players and mobs from jumping over them, while using only one actual block space. A wall occupies the center space of blocks. A wall block automatically connects to any adjacent solid block, and its top rises slightly to support any block immediately above.

Wall blocks are more efficient at fencing off mobs than a two-block high wall of regular blocks, costing half as many blocks, and being more space-efficient as well. However, a skeleton might shoot over the wall, a creeper could explode if a player is standing near the wall, and a spider could still climb over the wall.

Unlike fences, if two walls are placed one block apart diagonally, the player cannot walk between them.

Walls connect to other walls to create a large, flat wall. They also connect horizontally to iron bars and glass panes. However, they do not connect to fences (fence gates can be connected though).[1]

### Note Blocks
Walls can be placed under note blocks to produce "bass drum" sounds.

## Block states
See also: Block states

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
Non-blackstone and deepslate wall:

| Name                       | Metadata Bits                       | Default value | Allowed values                                                                                                                                                                                                                                        | Values forMetadata Bits                                                                                         | Description                                                            |
|----------------------------|-------------------------------------|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| wall_block_type            | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8` | `cobblestone` | `cobblestone`<br/>`mossy_cobblestone`<br/>`granite`<br/>`diorite`<br/>`andesite`<br/>`sandstone`<br/>`brick`<br/>`stone_brick`<br/>`mossy_stone_brick`<br/>`nether_brick`<br/>`end_brick`<br/>`prismarine`<br/>`red_sandstone`<br/>`red_nether_brick` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13` | The type of wall; for example,`stone_brick`denotes a stone brick wall. |
| wall_connection_type_east  | Not Supported                       | `none`        | `none`<br/>`short`<br/>`tall`                                                                                                                                                                                                                         | `Unsupported`                                                                                                   | How the wall extends from the center post to the east.                 |
| wall_connection_type_north | Not Supported                       | `none`        | `none`<br/>`short`<br/>`tall`                                                                                                                                                                                                                         | `Unsupported`                                                                                                   | How the wall extends from the center post to the north.                |
| wall_connection_type_south | Not Supported                       | `none`        | `none`<br/>`short`<br/>`tall`                                                                                                                                                                                                                         | `Unsupported`                                                                                                   | How the wall extends from the center post to the south.                |
| wall_connection_type_west  | Not Supported                       | `none`        | `none`<br/>`short`<br/>`tall`                                                                                                                                                                                                                         | `Unsupported`                                                                                                   | How the wall extends from the center post to the west.                 |
| wall_post_bit              | Not Supported                       | `true`        | `false`<br/>`true`                                                                                                                                                                                                                                    | `Unsupported`                                                                                                   | Whether or not the wall has a center post.                             |

Blackstone and deepslate wall:

| Name                       | Metadata Bits | Default value | Allowed values                | Values forMetadata Bits | Description                                             |
|----------------------------|---------------|---------------|-------------------------------|-------------------------|---------------------------------------------------------|
| wall_connection_type_east  | Not Supported | `none`        | `none`<br/>`short`<br/>`tall` | `Unsupported`           | How the wall extends from the center post to the east.  |
| wall_connection_type_north | Not Supported | `none`        | `none`<br/>`short`<br/>`tall` | `Unsupported`           | How the wall extends from the center post to the north. |
| wall_connection_type_south | Not Supported | `none`        | `none`<br/>`short`<br/>`tall` | `Unsupported`           | How the wall extends from the center post to the south. |
| wall_connection_type_west  | Not Supported | `none`        | `none`<br/>`short`<br/>`tall` | `Unsupported`           | How the wall extends from the center post to the west.  |
| wall_post_bit              | Not Supported | `true`        | `false`<br/>`true`            | `Unsupported`           | Whether or not the wall has a center post.              |

