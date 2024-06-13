# Carrot
A carrot is a food item obtained from carrot crops that can be used to plant them, eaten or used as a crafting ingredient.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Mob loot
	- 1.4 Chest loot
- 2 Usage
	- 2.1 Farming
	- 2.2 Breeding
	- 2.3 Trading
	- 2.4 Crafting ingredient
	- 2.5 Composting
- 3 Sounds
	- 3.1 Block
	- 3.2 Item
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 Advancements
- 6 History
	- 6.1 Carrots "item"
		- 6.1.1 Appearances
		- 6.1.2 Names
- 7 Issues
- 8 Gallery
	- 8.1 Screenshots
	- 8.2 In other media
- 9 References

## Obtaining
### Breaking
See also: Fortune § Seeds

Fully grown carrot crops drop 2 to 5 carrots (3 5⁄7 per crop harvested on average). Yield can be increased using a tool enchanted with Fortune, with Fortune III harvesting an average of 5 3⁄7 carrots.

The yield is calculated by a binomial distribution: 2 drops are fixed, then a drop is attempted three times with a success rate of 57.14286% to yield the extra 0–3 drops. Each level of Fortune enchantment increases the number of attempts by one.

| Block    | Carrots             |
|----------|---------------------|
| Hardness | 0                   |
|          | Breakingtime (secs) |
| Default  | 0.05                |

### Natural generation
Village farm plots have a chance of having carrots. The exact chance depends on the style of the village:

| Village style | Chance |
|---------------|--------|
| Plains        | 30%    |
| Snowy         | 10%    |

### Mob loot
Zombies, husks, and zombie villagers have a 2.5% (1⁄40) chance of dropping either an iron ingot, carrot, or potato when killed by a player or tamed wolf. This is increased by 1% (1⁄100) per level of looting. This gives carrots the following chances of dropping:

- 1⁄120(about 0.83%)
- 7⁄600(about 1.17%) with Looting I
- 9⁄600(about 1.50%) with Looting II
- 11⁄600(about 1.83%) with Looting III

| Source          | Roll Chance      | Quantity (Roll Chance) |           |            |             |
|-----------------|------------------|------------------------|-----------|------------|-------------|
|                 |                  | Default                | Looting I | Looting II | Looting III |
| Husk            | 0.83%–1.82%[d 1] | 1 (0.83%)              | 1 (1.16%) | 1 (1.49%)  | 1 (1.82%)   |
| Zombie Villager | 0.83%–1.82%[d 1] | 1 (0.83%)              | 1 (1.16%) | 1 (1.49%)  | 1 (1.82%)   |
| Zombie          | 0.83%–1.82%[d 1] | 1 (0.83%)              | 1 (1.16%) | 1 (1.49%)  | 1 (1.82%)   |


↑ a b c Only dropped when kill credit is given to the player


### Chest loot
| Item   | Structure        | Container    | Quantity | Chance          |
|--------|------------------|--------------|----------|-----------------|
|        |                  |              |          | Java Edition    |
| Carrot | Pillager Outpost | Chest        | 3–5      | 57.5%           |
|        | Shipwreck        | Supply chest | 4–8      | 42.1%           |
|        |                  |              |          | Bedrock Edition |
| Carrot | Bonus Chest      | Chest        | 1–2      | 50%             |
|        | Pillager Outpost | Chest        | 3–5      | 57.5%           |
|        | Shipwreck        | Supply chest | 4–8      | 42.1%           |

## Usage
See also: Hunger management

To eat a carrot, press and hold use while the carrot is selected in the hotbar. Eating a carrot restores 3 () hunger and 3.6 hunger saturation.

### Farming
See also: Crop farming

Carrots can be farmed and harvested on farmland. Planted carrots take 8 stages to grow, and go through 4 visually distinct stages. Planted carrots require a light level of 9 or greater to continue growing. If the light level is 7 or below, the crops instantly un-plant themselves ("pop off"). It is not possible to plant carrots if the light level is too low.

Crops grow faster if the farmland they are planted in is hydrated. Using bone meal on crops also increases the speed of growth by randomly increasing their growth stage by 2 to 5.

Crops break if pushed by a piston or if their supporting farmland breaks or turns to dirt (i.e. by being trampled), dropping their usual drops.

If /gamerule mobGriefing is true, rabbits will find mature carrot crops‌[Java Edition  only] / carrot crops with growth stage greater than 1‌[Bedrock Edition  only]. This reduces the growth stages by one, removing the crop completely when the growth stage reaches 0.

### Breeding
Carrots can also be used to breed and attract pigs and rabbits.

Villagers can pick up carrot items to become willing, which allow them to breed. Villagers require 12 carrots to become willing.

### Trading
Novice-level farmer villagers have a 25% (1⁄4)‌[Bedrock Edition  only] or 40% (2⁄5)‌[Java Edition  only] chance to buy 22 carrots for an emerald.

### Crafting ingredient
| Name              | Ingredients                                        | Crafting recipe | Description                                                                         |
|-------------------|----------------------------------------------------|-----------------|-------------------------------------------------------------------------------------|
| Carrot on a Stick | Fishing RodorDamagedFishing Rod+Carrot             |                 | The fishing rod must be diagonally above the carrot to craft the carrot on a stick. |
| Golden Carrot     | Gold Nugget+Carrot                                 |                 |                                                                                     |
| Rabbit Stew       | Cooked Rabbit+Carrot+Baked Potato+AnyMushroom+Bowl |                 |                                                                                     |

### Composting
Placing a carrot into a composter has a 65% chance of raising the compost level by 1.

## Data values
### ID
Java Edition:

| Name    | Identifier | Form  | Block tags         | Translation key         |
|---------|------------|-------|--------------------|-------------------------|
| Carrots | carrots    | Block | bee_growablescrops | block.minecraft.carrots |
| Carrot  | carrot     | Item  | —                  | item.minecraft.carrot   |

Bedrock Edition:

| Name    | Identifier | Numeric ID | Form                         | Item ID[i 1]   | Translation key  |
|---------|------------|------------|------------------------------|----------------|------------------|
| Carrots | carrots    | 141        | Block & Ungiveable Item[i 2] | Identical[i 3] | —                |
| Carrot  | carrot     | 279        | Item                         | —              | item.carrot.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Unavailable with /give command

↑ The block's direct item form has the same id as the block.


### Block states
See also: Block states

Java Edition:

| Name | Default value | Allowed values | Description  |
|------|---------------|----------------|--------------|
| age  | 0             | 01             |              |
|      |               | 23             |              |
|      |               | 456            |              |
|      |               | 7              | Fully grown. |

Bedrock Edition:

| Name   | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description  |
|--------|---------------|---------------|----------------|-------------------------|--------------|
| growth | 0x10x20x4     | 0             | 01             | 01                      |              |
|        |               |               | 23             | 23                      |              |
|        |               |               | 456            | 456                     |              |
|        |               |               | 7              | 7                       | Fully grown. |



