### Block states
See also: Block states

Java Edition
Floor:

| Name        | Default value | Allowed values | Description                                                       |
|-------------|---------------|----------------|-------------------------------------------------------------------|
| waterlogged | true          | falsetrue      | Whether or not there's water in the same place as this coral fan. |

Wall:

| Name        | Default value | Allowed values     | Description                                                                                                                                               |
|-------------|---------------|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing      | north         | eastnorthsouthwest | The direction in which the coral fan juts out from the block it is attached to.For example, a coral fan facing north is attached to a block to its south. |
| waterlogged | true          | falsetrue          | Whether or not there's water in the same place as this coral fan.                                                                                         |

Bedrock Edition
Floor:

| Name                | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                                  |
|---------------------|---------------|---------------|----------------|-------------------------|--------------------------------------------------------------|
| coral_color         | 0x10x20x4     | blue          | blue           | 0                       | Tube Coral Fan                                               |
|                     |               |               | pink           | 1                       | Brain Coral Fan                                              |
|                     |               |               | purple         | 2                       | Bubble Coral Fan                                             |
|                     |               |               | red            | 3                       | Fire Coral Fan                                               |
|                     |               |               | yellow         | 4                       | Horn Coral Fan                                               |
| coral_fan_direction | 0x8           | 0             | 01             | 01                      | The direction the coral is facing. East-west or north-south. |

Wall:

| Name                | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                                                                                                                               |
|---------------------|---------------|---------------|----------------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| coral_hang_type_bit | 0x1           | false         | falsetrue      | 01                      | Which coral it is; depends on the ID.Forhangfalse means tube and true means brain.Forhang2false means bubble and true means fire.Forhang3false mean horn. |
| coral_direction     | 0x40x8        | 0             | 0123           | 0123                    | The direction the top of the fan is facing.0: west 1: east 2: north 3: south                                                                              |
| dead_bit            | 0x2           | false         | falsetrue      | 01                      | Whether or not this coral is dead.                                                                                                                        |




