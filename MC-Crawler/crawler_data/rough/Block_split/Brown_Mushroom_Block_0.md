# Mushroom Block
A mushroom block is a solid block that makes up a huge mushroom, which consists of a mushroom stem and brown mushroom blocks or red mushroom blocks, depending on the color of the huge mushroom.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Creative inventory
- 2 Usage
	- 2.1 Composting
	- 2.2 Note Blocks
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Gallery
	- 6.1 Renders
		- 6.1.1 Mushroom
		- 6.1.2 Brown Mushroom
		- 6.1.3 Red Mushroom
		- 6.1.4 Mushroom Stem
- 7 References
- 8 External links

## Obtaining
### Breaking
Mushroom blocks are most quickly broken with an axe, with a chance of 77.77% of dropping 0 and respectively a chance of 11.11% to drop 1 or 2 mushroom items of the respective type. In Java Edition, only cap blocks drop mushroom items, while in Bedrock Edition stem blocks drop mushrooms as well. Fortune does not affect the drop rate of mushrooms in any form.[1]

The blocks themselves can be retrieved only by using a tool enchanted with Silk Touch. Mining the mushroom cap or stem yields a block with the cap or stem texture, respectively, on all faces.

Additionally, in Java Edition, if two similar mushroom blocks are placed next to each other and one of them is broken, the side of the other block that it was facing reveals the pore texture. This is because the side of these blocks change texture if they touch another block of the same type.

Mushroom blocks can be moved and are not broken by pistons.

| Block     | Mushroom Block        |
|-----------|-----------------------|
| Hardness  | 0.2                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 0.3                   |
| Wooden    | 0.15                  |
| Stone     | 0.1                   |
| Iron      | 0.05                  |
| Diamond   | 0.05                  |
| Netherite | 0.05                  |
| Golden    | 0.05                  |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Natural generation
Main article: Huge mushroom
Mushroom blocks generate as part of huge mushroom structures.


### Creative inventory
In Java Edition, the brown and red mushroom blocks as well as the mushroom stem are available in the Creative inventory.

In Bedrock Edition, all-sided cap blocks, all-sided stem block (with id of "brown_mushroom_block"), and all-sided pore block (with id of "brown_mushroom_block") are available in the Creative inventory.

## Usage
### Composting
Mushroom blocks can be used in the composter with an 85% chance to make a new layer.

Mushroom stems can be used in the composter with a 65%‌[JE  only] / 85%‌[BE  only] chance to make a new layer.

### Note Blocks
Mushroom blocks can be placed under note blocks to produce "bass" sound.

## Data values
### ID
Java Edition:

In Java Edition, there are 3 kinds of mushroom blocks: Red Mushroom Block, Brown Mushroom Block and Mushroom Stem, which have different IDs.

| Name                 | Identifier             | Form         | Translation key                        |
|----------------------|------------------------|--------------|----------------------------------------|
| Brown Mushroom Block | `brown_mushroom_block` | Block & Item | `block.minecraft.brown_mushroom_block` |
| Red Mushroom Block   | `red_mushroom_block`   | Block & Item | `block.minecraft.red_mushroom_block`   |
| Mushroom Stem        | `mushroom_stem`        | Block & Item | `block.minecraft.mushroom_stem`        |

Bedrock Edition:

In Bedrock Edition there are 4 kinds of mushroom blocks: Brown Mushroom Block, Mushroom Stem, Mushroom and Red Mushroom Block, encoded as block states of 2 block IDs, brown_mushroom_block and red_mushroom_block. For brown_mushroom_block the huge_mushroom_bits metadata value of the block state determine the block name: Brown Mushroom Block for 14, Mushroom Stem for 15, and Mushroom for all others. For red_mushroom_block all blocks are named Red Mushroom Block.

Metadata values 1–10 of both IDs are used to build Huge Mushrooms of the corresponding color (1–9 for the cap and 10 for the stem). Values 0 and 11–15 are not used for this purpose. Value 14 is a block with the cap texture on all faces; it differs from values 1–9 in that the latter only have cap textures on certain faces, with pore textures on the rest. Value 15 is a block with the stem texture on all faces; it differs from value 10 in that the latter has pore textures on the top and bottom faces. Value 14 represents the block dropped when a block in the cap of a Huge Mushroom of the corresponding color is mined with a Silk Touch tool. Value 15 represents the block dropped when a block in the stem of a Huge Mushroom is mined with a Silk Touch tool (the brown stem block is dropped even for a huge red mushroom).

| Name                 | Identifier             | Numeric ID | Form                       | Item ID[i 1]   | Translation key                                                                                |
|----------------------|------------------------|------------|----------------------------|----------------|------------------------------------------------------------------------------------------------|
| Brown Mushroom Block | `brown_mushroom_block` | `14`       | Block & Giveable Item[i 2] | Identical[i 3] | `brown_mushroom_block.mushroom`<br/>`brown_mushroom_block.cap`<br/>`brown_mushroom_block.stem` |
| Red Mushroom Block   | `red_mushroom_block`   | `14`       | Block & Giveable Item[i 2] | Identical[i 3] | `tile.red_mushroom_block.name`                                                                 |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑ a bAvailable with /give command.
3. ↑ a bThe block's direct item form has the same id as the block.

