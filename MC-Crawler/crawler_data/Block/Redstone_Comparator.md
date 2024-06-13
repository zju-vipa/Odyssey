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


#### Fullness of containers
|  |
|--|
|  |

A redstone comparator can output a signal indicating how full a container is. (0 for empty, 15 for full, etc.) The table on the right is described more in detail, later in this section.

Containers that can be measured by a comparator include:

- Barrel
- Blast furnace
- Brewing stand
- Chest
- Crafter‌[upcoming: JE 1.21 & BE 1.21.0]
- Decorated pot
- Dispenser
- Dropper
- Furnace
- Hopper
- Large chest
- Large trapped chest
- Minecart with cheston top of adetector rail
- Minecart with hopperon top of adetector rail
- Shulker box(any color)
- Smoker
- Trapped chest

Generally speaking, the comparator output signal strength represents the average fullness of the slots, based on how many of that item form a full stack (64, 16, or 1 for non-stackable items).

The Minimum items for container signal strength table (right) shows the minimum full-stack-equivalent (FSE) to produce different signal strengths from common containers. A full-stack-equivalent quantifies how many normal 64-stackable items are needed to output a corresponding signal strength. The 's' is a constant 64, with the additional amount needed following after.

One may also consider the terms: cumulative-weight or weighted-sum instead of full-stack-equivalent.

Items that stack to a max of 16  (snowballs, signs, ender pearls, etc.), contribute +4 to the full-stack-equivalent for each unity (count of 1 item). Similarly, items that stack to 1 (minecart, boat, etc.) contribute +64, and items that stack to 64 contribute +1.

Example 1: 3 ender pearls contribute a 3×4 = 12 full-stack-equivalent.

Example 2: 16 ender pearls and 60 redstone dust contributes a 16×4 + 60×1 = 124 full-stack-equivalent.

Example 3: 1 minecart and 60 redstone dust contributes a 1×64 + 60×1 = 124 full-stack-equivalent.

Example 4: To produce a signal strength of 10 from a hopper, one requires a full-stack-equivalent of at least 3s + 14 = 206 but strictly less than than 3s + 37 = 229. This can be done with 3 minecarts, and 14 dirt.

When a comparator measures a large chest or large trapped chest, it measures the entire large chest (54 slots), not just the half directly behind the comparator. A chest or trapped chest that cannot be opened (either because it has an opaque block, ocelot, or cat above it) always produces an output of 0 no matter how many items are in the container — shulker boxes can always be measured, even if they cannot open.

Calculating signal strength from items
When a container is empty, the output is off.
When it is not empty, the output signal strength is calculated as follows:
signal strength = floor(1 + ((sum of all slots' fullnesses) / (number of slots in container)) × 14)
fullness of a slot = number of items in slot / max stack size for this type of item
Example: 300 blocks in a dispenser (which has 9 slots), where each block stacks to a maximum of 64 has a 300 full-stack-equivalent. This produces an output with a signal strength of 8:

1 + ((300 items / 64 items per slot) / 9 slots) × 14 = 8.292, floored is 8


Calculating items from signal strength
It can be useful in redstone circuits to use containers with comparators to create signals of a specific strength. The number of items required in a container to produce a signal of desired strength is calculated as follows:
items required = max(desired signal strength, roundup((total slots in container × 64 / 14) × (desired signal strength − 1)))
Example: To use a furnace (which has 3 slots) to create a strength 9 signal, players need 110 items:

max(9, (3×64/14) × (9−1)) = 109.714, rounded up is 110



#### Miscellaneous
Comparators used to measure containers.
Some non-container blocks can also be measured by a redstone comparator:

Beehive and bee nest
A hive or nest outputs a signal strength equal to the amount of honey in the hive/nest.
Cake
A cake outputs a signal strength relative to the amount of cake remaining.  Each slice is worth 2 signal strength, with 7 total slices, for an output of 14 for a full cake.
Cauldron signal strength
Cauldron
A cauldron outputs different signal strengths depending on how much water or powdered snow is inside. From completely empty to completely full, the output values are 0, 1, 2, and 3. If lava is inside, the strength is always 3.
Chiseled bookshelf
A chiseled bookshelf outputs a signal strength between 1 and 6 indicating the last slot interacted with. When no slot has been interacted with yet, it outputs 0.
Composter signal strength
Composter
A composter outputs different signal strengths depending on the level inside. From completely empty to completely full, the output values are 0, 1, 2, 3, 4, 5, 6, 7 and 8.
Copper bulb‌[upcoming: JE 1.21 & BE 1.21.0]
A copper bulb at any oxidation stage emits a full signal of 15 when lit and 0 otherwise.
Command block
A command block stores the "success count" of the last command executed, which represents the number of times the most recently used command of this command block succeeded. A "success" is defined by the command's success conditions: if a red error message is returned in the chat, the command was not successful.
Most commands can succeed once per execution, but certain commands (such as those that accept players as arguments) can succeed multiple times, and the comparator outputs the number of times it succeeded (maximum 15 when sent to redstone dust, but in the code it is able to go up to the 32-bit integer limit, and can be used in contraptions with no redstone dust with those values).
A command block continues to store the success count of the last command executed until it executes its command again, thus the comparator continues to output the same signal strength even after the command block is no longer being activated (it doesn't turn off when the signal to the command block turns off).
Crafter‌[upcoming: JE 1.21 & BE 1.21.0]
A crafter outputs a signal strength equal to the number of crafting slots that are either disabled or occupied by an item. An empty crafter with no disabled slots does not output any signal through a comparator. A crafter with every slot either disabled or containing at least one item outputs a signal strength of nine through a comparator.
End portal frame
An end portal frame outputs a full signal of 15 if it contains an eye of ender and 0 otherwise.
A comparator can measure the presence and rotation of an item frame's contents.
Item frame
A comparator can measure the state of an item frame's contents. An item frame comparator outputs 0 if the item frame is empty, or 1 to 8 for any item depending on its rotation: 1 at initial placement, plus 1 for each 45° of rotation for a maximum of 8.
For an item frame that holds a map, a unit of rotation is 90° instead of 45°, but a comparator still outputs power levels 1 to 8. It takes two full rotations to cycle through all comparator outputs, and each orientation of the map corresponds to two output levels that differ by 4.
The comparator must be placed behind the block the item frame is attached to, facing away from the item frame. The block must be a full block, and the item frame cannot be submerged in water. Having a sign in the same block as the item frame prevents the frame from sending a signal as well.‌[Java Edition  only]
Jukebox
A jukebox outputs a signal strength indicating which music disc is currently playing. See the Minimum Items for Container Signal Strength table above.
Lectern
A lectern outputs a signal strength that depends on what page the player is currently on. The calculation used is:
signal strength = floor(1 + ((current page - 1) / (number of pages in book - 1)) × 14)
This results in page 1 having a signal strength of 1, and the last page having a signal strength of 15. The exception is a single page book, which outputs a signal strength of 15.
For example, a book with 15 pages outputs a signal equal to the current page number.  A book with 5 pages outputs signal strengths of 1, 4, 8, 11 and 15 for the different pages. A book with 100 pages has the signal strength increase to the next level on pages 1, 9, 16, 23, 30, 37, 44, 51, 58, 65, 72, 79, 86, 93 and 100.

Respawn anchor
A respawn anchor outputs a signal strength of 0, 3, 7, 11, or 15, depending on the "charged" value.
Sculk sensor
A sculk sensor outputs a signal strength depending on the type of vibration that is detected.

## Data values
### ID
Java Edition:

| Name                | Identifier | Form         | Translation key            |
|---------------------|------------|--------------|----------------------------|
| Redstone Comparator | comparator | Block & Item | block.minecraft.comparator |

| Name         | Identifier |
|--------------|------------|
| Block entity | comparator |

Bedrock Edition:

| Redstone Comparator | Identifier           | Numeric ID | Form                         | Item ID[i 1]   | Translation key      |
|---------------------|----------------------|------------|------------------------------|----------------|----------------------|
| Unpowered block     | unpowered_comparator | 149        | Block & Ungiveable Item[i 2] | Identical[i 3] | —                    |
| Powered block       | powered_comparator   | 150        | Block & Ungiveable Item[i 2] | Identical[i 3] | —                    |
| Item                | comparator           | 522        | Item                         | —              | item.comparator.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ a b Unavailable with /give command

↑ a b The block's direct item form has the same id as the block.


| Name         | Savegame ID |
|--------------|-------------|
| Block entity | Comparator  |

### Block states
See also: Block states

Java Edition:

| Name    | Default value | Allowed values     | Description                                                                                                                                          |
|---------|---------------|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing  | north         | eastnorthsouthwest | The direction from theoutputside to theinputside of the comparator,or the opposite from the direction the player faces while placing the comparator. |
| mode    | compare       | comparesubtract    | Specifies the current mode of the redstone comparator.                                                                                               |
| powered | false         | falsetrue          | True if the redstone comparator is being powered.                                                                                                    |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values     | Values forMetadata Bits | Description                                                                                                                                          |
|------------------------------|---------------|---------------|--------------------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| minecraft:cardinal_direction | Not Supported | south         | eastnorthsouthwest | Unsupported             | The direction from theoutputside to theinputside of the comparator,or the opposite from the direction the player faces while placing the comparator. |
| output_lit_bit               | 0x8           | false         | falsetrue          | 01                      | True if the redstone comparator is being powered.                                                                                                    |
| output_subtract_bit          | 0x4           | false         | falsetrue          | 01                      | Specifies the current mode of the redstone comparator.                                                                                               |



### Block data
A redstone comparator has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format


 Block entity data
Tags common to all block entities
 OutputSignal: Represents the strength of the analog signal output of this redstone comparator.

Bedrock Edition:

See Bedrock Edition level format/Block entity format.
