# Honey Block
Honey blocks are storage blocks equivalent to four honey bottles. Honey blocks are sticky and can be used in conjunction with pistons to move blocks and adhered entities.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Crafting
- 2 Usage
	- 2.1 Redstone
	- 2.2 Slowing down entities
	- 2.3 Sliding
	- 2.4 Falling
	- 2.5 Bees
	- 2.6 Crafting ingredient
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
- 5 Achievements
- 6 Advancements
- 7 History
- 8 Issues
- 9 Trivia
- 10 Gallery
	- 10.1 Screenshots
	- 10.2 Development images
- 11 Notes
- 12 References
- 13 External links

## Obtaining
### Breaking
Honey blocks can be broken instantly, and always drop as an item, regardless of held items.

| Block    | Honey Block         |
|----------|---------------------|
| Hardness | 0                   |
|          | Breakingtime (secs) |
| Default  | 0.05                |

### Crafting
| Ingredients  | Crafting recipe | Description                                                           |
|--------------|-----------------|-----------------------------------------------------------------------|
| Honey Bottle |                 | Emptybottlesremain in the crafting grid aftercraftingthe honey block. |

The 2×2 inventory crafting grid is sufficient to craft a honey block.

## Usage
### Redstone
Unlike the slime block, the honey block does not carry a redstone signal because it is a transparent block.‌[Java Edition  only]

When being moved by a piston, entities on a honey block's top surface move with it. They are not launched in the direction of the push, as a slime block would do.

When a honey block is moved by a piston, it attempts to move all adjacent blocks in the same direction. A honey block can move any block a sticky piston can pull, except for glazed terracotta and slime blocks. The blocks that are moved may, in turn, push other blocks, as if they were being pushed by a piston. For example, a honey block sitting on the ground attempts to move the ground block underneath itself, which pushes additional ground blocks in the direction of motion.

When the adjacent block that is moved is also a honey block, that block also attempts to move all its adjacent blocks. For example, a 2×2×2 cube of honey blocks may be pushed or pulled as a unit by a single piston acting on any of the blocks in the cube.

A honey block adjacent to a block that cannot be moved by pistons ignores the immobile block. However, if an adjacent block could be moved but is prevented by the presence of an immobile block, the honey block is also prevented from moving. Liquids are an exception: they are not moved, but neither do they stop a piston from pushing or pulling blocks into their space (usually destroying the liquid, and in a rare case displacing it through the piston). Honey blocks, unlike slime blocks, cannot have a redstone signal sent through them via a repeater or an observer, etc.

Honey blocks are not pulled by a non-sticky piston, nor are they moved if an adjacent (non-honey) block is moved by a piston.

The maximum of 12 blocks moved by a piston still applies. For example, a 2×2×3 of honey blocks may be pushed or pulled by a sticky piston as long as no other movable blocks are adjacent to it. However, the platform in which a honey block shifts is entirely dependent on the placement of the sticky piston, as well as placement of blocks too.

In Java Edition honey blocks moved by pistons do not move entities that are touching the side or bottom of the block.[1]
In Bedrock Edition honey blocks moved by pistons do move entities that are touching the side of the block.[more information needed for Bedrock Edition]

