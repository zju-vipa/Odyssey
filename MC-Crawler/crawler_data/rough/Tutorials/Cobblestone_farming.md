# Tutorials/Cobblestone farming
Cobblestone farming is the technique of using a cobblestone generator to produce cobblestone without damaging the terrain. Cobblestone generators work on the principle that when a lava stream comes into contact with water, the lava is turned into cobblestone. This fresh cobblestone then prevents the two streams from touching. When this fresh cobblestone is removed, the two fluids produce another piece of cobblestone. Variants of the generator can also produce stone, but this is generally trickier, because for stone, the lava must enter the water from above.

Many generator designs exist, but the simplest way is to make a five block long trench with a one block gap in the middle. Then, place water in it at the end closest to the hole and lava at the other end. This creates cobblestone where the fluids meet.  

When producing cobblestone, one must be careful not to let the flowing water touch the lava source block. Doing so destroys the lava source, converting it into obsidian. A basic understanding of fluids is helpful to prevent this.  If you place a stair into the water source (flat side to the lava), this prevents the water from flowing over the lava source, but the cobblestone still forms where flowing lava touches the waterlogged block.  Placing a non-flammable block over the lava helps prevent the cobblestone item from being destroyed by the lava when you mine it, as well as keep you from falling into it.

Adding pistons can let a generator extrude a whole line of blocks, safely away from the lava and easily mined as a batch.  Subtle variations of these designs can produce "plain" stone as described below.  The pistons and other arrangements for these generators can also be repurposed for a basalt generator.  Basalt generators don't need the water streams at all, just the lava, blue ice, and soul soil.  Note: soul soil is needed, not soul sand.  You can convert soul sand to soul soil by making and breaking soul campfires.

## Contents
- 1 Reasons to build
- 2 Pistonless generators
	- 2.1 Basic generators
	- 2.2 Fountain generator
	- 2.3 From below generator
- 3 Piston generators
	- 3.1 Components of a piston generator
	- 3.2 Basic piston generators
	- 3.3 Quad-piston generators
- 4 Stone generation
	- 4.1 More video examples
	- 4.2 AFK stone farm
	- 4.3 Semi-automatic stone generator
- 5 Videos

## Reasons to build
While the popularity of building any form of cobblestone generator varies, there are many reasons why a player should build a cobblestone generator. Here are a few.

- Obtaining cobblestone without changing the environment.
- Need for a massive quantity of cobblestone.
- Self-repairing objects, e.g. walls, floors, pillars.
- On a map without stone, e.g. superflat.
- To obtainexperiencethrough smelting.
- To trade stone with Mason villagers.

## Pistonless generators
Pistonless generators have been around for quite a while. However, Their usefulness is limited because cobblestone is so readily available. These generators require the player to mine and collect the fresh cobblestone in close proximity with lava. This both presents risks to the player and reduces efficiency if the dropped cobblestone is destroyed by the lava. These drawbacks can be mitigated by design choices, for example by removing the block under the cobblestone, allowing the loot to fall in a safe place, or collecting drops using a hopper.

Notes about the schematics here: Gold blocks indicate any fireproof block. Water and lava source blocks may be marked with "s" when there is possible confusion. Cobblestone or normal stone appear only where they form. An "x" indicates a place to stand while mining the cobblestone.

### Basic generators
A lava stream touching a water stream is the simplest type of generator. In a 10-block long trench with sources at either end, the cobblestone forms next to the lava. With a little more digging, you can manage this more compactly, and even get a current to wash the mined cobblestone away from the lava. This and the next design are easily expandable for multiplayer use. 

| YouTube Video (view on YouTube) |
|---------------------------------|
|                                 |

| YouTube Video (view on YouTube) |
|---------------------------------|
|                                 |

[Schematic Help]

Schematics for Basic CSGs View at: Tutorials/Cobblestone farming/Basic CSGs [edit]
### Fountain generator
A fountain-style generator offers more convenient mining, but takes more work to construct than the basic version. This one also uses two lava streams for faster production.

| YouTube Video (view on YouTube) |
|---------------------------------|
|                                 |

Schematics for Fountain CSG View at: Tutorials/Cobblestone farming/Basic Fountain CSG [edit]
### From below generator
The "From Below" generator is a small building with the generator on the roof. Putting the generator on the roof means very little cobblestone is lost to the lava, but it is a lot more work. This one also uses two lava streams. 

Schematics for "From Below" CSG View at: Tutorials/Cobblestone farming/From Below CSG [edit]
## Piston generators
Pistons can be used to automate cobblestone generation and reduce the amount of cobblestone lost. Piston cobblestone generators work on the same principle as standard generators, but rather than mining, a piston pushes the fresh stone out of the way, allowing the streams to touch once again. Piston cobblestone generators can be used both to create a large supply of cobblestone that the player can mine later, or to supply a self-repairing structure with blocks. The piston can be driven by a clock, or by a circuit to detect when a cobblestone block has appeared. The cobblestone extends in a long line or pillar; if you don't want it to extend out to the full 12 blocks, you can "cap" it with any unpushable block. Furnaces work well, and you have plenty of cobblestone handy to make them.

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

### More video examples
- A basic stone generator that can be expanded to have multiple outlets, for multiplayer use.

| YouTube Video (view on YouTube) |
|---------------------------------|
|                                 |

- A design that prevents the water source block from turning into cobblestone, a common issue with stone generators.

| YouTube Video (view on YouTube) |
|---------------------------------|
|                                 |

- A small and reliable stone generator that can be turned on and off by switch.

| YouTube Video (view on YouTube) |
|---------------------------------|
|                                 |

- A fast, small and compact that using 4×4 blocks only.

| YouTube Video (view on YouTube) |
|---------------------------------|
|                                 |

Fastest Largest Continuous Mining Stone Generator

| YouTube Video (view on YouTube) |
|---------------------------------|
|                                 |

### AFK stone farm
AFK design which allows you to put something heavy on your mouse and go away from your keyboard. After your pickaxe breaks, a new one is dispensed.

Redstone is not required in the short version. Hoppers can be mostly replaced with water transport. The water source is protected as it comes from a waterlogged block.




| YouTube Video (view on YouTube) |
|---------------------------------|
|                                 |

### Semi-automatic stone generator
This creates 24 blocks of stone at the press of a button. And because it runs by lava flowing over water, (not the other way around) you do not need to worry about the lava source block becoming obsidian.

Start by creating the structure where the stone is formed.

1. Find a place to build your farm. It should have a part that is exactly 4 blocks high and has at least 4 blocks of space in either direction.
2. In your chosen 4-block area, place adispenserfacing down on the ceiling.
3. On the floor below the dispenser, place two blocks on top of each other. The block to use depends on the type of pickaxe you plan to use.
	- If you plan to use an iron or diamond pickaxe, the blocks should be obsidian. Otherwise, you can also use an ore besides coal or nether quartz, or you can use a mineral block besides coal, quartz, or redstone.Iron oreandgold orecan be obtained without the silk touchenchantment.
	- If you plan to use a stone pickaxe, exclude iron ore,lapis lazuli ore,blocks of iron, orblocks of lapis lazuli.
4. Placefenceornether brick fence4 blocks away from your 2-block tower. These are the corners.
5. Connect the corners by placing fence or nether brick fence in a diagonal line toward adjacent fence posts.
6. Place water source blocks on the floor (not the two-block tower)
7. Finally, put a lava bucket in the dispenser.

You also need a redstone circuit to make the dispenser place the lava and then retrieve it. To create it, you must be above the future stone farm. The following steps explain how make a repeat circuit.

1. Place a sticky piston facing up.
2. Place an opaque block (The page "opacity" has a list of transparent blocks, which are the blocks you should not use.) on top of the sticky piston (the sticky piston should move the block. See the page "piston" for blocks where the sticky piston do something else if you're not sure).
3. Place someredstone dust. The redstone wire should connect to the dispenser. Connect this wire to a block with a button attached (Make sure this block is not directly above your future stone farm. This way, you can easily press the button outside the stone farm when you want to make stone.)
4. For the block on the sticky piston to transmit the redstone signal, there needs to be arepeaternext to the block facing away.
5. Place redstone dust in front of the repeater and set the repeater to a 4 tick delay.
6. Place a repeater facing away from the redstone dust. This repeater should face a different direction than the previously placed repeater.
7. Repeat steps 5 and 6 until you have 4 repeaters. Make sure that none of the repeaters are facing the same direction. If done correctly, you cannot place redstone in front of the last repeater. It should still be a 4-tick delay, however.
8. Connect the redstone between the last 2 repeaters to another circuit, which leads to the sticky piston. Include 5 repeaters and set 4 of them to a 4-tick delay. Make sure it is disconnected from any other redstone.

Now your stone farm is complete. To make stone, simply press the button.

