# Furnace
A furnace is a utility block used for the smelting of blocks and items.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Chest loot
	- 1.4 Crafting
- 2 Usage
	- 2.1 Smelting
	- 2.2 Light source
	- 2.3 Crafting ingredient
	- 2.4 Custom name
	- 2.5 Lock
	- 2.6 Note blocks
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
	- 4.3 Block data
- 5 Achievements
- 6 Advancements
- 7 History
	- 7.1 Lit furnace "item"
		- 7.1.1 Names
- 8 Issues
- 9 Trivia
- 10 Gallery
	- 10.1 Renders
		- 10.1.1 Java Edition
		- 10.1.2 Bedrock Edition
	- 10.2 Screenshots
	- 10.3 In other media
- 11 See also
- 12 References
- 13 External links

## Obtaining
### Breaking
A furnace can be mined using any pickaxe. A furnace also drops all of its contents when broken, including XP from smelting items that were extracted by hoppers.

In Java Edition, a furnace mined without a pickaxe drops nothing. In Bedrock Edition, a furnace drops itself when mined by hand or with any tool.

| Block     | Furnace               |
|-----------|-----------------------|
| Hardness  | 3.5                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 17.5                  |
| Wooden    | 2.65                  |
| Stone     | 1.35                  |
| Iron      | 0.9                   |
| Diamond   | 0.7                   |
| Netherite | 0.6                   |
| Golden    | 0.45                  |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Natural generation
Furnaces can be found in plains, desert, and some savanna village weaponsmiths. Furnaces also generate in some houses in snowy tundra villages, and in one of the taiga/snowy taiga‌[BE  only] village houses. They also appear in ancient cities and trail ruins, and one furnace generates in every igloo.

### Chest loot
| Item    | Structure | Container         | Quantity | Chance                         |
|---------|-----------|-------------------|----------|--------------------------------|
|         |           |                   |          | Java EditionandBedrock Edition |
| Furnace | Village   | Snowy house chest | 1        | 9.9%                           |

### Crafting
| Ingredients         | Crafting recipe | Description                                                 |
|---------------------|-----------------|-------------------------------------------------------------|
| Anystone-tier block |                 | Can use cobblestone and its other variants interchangeably. |

The lit furnace can be obtained in Java Edition only with commands such as /give @s minecraft:furnace{BlockStateTag:{lit:"true"}}, although it does not appear lit in the inventory. In Bedrock Edition, the lit furnace block can be obtained only by inventory editing. It always stays lit, despite containing no items.

## Usage
Furnaces cannot be pushed by pistons in Java Edition.

### Smelting
Main article: Smelting
Interface for the furnace.
The main purpose of a furnace is smelting. Its interface can be opened by pressing the use item button on it. A fuel source (up to one stack of fuel items) is placed in the lower slot, and the items (up to one stack) to be smelted are placed in the upper slot. A furnace smelts items at a speed of one item every 200 game ticks (10 seconds) or six items per minute.

The number of items that a fuel source can smelt depends on the type of fuel. As soon as smelting begins, the fuel slot is decremented immediately and that unit of fuel begins burning. The fuel continues burning until it is consumed, regardless of whether the upper slot has any items remaining to smelt. For example, a piece of coal burns for 80 seconds and can smelt eight items, but if only one item is smelted (or if the item is pulled out before smelting is complete), the coal still continues burning for the full 80 seconds, wasting seven items worth of smelting. After it burns out, no additional fuel is decremented from the fuel slot if the upper slot is empty. If the fuel slot is empty and the burning fuel is consumed before an item completes smelting, the smelting stops, the smelted item is unchanged, and smelting must be restarted with new fuel.

| Smelting recipe |
|-----------------|
|                 |

