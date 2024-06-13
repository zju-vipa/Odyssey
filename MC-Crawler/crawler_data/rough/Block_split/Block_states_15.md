#### 
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

### Redstone Comparator
Java Edition:

| Name    | Default value | Allowed values                            | Description                                                                                                                                               |
|---------|---------------|-------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing  | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction from theoutputside to theinputside of the comparator,<br/>or the opposite from the direction the player faces while placing the comparator. |
| mode    | `compare`     | `compare`<br/>`subtract`                  | Specifies the current mode of the redstone comparator.                                                                                                    |
| powered | `false`       | `false`<br/>`true`                        | True if the redstone comparator is being powered.                                                                                                         |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values                            | Values forMetadata Bits | Description                                                                                                                                               |
|------------------------------|---------------|---------------|-------------------------------------------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| minecraft:cardinal_direction | Not Supported | `south`       | `east`<br/>`north`<br/>`south`<br/>`west` | `Unsupported`           | The direction from theoutputside to theinputside of the comparator,<br/>or the opposite from the direction the player faces while placing the comparator. |
| output_lit_bit               | `0x8`         | `false`       | `false`<br/>`true`                        | `0`<br/>`1`             | True if the redstone comparator is being powered.                                                                                                         |
| output_subtract_bit          | `0x4`         | `false`       | `false`<br/>`true`                        | `0`<br/>`1`             | Specifies the current mode of the redstone comparator.                                                                                                    |



### Redstone Dust
Java Edition:

| Name  | Default value | Allowed values                                                                                                                    | Description                                                           |
|-------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| east  | `none`        | `none`<br/>`side`<br/>`up`                                                                                                        | The way redstone dust connects to the east, side can also mean down.  |
| north | `none`        | `none`<br/>`side`<br/>`up`                                                                                                        | The way redstone dust connects to the north, side can also mean down. |
| power | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | The redstone dust's current power level.                              |
| south | `none`        | `none`<br/>`side`<br/>`up`                                                                                                        | The way redstone dust connects to the south, side can also mean down. |
| west  | `none`        | `none`<br/>`side`<br/>`up`                                                                                                        | The way redstone dust connects to the west, side can also mean down.  |

Bedrock Edition:

| Name            | Metadata Bits                       | Default value | Allowed values                                                                                                                    | Values forMetadata Bits                                                                                                           | Description                              |
|-----------------|-------------------------------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|------------------------------------------|
| redstone_signal | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | The redstone dust's current power level. |



### Redstone Lamp
Java Edition:

| Name | Default value | Allowed values     | Description                  |
|------|---------------|--------------------|------------------------------|
| lit  | `false`       | `false`<br/>`true` | If the redstone lamp is lit. |



### Redstone Ore
Java Edition:

| Name | Default value | Allowed values     | Description                 |
|------|---------------|--------------------|-----------------------------|
| lit  | `false`       | `false`<br/>`true` | If the redstone ore is lit. |



### Redstone Repeater
Java Edition:

| Name    | Default value | Allowed values                            | Description                                                                                                                                      |
|---------|---------------|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| delay   | `1`           | `1`<br/>`2`<br/>`3`<br/>`4`               | The redstone repeater's delay in redstone ticks.                                                                                                 |
| facing  | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction from theoutputside to theinputside of a repeater.<br/>The opposite from the direction the player faces while placing the repeater. |
| locked  | `false`       | `false`<br/>`true`                        | True if the repeater is currently locked.                                                                                                        |
| powered | `false`       | `false`<br/>`true`                        | If the redstone repeater is lit.                                                                                                                 |

Bedrock Edition:

| Name                         | Metadata Bits   | Default value | Allowed values                            | Values forMetadata Bits     | Description                                                                                                                                      |
|------------------------------|-----------------|---------------|-------------------------------------------|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| minecraft:cardinal_direction | Not Supported   | `south`       | `east`<br/>`north`<br/>`south`<br/>`west` | `Unsupported`               | The direction from theoutputside to theinputside of a repeater.<br/>The opposite from the direction the player faces while placing the repeater. |
| repeater_delay               | `0x4`<br/>`0x8` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`               | `0`<br/>`1`<br/>`2`<br/>`3` | The redstone repeater's delay in redstone ticks minus 1.                                                                                         |



### Redstone Torch
Java Edition:
Floor:

| Name | Default value | Allowed values     | Description          |
|------|---------------|--------------------|----------------------|
| lit  | `true`        | `false`<br/>`true` | If the torch is lit. |

Wall:

| Name   | Default value | Allowed values                            | Description                                   |
|--------|---------------|-------------------------------------------|-----------------------------------------------|
| facing | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the top of the torch is facing. |
| lit    | `true`        | `false`<br/>`true`                        | If the torch is lit.                          |

Bedrock Edition:

| Name                   | Metadata Bits             | Default value | Allowed values                                      | Values forMetadata Bits             | Description                                                                                                                                  |
|------------------------|---------------------------|---------------|-----------------------------------------------------|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| torch_facing_direction | `0x1`<br/>`0x2`<br/>`0x4` | `west`        | `west`<br/>`east`<br/>`north`<br/>`south`<br/>`top` | `1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | The face of the block that the torch is attached to. If the torch is a wall torch, the top of the torch faces opposite to this direction.[3] |
|                        |                           |               | `unknown`                                           | `0`                                 | Unused                                                                                                                                       |

### Respawn Anchor
Java Edition:

| Name    | Default value | Allowed values                      | Description                                   |
|---------|---------------|-------------------------------------|-----------------------------------------------|
| charges | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4` | How many charges the Respawn Anchor has left. |

Bedrock Edition:

| Name                  | Metadata Bits             | Default value | Allowed values                      | Values forMetadata Bits             | Description                                   |
|-----------------------|---------------------------|---------------|-------------------------------------|-------------------------------------|-----------------------------------------------|
| respawn_anchor_charge | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4` | How many charges the Respawn Anchor has left. |



