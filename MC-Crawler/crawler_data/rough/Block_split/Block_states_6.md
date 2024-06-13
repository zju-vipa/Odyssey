### Conduit
Java Edition:

| Name        | Default value | Allowed values     | Description                                                     |
|-------------|---------------|--------------------|-----------------------------------------------------------------|
| waterlogged | `true`        | `false`<br/>`true` | Whether or not there's water in the same place as this conduit. |

### Coral
Java Edition:

| Name        | Default value | Allowed values     | Description                                                   |
|-------------|---------------|--------------------|---------------------------------------------------------------|
| waterlogged | `true`        | `false`<br/>`true` | Whether or not there's water in the same place as this coral. |



### Coral Block
Bedrock Edition:

| Name        | Metadata Bits             | Default value | Allowed values     | Values forMetadata Bits | Description                              |
|-------------|---------------------------|---------------|--------------------|-------------------------|------------------------------------------|
| coral_color | `0x1`<br/>`0x2`<br/>`0x4` | `blue`        | `blue`             | `0`                     | Tube Coral Block                         |
|             |                           |               | `pink`             | `1`                     | Brain Coral Block                        |
|             |                           |               | `purple`           | `2`                     | Bubble Coral Block                       |
|             |                           |               | `red`              | `3`                     | Fire Coral Block                         |
|             |                           |               | `yellow`           | `4`                     | Horn Coral Block                         |
| dead_bit    | `0x8`                     | `false`       | `false`<br/>`true` | `0`<br/>`1`             | Whether or not this coral block is dead. |



### Coral Fan
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



### Daylight Detector
Java Edition:

| Name     | Default value | Allowed values                                                                                                                    | Description                                                       |
|----------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| inverted | `false`       | `false`<br/>`true`                                                                                                                | If true, the daylight detector is inverted.                       |
| power    | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | The current redstone power level produced by the daylight sensor. |

Bedrock Edition:

| Name            | Metadata Bits                       | Default value | Allowed values                                                                                                                    | Values forMetadata Bits                                                                                                           | Description                                                       |
|-----------------|-------------------------------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| redstone_signal | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | The current redstone power level produced by the daylight sensor. |



### Deepslate
Java Edition:

| Name | Default value | Allowed values | Description                            |
|------|---------------|----------------|----------------------------------------|
| axis | `y`           | `x`            | The deepslate is oriented east–west.   |
|      |               | `y`            | The deepslate is oriented vertically.  |
|      |               | `z`            | The deepslate is oriented north–south. |

Bedrock Edition:

| Name        | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                            |
|-------------|---------------|---------------|----------------|-------------------------|----------------------------------------|
| pillar_axis | Not Supported | `y`           | `x`            | `Unsupported`           | The deepslate is oriented east–west.   |
|             |               |               | `y`            | `Unsupported`           | The deepslate is oriented vertically.  |
|             |               |               | `z`            | `Unsupported`           | The deepslate is oriented north–south. |



### Dirt
Bedrock Edition:

| Name      | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description |
|-----------|---------------|---------------|----------------|-------------------------|-------------|
| dirt_type | `0x1`         | `normal`      | `normal`       | `0`                     | Dirt        |
|           |               |               | `coarse`       | `1`                     | Coarse Dirt |



### Dispenser and Dropper
Java Edition:

| Name      | Default value | Allowed values                                                | Description                                                                                                                        |
|-----------|---------------|---------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| facing    | `north`       | `down`<br/>`east`<br/>`north`<br/>`south`<br/>`up`<br/>`west` | The direction in which contents are shot or dropped.<br/>The opposite from the direction the player faces while placing the block. |
| triggered | `false`       | `false`<br/>`true`                                            | True if this block is activated.                                                                                                   |

Bedrock Edition:

| Name             | Metadata Bits             | Default value | Allowed values                                              | Values forMetadata Bits                                     | Description                                                                                                                                                            |
|------------------|---------------------------|---------------|-------------------------------------------------------------|-------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing_direction | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7` | The direction in which contents are shot or dropped.0: facing down<br/>1: facing up<br/>2: facing north<br/>3: facing south<br/>4: facing west<br/>5: facing east<br/> |
| triggered_bit    | `0x8`                     | `false`       | `false`<br/>`true`                                          | `0`<br/>`1`                                                 | True if this block is activated.                                                                                                                                       |



### Doors
Java Edition:

| Name    | Default value | Allowed values                            | Description                                                                                                                                                                                  |
|---------|---------------|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing  | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the door's "inside" is facing.<br/>The direction the player faces while placing the door.<br/>For example, a door facing east occupies the west part of its block when closed. |
| half    | `lower`       | `lower`<br/>`upper`                       | Identifies which part of the door the block is.                                                                                                                                              |
| hinge   | `left`        | `left`<br/>`right`                        | Identifies the side the hinge is on (when facing the same direction as the door's inside).                                                                                                   |
| open    | `false`       | `false`<br/>`true`                        | True if the door is currently open.                                                                                                                                                          |
| powered | `false`       | `false`<br/>`true`                        | True if the door is currently powered by redstone.                                                                                                                                           |

Bedrock Edition:
Lower Door Block:

| Name            | Metadata Bits   | Default value | Allowed values              | Values forMetadata Bits     | Description                                                                                                                                                                                                                                                                |
|-----------------|-----------------|---------------|-----------------------------|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| direction       | `0x1`<br/>`0x2` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3` | `0`<br/>`1`<br/>`2`<br/>`3` | The direction the door's "inside" is facing.<br/>The direction the player faces while placing the door.<br/>For example, a door facing east occupies the west part of its block when closed.0: Facing east<br/>1: Facing south<br/>2: Facing west<br/>3: Facing north<br/> |
| door_hinge_bit  | `— [sic]`       | `false`       | `false`<br/>`true`          | `0`<br/>`0 [sic]`           | Identifies the side the hinge is on (when facing the same direction as the door's inside). false if hinge is on the left (the default), true if on the right.<br/>Lower door block has the same aux value when it is opened and closed.                                    |
| open_bit        | `0x4`           | `false`       | `false`<br/>`true`          | `0`<br/>`1`                 | True if the door is currently open.                                                                                                                                                                                                                                        |
| upper_block_bit | `0x8`           | `false`       | `false`<br/>`true`          | `0`<br/>`1`                 | Always false for the lower part of a door.                                                                                                                                                                                                                                 |

Upper Door Block:

| Name            | Metadata Bits | Default value | Allowed values              | Values forMetadata Bits           | Description                                                                                                                                                                                                                                                                                                                                |
|-----------------|---------------|---------------|-----------------------------|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| direction       | `— [sic]`     | `0`           | `0`<br/>`1`<br/>`2`<br/>`3` | `0`<br/>`0`<br/>`0`<br/>`0 [sic]` | The direction the door's "inside" is facing.<br/>The direction the player faces while placing the door.<br/>For example, a door facing east occupies the west part of its block when closed.0: Facing east<br/>1: Facing south<br/>2: Facing west<br/>3: Facing north<br/>Upper door block has the same aux value no matter what it faces. |
| door_hinge_bit  | `— [sic]`     | `false`       | `false`<br/>`true`          | `0`<br/>`Unsupported`             | Identifies the side the hinge is on (when facing the same direction as the door's inside). false if hinge is on the left (the default), true if on the right.<br/>Upper door block doesn't support aux value when its hinge is on theright.                                                                                                |
| open_bit        | `— [sic]`     | `false`       | `false`<br/>`true`          | `0`<br/>`0 [sic]`                 | True if the door is currently open.<br/>Lower door block has the same aux value when it is opened and closed.                                                                                                                                                                                                                              |
| upper_block_bit | `0x8`         | `false`       | `false`<br/>`true`          | `0`<br/>`1`                       | Always true for the upper part of a door.                                                                                                                                                                                                                                                                                                  |

