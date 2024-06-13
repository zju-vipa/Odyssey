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

### Slowing down entities
Honey blocks slow down entities walking on top of them and prevent them from jumping. Players walking on honey blocks move 2.508 m/s, about a 60% reduction from the normal walking speed. In Bedrock Edition, players also slow down slightly if walking up against the side of it. Players, who can ordinarily jump about 1 1⁄4 blocks high, can jump about 3⁄16 blocks high on honey; this is an 85% reduction. They can more easily step up onto other blocks than jump up onto them.

This effect applies even through other blocks on top of honey blocks as long as they are half-block or less in height - so the player cannot jump on carpets, bottom slabs or daylight detectors that are placed on honey blocks.

This effect also applies regardless of a player's mode of movement, such as flying with elytra or swimming.

### Sliding
Entities pressed against the sides of a honey block slide down at a slow speed and do not take fall damage, similar to going down a ladder but with a gradually decreasing horizontal momentum.‌[Java Edition  only] This allows players to jump 2 blocks further by holding on to the walls. The slowdown induced by honey blocks also stacks with the Slow Falling status effect.

### Falling
As with hay bales, falling onto a honey block reduces fall damage by 80%. For example, if a player or mob falls from a height that would normally cause 10 fall damage, the fall causes 2 damage instead.

### Bees
When a honey block is near bees and a beehive or bee nest, bees occasionally fly close and attach to it for a few seconds, resembling an action of eating honey. When doing this, the bee stops fluttering its wings, and firmly attaches its face to the honey block regardless of whether flowers are nearby.

### Crafting ingredient
Although the 2×2 inventory crafting grid is sufficient to craft a honey block, a 3×3 crafting table grid is required to convert a honey block back into four honey bottles.

| Name         | Ingredients                   | Crafting recipe |
|--------------|-------------------------------|-----------------|
| Honey Bottle | Glass Bottle+<br/>Honey Block | 4               |

## Data values
### ID
Java Edition:

| Name        | Identifier    | Form         | Translation key               |
|-------------|---------------|--------------|-------------------------------|
| Honey Block | `honey_block` | Block & Item | `block.minecraft.honey_block` |

Bedrock Edition:

| Name        | Identifier    | Numeric ID | Form                       | Item ID[i 1]   | Translation key         |
|-------------|---------------|------------|----------------------------|----------------|-------------------------|
| Honey Block | `honey_block` | `473`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.honey_block.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

## Notes
1. ↑Like leaves, this block diffuses sky light only from directly above.

