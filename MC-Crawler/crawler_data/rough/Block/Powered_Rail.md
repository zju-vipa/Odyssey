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

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

A powered rail also drops as an item when the block beneath it is removed or a piston moves it into a space with no floor below it. 

### Chest loot
| Item         | Structure | Container | Quantity | Chance                         |
|--------------|-----------|-----------|----------|--------------------------------|
|              |           |           |          | Java EditionandBedrock Edition |
| Powered Rail | Mineshaft | Chest     | 1–4      | 27.1%                          |

### Crafting
| Ingredients                              | Crafting recipe |
|------------------------------------------|-----------------|
| Gold Ingot+<br/>Stick+<br/>Redstone Dust | 6               |

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

** Activation **
A powered rail is aredstone mechanismand can be activated by:
- an adjacent activepower component(for example, aredstone torch, ablock of redstone, adaylight sensor, etc.)
- an adjacentpowered block(strongly-powered or weakly-powered)
- a poweredredstone comparatororredstone repeaterfacing the powered rail
- poweredredstone dustconfigured to point at the powered rail; a powered rail isnotactivated by adjacent powered redstone dust that is a directionless "dot" or configured to point in another direction.

An activated powered rail also activates any adjacent powered rails it is connected to, up to eight away from the original activation source. Thus a single activation source can activate up to 17 rails (one original in the middle and eight on either side). An activated powered rail does not activate non-connected adjacent rails.
** Behavior **
Anactivepowered rail:
- increases the speed of a moving minecart in the direction it is already moving. Specifically, let the speed in both the X and Z directions (meters / tick) combined be "speed". If speed > 0.01, then every tick the minecart is passing over the powered rail, its x velocity is increased by (xspeed * 0.06 / speed) and its z velocity is increased by (zspeed * 0.06 / speed)
- accelerate a non-moving minecart away from a solid opaque block the powered rail is facing (so a non-moving minecart moves away from the block when the powered rail activates, and a moving minecart bounces off a block an active powered rail is facing because it stops and then gets accelerated away)

Aninactivepowered rail reduces the speed of a moving minecart, usually stopping it within one block's distance even on a downward-slanted track. If a slanted powered rail activates with a non-moving minecart on it, the minecart starts moving downward (because it is no longer being braked by an inactive powered rail) and is then accelerated downward.
Powered rails cannot increase the speed of a minecart to more than 8 blocks per second on either the north-south or east-west axis. The speeds that can be achieved with varying numbers of powered rails or intervals of normal rails between powered rails is complex -- for a thorough discussion, seeTutorials/Minecarts.
### Mob interaction
Like other types of rails, spiders, cave spiders, and wardens are the only land mobs that can walk onto powered rails.

## Data values
### ID
Java Edition:

| Name         | Identifier     | Form         | Block tags                                | Item tags | Translation key                |
|--------------|----------------|--------------|-------------------------------------------|-----------|--------------------------------|
| Powered Rail | `powered_rail` | Block & Item | `prevent_mob_spawning_inside`<br/>`rails` | `rails`   | `block.minecraft.powered_rail` |

Bedrock Edition:

| Name         | Identifier    | Numeric ID | Form                       | Item ID[i 1]   | Translation key         |
|--------------|---------------|------------|----------------------------|----------------|-------------------------|
| Powered Rail | `golden_rail` | `27`       | Block & Giveable Item[i 2] | Identical[i 3] | `tile.golden_rail.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

Java Edition:

| Name        | Default value | Allowed values                                                                    | Description                                                                                                                                            |
|-------------|---------------|-----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| powered     | `false`       | `false`<br/>`true`                                                                | True if rail is activated.                                                                                                                             |
| shape       | `north_south` | `east_west`<br/>`north_south`                                                     | Specifies the rail's orientation.                                                                                                                      |
|             |               | `ascending_east`<br/>`ascending_north`<br/>`ascending_south`<br/>`ascending_west` | A rail that ascendstowardthe direction noted.<br/>For example, an`ascending_west`rail is a straight rail that goes upward from the easttowardthe west. |
| waterlogged | `false`       | `false`<br/>`true`                                                                | Whether or not there's water in the same place as this rail.                                                                                           |

Bedrock Edition:

| Name           | Metadata Bits             | Default value | Allowed values              | Values forMetadata Bits | Description                         |
|----------------|---------------------------|---------------|-----------------------------|-------------------------|-------------------------------------|
| rail_data_bit  | `0x8`                     | `false`       | `false`<br/>`true`          | `0`<br/>`1`             | True if rail is activated.          |
| rail_direction | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`                         | `0`                     | flat track going north-south        |
|                |                           |               | `1`                         | `1`                     | flat track going east-west          |
|                |                           |               | `2`                         | `2`                     | sloped track ascending to the east  |
|                |                           |               | `3`                         | `3`                     | sloped track ascending to the west  |
|                |                           |               | `4`                         | `4`                     | sloped track ascending to the north |
|                |                           |               | `5`                         | `5`                     | sloped track ascending to the south |
|                |                           |               | `6`<br/>`7`<br/>`8`<br/>`9` | `Unsupported`           | Unused                              |

