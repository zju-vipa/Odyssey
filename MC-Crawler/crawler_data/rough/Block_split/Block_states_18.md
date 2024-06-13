### Snow
Java Edition:

| Name   | Default value | Allowed values                                              | Description                                                                                                                                          |
|--------|---------------|-------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| layers | `1`           | `1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8` | The number of layers thick.<br/>Each layer adds two pixels to the block height, and each layer after the first adds two pixels to the collision box. |

Bedrock Edition:

| Name        | Metadata Bits             | Default value | Allowed values                                              | Values forMetadata Bits                                     | Description                                           |
|-------------|---------------------------|---------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------|
| height      | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7` | The number of layers in addition to the bottom layer. |
| covered_bit | `0x8`                     | `false`       | `true`<br/>`false`                                          | `0`<br/>`1`                                                 | True if the snow is covering a plant.                 |



### Sponge
Bedrock Edition:

| Name        | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description |
|-------------|---------------|---------------|----------------|-------------------------|-------------|
| sponge_type | `0x1`         | `dry`         | `dry`          | `0`                     | Sponge      |
|             |               |               | `wet`          | `1`                     | Wet Sponge  |



### Stairs
Java Edition:

| Name        | Default value | Allowed values                                                                   | Description                                                                                                                                                                                                                                                                                                                        |
|-------------|---------------|----------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing      | `north`       | `east`<br/>`north`<br/>`south`<br/>`west`                                        | The direction the stairs' full-block side faces.<br/>When placed in-game by a player, this matches the direction the player faces.                                                                                                                                                                                                 |
| half        | `bottom`      | `bottom`<br/>`top`                                                               | Top if the stairs are upside-down.                                                                                                                                                                                                                                                                                                 |
| shape       | `straight`    | `inner_left`<br/>`inner_right`<br/>`outer_left`<br/>`outer_right`<br/>`straight` | "straight" is the default stairs shape.<br/>"inner" is an "inside corner" stair shape, with two full-block and two stair-shaped side faces.<br/>"outer" is an "outside corner" stair shape, with two stair-shaped and two half-block side faces.<br/>"left" and "right" specify in which direction is the higher part of the step. |
| waterlogged | `false`       | `false`<br/>`true`                                                               | Whether or not there's water in the same place as these stairs.                                                                                                                                                                                                                                                                    |

Bedrock Edition:

| Name             | Metadata Bits   | Default value | Allowed values              | Values forMetadata Bits     | Description                                                                                        |
|------------------|-----------------|---------------|-----------------------------|-----------------------------|----------------------------------------------------------------------------------------------------|
| upside_down_bit  | `0x4`           | `false`       | `false`<br/>`true`          | `0`<br/>`1`                 | True if the stairs are upside-down.                                                                |
| weirdo_direction | `0x1`<br/>`0x2` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3` | `0`<br/>`1`<br/>`2`<br/>`3` | The direction the stairs' full-block side faces.0: East<br/>1: West<br/>2: South<br/>3: North<br/> |

### Stone Bricks
Bedrock Edition

| Name             | Metadata Bits             | Default value | Allowed values | Values forMetadata Bits | Description                                                |
|------------------|---------------------------|---------------|----------------|-------------------------|------------------------------------------------------------|
| stone_brick_type | `0x1`<br/>`0x2`<br/>`0x4` | `default`     | `default`      | `0`                     | Stone Bricks                                               |
|                  |                           |               | `mossy`        | `1`                     | Mossy Stone Bricks                                         |
|                  |                           |               | `cracked`      | `2`                     | Cracked Stone Bricks                                       |
|                  |                           |               | `chiseled`     | `3`                     | Chiseled Stone Bricks                                      |
|                  |                           |               | `smooth`       | `4`                     | Smooth Stone Bricks (unused, same texture as regular ones) |



### Stonecutter
Java Edition:

| Name   | Default value | Allowed values                            | Description                                                                                                               |
|--------|---------------|-------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| facing | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the stonecutter is facing.<br/>The opposite from the direction the player faces when placing a stonecutter. |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values                            | Values forMetadata Bits | Description                                                                                                               |
|------------------------------|---------------|---------------|-------------------------------------------|-------------------------|---------------------------------------------------------------------------------------------------------------------------|
| minecraft:cardinal_direction | Not Supported | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | `Unsupported`           | The direction the stonecutter is facing.<br/>The opposite from the direction the player faces when placing a stonecutter. |



### Structure Block
Java Edition:

| Name | Default value | Allowed values | Description            |
|------|---------------|----------------|------------------------|
| mode | `data`        | `corner`       | Corner Structure Block |
|      |               | `data`         | Data Structure Block   |
|      |               | `load`         | Load Structure Block   |
|      |               | `save`         | Save Structure Block   |

Bedrock Edition:

| Name                 | Metadata Bits             | Default value | Allowed values | Values forMetadata Bits | Description               |
|----------------------|---------------------------|---------------|----------------|-------------------------|---------------------------|
| structure_block_type | `0x1`<br/>`0x2`<br/>`0x4` | `data`        | `corner`       | `3`                     | Corner Structure Block    |
|                      |                           |               | `data`         | `0`                     | Data Structure Block      |
|                      |                           |               | `export`       | `5`                     | Export Structure Block    |
|                      |                           |               | `invalid`      | `4`                     | Inventory Structure Block |
|                      |                           |               | `load`         | `2`                     | Load Structure Block      |
|                      |                           |               | `save`         | `1`                     | Save Structure Block      |



### Structure Void
Bedrock Edition:

| Name                | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description    |
|---------------------|---------------|---------------|----------------|-------------------------|----------------|
| structure_void_type | `0x1`         | `void`        | `air`          | `1`                     | Structure Air  |
|                     |               |               | `void`         | `0`                     | Structure Void |



### Sugar Cane
Java Edition:

| Name | Default value | Allowed values                                                                                                                    | Description                                                                                                                                                                                              |
|------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| age  | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | A freshly planted cane – and a cane that has just grown cane above it – each have an age of 0.<br/>The age is incremented at random intervals.<br/>At age 15, a cane may try to grow more cane above it. |

Bedrock Edition:

| Name | Metadata Bits                       | Default value | Allowed values                                                                                                                    | Values forMetadata Bits                                                                                                           | Description                                                                                                                                                                                              |
|------|-------------------------------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| age  | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | A freshly planted cane – and a cane that has just grown cane above it – each have an age of 0.<br/>The age is incremented at random intervals.<br/>At age 15, a cane may try to grow more cane above it. |



### Sweet Berry Bush
Java Edition:

| Name | Default value | Allowed values | Description                                                                  |
|------|---------------|----------------|------------------------------------------------------------------------------|
| age  | `0`           | `0`            | Young plant                                                                  |
|      |               | `1`            | No berries                                                                   |
|      |               | `2`            | Some berries,usingthe bush gives 1–2sweet berriesand sets the age back to 1. |
|      |               | `3`            | Full berries,usingthe bush gives 2–3sweet berriesand sets the age back to 1. |

Bedrock Edition:

| Name   | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                                                     |
|--------|---------------|---------------|----------------|-------------------------|---------------------------------------------------------------------------------|
| growth | `0x1`         | `0`           | `0`            | `0`                     | Young plant                                                                     |
|        |               |               | `1`            | `1`                     | No berries                                                                      |
|        |               |               | `2`            | `2`                     | Some berries,usingthe bush gives 1–2sweet berriesand sets the growth back to 2. |
|        |               |               | `3`            | `3`                     | Full berries,usingthe bush gives 2–3sweet berriesand sets the growth back to 2. |



