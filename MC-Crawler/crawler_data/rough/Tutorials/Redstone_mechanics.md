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

### Signals and pulses
Circuits with a stable output are said to produce a signal — an ON signal (also "high" or "1") if powered, or an OFF signal ("low", "0") if unpowered. When a signal changes from OFF to ON ("rising edge") and then back to OFF ("falling edge"), that is described as a pulse (or ON pulse), while the opposite is described as an OFF pulse. ON pulses are far more common, and in casual discussion, "a signal" often refers to an ON pulse.

Very short pulses (1 or 2 ticks) can cause problems for some components or circuits because they have different update sequences to change states. For example, a redstone torch or a comparator will not respond to a 1-tick pulse.

### Activation
Activation of Mechanism Components — Mechanism components can be activated by power components (for example, redstone torches), powered blocks, redstone dust, repeaters, and comparators (not shown), but only if configured correctly.
Mechanism blocks (pistons, doors, redstone lamps, etc.) can be activated by incoming power, which causes the mechanism component to do something (push a block, open the door, turn on, etc.).   



#### Activation behavior
There are two main variations for how things can respond to activation:

- Many types only perform an action when initially activated by a rising edge (command blocks execute a command, droppers and dispensers eject an item, note blocks play a sound) and won't do anything again until deactivated and then activated again
- Other mechanism components change their state when activated, and then change back when the activation ends; Redstone lamps stay on while the power continues, while hoppers stay disabled. Pistons will extend when powered, and retract when the power turns off. Doors, fence gates, and trapdoors will open on a rising edge, and close on a falling edge; however, most of these (not iron doors or iron trapdoors) canalsobe opened or closed by players regardless of the redstone power. If they were already open when power turns on, or closed when power ends, they will simply remain so until their input changes again.

#### Powered vs. activated
Powered vs. ActivatedThe top lamp is both activated (the lamp is on) and powered (it powers the adjacent repeater).The bottom lamp is activated but not powered.
For opaque mechanism blocks (command blocks, dispensers, droppers, note blocks, and redstone lamps), it is important to make a distinction between a mechanism component being activated and being powered (and this is the reason why mechanism components are described as activated instead of just saying they are powered).

- A mechanism component ispoweredif it could power adjacent redstone dust (strongly), or repeaters or comparators (weakly).
- A mechanism component isactivatedif it is doing something (or has done something and is waiting to be activated again).

Any method of powering a mechanism component (such as a redstone torch underneath it) will also activate it, but some activation methods (such as a redstone torch next to or above a mechanism component) won't actually power the component (following the usual rules for power components).

Non-opaque mechanism components (doors, fence gates, hoppers, pistons, rails, trapdoors) can be activated (they can do things), but cannot be powered (i.e. they can not then power adjacent redstone dust, etc.).

#### Normal activation rules
In general mechanism components are activated by:

- an adjacent activepower component, including above or below.
	- Exception:A redstone torch will not activate a mechanism component it is attached to
	- Exception:A piston is not activated by a power component directly in front of it.)
- an adjacentpowered opaque block(either strongly-powered or weakly-powered), including above or below.
- a poweredredstone comparatororredstone repeaterfacing the mechanism component.
- poweredredstone dustconfigured to point at the mechanism component (or on top of it, for mechanical components that can support redstone dust, butnotbeneath it), or adjacent "directionless" redstone dust; a mechanism component isnotactivated by adjacent powered redstone dust that is not configured to point at it

#### Special activation rules
Activation by Quasi-Connectivity — Pistons can also be activated by anything that activates the space above them. Note that the piston on the far left is not activated by quasi-connectivity because the redstone dust is running past the block above the piston, rather than directly into it, and thus would not power a mechanism there
Some mechanism components have additional ways of being activated:

- InJava Edition,pistons,dispensers,droppers, and can also be activated if one of the methods abovewouldactivate a mechanism component in the block above the component, even if there is no mechanism component there (even if the block above the component isairor a transparent block). This rule is often simplified to saying that the components can be powered by blocks diagonally above or two blocks above, but other methods of such activation exist (see image to the right). This method of activation is known asquasi-connectivitybecause the mechanism component's activation is somewhat connected to the space above it.
- Doorsoccupy two spaces, one above the other, and anything that activates either space also activates the other.


### Redstone block updates
Block updates are how most redstone compenents "tell" each other that they need to change states.




























































Two blocks by taxicab distance
When a change occurs somewhere in a redstone circuit, it can produce other changes in surrounding blocks in what is called a block update. Each of these changes can then produce other changes in their surrounding blocks. The update will propagate following the redstone circuit rules within loaded chunks (block updates will not propagate into unloaded chunks), usually very quickly. Note: in Bedrock Edition, block updates and redstone are not connected.

A block update simply notifies other Redstone components and blocks that a change has occurred nearby and allows them to change their own state in response, but not all updates will necessarily require changes. For example, if a redstone torch activates and updates the dust below it, the dust may already be powered from something else, in which case the dust won't change state and the update propagation will stop there.

Block updates can also be generated by any immediate neighbor block being placed, moved, or destroyed.

Solid blocks don't "know" if they're powered or not. Block updates simply update enough blocks around a redstone component to update other redstone components around the solid block (for example, a pressure plate updates its neighbors and the neighbors of the block it's attached to, which includes the space under that block which might be redstone dust).

In addition to block updates, comparators can be updated by containers (including detector rails with container minecarts on them) and certain other blocks, up to two blocks away horizontally when their state changes (for example, when their inventory changes). This is known as a comparator update.

The following redstone components produce block updates up to two blocks away by taxicab distance, including up and down:

- Redstone Dust(All directions)
- Redstone Torch(Up and down)
- Flat and slantedrails,activator rails,detector rails, andpowered rails(Up and down if slanted, down only otherwise)































Neighbors of component and of attachment block
The following redstone components produce block updates in their immediate neighbors, including above and below, and in the immediate neighbors of the block they're attached to:

- Redstone Repeater(as if "attached" to the block it is facing)
- Redstone Comparator(as if "attached" to the block it is facing)
- Buttons
- Detector Rail(flat only; also produces comparator updates)
- Lever
- Pressure Plates
- Trapped Chest(as if "attached" to the block beneath; also produces comparator updates)
- Tripwire Hook
- Weighted Pressure Plates
- Observer

























Immediate neighbors
The following redstone components update only their immediate neighbors when they change their state, including above and below:

- Daylight Detector
- Inverted Daylight Detector(the Inverted Daylight Detector is not obtainable as anitem)
- Note Block
- Leaves
- Scaffolding

This is an XOR gate.
- Tripwire(can also activate tripwire hooks in valid tripwire circuit)
- Pistonand Sticky Piston (from both the piston base and the piston head when extended

The following redstone components do not produce block updates when they change their state (though any block will produce a block update in its immediate neighbors if moved or destroyed):

- Impulse Command Block(also produces comparator updates)
- Repeating Command Block(also produces comparator updates)
- Chain Command Block(also produces comparator updates)
- Dispenser(also produces comparator updates)
- Dropper(also produces comparator updates)
- Doors
- Fence Gates(can be moved)
- Hopper(also produces comparator updates)
- Redstone Lamp(can be moved)
- Trapdoors(can be moved)

