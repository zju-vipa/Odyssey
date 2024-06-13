### 
Java Edition:

| Name  | Default value | Allowed values     | Description                                                                                                      |
|-------|---------------|--------------------|------------------------------------------------------------------------------------------------------------------|
| snowy | `false`       | `false`<br/>`true` | If true, the block uses a snowy side and top texture.<br/>In-game, this is true when asnow blockorsnowis on top. |

### Grindstone
Java Edition:

| Name   | Default value | Allowed values                            | Description                                                                                                                                 |
|--------|---------------|-------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| face   | `wall`        | `ceiling`<br/>`floor`<br/>`wall`          | What the grindstone is attached to.                                                                                                         |
| facing | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the grindstone is facing.<br/>Opposite from the direction the player faces when placing a grindstone on the floor or ceiling. |

Bedrock Edition:

| Name       | Metadata Bits   | Default value | Allowed values                                     | Values forMetadata Bits     | Description                                                                                                                                                                              |
|------------|-----------------|---------------|----------------------------------------------------|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| attachment | `0x4`<br/>`0x8` | `standing`    | `standing`<br/>`hanging`<br/>`side`<br/>`multiple` | `0`<br/>`1`<br/>`2`<br/>`3` | What the grindstone is attached to.                                                                                                                                                      |
| direction  | `0x1`<br/>`0x2` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`                        | `0`<br/>`1`<br/>`2`<br/>`3` | The direction the grindstone is facing. Opposite from the direction a player faces when placing the block.0: South facing<br/>1: West facing<br/>2: North facing<br/>3: East facing<br/> |



### Hay Bale
Java Edition:

| Name | Default value | Allowed values | Description                            |
|------|---------------|----------------|----------------------------------------|
| axis | `y`           | `x`            | The hay block is oriented east–west.   |
|      |               | `y`            | The hay block is oriented vertically.  |
|      |               | `z`            | The hay block is oriented north–south. |

Bedrock Edition:

| Name        | Metadata Bits   | Default value | Allowed values              | Values forMetadata Bits     | Description                                |
|-------------|-----------------|---------------|-----------------------------|-----------------------------|--------------------------------------------|
| pillar_axis | `0x4`<br/>`0x8` | `y`           | `x`<br/>`y`<br/>`z`         | `1`<br/>`0`<br/>`2`         | The axis along which the block is oriented |
| deprecated  | `0x1`<br/>`0x2` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3` | `0`<br/>`1`<br/>`2`<br/>`3` | Unused, has no effect in game.             |



### Hopper
Java Edition:

| Name    | Default value | Allowed values                                       | Description                                                                                                                              |
|---------|---------------|------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| enabled | `true`        | `false`<br/>`true`                                   | True if hopper can move items to and from its inventory.<br/>When the hopper is being powered by redstone current, this is set to false. |
| facing  | `down`        | `down`<br/>`east`<br/>`north`<br/>`south`<br/>`west` | The direction the hopper's output points.<br/>The hopper pushes items into containers in this direction only.                            |

Bedrock Edition:

| Name             | Metadata Bits             | Default value | Allowed values                      | Values forMetadata Bits             | Description                                                                                                                                                                                                                                                       |
|------------------|---------------------------|---------------|-------------------------------------|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing_direction | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4` | The direction the hopper's output points.<br/>The hopper pushes items into containers in this direction only.0: Output facing down<br/>1: (unused)<br/>2: Output facing north<br/>3: Output facing south<br/>4: Output facing west<br/>5: Output facing east<br/> |
| toggle_bit       | `0x8`                     | `false`       | `false`<br/>`true`                  | `0`<br/>`1`                         | 1 if hopper cannot move items to and from its inventory.<br/>When the hopper is being powered by redstone current, this is set to true.                                                                                                                           |



### Infested Block
Bedrock Edition:
Infested Deepslate:

| Name        | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                            |
|-------------|---------------|---------------|----------------|-------------------------|----------------------------------------|
| pillar_axis | Not Supported | `y`           | `x`            | `Unsupported`           | The deepslate is oriented east–west.   |
|             |               |               | `y`            | `Unsupported`           | The deepslate is oriented vertically.  |
|             |               |               | `z`            | `Unsupported`           | The deepslate is oriented north–south. |

Others:

| Name                   | Metadata Bits             | Default value | Allowed values         | Values forMetadata Bits | Description                   |
|------------------------|---------------------------|---------------|------------------------|-------------------------|-------------------------------|
| monster_egg_stone_type | `0x1`<br/>`0x2`<br/>`0x4` | `stone`       | `stone`                | `0`                     | Infested Stone                |
|                        |                           |               | `cobblestone`          | `1`                     | Infested Cobblestone          |
|                        |                           |               | `stone_brick`          | `2`                     | Infested Stone Brick          |
|                        |                           |               | `mossy_stone_brick`    | `3`                     | Infested Mossy Stone Brick    |
|                        |                           |               | `cracked_stone_brick`  | `4`                     | Infested Cracked Stone Brick  |
|                        |                           |               | `chiseled_stone_brick` | `5`                     | Infested Chiseled Stone Brick |



### Iron Bars
Java Edition:

| Name        | Default value | Allowed values     | Description                                                        |
|-------------|---------------|--------------------|--------------------------------------------------------------------|
| east        | `false`       | `false`<br/>`true` | When true, the iron bars extend from the center post to the east.  |
| north       | `false`       | `false`<br/>`true` | When true, the iron bars extend from the center post to the north. |
| south       | `false`       | `false`<br/>`true` | When true, the iron bars extend from the center post to the south. |
| waterlogged | `false`       | `false`<br/>`true` | Whether or not there's water in the same place as these iron bars. |
| west        | `false`       | `false`<br/>`true` | When true, the iron bars extend from the center post to the west.  |

### Item Frame and Glow Item Frame
Bedrock Edition
Item Frame:

| Name                 | Metadata Bits   | Default value | Allowed values     | Values forMetadata Bits | Description                         |
|----------------------|-----------------|---------------|--------------------|-------------------------|-------------------------------------|
| facing_direction     | `0x1`<br/>`0x2` | `0`           | `5`                | `0`                     | East facing item frame              |
|                      |                 |               | `4`                | `1`                     | West facing item frame              |
|                      |                 |               | `3`                | `2`                     | South facing item frame             |
|                      |                 |               | `2`                | `3`                     | North facing item frame             |
|                      |                 |               | `1`                | `Unsupported`           | Up facing item frame                |
|                      |                 |               | `0`                | `Unsupported`           | Down facing item frame              |
| item_frame_map_bit   | `0x4`           | `false`       | `false`<br/>`true` | `0`<br/>`1`             | If this item frame contains a map.  |
| item_frame_photo_bit | Not Supported   | `false`       | `false`<br/>`true` | `Unsupported`           | If this item frame contains aphoto. |

Glow Item Frame:

| Name                 | Metadata Bits | Default value | Allowed values     | Values forMetadata Bits | Description                         |
|----------------------|---------------|---------------|--------------------|-------------------------|-------------------------------------|
| facing_direction     | Not Supported | `0`           | `5`                | `Unsupported`           | East facing item frame              |
|                      |               |               | `4`                | `Unsupported`           | West facing item frame              |
|                      |               |               | `3`                | `Unsupported`           | South facing item frame             |
|                      |               |               | `2`                | `Unsupported`           | North facing item frame             |
|                      |               |               | `1`                | `Unsupported`           | Up facing item frame                |
|                      |               |               | `0`                | `Unsupported`           | Down facing item frame              |
| item_frame_map_bit   | Not Supported | `false`       | `false`<br/>`true` | `Unsupported`           | If this item frame contains a map.  |
| item_frame_photo_bit | Not Supported | `false`       | `false`<br/>`true` | `Unsupported`           | If this item frame contains aphoto. |



