# End City
End cities are tall structures found on the outer islands of the End. They are inhabited by shulkers and hold valuable loot, including enchanted iron and diamond tools and armor. End ships, found in some end cities, are the only source of elytra.

## Contents
- 1 Generation
- 2 Structure
- 3 End ship
	- 3.1 Generation
	- 3.2 Structure
		- 3.2.1 Main deck
		- 3.2.2 Aftercastle
		- 3.2.3 Treasure room
- 4 Structure details
- 5 Loot
- 6 Data values
	- 6.1 ID
	- 6.2 Config
- 7 Advancements
- 8 History
- 9 Issues
- 10 Trivia
- 11 Gallery
	- 11.1 Screenshots
	- 11.2 In other media
- 12 Notes
- 13 References

## Generation
End cities naturally generate all over the End's outer islands. They can easily be accessed by entering the end gateway portal, but it is possible to cross the gap between the islands in other ways. They generate on the large islands, where chorus trees grow. If the end gateway portal teleports the player to a small island, the player can get to the nearest large island by building, using elytra, or throwing ender pearls.

End cities usually generate in flat areas, in "midlands" or "highlands" biomes, which are found on larger islands. One may find several cities clustered together, or travel for thousands of blocks before finding one. Unlike other structures, end cities are generated in a noticeable grid. They are located only in chunks numbered 0-8 ± a multiple of 20. For example one possible "cell" for an end city to be generated in is x_chunks=0-8 and z_chunks=80-88 which is equivalent to the coordinates x=0-128 and z=1280-1408. There can never be an end city at for example z=961-1279 or z=1409-1599 because it is outside any "cell".[note 1]

## Structure
Main article: /Structure
A view inside an end city tower.
A treasure room with both a regular chest and an ender chest.
End cities consist of tall skyscraper-like towers constructed out of end stone bricks and purpur blocks. An end city may generate as a single tower by itself, or as a sprawling complex of inter-connected towers and pathways branching from a main tower. End rods and ender chests are the only source of light. Many shulkers spawn around the city, and guard its various treasures. Decorative banners hang at the tops of some towers.

Several types of rooms can be found in an end city, and several different floors, including:

- Base floors, which are empty floors found at the base of every city; they are three stories tall, with each room wider than the one below it.
- Banner roomsthat have banners hanging on the outside, and ashulkerattached to the ceiling.
- Small roomsthat have nothing in them at all.
- Large roomsthat have precarious parkour-like staircases often leading up to another tower or a loot room.
- Loot roomsthat consist of twochestswith valuablelootat the end of a small parkour area; some rooms may have one normal chest next to anender chestinstead.

There are two types of towers:

- Small towersthat are hollow, consisting of a singlepurpur slabspiral staircase of sorts.
- Skyscrapersthat consist of a treacherous double spiral staircase made ofpurpur slabsandend rods; many shulkers spawn here.

Banners flying on top of a small tower.

## End ship
For the ocean structure, see Shipwreck.

| Biomes                                                                                                                                                                                                                                                          | End Midlands‌[Java Edition  only] End Highlands‌[Java Edition  only] The End‌[Bedrock Edition  only]                                                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Consists of                                                                                                                                                                                                                                                     | Brewing Stand Chest Dragon Wall Head End Rod End Stone Bricks Ladder Magenta Stained Glass Obsidian Purpur Block Purpur Pillar Purpur Slab Purpur Stairs Item Frame Shulker Elytra (In Item Frame) |
|                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                    |
| Brewing Stand<br/>Chest<br/>Dragon Wall Head<br/>End Rod<br/>End Stone Bricks<br/>Ladder<br/>Magenta Stained Glass<br/>Obsidian<br/>Purpur Block<br/>Purpur Pillar<br/>Purpur Slab<br/>Purpur Stairs<br/>Item Frame<br/>Shulker<br/>Elytra (In Item Frame)<br/> |                                                                                                                                                                                                    |

{
    "title": "End Ship",
    "rows": [
        {
            "field": "(values exceeds 1000 characters...)",
            "label": "(link to Biome article, displayed as Biomes)"
        },
        {
            "field": "(values exceeds 1000 characters...)",
            "label": "Consists of"
        }
    ],
    "invimages": [],
    "images": [
        "End Ship.png"
    ]
}
An end ship is a floating, boat-like structure found alongside end cities. It is relatively small, but holds even more valuable treasure than the city itself.

### Generation
Each direction of every tower of the end city has a 50% chance of generating a bridge, and the bridge itself has a 12.5% chance to generate an end ship.

When generated, the stern of the ship always faces toward the city and the bow always faces away. It generates in front of a bridge with a gated arch at the end, from which one can throw an ender pearl to reach the ship, or build a bridge.

### Structure
Main article: End City/Structure/Ship
The end ship is made of end stone bricks and purpur blocks, just like the city's main towers. Their design resembles that of European square rig sailing ships, commonly seen during the golden age of exploration. Three shulkers spawn on the ship; one on the main deck, one behind the stern of the ship, and one in the treasure room.

#### Main deck
The ship's main deck amounts to less than half of the walkable space on the ship. A ladder leads up the mast to an empty crow's nest, about 20 blocks high. There are no sails connected to the mast. 

A dragon head sits at the bow of the ship, making this the only way to obtain the dragon head in Survival mode. There are two small staircases on the outside; one that leads up to the empty upper deck, and one that leads to the cabin below.

#### Aftercastle
The aftercastle contains a brewing stand sitting on a small table, with two Instant Health II potions. Another staircase leads below deck to the ship's "hotspot"; the treasure room.

#### Treasure room
The floor of the treasure room is lined with obsidian. There are four small windows on the sides. It contains two loot chests and an item frame holding a pair of elytra; this is the only way to obtain elytra in Survival mode. A shulker guards the elytra and the two loot chests. 

- An end ship.
- The bridge that leads to the end ship.
- The dragon head, with the city in the background.
- The sterncastle of the ship. The doorway in the back leads to the treasure room. a brewing stand can be seen.
- The treasure room, where a shulker guards the elytra.
- The treasure room, only without the shulker.

## Structure details
One may access the individual structures of an end city by utilizing structure blocks to manually load city structures from the data/minecraft/structures/end_city folder in minecraft.jar. To do so, set a structure block to Load mode, enter end_city/StructureName and press LOAD. The names of these structures and a small description is provided below:

| Structure name                  | Description                                                                                                                                  | Consists of                                                                                                                                                                                                                                               | Images |
|---------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| `end_city/base_floor`           | A small room with 2shulkersguarding the entrance. Forms the entrance of end cities as well as the "empty rooms" found higher up in the city. | 68 Purpur Block 54 End Stone Bricks 12 Magenta Stained Glass 12 Purpur Pillar 2 Purpur Stairs 2 Shulker                                                                                                                                                   |        |
| `end_city/base_roof`            | The roof generated on top of base rooms.                                                                                                     | 100 Purpur Block 44 Purpur Stairs 4 End Rod                                                                                                                                                                                                               |        |
| `end_city/bridge_end`           | The small arch that forms the end and start of bridges, pointing toward end ships, or connecting to other rooms.                             | 21 Purpur Block 4 Purpur Slab 3 Purpur Stairs 2 End Rod 1 Purpur Pillar                                                                                                                                                                                   |        |
| `end_city/bridge_gentle_stairs` | Stairs on a bridge built at a small incline.                                                                                                 | 42 Purpur Block 22 Purpur Stairs 12 Purpur Slab 2 Purpur Pillar                                                                                                                                                                                           |        |
| `end_city/bridge_piece`         | A straight piece of bridge.                                                                                                                  | 20 Purpur Block 10 Purpur Stairs 4 Purpur Pillar                                                                                                                                                                                                          |        |
| `end_city/bridge_steep_stairs`  | Stairs on a bridge built at a steep incline.                                                                                                 | 24 Purpur Stairs 15 Purpur Block 2 Purpur Pillar                                                                                                                                                                                                          |        |
| `end_city/fat_tower_base`       | The entrance to the large towers. Preceded by an opening with a single slab.                                                                 | 84 Purpur Pillar 80 Purpur Block 4 End Rod 4 Purpur Stairs 3 Purpur Slab                                                                                                                                                                                  |        |
| `end_city/fat_tower_middle`     | The center of the large tower, lined with the purpur slab and end rod spiral staircase.                                                      | 164 Purpur Pillar 62 Purpur Block 8 End Rod 8 Purpur Slab 8 Purpur Stairs 4 Shulker                                                                                                                                                                       |        |
| `end_city/fat_tower_top`        | The "loot room" of the large tower, generated with 2 chests in the corner and a staircase to the roof.                                       | 352 Purpur Block 131 Purpur Stairs 106 End Stone Bricks 26 Magenta Stained Glass 18 Purpur Pillar 9 Purpur Slab 4 End Rod 2 Chest                                                                                                                         |        |
| `end_city/second_floor_1`       | The second floor of the base tower, preceded by a purpur slab staircase. The room is otherwise empty.                                        | 95 Purpur Block 84 End Stone Bricks 44 Purpur Stairs 16 Magenta Stained Glass 12 Purpur Pillar 7 Purpur Slab 4 End Rod                                                                                                                                    |        |
| `end_city/second_floor_2`       | Begins with a small spiral staircase in the center, with a small "statue" made of stairs in the upper corner.                                | 82 End Stone Bricks 70 Purpur Block 54 Purpur Stairs 14 Magenta Stained Glass 12 Purpur Pillar 9 Purpur Slab 4 End Rod 1 Shulker                                                                                                                          |        |
| `end_city/second_roof`          | Similar in structure to base_roof, but slightly larger.                                                                                      | 144 Purpur Block 52 Purpur Stairs 4 End Rod                                                                                                                                                                                                               |        |
| `end_city/ship`                 | The end ship.                                                                                                                                | 557 Purpur Block 175 Purpur Stairs 97 Purpur Pillar 36 End Stone Bricks 26 Obsidian 14 Ladder 7 Magenta Stained Glass 7 Purpur Slab 6 End Rod 2 Chest 1 Brewing Stand with two Instant Health II Potions 1 Dragon Head 1 Item Frame with Elytra 3 Shulker |        |
| `end_city/third_floor`          | An unused room, preceded by two sets of ladders. Bizarre checkerboard-style flooring with 4 shulkers guarding this room.                     |                                                                                                                                                                                                                                                           |        |
| `end_city/third_floor_1`        | A purpur pillar structure sits in the center, surrounded by purpur stairs. Preceded by a purpur slab staircase.                              | 140 Purpur Block 90 End Stone Bricks 64 Purpur Stairs 32 Magenta Stained Glass 18 Purpur Pillar 7 Purpur Slab 4 End Rod                                                                                                                                   |        |
| `end_city/third_floor_2`        | The second loot room, with a regular chest and an ender chest.                                                                               | 132 Purpur Block 98 End Stone Bricks 56 Purpur Stairs 24 Magenta Stained Glass 12 Purpur Pillar 6 End Rod 1 Chest 1 Ender Chest 2 Shulker                                                                                                                 |        |
| `end_city/third_roof`           | Similar in structure to base_roof and second_roof, but is even larger.                                                                       | 196 Purpur Block 60 Purpur Stairs 4 End Rod                                                                                                                                                                                                               |        |
| `end_city/tower_base`           | Entrance to the small tower with a ladder preceding it.                                                                                      | 40 Purpur Block 39 Purpur Pillar 4 Purpur Slab 4 Purpur Stairs 3 Ladder                                                                                                                                                                                   |        |
| `end_city/tower_floor`          | Similar in structure to tower_base, but the ladder entrance is replaced with a solid floor.                                                  | 36 Purpur Pillar 28 Purpur Stairs 21 Purpur Block 3 Purpur Slab                                                                                                                                                                                           |        |
| `end_city/tower_piece`          | The middle of the small tower, with a purpur slab spiral staircase.                                                                          | 36 Purpur Pillar 12 Purpur Block 4 Purpur Slab 4 Purpur Stairs                                                                                                                                                                                            |        |
| `end_city/tower_top`            | The roof of the small tower, with banners hanging from the sides.                                                                            | 66 Purpur Block 56 Purpur Stairs 26 End Stone Bricks 12 Purpur Pillar 8 Magenta Bannerwith Black Chevrons 6 Magenta Stained Glass 4 End Rod 2 Purpur Slab 1 Shulker                                                                                       |        |

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

