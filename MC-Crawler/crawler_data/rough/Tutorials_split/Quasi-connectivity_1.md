### Update QC activation
Update QC activation is the act of putting a piston into a state where it should activate by quasi-connectivity, but it hasn't received a redstone update so doesn't know it should activate — it then waits to activate until it receives an update.

Pistons can be updated in a number of ways:

- placing or destroying a block next to a piston
- moving a block next to a piston
- changing the state of some blocks next to a piston (for example, changing the delay on a repeater)
- changing some states of some redstone components within two spaces of a piston:
	- changing the state of a redstone torch within two spaces of a piston
	- changing the power level (but not the orientation) of redstone dust within two spaces of a piston
	- changing the power level (but not the delay) of a repeater facing a space next to a piston
	- changing the power level or changing the operating mode of a comparator facing a space next to a piston

** Powered block **
A powered block*can activate the space above a piston, from the side or from above, without updating the piston, producing an update QC activation:












*


















Update QC Activation by Button-Powered Block — When either button is pressed, neither piston activates unless updated before the button pops out.







*






















Update QC Activation by Comparator-Powered Block — Neither piston activates until updated.








*














Update QC Activation by Detector Rail-Powered Block — When the detector rail is activated, neither piston activates until updated.







*






*
























Update QC Activation by Dust-Powered Block — None of the pistons activate until updated.












*


















Update QC Activation by Lever-Powered Block — When either lever is activated, neither piston activates until updated.








*














Update QC Activation by Pressure Plate-Powered Block — When the pressure plate is activated, neither piston activates until updated.







*






















Update QC Activation by Repeater-Powered Block — Neither piston activates until updated.








*














Update QC Activation by Trapped Chest-Powered Block — When the trapped chest is activated, neither piston activates until updated.

Ablock of redstoneacts like a powered block but can't be turned off, so the only way it can activate or deactivate pistons by quasi-connectivity is if it is moved into or out of a position where it would activate the space above the piston, either from the side or from above.























































Update QC Activation by Block of Redstone — Neither of the bottom two pistons activate until updated.

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

Of these redstone components, only buttons, levers, and tripwire hooks can attach sideways so can be used to produce an update QC activation. The others can be attached to a block beneath them, but then it's the block creating the update QC activation (described above).
























Update QC Activation by Button — When the button is activated, neither piston activates unless updated before the button pops out.
























Update QC Activation by Lever — When the lever is activated, neither piston activates until updated.




































Update QC Activation by Tripwire Hook — When the tripwire hook is activated, neither piston activates until updated.

** Immediate neighbors **
























Immediate neighbors
The following redstone components update only their immediate neighbors when they change their state, including above and below:
- Activator Rail
- Daylight Detector
- Tripwire(can also activate tripwire hooks in valid tripwire circuit)
- Pistonand Sticky Piston (from both the piston base and the piston head when extended)
- Powered Rail
- Rail

Of these redstone components, only a daylight sensor can activate the space above a piston and thus can be used to produce an update QC activation.
























Update QC Activation by Daylight Sensor — When the daylight sensor is activated, neither piston activates until updated.

The redstone components that cannot be used to put a piston into a QC activation may still be useful for updating them. For example, a tripwire updates adjacent blocks when an entity moves into or out of its space, and activator rails and powered rails are useful in that they update adjacent blocks when activated or deactivated (thus updates can be controlled with redstone without directly powering neighbors).

## Benefits of quasi-connectivity
Although somewhat difficult to understand, quasi-connectivity does offer many benefits.

### More activation options
Because a piston can be activated in its own space or the space above it, there are simply more options when figuring out how to activate it.

### Remote activation
Because a piston can be activated by anything that would activate the space above it, pistons can be activated from two spaces away while most redstone components can only be activated from one space away.

### Block update detectors
Main article: Tutorials/Block update detector
Update QC activation can be used to create a block update detector: a redstone circuit that is triggered by a block update rather than a redstone power input.

A piston activated by quasi-connectivity is sometimes described as "BUD-powered". However, quasi-connectivity and block update detectors (BUDs) are neither synonymous nor even subsets of each other. There are methods of QC activation that do not produce block update detectors (for example, any immediate QC activation method) and there are block update detectors that do not depend on quasi-connectivity (for example, stuck-piston BUDs).

