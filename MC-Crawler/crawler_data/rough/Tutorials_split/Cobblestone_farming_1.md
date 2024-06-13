### Components of a piston generator
There are three basic components to consider in a piston cobblestone generator:

- The core. This part includes the water and lava that creates the fresh cobblestone in front of the piston. It's generally based on a basic generator plan, with modifications for the piston and redstone.
- Aclock circuitor block detector, driving a piston. This part generates a signal to drive the piston that pushes fresh cobblestone out. The clock period can be chosen to minimize excessive piston movement.
	- A block detector is simply a circuit from a power source to the piston, passing through redstone repeaters before and after the spot where the cobblestone appears. When the block does appear, the repeaters can push current through it to trigger the piston.
	- A clock generates its signal repeatedly at fixed intervals. Any of the basic repeater clocks suffice, but you want a total period of at least 7 or 8 (that is, a 4-clock or longer).
	- The core piston itself is usually non-sticky, but some block-detector CSG designs have a sticky piston with a transparent (non-conducting) block.



















Smart Piston.Blocks pushed into the "mobile" position are redirected to the right.
- Optional secondary pistons. Since pistons can only push a maximum of 12 blocks, the core produces at most 13 cobblestone blocks at a time. This can be greatly increased with secondary pistons that guide the row of cobblestone in other directions. Like the core piston, the idea is to get the fresh cobblestone out of the way so that more can be created. A line of secondary pistons may also be used to move the blocks directly into self-repairing structures. Secondary pistons can be triggered by the same clock or detection circuit as the core piston, but this can be noisy if there are many of them. Alternatively, they can get their own clock or detection circuit.
	- If nether quartz is available, the "smart piston" circuit shown here automatically redirects a stream of blocks from the side (that is, into or out of the screen) or from below.  It works because the note block triggers a block update any time the block beneath it changes.  The observer detects this and triggers the piston. Because this leaves the space empty, the next block repeats the process. The smart piston stops when its output stream is full or blocked, but once some blocks have been mined, it can be restarted by clicking the note block.



### Basic piston generators
The first design uses a redstone clock drives a piston which pushes out the generated cobblestone from a basic core. The second uses a block-detection circuit, and pushes the cobblestone upward.

| YouTube Video (view on YouTube) |
|---------------------------------|
|                                 |

| YouTube Video (view on YouTube) |
|---------------------------------|
|                                 |

| YouTube Video (view on YouTube) |
|---------------------------------|
|                                 |

Basic Piston Generator Schematics View at: Tutorials/Cobblestone farming/Basic Piston CSG [edit]
### Quad-piston generators
These advanced generator designs consistently produce four cobblestone blocks on every fourth piston cycle. The blocks are pushed upward, negating any chance of the cobblestone burning from touching lava.  

Cobblestone Quad-piston "Factory":

| YouTube Video (view on YouTube) |
|---------------------------------|
|                                 |

| YouTube Video (view on YouTube) |
|---------------------------------|
|                                 |

| YouTube Video (view on YouTube) |
|---------------------------------|
|                                 |

Factory Piston Generator (Version 3) Schematics View at: Tutorials/Cobblestone farming/Factory V3 Piston CSG [edit]
This build can easily be converted to a basalt generator:  

- Make all the pistons sticky.
- Put soul soil atop the pistons, filling everything else up to that level with blocks (corners and center).
- Put the blue ice on the level above, 2 blocks where the water would go.  (You can place any block on the other two corners.)  Finally, put the lava in the middle and cover it over.

Examples of Secondary Piston Usage:

- This one produces streams of cobblestone in two directions for more rapid output.

| YouTube Video (view on YouTube) |
|---------------------------------|
|                                 |

## Stone generation
Lava flowing into water from above creates stone. Stone can be mined slightly faster than cobblestone, and it can also be collected as stone using a pickaxe with the Silk Touch enchantment. Using stone also gives self-repairing structures a different, more natural look.

Stone generators are rarely designed without pistons, as lava needs to be directly above the stone generated. Lava must flow down into flowing water in front of the piston. As with cobblestone generators, a single-piston design can only make a row of stone up to 13 blocks long.

Stone generator examples:

Basic Stone Generator Schematics View at: Tutorials/Cobblestone farming/Basic SSG [edit]

Smooth Stone Generator A can be built in a 4×5×2 hole, with two blocks dug out of the bottom (level 0), and the clock extending two blocks out from one corner.

The upward facing piston is on level 0. The hole east of it contains redstone and is covered by any transparent block (glass shown for visibility). The redstone torch in the main section is temporary; once you've built the clock, place a lever on either input block (green wool), and flip the lever, then replace the torch with redstone dust.  (This lever is turning the clock, and generator, off, so turning the lever on stops the generator.)  After building, flipping the lever again runs the generator, or do a bit of tidying-up: The rest of level 2 can be filled with any block, and you may want to cover the lava (and even the exposed repeater), with a slab.

Variation: Since the clock is already protruding, you might substitute a longer one to cut down on the piston noise. Experiment carefully with the delays, as some clock cycles can stop production entirely. (With this 5-clock, the generator is moving the pistons three times for every block.)
Earliest Known Publication: May 29, 2012,  Minecraft Smooth Stone Generator Tutorial by DJ&Riggaz. 

Smooth Stone Generator B is a clockless build driven by a BUD switch.

- The block marked!is where stone is generated and moves as shown.  A trench beneath the stone path can contain unfortunate lava spills.
- The glass block needs some gravity block atop it: Sand is shown, gravel or even concrete powder also works.
- This build can be mirrored but not rotated:  It works only with the output going east or west, apparently due to asouth-east rule.

Earliest Known Publication: May 1, 2014,  Simplest Automatic Stone Generator - KollinsPlays Minecraft Vanilla Tutorial.  

