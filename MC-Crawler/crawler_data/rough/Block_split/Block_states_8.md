### Flowers
Java Edition:
Sunflower, lilac, rose bush, peony, and pitcher plant

| Name | Default value | Allowed values      | Description                                    |
|------|---------------|---------------------|------------------------------------------------|
| half | `lower`       | `lower`<br/>`upper` | The half of the plant contained in this block. |

Bedrock Edition:
All small flowers except dandelion, wither rose, and torchflower

| Name        | Metadata Bits                       | Default value | Allowed values       | Values forMetadata Bits | Description        |
|-------------|-------------------------------------|---------------|----------------------|-------------------------|--------------------|
| flower_type | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8` | `poppy`       | `poppy`              | `0`                     | Poppy              |
|             |                                     |               | `orchid`             | `1`                     | Blue Orchid        |
|             |                                     |               | `allium`             | `2`                     | Allium             |
|             |                                     |               | `houstonia`          | `3`                     | Azure Bluet        |
|             |                                     |               | `tulip_red`          | `4`                     | Red Tulip          |
|             |                                     |               | `tulip_orange`       | `5`                     | Orange Tulip       |
|             |                                     |               | `tulip_white`        | `6`                     | White Tulip        |
|             |                                     |               | `tulip_pink`         | `7`                     | Pink Tulip         |
|             |                                     |               | `oxeye`              | `8`                     | Oxeye Daisy        |
|             |                                     |               | `cornflower`         | `9`                     | Cornflower         |
|             |                                     |               | `lily_of_the_valley` | `10`                    | Lily of the Valley |

Sunflower, lilac, rose bush, and peony

| Name              | Metadata Bits             | Default value | Allowed values     | Values forMetadata Bits | Description                                               |
|-------------------|---------------------------|---------------|--------------------|-------------------------|-----------------------------------------------------------|
| double_plant_type | `0x1`<br/>`0x2`<br/>`0x4` | `sunflower`   | `sunflower`        | `0`                     | Sunflower                                                 |
|                   |                           |               | `syringa`          | `1`                     | Lilac                                                     |
|                   |                           |               | `grass`            | `2`                     | Double Tallgrass                                          |
|                   |                           |               | `fern`             | `3`                     | Large Fern                                                |
|                   |                           |               | `rose`             | `4`                     | Rose Bush                                                 |
|                   |                           |               | `paeonia`          | `5`                     | Peony                                                     |
| upper_block_bit   | `0x8`                     | `false`       | `false`<br/>`true` | `0`<br/>`1`             | If it is the upper half of the plant. For items, it is 0. |

Pitcher plant

| Name            | Metadata Bits | Default value | Allowed values     | Values forMetadata Bits | Description                           |
|-----------------|---------------|---------------|--------------------|-------------------------|---------------------------------------|
| upper_block_bit | Not Supported | `false`       | `false`<br/>`true` | `Unsupported`           | If it is the upper half of the plant. |



### Flower Pot
Bedrock Edition:

| Name       | Metadata Bits | Default value | Allowed values     | Values forMetadata Bits | Description                                                       |
|------------|---------------|---------------|--------------------|-------------------------|-------------------------------------------------------------------|
| update_bit | `0x1`         | `false`       | `false`<br/>`true` | `0`<br/>`1`             | false: Empty flower pot.<br/>true: Flower pot with contents.<br/> |



### Froglight
Java Edition:

| Name | Default value | Allowed values | Description                            |
|------|---------------|----------------|----------------------------------------|
| axis | `y`           | `x`            | The froglight is oriented east–west.   |
|      |               | `y`            | The froglight is oriented vertically.  |
|      |               | `z`            | The froglight is oriented north–south. |

Bedrock Edition:

| Name        | Metadata Bits   | Default value | Allowed values | Values forMetadata Bits | Description                            |
|-------------|-----------------|---------------|----------------|-------------------------|----------------------------------------|
| pillar_axis | `0x1`<br/>`0x2` | `y`           | `x`            | `1`                     | The froglight is oriented east–west.   |
|             |                 |               | `y`            | `0`                     | The froglight is oriented vertically.  |
|             |                 |               | `z`            | `2`                     | The froglight is oriented north–south. |



### Frosted Ice
Java Edition：

| Name | Default value | Allowed values      | Description                |
|------|---------------|---------------------|----------------------------|
| age  | `0`           | `0`                 | Freshly generated ice.     |
|      |               | `1`<br/>`2`<br/>`3` | Ice with spreading cracks. |

Bedrock Edition：

| Name | Metadata Bits   | Default value | Allowed values                                                                                    | Values forMetadata Bits | Description                |
|------|-----------------|---------------|---------------------------------------------------------------------------------------------------|-------------------------|----------------------------|
| age  | `0x1`<br/>`0x2` | `0`           | `0`                                                                                               | `0`                     | Freshly generated ice.     |
|      |                 |               | `1`<br/>`2`<br/>`3`                                                                               | `1`<br/>`2`<br/>`3`     | Ice with spreading cracks. |
|      |                 |               | `4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | `Unsupported`           | Unused                     |



### Furnace
Java Edition:

| Name   | Default value | Allowed values                            | Description                                                                                                                |
|--------|---------------|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| facing | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the furnace's opening faces.<br/>The opposite from the direction the player faces while placing the furnace. |
| lit    | `false`       | `false`<br/>`true`                        | If the furnace is lit.                                                                                                     |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values                            | Values forMetadata Bits | Description                                                                                                                |
|------------------------------|---------------|---------------|-------------------------------------------|-------------------------|----------------------------------------------------------------------------------------------------------------------------|
| minecraft:cardinal_direction | Not Supported | `south`       | `east`<br/>`north`<br/>`south`<br/>`west` | `Unsupported`           | The direction the furnace's opening faces.<br/>The opposite from the direction the player faces while placing the furnace. |



### Glass Panes
Java Edition:

| Name        | Default value | Allowed values     | Description                                                          |
|-------------|---------------|--------------------|----------------------------------------------------------------------|
| east        | `false`       | `false`<br/>`true` | When true, the glass pane extends from the center post to the east.  |
| north       | `false`       | `false`<br/>`true` | When true, the glass pane extends from the center post to the north. |
| south       | `false`       | `false`<br/>`true` | When true, the glass pane extends from the center post to the south. |
| waterlogged | `false`       | `false`<br/>`true` | Whether or not there's water in the same place as this glass pane.   |
| west        | `false`       | `false`<br/>`true` | When true, the glass pane extends from the center post to the west.  |



### Glazed Terracotta
Java Edition:

| Name   | Default value | Allowed values                            | Description                                                               |
|--------|---------------|-------------------------------------------|---------------------------------------------------------------------------|
| facing | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The opposite from the direction the player faces while placing the block. |

Bedrock Edition:

| Name             | Metadata Bits             | Default value | Allowed values              | Values forMetadata Bits     | Description                                                                                                                                             |
|------------------|---------------------------|---------------|-----------------------------|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing_direction | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `2`<br/>`3`<br/>`4`<br/>`5` | `2`<br/>`3`<br/>`4`<br/>`5` | The direction the block faces.<br/>Opposite from the direction a player faces when placing the block.2: North<br/>3: South<br/>4: West<br/>5: East<br/> |
|                  |                           |               | `0`<br/>`1`                 | `0`<br/>`1`                 | Unused                                                                                                                                                  |



### Glow Lichen
Java Edition:

| Name        | Default value | Allowed values     | Description                                                         |
|-------------|---------------|--------------------|---------------------------------------------------------------------|
| down        | `false`       | `false`<br/>`true` | When true, a glow lichen texture is displayed on the bottom.        |
| east        | `false`       | `false`<br/>`true` | When true, a glow lichen texture is displayed on the east.          |
| north       | `false`       | `false`<br/>`true` | When true, a glow lichen texture is displayed on the north.         |
| south       | `false`       | `false`<br/>`true` | When true, a glow lichen texture is displayed on the south.         |
| up          | `false`       | `false`<br/>`true` | When true, a glow lichen texture is displayed on the top.           |
| waterlogged | `false`       | `false`<br/>`true` | Whether or not there's water in the same place as this glow lichen. |
| west        | `false`       | `false`<br/>`true` | When true, a glow lichen texture is displayed on the west.          |

Bedrock Edition:

| Name                      | Metadata Bits                                             | Default value | Allowed values | Values forMetadata Bits | Description                                                                                                                                                                                        |
|---------------------------|-----------------------------------------------------------|---------------|----------------|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| multi_face_direction_bits | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8`<br/>`0x10`<br/>`0x20` | `0`           | `0 to 63`      | `0 to 63`               | The directions the glow lichen exists. Each bit determines one direction:0x1: Down<br/>0x2: Up<br/>0x4: South<br/>0x8: West<br/>0x10: North<br/>0x20: East<br/>0 is unused and it behaves like 63. |

