# Tutorials/Advanced redstone circuits
Advanced redstone circuits encompass mechanisms that require complicated redstone circuitry. They are usually composed of many simpler components, such as logic gates. For simpler mechanisms, see electronic mechanisms, wired traps, and redstone.

## Contents
- 1 Computers
- 2 Converters
	- 2.1 Piston mask demultiplexer
	- 2.2 Binary to 1-of-8
	- 2.3 Binary to 1-of-16 or 1-of-10
	- 2.4 1-of-16 to Binary
		- 2.4.1 Example
- 3 Miscellaneous
	- 3.1 Combination locks
	- 3.2 Sorting device
	- 3.3 Timer
	- 3.4 Serial interface lock with D flip-flops
- 4 See also

## Computers
Main article: Tutorials/Redstone computers
In Minecraft, several in-game systems can usefully perform information processing. These systems include water, sand, minecarts, pistons, and redstone. Of all these systems, only redstone was specifically added for its ability to manipulate information, in the form of redstone signals. 

Redstone, like electricity, has high reliability and high switching-speeds, which has seen it overtake the other mechanical systems as the high-tech of Minecraft, just as electricity overtook the various mechanics such as pneumatics to become the high-tech of our world.

In both modern digital electronics and redstone engineering, the construction of complex information processing elements is simplified using multiple layers of abstraction.

The first layer is that of atomic components; redstone/redstone torches/redstone repeaters/blocks, pistons, buttons, levers and pressure plates are all capable of affecting redstone signals. 

The second layer is binary logic gates; these are composite devices, possessing a very limited internal state and usually operating on between one and three bits.

The third layer is high-level components, made by combining logic gates. These devices operate on patterns of bits, often abstracting them into a more humanly comprehensible encoding like natural numbers. Such devices include mathematical adders, combination locks, memory-registers, etc.

In the fourth and final layer, a key set of components are combined to create functional computer systems which can process any arbitrary data, often without user oversight.

An 8-bit register page would be in the third layer of component abstraction
## Converters
These circuits simply convert inputs of a given format to another format. Converters include Binary to BCD, Binary to Octal, Binary to Hex, BCD to 7-Segment, etc.

### Piston mask demultiplexer
You can understand this design as a combination of AND gates. 

Demultiplexer is a circuit that uses the following logic:

Output 0 = (~bit2) & (~bit1) & (~bit0)

Output 1 = (~bit2) & (~bit1) & (bit0)

...

The most obvious way to implement a demultiplexer would be to put a whole bunch of logic gates and connect them together, but even with 3 or 4 bits it turns into a mess.

If you look at the binary numbers table, you can notice a pattern.

| N | Bit2 | Bit1 | Bit0 |
|---|------|------|------|
| 0 | 0    | 0    | 0    |
| 1 | 0    | 0    | 1    |
| 2 | 0    | 1    | 0    |
| 3 | 0    | 1    | 1    |
| 4 | 1    | 0    | 0    |
| 5 | 1    | 0    | 1    |
| 6 | 1    | 1    | 0    |
| 7 | 1    | 1    | 1    |

If the number of bits is Q, the most significant bit reverses every Q/2 numbers, the next bit reverses every Q/4 numbers an so on until we get to the Qth bit.

Therefore, we should make a circuit that looks like this:



Where the green triangles are non-reversing and red triangles are reversing. The black lines are imaginary AND gates.

We can easily implement this using 3 "punch cards" that consist of solid blocks and air. The "punch cards" or the masks are being moved by pistons with slime blocks. 

So the signal is only being propagated if all three layers of masks align in a specific way.



 Open the picture to see the layers.

As you can see, this system is very compact and comprehensible.

You can use this in reverse as well (not as a multiplexer, but if you reverse the repeaters the signal from every ex-outptut (0–7) will only propagate if it matches the current state of the demultiplexer, so it works like "Output3 = (Input3) AND (Demux=011)").

### Binary to 1-of-8
3-bit Binary to 1-of-8 gates.
A series of gates that converts a 3-bit binary input to a single active line out of many. They are useful in many ways as they are compact, 5×5×3 at the largest.

As there are many lines combined using implicit-ORs, you have to place diodes before each input into a circuit to keep signals from feeding back into other inputs.

Requirements for each output line (excluding separating diodes):

| Number   | 0     | 1     | 2     | 3     | 4     | 5     | 6     | 7     |
|----------|-------|-------|-------|-------|-------|-------|-------|-------|
| Size     | 5×3×2 | 5×3×3 | 5×5×3 | 5×5×3 | 5×3×3 | 5×4×3 | 5×5×3 | 5×5×3 |
| Torches  | 1     | 2     | 2     | 3     | 2     | 3     | 3     | 4     |
| Redstone | 7     | 7     | 12    | 10    | 7     | 7     | 10    | 10    |


