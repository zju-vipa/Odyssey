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

### Redstone component
See also: Redstone circuit

Activator rails can be used to affect minecarts that travel over them.

** Activation **
An activator rail is aredstone mechanismand can be activated by:
- an adjacent activepower component(for example, aredstone torch, ablock of redstone, adaylight sensor, etc.)
- an adjacentpowered block(strongly-powered or weakly-powered)
- a poweredredstone comparatororredstone repeaterfacing the activator rail
- poweredredstone dustconfigured to point at the activator rail, or configured as a plus sign. An activator rail isnotactivated by adjacent powered redstone dust that is configured to point in another direction.

An activated activator rail also activates any adjacent activator rails it is connected to, up to eight away from the original activation source. Thus a single activation source can activate up to 17 rails (one original in the middle and eight on either side). An activated activator rail does not activate adjacent rails not connected to it.
Activation and deactivation are instant and occur in the same gametick the power source turns on or off (any eventual delay depends on the power source).
** Behavior **
An activator rail affects minecarts above it with varying effects that occur as soon as any part of the minecart is on the activator rail.

An active activator rail:

- starts shaking, and ejects mobs (including players) from minecarts — the destination location is picked the same way as whendismountinga minecart
- repeatedly activatesminecarts with command blocks— a command block minecart executes its command every four game ticks until the command block minecart is no longer on the activator rail
- disablesminecarts with hoppers— a disabled hopper minecart cannot pick up items it travels through until it is enabled by an inactive activator rail (or until it is broken and re-placed)
- primesminecarts with TNT— primed TNT minecarts explode after four seconds with an explosive power proportional to their speed over the activator rail.

An inactive activator rail enables minecarts with hoppers — an enabled hopper minecart picks up items it travels through until it is disabled by an active activator rail.

A hopper minecart stops picking up items in the same tick it touches an active activator rail or in the same tick the inactive rail it is standing on is powered (it does not collect the item it could have taken from a container above in the same tick the activator rail turns on and takes the first item in the same tick the rail turns off again).

### Mob interaction
Like other types of rails, spiders, cave spiders, and wardens are the only land mobs that can walk onto activator rails.

## Data values
### ID
Java Edition:

| Name           | Identifier       | Form         | Block tags                                | Item tags | Translation key                  |
|----------------|------------------|--------------|-------------------------------------------|-----------|----------------------------------|
| Activator Rail | `activator_rail` | Block & Item | `prevent_mob_spawning_inside`<br/>`rails` | `rails`   | `block.minecraft.activator_rail` |

Bedrock Edition:

| Name           | Identifier       | Numeric ID | Form                       | Item ID[i 1]   | Translation key            |
|----------------|------------------|------------|----------------------------|----------------|----------------------------|
| Activator Rail | `activator_rail` | `126`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.activator_rail.name` |

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

