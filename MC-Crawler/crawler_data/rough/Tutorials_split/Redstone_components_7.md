###  Minecart with chest
Main article: Minecart with Chest
A minecart with chest (a.k.a. chest minecart, storage minecart) is used to store and transport items over rails.

** Behavior **
A minecart with chest accepts items from a hopper and allows a hopper underneath it to pull items from it.
###  Minecart with command block
Main article: Minecart with Command Block
A minecart with command block (a.k.a. command minecart, command block minecart) is used to execute commands.

** Behavior **
A minecart with command block executes its command every 2 redstone ticks while on anactivator rail.
###  Minecart with furnace
Main article: Minecart with Furnace
A minecart with furnace‌[Java Edition  only] (a.k.a. furnace minecart, powered minecart) is used to push other minecarts over rails.

** Behavior **
A minecart with furnace propels itself and other minecarts without requiring powered rails.
** Activation **
A minecart with furnace can be activated by pressing theusekey while facing the minecart with furnace and holding fuel (coal, lava, wood, etc.). It continues to move until the fuel runs out.
###  Minecart with hopper
Main article: Minecart with Hopper
A minecart with hopper (a.k.a. hopper minecart) is used to collect, transport, and distribute items over rails.

** Behavior **
A minecart with hopper pulls items from containers above it and push items intohoppersbelow it (the number of items transferred can depend on how long its velocity allows it to remain within reach of the containers). It also picks up items that have fallen on the rails. If a minecart with hopper passes over a powered activator rail, it stops transferring items indefinitely until it passes over an unpowered activator rail.
###  Minecart with TNT
Main article: Minecart with TNT
A minecart with TNT (a.k.a. TNT minecart) is used to create explosions.

** Behavior **
A minecart with TNT that passes over a powered activator rail explodes.
## Miscellaneous components
###  Powering opaque blocks
An opaque block can be powered differently (in this case, a Redstone Lamp). From top to bottom: Strongly powered: powers both Repeater and Dust. Weakly powered: powers Repeater, but not Dust. Not powered: powers neither.
Opaque blocks obstruct light and vision (with some exceptions: for example, glowstone is not considered an opaque block).

Opaque blocks are used to support redstone components and to transmit power.

** Strongly powered vs. weakly powered **
An opaque block is strongly powered by an active power component (except ablock of redstoneor adaylight detector), an activeredstone repeater, or an activeredstone comparator.
An opaque block is weakly poweredonlyby poweredredstone duston top of it, or pointing to it.
** Effect **
A powered opaque block turns OFF any attachedredstone torch, turns ON any adjacentredstone repeaterorredstone comparatorfacing away from it, and activates any adjacent mechanism component.
A strongly-powered opaque block turns ON any adjacent redstone dust, including redstone dust beneath or on top of the opaque block; but a weakly-powered opaque block does not.
###  Use of transparent blocks
Properties of some transparent blocks.
Transparent blocks either can be seen through fully (for example, glass) or partially (for example, stairs), or allow light to pass through (for example, leaves).

Transparent blocks cannot be powered, but can be used as insulators in compact circuits. Some transparent blocks have special properties that make them useful in redstone circuits:

**  Fences **
Main article: Fence
Aredstone torchor apressure platecan be attached to thetopof a fence or nether brick fence.
**  Glass **
Main article: Glass
Glass does not affect how redstone components can be placed on it, but neither receives nor transmits power.
**  Glowstone **
Main article: Glowstone
Glowstone behaves as an opaque block as it does not effect how redstone components can be placed on it.
Redstone dust on top of glowstone cannot transmit power diagonally downward to other redstone dust. Because glowstone is not opaque, it cannot power an adjacent block (including an attached trapdoor), but redstone dust on top of it can.
**  Slabs and Stairs **
Main articles: Slab and Stairs
Any redstone component that can be attached or placed on an opaque block can also be attached or placed on an upside-down slab or upside-down stairs.
Redstone dust on top of an upside-down slab or upside-down stairs cannot transmit power diagonally downward to other redstone dust. Because slabs and stairs are not opaque, they cannot be powered by power components and cannot provide power to adjacent blocks.
**  Walls **
Main article: Wall
Aredstone torchcan be attached to thetopof a wall. Walls change states when a block is moved to or away from a wall, and this output can be detected using observers.

