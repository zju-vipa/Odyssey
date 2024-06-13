# Redstone circuits
A redstone circuit is a contraption that activates or controls mechanisms. Circuits can act in response to player or entity/mob activation, along with different sound types continuously on a loop, or in response to non-player activity (Mob movement, Item drops, plant growth, etc).  

A useful distinction can be made between a circuit performing operations on signals (generating, modifying, combining, etc.), and a mechanism manipulating the environment (moving blocks, opening doors, changing the light level, producing sound, etc). Making this distinction lets us talk about the various circuits separately, and let players choose whichever circuits are useful for their purposes. The machines controlled by redstone circuits can range from simple devices such as automatic doors and light switches to complex devices such as elevators, automatic farms, or even in-game computers. However, this article provides only an overview of redstone circuits as above. These can be used to control simple mechanisms, or combined as parts of a larger build. Each circuit type on this page has links to its own page, which provides greater detail about them and give schematics for multiple variations of each.

Before working with any but the most basic redstone circuits, an understanding of some basic concepts is required: "power", "signal strength", "redstone ticks", and "block updates". Some relevant articles are listed below:

## Contents
- 1 Describing circuits
	- 1.1 Size
	- 1.2 Features
- 2 Circuit types
	- 2.1 Transmission circuit
	- 2.2 Logic circuit
	- 2.3 Pulse circuit
	- 2.4 Clock circuit
	- 2.5 Memory circuit
	- 2.6 Piston circuits
	- 2.7 Miscellaneous circuits
- 3 Video
- 4 References

## Describing circuits
Most circuits are described using Schematic diagrams; some of these require multiple images to show one or two layers per image. See the Help:Schematic page for details on how various blocks and components are represented.

### Size
The wiki describes circuit size (the volume of the rectangular solid it occupies) with the notation of depth × width × height, including support/floor blocks, but not including inputs/outputs.

Another method used for describing circuit size in the Minecraft community is to ignore non-Redstone blocks simply used for support (for example, blocks under Redstone dust or repeaters). However, this method is unable to distinguish between flat and 1-high circuits, as well as some other circuit differences.

Sometimes it is convenient to compare circuits simply by the area of their footprint (e.g., 3×4 for a circuit three-block wide by four blocks long), or by a single dimension important in a particular context (e.g., length in a sequence of sub-circuits, height in a confined space, etc.).

### Features
Several features may be considered desirable design goals:

** 1-high **
A structure is 1-high (aka "1-tall") if its vertical dimension is one block high (meaning it cannot have any redstone components that require support blocks below them, such as redstone dust or repeaters). Also seeflat.
** 1-wide **
A structure is 1-wide if at least one of its horizontal dimensions is exactly one block wide.
** Flat **
A structure is flat if it generally can be laid out on the ground with no components above another (support blocks under redstone components are okay). Flat structures are often easier for beginners to understand and build, and fit nicely under floors or on top of roofs. Also see1-high.
** Flush **
A structure is flush if it doesn't extend beyond a flat wall, floor, or ceiling and can still provide utility to the other side, though redstone mechanisms may be visible in the wall. Flush is a desirable design goal for piston-extenders, piston doors, etc. Also seehipsterandseamless.
** Hipster **
**  **
A structure is hipster if it is initially hidden behind a flat wall, floor, or ceiling and can still provide utility to the other side. See alsoflushandseamless.
** Instant **
A structure is instant if its output responds immediately to its input (a circuit delay of 0 ticks).
** Seamless **
A structure is seamless if no redstone components are visible both before and after it completes its task (but it's okay if some are visible during operation). Seamless is a desirable design goal for piston-extenders, piston doors, etc. See alsoflushandhipster.
** Silent **
A structure is silent if it makes no noise (such as from piston movement, dispenser/dropper triggering when empty, etc.). Silent structures are desirable for traps or peaceful homes.
** Stackable **
A structure is stackable if it can be placeddirectlyon top of other copies of itself, and they all can be controlled as a single unit. Also seetileable.
** Expandable **
A structure is Expandable if it can be placeddirectlynext to other copies of itself, and they all can be controlled as a single unit. Also seetileable.
** Tileable **
A structure is tileable if it can be placeddirectlynext to or on top of other copies of itself, and each copy can still be controlled independently. Also seestackable.
Structures might be described as "2-wide tileable" (tileable every two spaces in one dimension), or "2×4 tileable" (tileable in two directions), etc. Some structures might be described as "alternating tileable", meaning they can be placed next to each other if every other one is flipped or a slightly different design.
Other design goals may include reducing the delay a sub-circuit adds to a larger circuit, reducing the use of resource-expensive components (redstone, nether quartz, etc.), and re-arranging or redesigning a circuit to make it as small as possible.

Some components are not available before a player has access to the Nether, which limits the designs available. In particular, redstone comparators, observers and daylight detectors require nether quartz, which is available only from the Nether. Additionally, redstone lamps require glowstone, which is occasionally available from trading or witches, but is much more plentiful in the Nether.

## Circuit types
Although the number of ways to construct circuits is endless, certain patterns of construction occur repeatedly. The following sections attempt to categorize the circuits that have proven useful to the Minecraft community, while the main articles describe the specific circuits that fall into those categories.

Some of these circuits might be used by themselves for simple control of mechanisms, but frequently the player needs to combine them into more complex circuits to meet the needs of a mechanism.

### Transmission circuit
Main article: Transmission circuit
Some aspects of signal transmission can be helpful to understand: transmission types, vertical transmission, repeaters, and diodes.

** Vertical transmission **
Transmitting signals upward
Transmitting signals downward
Examples of two-way vertical ladders in Bedrock Edition
Although horizontal signal transmission is straightforward, vertical transmission involves options and trade-offs.
- Redstone staircases:The simplest way to transmit signals vertically is by placingredstone duston blocks diagonally upward, either in a straight staircase of blocks, in a 2×2 spiral of blocks, or in another similar variation. Redstone staircases can transmit signals both upward and downward but can take up much space and require repeaters every 15 blocks.
- Redstone ladders:Becauseglowstone, topslabs,glass, and upside-downstairscan supportredstone dustbut don't cut redstone dust, signals can be transmitted vertically (upward only) by alternating these blocks in a 2×1 "ladder". Redstone ladders take up less space than redstone staircases, but also require repeaters every 15 blocks. InBedrock Edition, glass and pistons can be used to create two-way vertical ladders that transmit signals both upward and downward (glowstone, hoppers, and slabs still allow the dust to power upward but not downward).
- Torch towers and torch ladders:Aredstone torchcan power a block above it, or redstone dust beneath it, allowing vertical transmission both upward and downward (different designs are required for each). Because it takes each torch a little time to change state, a torch tower can introduce some delay into a circuit, but no repeaters are necessary. However, every torch inverts the redstone signal (i.e. changes it from powered to unpowered), so having an even number of torches is required.
- Observer towers:Anobservercan power a block of a redstone circuit above or below it, allowing vertical transmission both upward and downward. Placing blocks that can be activated, such asredstone dust,note blocksordoors, both above and below it creates a state change to the block above when the observer is looking downward or to the block below when the observer is looking upward. Repeating this pattern means that updates are chained.
- Daylight detector exploiting:You can use daylight detectors to send a Redstone signal downward in 1 tick, but the path needs to be unobstructed by anything. You need to have a piston push a block over the sensor. It detects the change in light and emits a Redstone pulse. This design is extendable upward as far as you want, but you need to have the original hole open to sunlight. It also works only during the day, because it uses shadows to activate.
- Bubble columns:Anobservercan be used to detect the block update that occurs when awatersource changes to abubble column(or vice versa). When swapping the block below a column of water sources tosoul sandor amagma blockfrom some other block, the entire column immediately changes to bubble column blocks. This can be used to quickly transmit a redstone signal upward to an observer facing the top water source/bubble column block.
- Wall updating: A setup that can carry a pulse signal downwards across any distance involveswallsof any type of stone, a piston, and an observer. When a wall block has a solid block on two opposing sides and non-solid blocks (e.g., air) on the other two sides, it takes a flat shape. This is vertically repeatable up to any height. However, when a wall/solid block is placed into one of the two air blocks around a flat wall, the flat wall blockand every flat wall block below itare updated to a different version of the wall with a column in the middle. This update is instant and can be detected by an observer watching any flat wall in the tower. The update can be made repeatable by having a regular piston face the flat wall at the top of the tower, since the piston head also triggers the wall update.

** Repeater **
To "repeat" a signal means to boost it back up to full strength. The easiest way to do this is with aredstone repeater. Variations include:
- Instant repeater:Repeats a solid signal without the delay introduced by a redstone repeater.
- Two-way repeater:Repeats a signal in both directions.

** Diode **
A "diode" is a one-way circuit that allows a signal to travel in one direction. It is used to protect another circuit from the chance of a signal trying to enter through the output, which could incorrectly change the circuit's state or interfere with its timing. It is also used in a compact circuit to keep one part of the circuit from interfering with another. Common choices for a diode include aredstone repeateror a height elevation toglowstoneor a topslab, which does not transmit a signal back down.
Many circuits are already one-way simply because their output comes from a block that can't take input. For example, a signal cannot be pushed back into a circuit through a redstone torch except through the block it's attached to.
### Logic circuit
Main article: Logic circuit
It's sometimes necessary to check signals against each other and output a signal only when the inputs meet some criteria. A circuit that performs this function is known as a logic gate (a "gate" that allows signals through only if the logic is satisfied).   

In electronic or programming diagrams, logic gates are typically shown as if they were individual devices; However, when building redstone devices in Minecraft, all logic gates are formed from multiple blocks and components, which interact to produce the desired results.

** NOT gate **
A NOT gate (aka "inverter") is on if its input is off. The simplest NOT gate is an input signal with a redstone torch attached.
** OR gate **
An OR gate is on ifanyof its inputs are on. The simplest OR gate is to feed multiple input signals together into a single block or redstone wire.
** NOR gate **
A NOR gate is on only ifnoneof its inputs are on. The simplest NOR gate is to feed multiple input signals into a block with a redstone torch attached.
** AND gate **
An AND gate is on only ifallof its inputs are on. The simplest AND gate is to add redstone torches in front of each input to a NOR gate.
** NAND gate **
A NAND gate is on ifanyof its inputs are off. The simplest NAND gate is to remove the final redstone torch from an AND gate.
** XOR gate **
An XOR gate is on if its inputs aredifferent.
** XNOR gate **
An XNOR gate is on if its inputs areequal.
** IMPLY gate **
An IMPLY gate is on unless the first input is on and the second input is off.
| A                | On  | On  | Off | Off | Question Answered         |
|------------------|-----|-----|-----|-----|---------------------------|
| B                | On  | Off | On  | Off |                           |
| A AND B          | ON  | off | off | off | Are A and B on?           |
| NOT(A IMPLIES B) | off | ON  | off | off | Is A on and B off?        |
| NOT(B IMPLIES A) | off | off | ON  | off | Is B on and A off?        |
| A NOR B          | off | off | off | ON  | Are both inputs off?      |
| A                | ON  | ON  | off | off | Is A on?                  |
| A XOR B          | off | ON  | ON  | off | Are the inputs different? |
| NOT A            | off | off | ON  | ON  | Is A off?                 |
| A XNOR B         | ON  | off | off | ON  | Are the inputs the same?  |
| B                | ON  | off | ON  | off | Is B on?                  |
| NOT B            | off | ON  | off | ON  | Is B off?                 |
| A NAND B         | off | ON  | ON  | ON  | Is either input off?      |
| A IMPLIES B      | ON  | off | ON  | ON  | If A is on, is B also on? |
| B IMPLIES A      | ON  | ON  | off | ON  | If B is on, is A also on? |
| A OR B           | ON  | ON  | ON  | off | Is either input on?       |

### Pulse circuit
Main article: Pulse circuit
Some circuits require specific pulses; other circuits use pulse duration to convey information. Pulse circuits manage these requirements.

A circuit that is stable in one output state and unstable in the other is known as a monostable circuit.[note 1] Many pulse circuits are monostable because their OFF state is stable, but their ON state soon reverts to OFF.

** Pulse generator **
A pulse generator produces a pulse of a specific duration.
** Pulse limiter **
A pulse limiter (aka pulse shortener) reduces the duration of pulses that are too long.
** Pulse extender **
A pulse extender (aka pulse sustainer, pulse lengthener) increases the duration of pulses that are too short.
** Pulse multiplier **
A pulse multiplier outputs multiple pulses for every input pulse (it multiplies the number of pulses).
** Pulse divider **
A pulse divider (aka pulse counter) outputs a signal only after a certain number of pulses have been detected through the input (the number of pulses is indicative of the number of loops).
** Edge detector **
An edge detector reacts to either a redstone signal changing from OFF to ON (a "rising edge" detector), from ON to OFF (a "falling edge" detector), or switching between ON and OFF in either order(a "dual edge" detector).
** Pulse length detector **
A pulse length detector reacts only to pulses in a certain range of durations (often only to pulses of one specific duration).
### Clock circuit
Main article: Clock circuit
A clock circuit is a pulse generator that produces a loop of specific pulses repeatedly. Some are designed to run forever, while others can be stopped and started.

A simple clock with only two states of equal duration is named for the duration of its ON state (e.g., for example, a clock that alternates between a 5-tick ON state and a 5-tick OFF state is called a 5-clock) while others are usually named for their period (the time it takes for the clock to return to its original state; for example, a "1-minute clock" might produce a 1-tick pulse every 60 seconds).

** Observer clock 1 **
A repeating clock made with Observers and Pistons (an Observer looking at a piston).Observer clock 2
A repeating clock made with two Observers with their faces facing each other.
** Repeater clock **
A repeater clock consists of a loop of repeaters (usually eitherredstone repeatersorredstone torches) with occasional dust or blocks to draw off the appropriate pulses.
** Hopper clock **
A hopper clock produces timed pulses by moving items back and forth between 2 hoppers feeding into each other and taking a redstone output with comparators.
** Piston clock **
A piston clock produces a loop of pulses by passing a block back and forth (or around, with many pistons) and drawing off a redstone pulse when the block is in a certain location.
** Comparator clock **
The clock of short or moderate cycle length utilizing comparator's subtraction or signal fading feature. Clocks can also be built usingdaylight sensors,minecarts,boats, water flow, item despawn, etc.
### Memory circuit
Main article: Memory circuit
Unlike a logic circuit whose state always reflects its current inputs, a memory circuit's output depends not on the current state of its inputs, but on the history of its inputs. This allows a memory circuit to "remember" what state it should be in, until told to remember something else. There are five basic types of memory circuits. (A few circuits combine two different types.) 

** RS latch **
An RS latch has two inputs, one to set the output on and another to reset the output back to off. An RS latch built from NOR gates is known as an "RS NORlatch", which is the oldest and most common memory circuit inMinecraft.
** T flip-flop **
A T flip-flop is used to toggle a signal (like a lever). It has one input, which toggles the output between on and off.
** Gated D latch **
A gated D latch has a "data" input and a "clock" input. When the clock input turns on, it sets the output to equal its data input. Not to be confused with a D flip-flop, which sets the output equal to its data input on a clock rising transition.
** JK latch **
A JK latch has two inputs, one to set the output on and another to reset the output back to off (like an RS latch), but when both turn on simultaneously it toggles the output between on and off (like a T flip-flop).
** Counter **
Unlike T flip-flops and RS latches, which can hold two states (ON or OFF), a counter can be designed to hold a greater number of states.
Many other memory circuits are possible.

### Piston circuits
Main article: Piston circuits
Pistons allow players to design circuits that are smaller and/or faster than the standard, redstone-only counterparts. An understanding of standard redstone circuits is helpful, as this tutorial is focused on the circuit design rather than the function. The main components here are sticky pistons, regular pistons, redstone wire, repeaters and redstone torches.

There are several benefits of piston circuitry:

- Neither repeaters nor pistons 'burn out', unlike redstone torches.
- Piston circuits are often (not always) smaller and/or faster than their redstone counterparts. This allows building devices such as fast clocks and "instant" signal transmission.
- Pistons' ability to move blocks within the world makes them a natural for memory circuits, as well as the obvious doorways and switchable bridges. With slime or honey blocks involved, entire structures can "get up and move" (see alsotutorial on flying machines).
- Piston circuits can sharply reduce the use of redstone in favor of wood, stone, and iron.

### Miscellaneous circuits
Main article: Miscellaneous circuits
These circuits aren't generally needed for redstone projects, but might find use in complex projects, proofs of concept, and thought experiments. Some examples:

** Multiplexers and relays **
A multiplexer is an advanced form of logic gate that chooses which of two inputs to let through as output based on an additional input (for example, if input A is ON then output input B, otherwise output input C). The reverse of this is a relay, which copies a data input to one of two outputs, depending on whether the additional input is ON or OFF.
** Randomizers **
Main article: Tutorials/Randomizers
A randomizer produces output signals unpredictably. Randomizers can be designed to produce a pulse at random intervals, or to randomize which of multiple outputs are turned ON (such as random number generators, or RNGs). Some randomizers use the random nature ofMinecraft(such ascactusgrowth ordispenserslot selection), while others produce pseudo-randomness algorithmically.
** Multi-bit circuits **
Multi-bit circuits treat their input lines as a single multi-bit value (something other than zero and one) and perform an operation on them all at once. With such circuits, possibly combined with arrays of memory circuits, it's possible to build calculators, digital clocks, and even basic computers insideMinecraft.
** Block update detectors **
Main article: Tutorials/Block update detector
Main article: Tutorials/Comparator update detector
A block update detector (BUD, or BUD switch) is a circuit that reacts to a block changing its state (for example, stone being mined, water changing to ice, a pumpkin growing next to a pumpkin stem, etc.). BUDs react by producing a pulse, while T-BUDs (toggleable BUDs) react by toggling their output state. These are generally based on subtle quirks or glitches in device behavior; current circuits most often depend on pistons. As ofJava Edition 1.11, many of the functions of BUDs were condensed into theobserver, however, a BUD circuit can also detect other changes undetectable by observers, like a furnace finishing smelting or something being crafted in a crafting table. The addition of this was made to move toward feature parity withBedrock Editionversions.
** More advanced circuits **
Main article: Tutorials/Advanced redstone circuits
Many other complex circuits are possible.
