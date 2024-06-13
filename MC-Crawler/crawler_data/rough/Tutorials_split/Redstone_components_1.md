###  Jukebox
A jukebox with a music disc playing emits a redstone signal of strength 15.

###  Lectern



















P.












Lectern's range of activationIt powers the opaque block beneath it
Main article: Lectern
A lectern is a block that can hold written books so they can be read.

** Placement **
Lecterns can face north, south, east or west, facing toward the player when placed. This has a redstone effect judging on the book page.
** Activation **
When the page of the book it is holding is turned, the lectern emits a redstone pulse that is one game tick long (0.5 redstone ticks).
###  Lever














P.
















Lever's range of activationIt powers the opaque block it is attached to
Main article: Lever
Lever as power component
A lever is used to switch circuits on or off, or to permanently power a block.

** Placement **
A lever can be attached to any part of mostopaqueblocks, or to thetopof an upside-downslabor upside-downstairs. If the attachment block is removed, the lever drops as an item.
** Activation **
A player can turn a lever ON or OFF by right-clicking it.
** Effect **
While activated, a lever and its attachment block (unless attached to a slab or stairs) both power adjacent redstone dust (including beneath the lever, or beneath or on top of the block), and all adjacent mechanism components (including those above or below it). They also activate all adjacent redstone comparators or redstone repeaters facing away.


###  Lightning rod












ro






P.












Lightning Rod's range of activationIt powers the opaque block it is attached to
A lightning rod emits a redstone signal strength of 15 when struck by lightning.



### Observer














P.
















Observer's range of activationIt does not activate adjacent componentsIt powers the opaque block behind it
Main article: Observer
An observer can be used to detect block changes.

** Placement **
An observer can be placed anywhere and can face in any direction, including up or down. When placed, the observer's side that detects block changes (its face) faces away from the player and the side that produces a pulse faces the player.
** Activation **
An observer turns ON when the block in front of its face changes state (for example, a block being placed or mined, water changing to ice, a repeater having its delay changed by a player, etc.). The observer stays ON for 2 redstone ticks (4 game ticks, or 0.2 seconds barring lag) and then turns OFF automatically.
An observer also turns ON for 1 game ticks after it is moved by apiston.
** Effect **
When activated, an observer produces a 1tick pulse from the side opposite its face.
### Pressure plate



















P.












Pressure Plate's range of activationIt powers the opaque block that supports it
Main article: Pressure Plate
Pressure plate as power component
A pressure plate can be used to detect mobs, items, and other entities. A pressure plate may be of two types: wooden or stone.

** Placement **
A pressure plate can be attached to thetopof anyopaqueblock, or to thetopof afence,nether brick fence, an upside-downslabor upside-downstairs. If the attachment block is removed, the pressure plate drops as an item.
** Activation **
A pressure plate turns ON when anentity(mob, item, etc.) crosses or falls on it, and turns OFF when the entity leaves or is removed. A wooden pressure plate may be turned ON also by falling items andarrowshots. A wooden pressure plate that is activated in this way turns OFF when the object is picked up or despawns (after one minute for a shot arrow, or up to five minutes for an item).
** Effect **
While activated, a pressure plate and its attachment block (unless attached to a fence, nether brick fence, slab, or stairs) both power adjacent redstone dust (including beneath the block), and all adjacent mechanism components (including those above or below). They also activate all adjacent redstone comparators or redstone repeaters facing away.
** Considerations **
A pressure plate is not solid (it cannot be used as a wall or platform). Usually a block under a pressure plate provides solid ground (for mobs to walk across, items to fall on, etc.), but when a pressure plate is placed on a block with a small collision mask, like a fence or nether brick fence, it is possible for entities to move through the pressure plate and still activate it. Thus, a pressure plate on a fence can be used to detect entities without stopping them (more compactly than a tripwire circuit).
###  Redstone torch




















P.







P.












x








x













Redstone Torch's range of activationIt powers the opaque block that is above itIt does not power/activate the block/component it is attached to
Main article: Redstone Torch
Redstone torch as power component
A redstone torch powers circuits (horizontally and vertically), and can invert signals.

** Placement **
A redstone torch can be attached to any surface (except the bottom) of anyopaqueblock, or to thetopof: acobblestone wall, afence,glass,nether brick fence, an upside-downslabor upside-downstairs. If the attachment block is removed, the redstone torch drops as an item.
** Activation **
A redstone torch turns OFF when its attachment block receives power from another source and turns back on when the block loses power.
** Effect **
While activated, a redstone torch and any opaque block above it both power adjacent redstone dust (including beneath the redstone torch, or on top of the block), and all adjacent mechanism components (including those above or below it). They also activate all adjacent redstone comparators or redstone repeaters facing away from it.
A redstone torch does not affect the block it is attached to (even if it is a mechanism component).
** Considerations **
A redstone torch can burn out (stop turning on) when it is forced to flicker on and off too quickly (by powering and de-powering its attachment block). After burning out, a redstone torch re-lights when it receives a redstone update, or randomly after a short time.
One way to cause a burnout is with ashort-circuit– using a torch to turn itself off, which then allows the torch to turn back on, etc. For example, placing redstone dust on top of a block with a redstone torch on its side, then putting another block above the torch, causes the torch to power the top block, which activates the dust, which powers the first block, turning the torch off – this feedback loop causes the redstone torch to flicker and burn out. When putting a torch underneath a block, make sure that the block isn't adjacent to redstone dust or the torch can burn out.
