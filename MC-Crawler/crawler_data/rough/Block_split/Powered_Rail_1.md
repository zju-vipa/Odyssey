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


