## Data values
### ID
Java Edition:

| Name        | Identifier    | Form         | Block tags                                                                   | Translation key               |
|-------------|---------------|--------------|------------------------------------------------------------------------------|-------------------------------|
| Short Grass | `short_grass` | Block & Item | `enchantment_power_transmitter`<br/>`replaceable`<br/>`replaceable_by_trees` | `block.minecraft.short_grass` |

Bedrock Edition:

| Name  | Identifier                          | Alias ID        | Numeric ID | Form                       | Item ID[i 1]   | Translation key             |
|-------|-------------------------------------|-----------------|------------|----------------------------|----------------|-----------------------------|
| Grass | `tallgrass‌[until BE 1.21.0]`       | None            | `31`       | Block & Giveable Item[i 2] | Identical[i 3] | `tile.tallgrass.grass.name` |
| Grass | `short_grass‌[upcoming: BE 1.21.0]` | `tallgrass / 0` | `31`       | Block & Giveable Item[i 2] | Identical[i 3] | `tile.tallgrass.grass.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑ a bAvailable with /give command.
3. ↑ a bThe block's direct item form has the same id as the block.

### Block states
See also: Block states

Bedrock Edition:

| Name            | Metadata Bits   | Default value | Allowed values | Values forMetadata Bits | Description                                                                                         |
|-----------------|-----------------|---------------|----------------|-------------------------|-----------------------------------------------------------------------------------------------------|
| tall_grass_type | `0x1`<br/>`0x2` | `default`     | `default`      | `0`                     | Fern(Unused variant which looks identical to grass, but turns into alarge fernwhenbone mealis used) |
|                 |                 |               | `tall`         | `1`                     | Grass                                                                                               |
|                 |                 |               | `fern`         | `2`                     | Fern                                                                                                |
|                 |                 |               | `snow`         | `3`                     | Fern (looks identical to actual fern, but turns intodouble tallgrasswhenbone mealis used)           |


