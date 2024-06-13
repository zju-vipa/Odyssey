### Lectern
Java Edition:

| Name     | Default value | Allowed values                            | Description                                                                                                          |
|----------|---------------|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| facing   | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the lectern is facing.<br/>The opposite from the direction the player faces while placing the lectern. |
| has_book | `false`       | `false`<br/>`true`                        | If the lectern currently has a book.                                                                                 |
| powered  | `false`       | `false`<br/>`true`                        | If the lectern is currently outputting a redstone signal.                                                            |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values                            | Values forMetadata Bits | Description                                                                                                          |
|------------------------------|---------------|---------------|-------------------------------------------|-------------------------|----------------------------------------------------------------------------------------------------------------------|
| minecraft:cardinal_direction | Not Supported | `south`       | `east`<br/>`north`<br/>`south`<br/>`west` | `Unsupported`           | The direction the lectern is facing.<br/>The opposite from the direction the player faces while placing the lectern. |
| powered_bit                  | `0x4`         | `false`       | `false`<br/>`true`                        | `0`<br/>`1`             | If the lectern is currently outputting a redstone signal.                                                            |



### Lever
Java Edition:

| Name    | Default value | Allowed values                            | Description                                                                                                                           |
|---------|---------------|-------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| face    | `wall`        | `ceiling`<br/>`floor`<br/>`wall`          | The face of the block the lever placed on.<br/>Floor is on top of a block, ceiling is on the bottom, and wall is on one of its sides. |
| facing  | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the lever is facing.<br/>Opposite to the direction the player is facing if placed on the side of a block.               |
| powered | `false`       | `false`<br/>`true`                        | If true, the lever is currently activated.                                                                                            |

Bedrock Edition:

| Name            | Metadata Bits             | Default value    | Allowed values     | Values forMetadata Bits | Description                                  |
|-----------------|---------------------------|------------------|--------------------|-------------------------|----------------------------------------------|
| open_bit        | `0x8`                     | `false`          | `false`<br/>`true` | `0`<br/>`1`             | If the lever is currently activated.         |
| lever_direction | `0x1`<br/>`0x2`<br/>`0x4` | `down_east_west` | `down_east_west`   | `0`                     | Lever on block bottom points east when off   |
|                 |                           |                  | `east`             | `1`                     | Lever on block side facing east              |
|                 |                           |                  | `west`             | `2`                     | Lever on block side facing west              |
|                 |                           |                  | `south`            | `3`                     | Lever on block side facing south             |
|                 |                           |                  | `north`            | `4`                     | Lever on block side facing north             |
|                 |                           |                  | `up_north_south`   | `5`                     | Lever on block top points south when off.    |
|                 |                           |                  | `up_east_west`     | `6`                     | Lever on block top points east when off.     |
|                 |                           |                  | `down_north_south` | `7`                     | Lever on block bottom points south when off. |



### Light Block
Java Edition:

| Name        | Default value | Allowed values                                                                                                                    | Description                                                         |
|-------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| waterlogged | `false`       | `true`<br/>`false`                                                                                                                | Whether or not there's water in the same place as this light block. |
| level       | `15`          | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | The amount of light this block outputs.                             |

Bedrock Edition:

| Name              | Metadata Bits                       | Default value | Allowed values                                                                                                                    | Values forMetadata Bits                                                                                                           | Description                             |
|-------------------|-------------------------------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| block_light_level | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | The amount of light this block outputs. |



### Lightning Rod
Java Edition:

| Name        | Default value | Allowed values                                                | Description                                                                  |
|-------------|---------------|---------------------------------------------------------------|------------------------------------------------------------------------------|
| facing      | `up`          | `up`<br/>`down`<br/>`north`<br/>`south`<br/>`east`<br/>`west` | The direction that the lightning rod is facing, determined by its anchoring. |
| powered     | `false`       | `false`<br/>`true`                                            | Whether or not the lightning rod is powered.                                 |
| waterlogged | `false`       | `false`<br/>`true`                                            | Whether or not there's water in the same place as this lightning rod.        |

Bedrock Edition:

| Name             | Metadata Bits | Default value | Allowed values                              | Values forMetadata Bits | Description                                                                                                    |
|------------------|---------------|---------------|---------------------------------------------|-------------------------|----------------------------------------------------------------------------------------------------------------|
| facing_direction | Not Supported | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | `Unsupported`           | The direction the lightning rod faces.0: Down<br/>1: Up<br/>2: North<br/>3: South<br/>4: West<br/>5: East<br/> |



### Logs
Java Edition:

| Name | Default value | Allowed values | Description                              |
|------|---------------|----------------|------------------------------------------|
| axis | `y`           | `x`            | The log or stem is oriented east–west.   |
|      |               | `y`            | The log or stem is oriented vertically.  |
|      |               | `z`            | The log or stem is oriented north–south. |

Bedrock Edition:

| Name        | Metadata Bits   | Default value | Allowed values | Values forMetadata Bits | Description                      |
|-------------|-----------------|---------------|----------------|-------------------------|----------------------------------|
| pillar_axis | `0x1`<br/>`0x2` | `y`           | `y`            | `0`                     | The log is oriented vertically.  |
|             |                 |               | `x`            | `1`                     | The log is oriented east–west.   |
|             |                 |               | `z`            | `2`                     | The log is oriented north–south. |



### Loom
Java Edition:

| Name   | Default value | Allowed values                            | Description                                                                                             |
|--------|---------------|-------------------------------------------|---------------------------------------------------------------------------------------------------------|
| facing | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the loom is facing.<br/>Opposite from the direction the player faces when placing a loom. |

Bedrock Edition:

| Name      | Metadata Bits   | Default value | Allowed values              | Values forMetadata Bits     | Description                                                                                                                         |
|-----------|-----------------|---------------|-----------------------------|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| direction | `0x1`<br/>`0x2` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3` | `0`<br/>`1`<br/>`2`<br/>`3` | The direction the loom is facing.0: South facing loom<br/>1: West facing loom<br/>2: North facing loom<br/>3: East facing loom<br/> |



### Mangrove Roots
Java Edition:

| Name        | Default value | Allowed values     | Description                                                            |
|-------------|---------------|--------------------|------------------------------------------------------------------------|
| waterlogged | `false`       | `false`<br/>`true` | Whether or not there's water in the same place as this mangrove roots. |



### Melon Stem
Java Edition:
Growing

| Name | Default value | Allowed values                              | Description                                       |
|------|---------------|---------------------------------------------|---------------------------------------------------|
| age  | `0`           | `0`                                         | A newly planted stem.                             |
|      |               | `1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6` | Intermediate growth stages of the stem.           |
|      |               | `7`                                         | A fully mature stem, capable of producing melons. |

Attached

| Name   | Default value | Allowed values                            | Description                               |
|--------|---------------|-------------------------------------------|-------------------------------------------|
| facing | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction from the stem to the melon. |

Bedrock Edition:

| Name             | Metadata Bits             | Default value | Allowed values                              | Values forMetadata Bits                     | Description                                       |
|------------------|---------------------------|---------------|---------------------------------------------|---------------------------------------------|---------------------------------------------------|
| growth           | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`                                         | `0`                                         | A newly planted stem.                             |
|                  |                           |               | `1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6` | `1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6` | Intermediate growth stages of the stem.           |
|                  |                           |               | `7`                                         | `7`                                         | A fully mature stem, capable of producing melons. |
| facing_direction | Not Supported             | `0`           | `0`<br/>`1`                                 | `Unsupported`                               | Unused                                            |
|                  |                           |               | `2`                                         | `Unsupported`                               | Stem pointing north.                              |
|                  |                           |               | `3`                                         | `Unsupported`                               | Stem pointing south.                              |
|                  |                           |               | `4`                                         | `Unsupported`                               | Stem pointing west.                               |
|                  |                           |               | `5`                                         | `Unsupported`                               | Stem pointing east.                               |



