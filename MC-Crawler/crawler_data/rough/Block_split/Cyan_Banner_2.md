### Metadata
#### Item
In Bedrock Edition, banner items use the following data values:

| DV | Banner color |
|----|--------------|
| 0  | black        |
| 1  | red          |
| 2  | green        |
| 3  | brown        |
| 4  | blue         |
| 5  | purple       |
| 6  | cyan         |
| 7  | light gray   |
| 8  | gray         |
| 9  | pink         |
| 10 | lime         |
| 11 | yellow       |
| 12 | light blue   |
| 13 | magenta      |
| 14 | orange       |
| 15 | white        |

### Item
In Java Edition, banner items use the following data values:

| DV | Banner color |
|----|--------------|
| 15 | black        |
| 14 | red          |
| 13 | green        |
| 12 | brown        |
| 11 | blue         |
| 10 | purple       |
| 9  | cyan         |
| 8  | light gray   |
| 7  | gray         |
| 6  | pink         |
| 5  | lime         |
| 4  | yellow       |
| 3  | light blue   |
| 2  | magenta      |
| 1  | orange       |
| 0  | white        |

### Block states
See also: Block states

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

