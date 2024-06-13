# Floatater
A floatater is a block added in 24w14potato used to move large amounts of blocks.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Crafting
- 2 Usage
	- 2.1 Floating
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 Gallery
	- 7.1 Renders

## Obtaining
### Breaking
A floatater drops itself only when mined with a pickaxe; otherwise, it drops nothing.

| Block     | Floatater             |
|-----------|-----------------------|
| Hardness  | 0.5                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 2.5                   |
| Wooden    | 0.4                   |
| Stone     | 0.2                   |
| Iron      | 0.15                  |
| Diamond   | 0.1                   |
| Netherite | 0.1                   |
| Golden    | 0.1                   |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Crafting
| Ingredients                                    | Crafting recipe |
|------------------------------------------------|-----------------|
| Poisonous Potato+<br/>Floatato+<br/>Hot potato |                 |

## Usage
1 gametick after receiving a redstone signal, the floatater pushes all blocks connected via its sticky side. It does not check redstone signals when placed by a player.

### Floating
Unlike pistons, it does not have a standard max-number of pushable blocks, but rather a distance limit of 30 blocks (cubic range rather than spherical). If the stickied blocks are connected to a block that is 31 or more blocks from the floatater, the structure does not move. This means the maximum number of blocks moveable by the Floatater is 32,768 (including itself), as long as its built in a 32×32×32 cube with the Floatater itself at any place inside that area. Stop the structure by "grounding" it, or connecting it to a large enough amount of blocks. 

A block is pushed if it is in front of another block being pushed by the floatater. A block is also considered connected if its interaction box is touching that of a block being pushed, NOT the floatater itself unless it's on the sticky side. A slime or honey block is always connected with its adjacent blocks, including air, fluids and the floatater regardless of its direction. A not sticky piston and its head are not connected. Floataters can move blocks normally broken by piston pushing or cannot be moved, i.e., melons and redstone dust not inclusive of tile entities such as shulker boxes and comparators, which break off when pushed.

A floatater creates a "super extra magic" entity (minecraft:grid_carrier) storing moved blocks when starting to float. Tile entities placed as a part of the floatater structure breaks off when the floatater begins moving, even if not pushed by anything, and blocks connected to them are still moved. Waterlogged blocks are pushed without water.

Moved blocks are deleted after the "super extra magic" is created. Fluids are not deleted. When waterlogged blocks are deleted, water is kept. Deletion of tripwire may be rolled back if its hook is notified to update the attached state of the tripwire. Blocks in a floatater structure are stored in order, but the order in which moved blocks are deleted depends on location. This process sends neighbor changed updates and no post placement updates. Updates from a block deleted earlier can cause redstone wire, redstone repeaters, powered rails, detector rails, activator rails, and pistons attached to it that have been stored in the "super extra magic" and should be deleted later to drop.

When multiple floatater blocks are connected together, and all are powered simultaneously, the floatater moves faster.

It can transport redstone contraptions, including extended pistons, but freezes all redstone activity until it comes to a stop.

A floatater structure floats until one of the blocks at the front of the floatater structure collides with another block that cannot be replaced. The floatater structure replaces existing blocks and can be rolled back by tripwire notifying its hook to update its attached state.

## Data values
### ID
| Name      | Identifier  | Translation key             |
|-----------|-------------|-----------------------------|
| Floatater | `floatater` | `block.minecraft.floatater` |

### Block states
See also: Block states

| Name      | Default value | Allowed values                            | Description                             |
|-----------|---------------|-------------------------------------------|-----------------------------------------|
| facing    | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction this floatater is facing. |
| triggered | `false`       | `false`<br/>`true`                        | True if this block is activated.        |


