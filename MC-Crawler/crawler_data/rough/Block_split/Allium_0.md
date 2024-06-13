# Allium
An allium is a flower that can be crafted into magenta dye.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Post-generation
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
- 8 References

## Obtaining
### Breaking
An allium can be broken instantly with any item or by hand, dropping itself.

An allium also breaks if water or lava runs over its location, if a piston extends or pushes a block into its location, or if a block under the plant is moved or destroyed.

| Block    | Allium              |
|----------|---------------------|
| Hardness | 0                   |
|          | Breakingtime (secs) |
| Default  | 0.05                |

### Natural generation
Alliums generate naturally on dirt and grass blocks in flower forest and meadow biomes as part of gradients.

Potted alliums can also be found in woodland mansions.


### Post-generation
Main article: Flower § Post-generation
When bone meal is applied to a grass block in a flower forest, and a meadow in Java Edition, alliums have a chance of generating on the targeted block and adjacent grass blocks in a 15×5×15 area in Java Edition, or a 7×5×7 area in Bedrock Edition. Whether alliums can generate depends on the flower gradients.

In Bedrock Edition, when bone meal is applied to an allium that has been placed on top of a grass block in any biome, more alliums appear on top of nearby grass blocks. The flowers can appear up to 3 blocks away from the original, forming a 7×7 square.

### Mob loot
Endermen can pick up alliums, like any other one-block-tall flower, and drop one if killed while holding it.

### Chest loot
In Bedrock Edition, 8 alliums are found inside the chest in the "allium room" in woodland mansions. Due to a bug, this room does not generate in Java Edition.[1]

### Trading
Wandering traders may sell an allium for a single emerald.

## Usage
Main article: Flower § Usage
Like other flowers, alliums can be used as decoration and planted on grass blocks, dirt, coarse dirt, rooted dirt, farmland, podzol, mycelium, moss blocks, mud, or muddy mangrove roots.

Alliums can also be placed in flower pots.

### Crafting ingredient
| Name        | Ingredients | Crafting recipe |
|-------------|-------------|-----------------|
| Magenta Dye | Allium      |                 |

### Suspicious stew
Main article: Suspicious Stew
Using an allium to make suspicious stew, whether by direct crafting or by feeding a brown mooshroom and then milking it with a bowl, imbues it with a Fire Resistance effect that lasts 8 seconds in Java Edition and 6 seconds in Bedrock Edition.

| Ingredients                                            | Crafting recipe |
|--------------------------------------------------------|-----------------|
| Red Mushroom+<br/>Brown Mushroom+<br/>Bowl+<br/>Allium |                 |

### Bees
Bees engage in a pollinating behavior with alliums, increasing the honey level in beehives and bee nests by 1.

### Breeding
Alliums can be used to breed, grow, and lead bees.

### Bee nests
Oak, birch, and cherry trees grown from saplings that are within 2 blocks of an allium have a 5% chance to grow with a bee nest and 1-3 bees in it.

### Composting
Placing an allium into a composter has a 65% chance of raising the compost level by 1. A stack of alliums yields an average of 5.94 bone meal.

## Data values
### ID
Java Edition:

| Name   | Identifier | Form         | Block tags                    | Item tags                     | Translation key          |
|--------|------------|--------------|-------------------------------|-------------------------------|--------------------------|
| Allium | `allium`   | Block & Item | `flowers`<br/>`small_flowers` | `flowers`<br/>`small_flowers` | `block.minecraft.allium` |

Bedrock Edition:

| Name   | Identifier                      | Alias ID         | Numeric ID | Form                       | Item ID[i 1]   | Translation key               |
|--------|---------------------------------|------------------|------------|----------------------------|----------------|-------------------------------|
| Allium | `red_flower‌[until BE 1.20.80]` | None             | `38`       | Block & Giveable Item[i 2] | Identical[i 3] | `tile.red_flower.allium.name` |
| Allium | `allium‌[upcoming: BE 1.20.80]` | `red_flower / 2` | `-831`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.red_flower.allium.name` |

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


