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

