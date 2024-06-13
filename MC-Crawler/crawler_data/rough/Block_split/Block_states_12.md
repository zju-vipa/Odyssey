### Mob heads
Java Edition:
Floor

| Name     | Default value | Allowed values | Description                            |
|----------|---------------|----------------|----------------------------------------|
| powered  | `false`       | `true`         | The block receives a redstone signal.  |
|          |               | `false`        | The block receives no redstone signal. |
| rotation | `0`           | `0`            | The block is facing south.             |
|          |               | `1`            | The block is facing south-southwest.   |
|          |               | `2`            | The block is facing southwest.         |
|          |               | `3`            | The block is facing west-southwest.    |
|          |               | `4`            | The block is facing west.              |
|          |               | `5`            | The block is facing west-northwest.    |
|          |               | `6`            | The block is facing northwest.         |
|          |               | `7`            | The block is facing north-northwest.   |
|          |               | `8`            | The block is facing north.             |
|          |               | `9`            | The block is facing north-northeast.   |
|          |               | `10`           | The block is facing northeast.         |
|          |               | `11`           | The block is facing east-northeast.    |
|          |               | `12`           | The block is facing east.              |
|          |               | `13`           | The block is facing east-southeast.    |
|          |               | `14`           | The block is facing southeast.         |
|          |               | `15`           | The block is facing south-southeast.   |

Wall

| Name    | Default value | Allowed values                            | Description                                                                                           |
|---------|---------------|-------------------------------------------|-------------------------------------------------------------------------------------------------------|
| powered | `false`       | `true`                                    | The block receives a redstone signal.                                                                 |
|         |               | `false`                                   | The block receives no redstone signal.                                                                |
| facing  | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the head is facing.<br/>Opposite from the direction a player is facing when placing it. |

Bedrock Edition:

| Name             | Metadata Bits             | Default value | Allowed values | Values forMetadata Bits | Description                                          |
|------------------|---------------------------|---------------|----------------|-------------------------|------------------------------------------------------|
| facing_direction | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `1`            | `1`                     | On the floor (rotation is stored in the tile entity) |
|                  |                           |               | `2`            | `2`                     | On a wall, facing north                              |
|                  |                           |               | `3`            | `3`                     | On a wall, facing south                              |
|                  |                           |               | `4`            | `4`                     | On a wall, facing east                               |
|                  |                           |               | `5`            | `5`                     | On a wall, facing west                               |
|                  |                           |               | `0`            | `0`                     | Unused                                               |



### Muddy Mangrove Roots
Java Edition:

| Name | Default value | Allowed values | Description                                       |
|------|---------------|----------------|---------------------------------------------------|
| axis | `y`           | `x`            | The muddy mangrove roots is oriented east–west.   |
|      |               | `y`            | The muddy mangrove roots is oriented vertically.  |
|      |               | `z`            | The muddy mangrove roots is oriented north–south. |

Bedrock Edition:

| Name        | Metadata Bits   | Default value | Allowed values | Values forMetadata Bits | Description                                       |
|-------------|-----------------|---------------|----------------|-------------------------|---------------------------------------------------|
| pillar_axis | `0x1`<br/>`0x2` | `y`           | `x`            | `1`                     | The muddy mangrove roots is oriented east–west.   |
|             |                 |               | `y`            | `0`                     | The muddy mangrove roots is oriented vertically.  |
|             |                 |               | `z`            | `2`                     | The muddy mangrove roots is oriented north–south. |

### Mushroom Blocks
Java Edition:

| Name  | Default value | Allowed values     | Description                                                                                         |
|-------|---------------|--------------------|-----------------------------------------------------------------------------------------------------|
| east  | `true`        | `false`<br/>`true` | /If true, the east face has the cap/stem texture.<br/>If false, it has the pores texture instead.   |
| down  | `true`        | `false`<br/>`true` | /If true, the bottom face has the cap/stem texture.<br/>If false, it has the pores texture instead. |
| north | `true`        | `false`<br/>`true` | /If true, the north face has the cap/stem texture.<br/>If false, it has the pores texture instead.  |
| south | `true`        | `false`<br/>`true` | /If true, the south face has the cap/stem texture.<br/>If false, it has the pores texture instead.  |
| up    | `true`        | `false`<br/>`true` | /If true, the top face has the cap/stem texture.<br/>If false, it has the pores texture instead.    |
| west  | `true`        | `false`<br/>`true` | /If true, the west face has the cap/stem texture.<br/>If false, it has the pores texture instead.   |

Bedrock Edition:

| Name               | Metadata Bits                       | Default value | Allowed values         | Values forMetadata Bits | Description                                                                                         |
|--------------------|-------------------------------------|---------------|------------------------|-------------------------|-----------------------------------------------------------------------------------------------------|
| huge_mushroom_bits | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8` | `0`           | `0`                    | `0`                     | All six faces have the pores texture.                                                               |
|                    |                                     |               | `1`                    | `1`                     | Cap texture on top, west and north; pores on other sides.                                           |
|                    |                                     |               | `2`                    | `2`                     | Cap texture on top and north; pores on other sides.                                                 |
|                    |                                     |               | `3`                    | `3`                     | Cap texture on top, north and east; pores on other sides.                                           |
|                    |                                     |               | `4`                    | `4`                     | Cap texture on top and west; pores on other sides.                                                  |
|                    |                                     |               | `5`                    | `5`                     | Cap texture on top; pores on other sides.                                                           |
|                    |                                     |               | `6`                    | `6`                     | Cap texture on top and east; pores on other sides.                                                  |
|                    |                                     |               | `7`                    | `7`                     | Cap texture on top, south and west; pores on other sides.                                           |
|                    |                                     |               | `8`                    | `8`                     | Cap texture on top and south; pores on other sides.                                                 |
|                    |                                     |               | `9`                    | `9`                     | Cap texture on top, east and south; pores on other sides.                                           |
|                    |                                     |               | `10`                   | `10`                    | The four side faces have the stem texture,<br/>and the top and bottom faces have the pores texture. |
|                    |                                     |               | `11`<br/>`12`<br/>`13` | `11`<br/>`12`<br/>`13`  | All six faces have the pores texture.                                                               |
|                    |                                     |               | `14`                   | `14`                    | All six faces have the cap texture.                                                                 |
|                    |                                     |               | `15`                   | `15`                    | All six faces have the stem texture.                                                                |



