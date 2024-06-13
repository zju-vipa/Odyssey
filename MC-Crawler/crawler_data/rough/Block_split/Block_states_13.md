### Nether Wart
| Name | Default value | Allowed values | Description  |
|------|---------------|----------------|--------------|
| age  | `0`           | `0`            |              |
|      |               | `1`<br/>`2`    |              |
|      |               | `3`            | Fully grown. |

Bedrock Edition:

| Name | Metadata Bits   | Default value | Allowed values                                                                                    | Values forMetadata Bits | Description  |
|------|-----------------|---------------|---------------------------------------------------------------------------------------------------|-------------------------|--------------|
| age  | `0x1`<br/>`0x2` | `0`           | `0`                                                                                               | `0`                     |              |
|      |                 |               | `1`<br/>`2`                                                                                       | `1`<br/>`2`             |              |
|      |                 |               | `3`                                                                                               | `3`                     | Fully grown. |
|      |                 |               | `4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | `Unsupported`           | Unused       |



### Nether Portal
Java Edition:

| Name | Default value | Allowed values | Description                              |
|------|---------------|----------------|------------------------------------------|
| axis | `x`           | `x`            | The portal's long edge runs east–west.   |
|      |               | `z`            | The portal's long edge runs north–south. |

Bedrock Edition:

| Name        | Metadata Bits   | Default value | Allowed values | Values forMetadata Bits | Description                                                                                                                               |
|-------------|-----------------|---------------|----------------|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| portal_axis | `0x1`<br/>`0x2` | `unknown`     | `unknown`      | `0`                     | If placed with this state, the portal's long edge runs north–south. If set to it, its direction will be tied to that of adjacent portals. |
|             |                 |               | `x`            | `1`                     | The portal's long edge runs east–west.                                                                                                    |
|             |                 |               | `z`            | `2`                     | The portal's long edge runs north–south.                                                                                                  |



### Note Block
Java Edition:

| Name       | Default value | Allowed values                                                                                                                                                                                                                                                                                                            | Description                                    |
|------------|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| instrument | `harp`        | `banjo`<br/>`basedrum`<br/>`bass`<br/>`bell`<br/>`bit`<br/>`chime`<br/>`cow_bell`<br/>`creeper`<br/>`custom_head`<br/>`didgeridoo`<br/>`dragon`<br/>`flute`<br/>`guitar`<br/>`harp`<br/>`hat`<br/>`iron_xylophone`<br/>`piglin`<br/>`pling`<br/>`skeleton`<br/>`snare`<br/>`wither_skeleton`<br/>`xylophone`<br/>`zombie` | The instrument of the note block.              |
| note       | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15`<br/>`16`<br/>`17`<br/>`18`<br/>`19`<br/>`20`<br/>`21`<br/>`22`<br/>`23`<br/>`24`                                                                                                        | The pitch of the note block                    |
| powered    | `false`       | `false`<br/>`true`                                                                                                                                                                                                                                                                                                        | True if the note block is currently activated. |



### Observer
Java Edition:

| Name    | Default value | Allowed values                                                | Description                                                                                          |
|---------|---------------|---------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| facing  | `south`       | `down`<br/>`east`<br/>`north`<br/>`south`<br/>`up`<br/>`west` | The direction the observer is observing. The same direction the player faces when placing the block. |
| powered | `false`       | `false`<br/>`true`                                            | True while the observer is observing a change and emitting a pulse.                                  |

Bedrock Edition:

| Name                       | Metadata Bits | Default value | Allowed values                                                | Values forMetadata Bits | Description                                                                                          |
|----------------------------|---------------|---------------|---------------------------------------------------------------|-------------------------|------------------------------------------------------------------------------------------------------|
| minecraft:facing_direction | Not Supported | `down`        | `down`<br/>`east`<br/>`north`<br/>`south`<br/>`up`<br/>`west` | `Unsupported`           | The direction the observer is observing. The same direction the player faces when placing the block. |
| powered_bit                | `0x8`         | `false`       | `false`<br/>`true`                                            | `0`<br/>`1`             | True while the observer is observing a change and emitting a pulse.                                  |



### Pink Petals
Java Edition:

| Name          | Default value | Allowed values                            | Description                                                                                                                   |
|---------------|---------------|-------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| facing        | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the pink petals are facing.<br/>The opposite from the direction the player faces while placing the pink petals. |
| flower_amount | `1`           | `1`<br/>`2`<br/>`3`<br/>`4`               | The amount of pink petals in the block.                                                                                       |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values                                              | Values forMetadata Bits | Description                                                                                                                   |
|------------------------------|---------------|---------------|-------------------------------------------------------------|-------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| growth                       | Not Supported | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7` | `Unsupported`           | The amount of pink petals in the block. A value greater than 3 can only be obtained via commands.                             |
| minecraft:cardinal_direction | Not Supported | `south`       | `east`<br/>`north`<br/>`south`<br/>`west`                   | `Unsupported`           | The direction the pink petals are facing.<br/>The opposite from the direction the player faces while placing the pink petals. |



### Pistons
Java Edition:

| Name     | Default value | Allowed values                                                | Description                                                                                                               |
|----------|---------------|---------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| extended | `false`       | `false`<br/>`true`                                            | If true, the piston is extended.                                                                                          |
| facing   | `north`       | `down`<br/>`east`<br/>`north`<br/>`south`<br/>`up`<br/>`west` | The direction the piston head is pointing.<br/>The opposite from the direction the player faces while placing the piston. |

Bedrock Edition:

| Name             | Metadata Bits             | Default value | Allowed values                              | Values forMetadata Bits                     | Description                                                                                                                                             |
|------------------|---------------------------|---------------|---------------------------------------------|---------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing_direction | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | The direction the piston is pointing.0: facing down<br/>1: facing up<br/>2: facing south<br/>3: facing north<br/>4: facing east<br/>5: facing west<br/> |

#### Moving piston
Java Edition:

| Name   | Default value | Allowed values                                                | Description                                            |
|--------|---------------|---------------------------------------------------------------|--------------------------------------------------------|
| facing | `north`       | `down`<br/>`east`<br/>`north`<br/>`south`<br/>`up`<br/>`west` | The direction the block is being pushed by the piston. |
| type   | `normal`      | `normal`<br/>`sticky`                                         | What piston base this has.                             |



#### Piston head
Java Edition:

| Name   | Default value | Allowed values                                                | Description                                                 |
|--------|---------------|---------------------------------------------------------------|-------------------------------------------------------------|
| facing | `north`       | `down`<br/>`east`<br/>`north`<br/>`south`<br/>`up`<br/>`west` | The direction the piston head is pointing.                  |
| short  | `false`       | `false`<br/>`true`                                            | If true, the piston arm is shorter than usual, by 4 pixels. |
| type   | `normal`      | `normal`<br/>`sticky`                                         | The type of piston head.                                    |

Bedrock Edition:
Piston Head:

| Name             | Metadata Bits             | Default value | Allowed values                              | Values forMetadata Bits                     | Description                                                                                                                                                  |
|------------------|---------------------------|---------------|---------------------------------------------|---------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing_direction | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | The direction the piston head is pointing.0: facing up<br/>1: facing down<br/>2: facing south<br/>3: facing north<br/>4: facing east<br/>5: facing west<br/> |

Sticky Piston Head:

| Name             | Metadata Bits | Default value | Allowed values                              | Values forMetadata Bits | Description                                                                                                                                                  |
|------------------|---------------|---------------|---------------------------------------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing_direction | Not Supported | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | `Unsupported`           | The direction the piston head is pointing.0: facing up<br/>1: facing down<br/>2: facing south<br/>3: facing north<br/>4: facing east<br/>5: facing west<br/> |



### Potatoes
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



