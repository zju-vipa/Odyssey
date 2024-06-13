# Beetroot Seeds
Beetroot seeds are items that can be used to plant beetroot crops.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Chest loot
	- 1.4 Trading
- 2 Usage
	- 2.1 Farming
	- 2.2 Breeding
	- 2.3 Taming
	- 2.4 Composting
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 Advancements
- 6 History
	- 6.1 Beetroot "item"
		- 6.1.1 Appearances
		- 6.1.2 Names
- 7 Issues
- 8 Gallery
	- 8.1 Screenshots
- 9 References

## Obtaining
### Breaking
Harvesting fully-grown beetroot yields from 1 to 4 seeds per crop harvested (2 5⁄7 seeds per crop harvested on average). The Fortune enchantment can be used to improve the drop rate.

| Block    | Beetroots           |
|----------|---------------------|
| Hardness | 0                   |
|          | Breakingtime (secs) |
| Default  | 0.05                |

### Natural generation
Village farm plots have a chance of being beetroots. The exact chance depends on the style of the village:

| Village style | Chance |
|---------------|--------|
| Desert        | 20%    |
| Plains        | 5%     |

### Chest loot
| Item           | Structure        | Container         | Quantity | Chance          |
|----------------|------------------|-------------------|----------|-----------------|
|                |                  |                   |          | Java Edition    |
| Beetroot Seeds | Monster Room     | Chest             | 2–4      | 18.5%           |
|                | Mineshaft        | Chest             | 2–4      | 27.3%           |
|                | End City         | Chest             | 1–10     | 21.2%           |
|                | Trail Ruins      | Suspicious gravel | 1        | 2.2%            |
|                | Village          | Snowy house chest | 1–5      | 66.3%           |
|                | Woodland Mansion | Chest             | 2–4      | 18.5%           |
|                |                  |                   |          | Bedrock Edition |
| Beetroot Seeds | Monster Room     | Chest             | 2–4      | 18.5%           |
|                | Mineshaft        | Chest             | 2–4      | 27.3%           |
|                | Bonus Chest      | Chest             | 1–2      | 33.3%           |
|                | End City         | Chest             | 1–10     | 21.2%           |
|                | Trail Ruins      | Suspicious gravel | 1        | 2.2%            |
|                | Village          | Snowy house chest | 1–5      | 66.3%           |
|                | Woodland Mansion | Chest             | 2–4      | 18.5%           |

### Trading
Beetroot seeds are sold by wandering traders for one emerald.

## Usage
### Farming
Beetroot seeds can be placed on farmland. After being placed, it goes through four stages of growth. When fully grown it can be broken to produce beetroot seeds and beetroots.

While beetroot crops have only four growth stages compared to eight for wheat, carrots and potatoes, each growth tick has a 1⁄3 chance of not advancing the growth stage and therefore beetroot grows slightly faster than other crops.

Crops grow faster if the farmland they are planted in is hydrated. One application of bone meal has a 75% chance of advancing growth by one stage. This is less effective than for other crops: an average of 5 1⁄3 are needed to fully grow beetroot compared to 2 2⁄7 for other crops.

### Breeding
Like other seeds, beetroot seeds can be used to breed chickens, lead chickens around, and make baby chickens grow up faster by 10% of the remaining time.

### Taming
Like other seeds, beetroot seeds can be used to tame parrots.

### Composting
Placing beetroot seeds into a composter has a 30% chance of raising the compost level by 1.

## Data values
### ID
Java Edition:

| Name           | Identifier     | Form  | Block tags         | Translation key               |
|----------------|----------------|-------|--------------------|-------------------------------|
| Beetroots      | beetroots      | Block | bee_growablescrops | block.minecraft.beetroots     |
| Beetroot Seeds | beetroot_seeds | Item  | —                  | item.minecraft.beetroot_seeds |

Bedrock Edition:

| Name           | Identifier     | Numeric ID | Form                         | Item ID[i 1]  | Translation key          |
|----------------|----------------|------------|------------------------------|---------------|--------------------------|
| Beetroots      | beetroot       | 244        | Block & Ungiveable Item[i 2] | item.beetroot | tile.beetroot.name       |
| Beetroot Seeds | beetroot_seeds | 295        | Item                         | —             | item.beetroot_seeds.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Unavailable with /give command


### Block states
See also: Block states

Java Edition:

| Name | Default value | Allowed values | Description  |
|------|---------------|----------------|--------------|
| age  | 0             | 0              |              |
|      |               | 1              |              |
|      |               | 2              |              |
|      |               | 3              | Fully grown. |

Bedrock Edition:

| Name   | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description  |
|--------|---------------|---------------|----------------|-------------------------|--------------|
| growth | 0x10x20x4     | 0             | 01             | 01                      |              |
|        |               |               | 23             | 23                      |              |
|        |               |               | 456            | 456                     |              |
|        |               |               | 7              | 7                       | Fully grown. |




