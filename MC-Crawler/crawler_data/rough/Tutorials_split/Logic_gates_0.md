# Tutorials/Logic gates
A full adder takes two inputs A and B and a Carry input and produces the Sum and Carry outputs. It relies on two XOR gates, two AND gates, and one OR gate. With some thought, these gates can be compressed (as both AND and XOR gates already exist in the game, and an OR gate can simply be a redstone wire).

A and B are the bit inputs and C' is the carry in. It produces a sum at S and a carry out at C. When full adder modules are tiled together C' and C are connected, which allows the carry to propagate to the next module.

## Contents
- 1 Adders
	- 1.1 Version 1
	- 1.2 In-line adder
	- 1.3 Version 2
	- 1.4 Version 3
	- 1.5 Fast adding
	- 1.6 Piston adders
	- 1.7 4-bit adder
	- 1.8 Alternate 4-bit adder
- 2 Subtracting
- 3 Logic units
	- 3.1 Arithmetic logic unit

## Adders
### Version 1
In-game screenshot of the Full adder
Full adder 1 View at: Tutorials/Logic gates/Full adder 1 [edit]
** Full Adder **
A full adder takes two inputs A and B and a Carry input and produces the Sum and Carry outputs. It relies on two XOR gates, two AND gates, and one OR gate. With some thought, these gates can be compressed (as both AND and XOR gates already exist in the game, and an OR gate can simply be a redstone wire).

A and B are the bit inputs and C' is the carry in. It produces a sum at S and a carry out at C. When full adder modules are tiled together C' and C are connected, which allows the carry to propagate to the next module.


Full Adder Schematic



** Half adder **
The half adder is nearly identical to the full adder, except the second XOR gate is removed and the output from the first XOR gate becomes S. There is no carry in (C'), but the carry out (C) circuit is still on top of the first XOR gate and provides a carry to the first full adder. Some ALUs do not use a half adder for the first bit, to support INCREMENT (allow a carry in on the first bit).


### In-line adder
** Full adder **
In-game screenshot of the 2 wide Full Adder
This full adder is similar to the previous one, except for the fact that it is two wide and the inputs are aligned vertically. This design is great for minimizing horizontal space and can be built in-line with two redstone buses, eliminating the space required to expand a bus to reach the inputs of a wider full adder.


Schematic of the Full Adder



| Tutorial video (view on YouTube) |
|----------------------------------|
|                                  |


### Version 2
** Full Adder **
Gates: XNOR (2), IMPLIES, NOT, OR, AND 
Size: 6×12×5 (including I/O spaces)

This adder takes 2 bits and a carried over bit (actually C, rather than C, a value held in the redstone in the bottom left corner on layer 1) and adds them all together, producing a sum (S) bit and a carry (actually C rather than C).

When using the gates above; mind the inputs and outputs. You may be wondering why there are so many inverted signals being used instead of the regular signal.

The adders shown here use XNOR gates rather than XOR gates because they are more compact, and as a result, implies gates must be used instead of AND gates, which also happen to be more compact.

Therefore, for the most compact adder, inverse signals must be used. These adders are too complex to be easily deciphered with 2 layers per square, so each single layer has been drawn separately to ease the building process.


Schematic of the Full Adder



** Half Adder **
Gates: XNOR, IMPLIES
Size: 5×4×4

This adder takes 2 bits and adds them together. The resulting bit is the output of S (sum). If both bits are 1, there is a carry over, and C becomes 1 (C becomes 0). This half adder can be modified to create a non inverted C output, but this configuration is used so that it can be implemented as the start of a chain of full adders.

Extension:
for those new to advanced redstone like myself, it's easier to understand it like this: let's say output B (C) has a NOT gate that inverts the signal and it leads to an iron door or piston door etc. Output A (S) is connected to sticky pistons controlling the floor. Let's say for sake of argument that there is 1×1×1 block NOT affected by the sticky pistons, this is the safety block. When you activate input A, the door opens and the floor drops, if you're standing on the safety block, then you cannot fall. Input B controls only the floor, but if input A is on then input B controls them both. When both are on, input A affects only the floor. This means if you are off the server and want no one in, leave A and B on, when they deactivate A, the floor drops, but the door stays closed, so if they know the secret, they still cannot get in.


Schematic of the Half Adder



