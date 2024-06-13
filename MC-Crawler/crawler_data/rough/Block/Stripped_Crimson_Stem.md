# Stripped Log
A stripped log or stripped stem is a variant of the log and stem, obtained by using an axe on a log or a stem respectively. Once stripped, it cannot be reversed.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
		- 1.2.1 Structures
	- 1.3 Post-generation
- 2 Usage
	- 2.1 Crafting ingredient
	- 2.2 Smelting ingredient
	- 2.3 Fuel
	- 2.4 Cocoa beans
	- 2.5 Note blocks
- 3 Sounds
	- 3.1 Other logs
	- 3.2 Cherry log
	- 3.3 Stems
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 Gallery
	- 7.1 Renders
	- 7.2 Screenshots
	- 7.3 Development images
- 8 References

## Obtaining
### Breaking
Stripped logs and stems can be broken by hand, but using an axe speeds up the process. Stripped logs and stems drop themselves when broken with any tool.

| Block     | Stripped LogStripped Stem |
|-----------|---------------------------|
| Hardness  | 2                         |
| Tool      |                           |
|           | Breakingtime (sec)[A]     |
| Default   | 3                         |
| Wooden    | 1.5                       |
| Stone     | 0.75                      |
| Iron      | 0.5                       |
| Diamond   | 0.4                       |
| Netherite | 0.35                      |
| Golden    | 0.25                      |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Natural generation
#### Structures
** Oak **
- Stripped oak logs generate in plains villages.

** Spruce **
- Stripped spruce logs generate in snowy plains villages.

** Acacia **
- Stripped acacia logs generate as part of houses in savanna villages.

** Mixed **
- Stripped oak, spruce, jungle and dark oak logs can generate as masts in shipwrecks.‌[Bedrock Edition  only]

### Post-generation
Using an axe on a log or stem turns it into a stripped log or a stripped stem, which act the same as regular logs.

## Usage
### Crafting ingredient
| Name                                                                                                                                                                                                                                                           | Ingredients                                                 | Crafting recipe |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|-----------------|
| Campfire                                                                                                                                                                                                                                                       | Stick+<br/>Coal+<br/>AnyStripped LogorStem                  |                 |
| Campfire                                                                                                                                                                                                                                                       | Stick+<br/>Charcoal+<br/>AnyStripped LogorStem              |                 |
| Nether Planks                                                                                                                                                                                                                                                  | MatchingStripped Stem                                       | 44              |
| Oak Hanging Signor<br/>Spruce Hanging Signor<br/>Birch Hanging Signor<br/>Jungle Hanging Signor<br/>Acacia Hanging Signor<br/>Dark Oak Hanging Signor<br/>Mangrove Hanging Signor<br/>Cherry Hanging Signor<br/>Crimson Hanging Signor<br/>Warped Hanging Sign | Chain+<br/>MatchingStripped Logor<br/>MatchingStripped Stem | 6666666666      |
| Oak Planksor<br/>Spruce Planksor<br/>Birch Planksor<br/>Jungle Planksor<br/>Acacia Planksor<br/>Dark Oak Planksor<br/>Mangrove Planksor<br/>Cherry Planks                                                                                                      | MatchingStripped Log                                        | 44444444        |
| Smoker                                                                                                                                                                                                                                                         | AnyStripped LogorStem+<br/>Furnace                          |                 |
| Soul Campfire                                                                                                                                                                                                                                                  | Stick+<br/>Soul Soil+<br/>AnyStripped LogorStem             |                 |
| Soul Campfire                                                                                                                                                                                                                                                  | Stick+<br/>Soul Sand+<br/>AnyStripped LogorStem             |                 |
| Stripped Woodor<br/>Stripped Hyphae                                                                                                                                                                                                                            | MatchingStripped Logor<br/>MatchingStripped Stem            | 3333333333      |

### Smelting ingredient
| Name     | Ingredients                                                                                                                                                                                                            | Smelting recipe |
|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| Charcoal | Stripped Oak Logor<br/>Stripped Spruce Logor<br/>Stripped Birch Logor<br/>Stripped Jungle Logor<br/>Stripped Acacia Logor<br/>Stripped Dark Oak Logor<br/>Stripped Mangrove Logor<br/>Stripped Cherry Log+<br/>Anyfuel | 0.15            |

### Fuel
Stripped logs (but not stripped stems) can be used as fuel in furnaces, smelting 1.5 items per block.

### Cocoa beans
Cocoa beans can be placed on the side of stripped jungle logs to grow a new cocoa pod.

### Note blocks
Stripped logs and stems can be placed under note blocks to produce "bass" sounds.

## Data values
Note that when a stripped log or stem is placed, it changes its facing parameters, placing in the direction relative to the block it is placed on.

Stripped logs and stems consider only the axis; a sideways stripped log or stem placed while facing north does not have a top texture rotated 180 degrees from a stripped log or stem placed south.[1]

### ID
Java Edition:

| Name                  | Identifier              | Form         | Block tags                                                                                 | Item tags                                                               | Translation key                         |
|-----------------------|-------------------------|--------------|--------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|-----------------------------------------|
| Stripped Oak Log      | `stripped_oak_log`      | Block & Item | `logs`<br/>`logs_that_burn`<br/>`oak_logs`<br/>`mineable/axe`<br/>`stripped_logs`          | `logs`<br/>`logs_that_burn`<br/>`oak_logs`<br/>`stripped_logs`          | `block.minecraft.stripped_oak_log`      |
| Stripped Spruce Log   | `stripped_spruce_log`   | Block & Item | `logs`<br/>`logs_that_burn`<br/>`spruce_logs`<br/>`mineable/axe`<br/>`stripped_logs`       | `logs`<br/>`logs_that_burn`<br/>`spruce_logs`<br/>`stripped_logs`       | `block.minecraft.stripped_spruce_log`   |
| Stripped Birch Log    | `stripped_birch_log`    | Block & Item | `birch_logs`<br/>`logs`<br/>`logs_that_burn`<br/>`mineable/axe`<br/>`stripped_logs`        | `birch_logs`<br/>`logs`<br/>`logs_that_burn`<br/>`stripped_logs`        | `block.minecraft.stripped_birch_log`    |
| Stripped Jungle Log   | `stripped_jungle_log`   | Block & Item | `jungle_logs`<br/>`logs`<br/>`logs_that_burn`<br/>`mineable/axe`<br/>`stripped_logs`       | `jungle_logs`<br/>`logs`<br/>`logs_that_burn`<br/>`stripped_logs`       | `block.minecraft.stripped_jungle_log`   |
| Stripped Acacia Log   | `stripped_acacia_log`   | Block & Item | `acacia_logs`<br/>`logs`<br/>`logs_that_burn`<br/>`mineable/axe`<br/>`stripped_logs`       | `acacia_logs`<br/>`logs`<br/>`logs_that_burn`<br/>`stripped_logs`       | `block.minecraft.stripped_acacia_log`   |
| Stripped Dark Oak Log | `stripped_dark_oak_log` | Block & Item | `dark_oak_logs`<br/>`logs`<br/>`logs_that_burn`<br/>`mineable/axe`<br/>`stripped_logs`     | `dark_oak_logs`<br/>`logs`<br/>`logs_that_burn`<br/>`stripped_logs`     | `block.minecraft.stripped_dark_oak_log` |
| Stripped Mangrove Log | `stripped_mangrove_log` | Block & Item | `mangrove_logs`<br/>`logs`<br/>`logs_that_burn`<br/>`mineable/axe`<br/>`stripped_logs`     | `mangrove_logs`<br/>`logs`<br/>`logs_that_burn`<br/>`stripped_logs`     | `block.minecraft.stripped_mangrove_log` |
| Stripped Cherry Log   | `stripped_cherry_log`   | Block & Item | `cherry_logs`<br/>`logs`<br/>`logs_that_burn`<br/>`mineable/axe`<br/>`stripped_logs`       | `cherry_logs`<br/>`logs`<br/>`logs_that_burn`<br/>`stripped_logs`       | `block.minecraft.stripped_cherry_log`   |
| Stripped Crimson Stem | `stripped_crimson_stem` | Block & Item | `crimson_stems`<br/>`logs`<br/>`non_flammable_wood`<br/>`mineable/axe`<br/>`stripped_logs` | `crimson_stems`<br/>`logs`<br/>`non_flammable_wood`<br/>`stripped_logs` | `block.minecraft.stripped_crimson_stem` |
| Stripped Warped Stem  | `stripped_warped_stem`  | Block & Item | `warped_stems`<br/>`logs`<br/>`non_flammable_wood`<br/>`mineable/axe`<br/>`stripped_logs`  | `warped_stems`<br/>`logs`<br/>`non_flammable_wood`<br/>`stripped_logs`  | `block.minecraft.stripped_warped_stem`  |

Bedrock Edition:

| Name                  | Identifier              | Numeric ID | Form                       | Item ID[i 1]   | Item tags                                                                     | Translation key                   |
|-----------------------|-------------------------|------------|----------------------------|----------------|-------------------------------------------------------------------------------|-----------------------------------|
| Stripped Oak Log      | `stripped_oak_log`      | `-10`      | Block & Giveable Item[i 2] | Identical[i 3] | `minecraft:logs`<br/>`minecraft:logs_that_burn`                               | `tile.stripped_oak_log.name`      |
| Stripped Spruce Log   | `stripped_spruce_log`   | `-5`       | Block & Giveable Item[i 2] | Identical[i 3] | `minecraft:logs`<br/>`minecraft:logs_that_burn`                               | `tile.stripped_spruce_log.name`   |
| Stripped Birch Log    | `stripped_birch_log`    | `-6`       | Block & Giveable Item[i 2] | Identical[i 3] | `minecraft:logs`<br/>`minecraft:logs_that_burn`                               | `tile.stripped_birch_log.name`    |
| Stripped Jungle Log   | `stripped_jungle_log`   | `-7`       | Block & Giveable Item[i 2] | Identical[i 3] | `minecraft:logs`<br/>`minecraft:logs_that_burn`                               | `tile.stripped_jungle_log.name`   |
| Stripped Acacia Log   | `stripped_acacia_log`   | `-8`       | Block & Giveable Item[i 2] | Identical[i 3] | `minecraft:logs`<br/>`minecraft:logs_that_burn`                               | `tile.stripped_acacia_log.name`   |
| Stripped Dark Oak Log | `stripped_dark_oak_log` | `-9`       | Block & Giveable Item[i 2] | Identical[i 3] | `minecraft:logs`<br/>`minecraft:logs_that_burn`                               | `tile.stripped_dark_oak_log.name` |
| Stripped Mangrove Log | `stripped_mangrove_log` | `-485`     | Block & Giveable Item[i 2] | Identical[i 3] | `minecraft:mangrove_logs`<br/>`minecraft:logs`<br/>`minecraft:logs_that_burn` | `tile.stripped_mangrove_log.name` |
| Stripped Cherry Log   | `stripped_cherry_log`   | `-535`     | Block & Giveable Item[i 2] | Identical[i 3] | `minecraft:logs`<br/>`minecraft:logs_that_burn`                               | `tile.stripped_cherry_log.name`   |
| Stripped Crimson Stem | `stripped_crimson_stem` | `-240`     | Block & Giveable Item[i 2] | Identical[i 3] | `minecraft:crimson_stems`<br/>`minecraft:logs`                                | `tile.stripped_crimson_stem.name` |
| Stripped Warped Stem  | `stripped_warped_stem`  | `-241`     | Block & Giveable Item[i 2] | Identical[i 3] | `minecraft:warped_stems`<br/>`minecraft:logs`                                 | `tile.stripped_warped_stem.name`  |

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



