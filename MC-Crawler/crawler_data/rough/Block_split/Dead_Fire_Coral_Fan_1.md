### Block states
See also: Block states

Java Edition
Floor:

| Name        | Default value | Allowed values     | Description                                                       |
|-------------|---------------|--------------------|-------------------------------------------------------------------|
| waterlogged | `true`        | `false`<br/>`true` | Whether or not there's water in the same place as this coral fan. |

Wall:

| Name        | Default value | Allowed values                            | Description                                                                                                                                                    |
|-------------|---------------|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing      | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction in which the coral fan juts out from the block it is attached to.<br/>For example, a coral fan facing north is attached to a block to its south. |
| waterlogged | `true`        | `false`<br/>`true`                        | Whether or not there's water in the same place as this coral fan.                                                                                              |

Bedrock Edition
Floor:

| Name                | Metadata Bits             | Default value | Allowed values | Values forMetadata Bits | Description                                                  |
|---------------------|---------------------------|---------------|----------------|-------------------------|--------------------------------------------------------------|
| coral_color         | `0x1`<br/>`0x2`<br/>`0x4` | `blue`        | `blue`         | `0`                     | Tube Coral Fan                                               |
|                     |                           |               | `pink`         | `1`                     | Brain Coral Fan                                              |
|                     |                           |               | `purple`       | `2`                     | Bubble Coral Fan                                             |
|                     |                           |               | `red`          | `3`                     | Fire Coral Fan                                               |
|                     |                           |               | `yellow`       | `4`                     | Horn Coral Fan                                               |
| coral_fan_direction | `0x8`                     | `0`           | `0`<br/>`1`    | `0`<br/>`1`             | The direction the coral is facing. East-west or north-south. |

Wall:

| Name                | Metadata Bits   | Default value | Allowed values              | Values forMetadata Bits     | Description                                                                                                                                                                    |
|---------------------|-----------------|---------------|-----------------------------|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| coral_hang_type_bit | `0x1`           | `false`       | `false`<br/>`true`          | `0`<br/>`1`                 | Which coral it is; depends on the ID.<br/>For`hang`false means tube and true means brain.<br/>For`hang2`false means bubble and true means fire.<br/>For`hang3`false mean horn. |
| coral_direction     | `0x4`<br/>`0x8` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3` | `0`<br/>`1`<br/>`2`<br/>`3` | The direction the top of the fan is facing.0: west<br/>1: east<br/>2: north<br/>3: south<br/>                                                                                  |
| dead_bit            | `0x2`           | `false`       | `false`<br/>`true`          | `0`<br/>`1`                 | Whether or not this coral is dead.                                                                                                                                             |




