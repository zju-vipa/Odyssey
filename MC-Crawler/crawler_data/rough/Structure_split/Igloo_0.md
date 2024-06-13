# Igloo
An igloo is a hostel structure sometimes generated in snowy taigas, snowy plains or snowy slopes and built mainly of snow blocks.

## Contents
- 1 Structure
- 2 Loot
- 3 Data values
	- 3.1 ID
	- 3.2 Config
- 4 History
- 5 Issues
- 6 Trivia
- 7 Gallery
	- 7.1 Screenshots
- 8 References

## Structure
Main article: /Structure
Igloos are shaped like a small dwelling made of snow blocks, with an entrance but lacking a door, with a carpeted interior having a bed, furnace and crafting table. There are two windows made of ice blocks, and one redstone torch as a light source that does not melt the ice as a torch would.

Half of all igloos have an oak trapdoor under the third carpet from the doorway, leading down a long ladder shaft to a basement. This passageway and the basement are built from stone bricks, some of which are infested blocks with silverfish. To the left from the ladder is a table made of stairs blocks, with a brewing stand containing one splash potion weakness, and a flower pot holding a cactus. Beside the table is a cauldron, two-thirds full of water. To the right there is a chest that includes a golden apple. Beyond the far wall, behind iron bars in two different cages, are a villager and a zombie villager.[1]

Igloos that generate without a basement have a snow block in place of the trapdoor. The villagers, the brewing stand and the chest are absent in this case.

** Mobs **
|          |                 |
|----------|-----------------|
| Villager | Zombie Villager |

In Java Edition, the generated villager is always unemployed, and is a plains biome type.[2] The villager cannot pathfind to the brewing stand or cauldron to take on a profession unless some of the blocks confining them are broken. The generated zombie villager always has the profession of cleric, becoming unemployed if cured.

In Bedrock Edition, the villager is the snowy type with a random profession while the zombie villager is unemployed; although it can change its profession to cleric or leatherworker after being cured, due to the presence of the brewing stand and cauldron.

One may access the individual structures of an igloo by using structure blocks to manually load them from the /data/minecraft/structures/igloo folder in version.jar. To do so, set a structure block to Load mode, enter igloo/structure name, and press [LOAD].  The individual structures are bottom, middle, top.

| Structure name | Description                                                                                                        | Consists of                                                                                                                                                                                                                                                                                                                                                                                                                             | Images |
|----------------|--------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| `igloo/top`    | The above-ground room of the igloo, made of snow blocks.                                                           | 94 Snow Block 9 White Carpet 3 Light Gray Carpet 2 Ice 1 Crafting Table 1 Furnace 1 Oak Trapdoor 1 Red Bed 1 Redstone Torch                                                                                                                                                                                                                                                                                                             |        |
| `igloo/middle` | The stone tunnel that connects the room above with the basement.                                                   | 12 Stone Bricks 3 Ladder                                                                                                                                                                                                                                                                                                                                                                                                                |        |
| `igloo/bottom` | The basement, made of various stone blocks and infested stone blocks, containing a villager and a zombie villager. | 104 Stone Bricks 17 Mossy Stone Bricks 11 Stone 8 Cracked Stone Bricks 7 Chiseled Stone Bricks 6 Infested Stone Bricks 4 Iron Bars 4 Ladder 3 Torch 2 Infested Chiseled Stone Bricks 2 Red Carpet 2 Spruce Stairs 1 Infested Mossy Stone Bricks 1 Polished Andesite 1 Cauldron 1 Chest (1 Golden Apple) 1 Cobweb 1 Potted Cactus 1 Oak Sign 1 Spruce Slab 1 Brewing Stand with a Splash Potion of Weakness 1 Villager 1 Zombie Villager |        |

## Loot
See also: Chest loot

In Java Edition and Bedrock Edition, each igloo chest contains  items drawn from 2 pools,  with the following distribution: 

| Item         | Stack Size  [A] |    | Weight   [B]    |               | Chance   [C] | Avg.per chest   [D] | Avg. # cheststo search   [E] |
|--------------|-----------------|----|-----------------|---------------|--------------|---------------------|------------------------------|
|              | 2–8×            | 1× | 2–8×            | 1×            |              |                     |                              |
| Golden Apple | —               | 1  | —               | $\frac{1}{1}$ | 100.0%       | 1.000               | 1.0                          |
| Coal         | 1–4             | —  | $\frac{15}{63}$ | —             | 70.4%        | 2.976               | 1.4                          |
| Apple        | 1–3             | —  | $\frac{15}{63}$ | —             | 70.4%        | 2.381               | 1.4                          |
| Wheat        | 2–3             | —  | $\frac{10}{63}$ | —             | 55.3%        | 1.984               | 1.8                          |
| Gold Nugget  | 1–3             | —  | $\frac{10}{63}$ | —             | 55.3%        | 1.587               | 1.8                          |
| Rotten Flesh | 1               | —  | $\frac{10}{63}$ | —             | 55.3%        | 0.794               | 1.8                          |
| Stone Axe    | 1               | —  | $\frac{2}{63}$  | —             | 14.7%        | 0.159               | 6.8                          |
| Emerald      | 1               | —  | $\frac{1}{63}$  | —             | 7.6%         | 0.079               | 13.1                         |



↑ The size of stacks (or for unstackable items, number) of this item on any given roll.

↑ The weight of this item relative to other items in the pool.

↑ The odds of finding any of this item in a single chest.

↑ The number of items expected per chest, averaged over a large number of chests.

↑ The average number of chests the player should expect to search to find any of this item.



## Data values
### ID
Java Edition:

| Structure type | Identifier |
|----------------|------------|
| Igloo          | `igloo`    |

| Structure | Identifier |
|-----------|------------|
| Igloo     | `igloo`    |

Bedrock Edition:

| Structure | Identifier | Translation key  |
|-----------|------------|------------------|
| Temple    | `temple`   | `feature.temple` |

### Config
Java Edition:

- Structure configuration
	- type:minecraft:igloo
	- 
	- Fields common to all structures


