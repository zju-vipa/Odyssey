#### Ender Chest
Java Edition:

| Name        | Default value | Allowed values                            | Description                                                                                                                    |
|-------------|---------------|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| facing      | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the ender chest's latch is on.<br/>The opposite from the direction the player faces when placing an ender chest. |
| waterlogged | `false`       | `false`<br/>`true`                        | Whether or not there's water in the same place as this ender chest.                                                            |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values                            | Values forMetadata Bits | Description                                                                                                                    |
|------------------------------|---------------|---------------|-------------------------------------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| minecraft:cardinal_direction | Not Supported | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | `Unsupported`           | The direction the ender chest's latch is on.<br/>The opposite from the direction the player faces when placing an ender chest. |



### Chiseled Bookshelf
Java Edition:

| Name            | Default value | Allowed values                            | Description                                                                                              |
|-----------------|---------------|-------------------------------------------|----------------------------------------------------------------------------------------------------------|
| facing          | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the bookshelf is facing.<br/>Opposite from the direction the player faces when placing it. |
| slot_0_occupied | `false`       | `true`<br/>`false`                        | Whether there is a book in the upper-left slot.                                                          |
| slot_1_occupied | `false`       | `true`<br/>`false`                        | Whether there is a book in the upper-middle slot.                                                        |
| slot_2_occupied | `false`       | `true`<br/>`false`                        | Whether there is a book in the upper-right slot.                                                         |
| slot_3_occupied | `false`       | `true`<br/>`false`                        | Whether there is a book in the lower-left slot.                                                          |
| slot_4_occupied | `false`       | `true`<br/>`false`                        | Whether there is a book in the lower-middle slot.                                                        |
| slot_5_occupied | `false`       | `true`<br/>`false`                        | Whether there is a book in the lower-right slot.                                                         |

Bedrock Edition:

| Name         | Metadata Bits | Default value | Allowed values              | Values forMetadata Bits | Description                                                                                                                                                                            |
|--------------|---------------|---------------|-----------------------------|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| books_stored | Not Supported | `0`           | `0 — 63`                    | `Unsupported`           | The confguration of the books in the bookshelf.                                                                                                                                        |
| direction    | Not Supported | `0`           | `0`<br/>`1`<br/>`2`<br/>`3` | `Unsupported`           | The direction the bookshelf is facing.<br/>Opposite from the direction the player faces when placing it.0: facing South<br/>1: facing West<br/>2: facing North<br/>3: facing East<br/> |

### Chorus Flower
Java Edition

| Name | Default value | Allowed values                      | Description                                                                                                                                                                   |
|------|---------------|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| age  | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4` | A freshly planted chorus flower starts at age 0. The age is incremented when a chorus flower turns horizontally and/or generates additional chorus flowers on the same plant. |
|      |               | `5`                                 | At age 5, the chorus flower does not grow further. A chorus flower can become age 5 at any time.                                                                              |

Bedrock Edition

| Name | Metadata Bits             | Default value | Allowed values                                                                    | Values forMetadata Bits             | Description                                                                                                                                                                   |
|------|---------------------------|---------------|-----------------------------------------------------------------------------------|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| age  | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`                                               | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4` | A freshly planted chorus flower starts at age 0. The age is incremented when a chorus flower turns horizontally and/or generates additional chorus flowers on the same plant. |
|      |                           |               | `5`                                                                               | `5`                                 | At age 5, the chorus flower does not grow further. A chorus flower can become age 5 at any time.                                                                              |
|      |                           |               | `6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | `Unsupported`                       | Unused                                                                                                                                                                        |



### Chorus Plant
Java Edition:

| Name  | Default value | Allowed values     | Description                                                                       |
|-------|---------------|--------------------|-----------------------------------------------------------------------------------|
| down  | `false`       | `false`<br/>`true` | When true, the plant extends out from the center of the plant-block down.         |
| east  | `false`       | `false`<br/>`true` | When true, the plant extends out from the center of the plant-block to the east.  |
| north | `false`       | `false`<br/>`true` | When true, the plant extends out from the center of the plant-block to the north. |
| south | `false`       | `false`<br/>`true` | When true, the plant extends out from the center of the plant-block to the south. |
| up    | `false`       | `false`<br/>`true` | When true, the plant extends out from the center of the plant-block up.           |
| west  | `false`       | `false`<br/>`true` | When true, the plant extends out from the center of the plant-block to the west.  |



### Cocoa
Java Edition:

| Name   | Default value | Allowed values                            | Description                                                                                              |
|--------|---------------|-------------------------------------------|----------------------------------------------------------------------------------------------------------|
| age    | `0`           | `0`<br/>`1`<br/>`2`                       | The stage of the pod's growth, 2 is fully grown.                                                         |
| facing | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction from the cocoa bean to the log.<br/>The direction the player faces when placing the cocoa. |

Bedrock Edition:

| Name      | Metadata Bits   | Default value | Allowed values                                                                                            | Values forMetadata Bits     | Description                                                                                                                                                     |
|-----------|-----------------|---------------|-----------------------------------------------------------------------------------------------------------|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| age       | `0x4`<br/>`0x8` | `0`           | `0`<br/>`1`<br/>`2`                                                                                       | `0`<br/>`1`<br/>`2`         | The stage of the pod's growth, 2 is fully grown.                                                                                                                |
|           |                 |               | `3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | `Unsupported`               | Unused                                                                                                                                                          |
| direction | `0x1`<br/>`0x2` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`                                                                               | `0`<br/>`1`<br/>`2`<br/>`3` | The direction from the cocoa bean to the log.0: Attached to the south<br/>1: Attached to the east<br/>2: Attached to the north<br/>3: Attached to the west<br/> |



### Command Blocks
Java Edition:

| Name        | Default value | Allowed values                                                | Description                                       |
|-------------|---------------|---------------------------------------------------------------|---------------------------------------------------|
| conditional | `false`       | `false`<br/>`true`                                            | True if the command block is in conditional mode. |
| facing      | `north`       | `down`<br/>`east`<br/>`north`<br/>`south`<br/>`up`<br/>`west` | The direction the command block is pointing.      |

Bedrock Edition:

| Name             | Metadata Bits             | Default value | Allowed values                              | Values forMetadata Bits                     | Description                                                                                                                                                    |
|------------------|---------------------------|---------------|---------------------------------------------|---------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| conditional_bit  | `0x8`                     | `false`       | `false`<br/>`true`                          | `0`<br/>`1`                                 | True if the command block is in conditional mode.                                                                                                              |
| facing_direction | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | The direction the command block is pointing.0: facing down<br/>1: facing up<br/>2: facing north<br/>3: facing south<br/>4: facing west<br/>5: facing east<br/> |



### Composter
Java Edition:

| Name  | Default value | Allowed values                                                      | Description                                                            |
|-------|---------------|---------------------------------------------------------------------|------------------------------------------------------------------------|
| level | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8` | When at level 8, bone meal is able to be collected from the composter. |

Bedrock Edition:

| Name                 | Metadata Bits                       | Default value | Allowed values                                                      | Values forMetadata Bits                                             | Description                                                            |
|----------------------|-------------------------------------|---------------|---------------------------------------------------------------------|---------------------------------------------------------------------|------------------------------------------------------------------------|
| composter_fill_level | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8` | When at level 8, bone meal is able to be collected from the composter. |



