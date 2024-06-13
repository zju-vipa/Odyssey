### Tripwire Hook
Java Edition:

| Name     | Default value | Allowed values                            | Description                                                                                                                                                            |
|----------|---------------|-------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| attached | `false`       | `false`<br/>`true`                        | True if the tripwire hook is connected to a valid tripwire circuit.                                                                                                    |
| facing   | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction in which the tripwire hook juts out from the block it is attached to.<br/>For example, a tripwire hook facing north is attached to a block to its south. |
| powered  | `false`       | `false`<br/>`true`                        | True if the tripwire hook is active.                                                                                                                                   |

Bedrock Edition:

| Name         | Metadata Bits   | Default value | Allowed values              | Values forMetadata Bits     | Description                                                                                                                                                                                                                                                                       |
|--------------|-----------------|---------------|-----------------------------|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| attached_bit | `0x4`           | `false`       | `false`<br/>`true`          | `0`<br/>`1`                 | True if the tripwire hook is connected to a valid tripwire circuit.                                                                                                                                                                                                               |
| direction    | `0x1`<br/>`0x2` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3` | `0`<br/>`1`<br/>`2`<br/>`3` | The direction in which the tripwire hook juts out from the block it is attached to.0: Tripwire hook on block side facing south<br/>1: Tripwire hook on block side facing west<br/>2: Tripwire hook on block side facing north<br/>3: Tripwire hook on block side facing east<br/> |
| powered_bit  | `0x8`           | `false`       | `false`<br/>`true`          | `0`<br/>`1`                 | True if the tripwire hook is active.                                                                                                                                                                                                                                              |



### Turtle Egg
Java Edition:

| Name  | Default value | Allowed values              | Description                                                                          |
|-------|---------------|-----------------------------|--------------------------------------------------------------------------------------|
| eggs  | `1`           | `1`<br/>`2`<br/>`3`<br/>`4` | Number of eggs.                                                                      |
| hatch | `0`           | `0`<br/>`1`<br/>`2`         | Determines how close an egg is to hatching; starts at 0 and is randomly incremented. |

Bedrock Edition:

| Name             | Metadata Bits   | Default value | Allowed values                                         | Values forMetadata Bits     | Description                                                                                  |
|------------------|-----------------|---------------|--------------------------------------------------------|-----------------------------|----------------------------------------------------------------------------------------------|
| turtle_egg_count | `0x1`<br/>`0x2` | `one_egg`     | `one_egg`<br/>`two_egg`<br/>`three_egg`<br/>`four_egg` | `0`<br/>`1`<br/>`2`<br/>`3` | Number of eggs.                                                                              |
| cracked_state    | `0x4`<br/>`0x8` | `no_cracks`   | `no_cracks`<br/>`cracked`<br/>`max_cracked`            | `0`<br/>`1`<br/>`2`         | Determines how close an egg is to hatching; starts at no cracks and is randomly incremented. |



### Twisting Vines
Java Edition
Twisting Vines:

| Name | Default value | Allowed values                                                                                                                                                                                                              | Description                                         |
|------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| age  | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15`<br/>`16`<br/>`17`<br/>`18`<br/>`19`<br/>`20`<br/>`21`<br/>`22`<br/>`23`<br/>`24`<br/>`25` | Increments for every block the twisting vine grows. |

Bedrock Edition

| Name               | Metadata Bits                                  | Default value | Allowed values                                                                                                                                                                                                              | Values forMetadata Bits                                                                                                                                                                                                     | Description                                         |
|--------------------|------------------------------------------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| twisting_vines_age | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8`<br/>`0x10` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15`<br/>`16`<br/>`17`<br/>`18`<br/>`19`<br/>`20`<br/>`21`<br/>`22`<br/>`23`<br/>`24`<br/>`25` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15`<br/>`16`<br/>`17`<br/>`18`<br/>`19`<br/>`20`<br/>`21`<br/>`22`<br/>`23`<br/>`24`<br/>`25` | Increments for every block the twisting vine grows. |



### Underwater Torch
| Name                   | Metadata Bits             | Default value | Allowed values                                      | Values forMetadata Bits             | Description                                                                                                                                  |
|------------------------|---------------------------|---------------|-----------------------------------------------------|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| torch_facing_direction | `0x1`<br/>`0x2`<br/>`0x4` | `west`        | `west`<br/>`east`<br/>`north`<br/>`south`<br/>`top` | `1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | The face of the block that the torch is attached to. If the torch is a wall torch, the top of the torch faces opposite to this direction.[5] |
|                        |                           |               | `unknown`                                           | `0`                                 | Unused                                                                                                                                       |



### Vines
Java Edition:

| Name  | Default value | Allowed values     | Description                                          |
|-------|---------------|--------------------|------------------------------------------------------|
| east  | `false`       | `false`<br/>`true` | When true, a vine texture is displayed on the east.  |
| north | `false`       | `false`<br/>`true` | When true, a vine texture is displayed on the north. |
| south | `false`       | `false`<br/>`true` | When true, a vine texture is displayed on the south. |
| up    | `false`       | `false`<br/>`true` | When true, a vine texture is displayed on the top.   |
| west  | `false`       | `false`<br/>`true` | When true, a vine texture is displayed on the west.  |

Bedrock Edition:

| Name                | Metadata Bits                       | Default value | Allowed values                                                                                                                    | Values forMetadata Bits                                                                                                           | Description                                                                                                                                                                                                                                                                            |
|---------------------|-------------------------------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| vine_direction_bits | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | The directions the vine exists, excluding up. Each bit determines one direction:0x1: Vines at the south<br/>0x2: Vines at the west<br/>0x4: Vines at the north<br/>0x8: Vines at the east<br/>Note: Vines gain the ceiling vines if there's a block above, block state doesn't change. |



### Walls
Java Edition

| Name        | Default value | Allowed values              | Description                                                  |
|-------------|---------------|-----------------------------|--------------------------------------------------------------|
| east        | `none`        | `low`<br/>`none`<br/>`tall` | How the wall extends from the center post to the east.       |
| north       | `none`        | `low`<br/>`none`<br/>`tall` | How the wall extends from the center post to the north.      |
| south       | `none`        | `low`<br/>`none`<br/>`tall` | How the wall extends from the center post to the south.      |
| up          | `true`        | `false`<br/>`true`          | When true, the wall has a center post.                       |
| waterlogged | `false`       | `false`<br/>`true`          | Whether or not there's water in the same place as this wall. |
| west        | `none`        | `low`<br/>`none`<br/>`tall` | How the wall extends from the center post to the west.       |

Bedrock Edition
Non-blackstone and deepslate wall:

| Name                       | Metadata Bits                       | Default value | Allowed values                                                                                                                                                                                                                                        | Values forMetadata Bits                                                                                         | Description                                                            |
|----------------------------|-------------------------------------|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| wall_block_type            | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8` | `cobblestone` | `cobblestone`<br/>`mossy_cobblestone`<br/>`granite`<br/>`diorite`<br/>`andesite`<br/>`sandstone`<br/>`brick`<br/>`stone_brick`<br/>`mossy_stone_brick`<br/>`nether_brick`<br/>`end_brick`<br/>`prismarine`<br/>`red_sandstone`<br/>`red_nether_brick` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13` | The type of wall; for example,`stone_brick`denotes a stone brick wall. |
| wall_connection_type_east  | Not Supported                       | `none`        | `none`<br/>`short`<br/>`tall`                                                                                                                                                                                                                         | `Unsupported`                                                                                                   | How the wall extends from the center post to the east.                 |
| wall_connection_type_north | Not Supported                       | `none`        | `none`<br/>`short`<br/>`tall`                                                                                                                                                                                                                         | `Unsupported`                                                                                                   | How the wall extends from the center post to the north.                |
| wall_connection_type_south | Not Supported                       | `none`        | `none`<br/>`short`<br/>`tall`                                                                                                                                                                                                                         | `Unsupported`                                                                                                   | How the wall extends from the center post to the south.                |
| wall_connection_type_west  | Not Supported                       | `none`        | `none`<br/>`short`<br/>`tall`                                                                                                                                                                                                                         | `Unsupported`                                                                                                   | How the wall extends from the center post to the west.                 |
| wall_post_bit              | Not Supported                       | `true`        | `false`<br/>`true`                                                                                                                                                                                                                                    | `Unsupported`                                                                                                   | Whether or not the wall has a center post.                             |

Blackstone and deepslate wall:

| Name                       | Metadata Bits | Default value | Allowed values                | Values forMetadata Bits | Description                                             |
|----------------------------|---------------|---------------|-------------------------------|-------------------------|---------------------------------------------------------|
| wall_connection_type_east  | Not Supported | `none`        | `none`<br/>`short`<br/>`tall` | `Unsupported`           | How the wall extends from the center post to the east.  |
| wall_connection_type_north | Not Supported | `none`        | `none`<br/>`short`<br/>`tall` | `Unsupported`           | How the wall extends from the center post to the north. |
| wall_connection_type_south | Not Supported | `none`        | `none`<br/>`short`<br/>`tall` | `Unsupported`           | How the wall extends from the center post to the south. |
| wall_connection_type_west  | Not Supported | `none`        | `none`<br/>`short`<br/>`tall` | `Unsupported`           | How the wall extends from the center post to the west.  |
| wall_post_bit              | Not Supported | `true`        | `false`<br/>`true`            | `Unsupported`           | Whether or not the wall has a center post.              |

