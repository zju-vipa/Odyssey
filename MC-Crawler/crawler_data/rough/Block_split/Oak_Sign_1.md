### Interaction
Signs can be edited after being placed by using them, which opens the edit sign message GUI.

Signs are destroyed and drop as an item when pushed by a piston.‌[Bedrock Edition  only]

Signs are non-solid and have no collision, so items and mobs can move through sign blocks. Other blocks (including other signs) can be placed on any edge of a sign.

Water and lava flow around signs. Lava can create fire in air blocks next to signs as if the signs were flammable, but the signs do not burn (and cannot be burned by other methods either, except in Bedrock Edition).

### Fuel
Overworld signs can be used as a fuel in furnaces, smelting an item per sign. Nether signs (crimson and warped), cannot be used as fuel in a furnace.

### Note blocks
Signs can be placed under note blocks to produce a "bass" sound.

## Data values
### ID
Java Edition:

| Name               | Identifier           | Form         | Block tags                                            | Item tags                        | Translation key                      |
|--------------------|----------------------|--------------|-------------------------------------------------------|----------------------------------|--------------------------------------|
| Oak Sign           | `oak_sign`           | Block & Item | `signs`<br/>`standing_signs`<br/>`wall_post_override` | `signs`                          | `block.minecraft.oak_sign`           |
| Spruce Sign        | `spruce_sign`        | Block & Item | `signs`<br/>`standing_signs`<br/>`wall_post_override` | `signs`                          | `block.minecraft.spruce_sign`        |
| Birch Sign         | `birch_sign`         | Block & Item | `signs`<br/>`standing_signs`<br/>`wall_post_override` | `signs`                          | `block.minecraft.birch_sign`         |
| Jungle Sign        | `jungle_sign`        | Block & Item | `signs`<br/>`standing_signs`<br/>`wall_post_override` | `signs`                          | `block.minecraft.jungle_sign`        |
| Acacia Sign        | `acacia_sign`        | Block & Item | `signs`<br/>`standing_signs`<br/>`wall_post_override` | `signs`                          | `block.minecraft.acacia_sign`        |
| Dark Oak Sign      | `dark_oak_sign`      | Block & Item | `signs`<br/>`standing_signs`<br/>`wall_post_override` | `signs`                          | `block.minecraft.dark_oak_sign`      |
| Mangrove Sign      | `mangrove_sign`      | Block & Item | `signs`<br/>`standing_signs`<br/>`wall_post_override` | `signs`                          | `block.minecraft.mangrove_sign`      |
| Cherry Sign        | `cherry_sign`        | Block & Item | `signs`<br/>`standing_signs`<br/>`wall_post_override` | `signs`                          | `block.minecraft.cherry_sign`        |
| Bamboo Sign        | `bamboo_sign`        | Block & Item | `signs`<br/>`standing_signs`<br/>`wall_post_override` | `signs`                          | `block.minecraft.bamboo_sign`        |
| Crimson Sign       | `crimson_sign`       | Block & Item | `signs`<br/>`standing_signs`<br/>`wall_post_override` | `non_flammable_wood`<br/>`signs` | `block.minecraft.crimson_sign`       |
| Warped Sign        | `warped_sign`        | Block & Item | `signs`<br/>`standing_signs`<br/>`wall_post_override` | `non_flammable_wood`<br/>`signs` | `block.minecraft.warped_sign`        |
| Oak Wall Sign      | `oak_wall_sign`      | Block        | `signs`<br/>`wall_signs`                              | —                                | `block.minecraft.oak_wall_sign`      |
| Spruce Wall Sign   | `spruce_wall_sign`   | Block        | `signs`<br/>`wall_signs`                              | —                                | `block.minecraft.spruce_wall_sign`   |
| Birch Wall Sign    | `birch_wall_sign`    | Block        | `signs`<br/>`wall_signs`                              | —                                | `block.minecraft.birch_wall_sign`    |
| Jungle Wall Sign   | `jungle_wall_sign`   | Block        | `signs`<br/>`wall_signs`                              | —                                | `block.minecraft.jungle_wall_sign`   |
| Acacia Wall Sign   | `acacia_wall_sign`   | Block        | `signs`<br/>`wall_signs`                              | —                                | `block.minecraft.acacia_wall_sign`   |
| Dark Oak Wall Sign | `dark_oak_wall_sign` | Block        | `signs`<br/>`wall_signs`                              | —                                | `block.minecraft.dark_oak_wall_sign` |
| Mangrove Wall Sign | `mangrove_wall_sign` | Block        | `signs`<br/>`wall_signs`                              | —                                | `block.minecraft.mangrove_wall_sign` |
| Cherry Wall Sign   | `cherry_wall_sign`   | Block        | `signs`<br/>`wall_signs`                              | —                                | `block.minecraft.cherry_wall_sign`   |
| Bamboo Wall Sign   | `bamboo_wall_sign`   | Block        | `signs`<br/>`wall_signs`                              | —                                | `block.minecraft.bamboo_wall_sign`   |
| Crimson Wall Sign  | `crimson_wall_sign`  | Block        | `signs`<br/>`wall_signs`                              | —                                | `block.minecraft.crimson_wall_sign`  |
| Warped Wall Sign   | `warped_wall_sign`   | Block        | `signs`<br/>`wall_signs`                              | —                                | `block.minecraft.warped_wall_sign`   |

| Name         | Identifier |
|--------------|------------|
| Block entity | `sign`     |

Bedrock Edition:

| Sign              | Identifier               | Alias ID       | Numeric ID | Form                         | Item ID[i 1]   | Item tags        | Translation key                   |
|-------------------|--------------------------|----------------|------------|------------------------------|----------------|------------------|-----------------------------------|
| Oak standing      | `standing_sign`          | None           | `63`       | Block & Ungiveable Item[i 2] | Identical[i 3] | —                | `tile.standing_sign.name`         |
| Spruce standing   | `spruce_standing_sign`   | None           | `436`      | Block & Ungiveable Item[i 2] | Identical[i 3] | —                | `tile.spruce_standing_sign.name`  |
| Birch standing    | `birch_standing_sign`    | None           | `441`      | Block & Ungiveable Item[i 2] | Identical[i 3] | —                | `tile.birch_standing_sign.name`   |
| Jungle standing   | `jungle_standing_sign`   | None           | `443`      | Block & Ungiveable Item[i 2] | Identical[i 3] | —                | `tile.jungle_standing_sign.name`  |
| Acacia standing   | `acacia_standing_sign`   | None           | `445`      | Block & Ungiveable Item[i 2] | Identical[i 3] | —                | `tile.acacia_standing_sign.name`  |
| Dark Oak standing | `darkoak_standing_sign`  | None           | `447`      | Block & Ungiveable Item[i 2] | Identical[i 3] | —                | `tile.darkoak_standing_sign.name` |
| Mangrove standing | `mangrove_standing_sign` | None           | `-494`     | Block & Ungiveable Item[i 2] | Identical[i 3] | —                | —                                 |
| Cherry standing   | `cherry_standing_sign`   | None           | `-542`     | Block & Ungiveable Item[i 2] | Identical[i 3] | —                | —                                 |
| Bamboo standing   | `bamboo_standing_sign`   | None           | `-518`     | Block & Ungiveable Item[i 2] | Identical[i 3] | —                | —                                 |
| Crimson standing  | `crimson_standing_sign`  | None           | `505`      | Block & Ungiveable Item[i 2] | Identical[i 3] | —                | `tile.crimson_standing_sign.name` |
| Warped standing   | `warped_standing_sign`   | None           | `506`      | Block & Ungiveable Item[i 2] | Identical[i 3] | —                | `tile.warped_standing_sign.name`  |
| Oak wall          | `wall_sign`              | None           | `68`       | Block & Ungiveable Item[i 2] | Identical[i 3] | —                | —                                 |
| Spruce wall       | `spruce_wall_sign`       | None           | `437`      | Block & Ungiveable Item[i 2] | Identical[i 3] | —                | —                                 |
| Birch wall        | `birch_wall_sign`        | None           | `442`      | Block & Ungiveable Item[i 2] | Identical[i 3] | —                | —                                 |
| Jungle wall       | `jungle_wall_sign`       | None           | `444`      | Block & Ungiveable Item[i 2] | Identical[i 3] | —                | —                                 |
| Acacia wall       | `acacia_wall_sign`       | None           | `446`      | Block & Ungiveable Item[i 2] | Identical[i 3] | —                | —                                 |
| Dark Oak wall     | `darkoak_wall_sign`      | None           | `448`      | Block & Ungiveable Item[i 2] | Identical[i 3] | —                | —                                 |
| Mangrove wall     | `mangrove_wall_sign`     | None           | `-495`     | Block & Ungiveable Item[i 2] | Identical[i 3] | —                | —                                 |
| Cherry wall       | `cherry_wall_sign`       | None           | `-544`     | Block & Ungiveable Item[i 2] | Identical[i 3] | —                | —                                 |
| Bamboo wall       | `bamboo_wall_sign`       | None           | `-519`     | Block & Ungiveable Item[i 2] | Identical[i 3] | —                | —                                 |
| Crimson wall      | `crimson_wall_sign`      | None           | `507`      | Block & Ungiveable Item[i 2] | Identical[i 3] | —                | `tile.crimson_wall_sign.name`     |
| Warped wall       | `warped_wall_sign`       | None           | `508`      | Block & Ungiveable Item[i 2] | Identical[i 3] | —                | `tile.warped_wall_sign.name`      |
| Oak item          | `oak_sign`               | `sign`         | `360`      | Item                         | —              | `minecraft:sign` | `item.sign.name`                  |
| Spruce item       | `spruce_sign`            | None           | `576`      | Item                         | —              | `minecraft:sign` | `item.spruce_sign.name`           |
| Birch item        | `birch_sign`             | None           | `577`      | Item                         | —              | `minecraft:sign` | `item.birch_sign.name`            |
| Jungle item       | `jungle_sign`            | None           | `578`      | Item                         | —              | `minecraft:sign` | `item.jungle_sign.name`           |
| Acacia item       | `acacia_sign`            | None           | `579`      | Item                         | —              | `minecraft:sign` | `item.acacia_sign.name`           |
| Dark Oak item     | `dark_oak_sign`          | `darkoak_sign` | `587`      | Item                         | —              | `minecraft:sign` | `item.darkoak_sign.name`          |
| Mangrove item     | `mangrove_sign`          | None           | `642`      | Item                         | —              | `minecraft:sign` | `item.mangrove_sign.name`         |
| Cherry item       | `cherry_sign`            | None           | `659`      | Item                         | —              | `minecraft:sign` | `item.cherry_sign.name`           |
| Bamboo item       | `bamboo_sign`            | None           | `660`      | Item                         | —              | `minecraft:sign` | `item.bamboo_sign.name`           |
| Crimson item      | `crimson_sign`           | None           | `614`      | Item                         | —              | `minecraft:sign` | `item.crimson_sign.name`          |
| Warped item       | `warped_sign`            | None           | `615`      | Item                         | —              | `minecraft:sign` | `item.warped_sign.name`           |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑ a b c d e f g h i j k l m n o p q r s t u vUnavailable with /give command
3. ↑ a b c d e f g h i j k l m n o p q r s t u vThe block's direct item form has the same id as the block.

| Name         | Savegame ID |
|--------------|-------------|
| Block entity | `Sign`      |

