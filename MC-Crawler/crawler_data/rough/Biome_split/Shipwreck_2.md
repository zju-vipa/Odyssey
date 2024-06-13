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


