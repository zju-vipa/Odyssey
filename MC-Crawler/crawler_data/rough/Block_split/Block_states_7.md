### End Portal Frame
Java Edition:

| Name   | Default value | Allowed values                            | Description                                                                                                                                                                                                                                                        |
|--------|---------------|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| eye    | `false`       | `false`<br/>`true`                        | If true, the portal frame block contains aneye of ender.                                                                                                                                                                                                           |
| facing | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction of the end portal frame block.<br/>The opposite from the direction the player faces while placing the block.<br/>In order to activate a portal, all 12 blocks must be facing inward;<br/>for example, the northern three blocks must all face south. |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values                            | Values forMetadata Bits | Description                                                                                                                                                                                                                                                        |
|------------------------------|---------------|---------------|-------------------------------------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| end_portal_eye_bit           | `0x4`         | `false`       | `false`<br/>`true`                        | `0`<br/>`1`             | If the portal frame block contains aneye of ender.                                                                                                                                                                                                                 |
| minecraft:cardinal_direction | Not Supported | `south`       | `east`<br/>`north`<br/>`south`<br/>`west` | `Unsupported`           | The direction of the end portal frame block.<br/>The opposite from the direction the player faces while placing the block.<br/>In order to activate a portal, all 12 blocks must be facing inward;<br/>for example, the northern three blocks must all face south. |



### End Rod
Java Edition:

| Name   | Default value | Allowed values                                                | Description                                                                                                                                                                                                         |
|--------|---------------|---------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing | `up`          | `down`<br/>`east`<br/>`north`<br/>`south`<br/>`up`<br/>`west` | The direction to the end rod, from the block it is attached to; also the direction the white end points.<br/>Opposite from the direction the player faces when placing an end rod, and opposite from the wider end. |

Bedrock Edition:

| Name             | Metadata Bits             | Default value | Allowed values                              | Values forMetadata Bits                     | Description                                                                                                                                                                                                                |
|------------------|---------------------------|---------------|---------------------------------------------|---------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing_direction | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | The direction to the end rod, from the block it is attached to; also the direction the white end points.0: Facing down<br/>1: Facing up<br/>2: Facing north<br/>3: Facing south<br/>4: Facing west<br/>5: Facing east<br/> |



### Farmland
Java Edition:

| Name     | Default value | Allowed values                                              | Description                                                                                                                                                                                               |
|----------|---------------|-------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| moisture | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7` | Increasing levels of wetness. The wetness value counts down to 0 while the farmland does not have access to water. The wet texture is used only on level 7. Newly hydrated farmland jumps from 0 to 7.[2] |

Bedrock Edition:

| Name               | Metadata Bits             | Default value | Allowed values                                              | Values forMetadata Bits                                     | Description                                                                                                                                                                                            |
|--------------------|---------------------------|---------------|-------------------------------------------------------------|-------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| moisturized_amount | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7` | Increasing levels of wetness. The wetness value counts down to 0 while the farmland does not have access to water. The wet texture is used only on level 7. Newly hydrated farmland jumps from 0 to 7. |



### Fences
Java Edition:

| Name        | Default value | Allowed values     | Description                                                     |
|-------------|---------------|--------------------|-----------------------------------------------------------------|
| east        | `false`       | `false`<br/>`true` | When true, the fence extends from the center post to the east.  |
| north       | `false`       | `false`<br/>`true` | When true, the fence extends from the center post to the north. |
| south       | `false`       | `false`<br/>`true` | When true, the fence extends from the center post to the south. |
| waterlogged | `false`       | `false`<br/>`true` | Whether or not there's water in the same place as this fence.   |
| west        | `false`       | `false`<br/>`true` | When true, the fence extends from the center post to the west.  |

### Fence Gates
Java Edition:

| Name    | Default value | Allowed values                            | Description                                                                                                                                                                            |
|---------|---------------|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing  | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | For an open gate, the direction the gates swing open.<br/>For a closed gate, the direction the player was facing when the gate was placed, or the last direction the gates have swung. |
| in_wall | `false`       | `false`<br/>`true`                        | If true, the gate is lowered by three pixels, to accommodate attaching more cleanly withwalls.                                                                                         |
| open    | `false`       | `false`<br/>`true`                        | If true, the gate is opened.                                                                                                                                                           |
| powered | `false`       | `false`<br/>`true`                        | If true, the gate is receiving redstone power.                                                                                                                                         |

Bedrock Edition:

| Name        | Metadata Bits   | Default value | Allowed values              | Values forMetadata Bits     | Description                                                                                                                                                                                                                                                                                                    |
|-------------|-----------------|---------------|-----------------------------|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| direction   | `0x1`<br/>`0x2` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3` | `0`<br/>`1`<br/>`2`<br/>`3` | The direction the gate is facing0: Facing south<br/>1: Facing west<br/>2: Facing north<br/>3: Facing east<br/>For an open gate, it's the direction the gates swing open.<br/>For a closed gate, it's the direction the player was facing when the gate was placed, or the last direction the gates have swung. |
| in_wall_bit | `0x8`           | `false`       | `false`<br/>`true`          | `0`<br/>`1`                 | If the gate is lowered by three pixels, to accommodate attaching more cleanly withwalls.                                                                                                                                                                                                                       |
| open_bit    | `0x4`           | `false`       | `false`<br/>`true`          | `0`<br/>`1`                 | If the gate is opened.                                                                                                                                                                                                                                                                                         |

### Fire
Java Edition:
Fire:

| Name  | Default value | Allowed values                                                                                                                    | Description                                                                                                                                             |
|-------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| age   | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | $Newly placed fire has an age of 0, and has a\frac{1}{3}$chance of incrementing with eachblock tick.<br/>This factor affects how the fire extinguishes. |
| east  | `false`       | `false`<br/>`true`                                                                                                                | When true, fire texture shows on that face of the block to the east; false if there's a block below this fire.                                          |
| north | `false`       | `false`<br/>`true`                                                                                                                | When true, fire texture shows on that face of the block to the north; false if there's a block below this fire.                                         |
| south | `false`       | `false`<br/>`true`                                                                                                                | When true, fire texture shows on that face of the block to the south; false if there's a block below this fire.                                         |
| up    | `false`       | `false`<br/>`true`                                                                                                                | When true, fire texture shows on that face of the block above; false if there's a block below this fire.                                                |
| west  | `false`       | `false`<br/>`true`                                                                                                                | When true, fire texture shows on that face of the block to the west; false if there's a block below this fire.                                          |

Bedrock Edition:
Fire and Soul Fire:

| Name | Metadata Bits                       | Default value | Allowed values                                                                                                                    | Values forMetadata Bits                                                                                                           | Description                                                                           |
|------|-------------------------------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| age  | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | Newly placed fire has an age of 0.<br/>This factor affects how the fire extinguishes. |



