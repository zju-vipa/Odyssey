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

