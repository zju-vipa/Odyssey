# Suspicious Stew
Suspicious stew is a food item that can give the player a status effect that depends on the flower used to craft it.

## Contents
- 1 Obtaining
	- 1.1 Chest loot
	- 1.2 Crafting
	- 1.3 Harvesting
	- 1.4 Trading
- 2 Usage
	- 2.1 Food
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Item data
	- 4.3 Metadata
- 5 Achievements
- 6 Advancements
- 7 History
- 8 Issues
- 9 Trivia
- 10 References

## Obtaining
In Bedrock Edition, suspicious stew is the only food item in the game that can be obtained from the Creative inventory only by searching. However, it can be crafted and can also be found in shipwreck chests. Suspicious stew can be given with commands like /give, but in Java Edition, unless NBT data like that listed in the data values section is included, consuming it has no effect and still restores the same hunger points as a normal suspicious stew. In Bedrock Edition, giving the player a suspicious stew through commands causes the stew to choose an allowable status effect at random.

### Chest loot
| Item               | Structure   | Container       | Quantity | Chance          |
|--------------------|-------------|-----------------|----------|-----------------|
|                    |             |                 |          | Java Edition    |
| Suspicious Stew[A] | Desert well | Suspicious sand | 1        | 12.5%           |
|                    | Shipwreck   | Supply chest    | 1        | 54.3%           |
|                    |             |                 |          | Bedrock Edition |
| Suspicious Stew[A] | Desert well | Suspicious sand | 1        | 12.5%           |
|                    | Shipwreck   | Supply chest    | 1        | 54.3%           |

1. ↑ a bThe stew grants one of the following effects: 5–7 seconds of Blindness, 7–10 seconds of Jump Boost, 7-10 seconds of Night Vision, 10–20 seconds of Poison, 0.35-0.5 seconds of Saturation, or 6–8 seconds of Weakness.

### Crafting
| Ingredients                                                     | Crafting recipe |
|-----------------------------------------------------------------|-----------------|
| Red Mushroom+<br/>Brown Mushroom+<br/>Bowl+<br/>AnySmall Flower |                 |

Suspicious stew is not listed in the recipe book. However, it can be quickly assembled by clicking the mushroom stew recipe and adding one small flower to it.

### Harvesting
Suspicious stew can be obtained by “milking” a brown mooshroom by using an empty bowl on it after using a small flower on it. The flower type determines the stew's effect using the same rule as a crafted stew. After being milked once, the brown mooshroom returns to producing mushroom stew until fed another small flower. Red mooshrooms do not produce suspicious stew.

### Trading
In Java Edition, expert-level farmer villagers can offer either 1 or 2 suspicious stew trades, each stew for one emerald.

In Bedrock Edition, expert-level farmer villager offers to sell suspicious stew for one emerald as well.

The trading interface does not indicate the type of suspicious stew being sold, but each trade entry consistently yields the same type of stew, so the player can remember or make a note of the types offered by a given villager, such as "this villager's first stew gives blindness, and their second entry gives saturation".

## Usage
### Food
See also: Tutorials/Hunger management

To eat suspicious stew, press and hold use while it is selected in the hotbar. Eating one restores 6 () hunger and 7.2 hunger saturation and gives a few seconds of a status effect that varies depending on which flower was used to craft it. The effect is not displayed in the tooltip, texture, etc., meaning that the player cannot know in advance what the effect is without knowing which flower was used.

| Flower                    | Effect          | Duration (JE) | Duration (BE) |
|---------------------------|-----------------|---------------|---------------|
| Allium                    | Fire Resistance | 4s            | 2s            |
| Azure Bluet               | Blindness       | 8s            | 6s            |
| Blue Orchid<br/>Dandelion | Saturation      | 0.35s         | 0.3s          |
| Cornflower                | Jump Boost      | 6s            | 4s            |
| Lily of the Valley        | Poison          | 12s           | 10s           |
| Oxeye Daisy               | Regeneration    | 8s            | 6s            |
| Poppy<br/>Torchflower     | Night Vision    | 5s            | 4s            |
| Tulips                    | Weakness        | 9s            | 7s            |
| Wither Rose               | Wither          | 8s            | 6s            |

The bowl is emptied and returned to the player after the suspicious stew has been eaten, and can be re-used to craft more stews. Unlike most foods, suspicious stew can be eaten even if the player's hunger bar is full.

The Saturation effect effectively makes those two stews a superfood: In those 6 or 7 ticks it can restore up to 6(7) hunger and 12(14) saturation points on top of their food value, for a total of at least 12 ( × 6) hunger, and effectively maximizing saturation. This is the largest amount of hunger and saturation the player can get from a single food item. Regeneration can restore up to 3 health, and Poison or Wither can inflict up to 4 damage.

Consuming suspicious stew is the only way to obtain the Saturation and Blindness effects in vanilla Minecraft without the use of commands.

## Data values
### ID
Java Edition:

| Name            | Identifier        | Form | Translation key                  |
|-----------------|-------------------|------|----------------------------------|
| Suspicious Stew | `suspicious_stew` | Item | `item.minecraft.suspicious_stew` |

Bedrock Edition:

| Name            | Identifier        | Numeric ID | Form | Translation key             |
|-----------------|-------------------|------------|------|-----------------------------|
| Suspicious Stew | `suspicious_stew` | `590`      | Item | `item.suspicious_stew.name` |

### Item data
In Java Edition, suspicious stew uses the following NBT data:

- tag: The item'stagtag.

- 
	- effects: Thestatus effectsthis suspicious stew has.
		- One of these for each effect.
			- id: Theresource location of the effect.
			- duration: The duration of the effect inticks. Values 0 or lower are treated as 1. Optional, and defaults to 160 ticks (8 seconds).

### Metadata
In Bedrock Edition, suspicious stew uses the following data values:

|  | DV | Description                 |
|--|----|-----------------------------|
|  | 0  | Night VisionfromPoppy       |
|  | 1  | Jump Boost                  |
|  | 2  | Weakness                    |
|  | 3  | Blindness                   |
|  | 4  | Poison                      |
|  | 5  | SaturationfromDandelion     |
|  | 6  | SaturationfromBlue Orchid   |
|  | 7  | Fire Resistance             |
|  | 8  | Regeneration                |
|  | 9  | Wither                      |
|  | 10 | Night VisionfromTorchflower |

