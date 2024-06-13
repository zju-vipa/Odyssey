### Shulker Boxes
Java Edition:

| Name   | Default value | Allowed values                                                | Description                                                                                                                    |
|--------|---------------|---------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| facing | `up`          | `down`<br/>`east`<br/>`north`<br/>`south`<br/>`up`<br/>`west` | The direction the shulker box is pointing.<br/>The opposite from the direction the player faces while placing the shulker box. |



### Sign
Java Edition:

** Standing **
| Name        | Default value | Allowed values     | Description                                                  |
|-------------|---------------|--------------------|--------------------------------------------------------------|
| rotation    | `0`           | `0`                | The block is facing south.                                   |
|             |               | `1`                | The block is facing south-southwest.                         |
|             |               | `2`                | The block is facing southwest.                               |
|             |               | `3`                | The block is facing west-southwest.                          |
|             |               | `4`                | The block is facing west.                                    |
|             |               | `5`                | The block is facing west-northwest.                          |
|             |               | `6`                | The block is facing northwest.                               |
|             |               | `7`                | The block is facing north-northwest.                         |
|             |               | `8`                | The block is facing north.                                   |
|             |               | `9`                | The block is facing north-northeast.                         |
|             |               | `10`               | The block is facing northeast.                               |
|             |               | `11`               | The block is facing east-northeast.                          |
|             |               | `12`               | The block is facing east.                                    |
|             |               | `13`               | The block is facing east-southeast.                          |
|             |               | `14`               | The block is facing southeast.                               |
|             |               | `15`               | The block is facing south-southeast.                         |
| waterlogged | `false`       | `false`<br/>`true` | Whether or not there's water in the same place as this sign. |

** Wall **
| Name        | Default value | Allowed values                            | Description                                                                                                                                                                    |
|-------------|---------------|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing      | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the block is facing. For example, a block facing east is attached to a block to its west.<br/>Opposite from the direction a player faces when placing the block. |
| waterlogged | `false`       | `false`<br/>`true`                        | Whether or not there's water in the same place as this sign.                                                                                                                   |

Bedrock Edition:

** Standing **
| Name                  | Metadata Bits                       | Default value | Allowed values | Values forMetadata Bits | Description                          |
|-----------------------|-------------------------------------|---------------|----------------|-------------------------|--------------------------------------|
| ground_sign_direction | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8` | `0`           | `0`            | `0`                     | The block is facing south.           |
|                       |                                     |               | `1`            | `1`                     | The block is facing south-southwest. |
|                       |                                     |               | `2`            | `2`                     | The block is facing southwest.       |
|                       |                                     |               | `3`            | `3`                     | The block is facing west-southwest.  |
|                       |                                     |               | `4`            | `4`                     | The block is facing west.            |
|                       |                                     |               | `5`            | `5`                     | The block is facing west-northwest.  |
|                       |                                     |               | `6`            | `6`                     | The block is facing northwest.       |
|                       |                                     |               | `7`            | `7`                     | The block is facing north-northwest. |
|                       |                                     |               | `8`            | `8`                     | The block is facing north.           |
|                       |                                     |               | `9`            | `9`                     | The block is facing north-northeast. |
|                       |                                     |               | `10`           | `10`                    | The block is facing northeast.       |
|                       |                                     |               | `11`           | `11`                    | The block is facing east-northeast.  |
|                       |                                     |               | `12`           | `12`                    | The block is facing east.            |
|                       |                                     |               | `13`           | `13`                    | The block is facing east-southeast.  |
|                       |                                     |               | `14`           | `14`                    | The block is facing southeast.       |
|                       |                                     |               | `15`           | `15`                    | The block is facing south-southeast. |

** Wall **
| Name             | Metadata Bits             | Default value | Allowed values              | Values forMetadata Bits     | Description                                                                                                                                               |
|------------------|---------------------------|---------------|-----------------------------|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing_direction | `0x1`<br/>`0x2`<br/>`0x4` | `2`           | `2`<br/>`3`<br/>`4`<br/>`5` | `2`<br/>`3`<br/>`4`<br/>`5` | The direction the block is facing. For example, a block facing east is attached to a block to its west.2: north<br/>3: south<br/>4: west<br/>5: east<br/> |
|                  |                           |               | `0`<br/>`1`                 | `0`<br/>`1`                 | Unused                                                                                                                                                    |



### Slabs
Java Edition:

| Name        | Default value | Allowed values     | Description                                                  |
|-------------|---------------|--------------------|--------------------------------------------------------------|
| type        | `bottom`      | `bottom`<br/>`top` | Where the slab is within its block.                          |
|             |               | `double`           | The block is a double slab.                                  |
| waterlogged | `false`       | `false`<br/>`true` | Whether or not there's water in the same place as this slab. |

Bedrock Edition:

| Name                    | Metadata Bits | Default value | Allowed values     | Values forMetadata Bits | Description                         |
|-------------------------|---------------|---------------|--------------------|-------------------------|-------------------------------------|
| minecraft:vertical_half | Not Supported | `bottom`      | `bottom`<br/>`top` | `Unsupported`           | Where the slab is within its block. |



### Small Dripleaf
Java Edition:

| Name        | Default value | Allowed values                            | Description                                                                                                                        |
|-------------|---------------|-------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| facing      | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the small dripleaf is facing.<br/>The opposite from the direction the player faces while placing the small dripleaf. |
| half        | `lower`       | `lower`<br/>`upper`                       | What half of the small dripleaf this block is.                                                                                     |
| waterlogged | `false`       | `false`<br/>`true`                        | Whether or not there's water in the same place as this small dripleaf.                                                             |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values                            | Values forMetadata Bits | Description                                                                                                                        |
|------------------------------|---------------|---------------|-------------------------------------------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| minecraft:cardinal_direction | Not Supported | `south`       | `east`<br/>`north`<br/>`south`<br/>`west` | `Unsupported`           | The direction the small dripleaf is facing.<br/>The opposite from the direction the player faces while placing the small dripleaf. |
| upper_block_bit              | Not Supported | `true`        | `false`<br/>`true`                        | `Unsupported`           | What half of the small dripleaf this block is.                                                                                     |



### Smoker
Java Edition:

| Name   | Default value | Allowed values                            | Description                                                                                                              |
|--------|---------------|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| facing | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the smoker's opening faces.<br/>The opposite from the direction the player faces while placing the smoker. |
| lit    | `false`       | `false`<br/>`true`                        | If the smoker is lit.                                                                                                    |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values                            | Values forMetadata Bits | Description                                                                                                              |
|------------------------------|---------------|---------------|-------------------------------------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------|
| minecraft:cardinal_direction | Not Supported | `south`       | `east`<br/>`north`<br/>`south`<br/>`west` | `Unsupported`           | The direction the smoker's opening faces.<br/>The opposite from the direction the player faces while placing the smoker. |



