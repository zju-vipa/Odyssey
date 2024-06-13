# Powered Rail
A powered rail is a type of rail that either increases or decreases the velocity of minecarts that move over it, depending on its power state.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Chest loot
	- 1.3 Crafting
- 2 Usage
	- 2.1 Rail
	- 2.2 Redstone component
	- 2.3 Mob interaction
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 Video
- 6 History
	- 6.1 Data history
- 7 Issues
- 8 Trivia
- 9 Gallery
	- 9.1 Screenshots
- 10 See also
- 11 References

## Obtaining
### Breaking
Powered rails can be crafted, and previously placed powered rails can be broken with any tool or by hand, dropping themselves as items.

| Block     | Powered Rail          |
|-----------|-----------------------|
| Hardness  | 0.7                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 1.05                  |
| Wooden    | 0.55                  |
| Stone     | 0.3                   |
| Iron      | 0.2                   |
| Diamond   | 0.15                  |
| Netherite | 0.15                  |
| Golden    | 0.1                   |


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


A powered rail also drops as an item when the block beneath it is removed or a piston moves it into a space with no floor below it. 

### Chest loot
| Item         | Structure | Container | Quantity | Chance                         |
|--------------|-----------|-----------|----------|--------------------------------|
|              |           |           |          | Java EditionandBedrock Edition |
| Powered Rail | Mineshaft | Chest     | 1–4      | 27.1%                          |

### Crafting
| Ingredients                    | Crafting recipe |
|--------------------------------|-----------------|
| Gold Ingot+Stick+Redstone Dust | 6               |

## Usage
See also: Tutorials/Minecarts

A powered rail can be used as a rail and as a redstone component.

To place a powered rail, use a powered rail item while pointing at a surface facing the space the powered rail should occupy. A powered rail can be placed on:

- thetopof any full solidopaqueblock (stone, dirt, blocks of gold, etc.), including full-block mechanism components (command blocks,dispensers,droppers,note blocks, andredstone lamps)
- thetopof ahopper, upside-downslab, or upside-downstairs.

A powered rail cannot be attached to the side or bottom of any block, but attempting to make such an attachment may cause the powered rail to attach to the top of a block under the destination space. For example, if a fence is on the ground, attempting to attach a powered rail to the side of the fence causes the powered rail to be attached to the top of the ground next to the fence instead.

When placed, a powered rail configures itself to line up with any adjacent rails (including activator rails, detector rails, and other powered rails), as well as adjacent rails one block up. If there are two adjacent rails on non-opposite sides, or three or more adjacent rails, a powered rail lines up in the east-west direction. If there are no adjacent rails, a powered rail lines up in the north-south direction (but if a rail is later placed to the east or west, the powered rail re-orients itself in the east-west direction even if it is already connected to another rail to the north or south). If a rail it would line up with is one block up, a powered rail slants upward toward it (with multiple options to slant upward to, a powered rail "prefers", in order: west, east, south, and north). Other configurations can be created by placing and removing various rails. Unlike their unpowered counterparts, and like detector and activator rails, powered rails are always straight.

It cannot be placed suspended in midair, even with commands, which is not unintentional.[1]

### Rail
Main article: Rail
Powered rails (and other rails) can be used as "roads" for minecarts. A minecart that enters a powered rail's space from either end of the powered rail continues to move in the direction the powered rail is facing, but its speed may change depending on whether the powered rail is active or not (see below). A minecart that enters a powered rail's space from the side turns east or south (depending on the powered rail's orientation), or in the downward direction for a slanted powered rail.

### Redstone component
See also: Redstone circuit

Powered rails can be used to affect the speed of minecarts that travel over them.

Activation
A powered rail is a redstone mechanism and can be activated by:
an adjacent active power component (for example, a redstone torch, a block of redstone, a daylight sensor, etc.)
an adjacent powered block (strongly-powered or weakly-powered)
a powered redstone comparator or redstone repeater facing the powered rail
powered redstone dust configured to point at the powered rail; a powered rail is not activated by adjacent powered redstone dust that is a directionless "dot" or configured to point in another direction.
An activated powered rail also activates any adjacent powered rails it is connected to, up to eight away from the original activation source. Thus a single activation source can activate up to 17 rails (one original in the middle and eight on either side). An activated powered rail does not activate non-connected adjacent rails.
Behavior
An active powered rail:
increases the speed of a moving minecart in the direction it is already moving. Specifically, let the speed in both the X and Z directions (meters / tick) combined be "speed". If speed > 0.01, then every tick the minecart is passing over the powered rail, its x velocity is increased by (xspeed * 0.06 / speed) and its z velocity is increased by (zspeed * 0.06 / speed)
accelerate a non-moving minecart away from a solid opaque block the powered rail is facing (so a non-moving minecart moves away from the block when the powered rail activates, and a moving minecart bounces off a block an active powered rail is facing because it stops and then gets accelerated away)
An inactive powered rail reduces the speed of a moving minecart, usually stopping it within one block's distance even on a downward-slanted track. If a slanted powered rail activates with a non-moving minecart on it, the minecart starts moving downward (because it is no longer being braked by an inactive powered rail) and is then accelerated downward.
Powered rails cannot increase the speed of a minecart to more than 8 blocks per second on either the north-south or east-west axis. The speeds that can be achieved with varying numbers of powered rails or intervals of normal rails between powered rails is complex -- for a thorough discussion, see Tutorials/Minecarts.
