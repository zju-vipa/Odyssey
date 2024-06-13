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

