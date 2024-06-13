# Redstone circuits/Piston
Pistons have allowed players to design circuits that are smaller and/or faster than the standard, redstone-only counterparts. An understanding of standard redstone circuits is helpful, as this tutorial is focused on the circuit design rather than the function.

There are three benefits of piston circuitry:

## Contents
- 1 Principles
- 2 Piston gate designs
	- 2.1 NOT gate
	- 2.2 OR gate
	- 2.3 AND gate
	- 2.4 IMPLIES gate
	- 2.5 XNOR gate
	- 2.6 XOR gate
- 3 Latches
	- 3.1 RS latches
	- 3.2 T flip-flops
- 4 Ring memory
- 5 Clocks
	- 5.1 Rapidfire piston clock
	- 5.2 Alternate rapidfire piston clock
	- 5.3 Pulser
	- 5.4 Rapid fire trap clock
- 6 Edge detector
- 7 Double extender

## Principles
Power and Repeaters View at: Mechanics/Redstone/Piston circuits/Power 1 [edit]

Power is transmitted in several ways that are useful to pistons. The first thing to note is that there are two types of blocks; transparent and solid. Transparent blocks are things such as glass, slabs, or air, while solid blocks are more common materials such as dirt, stone, or wool. 

The key is that redstone power can be transmitted through solid blocks, but not transparent blocks.  However, power can pass through only one solid block at a go, it cannot be passed from one solid block to another.  A solid block can power wire leading from it only if it was "strongly powered" (by a redstone torch, repeater, or comparator, but not by redstone wire). Redstone dust can be placed on some transparent blocks, but then it transmits power only upward, not downward (that is, not through the transparent block).

Redstone torches are considered logic components only if they change states as the gate is used.  (Otherwise they're just power supplies.)  If they change state too often, they are susceptible to burning out.  If a solid block is on top of a redstone torch, any wire connected to the block becomes powered. If, however, the block is transparent, the torch does not power the wires. In Creative mode, using torches as power-supplies for blocks above is mostly deprecated by the introduction of redstone blocks, which are permanently powered. They have a higher cost in Survival, though.

When a repeater is directed at a solid block, it passes power into that block in the same way redstone torches do.  A repeater can also take power from a solid block that is powered, even weakly powered (that is, it turns a weakly powered signal into a strong one).  Power cannot be transmitted by transparent blocks.

Pistons extend if powered, but it's notable that they can take power from the block above them – that is, even if the block is air, if that block would have been powered, then the piston is powered. They can also be powered through their extended piston, which produces several useful quirks that are commonly used in circuits.  A piston can push up to 12 blocks when it extends; however, a sticky piston can pull back only one block when it retracts. Some blocks are immune to being pushed or pulled, notably obsidian and any block with a GUI or inventory (except crafting tables).  Other blocks drop as items if a piston tries to push them; this includes most "attached" blocks such as either sort of torch, or doors, but also a few others such as jack-o-lanterns.

## Piston gate designs
Main article: Logic circuit
Pistons can produce alternate designs for many of the classic logic gates.  Piston gates may also use redstone torches to supply a constant signal (in which case they can often be replaced by levers), or for other purposes.

### NOT gate
Piston NOT gate View at: Mechanics/Redstone/Piston circuits/Piston NOT [edit]
The piston-only NOT gate, also called an inverter, is slightly larger than a standard redstone NOT gate, so it is rarely used alone.  However, it demonstrates an important concept used in many piston mechanisms, namely that torches below solid blocks create a current in any surrounding wire. When an input is triggered, the piston extends, uncovering the torch hole removing the signal from the output line.  The input can power the piston from almost any direction. Alternatively, a block of redstone can be used in to shrink the design.


### OR gate
Piston OR gate View at: Mechanics/Redstone/Piston circuits/Piston OR [edit]
This design is slightly faster than the standard redstone OR gate, with a comparable size.
It uses one piston that covers a torch when extended by any of the inputs.


### AND gate
Piston AND gate View at: Mechanics/Redstone/Piston circuits/Piston AND [edit]
Incredibly fast AND gate. When unpowered, the sticky piston pulls the block over the hole, breaking the circuit.  When powered, it extends and lets the current flow in and out of the hole.  One input feeds the piston, the other feeds the circuit it interrupts; both must be ON to release a signal.


### IMPLIES gate
Piston IMPLIES gate View at: Mechanics/Redstone/Piston circuits/Piston IMPLIES [edit]
Comparable size and speed to some of the basic redstone IMPLIES gate.
This gate represents material implication. Returns false only if the implication A → B is false. That is, if the conditional A is true, but the consequent B is false. It is often read "if A then B." It is the logical equivalent of "B or NOT A".  The torch under the mobile block is in a hole.




### XNOR gate
Piston XNOR gate View at: Mechanics/Redstone/Piston circuits/Piston XNOR [edit]
Pronounced "ex-nor", this device activates when both inputs are equal. A useful attribute is that a XOR or XNOR gate always changes its output when one of its inputs changes, allowing for 2 switches to be combined to open or close a door, or activate another device. This design is significantly smaller than the redstone-only equivalent and slightly faster. Adding a NOT gate to the end or to either input produces an XOR gate, which activates when the inputs are different.


