# Tutorials/Quasi-connectivity
Quasi-connectivity is a property of dispensers, droppers, and pistons that allows them to be activated by anything that would activate the space above them, no matter what is actually in that space. While quasi-connectivity can be difficult to work around sometimes and might seem like a bug, it was a bug, but now it  is officially recognized as a feature that "works as intended" and does make some builds much easier (for example, piston walls).

"Quasi-connectivity" means the block's activation is quasi-connected to the space above itself ("quasi-" means "seemingly" or "apparently"). Quasi-connectivity can be abbreviated as QC. Other terms used for this property include "connectivity", "piston connectivity" (as the property originated with pistons), "indirect power" (but that term is also sometimes used for activating mechanism components with an adjacent powered block), and "BUD-powered" (although quasi-connectivity and block update detectors are not synonymous).

Rather than repeating "dispensers, droppers, and pistons", this tutorial discusses only pistons, but everything discussed here applies to dispensers and droppers as well.

## Contents
- 1 Activation by normal methods
- 2 Activation by quasi-connectivity
	- 2.1 Immediate QC activation
	- 2.2 Update QC activation
- 3 Benefits of quasi-connectivity
	- 3.1 More activation options
	- 3.2 Remote activation
	- 3.3 Block update detectors
	- 3.4 Torch keys
	- 3.5 Floating button
- 4 Drawbacks of quasi-connectivity
	- 4.1 Workarounds

## Activation by normal methods
Activation of Mechanism Components — Mechanism components can be activated by power components (for example, redstone torches), powered blocks, redstone dust, repeaters, and comparators (not shown), but only if configured correctly.
Before discussing activation by quasi-connectivity, let's review more general methods of activation.

Mechanism components (pistons, doors, redstone lamps, etc.) can be activated, which causes the mechanism component to do something (push a block, open the door, turn on, etc.). Most Minecrafters would just say they are "powered", but it can be useful to distinguish powered and activated.

All mechanism components are activated by:

- an adjacent activepower component, including above or below

Exceptions:a redstone torch does not activate a mechanism component it is attached to, and a piston is not activated by a power component directly in front of it
Examples:Redstone torches don't power blocks that aren't above them, but can activate mechanism components in any space next to them. Levers and buttons don't power blocks they aren't attached to, but can activate mechanism components in any space next to them.
- an adjacentpowered opaque block(either strongly-powered or weakly-powered), including above or below

- a poweredredstone comparatororredstone repeaterfacing the mechanism component

- poweredredstone dustconfigured to point at the mechanism component (or on top of it, for mechanism components that can support redstone dust, butnotbeneath it), or adjacent "directionless" redstone dust; a mechanism component isnotactivated by adjacent powered redstone dust that is not configured to point at it.


## Activation by quasi-connectivity





















Quasi-Connectivity — Anything that would activate the lamp can also activate the piston, even if the lamp isn't there.
In addition to the normal methods of activation described above, pistons can also be activated if one of the methods above would activate a mechanism component in the space above the piston, even if there is no mechanism component there (even if the block above the component is air or a transparent block).

Another way to look at it is that pistons have an activation "shape"/"hitbox" similar to doors. Anything that activates the top of a door also activates the bottom of the door, and anything that activates the space above a piston also activates the piston.

This method of activation is known as "quasi-connectivity" (QC) and is often simplified to saying that pistons can be powered by blocks diagonally above or two blocks above, but other methods of such activation exist (described below).



















The Update Problem — The lever can activate the piston by quasi-connectivity, but is too far away to update the piston when it changes.
Where quasi-connectivity gets complicated is that it can cause states where a piston should be activated by QC … but doesn't know it. When redstone components change their state, they update other redstone component around them of the change so that they can update their state in response (for example, when a lever turns on, it updates nearby components that they should now be powered or activated). However, redstone components only update other blocks a maximum of two spaces away, but quasi-connectivity can create situations where a piston should be activated from a redstone component three spaces away. For example, a redstone component powering a block next to the space above a piston—the redstone component can activate the piston by QC but is three spaces away so does not provide an update to the piston.

Because of this update problem, some methods of activation by quasi-connectivity  ("QC activation", for short) update the piston immediately ("immediate QC activation"), while others put the piston into a state where it should be activated but doesn't know it yet, so it waits to activate until it is updated ("update QC activation").


### Immediate QC activation
Immediate QC activation is the activation of a piston by quasi-connectivity that occurs immediately and doesn't require the piston to be separately updated. This only works with redstone components that can update other redstone components two blocks away from them.

** Two blocks by taxicab distance **



























































Two blocks by taxicab distance
The following redstone components canactivatemechanism components one block away, butupdateall redstone components up to two blocks away (bytaxicab distance):
- Redstone Comparator
- Redstone Dust
- Redstone Repeater
- Redstone Torch

This means that when these redstone components activate the space above a piston (one block away), they also simultaneously update the piston as well (two blocks away). Redstone comparators and repeaters can only activate mechanism components adjacent to themselves horizontally, but redstone dust and torches can also activate mechanism components below themselves as well (redstone torches can also activate above, but that doesn't help for QC activation).


















Immediate QC Activation by Redstone Comparator — The piston activates immediately when the redstone comparator turns on.






























Immediate QC Activation by Redstone Dust — Both pistons activate immediately when the redstone dust turns on (we're not using a solid block under the dust because its powering would activate the pistons directly).

















Immediate QC Activation by Redstone Repeater — The piston activates immediately when the redstone repeater turns on.






























Immediate QC Activation by Redstone Torch — Both pistons activate immediately when the redstone torch turns on.

** Neighbors of component and of attachment block **
































Neighbors of component and of attachment block
The following redstone components canactivatemechanism components one block away, andupdateredstone components adjacent to the block they are attached to (including above and below) as well as redstone components adjacent to themselves:
- Buttons(attaches in any direction)
- Detector Rail(attaches only downward)
- Lever(attaches in any direction)
- Pressure Plates(attaches only downward)
- Trapped Chest(doesn't actually attach, but updates as if attached to block beneath)
- Tripwire Hook(attaches only sideways)
- Weighted Pressure Plates(attaches only downward)

This means that when these redstone components are attached to a block beneath them, they can activate the space above a piston (one block away), and also simultaneously update the piston as well (two blocks away). A trapped chest updates redstone components adjacent to the space beneath it, but doesn't need to be attached to any block (for example, like a pressure plate) — the other examples below use an upside-down slab instead of a block because a powered block would activate the pistons directly. A tripwire hook cannot be attached to a block beneath itself so cannot be used for immediate QC activation.



















Immediate QC Activation by Button — Both pistons activate immediately when the button gets pressed.


















Immediate QC Activation by Detector Rail — Both pistons activate immediately when the detector rail gets activated by a minecart.


















Immediate QC Activation by Lever — Both pistons activate immediately when the lever gets switched on.


















Immediate QC Activation by Pressure Plate — Both pistons activate immediately when the pressure plate gets stepped on. Also works with weighted pressure plates.


















Immediate QC Activation by Trapped Chest — Both pistons activate immediately when the trapped chest gets opened.

Other redstone components cannot update redstone components more than one block away so cannot be used for immediate QC activation, only for update QC activation.

