## Data values
### ID
Java Edition:

| Name | Identifier | Form         | Block tags                                | Item tags | Translation key        |
|------|------------|--------------|-------------------------------------------|-----------|------------------------|
| Rail | `rail`     | Block & Item | `prevent_mob_spawning_inside`<br/>`rails` | `rails`   | `block.minecraft.rail` |

Bedrock Edition:

| Name | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key  |
|------|------------|------------|----------------------------|----------------|------------------|
| Rail | `rail`     | `66`       | Block & Giveable Item[i 2] | Identical[i 3] | `tile.rail.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

Java Edition:

| Name        | Default value | Allowed values                                                                                    | Description                                                                                                                                            |
|-------------|---------------|---------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| shape       | `north_south` | `east_west`<br/>`north_east`<br/>`north_south`<br/>`north_west`<br/>`south_east`<br/>`south_west` | The two directions a rail connects to.<br/>For example, a`south_east`rail is a curved rail that connects to the south and to the east.                 |
|             |               | `ascending_east`<br/>`ascending_north`<br/>`ascending_south`<br/>`ascending_west`                 | A rail that ascendstowardthe direction noted.<br/>For example, an`ascending_west`rail is a straight rail that goes upward from the easttowardthe west. |
| waterlogged | `false`       | `true`<br/>`false`                                                                                | Whether or not there's water in the same place as this rail.                                                                                           |

Bedrock Edition:

| Name           | Metadata Bits                       | Default value | Allowed values | Values forMetadata Bits | Description                                      |
|----------------|-------------------------------------|---------------|----------------|-------------------------|--------------------------------------------------|
| rail_direction | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8` | `0`           | `0`            | `0`                     | Straight rail connecting to the north and south. |
|                |                                     |               | `1`            | `1`                     | Straight rail connecting to the east and west.   |
|                |                                     |               | `2`            | `2`                     | Sloped rail ascending to the east.               |
|                |                                     |               | `3`            | `3`                     | Sloped rail ascending to the west.               |
|                |                                     |               | `4`            | `4`                     | Sloped rail ascending to the north.              |
|                |                                     |               | `5`            | `5`                     | Sloped rail ascending to the south.              |
|                |                                     |               | `6`            | `6`                     | Curved rail connecting to the south and east.    |
|                |                                     |               | `7`            | `7`                     | Curved rail connecting to the south and west.    |
|                |                                     |               | `8`            | `8`                     | Curved rail connecting to the north and west.    |
|                |                                     |               | `9`            | `9`                     | Curved rail connecting to the north and east.    |


