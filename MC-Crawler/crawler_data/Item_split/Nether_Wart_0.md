# Nether Wart
Nether wart is a fungus harvested from nether wart crops and is used to plant them, as well as being vital in the creation of potions.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Chest loot
- 2 Usage
	- 2.1 Brewing ingredient
	- 2.2 Crafting ingredient
	- 2.3 Trading
	- 2.4 Farming
	- 2.5 Composting
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 Advancements
- 6 History
	- 6.1 Nether wart "item" (the crop item)
		- 6.1.1 Appearances
		- 6.1.2 Names
- 7 Issues
- 8 Trivia
- 9 Gallery
	- 9.1 Renders
	- 9.2 Screenshots
- 10 References

## Obtaining
### Breaking
Nether wart can be mined instantly with any tool. A fully mature nether wart crop yields 2–4 nether wart. This is increased by one for each level of Fortune, this allows for a maximum of 7 nether warts dropping from one crop. Less mature stages drop one nether wart, even with the Fortune enchantment.

| Block    | Nether Wart         |
|----------|---------------------|
| Hardness | 0                   |
|          | Breakingtime (secs) |
| Default  | 0.05                |

### Natural generation
Nether wart can generate in nether fortresses in soul sand gardens around stairwells. Nether wart can also generate in the courtyards of housing unit bastion remnants. Due to only spawning in these specific structures, it's entirely possible for a nether fortress or bastion remnant to generate without nether wart (though they may still appear in the chests that generate in the fortress). 

| Location        | Description                                                                                                        | Image                                     |
|-----------------|--------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| Nether Fortress | Nether wart can be found growing near stairwells in small soul sand gardens.                                       | Nether wart growing in a nether fortress. |
| Bastion Remnant | Nether wart can be found growing in the central courtyard of each of the sections of piglin housing unit bastions. | Nether wart growing in a bastion remnant. |



### Chest loot
| Item        | Structure       | Container | Quantity | Chance                         |
|-------------|-----------------|-----------|----------|--------------------------------|
|             |                 |           |          | Java EditionandBedrock Edition |
| Nether Wart | Nether Fortress | Chest     | 3–7      | 19%                            |

## Usage
### Brewing ingredient
Nether wart's primary purpose is to brew the awkward potion, the base for all potions, but optional for Weakness.

| Name           | Ingredients              | Brewing recipe |
|----------------|--------------------------|----------------|
| Awkward Potion | Nether Wart+Water Bottle |                |

### Crafting ingredient
| Name              | Ingredients              | Crafting recipe | Description                                                             |
|-------------------|--------------------------|-----------------|-------------------------------------------------------------------------|
| Nether Wart Block | Nether Wart              |                 | The nether wart block cannot be crafted back into nether wart.[1][2][3] |
| Red Nether Bricks | Nether Wart+Nether Brick |                 |                                                                         |

### Trading
Master-level cleric villagers buy 22 nether warts for an emerald as part of their trades.

### Farming
Main article: Tutorials/Nether Wart farming
When planted on soul sand, nether wart grows through four stages, though the middle two stages use the same texture (the hitbox of stage 3 is three pixels taller). In Java Edition, the exact age can be seen using the debug screen, and the ages range from 0 to 3. Each random tick, nether wart has a 10% chance of growing one stage. At default random tick speed, each nether wart grows one age step approximately every 13653 game ticks (11.3775 minutes) on average, and fully grows from planting to harvest every 40960 game ticks (34.133333333333 minutes) on average. The growth rate is not affected by light or any other environmental factors. Bone meal cannot be used on the nether wart.

Nether wart can only be planted on soul sand. It cannot be planted on soul soil. It can grow in any dimension.

Nether wart is ready to harvest when it reaches its fourth stage (age:3). Breaking a fully grown nether wart drops 2 to 4 nether wart, while an immature one drops a single nether wart. Using a tool enchanted with fortune increases the maximum number of nether wart dropped by 1 per level, for a maximum of 7 for a tool enchanted with Fortune III.

### Composting
Placing a nether wart into a composter has a 30% chance of raising the compost level by 1.

Note that one should preferably not craft nether wart blocks for composting purposes. Using 9 nether warts gives more than 95% chance of raising the compost level, while using a nether wart block gives an 85% chance.

## Data values
### ID
Java Edition:

| Name        | Identifier  | Form         | Translation key                                       |
|-------------|-------------|--------------|-------------------------------------------------------|
| Nether Wart | nether_wart | Block & Item | block.minecraft.nether_wartitem.minecraft.nether_wart |

Bedrock Edition:

| Nether Wart | Identifier  | Numeric ID | Form                         | Item ID[i 1]     | Translation key       |
|-------------|-------------|------------|------------------------------|------------------|-----------------------|
| Block       | nether_wart | 115        | Block & Ungiveable Item[i 2] | item.nether_wart | tile.nether_wart.name |
| Item        | nether_wart | 294        | Item                         | —                | item.nether_wart.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Unavailable with /give command


### Block states
See also: Block states

| Name | Default value | Allowed values | Description  |
|------|---------------|----------------|--------------|
| age  | 0             | 0              |              |
|      |               | 12             |              |
|      |               | 3              | Fully grown. |

Bedrock Edition:

| Name | Metadata Bits | Default value | Allowed values     | Values forMetadata Bits | Description  |
|------|---------------|---------------|--------------------|-------------------------|--------------|
| age  | 0x10x2        | 0             | 0                  | 0                       |              |
|      |               |               | 12                 | 12                      |              |
|      |               |               | 3                  | 3                       | Fully grown. |
|      |               |               | 456789101112131415 | Unsupported             | Unused       |




