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


