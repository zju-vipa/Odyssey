# Shipwreck
A shipwreck is a structure found in oceanic biomes that resembles a sunken sailing ship.

## Contents
- 1 Generation
- 2 Structure
- 3 Loot
	- 3.1 Supply chests
	- 3.2 Treasure chests
	- 3.3 Map chests
- 4 Data values
	- 4.1 ID
	- 4.2 Config
- 5 Achievements
- 6 History
- 7 Issues
- 8 Gallery
	- 8.1 Screenshots
- 9 References

## Generation
Shipwrecks generate in all ocean biomes rarely. On rarer occasions, they generate above sea level nearby the water, in beaches, snowy beaches or inside an iceberg,[1] underwater ruin, monument or ravine.

## Structure
Main article: Shipwreck/Structure
Shipwrecks generate in one of three ways: upright, keeled sideways or upside-down. In many cases, they are missing their bow (front) or stern (rear), mast or multiple other blocks, giving them a damaged appearance; however, it is also possible, but rare, to find them completely intact. They consist solely of wooden materials, including logs‌[JE  only]/stripped logs‌[BE  only], planks, fences, slabs, stairs, trapdoors, a door (if the ship is upright), and up to 3 chests, depending on rotation and intact sections of the ship. The bow is supposed to generate one chest (unless upside-down) while the stern should generate two, and the whole ship generates a maximum of three chests, regardless of the ship's rotation or condition. However, there are some instances in which chests that usually generate in a shipwreck section are missing. Only two wood types are used per ship (one is the primary type, which is used by the logs and exterior, and the other the secondary type), but only 8‌[JE  only] combinations are possible: Primary dark oak with secondary jungle and spruce, primary jungle with secondary spruce, primary oak with secondary birch and spruce, primary spruce with secondary dark oak, jungle, and oak. Acacia is a possible secondary type on bedrock edition.

| Structure name                             | Description                                                                                                 | Consists of                                                                                                                                                          | Images |
|--------------------------------------------|-------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| `shipwreck/rightsideup_backhalf`           | The stern of a ship, upright, intact.                                                                       | 166 Oak Planks 112 Oak Stairs 67 Spruce Planks 20 Spruce Slab 15 Spruce Fence 13 Spruce Stairs 6 Oak Fence 4 Oak Log 3 Oak Trapdoor 2 Oak Slab 2 Chest 1 Oak Door    |        |
| `shipwreck/rightsideup_backhalf_degraded`  | The stern of a ship, upright, with a degraded appearance.                                                   | 153 Oak Planks 109 Oak Stairs 59 Spruce Planks 20 Spruce Slab 14 Spruce Fence 10 Spruce Stairs 6 Oak Fence 4 Oak Log 4 Oak Slab 2 Oak Trapdoor 2 Chest 1 Oak Door    |        |
| `shipwreck/rightsideup_fronthalf`          | The bow of a ship, upright, intact.                                                                         | 128 Oak Planks 108 Oak Stairs 58 Spruce Planks 20 Spruce Stairs 18 Spruce Fence 11 Oak Trapdoor 8 Oak Log 1 Chest 1 Oak Door                                         |        |
| `shipwreck/rightsideup_fronthalf_degraded` | The bow of a ship, upright, with a degraded appearance.                                                     | 111 Oak Planks 100 Oak Stairs 44 Spruce Planks 12 Spruce Stairs 10 Spruce Fence 11 Oak Trapdoor 7 Oak Log 1 Chest 1 Oak Door                                         |        |
| `shipwreck/rightsideup_full`               | A whole ship, upright, intact.                                                                              | 252 Oak Planks 178 Oak Stairs 104 Spruce Planks 31 Spruce Fence 31 Spruce Slab 26 Spruce Stairs 14 Oak Trapdoor 10 Oak Log 6 Oak Fence 3 Chest 2 Oak Slab 1 Oak Door |        |
| `shipwreck/rightsideup_full_degraded`      | A whole ship, upright, with a degraded appearance.                                                          | 243 Oak Planks 171 Oak Stairs 89 Spruce Planks 31 Spruce Slab 27 Spruce Fence 23 Spruce Stairs 10 Oak Log 9 Oak Trapdoor 6 Oak Fence 3 Chest 2 Oak Slab 1 Oak Door   |        |
| `shipwreck/sideways_backhalf`              | The stern of a ship, capsized, intact.                                                                      | 143 Oak Planks 105 Oak Stairs 101 Spruce Planks 10 Spruce Fence 6 Oak Fence 5 Spruce Stairs 4 Oak Log 3 Oak Trapdoor 2 Chest                                         |        |
| `shipwreck/sideways_backhalf_degraded`     | The stern of a ship, capsized, with a degraded appearance.                                                  | 123 Oak Planks 99 Oak Stairs 88 Spruce Planks 10 Spruce Fence 6 Oak Fence 4 Oak Log 3 Oak Trapdoor 3 Spruce Stairs 2 Chest                                           |        |
| `shipwreck/sideways_fronthalf`             | The bow of a ship, capsized, intact.                                                                        | 117 Oak Planks 104 Oak Stairs 60 Spruce Planks 13 Spruce Stairs 11 Spruce Fence 7 Oak Log 7 Oak Trapdoor 1 Chest                                                     |        |
| `shipwreck/sideways_fronthalf_degraded`    | The bow of a ship, capsized, with a degraded appearance.                                                    | 83 Oak Planks 81 Oak Stairs 46 Spruce Planks 13 Spruce Stairs 8 Spruce Fence 7 Oak Trapdoor 6 Oak Log 1 Chest                                                        |        |
| `shipwreck/sideways_full`                  | A whole ship, capsized, intact.                                                                             | 223 Oak Planks 171 Oak Stairs 159 Spruce Planks 30 Spruce Fence 22 Spruce Stairs 14 Oak Trapdoor 10 Oak Log 6 Oak Fence 3 Chest                                      |        |
| `shipwreck/sideways_full_degraded`         | A whole ship, capsized, with a degraded appearance.                                                         | 206 Oak Planks 150 Spruce Planks 149 Oak Stairs 24 Spruce Fence 21 Spruce Stairs 11 Oak Trapdoor 10 Oak Log 6 Oak Fence 3 Chest                                      |        |
| `shipwreck/upsidedown_backhalf`            | The stern of a ship, turtled, intact.                                                                       | 176 Oak Planks 107 Oak Stairs 60 Spruce Planks 10 Spruce Fence 10 Spruce Stairs 7 Spruce Slab 4 Oak Trapdoor 4 Oak Log 3 Oak Slab 2 Oak Fence 2 Chest                |        |
| `shipwreck/upsidedown_backhalf_degraded`   | The stern of a ship, turtled, with a degraded appearance.                                                   | 167 Oak Planks 98 Oak Stairs 55 Spruce Planks 10 Spruce Fence 8 Spruce Stairs 7 Spruce Slab 4 Oak Trapdoor 4 Oak Log 3 Oak Slab 2 Oak Fence 2 Chest                  |        |
| `shipwreck/upsidedown_fronthalf`           | The bow of a ship, turtled, intact.                                                                         | 123 Oak Planks 93 Oak Stairs 60 Spruce Planks 21 Spruce Stairs 14 Oak Trapdoor 9 Oak Log 8 Spruce Fence 2 Chest                                                      |        |
| `shipwreck/upsidedown_fronthalf_degraded`  | The bow of a ship, turtled, with a degraded appearance.                                                     | 112 Oak Planks 82 Oak Stairs 54 Spruce Planks 20 Spruce Stairs 11 Oak Trapdoor 9 Oak Log 8 Spruce Fence 2 Chest                                                      |        |
| `shipwreck/upsidedown_full`                | A whole ship, turtled, intact.                                                                              | 219 Oak Planks 153 Oak Stairs 116 Spruce Planks 30 Spruce Fence 28 Spruce Stairs 19 Spruce Slab 14 Oak Trapdoor 10 Oak Log 4 Oak Fence 3 Chest 2 Oak Slab            |        |
| `shipwreck/upsidedown_full_degraded`       | A whole ship, turtled, with a degraded appearance.                                                          | 194 Oak Planks 133 Oak Stairs 109 Spruce Planks 28 Spruce Stairs 27 Spruce Fence 19 Spruce Slab 14 Oak Trapdoor 10 Oak Log 4 Oak Fence 3 Chest 2 Oak Slab            |        |
| `shipwreck/with_mast`                      | The most complete shipwreck structure. A whole ship, upright, with all components, and three masts, intact. | 209 Oak Planks 182 Oak Stairs 108 Spruce Planks 70 Spruce Slab 67 Oak Log 35 Spruce Fence 24 Spruce Stairs 16 Oak Trapdoor 6 Oak Fence 4 Oak Slab 3 Chest 1 Oak Door |        |
| `shipwreck/with_mast_degraded`             | A whole ship, upright, with all components, three masts, and a degraded appearance.                         | 201 Oak Planks 172 Oak Stairs 107 Spruce Planks 63 Spruce Slab 28 Spruce Fence 24 Oak Log 23 Spruce Stairs 16 Oak Trapdoor 6 Oak Fence 4 Oak Slab 3 Chest 1 Oak Door |        |

## Loot
Internal structure of a whole shipwreck.
See also: Chest loot

Shipwrecks contain up to 3 loot chests, depending on the sections still intact. Supply chests generate in the bow of the ships, treasure chests generate in the upper section of the stern, and map chests in the lower section. In the case of certain shipwrecks, especially those that intersect other structures, the chests that would normally be present in the corresponding section may be absent, resulting in some shipwrecks holding no chests at all. Although chests don't usually generate for missing sections, map chests from shipwreck sterns may generate in upside-down bows even if the stern is missing. Furthermore, each shipwreck with at least 2 chests always contains its map chest.

### Supply chests
In Java Edition and Bedrock Edition, each shipwreck supply chest contains  items drawn from 2 pools,  with the following distribution: 

| Item                               | Stack Size  [A] |    | Weight   [B]    |               | Chance   [C] | Avg.per chest   [D] | Avg. # cheststo search   [E] |
|------------------------------------|-----------------|----|-----------------|---------------|--------------|---------------------|------------------------------|
|                                    | 3–10×           | 1× | 3–10×           | 1×            |              |                     |                              |
| Nothing[F]                         | —               | 1  | —               | $\frac{5}{6}$ | 83.3%        | 0.833               | 1.2                          |
| Suspicious Stew[G]                 | 1               | —  | $\frac{10}{84}$ | —             | 54.3%        | 0.774               | 1.8                          |
| Paper                              | 1–12            | —  | $\frac{8}{84}$  | —             | 46.4%        | 4.024               | 2.2                          |
| Wheat                              | 8–21            | —  | $\frac{7}{84}$  | —             | 42.1%        | 7.854               | 2.4                          |
| Carrot                             | 4–8             | —  | $\frac{7}{84}$  | —             | 42.1%        | 3.250               | 2.4                          |
| Poisonous Potato                   | 2–6             | —  | $\frac{7}{84}$  | —             | 42.1%        | 2.167               | 2.4                          |
| Potato                             | 2–6             | —  | $\frac{7}{84}$  | —             | 42.1%        | 2.167               | 2.4                          |
| Moss Block                         | 1–4             | —  | $\frac{7}{84}$  | —             | 42.1%        | 1.354               | 2.4                          |
| Coal                               | 2–8             | —  | $\frac{6}{84}$  | —             | 37.3%        | 2.321               | 2.7                          |
| Rotten Flesh                       | 5–24            | —  | $\frac{5}{84}$  | —             | 32.2%        | 5.610               | 3.1                          |
| Gunpowder                          | 1–5             | —  | $\frac{3}{84}$  | —             | 20.8%        | 0.696               | 4.8                          |
| Enchanted Leather Cap[H]           | 1               | —  | $\frac{3}{84}$  | —             | 20.8%        | 0.232               | 4.8                          |
| Enchanted Leather Tunic[H]         | 1               | —  | $\frac{3}{84}$  | —             | 20.8%        | 0.232               | 4.8                          |
| Enchanted Leather Pants[H]         | 1               | —  | $\frac{3}{84}$  | —             | 20.8%        | 0.232               | 4.8                          |
| Enchanted Leather Boots[H]         | 1               | —  | $\frac{3}{84}$  | —             | 20.8%        | 0.232               | 4.8                          |
| Coast Armor Trim Smithing Template | —               | 2  | —               | $\frac{1}{6}$ | 16.7%        | 0.333               | 6.0                          |
| Bamboo                             | 1–3             | —  | $\frac{2}{84}$  | —             | 14.4%        | 0.310               | 7.0                          |
| Pumpkin                            | 1–3             | —  | $\frac{2}{84}$  | —             | 14.4%        | 0.310               | 7.0                          |
| TNT                                | 1–2             | —  | $\frac{1}{84}$  | —             | 7.5%         | 0.116               | 13.4                         |



↑ The size of stacks (or for unstackable items, number) of this item on any given roll.

↑ The weight of this item relative to other items in the pool.

↑ The odds of finding any of this item in a single chest.

↑ The number of items expected per chest, averaged over a large number of chests.

↑ The average number of chests the player should expect to search to find any of this item.

↑ 'Nothing' does not refer to the chance of an empty chest.  Instead, it refers to the chance that the random loot generator does not add any loot on a single roll.

↑ The stew grants one of the following effects: 5–7 seconds of Blindness, 7–10 seconds of Jump Boost, 7-10 seconds of Night Vision, 10–20 seconds of Poison, 0.35-0.5 seconds of Saturation, or 6–8 seconds of Weakness.

↑ a b c d All enchantments are equally probable, including treasure enchantments (except Soul Speed, and Swift Sneak), and any level of the enchantment is equally probable.





### Treasure chests
In Java Edition and Bedrock Edition, each shipwreck treasure chest contains  items drawn from 3 pools,  with the following distribution: 

| Item                               | Stack Size  [A] |      |    | Weight   [B]     |                 |               | Chance   [C] | Avg.per chest   [D] | Avg. # cheststo search   [E] |
|------------------------------------|-----------------|------|----|------------------|-----------------|---------------|--------------|---------------------|------------------------------|
|                                    | 3–6×            | 2–5× | 1× | 3–6×             | 2–5×            | 1×            |              |                     |                              |
| Iron Ingot                         | 1–5             | —    | —  | $\frac{90}{150}$ | —               | —             | 97.4%        | 8.100               | 1.0                          |
| Iron Nugget                        | —               | 1–10 | —  | —                | $\frac{50}{80}$ | —             | 94.5%        | 12.031              | 1.1                          |
| Nothing[F]                         | —               | —    | 1  | —                | —               | $\frac{5}{6}$ | 83.3%        | 0.833               | 1.2                          |
| Emerald                            | 1–5             | —    | —  | $\frac{40}{150}$ | —               | —             | 73.7%        | 3.600               | 1.4                          |
| Lapis Lazuli                       | —               | 1–10 | —  | —                | $\frac{20}{80}$ | —             | 61.5%        | 4.812               | 1.6                          |
| Gold Nugget                        | —               | 1–10 | —  | —                | $\frac{10}{80}$ | —             | 36.6%        | 2.406               | 2.7                          |
| Gold Ingot                         | 1–5             | —    | —  | $\frac{10}{150}$ | —               | —             | 26.5%        | 0.900               | 3.8                          |
| Coast Armor Trim Smithing Template | —               | —    | 2  | —                | —               | $\frac{1}{6}$ | 16.7%        | 0.333               | 6.0                          |
| Bottle o' Enchanting               | 1               | —    | —  | $\frac{5}{150}$  | —               | —             | 14.1%        | 0.150               | 7.1                          |
| Diamond                            | 1               | —    | —  | $\frac{5}{150}$  | —               | —             | 14.1%        | 0.150               | 7.1                          |



↑ The size of stacks (or for unstackable items, number) of this item on any given roll.

↑ The weight of this item relative to other items in the pool.

↑ The odds of finding any of this item in a single chest.

↑ The number of items expected per chest, averaged over a large number of chests.

↑ The average number of chests the player should expect to search to find any of this item.

↑ 'Nothing' does not refer to the chance of an empty chest.  Instead, it refers to the chance that the random loot generator does not add any loot on a single roll.



### Map chests
In Java Edition, each shipwreck map chest contains  items drawn from 3 pools,  with the following distribution: 

| Item                               | Stack Size  [A] |      |    | Weight   [B]  |                 |               | Chance   [C] | Avg.per chest   [D] | Avg. # cheststo search   [E] |
|------------------------------------|-----------------|------|----|---------------|-----------------|---------------|--------------|---------------------|------------------------------|
|                                    | 1×              | 3×   | 1× | 1×            | 3×              | 1×            |              |                     |                              |
| Buried Treasure Map                | 1               | —    | —  | $\frac{1}{1}$ | —               | —             | 100.0%       | 1.000               | 1.0                          |
| Paper                              | —               | 1–10 | —  | —             | $\frac{20}{38}$ | —             | 89.4%        | 8.684               | 1.1                          |
| Nothing[F]                         | —               | —    | 1  | —             | —               | $\frac{5}{6}$ | 83.3%        | 0.833               | 1.2                          |
| Feather                            | —               | 1–5  | —  | —             | $\frac{10}{38}$ | —             | 60.0%        | 2.368               | 1.7                          |
| Book                               | —               | 1–5  | —  | —             | $\frac{5}{38}$  | —             | 34.5%        | 1.184               | 2.9                          |
| Coast Armor Trim Smithing Template | —               | —    | 2  | —             | —               | $\frac{1}{6}$ | 16.7%        | 0.333               | 6.0                          |
| Clock                              | —               | 1    | —  | —             | $\frac{1}{38}$  | —             | 7.7%         | 0.079               | 13.0                         |
| Compass                            | —               | 1    | —  | —             | $\frac{1}{38}$  | —             | 7.7%         | 0.079               | 13.0                         |
| Empty Map                          | —               | 1    | —  | —             | $\frac{1}{38}$  | —             | 7.7%         | 0.079               | 13.0                         |

In Bedrock Edition, each shipwreck map chest contains  items drawn from 3 pools,  with the following distribution: 

| Item                               | Stack Size  [A] |      |    | Weight   [B]  |                 |               | Chance   [C] | Avg.per chest   [D] | Avg. # cheststo search   [E] |
|------------------------------------|-----------------|------|----|---------------|-----------------|---------------|--------------|---------------------|------------------------------|
|                                    | 1×              | 3×   | 1× | 1×            | 3×              | 1×            |              |                     |                              |
| Buried Treasure Map                | 1               | —    | —  | $\frac{1}{1}$ | —               | —             | 100.0%       | 1.000               | 1.0                          |
| Paper                              | —               | 1–10 | —  | —             | $\frac{20}{38}$ | —             | 89.4%        | 8.684               | 1.1                          |
| Nothing[F]                         | —               | —    | 1  | —             | —               | $\frac{5}{6}$ | 83.3%        | 0.833               | 1.2                          |
| Feather                            | —               | 1–5  | —  | —             | $\frac{10}{38}$ | —             | 60.0%        | 2.368               | 1.7                          |
| Book                               | —               | 1–5  | —  | —             | $\frac{5}{38}$  | —             | 34.5%        | 1.184               | 2.9                          |
| Coast Armor Trim Smithing Template | —               | —    | 2  | —             | —               | $\frac{1}{6}$ | 16.7%        | 0.333               | 6.0                          |
| Clock                              | —               | 1    | —  | —             | $\frac{1}{38}$  | —             | 7.7%         | 0.079               | 13.0                         |
| Compass                            | —               | 1    | —  | —             | $\frac{1}{38}$  | —             | 7.7%         | 0.079               | 13.0                         |
| Map[G]                             | —               | 1    | —  | —             | $\frac{1}{38}$  | —             | 7.7%         | 0.079               | 13.0                         |



↑ a b The size of stacks (or for unstackable items, number) of this item on any given roll.

↑ a b The weight of this item relative to other items in the pool.

↑ a b The odds of finding any of this item in a single chest.

↑ a b The number of items expected per chest, averaged over a large number of chests.

↑ a b The average number of chests the player should expect to search to find any of this item.

↑ a b 'Nothing' does not refer to the chance of an empty chest.  Instead, it refers to the chance that the random loot generator does not add any loot on a single roll.

↑ Named unknown map, but changed to map 0, the scale level is 1:4, Maps from the same stack are stackable, but maps that are not stacked are unstackable despite looking identical.





## Data values
### ID
Java Edition:

| Structure type | Identifier  |
|----------------|-------------|
| Shipwreck      | `shipwreck` |

| Structure         | Identifier          |
|-------------------|---------------------|
| Shipwreck         | `shipwreck`         |
| Beached Shipwreck | `shipwreck_beached` |

Bedrock Edition:

| Structure | Identifier  | Translation key     |
|-----------|-------------|---------------------|
| Shipwreck | `shipwreck` | `feature.shipwreck` |

### Config
Java Edition:

- Structure configuration
	- type:minecraft:shipwreck
	- 
	- Fields common to all structures
	- is_beached: (optional, defaults to false) Whether or not the shipwreck is beached.

