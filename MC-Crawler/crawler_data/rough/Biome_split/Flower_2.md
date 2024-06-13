### Suspicious stew
Main article: Suspicious Stew
All small flowers can be used to create suspicious stew. When a flower is used on a brown mooshroom, the brown mooshroom produces a suspicious stew related to that flower the next time it is milked with a bowl. The mooshroom returns to producing regular mushroom stew until fed another flower. Eating one bowl of suspicious stew restores 6 () hunger and 7.2 hunger saturation, as well as producing a brief status effect.

| Ingredients                                                     | Crafting recipe |
|-----------------------------------------------------------------|-----------------|
| Red Mushroom+<br/>Brown Mushroom+<br/>Bowl+<br/>AnySmall Flower |                 |

Using different flowers results in different effects. All are short-lived, but some have lasting effects: The regeneration restores 2 or 3 health; Wither or poison inflicts up to 2 hearts damage. The saturation effectively makes those stews a superfood: they restore up to 6 hunger and 12 saturation points on top of their food value, for a total of 12 ( × 6) and over 19 points of saturation.

| Flower                    | Effect          | Duration (JE) | Duration (BE) |
|---------------------------|-----------------|---------------|---------------|
| Allium                    | Fire Resistance | 4s            | 2s            |
| Azure Bluet               | Blindness       | 8s            | 6s            |
| Blue Orchid<br/>Dandelion | Saturation      | 0.35s         | 0.3s          |
| Cornflower                | Jump Boost      | 6s            | 4s            |
| Lily of the Valley        | Poison          | 12s           | 10s           |
| Oxeye Daisy               | Regeneration    | 8s            | 6s            |
| Poppy<br/>Torchflower     | Night Vision    | 5s            | 4s            |
| Tulips                    | Weakness        | 9s            | 7s            |
| Wither Rose               | Wither          | 8s            | 6s            |

### Bees
Bees engage in a pollinating behavior with flowers, increasing the honey level in beehives and bee nests by 1. Bees attempt to pollinate wither roses, although they get damaged in the process.[2] In Bedrock Edition, bees ignore snowlogged flowers.[3]

### Breeding
Any flower can be used for bees, including wither roses.[4]

### Bee nests
Oak, birch, and cherry trees grown from saplings that are within 2 blocks of any flower have a 5% chance to grow with a bee nest and 1-3 bees in it.

### Composting
Placing any flower (except for the torchflower or a pitcher plant) into a composter has a 65% chance of raising the compost level by 1. A stack of flowers yields an average of 5.94 bone meal.

Placing a torchflower or a pitcher plant into a composter has a 85% chance of raising the compost level by 1.

## Block states
See also: Block states

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




