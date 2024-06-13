### XOR gate
Piston XOR gate View at: Mechanics/Redstone/Piston circuits/Piston XOR [edit]
Pronounced "ex-or" (a shortening of "exclusive or"), this device activates when only one of the inputs is on. This design, like the XNOR gate, is smaller and faster than the redstone-only equivalent.


## Latches
Main article: Memory circuit
Latches are memory circuits.  Naturally, pistons' ability to physically move blocks to new locations make them a natural tool for these.

### RS latches
Piston RS Latches View at: Mechanics/Redstone/Piston circuits/Piston RS Latches [edit]
The basic piston RS Latch is small and easy to make. The pistons used here are regular pistons, not sticky pistons, and push a block over one of two holes containing a Redstone Torch. One hole can be omitted if only one output is required.  Using a Block of Redstone lets the circuit become even smaller, and adds the inverse output.


### T flip-flops
These T flip-flops use one input to switch between two states. 

Sticky pistons behave strangely when they receive a 1-tick signal. If a block is directly next to the piston, the piston pushes the block but does not pull it back when the signal ends. If the piston receives another 1-tick signal, the piston extends and retract the block. This can be used to toggle the position of blocks. 

Piston Toggle A View at: Mechanics/Redstone/Piston circuits/Piston Toggle A [edit]
Design A, 4×2×4. Uses regular pistons. Both of the pistons are regular pistons. This flip flop is quite fast and quite small. It toggles when the input changes from ON to OFF. Inverting the input increases the speed of the circuit.  


Piston Toggle B View at: Mechanics/Redstone/Piston circuits/Piston Toggle B [edit]
Design B (5×3×2) is actually an RST latch, combining the functionality of both the Set/Reset (RS) and toggle (T) latches.  Uses regular pistons. This flip flop doesn't use torches for logic so it can work with signals of any length.   The dust on level 1 is there to redirect the redstone wire away from block X, which powers the piston.   However, this circuit does not have an inverse output.


Piston Toggle C View at: Mechanics/Redstone/Piston circuits/Piston Toggle C [edit]
Design C is a combination pulse limiter and downward edge detector. When the signal turns off, the first sticky piston retracts the second, which receives a 1-tick signal. The 1-tick signal toggles the mobile block.  It is sensitive to timing.


1-wide Sticky Piston TFF View at: Mechanics/Redstone/Piston circuits/Sticky Piston Compact TFF [edit]
The 1-wide Sticky Piston TFF design is 5×1×3. It depends on the fact that a sticky piston leaves the block after extending when given a short pulse of 0.5 ticks of delay. A circuit breaker is used to give a 0.5 ticks pulse to the sticky piston. This makes the sticky piston leave the redstone block, which then provides power to the output. When powered again, the sticky piston pulls the redstone block switching the output off. It is possible to make this TFF tileable.


## Ring memory

  

This section needs schematic(s) or diagram(s) instead of YouTube video links. 
Please remove this notice once you've added suitable diagram(s) to the article.


A simple ring of blocks, rotated by pistons. The reading head is on the right side of the ring. The rightmost circuit is a clock that drives the pistons
This is a ring of blocks attached to regular pistons at the corners so it can rotate. The blocks are usually a combination of solid and non-solid blocks. The pistons are often connected to a clock so that they rotate the ring. Most (if not all) rings have a reading head consisting of a repeater pointing at the ring and a redstone torch powering the repeater. By using redstone on the other side of a ring, one can see which type of block is in front of the reading head (1 = Solid; 0 = Non-solid). This information now can be passed to a circuit. By using a comparator and reading a cauldron's fill level, 3 additional memory cell states are available. For repeater-based reading heads those act as zeroes.

Adding multiple rings together in a row creates a band. A band stores even more information and works similar to punched tape. Examples include music machines, combination locks, and memory.



## Clocks
Main article: Mechanics/Redstone/Clock circuit
### Rapidfire piston clock
Rapidfire Piston Clock View at: Mechanics/Redstone/Piston circuits/Rapidfire Piston Clock [edit]
This rapidfire clock is fairly simple to build.  It requires 2 non-sticky pistons, 2 repeaters, and 6 redstone, and 5 solid blocks. The repeaters must be set to at least 2 ticks, and they must match.  Place the mobile block last to start the clock, and take output from either end or any wire.  Note that this clock is not switchable, and if it does stop for any reason, it's difficult to restart by a redstone signal.  The player can restart it by breaking and replacing the mobile block, or by changing the repeater delays (both of them; the clock restarts when they match and are set to at least 2 ticks).


### Alternate rapidfire piston clock
Alternate Rapidfire Piston Clock View at: Mechanics/Redstone/Piston circuits/Alternate Rapidfire Piston Clock [edit]
This piston clock is a simple way of repeating a circuit that goes at high speed without burning out. It does not require repeaters or redstone torches. A tutorial is available here. It requies a single sticky piston, one lever, a small amount of redstone, and some solid blocks. From the lever, the redstone has to be placed so it goes up a block, before linking up to the piston. The piston has to be placed in a way that, when it is extended, it blocks the redstone from going up the side of the block without breaking the redstone. This breaks the circuit, removing power from the piston and thus retracting it, causing the circuit to open again. The signals are too fast to affect lighting sources such as lamps and redstone torches. Doors and dispensers both work well at this speed.


