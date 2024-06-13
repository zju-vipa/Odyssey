# Potato
A potato is a food item obtained from potato crops that can be used to plant them, consumed raw or cooked to make baked potatoes.

Potato crops are planted in farmland and used to grow potatoes and, rarely, poisonous potatoes.

## Contents
- 1 Obtaining
	- 1.1 Natural generation
	- 1.2 Mob loot
	- 1.3 Chest loot
- 2 Usage
	- 2.1 Farming
	- 2.2 Food
	- 2.3 Breeding
	- 2.4 Smelting ingredient
	- 2.5 Trading
	- 2.6 Composting
- 3 Sounds
	- 3.1 Block
	- 3.2 Item
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 Advancements
- 6 History
	- 6.1 Potatoes "item"
		- 6.1.1 Appearances
		- 6.1.2 Names
- 7 Issues
- 8 Gallery
	- 8.1 Screenshots
	- 8.2 In other media
- 9 References
- 10 External links

## Obtaining
### Natural generation
Village farm plots have a chance of being planted with potatoes. The exact chance depends on the style of the village:

| Village style | Chance |
|---------------|--------|
| Snowy         | 70%    |
| Plains        | 15%    |
| Taiga         | 10%    |

Fully grown potato crops drop 2 to 5 potatoes (3 5⁄7 per crop harvested on average) and have a 2% chance of dropping an additional poisonous potato. Potato yield can be increased using a tool enchanted with Fortune, with Fortune III harvesting an average of 5 3⁄7 potatoes. Bone meal can be used to mature the potato to its last stage of growth.

The first two potatoes always drop, and then three more attempts are made to drop a potato with a success rate of 57.14286% to yield the extra 0–3 drops. Each level of Fortune enchantment increases the number of attempts by one.

### Mob loot
Zombies, husks, and zombie villagers have a 2.5% (1⁄40) chance of dropping either an iron ingot, carrot, or potato when killed by a player or tamed wolf. This is increased by 1% (1⁄100) per level of looting. This gives potatoes the following chances of dropping:

- 1⁄120(about 0.83%)
- 7⁄600(about 1.17%) with Looting I
- 9⁄600(1.50%) with Looting II
- 11⁄600(about 1.83%) with Looting III

When killed with fire, a zombie drops a baked potato instead.

| Source          | Roll Chance      | Quantity (Roll Chance) |           |            |             |
|-----------------|------------------|------------------------|-----------|------------|-------------|
|                 |                  | Default                | Looting I | Looting II | Looting III |
| Husk            | 0.83%–1.82%[d 1] | 1 (0.83%)              | 1 (1.16%) | 1 (1.49%)  | 1 (1.82%)   |
| Zombie Villager | 0.83%–1.82%[d 1] | 1 (0.83%)              | 1 (1.16%) | 1 (1.49%)  | 1 (1.82%)   |
| Zombie          | 0.83%–1.82%[d 1] | 1 (0.83%)              | 1 (1.16%) | 1 (1.49%)  | 1 (1.82%)   |

1. ↑ a b cOnly dropped when kill credit is given to the player

### Chest loot
| Item   | Structure        | Container          | Quantity | Chance          |
|--------|------------------|--------------------|----------|-----------------|
|        |                  |                    |          | Java Edition    |
| Potato | Pillager Outpost | Chest              | 2–5      | 57.5%           |
|        | Shipwreck        | Supply chest       | 2–6      | 42.1%           |
|        | Village          | Snowy house chest  | 1–7      | 66.3%           |
|        |                  | Taiga house chest  | 1–7      | 65.6%           |
|        |                  | Plains house chest | 1–7      | 74.2%           |
|        |                  |                    |          | Bedrock Edition |
| Potato | Bonus Chest      | Chest              | 1–2      | 50%             |
|        | Pillager Outpost | Chest              | 2–5      | 57.5%           |
|        | Shipwreck        | Supply chest       | 2–6      | 42.1%           |
|        | Village          | Snowy house chest  | 1–7      | 66.3%           |
|        |                  | Taiga house chest  | 1–7      | 69.3%           |
|        |                  | Plains house chest | 1–7      | 74.2%           |

## Usage
### Farming
Main article: Tutorials/Crop farming
When farmed, potatoes require 8 stages to grow. However, there are four visible stages due to having only four distinct textures: every two stages have the same texture, except that growth stage 7 keeps the same appearance as stages 5–6, so that only stage 8 has the final, mature appearance. Planted potatoes require a light level of 9 or greater to continue growing. If the light level is 7 or below, the crops instantly un-plant themselves ("pop off"). It is not possible to plant potatoes if the light level is too low.

Crops grow faster if the farmland they are planted in is hydrated. Using bone meal on crops also increases the speed of growth by randomly increasing their growth stage by 2 to 5.

Crops break if pushed by a piston or if their supporting farmland breaks or turns to dirt (i.e. by being trampled), dropping their usual drops.

### Food
To eat a potato, press and hold use while it is selected in the hotbar. Eating a potato restores 1 () hunger and 0.6 saturation.

### Breeding
Pigs follow and can be bred by a player holding a potato.

Villagers can pick up potato items to become willing, which allow them to breed. Villagers require 12 potatoes to become willing.

### Smelting ingredient
| Name         | Ingredients         | Smelting recipe |
|--------------|---------------------|-----------------|
| Baked Potato | Potato+<br/>Anyfuel | 0.35            |

### Trading
Novice-level farmer villagers have a 25%‌[Bedrock Edition  only] or 40%‌[Java Edition  only] chance to buy 26 potatoes for an emerald as part of their trade.

### Composting
Placing a potato into a composter has a 65% chance of raising the compost level by 1. This is less efficient than composting with baked potatoes, which has a higher success chance of 85%.

## Data values
### ID
Java Edition:

| Name     | Identifier | Form  | Block tags                  | Translation key            |
|----------|------------|-------|-----------------------------|----------------------------|
| Potatoes | `potatoes` | Block | `bee_growables`<br/>`crops` | `block.minecraft.potatoes` |
| Potato   | `potato`   | Item  | —                           | `item.minecraft.potato`    |

Bedrock Edition:

| Name     | Identifier | Numeric ID | Form                         | Item ID[i 1]   | Translation key      |
|----------|------------|------------|------------------------------|----------------|----------------------|
| Potatoes | `potatoes` | `142`      | Block & Ungiveable Item[i 2] | Identical[i 3] | `tile.potatoes.name` |
| Potato   | `potato`   | `280`      | Item                         | —              | `item.potato.name`   |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Unavailable with /give command
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

Java Edition:

| Name | Default value | Allowed values      | Description  |
|------|---------------|---------------------|--------------|
| age  | `0`           | `0`<br/>`1`         |              |
|      |               | `2`<br/>`3`         |              |
|      |               | `4`<br/>`5`<br/>`6` |              |
|      |               | `7`                 | Fully grown. |

Bedrock Edition:

| Name   | Metadata Bits             | Default value | Allowed values      | Values forMetadata Bits | Description  |
|--------|---------------------------|---------------|---------------------|-------------------------|--------------|
| growth | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`<br/>`1`         | `0`<br/>`1`             |              |
|        |                           |               | `2`<br/>`3`         | `2`<br/>`3`             |              |
|        |                           |               | `4`<br/>`5`<br/>`6` | `4`<br/>`5`<br/>`6`     |              |
|        |                           |               | `7`                 | `7`                     | Fully grown. |



