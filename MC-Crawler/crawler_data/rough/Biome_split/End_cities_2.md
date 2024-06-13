## Loot
See also: Chest loot

In Java Edition and Bedrock Edition, each end city chest contains  items drawn from 2 pools,  with the following distribution: 

| Item                               | Stack Size  [A] |    | Weight   [B]    |                 | Chance   [C] | Avg.per chest   [D] | Avg. # cheststo search   [E] |
|------------------------------------|-----------------|----|-----------------|-----------------|--------------|---------------------|------------------------------|
|                                    | 2–6×            | 1× | 2–6×            | 1×              |              |                     |                              |
| Nothing[F]                         | —               | 1  | —               | $\frac{14}{15}$ | 93.3%        | 0.933               | 1.1                          |
| Gold Ingot                         | 2–7             | —  | $\frac{15}{85}$ | —               | 52.3%        | 3.176               | 1.9                          |
| Iron Ingot                         | 4–8             | —  | $\frac{10}{85}$ | —               | 38.4%        | 2.824               | 2.6                          |
| Beetroot Seeds                     | 1–10            | —  | $\frac{5}{85}$  | —               | 21.2%        | 1.294               | 4.7                          |
| Diamond                            | 2–7             | —  | $\frac{5}{85}$  | —               | 21.2%        | 1.059               | 4.7                          |
| Saddle                             | 1               | —  | $\frac{3}{85}$  | —               | 13.3%        | 0.141               | 7.5                          |
| Enchanted Iron Pickaxe[G]          | 1               | —  | $\frac{3}{85}$  | —               | 13.3%        | 0.141               | 7.5                          |
| Enchanted Iron Shovel[G]           | 1               | —  | $\frac{3}{85}$  | —               | 13.3%        | 0.141               | 7.5                          |
| Enchanted Iron Sword[G]            | 1               | —  | $\frac{3}{85}$  | —               | 13.3%        | 0.141               | 7.5                          |
| Enchanted Iron Helmet[G]           | 1               | —  | $\frac{3}{85}$  | —               | 13.3%        | 0.141               | 7.5                          |
| Enchanted Iron Chestplate[G]       | 1               | —  | $\frac{3}{85}$  | —               | 13.3%        | 0.141               | 7.5                          |
| Enchanted Iron Leggings[G]         | 1               | —  | $\frac{3}{85}$  | —               | 13.3%        | 0.141               | 7.5                          |
| Enchanted Iron Boots[G]            | 1               | —  | $\frac{3}{85}$  | —               | 13.3%        | 0.141               | 7.5                          |
| Enchanted Diamond Pickaxe[G]       | 1               | —  | $\frac{3}{85}$  | —               | 13.3%        | 0.141               | 7.5                          |
| Enchanted Diamond Shovel[G]        | 1               | —  | $\frac{3}{85}$  | —               | 13.3%        | 0.141               | 7.5                          |
| Enchanted Diamond Sword[G]         | 1               | —  | $\frac{3}{85}$  | —               | 13.3%        | 0.141               | 7.5                          |
| Enchanted Diamond Helmet[G]        | 1               | —  | $\frac{3}{85}$  | —               | 13.3%        | 0.141               | 7.5                          |
| Enchanted Diamond Chestplate[G]    | 1               | —  | $\frac{3}{85}$  | —               | 13.3%        | 0.141               | 7.5                          |
| Enchanted Diamond Leggings[G]      | 1               | —  | $\frac{3}{85}$  | —               | 13.3%        | 0.141               | 7.5                          |
| Enchanted Diamond Boots[G]         | 1               | —  | $\frac{3}{85}$  | —               | 13.3%        | 0.141               | 7.5                          |
| Emerald                            | 2–6             | —  | $\frac{2}{85}$  | —               | 9.0%         | 0.376               | 11.1                         |
| Spire Armor Trim Smithing Template | —               | 1  | —               | $\frac{1}{15}$  | 6.7%         | 0.067               | 15.0                         |
| Iron Horse Armor                   | 1               | —  | $\frac{1}{85}$  | —               | 4.6%         | 0.047               | 21.7                         |
| Golden Horse Armor                 | 1               | —  | $\frac{1}{85}$  | —               | 4.6%         | 0.047               | 21.7                         |
| Diamond Horse Armor                | 1               | —  | $\frac{1}{85}$  | —               | 4.6%         | 0.047               | 21.7                         |



↑ The size of stacks (or for unstackable items, number) of this item on any given roll.

↑ The weight of this item relative to other items in the pool.

↑ The odds of finding any of this item in a single chest.

↑ The number of items expected per chest, averaged over a large number of chests.

↑ The average number of chests the player should expect to search to find any of this item.

↑ 'Nothing' does not refer to the chance of an empty chest.  Instead, it refers to the chance that the random loot generator does not add any loot on a single roll.

↑ a b c d e f g h i j k l m n Enchantment probabilities are the same as a level-20 to level-39 enchantment would be on an enchantment table that had no cap at level 30, and that was able to apply treasure enchantments (except Soul Speed, and Swift Sneak), and where the chance of multiple enchantments is not reduced.



## Data values
### ID
Java Edition:

| Structure type | Identifier |
|----------------|------------|
| End City       | `end_city` |

| Structure | Identifier |
|-----------|------------|
| End City  | `end_city` |

Bedrock Edition:

| Structure | Identifier | Alias ID  | Translation key    |
|-----------|------------|-----------|--------------------|
| End City  | `end_city` | `endcity` | `feature.end_city` |

### Config
Java Edition:

- Structure configuration
	- type:minecraft:end_city
	- 
	- Fields common to all structures

## Notes
1. ↑Relevant code: 
int i = chunkX;
int j = chunkZ;
if (chunkX < 0) chunkX -= 19;
if (chunkZ < 0) chunkZ -= 19;
int k = chunkX / 20;
int l = chunkZ / 20;
Random random = this.worldObj.setRandomSeed(k, l, 10387313);
k = k * 20;
l = l * 20;
k = k + (random.nextInt(9) + random.nextInt(9)) / 2;
l = l + (random.nextInt(9) + random.nextInt(9)) / 2;
return i == k && j == l && this.endProvider.isIslandChunk(i, j);


