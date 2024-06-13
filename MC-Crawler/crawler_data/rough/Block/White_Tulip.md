# Tulip
Tulips are a kind of flower found in plains and flower forests that come in multiple colored variants: red, orange, white, and pink. They yield dyes of their respective colors, with the exception of white tulips, which yield light gray dye.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Post-generation
	- 1.4 Mob loot
	- 1.5 Trading
- 2 Usage
	- 2.1 Crafting ingredient
	- 2.2 Suspicious stew
	- 2.3 Bees
	- 2.4 Breeding
	- 2.5 Bee nests
	- 2.6 Composting
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
	- 5.1 Data history
- 6 Issues
- 7 Trivia
- 8 Gallery
- 9 References

## Obtaining
### Breaking
A tulip can be broken instantly with any item or by hand, dropping itself.

A tulip also breaks if water or lava runs over its location, if a piston extends or pushes a block into its location, or if a block under the plant is moved or destroyed.

| Block    | Tulip               |
|----------|---------------------|
| Hardness | 0                   |
|          | Breakingtime (secs) |
| Default  | 0.05                |

### Natural generation
Main article: Flower § Flower gradients
Tulip/Non-tulip gradient in plains
Tulips of any color generate naturally on dirt and grass blocks in plains and sunflower plains, exclusively in rare tulip-only areas. All kinds of tulips also generate in flower forest biomes as part of the gradient. In Java Edition, tulips are also technically capable of growing in dripstone caves and deep dark biomes, though it is very unlikely due to lack of grass blocks in these biomes.

Potted red and white tulips can also be found in woodland mansions.


### Post-generation
Main article: Flower § Post-generation
When bone meal is applied to a grass block in a plains, sunflower plains, and flower forest biome (as well as dripstone caves and deep dark biomes in Java Edition), tulips have a chance of generating on the targeted block and adjacent grass blocks in a 15×5×15 area in Java Edition, or a 7×5×7 area in Bedrock Edition. In flower forests, whether a tulip can generate and the specific color depend on the flower gradient. In plains and sunflower plains (as well as dripstone cave and deep dark in Java Edition), tulips of any color can generate exclusively in tulip-only areas.

In Bedrock Edition, when bone meal is applied to a tulip that has been placed on top of a grass block in any biome, more tulips of the same color appear on top of nearby grass blocks. The flowers can appear up to 3 blocks away from the original, forming a 7×7 square.

### Mob loot
Endermen can pick up tulips, like any other one-block-tall flower, and drop one if killed while holding it.

### Trading
Wandering traders may sell a tulip of any color for a single emerald.

## Usage
Main article: Flower § Usage
Like other flowers, tulips can be used as decoration and planted on grass blocks, dirt, coarse dirt, rooted dirt, farmland, podzol, mycelium, moss blocks, mud, or muddy mangrove roots.

Tulips can also be placed inside flower pots.

### Crafting ingredient
| Name           | Ingredients  | Crafting recipe |
|----------------|--------------|-----------------|
| Light Gray Dye | White Tulip  |                 |
| Orange Dye     | Orange Tulip |                 |
| Pink Dye       | Pink Tulip   |                 |
| Red Dye        | Red Tulip    |                 |

### Suspicious stew
Main article: Suspicious Stew
Using tulips to make suspicious stew, whether by direct crafting or by feeding a brown mooshroom and then milking it with a bowl, imbues it with a Weakness effect that lasts 9 seconds in Java Edition and 7 seconds in Bedrock Edition.

| Ingredients                                              | Crafting recipe |
|----------------------------------------------------------|-----------------|
| Red Mushroom+<br/>Brown Mushroom+<br/>Bowl+<br/>AnyTulip |                 |

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

