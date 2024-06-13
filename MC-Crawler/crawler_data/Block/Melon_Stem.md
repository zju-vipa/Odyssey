# Melon Seeds
Melon seeds are items obtained from melon slices that can be used to grow melon stems.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Chest loot
	- 1.4 Crafting
	- 1.5 Trading
- 2 Usage
	- 2.1 Farming
	- 2.2 Breeding
	- 2.3 Taming
	- 2.4 Composting
- 3 Melon stem
- 4 Sounds
- 5 Data values
	- 5.1 ID
	- 5.2 Block states
- 6 Advancements
- 7 History
	- 7.1 Melon stem "item"
		- 7.1.1 Appearances
		- 7.1.2 Names
- 8 Issues
- 9 Gallery
	- 9.1 Renders
		- 9.1.1 Melon stem
		- 9.1.2 Attached melon stem
	- 9.2 Screenshots
- 10 See also
- 11 References

## Obtaining
### Breaking
When broken, a melon stem drops 0–3 melon seeds. The chance for melon seeds to drop increases with the stem's age.

| Resource location          | Source              | Default |        |         |             |
|----------------------------|---------------------|---------|--------|---------|-------------|
|                            |                     |         |        | Nothing | Melon seeds |
|                            |                     |         | 1      | 2       | 3           |
| blocks/melon_stem          | Melon stemage = 0   | 81.3%   | 17.42% | 1.24%   | 0.03%       |
|                            | Melon stemage = 1   | 65.1%   | 30.04% | 4.62%   | 0.24%       |
|                            | Melon stemage = 2   | 51.2%   | 38.4%  | 9.6%    | 0.8%        |
|                            | Melon stemage = 3   | 39.44%  | 43.02% | 15.64%  | 1.9%        |
|                            | Melon stemage = 4   | 29.13%  | 44.44% | 22.22%  | 3.7%        |
|                            | Melon stemage = 5   | 21.6%   | 43.2%  | 28.8%   | 6.4%        |
|                            | Melon stemage = 6   | 15.17%  | 39.82% | 34.84%  | 10.16%      |
|                            | Melon stemage = 7   | 10.16%  | 34.84% | 39.82%  | 15.17%      |
| blocks/attached_melon_stem | Attached Melon stem | 10.16%  | 34.84% | 39.82%  | 15.17%      |

### Natural generation
Melon stems generate naturally in stem farm rooms inside woodland mansions.

Melon stems generate in 20% of the farm plots in savanna villages, and 10% of the farm plots in desert villages.

### Chest loot
| Item        | Structure        | Container | Quantity | Chance          |
|-------------|------------------|-----------|----------|-----------------|
|             |                  |           |          | Java Edition    |
| Melon Seeds | Monster Room     | Chest     | 2–4      | 18.5%           |
|             | Mineshaft        | Chest     | 2–4      | 27.3%           |
|             | Woodland Mansion | Chest     | 2–4      | 18.5%           |
|             |                  |           |          | Bedrock Edition |
| Melon Seeds | Monster Room     | Chest     | 2–4      | 18.5%           |
|             | Mineshaft        | Chest     | 2–4      | 27.3%           |
|             | Bonus Chest      | Chest     | 1–2      | 33.3%           |
|             | Woodland Mansion | Chest     | 2–4      | 18.5%           |

### Crafting
| Ingredients | Crafting recipe |
|-------------|-----------------|
| Melon Slice |                 |

### Trading
Wandering traders sell melon seeds for 1 emerald.

## Usage
### Farming
See also: Tutorials/Pumpkin and melon farming

Melon seeds can be planted only on farmland, as stems. Over time, a stem grows through several stages[needs testing] and, at its final growth stage, will produce melons on any adjacent dirt, coarse dirt, rooted dirt, grass block, farmland, podzol, mycelium, moss block, mud or muddy mangrove roots. If a melon is already occupying a spot adjacent to a stem it does not grow more melons until the melons is removed. A single stem can grow an unlimited number of melons. Melon stems need a minimum light level of 10 in the block above the stem to grow and give melons. Melon seeds are affected by bone meal only with respect to stem growth; bone meal does not help produce the actual melons.

### Breeding
Like other seeds, melon seeds can be used to breed chickens, lead chickens around, and make baby chickens grow up faster by 10% of the remaining time.

### Taming
Like other seeds, melon seeds can be used to tame parrots.

### Composting
Placing melon seeds into a composter has a 30% chance of raising the compost level by 1.

## Melon stem
A melon stem is the block that is planted on farmland when melon seeds are used on it. It starts underground, and rises up as the plant grows. The stem is colored green when young, and then yellow once fully grown.

The stem curves once a melon has grown from it. A fully-grown single stem connects to any melon in an adjacent square, thus there are 5 possible appearances to a stem. If there are multiple melons it can connect to, it favors the east, then west, north, and south. When the melon is removed, the stem returns to its straight shape.

## Data values
### ID
Java Edition:

| Name                | Identifier          | Form  | Block tags         | Translation key                     |
|---------------------|---------------------|-------|--------------------|-------------------------------------|
| Melon Stem          | melon_stem          | Block | bee_growablescrops | block.minecraft.melon_stem          |
| Attached Melon Stem | attached_melon_stem | Block | None               | block.minecraft.attached_melon_stem |
| Melon Seeds         | melon_seeds         | Item  | —                  | item.minecraft.melon_seeds          |

Bedrock Edition:

| Name        | Identifier  | Numeric ID | Form                         | Item ID[i 1]   | Translation key       |
|-------------|-------------|------------|------------------------------|----------------|-----------------------|
| Melon Stem  | melon_stem  | 105        | Block & Ungiveable Item[i 2] | Identical[i 3] | —                     |
| Melon Seeds | melon_seeds | 293        | Item                         | —              | item.melon_seeds.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Unavailable with /give command

↑ The block's direct item form has the same id as the block.


### Block states
See also: Block states

Java Edition:
Growing

| Name | Default value | Allowed values | Description                                       |
|------|---------------|----------------|---------------------------------------------------|
| age  | 0             | 0              | A newly planted stem.                             |
|      |               | 123456         | Intermediate growth stages of the stem.           |
|      |               | 7              | A fully mature stem, capable of producing melons. |

Attached

| Name   | Default value | Allowed values     | Description                               |
|--------|---------------|--------------------|-------------------------------------------|
| facing | north         | eastnorthsouthwest | The direction from the stem to the melon. |

Bedrock Edition:

| Name             | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                       |
|------------------|---------------|---------------|----------------|-------------------------|---------------------------------------------------|
| growth           | 0x10x20x4     | 0             | 0              | 0                       | A newly planted stem.                             |
|                  |               |               | 123456         | 123456                  | Intermediate growth stages of the stem.           |
|                  |               |               | 7              | 7                       | A fully mature stem, capable of producing melons. |
| facing_direction | Not Supported | 0             | 01             | Unsupported             | Unused                                            |
|                  |               |               | 2              | Unsupported             | Stem pointing north.                              |
|                  |               |               | 3              | Unsupported             | Stem pointing south.                              |
|                  |               |               | 4              | Unsupported             | Stem pointing west.                               |
|                  |               |               | 5              | Unsupported             | Stem pointing east.                               |



## See also
- Melon
- Pumpkin Seeds

