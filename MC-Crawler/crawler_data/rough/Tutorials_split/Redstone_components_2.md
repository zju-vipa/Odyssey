###  Sculk sensor
A sculk sensor emits a redstone signal when it detects a vibration

###  Target























Target's range of activationIt does not power any adjacent opaque block
Main article: Target
A Target emits a redstone signal when hit by a projectile (including arrows, tridents, eggs, snowballs, splash potions, fire charges fired from dispensers, and lingering potions, but excluding ender pearls and eyes of ender).

** Activation **
Arrows and Tridents emit a pulse of 10 redstone ticks, while other projectiles emit a pulse of 4 redstone ticks. The closer the projectile is to the center of the block, the stronger the signal it produces is, from 1 (at the edge) to 15 (in the center).
###  Trapped chest



















P.












Trapped Chest's range of activationIt powers the opaque block beneath it
Main article: Trapped Chest
A trapped chest can be used to detect when a player tries to take from it.

** Activation **
A trapped chest is turned ON when a player accesses its contents.
** Effect **
While activated, a trapped chest and any opaque block beneath it both power adjacent redstone dust (including beneath the block), and all adjacent mechanism components (including those above or below it). They also activate all adjacent redstone comparators or redstone repeaters facing away from it, at a power level equal to the number of players simultaneously accessing its contents (maximum 15).
###  Tripwire hook
















P.














x

x



Tripwire Hook's range of activationIt powers the opaque block it is attached to
Main article: Tripwire Hook
Tripwire hook as power component – The tripwire hooks and the blocks they are attached to provide power, but the tripwire does not.
A tripwire hook is used to detect mobs, items, and other entities over a large area.

** Placement **
A tripwire hook can be attached to thesideof mostopaqueblocks. If the attachment block is removed, the tripwire hook drops as an item.
In order to function correctly, a tripwire hook must be part of a tripwire circuit: two opaque blocks attached to tripwire hooks, at the ends of a tripwire line (one or more blocks oftripwire).
To place tripwire, right-click on an adjacent block with astring. Tripwire can be placed on the ground or in the air, and forms a valid tripwire line only if all the tripwire is of the same type. Tripwire is considered on the ground if placed on any opaque block, or on a block of redstone, a hopper, an upside-down slab, or an upside-down stairs. Tripwire is considered in the air if placed on or above any other block. Tripwire on the ground has a short hitbox (1/8 block tall), while tripwire in the air has a taller hitbox (1/2 block tall).
If the attachment block under ground tripwire is removed, the tripwire drops as string.
A tripwire circuit is properly placed when the tripwire hooks are fully extended and the tripwire line runs continuously between the tripwire hooks. Tripwire lines from separate tripwire circuits can be placed next to each other (in parallel), above each other, and can even intersect each other.
** Activation **
A tripwire hook turns ON when anentity(mob, item, etc.) crosses or falls on the hook's tripwire line (butnotthe tripwire hook), and turns OFF when all entities leave or are removed from the tripwire line. A tripwire hook also turns ON for 5 ticks (1/2 second) when any of its tripwires are destroyed, except when usingshearsto cut the tripwire. Breaking the tripwire hook, or its attachment block, does not generate a pulse.
** Effect **
While activated, a tripwire hook and its attachment block both power any adjacent redstone dust (including below the tripwire hook, or beneath or above the block), and all adjacent mechanism components (including those above or below it). They also activate all adjacent redstone comparators or redstone repeaters facing away from it.
Tripwire itself provides no power.
##  Transmission components
Transmission components propagate signals and pulses from power components to mechanism components. Complex effects can also be produced by allowing a signal to affect itself or its circuit.

###  Redstone dust
















w.




w.

w.
















Redstone Dust's range of activationIt weakly powers the opaque blocks beneath it and it points to
Redstone dust as redstone component
Redstone dust transmits power.

Main article: Redstone Dust § Redstone component
** Placement **
Redstone dust is placed by right-clicking withredstone dust. Redstone dust can be attached to thetopof anyopaqueblock, or to thetopofglowstone, an upside-downslabor upside-downstairs. If the attachment block is removed, the redstone dust drops as an item.
When placed, redstone dust configures itself to point toward adjacent redstone dust (at the same level or one level up or down), correctly-facingredstone repeatersandredstone comparators, and power components. If there is only one such neighbor, redstone dust forms a line pointing toward and away from that one neighbor (which can cause it to point toward blocks it wouldn't normally point toward). If there are multiple such neighbors, redstone dust forms either a line, an "L", a "T", or a "+". If there are no such neighbors, redstone dust forms a large directionless dot. Redstone dust does not automatically configure itself to point toward adjacent mechanism components, it must be arranged to do so.
When two redstone dust trails are placed vertically diagonally (one block over and one up, or one over and one down), the lower dust trail appears to crawl up the side of the higher block to join the other dust. This linking can be cut by an opaque block above the lower trail, which prevents the two trails from connecting. If the higher trail is on an upside-down slab or upside-down stairs, the higher trail configures itself to point toward the lower trail (and other adjacent dust), but the lower trail (although visually) does not configure itself to point toward the higher trail (including not appearing to crawl up the side of the slab or stairs).
The directions in which redstone dust configures itself can affect whether it powers adjacent opaque blocks and mechanisms.
** Activation **
Redstone dust can be turned ON by any adjacent power component, redstone repeater pointing at it, or strongly-powered opaque block. Redstone dust can also be turned ON by other adjacent powered redstone dust, but the power decreases with distance from a strongly-powered block. Redstone dust transmits power up to 15 blocks away.
Redstone dust can transmit power diagonally upward to dust on an upside-down slab or upside-down stairs, but not diagonally downward from an upside-down slab or upside-down stairs.
** Effect **
Powered redstone dust turns ON any mechanism component it is configured to point at. It powers, weakly, an opaque block that it lies on or points to.
