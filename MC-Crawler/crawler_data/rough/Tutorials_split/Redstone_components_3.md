###  Redstone repeater
















P.














Redstone Repeater's range of activationIt powers the opaque block it points to
Main article: Redstone Repeater
Redstone repeater as redstone component
A redstone repeater is used to transmit power, strengthen redstone dust signals weakened by distance, delay a signal, and redirect a signal.

** Placement **
A redstone repeater can be attached to thetopof anyopaqueblock, or to thetopof an upside-downslabor upside-downstairs. If the attachment block is removed, the redstone repeater drops as an item.
A redstone repeater is marked with an arrow pointing toward its front. The repeater reacts only to signals from the block behind it and propagates signals only to the block in front of it (in the direction of the arrow). It also has an adjustable delay that can be set from 1 to 4 ticks by right-clicking it.
** Activation **
A redstone repeater is turned ON by any powered component at its back and is unaffected by the powered state of any block beside, above, below, or in front of it (but see below about locking a repeater).
** Effect **
A powered redstone repeater turns ON redstone dust or a mechanism component in front of it, or strongly powers an opaque block in front of it. It has no effect on the blocks under, above, beside, or behind it.
A redstone repeater not only strengthens it for further transmission, it also delays it by 1 to 4 ticks. A redstone repeater also increases the duration of any pulse shorter than its delay to match the duration of its delay.
A redstone repeater can be locked by powering it from the side with another redstone repeater or with aredstone comparator. A locked repeater does not change its output state until unlocked, even if its input changes. A locked repeater displays its locked status with a bedrock bar.
###  Redstone comparator
















P.














Redstone Comparator's range of activationIt powers the opaque block it points to
Main article: Redstone Comparator
A redstone comparator is used to compare or subtract two signals, or to measure how full a container is.

** Placement **
A redstone comparator can be attached to thetopof any opaque block, or to thetopof an upside-downslabor upside-downstairs. If the attachment block is removed, the redstone comparator drops as an item.
A redstone comparator is marked with an arrow that point toward itsfront. The comparator takes a signal from its back as its input, and outputs a signal to the block in front of it, but can also be affected by signals from its sides (see below).
|  |
|--|
|  |

A redstone comparator has twomodes. Right-clicking it toggles between comparison mode (front torch down/off) and subtraction mode (front torch up/on).
** Activation **
A redstone comparator is turned ON by a power source at its input or a power source separated by one opaque block from its input. Power sources include any powered component, a non-empty container, a container minecart on a detector rail, acommand blockthat has run its last command successfully, acauldroncontaining water, anend portal framewith aneye of ender, or ajukeboxwith amusic disc. Either at its back or separated from its back by an opaque block. It is not affected by blocks beneath it or above it, but its signal strength can be modified by signals from its sides (see below).
** Effect **
A powered redstone comparator turns ON redstone dust, a properly-facing redstone comparator or redstone repeater, or a mechanism component in front of it; or strongly powers an opaque block in front of it – all at the same power level as its input signal (unless modified by a side signal, see below). It has no effect on blocks in other adjacent positions (including the block beneath it).
The output of a redstone comparator can be affected by a signal provided from its side by a transmission component (redstone dust, redstone repeater, or another redstone comparator only):
- Incomparison mode, a redstone comparator propagates its input signal only if the input signal is greater than the side signal, and outputs no signal if not.
- Insubtraction mode, a redstone comparator outputs a power level equal to the difference of the power level of the input signal minus the power level of the side signal.

A redstone comparator that is activated by a container outputs a power level in proportion to how full the container is (rounded up, so a single item in a container produces a power level of at least 1). A container's fullness is measured by stacks: for example, a singleshovel(a non-stackable item), 16signs, or 64sticksare all considered to be equivalent, full stacks.
TheComparator Output Table(right) shows the minimum stacks ("s") plus items ("i") required to produce a specific power level from a container. For example, to get power level 5 from a hopper, put 1 stack plus 28 items in the hopper. Divide items by 4 and round up for items with a stack maximum of 16. The values for the chest, dispenser, furnace and hopper apply to minecarts with those components as well (when on adetector rail).
Some blocks (such ascrafting tables,enchantment tables, etc.) can hold items temporarily while the player uses the block's interface – the items are returned to the player if the player exits the interface with items still inside. Other blocks (such asbeacons) only consume items. Putting items in these blocks never activates a redstone comparator.

##  Mechanism components
Mechanism components are blocks that react to redstone power by affecting the environment – by moving themselves or other entities, by producing light, sound, or explosions, etc.

Activating a mechanism component (in this case, a redstone lamp)
** Activation **
Mechanism components are turned on by:
- an adjacent active power component (Exceptions:a redstone torch does not activate a mechanism component it is attached to, and a piston is activated only by a power component directly in front of it if the component is connected to it.)
- an adjacent powered opaque block (strongly-powered or weakly-powered)
- a poweredredstone repeaterorredstone comparatorfacing the mechanism component
- poweredredstone dustconfigured to point toward the mechanism component (or on top of it, for opaque mechanism components); a mechanism component isnotturned ON by adjacent powered redstone dust that is not configured to point toward it.

Activating a piston by quasi-connectivity – Note that the piston on the left is not powered by quasi-connectivity because the redstone dust is running past the block above the piston, rather than directly into it, and thus would not power a mechanism there)
**  Quasi-Connectivity **

  

This feature is exclusive to  Java Edition. 


In addition to the methods above,pistons,dispensers, anddropperscan also be turned ON if a block above it receives a block update (including a redstone update within two blocks of the component) and is powered by any of the above means, even without a mechanism component (e.g.; even if the block above the component isairor a transparent block). This rule is often simplified to say that the components can be powered by blocks diagonally above or two blocks above, however other methods of activation by connectivity exist (see image to the right). This method of activation is also known as "connectivity", "piston connectivity" (as it originated with pistons), or simply "indirect power".

Activated vs. Powered – The top lamp is both activated (the lamp is on) and powered (it can power the repeater), while the bottom lamp is activated, but not powered.
**  Activated vs. Powered **
For opaque mechanism components (command blocks, droppers, dispensers, note blocks and redstone lamps), it's important to make a distinction between a mechanism component beingactivated(so that it performs an action) and beingpowered(so that a redstone signal could be drawn from it by a transmission component). Any method of powering a mechanism component (such as a redstone torch underneath it) also activates it, but some activation methods (such as a redstone torch next to or above a mechanism component) does not actually power the component (following the usual rules for power components).

