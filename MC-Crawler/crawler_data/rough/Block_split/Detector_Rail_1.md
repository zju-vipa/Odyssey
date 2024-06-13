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


