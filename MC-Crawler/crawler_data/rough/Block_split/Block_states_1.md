### Bamboo
Java Edition:
Bamboo

| Name   | Default value | Allowed values                 | Description                                                                                                |
|--------|---------------|--------------------------------|------------------------------------------------------------------------------------------------------------|
| age    | `0`           | `0`<br/>`1`                    | The age of the bamboo, if this is 1 the bamboo appears thicker.                                            |
| leaves | `none`        | `large`<br/>`none`<br/>`small` | The size of the leaves on this bamboo block.                                                               |
| stage  | `0`           | `0`<br/>`1`                    | The stage is incremented at random intervals.<br/>At stage 1, bamboo may try to grow more bamboo above it. |

Bedrock Edition:
Bamboo:

| Name                   | Metadata Bits   | Default value | Allowed values                                    | Values forMetadata Bits | Description                                                                                               |
|------------------------|-----------------|---------------|---------------------------------------------------|-------------------------|-----------------------------------------------------------------------------------------------------------|
| age_bit                | `0x8`           | `false`       | `false`<br/>`true`                                | `0`<br/>`1`             | The stage is incremented at random intervals.<br/>When true, bamboo may try to grow more bamboo above it. |
| bamboo_leaf_size       | `0x2`<br/>`0x4` | `no_leaves`   | `no_leaves`<br/>`small_leaves`<br/>`large_leaves` | `0`<br/>`1`<br/>`2`     | The size of the leaves on this bamboo block.                                                              |
| bamboo_stalk_thickness | `0x1`           | `thin`        | `thin`<br/>`thick`                                | `0`<br/>`1`             | The thickness of the bamboo, if this is thick the bamboo appears thicker.                                 |

Bamboo Sapling:

| Name         | Metadata Bits | Default value | Allowed values                                                          | Values forMetadata Bits | Description                           |
|--------------|---------------|---------------|-------------------------------------------------------------------------|-------------------------|---------------------------------------|
| age_bit      | `0x1`         | `false`       | `false`<br/>`true`                                                      | `0`<br/>`1`             | Specifies the sapling's growth stage. |
| sapling_type | Not Supported | `oak`         | `acacia`<br/>`birch`<br/>`dark_oak`<br/>`jungle`<br/>`oak`<br/>`spruce` | `Unsupported`           | Unused.                               |



### Banners
Java Edition:
Floor

| Name     | Default value | Allowed values | Description                          |
|----------|---------------|----------------|--------------------------------------|
| rotation | `0`           | `0`            | The block is facing south.           |
|          |               | `1`            | The block is facing south-southwest. |
|          |               | `2`            | The block is facing southwest.       |
|          |               | `3`            | The block is facing west-southwest.  |
|          |               | `4`            | The block is facing west.            |
|          |               | `5`            | The block is facing west-northwest.  |
|          |               | `6`            | The block is facing northwest.       |
|          |               | `7`            | The block is facing north-northwest. |
|          |               | `8`            | The block is facing north.           |
|          |               | `9`            | The block is facing north-northeast. |
|          |               | `10`           | The block is facing northeast.       |
|          |               | `11`           | The block is facing east-northeast.  |
|          |               | `12`           | The block is facing east.            |
|          |               | `13`           | The block is facing east-southeast.  |
|          |               | `14`           | The block is facing southeast.       |
|          |               | `15`           | The block is facing south-southeast. |

Wall

| Name   | Default value | Allowed values                            | Description                                                                                                                                                                    |
|--------|---------------|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the block is facing. For example, a block facing east is attached to a block to its west.<br/>Opposite from the direction a player faces when placing the block. |

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
| facing_direction | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `2`<br/>`3`<br/>`4`<br/>`5` | `2`<br/>`3`<br/>`4`<br/>`5` | The direction the block is facing. For example, a block facing east is attached to a block to its west.2: north<br/>3: south<br/>4: west<br/>5: east<br/> |
|                  |                           |               | `0`<br/>`1`                 | `0`<br/>`1`                 | Unused                                                                                                                                                    |

### Barrel
Java Edition:

| Name   | Default value | Allowed values                                                | Description                                                                                       |
|--------|---------------|---------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| facing | `north`       | `down`<br/>`east`<br/>`north`<br/>`south`<br/>`up`<br/>`west` | The direction the barrel is facing.                                                               |
| open   | `false`       | `false`<br/>`true`                                            | Whether the barrel is currently being looked at by a player; changes the texture on the top face. |

Bedrock Edition:

| Name             | Metadata Bits             | Default value | Allowed values                              | Values forMetadata Bits                     | Description                                                                                                                                                                               |
|------------------|---------------------------|---------------|---------------------------------------------|---------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing_direction | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | The direction the barrel is facing.0:Down facing barrel<br/>1:Up facing barrel<br/>2:East facing barrel<br/>3:West facing barrel<br/>4:South facing barrel<br/>5:North facing barrel<br/> |
| open_bit         | `0x8`                     | `0`           | `0`<br/>`1`                                 | `0`<br/>`1`                                 | Whether the barrel is currently being looked at by a player; changes the texture on the top face.                                                                                         |



### Basalt and Polished Basalt
Java Edition:

| Name | Default value | Allowed values | Description                         |
|------|---------------|----------------|-------------------------------------|
| axis | `y`           | `x`            | The basalt is oriented east–west.   |
|      |               | `y`            | The basalt is oriented vertically.  |
|      |               | `z`            | The basalt is oriented north–south. |

Bedrock Edition:

| Name        | Metadata Bits   | Default value | Allowed values | Values forMetadata Bits | Description                         |
|-------------|-----------------|---------------|----------------|-------------------------|-------------------------------------|
| pillar_axis | `0x1`<br/>`0x2` | `y`           | `x`            | `1`                     | The basalt is oriented east–west.   |
|             |                 |               | `y`            | `0`                     | The basalt is oriented vertically.  |
|             |                 |               | `z`            | `2`                     | The basalt is oriented north–south. |



