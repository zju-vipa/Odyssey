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
| Ingredients                        | Crafting recipe |
|------------------------------------|-----------------|
| Redstone Torch+Redstone Dust+Stone |                 |

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

### Signal delay
When initially placed, a redstone repeater has a delay of one redstone tick (equivalent to two game ticks, or 0.1 seconds barring lag).

A repeater's delay can be modified by using the Use Item control. Each use increases the repeater's delay by one redstone tick, to a maximum of four redstone ticks, then back to one redstone tick. Longer delays can be made with multiple repeaters – for example, a repeater set to 'four' and another to 'one' provides a half-second delay (0.4s + 0.1s = 0.5s).

A repeater set to a delay of two to four redstone ticks increases the length of any shorter on-pulse to match the length of the repeater's delay, and suppress any shorter off-pulse. For example, a repeater set to a 4-tick delay changes a 1-tick, 2-tick, or 3-tick on-pulse into a 4-tick on-pulse, and does not allow through any off-pulse shorter than 4 ticks.

Although a repeater cannot be set to have a delay of zero, instant repeater circuits are possible (circuits that repeat a signal with no delay).

In Bedrock Edition, the first repeater have a delay of zero but the repeater is still showing 1-tick.[more information needed]

###  Signal direction
See also: Mechanics/Redstone/Transmission circuit § Diode

A redstone repeater acts as a diode – it allows redstone signals through in one direction (unlike redstone dust or opaque blocks that can transmit redstone signals in any direction).

A diode can be used to protect a redstone circuit from redstone signals feeding back into the circuit from its output, or can be used to isolate one part of a circuit from another.

###  Signal locking
See also: Mechanics/Redstone/Memory circuit

The left repeater has been locked in an unpowered output state by the right repeater.
A redstone repeater can be "locked" by another powered redstone repeater facing its side. When locked, the repeater does not change its output (whether powered or unpowered), no matter what the input does. When the side repeater turns back off, the repeater returns to its normal behavior.

A repeater can also be locked by a powered redstone comparator facing its side. This offers additional possibilities for locking signals because a comparator's output can be affected from 3 sides as well as by containers.

If a repeater is locked again too quickly after unlocking (e.g. the lock is controlled by a fast clock circuit), or the lock and the input are changed only on the same tick (e.g. because they're fed by the same clock and both repeaters have the same delay), the repeater does not switch states.

## Data values
### ID
Java Edition:

| Name              | Identifier | Form         | Translation key          |
|-------------------|------------|--------------|--------------------------|
| Redstone Repeater | repeater   | Block & Item | block.minecraft.repeater |

Bedrock Edition:

| Redstone Repeater | Identifier         | Numeric ID | Form                         | Item ID[i 1]   | Translation key    |
|-------------------|--------------------|------------|------------------------------|----------------|--------------------|
| Unpowered block   | unpowered_repeater | 93         | Block & Ungiveable Item[i 2] | Identical[i 3] | —                  |
| Powered block     | powered_repeater   | 94         | Block & Ungiveable Item[i 2] | Identical[i 3] | —                  |
| Item              | repeater           | 419        | Item                         | —              | item.repeater.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ a b Unavailable with /give command

↑ a b The block's direct item form has the same id as the block.


### Block states
See also: Block states

Java Edition:

| Name    | Default value | Allowed values     | Description                                                                                                                                 |
|---------|---------------|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| delay   | 1             | 1234               | The redstone repeater's delay in redstone ticks.                                                                                            |
| facing  | north         | eastnorthsouthwest | The direction from theoutputside to theinputside of a repeater.The opposite from the direction the player faces while placing the repeater. |
| locked  | false         | falsetrue          | True if the repeater is currently locked.                                                                                                   |
| powered | false         | falsetrue          | If the redstone repeater is lit.                                                                                                            |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values     | Values forMetadata Bits | Description                                                                                                                                 |
|------------------------------|---------------|---------------|--------------------|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| minecraft:cardinal_direction | Not Supported | south         | eastnorthsouthwest | Unsupported             | The direction from theoutputside to theinputside of a repeater.The opposite from the direction the player faces while placing the repeater. |
| repeater_delay               | 0x40x8        | 0             | 0123               | 0123                    | The redstone repeater's delay in redstone ticks minus 1.                                                                                    |



