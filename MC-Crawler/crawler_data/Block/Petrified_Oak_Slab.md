# Petrified Oak Slab
A petrified oak slab, known as a wooden slab (formerly fake wood slab) in Bedrock Edition, is a unique type of slab available through commands or by upgrading from legacy versions. Unlike all other slabs, they are unobtainable in vanilla Survival gameplay.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Crafting
	- 1.3 Upgrading
- 2 Usage
	- 2.1 Differences from normal slabs
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
	- 5.1 Appearance changes
		- 5.1.1 Block
		- 5.1.2 Item
	- 5.2 Info pertaining to all slabs
	- 5.3 Data history
- 6 Issues
- 7 Gallery

## Obtaining
Petrified oak slabs are unobtainable in new Survival worlds. They can be obtained only by using commands such as /give or placed in the world using commands such as /setblock.

### Breaking
Petrified oak slabs require a pickaxe to mine. When broken, they drop themselves in Java Edition or regular oak slabs in Bedrock Edition.

| Block     | Petrified Oak Slab    |
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


### Crafting
Petrified oak slabs are uncraftable in current versions without the use of a data pack or behavior pack.

### Upgrading
Petrified oak slabs are obtainable and craftable as one would expect in versions released before Java Edition 1.3.1 (snapshot 12w17a) or  Pocket Edition v0.7.3 alpha, in which they are the only wooden slab type.

## Usage
Main article: Slab § Usage
Petrified oak slabs are functionally like other slabs and share most of their placement, collision, and other block behaviors with them. They date back to the earliest releases when there was only one kind of wooden slab, which had the texture of oak planks but was implemented as a variant of the generic slab, all other variants of which were made of stone. It therefore had stone properties as well.

When other species of planks were introduced, true wooden slabs were added to the game with variants for each species and properties more appropriate for wood. From then on, all wooden slabs that were crafted or generated in structures were of the real wood type, but the stone variants can still exist in older worlds. These stonelike "wooden" slabs are noteworthy for how their behavior differs from what their name and appearance imply.

### Differences from normal slabs
Unlike other wooden slabs:

- Petrified oak slabs make the sounds characteristic ofstone.
- They require a pickaxe tomine. If broken without a pickaxe, they drop nothing.
- They are notflammable, nor are they set on fire by nearbylava.
- They cannot be used as fuel in afurnace.
- They have a greater blast resistance.
- Note blocksplaced on top produce bass drum sounds, similarly to other stone-like blocks.

Unlike other slabs in general:

- They cannot be crafted or obtained normally in Survival.
- They do not have a direct full-block equivalent.
- InBedrock Editionthey do not drop themselves, but rather drop anoak slab.

## Data values
### ID
Java Edition:

| Name               | Identifier         | Form         | Block tags            | Item tags | Translation key                    |
|--------------------|--------------------|--------------|-----------------------|-----------|------------------------------------|
| Petrified Oak Slab | petrified_oak_slab | Block & Item | slabsmineable/pickaxe | slabs     | block.minecraft.petrified_oak_slab |

Bedrock Edition:

| Name               | Identifier              | Alias ID          | Numeric ID | Form                         | Item ID[i 1]                                           | Translation key                  |
|--------------------|-------------------------|-------------------|------------|------------------------------|--------------------------------------------------------|----------------------------------|
| Double Wooden Slab | double_stone_block_slab | double_stone_slab | 43         | Block & Ungiveable Item[i 2] | double_stone_block_slabAlias ID:real_double_stone_slab | tile.double_stone_slab.wood.name |
| Wooden Slab        | stone_block_slab / 2    | stone_slab / 2    | 44         | Block & Giveable Item[i 3]   | stone_block_slabAlias ID:double_stone_slab             | tile.stone_slab.wood.name        |


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



