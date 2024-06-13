## Data values
Note that when a log or stem is placed, it changes its facing parameters, placing in the direction relative to the block it is placed on.

Logs and stems consider only the axis; a sideways log or stem placed while facing north does not have a top texture rotated 180 degrees from a log or stem placed south.[1]

### ID
Java Edition:

| Name         | Identifier     | Form         | Block tags                                                             | Item tags                                           | Translation key                |
|--------------|----------------|--------------|------------------------------------------------------------------------|-----------------------------------------------------|--------------------------------|
| Oak Log      | `oak_log`      | Block & Item | `logs`<br/>`logs_that_burn`<br/>`oak_logs`<br/>`mineable/axe`          | `logs`<br/>`logs_that_burn`<br/>`oak_logs`          | `block.minecraft.oak_log`      |
| Spruce Log   | `spruce_log`   | Block & Item | `logs`<br/>`logs_that_burn`<br/>`spruce_logs`<br/>`mineable/axe`       | `logs`<br/>`logs_that_burn`<br/>`spruce_logs`       | `block.minecraft.spruce_log`   |
| Birch Log    | `birch_log`    | Block & Item | `birch_logs`<br/>`logs`<br/>`logs_that_burn`<br/>`mineable/axe`        | `birch_logs`<br/>`logs`<br/>`logs_that_burn`        | `block.minecraft.birch_log`    |
| Jungle Log   | `jungle_log`   | Block & Item | `jungle_logs`<br/>`logs`<br/>`logs_that_burn`<br/>`mineable/axe`       | `jungle_logs`<br/>`logs`<br/>`logs_that_burn`       | `block.minecraft.jungle_log`   |
| Acacia Log   | `acacia_log`   | Block & Item | `acacia_logs`<br/>`logs`<br/>`logs_that_burn`<br/>`mineable/axe`       | `acacia_logs`<br/>`logs`<br/>`logs_that_burn`       | `block.minecraft.acacia_log`   |
| Dark Oak Log | `dark_oak_log` | Block & Item | `dark_oak_logs`<br/>`logs`<br/>`logs_that_burn`<br/>`mineable/axe`     | `dark_oak_logs`<br/>`logs`<br/>`logs_that_burn`     | `block.minecraft.dark_oak_log` |
| Mangrove Log | `mangrove_log` | Block & Item | `mangrove_logs`<br/>`logs`<br/>`logs_that_burn`<br/>`mineable/axe`     | `mangrove_logs`<br/>`logs`<br/>`logs_that_burn`     | `block.minecraft.mangrove_log` |
| Cherry Log   | `cherry_log`   | Block & Item | `cherry_logs`<br/>`logs`<br/>`logs_that_burn`<br/>`mineable/axe`       | `mangrove_logs`<br/>`logs`<br/>`logs_that_burn`     | `block.minecraft.cherry_log`   |
| Crimson Stem | `crimson_stem` | Block & Item | `crimson_stems`<br/>`logs`<br/>`non_flammable_wood`<br/>`mineable/axe` | `crimson_stems`<br/>`logs`<br/>`non_flammable_wood` | `block.minecraft.crimson_stem` |
| Warped Stem  | `warped_stem`  | Block & Item | `warped_stems`<br/>`logs`<br/>`non_flammable_wood`<br/>`mineable/axe`  | `warped_stems`<br/>`logs`<br/>`non_flammable_wood`  | `block.minecraft.warped_stem`  |

Bedrock Edition:

| Name         | Identifier     | Alias ID   | Numeric ID | Form                       | Item ID[i 1]   | Item tags                                                                     | Translation key          |
|--------------|----------------|------------|------------|----------------------------|----------------|-------------------------------------------------------------------------------|--------------------------|
| Oak Log      | `oak_log`      | `log / 0`  | `17`       | Block & Giveable Item[i 2] | Identical[i 3] | `minecraft:logs`<br/>`minecraft:logs_that_burn`                               | `tile.log.oak.name`      |
| Spruce Log   | `spruce_log`   | `log / 1`  | `-569`     | Block & Giveable Item[i 2] | Identical[i 3] | `minecraft:logs`<br/>`minecraft:logs_that_burn`                               | `tile.log.spruce.name`   |
| Birch Log    | `birch_log`    | `log / 2`  | `-570`     | Block & Giveable Item[i 2] | Identical[i 3] | `minecraft:logs`<br/>`minecraft:logs_that_burn`                               | `tile.log.birch.name`    |
| Jungle Log   | `jungle_log`   | `log / 3`  | `-571`     | Block & Giveable Item[i 2] | Identical[i 3] | `minecraft:logs`<br/>`minecraft:logs_that_burn`                               | `tile.log.jungle.name`   |
| Acacia Log   | `acacia_log`   | `log2 / 0` | `162`      | Block & Giveable Item[i 2] | Identical[i 3] | `minecraft:logs`<br/>`minecraft:logs_that_burn`                               | `tile.log.acacia.name`   |
| Dark Oak Log | `dark_oak_log` | `log2 / 1` | `-572`     | Block & Giveable Item[i 2] | Identical[i 3] | `minecraft:logs`<br/>`minecraft:logs_that_burn`                               | `tile.log.big_oak.name`  |
| Mangrove Log | `mangrove_log` | None       | `-484`     | Block & Giveable Item[i 2] | Identical[i 3] | `minecraft:mangrove_logs`<br/>`minecraft:logs`<br/>`minecraft:logs_that_burn` | `tile.mangrove_log.name` |
| Cherry Log   | `cherry_log`   | None       | `-536`     | Block & Giveable Item[i 2] | Identical[i 3] | `minecraft:logs`<br/>`minecraft:logs_that_burn`                               | `tile.cherry_log.name`   |
| Crimson Stem | `crimson_stem` | None       | `-225`     | Block & Giveable Item[i 2] | Identical[i 3] | `minecraft:crimson_stems`<br/>`minecraft:logs`                                | `tile.crimson_stem.name` |
| Warped Stem  | `warped_stem`  | None       | `-226`     | Block & Giveable Item[i 2] | Identical[i 3] | `minecraft:warped_stems`<br/>`minecraft:logs`                                 | `tile.warped_stem.name`  |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑ a b c d e f g h i jAvailable with /give command.
3. ↑ a b c d e f g h i jThe block's direct item form has the same id as the block.

### Block states
See also: Block states

Java Edition:

| Name | Default value | Allowed values | Description                              |
|------|---------------|----------------|------------------------------------------|
| axis | `y`           | `x`            | The log or stem is oriented east–west.   |
|      |               | `y`            | The log or stem is oriented vertically.  |
|      |               | `z`            | The log or stem is oriented north–south. |

Bedrock Edition:

| Name        | Metadata Bits   | Default value | Allowed values | Values forMetadata Bits | Description                      |
|-------------|-----------------|---------------|----------------|-------------------------|----------------------------------|
| pillar_axis | `0x1`<br/>`0x2` | `y`           | `y`            | `0`                     | The log is oriented vertically.  |
|             |                 |               | `x`            | `1`                     | The log is oriented east–west.   |
|             |                 |               | `z`            | `2`                     | The log is oriented north–south. |




