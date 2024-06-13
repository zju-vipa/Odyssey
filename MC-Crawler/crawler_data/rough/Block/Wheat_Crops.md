# Wheat Seeds
Wheat seeds (in Java Edition) or seeds (in Bedrock Edition) are items obtained by breaking grass, or more abundantly harvested from wheat crops, and are used to plant them.

Wheat crops are planted in farmland and used to grow wheat and wheat seeds. 

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Chest loot
	- 1.4 Trading
	- 1.5 Villager gifts
- 2 Usage
	- 2.1 Crop
	- 2.2 Breeding
	- 2.3 Taming
	- 2.4 Composting
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 Advancements
- 6 History
	- 6.1 Wheat "item"
		- 6.1.1 Appearances
		- 6.1.2 Names
- 7 Issues
- 8 Gallery
	- 8.1 Renders
		- 8.1.1 Java Edition
		- 8.1.2 Bedrock Edition
	- 8.2 Screenshots
- 9 References

## Obtaining
### Breaking
Wheat seeds can be obtained from breaking short grass, tall grass, fern or large fern, which have a 12.5% chance to yield 1 seed. If harvested with a tool enchanted with Fortune, the drop rate is increased to 1-3, 1-5, or 1-7 wheat seeds respectively with Fortune I, II, and III.

Harvesting fully-grown wheat crops yields from 1 to 4 seeds per crop harvested (about 2 5⁄7 seeds/crop harvested on average).

The looting is calculated by a binomial distribution: a drop is attempted three times with a success rate of around 57% to yield the 0–3 drops. Each level of Fortune enchantment increases the number of attempts by one.

| Resource location | Source         | Drops |                                                              |                                                                               |                                                                                              |                                                                                                               |
|-------------------|----------------|-------|--------------------------------------------------------------|-------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
|                   |                | Wheat |                                                              |                                                                               |                                                                                              | Wheat Seeds                                                                                                   |
|                   |                |       | Default tool                                                 | WithFortuneI                                                                  | With Fortune II                                                                              | With Fortune III                                                                                              |
| `blocks/wheat`    | Wheat(age 0–6) | 0     | 1                                                            | 1                                                                             | 1                                                                                            | 1                                                                                                             |
|                   | Wheat(age 7)   | 1     | 1(~7.87%)or<br/>2(~31.49%)or<br/>3(~41.98%)or<br/>4(~18.66%) | 1(~3.37%)or<br/>2(~17.99%)or<br/>3(~35.98%)or<br/>4(~31.99%)or<br/>5(~10.66%) | 1(~1.44%)or<br/>2(~9.64%)or<br/>3(~25.70%)or<br/>4(~34.27%)or<br/>5(~22.85%)or<br/>6(~6.09%) | 1(~0.62%)or<br/>2(~4.96%)or<br/>3(~16.52%)or<br/>4(~29.38%)or<br/>5(~29.38%)or<br/>6(~15.67%)or<br/>7(~3.48%) |

### Natural generation
Village farm plots have a chance of being wheat crops. The exact chance depends on the style of the village:

| Village style | Chance |
|---------------|--------|
| Savanna       | 80%    |
| Desert        | 70%    |
| Taiga         | 60%    |
| Plains        | 50%    |
| Snowy         | 20%    |

### Chest loot
| Item        | Structure   | Container           | Quantity | Chance          |
|-------------|-------------|---------------------|----------|-----------------|
|             |             |                     |          | Java Edition    |
| Wheat Seeds | Trail Ruins | Suspicious gravel   | 1        | 2.2%            |
|             | Village     | Fisherman's chest   | 1–3      | 57.5%           |
|             |             | Savanna house chest | 1–5      | 71.7%           |
|             |             |                     |          | Bedrock Edition |
| Wheat Seeds | Trail Ruins | Suspicious gravel   | 1        | 2.2%            |
|             | Village     | Savanna house chest | 1–5      | 71.7%           |

### Trading
Wandering traders sell wheat seeds for an emerald.

### Villager gifts

  

This feature is exclusive to  Java Edition. 


Nitwit and unemployed villagers throw wheat seeds at players under the Hero of the Village effect.

## Usage
### Crop
Main article: Crop Farming
Different stages of crop growth.
Wheat seeds can be placed on farmland by right-clicking, where they grow through eight stages. When left alone, wheat seeds planted on farmland grow to become wheat crops, which can be harvested by the player. Planted seeds require a light level of 9 or greater to continue growing.

If the light level is 7 or below, the crops instantly un-plant themselves ("pop off"). It is not possible to plant seeds if the light level is too low, as the game physically prevents you from planting them (like how you can't plant sugarcane away from water).

Crops grow faster if the farmland they are planted on is hydrated. Using bone meal on crops also increases the speed of growth by randomly increasing their growth stage by 2 to 5.

Breaking the final stage produces 1 to 4 wheat seeds (or more with Fortune) and 1 wheat. If they are harvested early, they drop 1 seed without any wheat. Crops break if pushed by a piston or if their supporting farmland breaks or turns to dirt (i.e. by being trampled), dropping their usual drops.

### Breeding
Like other seeds, wheat seeds can be used to breed chickens and reduce the remaining growth duration of baby chickens by 10%. Chickens also follow a player holding wheat seeds.

### Taming
Like other seeds, wheat seeds can be used to tame parrots.

### Composting
Placing wheat seeds into a composter has a 30% chance of raising the compost level by 1. A stack of wheat seeds yields an average of 2.74 bone meal.

## Data values
### ID
Java Edition:

| Name        | Identifier    | Form  | Block tags                  | Translation key              |
|-------------|---------------|-------|-----------------------------|------------------------------|
| Wheat Crops | `wheat`       | Block | `bee_growables`<br/>`crops` | `block.minecraft.wheat`      |
| Wheat Seeds | `wheat_seeds` | Item  | —                           | `item.minecraft.wheat_seeds` |

Bedrock Edition:

| Name  | Identifier    | Numeric ID | Form                         | Item ID[i 1] | Translation key         |
|-------|---------------|------------|------------------------------|--------------|-------------------------|
| Wheat | `wheat`       | `59`       | Block & Ungiveable Item[i 2] | `item.wheat` | `tile.wheat.name`       |
| Seeds | `wheat_seeds` | `291`      | Item                         | —            | `item.wheat_seeds.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Unavailable with /give command

### Block states
See also: Block states

Java Edition:

| Name | Default value | Allowed values | Description  |
|------|---------------|----------------|--------------|
| age  | `0`           | `0`            |              |
|      |               | `1`            |              |
|      |               | `2`            |              |
|      |               | `3`            |              |
|      |               | `4`            |              |
|      |               | `5`            |              |
|      |               | `6`            |              |
|      |               | `7`            | Fully grown. |

Bedrock Edition:

| Name   | Metadata Bits             | Default value | Allowed values | Values forMetadata Bits | Description  |
|--------|---------------------------|---------------|----------------|-------------------------|--------------|
| growth | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`            | `0`                     |              |
|        |                           |               | `1`            | `1`                     |              |
|        |                           |               | `2`            | `2`                     |              |
|        |                           |               | `3`            | `3`                     |              |
|        |                           |               | `4`            | `4`                     |              |
|        |                           |               | `5`            | `5`                     |              |
|        |                           |               | `6`            | `6`                     |              |
|        |                           |               | `7`            | `7`                     | Fully grown. |



