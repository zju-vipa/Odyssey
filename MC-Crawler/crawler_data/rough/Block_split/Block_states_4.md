### Campfire
Java Edition:

| Name        | Default value | Allowed values                            | Description                                                                                                            |
|-------------|---------------|-------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| facing      | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the campfire is facing.<br/>The opposite from the direction the player faces while placing the campfire. |
| lit         | `true`        | `false`<br/>`true`                        | Whether the campfire is lit.                                                                                           |
| signal_fire | `false`       | `false`<br/>`true`                        | Whether the campfire has ahay balebelow it.                                                                            |
| waterlogged | `false`       | `false`<br/>`true`                        | Whether or not there's water in the same place as this campfire.                                                       |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values                            | Values forMetadata Bits | Description                                                                                                            |
|------------------------------|---------------|---------------|-------------------------------------------|-------------------------|------------------------------------------------------------------------------------------------------------------------|
| extinguished                 | `0x4`         | `false`       | `false`<br/>`true`                        | `0`<br/>`1`             | Whether the campfire is put out.                                                                                       |
| minecraft:cardinal_direction | Not Supported | `south`       | `east`<br/>`north`<br/>`south`<br/>`west` | `Unsupported`           | The direction the campfire is facing.<br/>The opposite from the direction the player faces while placing the campfire. |



### Candles
Java Edition:

| Name        | Default value | Allowed values              | Description                                                      |
|-------------|---------------|-----------------------------|------------------------------------------------------------------|
| candles     | `1`           | `1`<br/>`2`<br/>`3`<br/>`4` | Number of candles.                                               |
| lit         | `false`       | `false`<br/>`true`          | Whether or not these candles are lit.                            |
| waterlogged | `false`       | `false`<br/>`true`          | Whether or not there's water in the same place as these candles. |

Bedrock Edition:

| Name    | Metadata Bits   | Default value | Allowed values              | Values forMetadata Bits     | Description                              |
|---------|-----------------|---------------|-----------------------------|-----------------------------|------------------------------------------|
| candles | `0x1`<br/>`0x2` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3` | `0`<br/>`1`<br/>`2`<br/>`3` | Number of candles, starting from 1 to 4. |
| lit     | `0x4`           | `false`       | `false`<br/>`true`          | `0`<br/>`1`                 | Whether or not these candles are lit.    |

### Carrots
Java Edition:

| Name | Default value | Allowed values      | Description  |
|------|---------------|---------------------|--------------|
| age  | `0`           | `0`<br/>`1`         |              |
|      |               | `2`<br/>`3`         |              |
|      |               | `4`<br/>`5`<br/>`6` |              |
|      |               | `7`                 | Fully grown. |

Bedrock Edition:

| Name   | Metadata Bits             | Default value | Allowed values      | Values forMetadata Bits | Description  |
|--------|---------------------------|---------------|---------------------|-------------------------|--------------|
| growth | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`<br/>`1`         | `0`<br/>`1`             |              |
|        |                           |               | `2`<br/>`3`         | `2`<br/>`3`             |              |
|        |                           |               | `4`<br/>`5`<br/>`6` | `4`<br/>`5`<br/>`6`     |              |
|        |                           |               | `7`                 | `7`                     | Fully grown. |



### Cauldron
Java Edition:
Water cauldron and powder snow cauldron:

| Name  | Default value | Allowed values              | Description                                       |
|-------|---------------|-----------------------------|---------------------------------------------------|
| level | `0`           | `0`<br/>`1`<br/>`2`<br/>`3` | Fullness of a cauldron, 0 is empty and 3 is full. |

Bedrock Edition:

| Name            | Metadata Bits             | Default value | Allowed values                                      | Values forMetadata Bits                             | Description                                       |
|-----------------|---------------------------|---------------|-----------------------------------------------------|-----------------------------------------------------|---------------------------------------------------|
| fill_level      | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6` | Fullness of a cauldron, 0 is empty and 6 is full. |
| cauldron_liquid | `0x8`                     | `water`       | `water`                                             | `0`                                                 | The cauldron contains water.                      |
|                 |                           |               | `lava`                                              | `1`                                                 | The cauldron contains lava.                       |
|                 |                           |               | `powder_snow`                                       | `Unsupported [sic]`                                 | The cauldron contains powder snow.                |



### Cave Vines
Java Edition:
Cave Vines:

| Name    | Default value | Allowed values                                                                                                                                                                                                              | Description                         |
|---------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------|
| berries | `false`       | `false`<br/>`true`                                                                                                                                                                                                          | Whether this cave vine has berries. |
| age     | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15`<br/>`16`<br/>`17`<br/>`18`<br/>`19`<br/>`20`<br/>`21`<br/>`22`<br/>`23`<br/>`24`<br/>`25` | How old this cave vine is.          |

Cave Vines Plant:

| Name    | Default value | Allowed values     | Description                         |
|---------|---------------|--------------------|-------------------------------------|
| berries | `false`       | `false`<br/>`true` | Whether this cave vine has berries. |

Bedrock Edition:
Cave Vines, Cave Vines Body With Berries, Cave Vines Head With Berries:

| Name              | Metadata Bits | Default value | Allowed values                                                                                                                                                                                                              | Values forMetadata Bits | Description                |
|-------------------|---------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|----------------------------|
| growing_plant_age | Not Supported | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15`<br/>`16`<br/>`17`<br/>`18`<br/>`19`<br/>`20`<br/>`21`<br/>`22`<br/>`23`<br/>`24`<br/>`25` | `Unsupported`           | How old this cave vine is. |



### Chain
Java Edition:

| Name        | Default value | Allowed values     | Description                                                   |
|-------------|---------------|--------------------|---------------------------------------------------------------|
| axis        | `y`           | `x`                | The chain is oriented east–west.                              |
|             |               | `y`                | The chain is oriented vertically.                             |
|             |               | `z`                | The chain is oriented north–south.                            |
| waterlogged | `false`       | `false`<br/>`true` | Whether or not there's water in the same place as this chain. |

Bedrock Edition:

| Name        | Metadata Bits   | Default value | Allowed values | Values forMetadata Bits | Description                        |
|-------------|-----------------|---------------|----------------|-------------------------|------------------------------------|
| pillar_axis | `0x1`<br/>`0x2` | `y`           | `x`            | `1`                     | The chain is oriented east–west.   |
|             |                 |               | `y`            | `0`                     | The chain is oriented vertically.  |
|             |                 |               | `z`            | `2`                     | The chain is oriented north–south. |



### Chemistry Table
| Name                 | Metadata Bits   | Default value      | Allowed values              | Values forMetadata Bits     | Description                                                                           |
|----------------------|-----------------|--------------------|-----------------------------|-----------------------------|---------------------------------------------------------------------------------------|
| chemistry_table_type | `0x1`<br/>`0x2` | `compound_creator` | `compound_creator`          | `0`                         | Compound Creator                                                                      |
|                      |                 |                    | `element_constructor`       | `2`                         | Element Constructor                                                                   |
|                      |                 |                    | `lab_table`                 | `3`                         | Lab Table                                                                             |
|                      |                 |                    | `material_reducer`          | `1`                         | Material Reducer                                                                      |
| direction            | `0x4`<br/>`0x8` | `0`                | `0`<br/>`1`<br/>`2`<br/>`3` | `0`<br/>`1`<br/>`2`<br/>`3` | The direction the block's front is.0: north<br/>1: east<br/>2: south<br/>3: west<br/> |



### Chests
#### Chest and Trapped Chest
Java Edition:

| Name        | Default value | Allowed values                            | Description                                                                                                       |
|-------------|---------------|-------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| facing      | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the chest's latch is on.<br/>The opposite from the direction the player faces when placing a chest. |
| type        | `single`      | `left`<br/>`right`<br/>`single`           | The direction the chest has a connection with.                                                                    |
| waterlogged | `false`       | `false`<br/>`true`                        | Whether or not there's water in the same place as this chest.                                                     |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values                            | Values forMetadata Bits | Description                                                                                                       |
|------------------------------|---------------|---------------|-------------------------------------------|-------------------------|-------------------------------------------------------------------------------------------------------------------|
| minecraft:cardinal_direction | Not Supported | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | `Unsupported`           | The direction the chest's latch is on.<br/>The opposite from the direction the player faces when placing a chest. |



