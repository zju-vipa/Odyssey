# Redstone mechanics
Redstone mechanics provide Minecraft with a loose analogue to electricity, which is useful for controlling and activating a variety of mechanisms. Redstone circuits and devices have many uses including automatic farms, controlling doorways, changeable or mobile buildings, transporting players and mobs, and more. Some relevant pages include:

## Contents
- 1 Redstone Concepts
	- 1.1 Redstone tick
	- 1.2 Redstone components
	- 1.3 Power
	- 1.4 Signal strength
	- 1.5 Signals and pulses
	- 1.6 Activation
		- 1.6.1 Activation behavior
		- 1.6.2 Powered vs. activated
		- 1.6.3 Normal activation rules
		- 1.6.4 Special activation rules
	- 1.7 Redstone block updates

## Redstone Concepts
### Redstone tick
A redstone tick is a unit of time, in redstone, that is equal to two game ticks, 0.1 seconds. Most redstone components take a multiple of a redstone tick to change states. Redstone torches, redstone repeaters, and other redstone components require one or more ticks to change state, so it can take several ticks for a signal to propagate through a complicated circuit.

Redstone ticks differ from "game ticks" (20 per second) and "block ticks" (block updates that occur at each game tick). When discussing redstone circuits, the term "tick" should always be interpreted to mean a redstone tick, unless otherwise specified.

### Redstone components
Main article: Redstone components
A Redstone component is a block that provides some purpose to a Redstone circuit.

- Apower componentprovides power to other parts of a circuit—e.g.,redstone torches,buttons,levers,redstone blocks,target blocks, etc. Some of these fall into one of three overlapping subgroups:
	- Switches provide power depending on request by the player.Buttonsandleversare switches.
	- Sensors provide power or signals (see below) in response to some environmental condition.Pressure platesandObserversare sensors, andcomparatorscan be used as sensors. Note that some pressure plates can be triggered by a player standing on them, which also qualifies them as switches.
	- Logic components provide power conditionally, depending on their input conditions. Redstone torches, and comparators are classic logic components; redstone wire and ordinary opaque blocks can also be used to combine signals in various ways.
- Atransmission componentpasses power from one part of the circuit to another.Redstone dust(placed as redstone wire) is the most fundamental transmission component, butredstone repeatersandredstone comparatorsare also important.
- Amechanism componentaffects the environment (by moving, producing light, etc.)—e.g.,Doors,pistons,redstone lamps,dispensers, etc.

### Power
The Redstone Lamps are all activated, but are powered differently. From top to bottom: Strongly powered: powers both Repeater and Dust. Weakly powered: powers Repeater, but not Dust. Not powered: powers neither.
Redstone components and blocks may or may not be powered. A "powered block" can be thought of as a block that has electricity running through it. Some blocks will show their powered state visibly (for example, redstone dust lights up, a redstone lamp illuminates its surroundings and a redstone torch turns off), but other blocks may give no visual indication of their powered state other than their effect on other redstone components.

An opaque block (e.g. stone, dirt, etc.) powered by a power component, or by a repeater or comparator, is said to be strongly powered or 'hard-powered' (a different concept from power level). A strongly powered block can power adjacent redstone dust (including dust on top of the block or dust beneath it).

An opaque block powered only by redstone dust (and no other components) is said to be weakly powered or 'soft-powered' because a block powered only by redstone dust will not power other redstone dust (but can still power other components or devices, such as repeaters and pistons).

No opaque block can directly power another opaque block—there must be dust or a device in between. A transparent block can't be powered by anything. "Strong"/"hard" vs. "weak"/"soft" power applies only to opaque blocks, not to dust or other redstone components.

A powered block (strong or weak) can affect adjacent redstone components. Different redstone components react differently to powered blocks—see their individual descriptions for details.

### Signal strength
Redstone "signal strength" can be an integer between 0 and 15. Most power components provide an output of power level 15, but a few components provide a variable amount of power. These include daylight sensors and redstone comparators.

Redstone dust transmits power to adjacent redstone dust and blocks in the direction it is pointing, but its strength decreases by 1 for each block the redstone power travels. Redstone dust can thus transmit power up to 15 blocks before needing to be maintained with a redstone comparator or re-strengthened with a repeater. Power level only fades with the dust-to-dust transmission, not between dust and a device or block.

The power level can also be adjusted directly with a redstone comparator in comparison or subtraction mode.

