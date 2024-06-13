### Bees
Bees engage in a pollinating behavior with tulips, increasing the honey level in beehives and bee nests by 1.

### Breeding
Tulips can be used to breed, grow, and lead bees.

### Bee nests
Oak, birch, and cherry trees grown from saplings that are within 2 blocks of a tulip have a 5% chance to grow with a bee nest and 1-3 bees in it.

### Composting
Placing a tulip into a composter has a 65% chance of raising the compost level by 1. A stack of tulips yields an average of 5.94 bone meal.

## Data values
### ID
Java Edition:

| Name         | Identifier     | Form         | Block tags                    | Item tags                     | Translation key                |
|--------------|----------------|--------------|-------------------------------|-------------------------------|--------------------------------|
| Red Tulip    | `red_tulip`    | Block & Item | `flowers`<br/>`small_flowers` | `flowers`<br/>`small_flowers` | `block.minecraft.red_tulip`    |
| Orange Tulip | `orange_tulip` | Block & Item | `flowers`<br/>`small_flowers` | `flowers`<br/>`small_flowers` | `block.minecraft.orange_tulip` |
| White Tulip  | `white_tulip`  | Block & Item | `flowers`<br/>`small_flowers` | `flowers`<br/>`small_flowers` | `block.minecraft.white_tulip`  |
| Pink Tulip   | `pink_tulip`   | Block & Item | `flowers`<br/>`small_flowers` | `flowers`<br/>`small_flowers` | `block.minecraft.pink_tulip`   |

Bedrock Edition:

| Name         | Identifier                            | Alias ID         | Numeric ID | Form                       | Item ID[i 1]   | Translation key                                                                                                                                   |
|--------------|---------------------------------------|------------------|------------|----------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| Tulips       | `red_flower‌[until BE 1.20.80]`       | None             | `38`       | Block & Giveable Item[i 2] | Identical[i 3] | `tile.red_flower.tulipRed.name`<br/>`tile.red_flower.tulipOrange.name`<br/>`tile.red_flower.tulipWhite.name`<br/>`tile.red_flower.tulipPink.name` |
| Red Tulip    | `red_tulip‌[upcoming: BE 1.20.80]`    | `red_flower / 4` | `-833`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.red_flower.tulipRed.name`                                                                                                                   |
| Orange Tulip | `orange_tulip‌[upcoming: BE 1.20.80]` | `red_flower / 5` | `-834`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.red_flower.tulipOrange.name`                                                                                                                |
| White Tulip  | `white_tulip‌[upcoming: BE 1.20.80]`  | `red_flower / 6` | `-835`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.red_flower.tulipWhite.name`                                                                                                                 |
| Pink Tulip   | `pink_tulip‌[upcoming: BE 1.20.80]`   | `red_flower / 7` | `-836`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.red_flower.tulipPink.name`                                                                                                                  |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑ a b c d eAvailable with /give command.
3. ↑ a b c d eThe block's direct item form has the same id as the block.

### Block states
See also: Block states

Bedrock Edition:

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


