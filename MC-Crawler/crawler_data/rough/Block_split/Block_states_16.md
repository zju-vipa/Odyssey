### Sand and Red Sand
Bedrock Edition:

| Name      | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description |
|-----------|---------------|---------------|----------------|-------------------------|-------------|
| sand_type | `0x1`         | `normal`      | `normal`       | `0`                     | Sand        |
|           |               |               | `red`          | `1`                     | Red Sand    |



### Sandstone and Red Sandstone
Bedrock Edition:

| Name            | Metadata Bits   | Default value | Allowed values | Values forMetadata Bits | Description        |
|-----------------|-----------------|---------------|----------------|-------------------------|--------------------|
| sand_stone_type | `0x1`<br/>`0x2` | `default`     | `default`      | `0`                     | Sandstone          |
|                 |                 |               | `heiroglyphs`  | `1`                     | Chiseled Sandstone |
|                 |                 |               | `cut`          | `2`                     | Cut Sandstone      |
|                 |                 |               | `smooth`       | `3`                     | Smooth Sandstone   |



### Saplings
Java Edition:

** Sapling **
| Name  | Default value | Allowed values | Description                           |
|-------|---------------|----------------|---------------------------------------|
| stage | `0`           | `0`<br/>`1`    | Specifies the sapling's growth stage. |

Bedrock Edition:

| Name         | Metadata Bits             | Default value | Allowed values     | Values forMetadata Bits | Description                           |
|--------------|---------------------------|---------------|--------------------|-------------------------|---------------------------------------|
| age_bit      | `0x8`                     | `false`       | `false`<br/>`true` | `0`<br/>`1`             | Specifies the sapling's growth stage. |
| sapling_type | `0x1`<br/>`0x2`<br/>`0x4` | `oak`         | `acacia`           | `4`                     | Acacia Sapling                        |
|              |                           |               | `birch`            | `2`                     | Birch Sapling                         |
|              |                           |               | `dark_oak`         | `5`                     | Dark Oak Sapling                      |
|              |                           |               | `jungle`           | `3`                     | Jungle Sapling                        |
|              |                           |               | `oak`              | `0`                     | Oak Sapling                           |
|              |                           |               | `spruce`           | `1`                     | Spruce Sapling                        |



### Scaffolding
Java Edition:

| Name        | Default value | Allowed values                                              | Description                                                                                         |
|-------------|---------------|-------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| bottom      | `false`       | `false`<br/>`true`                                          | If this scaffolding is floating.                                                                    |
| distance    | `7`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7` | The distance from a center scaffolding horizontally. If it is 7, it becomes a falling block entity. |
| waterlogged | `false`       | `false`<br/>`true`                                          | Whether or not there's water in the same place as this scaffolding.                                 |

Bedrock Edition:

| Name            | Metadata Bits             | Default value | Allowed values                                              | Values forMetadata Bits                                     | Description                                                                                         |
|-----------------|---------------------------|---------------|-------------------------------------------------------------|-------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| stability       | `0x2`<br/>`0x4`<br/>`0x8` | `7`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7` | The distance from a center scaffolding horizontally. If it is 7, it becomes a falling block entity. |
| stability_check | `0x1`                     | `false`       | `false`<br/>`true`                                          | `0`<br/>`1`                                                 | If a scaffolding block has been checked for stability.[more information needed]                     |

### Sculk Catalyst
Java Edition:

| Name  | Default value | Allowed values     | Description                                                        |
|-------|---------------|--------------------|--------------------------------------------------------------------|
| bloom | `false`       | `false`<br/>`true` | Whether the sculk catalyst is actively spreading the sculk or not. |

Bedrock Edition:

| Name  | Default value | Allowed values | Description                                                        |
|-------|---------------|----------------|--------------------------------------------------------------------|
| bloom | `0`           | `0`<br/>`1`    | Whether the sculk catalyst is actively spreading the sculk or not. |



### Sculk Sensor
Java Edition:

| Name               | Default value | Allowed values                                                                                                                    | Description                                                          |
|--------------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| power              | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | The sculk sensor's current power level.                              |
| sculk_sensor_phase | `inactive`    | `active`<br/>`cooldown`<br/>`inactive`                                                                                            | Whether or not the sculk sensor is active.[more information needed]  |
| waterlogged        | `false`       | `false`<br/>`true`                                                                                                                | Whether or not there's water in the same place as this sculk sensor. |

Bedrock Edition:

| Name               | Metadata Bits | Default value | Allowed values      | Values forMetadata Bits | Description                                      |
|--------------------|---------------|---------------|---------------------|-------------------------|--------------------------------------------------|
| sculk_sensor_phase | Not Supported | `0`           | `0`<br/>`1`<br/>`2` | `Unsupported`           | The sculk sensor phase.[more information needed] |



### Sculk Shrieker
Java Edition:

| Name        | Default value | Allowed values     | Description                                                            |
|-------------|---------------|--------------------|------------------------------------------------------------------------|
| can_summon  | `false`       | `false`<br/>`true` | If true, the sculk shrieker can summon thewarden.                      |
| shrieking   | `false`       | `false`<br/>`true` | Whether the sculk shrieker is shrieking or not.                        |
| waterlogged | `false`       | `false`<br/>`true` | Whether or not there's water in the same place as this sculk shrieker. |

Bedrock Edition:

| Name       | Metadata Bits | Default value | Allowed values     | Values forMetadata Bits | Description                                       |
|------------|---------------|---------------|--------------------|-------------------------|---------------------------------------------------|
| active     | Not Supported | `0`           | `0`<br/>`1`        | `Unsupported`           | Whether the sculk shrieker is shrieking or not.   |
| can_summon | Not Supported | `false`       | `true`<br/>`false` | `Unsupported`           | If true, the sculk shrieker can summon thewarden. |



### Sculk Vein
Java Edition:

| Name        | Default value | Allowed values     | Description                                                        |
|-------------|---------------|--------------------|--------------------------------------------------------------------|
| down        | `false`       | `false`<br/>`true` | When true, a sculk vein texture is displayed on the bottom.        |
| east        | `false`       | `false`<br/>`true` | When true, a sculk vein texture is displayed on the east.          |
| north       | `false`       | `false`<br/>`true` | When true, a sculk vein texture is displayed on the north.         |
| south       | `false`       | `false`<br/>`true` | When true, a sculk vein texture is displayed on the south.         |
| up          | `false`       | `false`<br/>`true` | When true, a sculk vein texture is displayed on the top.           |
| waterlogged | `false`       | `false`<br/>`true` | Whether or not there's water in the same place as this sculk vein. |
| west        | `false`       | `false`<br/>`true` | When true, a sculk vein texture is displayed on the west.          |

Bedrock Edition:

| Name                      | Metadata Bits                                             | Default value | Allowed values | Values forMetadata Bits | Description                                                                                                                                                                                       |
|---------------------------|-----------------------------------------------------------|---------------|----------------|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| multi_face_direction_bits | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8`<br/>`0x10`<br/>`0x20` | `0`           | `0 to 63`      | `0 to 63`               | The directions the sculk vein exists. Each bit determines one direction:0x1: Down<br/>0x2: Up<br/>0x4: North<br/>0x8: South<br/>0x10: West<br/>0x20: East<br/>0 is unused and it behaves like 63. |



### Sea Pickle
Java Edition:

| Name        | Default value | Allowed values              | Description                                                      |
|-------------|---------------|-----------------------------|------------------------------------------------------------------|
| pickles     | `1`           | `1`<br/>`2`<br/>`3`<br/>`4` | Number of pickles.                                               |
| waterlogged | `true`        | `false`<br/>`true`          | Whether or not there's water in the same place as these pickles. |

Bedrock Edition:

| Name          | Metadata Bits   | Default value | Allowed values              | Values forMetadata Bits     | Description                                                  |
|---------------|-----------------|---------------|-----------------------------|-----------------------------|--------------------------------------------------------------|
| cluster_count | `0x1`<br/>`0x2` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3` | `0`<br/>`1`<br/>`2`<br/>`3` | Number of additional pickles.                                |
| dead_bit      | `0x4`           | `false`       | `false`<br/>`true`          | `0`<br/>`1`                 | True if there's no water in the same place as these pickles. |

