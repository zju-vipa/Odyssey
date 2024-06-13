# Bonus Chest
The bonus chest is a feature that appears near the player's spawn if the "Bonus Chest" option is toggled on the "Create New World" screen. It generates with a semi-random collection of basic items to help the player survive early on and gather necessary resources, including tools, blocks, and food.

## Contents
- 1 Generation
- 2 Construction
- 3 Loot
- 4 Data values
	- 4.1 ID
	- 4.2 Config
- 5 History
- 6 Issues

## Generation
If the "Bonus Chest" option is set to "ON" in the "More World Options..." in Java Edition or "Game Settings" in Bedrock Edition part of the "Create New World" screen, a single bonus chest is generated in the world, no matter how many players there are. It appears somewhere near the player's initial spawn point, with up to four torches generated around it on adjacent blocks. It always generates on the highest block, and cannot generate naturally nor with the /place command if it reaches the build limit.

The Bonus Chest option is not available in hardcore mode, thus making the bonus chest unavailable as well.

In Java Edition, on servers, the bonus chest can be enabled by running the server with the --bonusChest argument.

## Construction
Bonus chests contain a single chest surrounded by four torches. The torches may be overridden if the torch locations are obstructed by other blocks such as uneven ground, trees, or leaves, or they may instead float.

|  |  |  |
|--|--|--|
|  |  |  |
|  |  |  |

## Loot



Chest24Inventory

Example of loot in a bonus chest.


In Java Edition, each bonus chest contains  items drawn from 4 pools,  with the following distribution: 

| Item           | Stack Size  [A] |    |     |      | Weight   [B]  |               |                |                 | Chance   [C] | Avg.per chest   [D] | Avg. # cheststo search   [E] |
|----------------|-----------------|----|-----|------|---------------|---------------|----------------|-----------------|--------------|---------------------|------------------------------|
|                | 1×              | 1× | 3×  | 4×   | 1×            | 1×            | 3×             | 4×              |              |                     |                              |
| Apple          | —               | —  | 1–2 | —    | —             | —             | $\frac{5}{11}$ | —               | 83.8%        | 2.045               | 1.2                          |
| Wooden Axe     | 1               | —  | —   | —    | $\frac{3}{4}$ | —             | —              | —               | 75.0%        | 0.750               | 1.3                          |
| Wooden Pickaxe | —               | 1  | —   | —    | —             | $\frac{3}{4}$ | —              | —               | 75.0%        | 0.750               | 1.3                          |
| Oak Planks     | —               | —  | —   | 1–12 | —             | —             | —              | $\frac{10}{41}$ | 67.3%        | 6.341               | 1.5                          |
| Stick          | —               | —  | —   | 1–12 | —             | —             | —              | $\frac{10}{41}$ | 67.3%        | 6.341               | 1.5                          |
| Bread          | —               | —  | 1–2 | —    | —             | —             | $\frac{3}{11}$ | —               | 61.5%        | 1.227               | 1.6                          |
| Raw Salmon     | —               | —  | 1–2 | —    | —             | —             | $\frac{3}{11}$ | —               | 61.5%        | 1.227               | 1.6                          |
| Acacia Log     | —               | —  | —   | 1–3  | —             | —             | —              | $\frac{3}{41}$  | 26.2%        | 0.585               | 3.8                          |
| Birch Log      | —               | —  | —   | 1–3  | —             | —             | —              | $\frac{3}{41}$  | 26.2%        | 0.585               | 3.8                          |
| Dark Oak Log   | —               | —  | —   | 1–3  | —             | —             | —              | $\frac{3}{41}$  | 26.2%        | 0.585               | 3.8                          |
| Jungle Log     | —               | —  | —   | 1–3  | —             | —             | —              | $\frac{3}{41}$  | 26.2%        | 0.585               | 3.8                          |
| Mangrove Log   | —               | —  | —   | 1–3  | —             | —             | —              | $\frac{3}{41}$  | 26.2%        | 0.585               | 3.8                          |
| Oak Log        | —               | —  | —   | 1–3  | —             | —             | —              | $\frac{3}{41}$  | 26.2%        | 0.585               | 3.8                          |
| Spruce Log     | —               | —  | —   | 1–3  | —             | —             | —              | $\frac{3}{41}$  | 26.2%        | 0.585               | 3.8                          |
| Stone Axe      | 1               | —  | —   | —    | $\frac{1}{4}$ | —             | —              | —               | 25.0%        | 0.250               | 4.0                          |
| Stone Pickaxe  | —               | 1  | —   | —    | —             | $\frac{1}{4}$ | —              | —               | 25.0%        | 0.250               | 4.0                          |



↑ The size of stacks (or for unstackable items, number) of this item on any given roll.

↑ The weight of this item relative to other items in the pool.

↑ The odds of finding any of this item in a single chest.

↑ The number of items expected per chest, averaged over a large number of chests.

↑ The average number of chests the player should expect to search to find any of this item.



In Bedrock Edition, each bonus chest contains  items drawn from 14 pools,  with the following distribution: 

| Item             | Chance   [A] | Avg.per chest   [B] | Avg. # cheststo search   [C] |
|------------------|--------------|---------------------|------------------------------|
| Oak Planks       | 100.0%       | 6.500               | 1.0                          |
| Stick            | 100.0%       | 6.500               | 1.0                          |
| Apple            | 100.0%       | 1.500               | 1.0                          |
| Bread            | 100.0%       | 1.500               | 1.0                          |
| Brown Mushroom   | 100.0%       | 1.500               | 1.0                          |
| Raw Salmon       | 100.0%       | 1.500               | 1.0                          |
| Wooden Axe       | 75.0%        | 0.750               | 1.3                          |
| Wooden Pickaxe   | 75.0%        | 0.750               | 1.3                          |
| Cactus           | 60.0%        | 0.900               | 1.7                          |
| Acacia Log       | 50.0%        | 1.000               | 2.0                          |
| Dark Oak Log     | 50.0%        | 1.000               | 2.0                          |
| Carrot           | 50.0%        | 0.750               | 2.0                          |
| Potato           | 50.0%        | 0.750               | 2.0                          |
| Cocoa Beans      | 40.0%        | 0.600               | 2.5                          |
| Beetroot Seeds   | 33.3%        | 0.500               | 3.0                          |
| Melon Seeds      | 33.3%        | 0.500               | 3.0                          |
| Pumpkin Seeds    | 33.3%        | 0.500               | 3.0                          |
| Jungle Sapling   | 28.6%        | 1.143               | 3.5                          |
| Birch Log        | 25.0%        | 0.500               | 4.0                          |
| Jungle Log       | 25.0%        | 0.500               | 4.0                          |
| Oak Log          | 25.0%        | 0.500               | 4.0                          |
| Spruce Log       | 25.0%        | 0.500               | 4.0                          |
| Stone Axe        | 25.0%        | 0.250               | 4.0                          |
| Stone Pickaxe    | 25.0%        | 0.250               | 4.0                          |
| Acacia Sapling   | 14.3%        | 0.571               | 7.0                          |
| Birch Sapling    | 14.3%        | 0.571               | 7.0                          |
| Dark Oak Sapling | 14.3%        | 0.571               | 7.0                          |
| Oak Sapling      | 14.3%        | 0.571               | 7.0                          |
| Spruce Sapling   | 14.3%        | 0.571               | 7.0                          |



↑ The odds of finding any of this item in a single chest.

↑ The number of items expected per chest, averaged over a large number of chests.

↑ The average number of chests the player should expect to search to find any of this item.



## Data values
### ID
Java Edition:

| Feature type        | Identifier    |
|---------------------|---------------|
| [No displayed name] | `bonus_chest` |

| Configured feature  | Identifier    |
|---------------------|---------------|
| [No displayed name] | `bonus_chest` |

Bedrock Edition:

| Feature             | Identifier |
|---------------------|------------|
| [No displayed name] | `[No ID]`  |

### Config
Main article: Configured feature
Java Edition:

- config: Empty


An example

{
  "type": "minecraft:bonus_chest",
  "config": {}
}



