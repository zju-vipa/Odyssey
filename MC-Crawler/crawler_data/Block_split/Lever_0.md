# Lever
A lever is a non-solid block that can be switched to provide redstone power.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
- 2 Usage
	- 2.1 Placement
	- 2.2 Activation
	- 2.3 Behavior
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 Video
- 6 History
- 7 Issues
- 8 References
- 9 External links

## Obtaining
### Breaking
A lever can be mined using any tool, or without a tool, and always drops itself as an item.

| Block    | Lever               |
|----------|---------------------|
| Hardness | 0.5                 |
|          | Breakingtime (secs) |
| Default  | 0.75                |

A lever is also removed and drops as an item if:

- its attachment block is moved, removed, or destroyed
- waterorlavaflows into its space, inJava Edition
- apistontries to push it or moves a block into its space

### Natural generation
Three levers are generated naturally in each jungle temple. They also generate in woodland mansions and ancient cities.


### Crafting
| Ingredients       | Crafting recipe |
|-------------------|-----------------|
| Stick+Cobblestone |                 |

## Usage
Five of the eight possible orientations, levers off.
See also: Redstone circuits

A lever can be used as a player-switchable redstone power source.

### Placement
A lever can be attached to the top, side, or bottom of any full solid opaque block (stone, dirt, blocks of gold, etc.), or to the top of an upside-down slab or upside-down stairs (but not to the bottom of a right-side-up slab or stairs). When placed on the top or bottom of a block, the lever orients itself in-line with the placing player.

In Bedrock Edition, it can additionally be placed on the top of a fence, stone wall or hopper, and can be placed underwater.

When placed on the side of blocks, down is on and up is off. On the top or bottom of blocks, off is north or west, on is south or east.

### Activation
To activate or deactivate a lever, use the "Use Item/Place Block" control (right-click, by default). A lever can be turned on and off as fast as it can be clicked.

Mobs cannot turn a lever on or off.

### Behavior
While active, a lever:

- powers any adjacentredstone dust(including beneath the lever) topower level15
- powers any adjacentredstone comparatororredstone repeaterfacing away from the lever to power level 15
- strongly powers its attachment block to power level 15 (only if the attachment block is a full solid opaque block)
- activates any adjacentmechanism components, including above or below, such aspistons,redstone lamps, etc.
- emits redstone particles to indicate that it is active (inJava Edition).

## Data values
### ID
Java Edition:

| Name  | Identifier | Form         | Translation key       |
|-------|------------|--------------|-----------------------|
| Lever | lever      | Block & Item | block.minecraft.lever |

Bedrock Edition:

| Name  | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key |
|-------|------------|------------|----------------------------|----------------|-----------------|
| Lever | lever      | 69         | Block & Giveable Item[i 2] | Identical[i 3] | tile.lever.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


### Block states
See also: Block states

Java Edition:

| Name    | Default value | Allowed values     | Description                                                                                                                      |
|---------|---------------|--------------------|----------------------------------------------------------------------------------------------------------------------------------|
| face    | wall          | ceilingfloorwall   | The face of the block the lever placed on.Floor is on top of a block, ceiling is on the bottom, and wall is on one of its sides. |
| facing  | north         | eastnorthsouthwest | The direction the lever is facing.Opposite to the direction the player is facing if placed on the side of a block.               |
| powered | false         | falsetrue          | If true, the lever is currently activated.                                                                                       |

Bedrock Edition:

| Name            | Metadata Bits | Default value  | Allowed values   | Values forMetadata Bits | Description                                  |
|-----------------|---------------|----------------|------------------|-------------------------|----------------------------------------------|
| open_bit        | 0x8           | false          | falsetrue        | 01                      | If the lever is currently activated.         |
| lever_direction | 0x10x20x4     | down_east_west | down_east_west   | 0                       | Lever on block bottom points east when off   |
|                 |               |                | east             | 1                       | Lever on block side facing east              |
|                 |               |                | west             | 2                       | Lever on block side facing west              |
|                 |               |                | south            | 3                       | Lever on block side facing south             |
|                 |               |                | north            | 4                       | Lever on block side facing north             |
|                 |               |                | up_north_south   | 5                       | Lever on block top points south when off.    |
|                 |               |                | up_east_west     | 6                       | Lever on block top points east when off.     |
|                 |               |                | down_north_south | 7                       | Lever on block bottom points south when off. |




