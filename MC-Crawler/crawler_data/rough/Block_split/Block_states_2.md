### Beds
Java Edition:

| Name     | Default value | Allowed values                            | Description                                                                                                  |
|----------|---------------|-------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| facing   | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the head of the bed is pointing.<br/>The same direction the player faces when placing the bed. |
| occupied | `false`       | `false`<br/>`true`                        | True when a player or villager is using the bed.                                                             |
| part     | `foot`        | `foot`<br/>`head`                         | The half of the bed in the current block.                                                                    |

Bedrock Edition:

| Name           | Metadata Bits   | Default value | Allowed values              | Values forMetadata Bits     | Description                                                                                                                                  |
|----------------|-----------------|---------------|-----------------------------|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| direction      | `0x1`<br/>`0x2` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3` | `0`<br/>`1`<br/>`2`<br/>`3` | The direction the head of the bed is pointing.0:Head facing South<br/>1:Head facing West<br/>2:Head facing North<br/>3:Head facing East<br/> |
| head_piece_bit | `0x8`           | `true`        | `false`<br/>`true`          | `0`<br/>`1`                 | If the current block is the head part.                                                                                                       |
| occupied_bit   | `0x4`           | `false`       | `false`<br/>`true`          | `0`<br/>`1`                 | True when a player or villager is using the bed.                                                                                             |



### Bedrock
Bedrock Edition:

| Name           | Metadata Bits | Default value | Allowed values     | Values forMetadata Bits | Description                                      |
|----------------|---------------|---------------|--------------------|-------------------------|--------------------------------------------------|
| infiniburn_bit | `0x1`         | `false`       | `false`<br/>`true` | `0`<br/>`1`             | Specifies if this bedrock can burn indefinitely. |



### Beehive and Bee Nest
Java Edition:

| Name        | Default value | Allowed values                              | Description                                                                                                                                                     |
|-------------|---------------|---------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing      | `north`       | `east`<br/>`north`<br/>`south`<br/>`west`   | The opposite from the direction the player faces while placing the block.                                                                                       |
| honey_level | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | Every pollinated bee that leaves the hive after working increases the honey level by one. When at level 5, honey can be bottled or honeycombs can be harvested. |

Bedrock Edition:

| Name        | Metadata Bits | Default value | Allowed values                              | Values forMetadata Bits | Description                                                                                                                                                     |
|-------------|---------------|---------------|---------------------------------------------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| direction   | Not Supported | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`                 | `Unsupported`           | The direction the block faces.0: south<br/>1: west<br/>2: north<br/>3: east<br/>                                                                                |
| honey_level | Not Supported | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | `Unsupported`           | Every pollinated bee that leaves the hive after working increases the honey level by one. When at level 5, honey can be bottled or honeycombs can be harvested. |



### Beetroots
Java Edition:

| Name | Default value | Allowed values | Description  |
|------|---------------|----------------|--------------|
| age  | `0`           | `0`            |              |
|      |               | `1`            |              |
|      |               | `2`            |              |
|      |               | `3`            | Fully grown. |

Bedrock Edition:

| Name   | Metadata Bits             | Default value | Allowed values      | Values forMetadata Bits | Description  |
|--------|---------------------------|---------------|---------------------|-------------------------|--------------|
| growth | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`<br/>`1`         | `0`<br/>`1`             |              |
|        |                           |               | `2`<br/>`3`         | `2`<br/>`3`             |              |
|        |                           |               | `4`<br/>`5`<br/>`6` | `4`<br/>`5`<br/>`6`     |              |
|        |                           |               | `7`                 | `7`                     | Fully grown. |



### Bell
Java Edition:

| Name       | Default value | Allowed values                                            | Description                                                                                             |
|------------|---------------|-----------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| attachment | `floor`       | `ceiling`<br/>`double_wall`<br/>`floor`<br/>`single_wall` | What the bell is attached to.                                                                           |
| facing     | `north`       | `east`<br/>`north`<br/>`south`<br/>`west`                 | The direction the bell is facing.<br/>Opposite from the direction the player faces when placing a bell. |
| powered    | `false`       | `true`<br/>`false`                                        | Whether the bell is attached to a power source, such as a redstone torch.                               |

Bedrock Edition:

| Name       | Metadata Bits   | Default value | Allowed values                                     | Values forMetadata Bits     | Description                                                                                                                                                                                            |
|------------|-----------------|---------------|----------------------------------------------------|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| attachment | `0x4`<br/>`0x8` | `standing`    | `standing`<br/>`hanging`<br/>`side`<br/>`multiple` | `0`<br/>`1`<br/>`2`<br/>`3` | What the bell is attached to.                                                                                                                                                                          |
| direction  | `0x1`<br/>`0x2` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`                        | `0`<br/>`1`<br/>`2`<br/>`3` | The direction the bell is facing. Opposite from the direction a player faces when placing the block.0: South facing bell<br/>1: West facing bell<br/>2: North facing bell<br/>3: East facing bell<br/> |
| toggle_bit | `0x10`          | `false`       | `false`<br/>`true`                                 | `0`<br/>`1`                 | Each time the bell is rung, this value toggles between true and false.                                                                                                                                 |



### Big Dripleaf
Java Edition:
Leaf:

| Name        | Default value | Allowed values                                 | Description                                                                                                                    |
|-------------|---------------|------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| facing      | `north`       | `east`<br/>`north`<br/>`south`<br/>`west`      | The direction the big dripleaf is facing.<br/>The opposite from the direction the player faces while placing the big dripleaf. |
| tilt        | `none`        | `full`<br/>`none`<br/>`partial`<br/>`unstable` | How far this big dripleaf is tilted.                                                                                           |
| waterlogged | `false`       | `false`<br/>`true`                             | Whether there is water in the same place as this big dripleaf.                                                                 |

Stem:

| Name        | Default value | Allowed values                            | Description                                                         |
|-------------|---------------|-------------------------------------------|---------------------------------------------------------------------|
| facing      | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the big dripleaf stem is facing.                      |
| waterlogged | `false`       | `false`<br/>`true`                        | Whether there is water in the same place as this big dripleaf stem. |


Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values                                           | Values forMetadata Bits | Description                                                                                                                    |
|------------------------------|---------------|---------------|----------------------------------------------------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| big_dripleaf_head            | Not Supported | `1`           | `0`<br/>`1`                                              | `Unsupported`           | Whether this is the leaf part or the stem part of big dripleaf.                                                                |
| big_dripleaf_tilt            | Not Supported | `none`        | `none`<br/>`unstable`<br/>`partial_tilt`<br/>`full_tilt` | `Unsupported`           | How far this big dripleaf is tilted.                                                                                           |
| minecraft:cardinal_direction | Not Supported | `south`       | `east`<br/>`north`<br/>`south`<br/>`west`                | `Unsupported`           | The direction the big dripleaf is facing.<br/>The opposite from the direction the player faces while placing the big dripleaf. |



### Blast Furnace
Java Edition:

| Name   | Default value | Allowed values                            | Description                                                                                                                            |
|--------|---------------|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| facing | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the blast furnace's opening faces.<br/>The opposite from the direction the player faces while placing the blast furnace. |
| lit    | `false`       | `false`<br/>`true`                        | If the blast furnace is lit.                                                                                                           |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values                            | Values forMetadata Bits | Description                                                                                                                            |
|------------------------------|---------------|---------------|-------------------------------------------|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| minecraft:cardinal_direction | Not Supported | `south`       | `east`<br/>`north`<br/>`south`<br/>`west` | `Unsupported`           | The direction the blast furnace's opening faces.<br/>The opposite from the direction the player faces while placing the blast furnace. |



