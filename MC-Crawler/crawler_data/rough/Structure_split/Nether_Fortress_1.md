### Java Edition
In Java Edition, the spawning algorithm has two checks:

1. It checks if the spawn coordinates are within the "bounding box" of a single piece (e.g. corridor or walkway) of the fortress.(referred as "structure bounding box" above)In this case the block type of the ground does not matter.
2. It checks if the spawn coordinates are within the "bounding box"(referred as "area bounding box" above)of the entire fortress and whether the ground consists ofnether bricks.

If either check passes, it uses the special mob list for fortresses rather than the list for the biome when choosing the mob to spawn. The actual mob spawning proceeds as normal for the mob chosen from this list.

| Mob              | Spawn weight    | Group size       |
|------------------|-----------------|------------------|
|                  |                 | Monster category |
| Blaze            | $\frac{10}{28}$ | 2–3              |
| Wither Skeleton  | $\frac{8}{28}$  | 5                |
| Zombified Piglin | $\frac{5}{28}$  | 4                |
| Magma Cube       | $\frac{3}{28}$  | 4                |
| Skeleton         | $\frac{2}{28}$  | 5                |

{ "monster": { "mobs": [ { "size": "2&ndash;3", "mob": "Blaze", "weight": 10 }, { "size": "5", "mob": "Wither Skeleton", "weight": 8 }, { "size": "4", "mob": "Zombified Piglin", "weight": 5 }, { "size": "4", "mob": "Magma Cube", "weight": 3 }, { "size": "5", "mob": "Skeleton", "weight": 2 } ], "totalWeight": 28 } }
### Bedrock Edition
In Bedrock Edition, instead of spawning anywhere within a structural bounding box, most mobs spawn only in structure spawn locations along varied-length lines spaced apart 4-11 blocks throughout the fortress. They are not set to a particular Y level other than "inside the structure" and are indeed columns several blocks high. They do not require any special type of block, any regular spawnable block suffices. 

To identify these spawning columns, glass panes can be placed all over the fortress, 1 block above surface blocks. This keeps the mobs stationary. (This technique works in Bedrock due to mobs spawning in the northwest corner of blocks.) Note that these spots may be on top of the raised side blocks, so these side blocks have to be removed before a glass pane grid can be placed. 

Zombified Piglin spawns do not obey structure spawn locations; they can spawn anywhere in the fortress.

## Loot
See also: Chest loot

A chest that generated in a nether fortress.
Fortresses generate nether fortress loot with chests in the indoor sections placed at some corridor turns.

In Java Edition and Bedrock Edition, each nether fortress chest contains  items drawn from 2 pools,  with the following distribution: 

| Item                             | Stack Size  [A] |    | Weight   [B]    |                 | Chance   [C] | Avg.per chest   [D] | Avg. # cheststo search   [E] |
|----------------------------------|-----------------|----|-----------------|-----------------|--------------|---------------------|------------------------------|
|                                  | 2–4×            | 1× | 2–4×            | 1×              |              |                     |                              |
| Nothing[F]                       | —               | 1  | —               | $\frac{14}{15}$ | 93.3%        | 0.933               | 1.1                          |
| Gold Ingot                       | 1–3             | —  | $\frac{15}{73}$ | —               | 49.0%        | 1.233               | 2.0                          |
| Saddle                           | 1               | —  | $\frac{10}{73}$ | —               | 35.3%        | 0.411               | 2.8                          |
| Golden Horse Armor               | 1               | —  | $\frac{8}{73}$  | —               | 29.1%        | 0.329               | 3.4                          |
| Nether Wart                      | 3–7             | —  | $\frac{5}{73}$  | —               | 19.0%        | 1.027               | 5.3                          |
| Iron Ingot                       | 1–5             | —  | $\frac{5}{73}$  | —               | 19.0%        | 0.616               | 5.3                          |
| Diamond                          | 1–3             | —  | $\frac{5}{73}$  | —               | 19.0%        | 0.411               | 5.3                          |
| Flint and Steel                  | 1               | —  | $\frac{5}{73}$  | —               | 19.0%        | 0.205               | 5.3                          |
| Iron Horse Armor                 | 1               | —  | $\frac{5}{73}$  | —               | 19.0%        | 0.205               | 5.3                          |
| Golden Sword                     | 1               | —  | $\frac{5}{73}$  | —               | 19.0%        | 0.205               | 5.3                          |
| Golden Chestplate                | 1               | —  | $\frac{5}{73}$  | —               | 19.0%        | 0.205               | 5.3                          |
| Diamond Horse Armor              | 1               | —  | $\frac{3}{73}$  | —               | 11.8%        | 0.123               | 8.5                          |
| Obsidian                         | 2–4             | —  | $\frac{2}{73}$  | —               | 8.0%         | 0.247               | 12.5                         |
| Rib Armor Trim Smithing Template | —               | 1  | —               | $\frac{1}{15}$  | 6.7%         | 0.067               | 15.0                         |



↑ The size of stacks (or for unstackable items, number) of this item on any given roll.

↑ The weight of this item relative to other items in the pool.

↑ The odds of finding any of this item in a single chest.

↑ The number of items expected per chest, averaged over a large number of chests.

↑ The average number of chests the player should expect to search to find any of this item.

↑ 'Nothing' does not refer to the chance of an empty chest.  Instead, it refers to the chance that the random loot generator does not add any loot on a single roll.



## Data values
### ID
Java Edition:

| Structure type  | Identifier |
|-----------------|------------|
| Nether Fortress | `fortress` |

| Structure       | Identifier |
|-----------------|------------|
| Nether Fortress | `fortress` |

Bedrock Edition:

| Structure       | Identifier | Translation key    |
|-----------------|------------|--------------------|
| Nether Fortress | `fortress` | `feature.fortress` |

### Config
Java Edition:

- Structure configuration
	- type:minecraft:fortress
	- 
	- Fields common to all structures


