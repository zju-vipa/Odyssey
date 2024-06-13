# Redstone Repeater
A redstone repeater is a block that produces a full-strength redstone signal from its front while its back is powered, with four toggleable delay settings. It can also be locked into its current power state by directly powering its side with another repeater or a redstone comparator.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
- 2 Usage
	- 2.1 Signal transmission
	- 2.2 Signal repeating
	- 2.3 Signal delay
	- 2.4 Signal direction
	- 2.5 Signal locking
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 Video
- 6 History
	- 6.1 Redstone repeater "items"
		- 6.1.1 Appearances
			- 6.1.1.1 Unpowered Repeater
			- 6.1.1.2 Powered Repeater
		- 6.1.2 Names
			- 6.1.2.1 Unpowered Repeater
			- 6.1.2.2 Powered Repeater
- 7 Issues
- 8 Trivia
- 9 Gallery
	- 9.1 Renders
		- 9.1.1 Java Edition
		- 9.1.2 Bedrock Edition
		- 9.1.3 Contraption
	- 9.2 Screenshots
	- 9.3 In other media
- 10 References

## Obtaining
### Breaking
A redstone repeater can be broken instantly using any tool, or without a tool, and drops itself as an item. To remove a redstone repeater, mine it.

A redstone repeater is removed and drops as an item if:

- its attachment block is moved, removed, or destroyed;
- waterorlavaflows into its space;‌[Java Edition  only]
- apistontries to push it or moves a block into its space.

### Natural generation
A redstone repeater generated in the jungle temple's hidden room.
A single redstone repeater is generated naturally in each jungle temple.

They also generate in ancient cities.

### Crafting
| Ingredients                                  | Crafting recipe |
|----------------------------------------------|-----------------|
| Redstone Torch+<br/>Redstone Dust+<br/>Stone |                 |

## Usage
See also: Redstone circuit

A redstone repeater can be used in four different ways: to "repeat" redstone signals back to full strength, delay signals, prevent signals moving backward, or to "lock" signals in one state.

A repeater can be placed only on top of opaque blocks (dirt, stone, etc.), on top of upside-down slabs, upside-down stairs, furnaces, and glass. In Bedrock Edition, a repeater can also be placed on fences and stone walls. They can also be placed on some transparent blocks. See Opacity/Placement for more information. To place a repeater, use the Place Block control.

A redstone repeater has a front and back – the arrow on the top points to the repeater's front. A repeater also has two small redstone torches on its top – the color of the torches indicates whether its output is on (dark red when off, bright red when on) and the distance between them indicates the delay the repeater adds to the signal transmission.

A repeater is 0.125 (1⁄8) blocks high.

### Signal transmission
A repeater transmits signals only from its back to its front, but its behavior can be modified from the side (see signal locking, below).

Different ways to power a repeater
A redstone repeater can be powered by any of the following components at its back:

- an activepower component(redstone torch, lever, block of redstone, etc.)
- poweredredstone dust
- a poweredredstone comparatoror another powered redstone repeater facing the repeater
- a powered opaque block (including any opaquemechanism components, such asdispensers,redstone lamps, etc.)

A redstone repeater can power any of the following components at its front:

- redstone dust
- a redstone comparator or another redstone repeater facing away from the repeater
- any opaque block (including any opaquemechanism components)

A redstone repeater can activate any mechanism component it is facing.

An opaque block powered by a redstone repeater is called "strongly-powered" (as opposed to an opaque block "weakly-powered" by redstone dust). A strongly-powered opaque block can power adjacent redstone dust, as well as other redstone components.

### Signal repeating
See also: Transmission circuit § Repeater

A redstone repeater can "repeat" a redstone signal, boosting it back up to power level 15.

Redstone signals have a maximum power level of 15 and that level drops by 1 for every block of redstone dust the signal travels through. If a signal must travel through more than 15 blocks of redstone dust, a redstone repeater can be used to boost the signal back up to full strength. An extra two blocks of distance can be achieved by placing solid opaque blocks before and after the repeater.

While redstone repeaters can allow signals to travel great distances, each always adds some delay to the transmission since the minimum amount of delay is 1 redstone tick (0.1 seconds, barring lag).

