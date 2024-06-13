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

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

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
| Ingredients                                             | Crafting recipe |
|---------------------------------------------------------|-----------------|
| Iron Ingot+<br/>Stone Pressure Plate+<br/>Redstone Dust | 6               |

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

### Redstone component
Example for signal strength of a full minecart (right) and a half-full one (left)
See also: Redstone circuit

A detector rail activates when any minecart is on it (even if only a portion of the minecart is on it), and deactivates when no minecarts are on it. The duration of the signal is always a multiple of 10 redstone ticks (although lag or unloading/reloading a chunk might affect this). While active, a detector rail:

- powers adjacentredstone dustand adjacentredstone repeatersfacing away from the detector rail, topower level15
- powers adjacentredstone comparatorsfacing away from the detector rail to a level corresponding to the fullness of the minecart if it is aminecart with chestor aMinecart with Hopper.
- strongly powers any full solid opaqueblockbeneath the detector rail to power level 15
- activates any adjacentmechanism components, including above or below, such aspistons,redstone lamps,powered rails,hoppers, etc.

Comparators give a signal for a minecart with chest or a minecart with hopper
If the minecart on the detector rail is a minecart with chest or minecart with hopper, an adjacent redstone comparator facing away from the detector rail outputs a power level proportional to the container's fullness, possibly power level 0. For any other type of minecart (including a regular minecart with a mob riding it) the comparator's output is zero.

A comparator can read the contents of a minecart with hopper or with chest on a detector rail through a solid opaque block, as it can with other container blocks.


### Mob interaction
Like other types of rails, spiders, cave spiders, and wardens are the only land mobs that can walk onto detector rails.

## Data values
### ID
Java Edition:

| Name          | Identifier      | Form         | Block tags                                | Item tags | Translation key                 |
|---------------|-----------------|--------------|-------------------------------------------|-----------|---------------------------------|
| Detector Rail | `detector_rail` | Block & Item | `prevent_mob_spawning_inside`<br/>`rails` | `rails`   | `block.minecraft.detector_rail` |

Bedrock Edition:

| Name          | Identifier      | Numeric ID | Form                       | Item ID[i 1]   | Translation key           |
|---------------|-----------------|------------|----------------------------|----------------|---------------------------|
| Detector Rail | `detector_rail` | `28`       | Block & Giveable Item[i 2] | Identical[i 3] | `tile.detector_rail.name` |

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

