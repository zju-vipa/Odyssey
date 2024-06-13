##### Exceptions
- Rails: as long as they remain on top of a solid face of a block in their new position, and that block isn't moving at the same time.
	- An exception is when the rail and block supporting it are on two parallelextendedpistons at which the rail remains attached. InJava Edition, in order for the rail to successfully move without breaking, the piston moving the block must be powered 1 block event after the piston moving the rail. Trying to move both on the same piston usingslime blocksdoes not work, nor does moving them on perpendicular pistons (although the latter temporarilyappearsto work because of the bugMC-75716).
	- Rails re-orient themselves after being pushed, similar to when placed manually.



### Powering pistons
Pistons powered by one line of redstone.
Pistons can be powered in various ways:

- If a redstone wire is in a line shape toward the piston. InJava Edition, the wire does not automatically curve to the piston.
- Pistons can be powered by a powered block directly adjacent to them, whether it is strongly powered or weakly powered.
- Pistons can be powered by aredstone torchdirectly adjacent to them.
- InJava Edition, pistons can be powered by any powered block one block above and to the side, including the "activated space" above it (if a piston, both sticky and normal were to be facing up and ablock of redstoneplaced on its head, it extends when powered, but doesn't retract when the power it receives from the side or back turns off). However, the piston doesn't extend or retract until it receives a block update. This property is calledquasi-connectivityand can be used to make aBUD switch.
- A repeater cannot transfer power through a piston, as pistons are a transparent block.
- An upward-facing piston can't be powered by a block above it, unless it is extended InJava Edition.
- InBedrock Editiona redstone torch attached to a piston turns off whenever the piston is powered. This mechanic is called soft inversion.
- Pistons can also be powered by observers. This can create a clock if the setup is correct.

### Slime blocks and honey blocks



A







B





















Piston A may extend because the slime block ignores the adjacent obsidian. Piston B may not extend because the diamond block is prevented from moving by the obsidian and so the slime block also refuses to move.
When a slime block is pushed or pulled by a piston, while moving, adjacent blocks also move with the slime block, unless a non-piston movable block stops the blocks that are "grabbed" by the slime blocks. These blocks may in turn push other blocks, not just the blocks in the line in front of the piston. For example, a slime block sitting on the ground attempts to move the ground block underneath itself, which in turn has to pushsticky additional ground blocks in the direction of motion just as if it were being pushed directly by a piston.

Glazed terracotta is an exception; it does not move when adjacent slime blocks are moved. The same occurs when a slime block is moved by an adjacent slime block. For example, a 2×2×2 cube of slime blocks may be pushed or pulled as a unit by a single piston acting on any of the blocks in the cube. A slime block adjacent to a block that cannot be moved by pistons ignores the immobile block. But if an adjacent block could be moved but is prevented by the presence of an immobile block, the slime block is prevented from moving.

Slime blocks are not pulled by a non-sticky piston, nor are they moved if an adjacent (non-slime) block is moved by a piston. The maximum of 12 blocks moved by a piston still applies. For example, a 2×2×3 collection of slime blocks may be pushed by a piston as long as no other movable blocks are adjacent to it. A piston cannot move itself via a "hook" constructed of slime blocks, but self-propelled contraptions can be created with multiple pistons. For that, see the article Tutorials/Flying machines. The same happens for the honey block, but it does not stick to slime blocks.

## Technical components
Main article: Piston/Technical components
Pistons have 2 technical blocks that cannot be obtained. These include the piston head and moving piston blocks.

## Data values
### ID
Java Edition:

| Name   | Identifier | Form         | Block tags | Translation key        |
|--------|------------|--------------|------------|------------------------|
| Piston | piston     | Block & Item | None       | block.minecraft.piston |

Bedrock Edition:

| Name   | Identifier | Alias ID | Numeric ID | Form                       | Item ID[i 1]   | Translation key  |
|--------|------------|----------|------------|----------------------------|----------------|------------------|
| Piston | piston     | None     | 33         | Block & Giveable Item[i 2] | Identical[i 3] | tile.piston.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


| Name                | Savegame ID |
|---------------------|-------------|
| Piston block entity | PistonArm   |

