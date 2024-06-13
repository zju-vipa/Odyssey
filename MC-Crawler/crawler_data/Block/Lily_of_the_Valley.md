# Lily of the Valley
A lily of the valley is a flower that can be crafted into white dye.

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
- 6 Issues
- 7 References

## Obtaining
### Breaking
A lily of the valley can be broken instantly with any item or by hand, dropping itself.

A lily of the valley also breaks if water or lava runs over its location, if a piston extends or pushes a block into its location, or if a block under the plant is moved or destroyed.

| Block    | Lily of the Valley  |
|----------|---------------------|
| Hardness | 0                   |
|          | Breakingtime (secs) |
| Default  | 0.05                |

### Natural generation
Lilies of the valley generate naturally on dirt and grass blocks in forest, flower forest, birch forest, old growth birch forest, and dark forest biomes as part of vegetation features. In flower forests, they generate both in random patches and as part of the flower gradient in Java Edition, and only as part of the gradient in Bedrock Edition.


### Post-generation
Main article: Flower § Post-generation
#### Java Edition
When bone meal is applied to a grass block in a flower forest biome, lilies of the valley have a chance of generating on the targeted block and adjacent grass blocks in a 15×5×15 area, depending entirely on the flower gradient. Lilies of the valley cannot be regrown in areas where they generated naturally as part of a random patch,[1] as well as in other biomes where it generates naturally.[2]

#### Bedrock Edition
When bone meal is applied to a grass block in a forest, flower forest, birch forest, old growth birch forest, or dark forest biome, lilies of the valley have a chance of generating on the targeted block and adjacent grass blocks in a 7×5×7 area. In flower forests, lilies of the valley can generate only in specific locations depending on the flower gradient.

When bone meal is applied to a lily of the valley that has been placed on top of a grass block in any biome, more lilies of the valley appear on top of nearby grass blocks. The flowers can appear up to 3 blocks away from the original, forming a 7×7 square.

### Mob loot
Endermen can pick up lilies of the valley, like any other one-block-tall flower, and drop one if killed while holding it.

### Trading
Wandering traders may sell a lily of the valley for a single emerald.

## Usage
Main article: Flower § Usage
Like other flowers, lilies of the valley can be used as decoration and planted on grass blocks, dirt, coarse dirt, rooted dirt, farmland, podzol, mycelium, moss blocks, mud, or muddy mangrove roots.

Lilies of the valley can also be placed in flower pots.

### Crafting ingredient
| Name      | Ingredients        | Crafting recipe |
|-----------|--------------------|-----------------|
| White Dye | Lily of the Valley |                 |

### Suspicious stew
Main article: Suspicious Stew
Using a lily of the valley to make suspicious stew, whether by direct crafting or by feeding a brown mooshroom and then milking it with a bowl, imbues it with a Poison effect that lasts 12 seconds in Java Edition and 10 seconds in Bedrock Edition. The Poison effect deals 9 in Java Edition or 8 in Bedrock Edition.

| Ingredients                                         | Crafting recipe |
|-----------------------------------------------------|-----------------|
| Red Mushroom+Brown Mushroom+Bowl+Lily of the Valley |                 |

### Bees
Bees engage in a pollinating behavior with lilies of the valley, increasing the honey level in beehives and bee nests by 1.

### Breeding
Lilies of the valley can be used to breed, grow, and lead bees.

### Bee nests
Oak, birch, and cherry trees grown from saplings that are within 2 blocks of a lily of the valley have a 5% chance to grow with a bee nest and 1-3 bees in it.

### Composting
Placing a lily of the valley into a composter has a 65% chance of raising the compost level by 1. A stack of lilies of the valley yields an average of 5.94 bone meal.

## Data values
### ID
Java Edition:

| Name               | Identifier         | Form         | Block tags           | Item tags            | Translation key                    |
|--------------------|--------------------|--------------|----------------------|----------------------|------------------------------------|
| Lily of the Valley | lily_of_the_valley | Block & Item | flowerssmall_flowers | flowerssmall_flowers | block.minecraft.lily_of_the_valley |

Bedrock Edition:

| Name               | Identifier                                | Alias ID        | Numeric ID | Form                       | Item ID[i 1]   | Translation key                      |
|--------------------|-------------------------------------------|-----------------|------------|----------------------------|----------------|--------------------------------------|
| Lily of the Valley | red_flower‌[until BE 1.20.80]             | None            | 38         | Block & Giveable Item[i 2] | Identical[i 3] | tile.red_flower.lilyOfTheValley.name |
| Lily of the Valley | lily_of_the_valley‌[upcoming: BE 1.20.80] | red_flower / 10 | -839       | Block & Giveable Item[i 2] | Identical[i 3] | tile.red_flower.lilyOfTheValley.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ a b Available with /give command.

↑ a b The block's direct item form has the same id as the block.


### Block states
See also: Block states

Bedrock Edition:

| Name        | Metadata Bits | Default value | Allowed values     | Values forMetadata Bits | Description        |
|-------------|---------------|---------------|--------------------|-------------------------|--------------------|
| flower_type | 0x10x20x40x8  | poppy         | poppy              | 0                       | Poppy              |
|             |               |               | orchid             | 1                       | Blue Orchid        |
|             |               |               | allium             | 2                       | Allium             |
|             |               |               | houstonia          | 3                       | Azure Bluet        |
|             |               |               | tulip_red          | 4                       | Red Tulip          |
|             |               |               | tulip_orange       | 5                       | Orange Tulip       |
|             |               |               | tulip_white        | 6                       | White Tulip        |
|             |               |               | tulip_pink         | 7                       | Pink Tulip         |
|             |               |               | oxeye              | 8                       | Oxeye Daisy        |
|             |               |               | cornflower         | 9                       | Cornflower         |
|             |               |               | lily_of_the_valley | 10                      | Lily of the Valley |

