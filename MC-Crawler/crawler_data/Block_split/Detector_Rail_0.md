# Detector Rail
A detector rail is a type of rail that produces a redstone signal while a minecart is on it.

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
- 8 Gallery
	- 8.1 Screenshots
- 9 See also

## Obtaining
### Breaking
A detector rail can be broken fairly easily by hand, dropping itself as an item. It can be broken faster by using a pickaxe. 

| Block     | Detector Rail         |
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


A detector rail also drops as an item if:

- the block beneath it is removed
- waterorlavaflows over it‌[Java Edition  only]
- apistonmoves it into a space with no floor below it.

### Chest loot
| Item          | Structure | Container | Quantity | Chance                         |
|---------------|-----------|-----------|----------|--------------------------------|
|               |           |           |          | Java EditionandBedrock Edition |
| Detector Rail | Mineshaft | Chest     | 1–4      | 27.1%                          |

### Crafting
| Ingredients                                   | Crafting recipe |
|-----------------------------------------------|-----------------|
| Iron Ingot+Stone Pressure Plate+Redstone Dust | 6               |

## Usage
A detector rail can be used as a rail that can detect when minecarts are on it or how full container minecarts on it are.

To place a detector rail, use the Place Block control on the face of a block adjacent to the destination space.

A detector rail can be attached to:

- thetopof any full solidopaqueblock (stone, dirt, blocks of gold, etc.), including full-block mechanism components (command blocks,dispensers,droppers,note blocks, andredstone lamps)
- thetopof ahopper, upside-downslab, or upside-downstairs.

A detector rail cannot be attached to the side or bottom of any block, but attempting to make such an attachment may cause the detector rail to attach to the top of a block under the destination space. For example, if a fence is on the ground, attempting to attach a detector rail to the side of the fence causes the detector rail to be attached to the top of the ground next to the fence instead.

If updated while on an opened trapdoor, a detector rail (or other rails) breaks drops as an item. Placing a minecart on a detector rail on top of a closed and unpowered trapdoor opens the trapdoor and updates it, causing the detector rail to break. If the trapdoor is powered while the minecart is placed, the trapdoor does not open and the rail does not break. The minecart on the detector rail powers the trapdoor and keeps it closed even if the external power source is removed, allowing the detector rail to stay on.

When placed, a detector rail configures itself to line up with any adjacent rails (including activator rails, powered rails, and other detector rails), as well as adjacent rails one block up. If there are two adjacent rails on non-opposite sides, or three or more adjacent rails, a detector rail lines up in the east-west direction. If there are no adjacent rails, a detector rail lines up in the north-south direction (but if a rail is later placed to the east or west, the detector rail re-orients itself in the east-west direction even if it is already connected to another rail to the north or south). If a rail it would line up with is one block up, a detector rail slants upward toward it (with multiple options to slant upward to, a detector rail "prefers", in order: west, east, south, and north). Other configurations can be created by placing and removing various rails.

Mobs avoid walking across a detector rail (or other rails), but can be pushed onto them.

It cannot be placed suspended in midair, even with commands.[1]

### Rail
Main article: Rail
Detector rails (and other rails) act as "roads" for minecarts. A minecart that enters a detector rail's space from either end of the detector rail continues to move, losing only a little velocity (which can then be increased again with powered rails). A minecart that enters a detector rail's space from the side turns east or south (depending on the detector rail's orientation), or in the downward direction for a slanted detector rail.

