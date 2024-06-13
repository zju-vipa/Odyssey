# Tutorials/Item transportation
Item transportation is the automatic movement of items from one location to another. Item transportation is used frequently in combination with storage systems and item sorters.

## Contents
- 1 Definitions
	- 1.1 Item forms
	- 1.2 Throughput and delay
- 2 Horizontal transportation
	- 2.1 Hopper lines
	- 2.2 Water streams
- 3 Vertical transportation
	- 3.1 Bubble elevator
	- 3.2 Dropper elevator
	- 3.3 Block elevator
- 4 Diagonal transportation
- 5 Video

## Definitions
### Item forms
Items can exist in two forms in the game: as an inventory slot or as an entity floating around in the world. A dropper with a clock circuit is used to convert the former into the latter, while a hopper can convert the latter into the former.

### Throughput and delay
Any pipeline has two measures for its "speed":

- Thethroughputis how many items it can transfer per second.
- Thedelayis how long an item takes to reach the other end.

To use an internet analogy, a flock of pigeons carrying memory sticks would have a high throughput, but the delay would be high due to their flying speed. Similarly, a stack of items moving down a regular stream of water is fast in terms of throughput and slow in terms of delay.

## Horizontal transportation
Often, items need to be transported from one point to another. The easiest ways to do this are hopper lines and water streams.

### Hopper lines
By placing a line of hoppers all pointing into each other, items can be transported at a throughput of 2.5 ips. This method is among the simplest to create, but is also somewhat iron expensive at 5 ingots a hopper.

On large scale, hoppers have been known to create lag. To remedy this, some players place containers, such as droppers, furnaces, or composters on top of each hopper. This is to prevent the hoppers from attempting to search for entities with inventories above them, which then have to be checked for valid items to transfer, and/or item entities.[1][2]

### Water streams
A less iron expensive method is the use of water streams. This uses the mechanic of dropped items moving in flowing water streams. Using water also gets around the ips throughput problem, as items can be moved around in a full merged stack entity and many entities can travel at the same time. The delay is longer, however.

Since water can only flow 7 blocks from the source, it is usually necessary to use multiple water sources. To handle the breaks, a packed ice block and sign can be used. When the items come out of one stream, they will slide across the ice to the next. The sign is necessary to prevent the second stream from flowing backwards. Placing the sign in place of the last water flow block instead of after it eliminates the need for packed ice. A number of other items can be used instead of a sign (which has a hitbox and can trap items): an upright slab or a closed trapdoor can let the items pass under; and a pressure plate can let items pass without any hit.

Water flowing on packed ice blocks and blue ice block makes the items go faster, reducing the delay. (Ice works too, but one needs to carefully manage the light levels so it does not melt.)

It is a good idea to slow items down at some points so they can group into stack-sized entities and reduce server load. One way to do so is to use a cobweb in a free-air drop: this is simple and reliable, but uses a non-renewable resource. Other ways include timed trapdoors delaying item flow and sea pickles blocking items temporarily with its tiny hitbox. For enormous amounts of items, a shulker box loader might be a better idea.

## Vertical transportation
When items are transported upwards, the mechanism is usually called an item elevator. These can be useful when it is necessary to move items from underground. Items can either be transported with containers, such as droppers, or in item form, such as through water.

### Bubble elevator
Using soul sand and bubble columns, it is possible to transport items upward very quickly. To build one, just create an enclosed column of water sources and place soul sand at the bottom. It is possible to create this without soul sand, however it will be much slower.

### Dropper elevator
See also: Ultimate Guide to Reliable Dropper Towers
Dropper elevators usually work by having a line of droppers pointing upwards. When the droppers are powered, items can travel upwards. The video demonstrates two of these designs. Note that the third design in the video is an outdated block elevator and may not work and that if it is running there will be a lot of lag and sound.

| Dropper item elevator tutorial (view on YouTube) |
|--------------------------------------------------|
|                                                  |

### Block elevator
When items are glitched into blocks with a dropper, they will float upwards until they get out of the blocks. The video demonstrates a design that uses this technique. Note that the second design is for a fast, silent dropper elevator and not a block elevator.

| Block item elevator (view on YouTube) |
|---------------------------------------|
|                                       |

## Diagonal transportation
Using pistons it is possible to move items horizontally as well as vertically.

| YouTube Video (view on YouTube) |
|---------------------------------|
|                                 |

