### Pointed Dripstone
Java Edition:

| Name               | Default value | Allowed values     | Description                                                               |
|--------------------|---------------|--------------------|---------------------------------------------------------------------------|
| thickness          | `tip`         | `tip_merge`        |                                                                           |
|                    |               | `tip`              |                                                                           |
|                    |               | `frustum`          |                                                                           |
|                    |               | `middle`           |                                                                           |
|                    |               | `base`             |                                                                           |
| vertical_direction | `up`          | `up`<br/>`down`    | The direction of the pointed dripstone.                                   |
| waterlogged        | `false`       | `true`<br/>`false` | Whether or not there's water in the same place as this pointed dripstone. |

Bedrock Edition:

| Name                | Metadata Bits | Default value | Allowed values     | Values forMetadata Bits | Description                                            |
|---------------------|---------------|---------------|--------------------|-------------------------|--------------------------------------------------------|
| dripstone_thickness | Not Supported | `tip`         | `merge`            | `Unsupported`           |                                                        |
|                     |               |               | `tip`              | `Unsupported`           |                                                        |
|                     |               |               | `frustum`          | `Unsupported`           |                                                        |
|                     |               |               | `middle`           | `Unsupported`           |                                                        |
|                     |               |               | `base`             | `Unsupported`           |                                                        |
| hanging             | Not Supported | `true`        | `false`<br/>`true` | `Unsupported`           | Whether or not the pointed dripstone is pointing down. |



### Pressure Plates
Java Edition:

** Stone and wooden pressure plates **
| Name    | Default value | Allowed values     | Description                                           |
|---------|---------------|--------------------|-------------------------------------------------------|
| powered | `false`       | `false`<br/>`true` | True if pressure plate is depressed, providing power. |

** Weighted pressure plates **
| Name  | Default value | Allowed values                                                                                                                    | Description                                                                                 |
|-------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| power | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | Specifies the redstone power level currently being produced by the weighted pressure plate. |

Bedrock Edition:

** Stone and wooden pressure plates **
| Name            | Metadata Bits | Default value | Allowed values                                                                                                    | Values forMetadata Bits | Description                                      |
|-----------------|---------------|---------------|-------------------------------------------------------------------------------------------------------------------|-------------------------|--------------------------------------------------|
| redstone_signal | `0x1`         | `0`           | `0`<br/>`1`                                                                                                       | `0`<br/>`1`             | Specifies whether the pressure plate is pressed. |
|                 |               |               | `2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | `Unsupported`           | Unused                                           |

** Weighted pressure plates **
| Name            | Metadata Bits                       | Default value | Allowed values                                                                                                                    | Values forMetadata Bits                                                                                                           | Description                                                                        |
|-----------------|-------------------------------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| redstone_signal | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | Specifies the redstone power level currently being produced by the pressure plate. |

### Prismarine
Bedrock Edition:

| Name                  | Metadata Bits   | Default value | Allowed values | Values forMetadata Bits | Description       |
|-----------------------|-----------------|---------------|----------------|-------------------------|-------------------|
| prismarine_block_type | `0x1`<br/>`0x2` | `default`     | `bricks`       | `2`                     | Prismarine Bricks |
|                       |                 |               | `dark`         | `1`                     | Dark Prismarine   |
|                       |                 |               | `default`      | `0`                     | Prismarine        |



### Pumpkin and Carved Pumpkin
Java Edition:
Carved pumpkin:

| Name   | Default value | Allowed values                            | Description                                                                                                                        |
|--------|---------------|-------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| facing | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the pumpkin's carved face is facing.<br/>The opposite from the direction the player faces while placing the pumpkin. |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values                            | Values forMetadata Bits | Description                                                                                                                                                                            |
|------------------------------|---------------|---------------|-------------------------------------------|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| minecraft:cardinal_direction | Not Supported | `south`       | `east`<br/>`north`<br/>`south`<br/>`west` | `Unsupported`           | The direction the pumpkin and carved pumpkin are facing.<br/>The opposite from the direction the player faces while placing the pumpkins. Though it doesn't affect the pumpkin at all. |



#### Pumpkin Stem
Java Edition:
Growing

| Name | Default value | Allowed values                              | Description                                         |
|------|---------------|---------------------------------------------|-----------------------------------------------------|
| age  | `0`           | `0`                                         | A newly planted stem.                               |
|      |               | `1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6` | Intermediate growth stages of the stem.             |
|      |               | `7`                                         | A fully mature stem, capable of producing pumpkins. |

Attached

| Name   | Default value | Allowed values                            | Description                                 |
|--------|---------------|-------------------------------------------|---------------------------------------------|
| facing | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction from the stem to the pumpkin. |

Bedrock Edition:

| Name             | Metadata Bits             | Default value | Allowed values                              | Values forMetadata Bits                     | Description                                         |
|------------------|---------------------------|---------------|---------------------------------------------|---------------------------------------------|-----------------------------------------------------|
| growth           | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`                                         | `0`                                         | A newly planted stem.                               |
|                  |                           |               | `1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6` | `1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6` | Intermediate growth stages of the stem.             |
|                  |                           |               | `7`                                         | `7`                                         | A fully mature stem, capable of producing pumpkins. |
| facing_direction | Not Supported             | `0`           | `0`<br/>`1`                                 | `Unsupported`                               | Unused                                              |
|                  |                           |               | `2`                                         | `Unsupported`                               | Stem pointing north.                                |
|                  |                           |               | `3`                                         | `Unsupported`                               | Stem pointing south.                                |
|                  |                           |               | `4`                                         | `Unsupported`                               | Stem pointing west.                                 |
|                  |                           |               | `5`                                         | `Unsupported`                               | Stem pointing east.                                 |



### Purpur and Quartz Pillar
Bedrock Edition:

| Name        | Metadata Bits   | Default value | Allowed values | Values forMetadata Bits | Description                               |
|-------------|-----------------|---------------|----------------|-------------------------|-------------------------------------------|
| chisel_type | `0x1`<br/>`0x2` | `default`     | `default`      | `0`                     | Purpur Block                              |
|             |                 |               | `chiseled`     | `1`                     | Chiseled Purpur(Unused)                   |
|             |                 |               | `lines`        | `2`                     | Purpur Pillar                             |
|             |                 |               | `smooth`       | `3`                     | Smooth Purpur(Unused)                     |
| pillar_axis | `0x4`<br/>`0x8` | `y`           | `x`            | `1`                     | The purpur block is oriented east–west.   |
|             |                 |               | `y`            | `0`                     | The purpur block is oriented vertically.  |
|             |                 |               | `z`            | `2`                     | The purpur block is oriented north–south. |



### Rails
#### Rail
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

