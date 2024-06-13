### Water
Java Edition:

| Name  | Default value | Allowed values                                                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| level | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | If bit 0x8 is set, this fluid is "falling" and spreads only downward. At this level, the lower bits are essentially ignored, since this block is then at its highest fluid level. This level is equal to the falling water above, equal to 8 plus the level of the non-falling water above it.The lower three bits are the fluid block's level. 0 is the highest fluid level (not necessarily filling the block - this depends on the neighboring fluid blocks above each upper corner of the block). Data values increase as the fluid level of the block drops: 1 is the next highest, 2 lower, on through 7, the lowest fluid level. Along a line on a flat plane, water drops one level per meter. |

Bedrock Edition:
Water and flowing water

| Name         | Metadata Bits                       | Default value | Allowed values                                                                                                                    | Values forMetadata Bits                                                                                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|--------------|-------------------------------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| liquid_depth | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | If bit 0x8 is set, this fluid is "falling" and spreads only downward. At this level, the lower bits are essentially ignored, since this block is then at its highest fluid level. This level is equal to the falling water above, equal to 8 plus the level of the non-falling water above it.The lower three bits are the fluid block's level. 0 is the highest fluid level (not necessarily filling the block - this depends on the neighboring fluid blocks above each upper corner of the block). Data values increase as the fluid level of the block drops: 1 is the next highest, 2 lower, on through 7, the lowest fluid level. Along a line on a flat plane, water drops one level per meter. |



### Weeping Vines
Java Edition
Weeping Vines:

| Name | Default value | Allowed values                                                                                                                                                                                                              | Description                                        |
|------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| age  | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15`<br/>`16`<br/>`17`<br/>`18`<br/>`19`<br/>`20`<br/>`21`<br/>`22`<br/>`23`<br/>`24`<br/>`25` | Increments for every block the weeping vine grows. |

Bedrock Edition

| Name              | Metadata Bits                                  | Default value | Allowed values                                                                                                                                                                                                              | Values forMetadata Bits                                                                                                                                                                                                     | Description                                        |
|-------------------|------------------------------------------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| weeping_vines_age | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8`<br/>`0x10` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15`<br/>`16`<br/>`17`<br/>`18`<br/>`19`<br/>`20`<br/>`21`<br/>`22`<br/>`23`<br/>`24`<br/>`25` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15`<br/>`16`<br/>`17`<br/>`18`<br/>`19`<br/>`20`<br/>`21`<br/>`22`<br/>`23`<br/>`24`<br/>`25` | Increments for every block the weeping vine grows. |



### Wheat crop
Java Edition:

| Name | Default value | Allowed values | Description  |
|------|---------------|----------------|--------------|
| age  | `0`           | `0`            |              |
|      |               | `1`            |              |
|      |               | `2`            |              |
|      |               | `3`            |              |
|      |               | `4`            |              |
|      |               | `5`            |              |
|      |               | `6`            |              |
|      |               | `7`            | Fully grown. |

Bedrock Edition:

| Name   | Metadata Bits             | Default value | Allowed values | Values forMetadata Bits | Description  |
|--------|---------------------------|---------------|----------------|-------------------------|--------------|
| growth | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`            | `0`                     |              |
|        |                           |               | `1`            | `1`                     |              |
|        |                           |               | `2`            | `2`                     |              |
|        |                           |               | `3`            | `3`                     |              |
|        |                           |               | `4`            | `4`                     |              |
|        |                           |               | `5`            | `5`                     |              |
|        |                           |               | `6`            | `6`                     |              |
|        |                           |               | `7`            | `7`                     | Fully grown. |



### Wood
Java Edition:

| Name | Default value | Allowed values | Description                                 |
|------|---------------|----------------|---------------------------------------------|
| axis | `y`           | `x`            | The wood or hyphae is oriented east–west.   |
|      |               | `y`            | The wood or hyphae is oriented vertically.  |
|      |               | `z`            | The wood or hyphae is oriented north–south. |

Bedrock Edition:

| Name        | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                 |
|-------------|---------------|---------------|----------------|-------------------------|---------------------------------------------|
| pillar_axis | Not Supported | `y`           | `x`            | `Unsupported`           | The wood or hyphae is oriented east–west.   |
|             |               |               | `y`            | `Unsupported`           | The wood or hyphae is oriented vertically.  |
|             |               |               | `z`            | `Unsupported`           | The wood or hyphae is oriented north–south. |



## List of fluid states
### Water
Java Edition:
Water

| Name    | Default value | Allowed values     | Description   |
|---------|---------------|--------------------|---------------|
| falling | `false`       | `true`<br/>`false` | Always false. |

Flowing water

| Name    | Default value | Allowed values                                              | Description                                                 |
|---------|---------------|-------------------------------------------------------------|-------------------------------------------------------------|
| falling | `false`       | `true`<br/>`false`                                          | True for falling water, false for water with a block below. |
| level   | `1`           | `1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8` | Height of the water, 8 when the water is falling.           |

### Lava
Java Edition:
Lava

| Name    | Default value | Allowed values     | Description   |
|---------|---------------|--------------------|---------------|
| falling | `false`       | `true`<br/>`false` | Always false. |

Flowing lava

| Name    | Default value | Allowed values                                              | Description                                               |
|---------|---------------|-------------------------------------------------------------|-----------------------------------------------------------|
| falling | `false`       | `false`<br/>`true`                                          | True for falling lava, false for lava with a block below. |
| level   | `1`           | `1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8` | Height of the lava, 8 when the lava is falling.           |


