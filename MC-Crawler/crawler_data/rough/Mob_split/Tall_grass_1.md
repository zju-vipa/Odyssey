## Data values
### ID
Java Edition:

| Name       | Identifier   | Form         | Block tags                                                                   | Translation key              |
|------------|--------------|--------------|------------------------------------------------------------------------------|------------------------------|
| Tall Grass | `tall_grass` | Block & Item | `enchantment_power_transmitter`<br/>`replaceable`<br/>`replaceable_by_trees` | `block.minecraft.tall_grass` |

Bedrock Edition:

| Name             | Identifier                         | Alias ID           | Numeric ID | Form                       | Item ID[i 1]   | Translation key                |
|------------------|------------------------------------|--------------------|------------|----------------------------|----------------|--------------------------------|
| Double Tallgrass | `double_plant‌[until BE 1.21.0]`   | None               | `175`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.double_plant.grass.name` |
| Double Tallgrass | `tall_grass‌[upcoming: BE 1.21.0]` | `double_plant / 2` | `-864`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.double_plant.grass.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑ a bAvailable with /give command.
3. ↑ a bThe block's direct item form has the same id as the block.

### Block states
See also: Block states

Java Edition:

| Name | Default value | Allowed values      | Description                                    |
|------|---------------|---------------------|------------------------------------------------|
| half | `lower`       | `lower`<br/>`upper` | The half of the plant contained in this block. |

Bedrock Edition:

| Name              | Metadata Bits             | Default value | Allowed values     | Values forMetadata Bits | Description                                               |
|-------------------|---------------------------|---------------|--------------------|-------------------------|-----------------------------------------------------------|
| double_plant_type | `0x1`<br/>`0x2`<br/>`0x4` | `sunflower`   | `sunflower`        | `0`                     | Sunflower                                                 |
|                   |                           |               | `syringa`          | `1`                     | Lilac                                                     |
|                   |                           |               | `grass`            | `2`                     | Double Tallgrass                                          |
|                   |                           |               | `fern`             | `3`                     | Large Fern                                                |
|                   |                           |               | `rose`             | `4`                     | Rose Bush                                                 |
|                   |                           |               | `paeonia`          | `5`                     | Peony                                                     |
| upper_block_bit   | `0x8`                     | `false`       | `false`<br/>`true` | `0`<br/>`1`             | If it is the upper half of the plant. For items, it is 0. |


