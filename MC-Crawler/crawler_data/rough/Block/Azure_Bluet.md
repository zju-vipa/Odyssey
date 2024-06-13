# Azure Bluet
An azure bluet is a flower that can be crafted into light gray dye.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Post-generation
		- 1.3.1 Java Edition
		- 1.3.2 Bedrock Edition
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
- 8 References

## Obtaining
### Breaking
An azure bluet can be broken instantly with any item or by hand, dropping itself.

An azure bluet also breaks if water or lava runs over its location, if a piston extends or pushes a block into its location, or if a block under the plant is moved or destroyed.

| Block    | Azure Bluet         |
|----------|---------------------|
| Hardness | 0                   |
|          | Breakingtime (secs) |
| Default  | 0.05                |

### Natural generation
Azure bluets generate naturally on dirt and grass blocks in plains, sunflower plains, flower forest and meadow biomes as part of vegetation features. In Java Edition, they are also technically capable of growing in dripstone caves and deep dark biomes, though it is very unlikely due to lack of grass blocks in these biomes. In flower forests and meadows, azure bluets only generate as part of gradients. 

Natural azure bluets are found in plains villages. Potted azure bluets can also be generated in woodland mansions.


### Post-generation
Main article: Flower § Post-generation
#### Java Edition
When bone meal is applied to a grass block in a plains, sunflower plains, flower forest, meadow, dripstone caves, or deep dark biome, azure bluets have a chance of generating on the targeted block and adjacent grass blocks in a 15×5×15 area. In meadows and flower forests, azure bluets can generate only in specific locations depending on the flower gradient. In plains, sunflower plains, dripstone caves, and the deep dark, azure bluets cannot generate in tulip-only areas.

#### Bedrock Edition
When bone meal is applied to a grass block in a plains, sunflower plains, or flower forest biome, azure bluets have a chance of generating on the targeted block and adjacent grass blocks in a 7×5×7 area. In flower forests, azure bluets can generate only in specific locations depending on the flower gradient. In plains and sunflower plains, azure bluets cannot generate in tulip-only areas.

When bone meal is applied to an azure bluet that has been placed on top of a grass block in any biome, more azure bluets appear on top of nearby grass blocks. The flowers can appear up to 3 blocks away from the original, forming a 7×7 square.

### Mob loot
Endermen can pick up azure bluets, like any other one-block-tall flower, and drop one if killed while holding it.

### Trading
Wandering traders may sell an azure bluet for a single emerald.

## Usage
Main article: Flower § Usage
Like other flowers, azure bluets can be used as decoration and planted on grass blocks, dirt, coarse dirt, rooted dirt, farmland, podzol, mycelium, moss blocks, mud, or muddy mangrove roots.

Azure bluets can also be placed in flower pots.

### Crafting ingredient
| Name           | Ingredients | Crafting recipe |
|----------------|-------------|-----------------|
| Light Gray Dye | Azure Bluet |                 |

### Suspicious stew
Main article: Suspicious Stew
Using an azure bluet to make suspicious stew, whether by direct crafting or by feeding a brown mooshroom and then milking it with a bowl, imbues it with a Blindness effect that lasts 8 seconds in Java Edition and 6 seconds in Bedrock Edition.

| Ingredients                                                 | Crafting recipe |
|-------------------------------------------------------------|-----------------|
| Red Mushroom+<br/>Brown Mushroom+<br/>Bowl+<br/>Azure Bluet |                 |

### Bees
Bees engage in a pollinating behavior with azure bluets, increasing the honey level in beehives and bee nests by 1.

### Breeding
Azure bluets can be used to breed, grow, and lead bees.

### Bee nests
Oak, birch, and cherry trees grown from saplings that are within 2 blocks of an azure bluet have a 5% chance to grow with a bee nest and 1-3 bees in it.

### Composting
Placing an azure bluet into a composter has a 65% chance of raising the compost level by 1. A stack of azure bluets yields an average of 5.94 bone meal.

## Data values
### ID
Java Edition:

| Name        | Identifier    | Form         | Block tags                    | Item tags                     | Translation key               |
|-------------|---------------|--------------|-------------------------------|-------------------------------|-------------------------------|
| Azure Bluet | `azure_bluet` | Block & Item | `flowers`<br/>`small_flowers` | `flowers`<br/>`small_flowers` | `block.minecraft.azure_bluet` |

Bedrock Edition:

| Name        | Identifier                           | Alias ID         | Numeric ID | Form                       | Item ID[i 1]   | Translation key                  |
|-------------|--------------------------------------|------------------|------------|----------------------------|----------------|----------------------------------|
| Azure Bluet | `red_flower‌[until BE 1.20.80]`      | None             | `38`       | Block & Giveable Item[i 2] | Identical[i 3] | `tile.red_flower.houstonia.name` |
| Azure Bluet | `azure_bluet‌[upcoming: BE 1.20.80]` | `red_flower / 3` | `-832`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.red_flower.houstonia.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑ a bAvailable with /give command.
3. ↑ a bThe block's direct item form has the same id as the block.

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

