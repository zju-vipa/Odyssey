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

