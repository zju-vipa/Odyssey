### Bee nests
Oak, birch, and cherry trees grown from saplings that are within 2 blocks of any flower, flowering azalea,‌[JE  only] or flowering azalea leaves‌[JE  only] have a 5% chance to grow with a bee nest and 1-3 bees in it.

### Decoration
Any kind of sapling can be placed in a flower pot.

### Fuel
Saplings can be used as a fuel in furnaces, smelting 0.5 items per sapling.

### Composting
Placing a sapling into a composter has a 30% chance of raising the compost level by 1. A stack of saplings yields an average of 2.74 bone meal.

## Data values
### ID
Java Edition:

| Name             | Identifier         | Form         | Block tags | Item tags  | Translation key                    |
|------------------|--------------------|--------------|------------|------------|------------------------------------|
| Oak Sapling      | `oak_sapling`      | Block & Item | `saplings` | `saplings` | `block.minecraft.oak_sapling`      |
| Spruce Sapling   | `spruce_sapling`   | Block & Item | `saplings` | `saplings` | `block.minecraft.spruce_sapling`   |
| Birch Sapling    | `birch_sapling`    | Block & Item | `saplings` | `saplings` | `block.minecraft.birch_sapling`    |
| Jungle Sapling   | `jungle_sapling`   | Block & Item | `saplings` | `saplings` | `block.minecraft.jungle_sapling`   |
| Acacia Sapling   | `acacia_sapling`   | Block & Item | `saplings` | `saplings` | `block.minecraft.acacia_sapling`   |
| Dark Oak Sapling | `dark_oak_sapling` | Block & Item | `saplings` | `saplings` | `block.minecraft.dark_oak_sapling` |
| Cherry Sapling   | `cherry_sapling`   | Block & Item | `saplings` | `saplings` | `block.minecraft.cherry_sapling`   |

Bedrock Edition:

| Name             | Identifier                                | Alias ID      | Numeric ID | Form                       | Item ID[i 1]   | Translation key                                                                                                                                                                    |
|------------------|-------------------------------------------|---------------|------------|----------------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Sapling          | `sapling‌[until BE 1.20.80]`              | None          | `6`        | Block & Giveable Item[i 2] | Identical[i 3] | `tile.sapling.oak.name`<br/>`tile.sapling.spruce.name`<br/>`tile.sapling.birch.name`<br/>`tile.sapling.jungle.name`<br/>`tile.sapling.acacia.name`<br/>`tile.sapling.big_oak.name` |
| Oak Sapling      | `oak_sapling‌[upcoming: BE 1.20.80]`      | `sapling / 0` | `6`        | Block & Giveable Item[i 2] | Identical[i 3] | `tile.sapling.oak.name`                                                                                                                                                            |
| Spruce Sapling   | `spruce_sapling‌[upcoming: BE 1.20.80]`   | `sapling / 1` | `-825`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.sapling.spruce.name`                                                                                                                                                         |
| Birch Sapling    | `birch_sapling‌[upcoming: BE 1.20.80]`    | `sapling / 2` | `-826`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.sapling.birch.name`                                                                                                                                                          |
| Jungle Sapling   | `jungle_sapling‌[upcoming: BE 1.20.80]`   | `sapling / 3` | `-827`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.sapling.jungle.name`                                                                                                                                                         |
| Acacia Sapling   | `acacia_sapling‌[upcoming: BE 1.20.80]`   | `sapling / 4` | `-828`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.sapling.acacia.name`                                                                                                                                                         |
| Dark Oak Sapling | `dark_oak_sapling‌[upcoming: BE 1.20.80]` | `sapling / 5` | `-829`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.sapling.big_oak.name`                                                                                                                                                        |
| Cherry Sapling   | `cherry_sapling`                          | None          | `-547`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.cherry_sapling.name`                                                                                                                                                         |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑ a b c d e f g hAvailable with /give command.
3. ↑ a b c d e f g hThe block's direct item form has the same id as the block.

### Block states
See also: Block states

Java Edition:

** Sapling **
| Name  | Default value | Allowed values | Description                           |
|-------|---------------|----------------|---------------------------------------|
| stage | `0`           | `0`<br/>`1`    | Specifies the sapling's growth stage. |

Bedrock Edition:

| Name         | Metadata Bits             | Default value | Allowed values     | Values forMetadata Bits | Description                           |
|--------------|---------------------------|---------------|--------------------|-------------------------|---------------------------------------|
| age_bit      | `0x8`                     | `false`       | `false`<br/>`true` | `0`<br/>`1`             | Specifies the sapling's growth stage. |
| sapling_type | `0x1`<br/>`0x2`<br/>`0x4` | `oak`         | `acacia`           | `4`                     | Acacia Sapling                        |
|              |                           |               | `birch`            | `2`                     | Birch Sapling                         |
|              |                           |               | `dark_oak`         | `5`                     | Dark Oak Sapling                      |
|              |                           |               | `jungle`           | `3`                     | Jungle Sapling                        |
|              |                           |               | `oak`              | `0`                     | Oak Sapling                           |
|              |                           |               | `spruce`           | `1`                     | Spruce Sapling                        |




