# Slime Block
A slime block is a storage block equivalent to nine slimeballs. It has both sticky and bouncy properties making it useful in conjunction with pistons to move both blocks and entities.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Crafting
- 2 Usage
	- 2.1 Bouncing
	- 2.2 Pistons
	- 2.3 Crafting ingredient
	- 2.4 Brewing ingredient
- 3 Sounds
- 4 Data values
	- 4.1 ID
- 5 Achievements
- 6 History
- 7 Issues
- 8 Trivia
- 9 Gallery
	- 9.1 Screenshots
	- 9.2 In other media
- 10 Notes
- 11 References
- 12 External links

## Obtaining
### Breaking
Slime blocks can be broken instantly, regardless of held items, or when under the Mining Fatigue effect.

| Block    | Slime Block         |
|----------|---------------------|
| Hardness | 0                   |
|          | Breakingtime (secs) |
| Default  | 0.05                |

### Crafting
| Ingredients | Crafting recipe |
|-------------|-----------------|
| Slimeball   |                 |

## Usage
Landing on a slime block does not cause fall damage unless the player is sneaking.

Slime blocks are also slightly slippery, but less so than ice.

Slime blocks cause movement on top of them to slow down.

### Bouncing
A player or mob that falls onto the top of a slime block bounces to a height proportional to the falling velocity. The bounce height quickly deteriorates. For example, a fall of 255 blocks produces a bounce height of about 50 blocks, while a fall of 50 blocks results in a bounce height of 22 blocks. The maximum bounce height is 57.625 blocks. Entities hitting the side of a slime block do not bounce, unless the slime block is moving using a piston.

A player holding the jump key performs a normal jump on contact with the slime block without taking fall damage. A player holding sneak does not bounce at all and takes fall damage.

Placing carpets, rails, trapdoors, redstone repeaters or redstone comparators on a slime block does not stop mobs from bouncing and not taking fall damage. Likewise, placing a pressure plate on a slime block does not stop mobs from bouncing, but the pressure plate still activates. Half-blocks such as cakes and slabs stop the bouncing effect.

Most mobs bounce off slime blocks. Exceptions are chickens, ghasts, bats, phantoms, bees, parrots, and vexes. Occasionally a horse may get stuck on a block when a player tries to spawn it on top of a slime block in Creative mode.

Items, falling blocks, minecarts and boats do not bounce on slime blocks. Particles, however, do bounce. Players can also get around the fact that falling blocks, minecarts, and boats don't bounce by having sticky pistons with slime blocks bounce them.

### Pistons



A







B





















Piston A can extend because the slime block ignores the adjacent obsidian. Piston B cannot extend because the diamond block is prevented from moving by the obsidian and so the slime block also refuses to move.
A self-propelled aircraft engine. Place the top block of redstone and sticky piston last.
When being pushed by a piston, entities (except ender dragons, item frames and paintings) that are ahead are launched into the direction the block is pushed into. When pulled by a piston, no entities are launched.

When a slime block is pushed or pulled by a piston, it attempts to move all adjacent blocks in the same direction. The types of blocks that can be moved are the same as those that can be pulled by a sticky piston. Blocks that cannot be pulled by a sticky piston (i.e. all the blocks listed on the table on the pistons page) stay in place. The blocks that are moved may in turn push other blocks. For example, a slime block sitting on the ground attempts to move the ground block underneath itself, which pushes additional ground blocks in the direction of motion just as if it were being pushed directly by a piston.

Blocks such as glazed terracotta and honey blocks are exceptions; they do not move when adjacent slime blocks are moved, even if they are normally pushable by a piston.

When the adjacent block that is moved is also a slime block, that block attempts to move all its adjacent blocks. For example, a 2×2×2 cube of slime blocks may be pushed or pulled as a unit by a single piston acting on any of the blocks in the cube and attempts to move all blocks adjacent to the cube.

A slime block adjacent to a block that cannot be moved by pistons ignores the immobile block. However, if an adjacent block could be moved but is prevented by the presence of an immobile block, the slime block is also prevented from moving. This includes slime blocks being pulled rather than pushed, in which case the piston retracts without pulling anything. Liquids are an exception: they aren't moved, but neither do they stop a piston from pushing or pulling blocks into their space (usually destroying the liquid, and in a rare case displacing it through the piston).

Slime blocks are not pulled by a non-sticky piston, nor are they moved if an adjacent (non-slime) block is moved by a piston.

The maximum of 12 blocks moved by a piston still applies. For example, a 2×2×3 of slime blocks may be pushed or pulled by a sticky piston as long as no other movable blocks are adjacent to it.

A piston cannot move itself via a "loop" constructed of slime blocks, but self-propelled contraptions can be created with multiple pistons.

### Crafting ingredient
| Name      | Ingredients | Crafting recipe |
|-----------|-------------|-----------------|
| Slimeball | Slime Block | 9               |

### Brewing ingredient
| Name             | Ingredients                     | Brewing recipe |
|------------------|---------------------------------|----------------|
| Potion of Oozing | Slime Block+<br/>Awkward Potion |                |

## Data values
### ID
Java Edition:

| Name        | Identifier    | Form         | Translation key               |
|-------------|---------------|--------------|-------------------------------|
| Slime Block | `slime_block` | Block & Item | `block.minecraft.slime_block` |

Bedrock Edition:

| Name        | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key   |
|-------------|------------|------------|----------------------------|----------------|-------------------|
| Slime Block | `slime`    | `165`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.slime.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

## Notes
1. ↑Like leaves, this block diffuses sky light only from directly above.

