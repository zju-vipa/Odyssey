# Pumpkin Seeds
Pumpkin seeds are items obtained from pumpkins that can be used to grow pumpkin stems.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Chest loot
	- 1.4 Crafting
	- 1.5 Trading
	- 1.6 Post-generation
- 2 Usage
	- 2.1 Farming
	- 2.2 Breeding
	- 2.3 Taming
	- 2.4 Composting
- 3 Pumpkin stem
- 4 Sounds
- 5 Data values
	- 5.1 ID
	- 5.2 Block states
- 6 Advancements
- 7 History
	- 7.1 Pumpkin stem "item"
		- 7.1.1 Appearances
		- 7.1.2 Names
- 8 Issues
- 9 Gallery
	- 9.1 Renders
		- 9.1.1 Pumpkin stem
		- 9.1.2 Attached pumpkin stem
	- 9.2 Screenshots
- 10 References

## Obtaining
### Breaking
When broken, a pumpkin stem drops 0–3 pumpkin seeds. The chance for pumpkin seeds to drop increases with the stem's age.

| Resource location            | Source                | Default |        |         |               |
|------------------------------|-----------------------|---------|--------|---------|---------------|
|                              |                       |         |        | Nothing | Pumpkin seeds |
|                              |                       |         | 1      | 2       | 3             |
| blocks/pumpkin_stem          | Pumpkin stemage = 0   | 81.3%   | 17.42% | 1.24%   | 0.03%         |
|                              | Pumpkin stemage = 1   | 65.1%   | 30.04% | 4.62%   | 0.24%         |
|                              | Pumpkin stemage = 2   | 51.2%   | 38.4%  | 9.6%    | 0.8%          |
|                              | Pumpkin stemage = 3   | 39.44%  | 43.02% | 15.64%  | 1.9%          |
|                              | Pumpkin stemage = 4   | 29.13%  | 44.44% | 22.22%  | 3.7%          |
|                              | Pumpkin stemage = 5   | 21.6%   | 43.2%  | 28.8%   | 6.4%          |
|                              | Pumpkin stemage = 6   | 15.17%  | 39.82% | 34.84%  | 10.16%        |
|                              | Pumpkin stemage = 7   | 10.16%  | 34.84% | 39.82%  | 15.17%        |
| blocks/attached_pumpkin_stem | Attached Pumpkin stem | 10.16%  | 34.84% | 39.82%  | 15.17%        |

### Natural generation
Pumpkin stems generate naturally in stem farm rooms in woodland mansions.

Pumpkin stems generate in taiga and snowy taiga‌[BE  only] village farms.

### Chest loot
| Item          | Structure        | Container         | Quantity | Chance          |
|---------------|------------------|-------------------|----------|-----------------|
|               |                  |                   |          | Java Edition    |
| Pumpkin Seeds | Monster Room     | Chest             | 2–4      | 18.5%           |
|               | Mineshaft        | Chest             | 2–4      | 27.3%           |
|               | Village          | Taiga house chest | 1–5      | 40.6%           |
|               | Woodland Mansion | Chest             | 2–4      | 18.5%           |
|               |                  |                   |          | Bedrock Edition |
| Pumpkin Seeds | Monster Room     | Chest             | 2–4      | 18.5%           |
|               | Mineshaft        | Chest             | 2–4      | 27.3%           |
|               | Bonus Chest      | Chest             | 1–2      | 33.3%           |
|               | Village          | Taiga house chest | 1–5      | 43.7%           |
|               | Woodland Mansion | Chest             | 2–4      | 18.5%           |

### Crafting
| Ingredients | Crafting recipe |
|-------------|-----------------|
| Pumpkin     | 4               |

### Trading
Wandering traders sell pumpkin seeds for 1 emerald.

### Post-generation
Shearing an uncarved pumpkin yields 4 pumpkin seeds in Java Edition or 1 unit of pumpkin seeds in Bedrock Edition.

## Usage
### Farming
See also: Tutorials/Pumpkin and melon farming

Pumpkin seeds can be planted only on farmland, as stems. Over time, a stem grows through several stages and, at its final growth stage, will produce pumpkins on any adjacent dirt, coarse dirt, rooted dirt, grass block, farmland, podzol, mycelium, moss block, mud or muddy mangrove roots. If a pumpkin is already occupying a spot adjacent to a stem it does not grow more pumpkins until the pumpkin is removed. A single stem can grow an unlimited number of pumpkins. Pumpkin stems need a minimum light level of 10 in the block above the stem to grow and give pumpkins. Pumpkin seeds are affected by bone meal only with respect to stem growth; bone meal does not help produce the actual pumpkins.

### Breeding
Like other seeds, pumpkin seeds can be used to breed chickens, lead chickens around, and make baby chickens grow up faster by 10% of the remaining time.

### Taming
Like other seeds, pumpkin seeds can be used to tame parrots.

### Composting
Placing pumpkin seeds into a composter has a 30% chance of raising the compost level by 1.

## Pumpkin stem
A pumpkin stem is the block that is planted on farmland when pumpkin seeds are used on it. It starts underground, and rises up as the plant grows. The stem is colored green when young, and then yellow once fully grown.

The stem curves once a pumpkin has grown from it. A fully-grown single stem connects to any pumpkin in an adjacent square, thus there are 5 possible appearances to a stem. If there are multiple pumpkins it can connect to, it favors the east, then west, north, and south. When the pumpkin is removed, the stem returns to its straight shape.

## Data values
### ID
Java Edition:

| Name                  | Identifier            | Form  | Block tags         | Translation key                       |
|-----------------------|-----------------------|-------|--------------------|---------------------------------------|
| Pumpkin Stem          | pumpkin_stem          | Block | bee_growablescrops | block.minecraft.pumpkin_stem          |
| Attached Pumpkin Stem | attached_pumpkin_stem | Block | None               | block.minecraft.attached_pumpkin_stem |
| Pumpkin Seeds         | pumpkin_seeds         | Item  | —                  | item.minecraft.pumpkin_seeds          |

Bedrock Edition:

| Name          | Identifier    | Numeric ID | Form                         | Item ID[i 1]   | Translation key         |
|---------------|---------------|------------|------------------------------|----------------|-------------------------|
| Pumpkin Stem  | pumpkin_stem  | 104        | Block & Ungiveable Item[i 2] | Identical[i 3] | tile.pumpkin_stem.name  |
| Pumpkin Seeds | pumpkin_seeds | 292        | Item                         | —              | item.pumpkin_seeds.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Unavailable with /give command

↑ The block's direct item form has the same id as the block.


### Block states
See also: Block states

Java Edition:
Growing

| Name | Default value | Allowed values | Description                                         |
|------|---------------|----------------|-----------------------------------------------------|
| age  | 0             | 0              | A newly planted stem.                               |
|      |               | 123456         | Intermediate growth stages of the stem.             |
|      |               | 7              | A fully mature stem, capable of producing pumpkins. |

Attached

| Name   | Default value | Allowed values     | Description                                 |
|--------|---------------|--------------------|---------------------------------------------|
| facing | north         | eastnorthsouthwest | The direction from the stem to the pumpkin. |

Bedrock Edition:

| Name             | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                         |
|------------------|---------------|---------------|----------------|-------------------------|-----------------------------------------------------|
| growth           | 0x10x20x4     | 0             | 0              | 0                       | A newly planted stem.                               |
|                  |               |               | 123456         | 123456                  | Intermediate growth stages of the stem.             |
|                  |               |               | 7              | 7                       | A fully mature stem, capable of producing pumpkins. |
| facing_direction | Not Supported | 0             | 01             | Unsupported             | Unused                                              |
|                  |               |               | 2              | Unsupported             | Stem pointing north.                                |
|                  |               |               | 3              | Unsupported             | Stem pointing south.                                |
|                  |               |               | 4              | Unsupported             | Stem pointing west.                                 |
|                  |               |               | 5              | Unsupported             | Stem pointing east.                                 |



