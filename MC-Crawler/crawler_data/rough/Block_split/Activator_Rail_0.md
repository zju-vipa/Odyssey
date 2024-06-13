# Activator Rail
An activator rail is a type of powerable rail that can eject players and mobs from regular minecarts, lock and unlock minecarts with hoppers and ignite minecarts with TNT.

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
- 5 History
- 6 Issues
- 7 Gallery
	- 7.1 Screenshots
- 8 See also
- 9 References

## Obtaining
### Breaking
An activator rail can be broken by hand or using any tool, dropping itself as an item, but a pickaxe is fastest. To break an activator rail, mine it:

| Block     | Activator Rail        |
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

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

An activator rail also drops as an item when the block beneath it is removed or a piston moves it into a space with no floor below it.

### Chest loot
| Item           | Structure | Container | Quantity | Chance                         |
|----------------|-----------|-----------|----------|--------------------------------|
|                |           |           |          | Java EditionandBedrock Edition |
| Activator Rail | Mineshaft | Chest     | 1–4      | 27.1%                          |

### Crafting
| Ingredients                               | Crafting recipe |
|-------------------------------------------|-----------------|
| Iron Ingot+<br/>Stick+<br/>Redstone Torch | 6               |

## Usage
An activator rail can be used as a rail and as a redstone component.

To place an activator rail, use an activator rail item while pointing at a surface facing the space the activator rail should occupy. An activator rail can be placed on:

- thetopof any full solidopaqueblock (stone, dirt, blocks of gold, etc.), including full-block mechanism components (command blocks,dispensers,droppers,note blocks, andredstone lamps)
- thetopof ahopper, upside-downslab, or upside-downstairs.
- thetopof any transparent block (glass, etc.)

An activator rail cannot be attached to the side or bottom of any block, but attempting to make such an attachment may cause the activator rail to attach to the top of a block under the destination space. For example, if a fence is on the ground, attempting to attach an activator rail to the side of the fence causes the activator rail to be attached to the top of the ground next to the fence instead.

When placed, an activator rail configures itself to line up with any adjacent rails (including detector rails, powered rails, and other activator rails), as well as adjacent rails one block up. The behaviors in Java and Bedrock editions diverge in the following ways.

In Java Edition:

If there are two adjacent rails on non-opposite sides, or three or more adjacent rails, or no adjacent rails at all, an activator rail aligns itself in the direction the player is facing. If an existing activator rail is connected to only one other rail or none at all, and a new rail is placed perpendicular to the activator rail, then the activator rail aligns itself in the east-west direction (if it isn't already facing that way). If a rail it would align with is one block up, an activator rail slants upward toward it (with multiple options to slant upward to, an activator rail "prefers" west or south). Other configurations can be created by placing and removing various rails.[needs in-game testing]
In Bedrock Edition:[needs in-game testing]

If there are two adjacent rails on non-opposite sides, or three or more adjacent rails, an activator rail aligns itself in the east-west direction. If there are no adjacent rails, an activator rail aligns itself in the north-south direction (but if a rail is later placed to the east or west, the activator rail re-orients itself in the east-west direction even if it is already connected to another rail to the north or south). If a rail it would align with is one block up, an activator rail slants upward toward it (with multiple options to slant upward to, an activator rail "prefers", in order: west, east, south, and north). Other configurations can be created by placing and removing various rails.
It cannot be placed suspended in midair, even with commands.[1]

### Rail
Main article: Rail
Activator rails (and other rails) can be used as "roads" for minecarts. A minecart that enters an activator rail's space from either end of the activator rail continues to move, losing only a little velocity (which can then be increased again with powered rails). A minecart that enters an activator rail's space from the side turns east or south (depending on the activator rail's orientation), or in the downward direction for a slanted activator rail.

