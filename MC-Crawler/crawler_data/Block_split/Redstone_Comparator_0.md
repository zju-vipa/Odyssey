# Redstone Comparator
A redstone comparator is a block that can produce a redstone signal from its front by reading chests, lecterns, beehives and similar blocks, or repeat a signal without changing its strength. It can also be set to either stop outputting a signal while its side input is receiving a stronger one (front torch off), or subtract its side input's signal strength from its output (front torch on).

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
- 2 Usage
	- 2.1 Maintain signal strength
	- 2.2 Compare signal strength
	- 2.3 Subtract signal strength
	- 2.4 Measure block state
		- 2.4.1 Fullness of containers
		- 2.4.2 Miscellaneous
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
	- 4.3 Block data
- 5 Advancements
- 6 Video
- 7 History
	- 7.1 Redstone comparator "items"
		- 7.1.1 Appearances
			- 7.1.1.1 Unpowered comparator
			- 7.1.1.2 Powered comparator
		- 7.1.2 Names
			- 7.1.2.1 Unpowered comparator
			- 7.1.2.2 Powered comparator
- 8 Issues
- 9 Trivia
- 10 Gallery
	- 10.1 Screenshots
- 11 References

## Obtaining
### Breaking
A redstone comparator can be broken instantly with any tool, or by hand, and drops itself as an item.

| Block    | Redstone Comparator |
|----------|---------------------|
| Hardness | 0                   |
|          | Breakingtime (secs) |
| Default  | 0.05                |

A redstone comparator is removed and dropped as an item if:

- its attachment block is moved, removed, or destroyed;
- waterflows into its space;‌[Java Edition  only]
- apistontries to push it or moves a block into its space.

If lava flows into a redstone comparator's space, the redstone comparator is destroyed without dropping as an item.

### Natural generation
Redstone comparators generate in ancient cities.

### Crafting
| Ingredients                        | Crafting recipe |
|------------------------------------|-----------------|
| Redstone Torch+Nether Quartz+Stone |                 |

## Usage
A redstone comparator can be placed on the top of any opaque block with a solid full-height top surface (including upside-down slabs and upside-down stairs). In Bedrock Edition, a comparator can also be placed on walls and fences. For more information about placement on transparent blocks, see Opacity/Placement.

The redstone comparator has a front and a back — the arrow on the top of the comparator points to the front. When placed, the comparator faces away from the player. The comparator has two miniature redstone torches at the back and one at the front. The back torches turn on when the comparator's output is greater than zero (the arrow on top also turns red). The front torch has two states that can be toggled by using the comparator:

- Down and unpowered (indicating the comparator is in "comparison mode")
- Up and powered (indicating the comparator is in "subtraction mode")

The redstone comparator can take a signal strength input from its rear as well as from both sides. Side inputs are accepted only from redstone dust, block of redstone‌[Java Edition  only], redstone repeaters, other comparators, and observers in specific scenarios. The redstone comparator's front is its output.

It takes 1 redstone tick (2 game ticks, or 0.1 seconds barring lag) for signals to move through a redstone comparator, either from the rear or from the sides. This applies to changing signal strengths as well as simply to turning on and off. 

Redstone comparators check their power state before their scheduled ticks update. This results in redstone comparators not usually responding to 1-tick fluctuations of power or signal strength — for example, a 1-clock input is treated as always off from the side, and always on from the rear. This happens because the signal changes back to its original state before the redstone comparator checks its input states. However, certain setups such as powering any input with two separate observer pulses at the same time causes a redstone comparator to respond to 2 gametick pulses.

The redstone comparator has four functions: maintain signal strength, compare signal strength, subtract signal strength, and measure certain block states (primarily the fullness of containers).

### Maintain signal strength
A redstone comparator with no powered sides outputs the same signal strength as its rear input, with a 1 tick delay.

### Compare signal strength
Comparators in comparison mode.
A redstone comparator in comparison mode (front torch down and unpowered) compares its rear input to its two side inputs. If either side input is greater than the rear input, the comparator output turns off. If neither side input is greater than the rear input, the comparator outputs the same signal strength as its rear input.

The formula for calculating the output signal strength is as follows:

output = rear × [left ≤ rear AND right ≤ rear]


### Subtract signal strength
The greatest of the side inputs A and C is subtracted from the rear input B, outputting 1. If either A or C were greater than B, it would output 0.
A redstone comparator in subtraction mode (front torch up and powered) subtracts the signal strength of the higher side input from the signal strength of the rear input.

output = max(rear − max(left, right), 0)

For example: if the signal strength is 6 at the left input, 7 at the right input and 4 at the rear, the output signal has a strength of max(4 − max(6, 7), 0) = max(4−7, 0) = max(−3, 0) = 0.

If the signal strength is 9 at the rear, 2 at the right input and 5 at the left input, the output signal has a strength of max(9 − max(2, 5), 0) = max(9−5, 0) = 4.

### Measure block state
















A redstone comparator can measure the fullness of a chest, as well as other block states, even through an opaque block.
A redstone comparator treats certain blocks behind it as power sources and outputs a signal strength proportional to the block's state. The comparator may be separated from the measured block by an opaque block. However, in Java Edition, if the opaque block is powered to signal strength 15, then the comparator outputs 15 no matter the fullness of the container.[1]


