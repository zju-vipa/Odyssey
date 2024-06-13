# Poppy
A poppy is a flower that can be crafted into red dye.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Post-generation
		- 1.3.1 Java Edition
		- 1.3.2 Bedrock Edition
	- 1.4 Mob loot
	- 1.5 Chest loot
	- 1.6 Trading
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
	- 8.1 Screenshots
- 9 References

## Obtaining
### Breaking
A poppy can be broken instantly with any item or by hand, dropping itself.

A poppy also breaks if water or lava runs over its location, if a piston extends or pushes a block into its location, or if a block under the plant is moved or destroyed.

| Block    | Poppy               |
|----------|---------------------|
| Hardness | 0                   |
|          | Breakingtime (secs) |
| Default  | 0.05                |

### Natural generation
Poppies generate naturally on dirt and grass blocks in multiple biomes as part of vegetation features. In both Java Edition and Bedrock Edition, poppies can be found in the following biomes:

- Plains
- Sunflower Plains
- Meadow
- Flower Forest

In Java Edition, poppies can also generate in many additional biomes:

- Savanna
- Savanna Plateau
- Windswept Savanna
- Snowy Plains
- Forest
- Birch Forest
- Old Growth Birch Forest
- Taiga
- Old Growth Spruce Taiga
- Old Growth Pine Taiga
- Snowy Taiga
- Jungle
- Bamboo Jungle
- Sparse Jungle
- Dark Forest
- Windswept Hills
- Windswept Gravelly Hills
- Windswept Forest
- River
- Frozen River

In Java Edition, the following additional biomes are also technically allowed to generate poppies, although they very rarely or never generate grass blocks on the surface in normal worlds. As a result, poppies can generate only in edge cases or custom worlds.

- Beach
- Snowy Beach
- Stony Shore
- Ocean
- Deep Ocean
- Cold Ocean
- Deep Cold Ocean
- Frozen Ocean
- Deep Frozen Ocean
- Lukewarm Ocean
- Deep Lukewarm Ocean
- Warm Ocean
- Desert
- Ice Spikes
- Dripstone Caves
- Deep Dark

In jungles, bamboo jungles, sparse jungles, savannas and savanna plateaus, poppies are twice as common as in other biomes. In flower forests and meadows, poppies only generate as part of gradients.

Natural poppies are found in plains, savanna, and taiga villages, as well as snowy villages in Bedrock Edition. Potted poppies can also generate in woodland mansions.


### Post-generation
Main article: Flower § Post-generation
#### Java Edition
When bone meal is applied to a grass block in one of the biomes listed above, poppies have a chance of generating on the targeted block and adjacent grass blocks in a 15×5×15 area. In meadows and flower forests, poppies can generate only in specific locations depending on the flower gradient. In plains, sunflower plains, dripstone caves, and the deep dark, poppies cannot generate in tulip-only areas.

#### Bedrock Edition
When bone meal is applied to a grass block in plains, sunflower plains, and flower forest, poppies have a chance of generating on the targeted block and adjacent grass blocks in a 7×5×7 area. In flower forests, poppies can generate only in specific locations depending on the flower gradient. In plains and sunflower plains, poppies cannot generate in tulip-only areas.

When bone meal is applied to a poppy that has been placed on top of a grass block in any biome, more poppies appear on top of nearby grass blocks. Dandelions can also occasionally appear, and poppies can occasionally appear when bone meal is applied to dandelions. The flowers can appear up to 3 blocks away from the original, forming a 7×7 square.

### Mob loot
Iron golems drop 0 to 2 poppies upon death. This is unaffected by the Looting enchantment.

Endermen can pick up poppies, like any other one-block-tall flower, and drop one if killed while holding it.

In Java Edition, baby villagers may give a poppy to players with the Hero of the Village effect.

| Source | Roll Chance | Quantity (Roll Chance) |           |            |             |
|--------|-------------|------------------------|-----------|------------|-------------|
|        |             | Default                | Looting I | Looting II | Looting III |

### Chest loot
| Item  | Structure | Container          | Quantity | Chance                         |
|-------|-----------|--------------------|----------|--------------------------------|
|       |           |                    |          | Java EditionandBedrock Edition |
| Poppy | Village   | Plains house chest | 1        | 12.1%                          |

### Trading
Wandering traders may sell a poppy for a single emerald.

## Usage
Main article: Flower § Usage
Like other flowers, poppies can be used as decoration and planted on grass blocks, dirt, coarse dirt, rooted dirt, farmland, podzol, mycelium, moss blocks, mud, or muddy mangrove roots.

Poppies can also be placed in flower pots.

### Crafting ingredient
| Name    | Ingredients | Crafting recipe |
|---------|-------------|-----------------|
| Red Dye | Poppy       |                 |

### Suspicious stew
Main article: Suspicious Stew
Using a poppy to make suspicious stew, whether by direct crafting or by feeding a brown mooshroom and then milking it with a bowl, imbues it with a Night Vision effect that lasts 8 seconds in Java Edition and 6 seconds in Bedrock Edition.

| Ingredients                                           | Crafting recipe |
|-------------------------------------------------------|-----------------|
| Red Mushroom+<br/>Brown Mushroom+<br/>Bowl+<br/>Poppy |                 |

### Bees
Bees engage in a pollinating behavior with poppies, increasing the honey level in beehives and bee nests by 1.

### Breeding
Poppies can be used to breed, grow, and lead bees.

### Bee nests
Oak, birch, and cherry trees grown from saplings that are within 2 blocks of a poppy have a 5% chance to grow with a bee nest and 1-3 bees in it.

### Composting
Placing a poppy into a composter has a 65% chance of raising the compost level by 1. A stack of poppies yields an average of 5.94 bone meal.

## Data values
### ID
Java Edition:

| Name  | Identifier | Form         | Block tags                    | Item tags                     | Translation key         |
|-------|------------|--------------|-------------------------------|-------------------------------|-------------------------|
| Poppy | `poppy`    | Block & Item | `flowers`<br/>`small_flowers` | `flowers`<br/>`small_flowers` | `block.minecraft.poppy` |

Bedrock Edition:

| Name  | Identifier                      | Alias ID         | Numeric ID | Form                       | Item ID[i 1]   | Translation key              |
|-------|---------------------------------|------------------|------------|----------------------------|----------------|------------------------------|
| Poppy | `red_flower‌[until BE 1.20.80]` | None             | `38`       | Block & Giveable Item[i 2] | Identical[i 3] | `tile.red_flower.poppy.name` |
| Poppy | `poppy‌[upcoming: BE 1.20.80]`  | `red_flower / 0` | `38`       | Block & Giveable Item[i 2] | Identical[i 3] | `tile.red_flower.poppy.name` |

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

