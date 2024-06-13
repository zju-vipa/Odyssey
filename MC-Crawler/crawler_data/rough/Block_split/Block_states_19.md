### Tall Grass and Large Fern
Bedrock Edition:

| Name            | Metadata Bits   | Default value | Allowed values | Values forMetadata Bits | Description                                                                                         |
|-----------------|-----------------|---------------|----------------|-------------------------|-----------------------------------------------------------------------------------------------------|
| tall_grass_type | `0x1`<br/>`0x2` | `default`     | `default`      | `0`                     | Fern(Unused variant which looks identical to grass, but turns into alarge fernwhenbone mealis used) |
|                 |                 |               | `tall`         | `1`                     | Grass                                                                                               |
|                 |                 |               | `fern`         | `2`                     | Fern                                                                                                |
|                 |                 |               | `snow`         | `3`                     | Fern (looks identical to actual fern, but turns intodouble tallgrasswhenbone mealis used)           |

### Tall Seagrass
Java Edition:
Tall

| Name | Default value | Allowed values      | Description                                    |
|------|---------------|---------------------|------------------------------------------------|
| half | `lower`       | `lower`<br/>`upper` | The half of the plant contained in this block. |

Bedrock Edition:

| Name           | Metadata Bits   | Default value | Allowed values | Values forMetadata Bits | Description                               |
|----------------|-----------------|---------------|----------------|-------------------------|-------------------------------------------|
| sea_grass_type | `0x1`<br/>`0x2` | `default`     | `default`      | `0`                     | This is seagrass.                         |
|                |                 |               | `double_bot`   | `1`                     | This is the bottom half of tall seagrass. |
|                |                 |               | `double_top`   | `2`                     | This is the top half of tall seagrass.    |

### Target
Java Edition:

| Name  | Default value | Allowed values                                                                                                                    | Description                          |
|-------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|
| power | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | Redstone power output of the target. |



### TNT
Java Edition:

| Name     | Default value | Allowed values | Description                                                                   |
|----------|---------------|----------------|-------------------------------------------------------------------------------|
| unstable | `false`       | `false`        | Hittingthe TNT block breaks it, dropping it as an item that can be picked up. |
|          |               | `true`         | Hittingthe TNT block causes it to ignite and then explode.                    |

Bedrock Edition:

| Name                 | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                                                   |
|----------------------|---------------|---------------|----------------|-------------------------|-------------------------------------------------------------------------------|
| allow_underwater_bit | `0x2`         | `false`       | `false`        | `0`                     | This is normal TNT.                                                           |
|                      |               |               | `true`         | `1`                     | This is Underwater TNT.                                                       |
| explode_bit          | `0x1`         | `false`       | `false`        | `0`                     | Hittingthe TNT block breaks it, dropping it as an item that can be picked up. |
|                      |               |               | `true`         | `1`                     | Hittingthe TNT block causes it to ignite and then explode.                    |



### Torch and Soul Torch
Java Edition:
Wall

| Name   | Default value | Allowed values                            | Description                                   |
|--------|---------------|-------------------------------------------|-----------------------------------------------|
| facing | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the top of the torch is facing. |

Bedrock Edition:

| Name                   | Metadata Bits             | Default value | Allowed values                                      | Values forMetadata Bits             | Description                                                                                                                                  |
|------------------------|---------------------------|---------------|-----------------------------------------------------|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| torch_facing_direction | `0x1`<br/>`0x2`<br/>`0x4` | `west`        | `west`<br/>`east`<br/>`north`<br/>`south`<br/>`top` | `1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | The face of the block that the torch is attached to. If the torch is a wall torch, the top of the torch faces opposite to this direction.[4] |
|                        |                           |               | `unknown`                                           | `0`                                 | Unused                                                                                                                                       |



### Trapdoors
Java Edition:

| Name        | Default value | Allowed values                            | Description                                                                                      |
|-------------|---------------|-------------------------------------------|--------------------------------------------------------------------------------------------------|
| facing      | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the trapdoor swings open.<br/>The opposite from the side its hinge is attached to. |
| half        | `bottom`      | `bottom`<br/>`top`                        | Whether the trapdoor occupies the top or bottom part of a block.                                 |
| open        | `false`       | `false`<br/>`true`                        | True if the trapdoor is currently open (may differ from`powered`).                               |
| powered     | `false`       | `false`<br/>`true`                        | True if the trapdoor is currently powered (may differ from`open`).                               |
| waterlogged | `false`       | `false`<br/>`true`                        | Whether or not there's water in the same place as this trapdoor.                                 |

Bedrock Edition:

| Name            | Metadata Bits   | Default value | Allowed values              | Values forMetadata Bits     | Description                                                                                                                                                                                                             |
|-----------------|-----------------|---------------|-----------------------------|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| direction       | `0x1`<br/>`0x2` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3` | `0`<br/>`1`<br/>`2`<br/>`3` | The direction the trapdoor is facing.0: Trapdoor on the west side of a block<br/>1: Trapdoor on the east side of a block<br/>2: Trapdoor on the north side of a block<br/>3: Trapdoor on the south side of a block<br/> |
| open_bit        | `0x8`           | `false`       | `false`<br/>`true`          | `0`<br/>`1`                 | True if the trapdoor is currently open.                                                                                                                                                                                 |
| upside_down_bit | `0x4`           | `false`       | `false`<br/>`true`          | `0`<br/>`1`                 | Whether the trapdoor occupies the top or bottom part of a block.                                                                                                                                                        |

### Tripwire
Java Edition:

| Name     | Default value | Allowed values     | Description                                                                     |
|----------|---------------|--------------------|---------------------------------------------------------------------------------|
| attached | `false`       | `false`<br/>`true` | True if the tripwire is connected to a valid tripwire circuit.                  |
| disarmed | `false`       | `false`<br/>`true` | True if the tripwire is disarmed, that is, broken usingshears.                  |
| east     | `false`       | `false`<br/>`true` | True if the tripwire connects to other tripwire or tripwire hooks to the east.  |
| north    | `false`       | `false`<br/>`true` | True if the tripwire connects to other tripwire or tripwire hooks to the north. |
| powered  | `false`       | `false`<br/>`true` | True if the tripwire is active.                                                 |
| south    | `false`       | `false`<br/>`true` | True if the tripwire connects to other tripwire or tripwire hooks to the south. |
| west     | `false`       | `false`<br/>`true` | True if the tripwire connects to other tripwire or tripwire hooks to the west.  |

Bedrock Edition:

| Name          | Metadata Bits | Default value | Allowed values     | Values forMetadata Bits | Description                                                                                      |
|---------------|---------------|---------------|--------------------|-------------------------|--------------------------------------------------------------------------------------------------|
| attached_bit  | `0x4`         | `false`       | `false`<br/>`true` | `0`<br/>`1`             | True if the tripwire is connected to a valid tripwire circuit.                                   |
| disarmed_bit  | `0x8`         | `false`       | `false`<br/>`true` | `0`<br/>`1`             | True if the tripwire is disarmed, that is, broken usingshears.                                   |
| powered_bit   | `0x1`         | `false`       | `false`<br/>`true` | `0`<br/>`1`             | True if the tripwire is active.                                                                  |
| suspended_bit | `0x2`         | `true`        | `false`<br/>`true` | `0`<br/>`1`             | True if the tripwire hasn't connected to a valid tripwire circuit. (makeshitboxlarger when true) |



