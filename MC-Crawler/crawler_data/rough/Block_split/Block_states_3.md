### Block of Bamboo and Block of Stripped Bamboo
Java Edition:

| Name | Default value | Allowed values | Description                        |
|------|---------------|----------------|------------------------------------|
| axis | `y`           | `x`            | The block is oriented east–west.   |
|      |               | `y`            | The block is oriented vertically.  |
|      |               | `z`            | The block is oriented north–south. |

Bedrock Edition:

| Name        | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                        |
|-------------|---------------|---------------|----------------|-------------------------|------------------------------------|
| pillar_axis | Not Supported | `y`           | `x`            | `Unsupported`           | The block is oriented east-west.   |
|             |               |               | `y`            | `Unsupported`           | The block is oriented vertically.  |
|             |               |               | `z`            | `Unsupported`           | The block is oriented north-south. |



### Bone Block
Java Edition:

| Name | Default value | Allowed values | Description                             |
|------|---------------|----------------|-----------------------------------------|
| axis | `y`           | `x`            | The bone block is oriented east–west.   |
|      |               | `y`            | The bone block is oriented vertically.  |
|      |               | `z`            | The bone block is oriented north–south. |

Bedrock Edition:

| Name        | Metadata Bits   | Default value | Allowed values              | Values forMetadata Bits     | Description                                |
|-------------|-----------------|---------------|-----------------------------|-----------------------------|--------------------------------------------|
| pillar_axis | `0x4`<br/>`0x8` | `y`           | `y`<br/>`x`<br/>`z`         | `0`<br/>`1`<br/>`2`         | The axis along which the block is oriented |
| deprecated  | `0x1`<br/>`0x2` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3` | `0`<br/>`1`<br/>`2`<br/>`3` | Unused, has no effect in game.             |



### Border
Bedrock Edition and Minecraft Education:

| Name                       | Metadata Bits | Default value | Allowed values                | Values forMetadata Bits | Description                                             |
|----------------------------|---------------|---------------|-------------------------------|-------------------------|---------------------------------------------------------|
| wall_connection_type_east  | Not Supported | `none`        | `none`<br/>`short`<br/>`tall` | `Unsupported`           | How the wall extends from the center post to the east.  |
| wall_connection_type_north | Not Supported | `none`        | `none`<br/>`short`<br/>`tall` | `Unsupported`           | How the wall extends from the center post to the north. |
| wall_connection_type_south | Not Supported | `none`        | `none`<br/>`short`<br/>`tall` | `Unsupported`           | How the wall extends from the center post to the south. |
| wall_connection_type_west  | Not Supported | `none`        | `none`<br/>`short`<br/>`tall` | `Unsupported`           | How the wall extends from the center post to the west.  |
| wall_post_bit              | Not Supported | `true`        | `false`<br/>`true`            | `Unsupported`           | Whether or not the wall has a center post.              |



### Brewing Stand
Java Edition:

| Name         | Default value | Allowed values     | Description                      |
|--------------|---------------|--------------------|----------------------------------|
| has_bottle_0 | `false`       | `false`<br/>`true` | True when a bottle is in slot 1. |
| has_bottle_1 | `false`       | `false`<br/>`true` | True when a bottle is in slot 2. |
| has_bottle_2 | `false`       | `false`<br/>`true` | True when a bottle is in slot 3. |

Bedrock Edition:

| Name                     | Metadata Bits | Default value | Allowed values     | Values forMetadata Bits | Description                      |
|--------------------------|---------------|---------------|--------------------|-------------------------|----------------------------------|
| brewing_stand_slot_a_bit | `0x1`         | `false`       | `false`<br/>`true` | `0`<br/>`1`             | True when a bottle is in slot 1. |
| brewing_stand_slot_b_bit | `0x2`         | `false`       | `false`<br/>`true` | `0`<br/>`1`             | True when a bottle is in slot 2. |
| brewing_stand_slot_c_bit | `0x4`         | `false`       | `false`<br/>`true` | `0`<br/>`1`             | True when a bottle is in slot 3. |



### Bubble Column
Java Edition:

| Name | Default value | Allowed values     | Description                                                  |
|------|---------------|--------------------|--------------------------------------------------------------|
| drag | `true`        | `false`<br/>`true` | Determines whether the bubble column is upward or whirlpool. |

Bedrock Edition:

| Name      | Metadata Bits | Default value | Allowed values     | Values forMetadata Bits | Description                                                  |
|-----------|---------------|---------------|--------------------|-------------------------|--------------------------------------------------------------|
| drag_down | `0x1`         | `false`       | `false`<br/>`true` | `0`<br/>`1`             | Determines whether the bubble column is upward or whirlpool. |



### Buttons
Java Edition:

| Name    | Default value | Allowed values                            | Description                                                                                                                      |
|---------|---------------|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| face    | `wall`        | `ceiling`<br/>`floor`<br/>`wall`          | The face of the block it's placed on.<br/>Floor is on top of a block, ceiling is on the bottom, and wall is on one of its sides. |
| facing  | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction it's facing.<br/>Opposite to the direction the player is facing if placed on the side of a block.                  |
| powered | `false`       | `false`<br/>`true`                        | If true, the button is currently activated.                                                                                      |

Bedrock Edition:

| Name               | Metadata Bits             | Default value | Allowed values                              | Values forMetadata Bits                     | Description                                                                                                                                                                                                                                                                 |
|--------------------|---------------------------|---------------|---------------------------------------------|---------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| button_pressed_bit | `0x8`                     | `false`       | `false`<br/>`true`                          | `0`<br/>`1`                                 | If the button is currently activated.                                                                                                                                                                                                                                       |
| facing_direction   | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | The direction it's facing.0: Button on block bottom facing down<br/>1: Button on block top facing up<br/>2: Button on block side facing north<br/>3: Button on block side facing south<br/>4: Button on block side facing west<br/>5: Button on block side facing east<br/> |



### Cactus
Java Edition

| Name | Default value | Allowed values                                                                                                                    | Description                                                                                                                                                                                                        |
|------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| age  | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | A freshly-planted cactus – and a cactus that has just grown cactus above it – each have an age of 0.<br/>The age is incremented at random intervals.<br/>At age 15, a cactus may try to grow more cactus above it. |

Bedrock Edition

| Name | Metadata Bits                       | Default value | Allowed values                                                                                                                    | Values forMetadata Bits                                                                                                           | Description                                                                                                                                                                                                        |
|------|-------------------------------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| age  | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | A freshly-planted cactus – and a cactus that has just grown cactus above it – each have an age of 0.<br/>The age is incremented at random intervals.<br/>At age 15, a cactus may try to grow more cactus above it. |



### Cake
Java Edition
Cakes:

| Name  | Default value | Allowed values                                      | Description                          |
|-------|---------------|-----------------------------------------------------|--------------------------------------|
| bites | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6` | Number of bites taken from the cake. |

Candle cakes:

| Name | Default value | Allowed values     | Description                            |
|------|---------------|--------------------|----------------------------------------|
| lit  | `false`       | `false`<br/>`true` | Whether the candle on the cake is lit. |

Bedrock Edition
Cakes:

| Name         | Metadata Bits             | Default value | Allowed values                                      | Values forMetadata Bits                             | Description                          |
|--------------|---------------------------|---------------|-----------------------------------------------------|-----------------------------------------------------|--------------------------------------|
| bite_counter | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6` | Number of bites taken from the cake. |

Candle cakes:

| Name | Metadata Bits | Default value | Allowed values     | Values forMetadata Bits | Description                            |
|------|---------------|---------------|--------------------|-------------------------|----------------------------------------|
| lit  | `0x1`         | `false`       | `false`<br/>`true` | `0`<br/>`1`             | Whether the candle on the cake is lit. |



