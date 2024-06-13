# Monster room
 The monster room, commonly and formerly known as a dungeon, is a small building in the Overworld where a monster spawner that produces either zombies, skeletons or spiders is found in the middle of a room with cobblestone lateral walls and cobblestone mixed with mossy cobblestone floors.

## Contents
- 1 Generation
- 2 Construction
- 3 Loot
- 4 Data values
	- 4.1 ID
	- 4.2 Config
- 5 History
- 6 Issues
- 7 Gallery
	- 7.1 Screenshots
- 8 References
- 9 Notes

## Generation
Monster rooms generate naturally in the Overworld terrain in any biome uncommonly and always nearby carver caves, canyons, abandoned mineshafts and strongholds. Each chunk has fourteen attempts to generate monster rooms underground within y-coordinates 0 to 320 or -58 to -1, each altitude range with different uniformity. For the higher altitude Y levels 0 to 320, up to 10 monster rooms can generate, while up to 4 monster rooms can generate in lower altitude Y levels -58 to -1. It is possible, though unlikely, for multiple attempts to succeed. In Bedrock Edition, monster rooms can generate as underground structures above sea level.

Monster rooms are a feature instead of a structure, so they generate regardless of whether the "Generate structures" world creation option has been toggled off for said world.[1] They also cannot be searched by the /locate command.[2]

For each attempt, a location (the position for monster spawner) and size (an open area with a width and length of 7 or 9 and a height of 6) is chosen. The attempt succeeds if the following conditions are met:

- Blocks in the floor area (including under the walls) of the potential monster room must besolid.
- Blocks in the ceiling area (including over the walls) of the potential monster room must be solid. The ceiling blocks may be gravity-affected such asgravelorsand, which fall if disturbed by the player.
- The walls of the potential monster room must have 1–5 openings (2-high air blocks) at floor level. Monster rooms are always connected to acarver caveor other hollow structure, although it is possible for the monster room itself to overwrite most of a tiny cave.

If the location passes, air and cobblestone are placed, then 3 attempts are made to generate each of two chests. To generate a chest, the chosen block must be empty and must have a solid block on exactly one of its four sides. The monster spawner is placed at the center of the monster room.

The monster spawner has a 50% chance of producing zombies, a 25% chance of producing skeletons, or a 25% chance of producing spiders. A zombie monster spawner in Bedrock Edition also has the same chance (5%) of producing zombie villagers as in natural generation.

Cobblestone has a 75% chance to be mossy when it is on the floor of the monster room.

The command /place feature minecraft:monster_room ~ ~ ~ can be used to generate a monster room only when the player is under the specific location where the monster room could be found naturally.

## Construction
Main article: Monster Room/Structure
Monster rooms are small rooms made of cobblestone and mossy cobblestone that contain a monster spawner and up to 2 chests. Finding a monster room without a chest is unlikely but possible. Additionally, there is a rare chance of a monster room being found without a monster spawner. Occasionally, a monster room generates with its chests in such a way as to create a double chest. Monster rooms generate with either a zombie (50% chance), skeleton (25% chance), or spider (25% chance) monster spawner. The monster spawner is always in the center of the monster room, with chests located around the walls of the room (large chests can connect with the short side against the wall). Each block of the floor has a 25% chance of being cobblestone and a 75% chance of being mossy cobblestone.

Because the horizontal range for spawning mobs is 4 blocks from the monster spawner, it is possible for mobs to be spawned outside the walls of a 5×5 monster room that is surrounded by air outside the walls.

## Loot
An example of monster room chest loot in Java Edition.
See also: Chest loot

In Java Edition and Bedrock Edition, each monster room chest contains  items drawn from 3 pools,  with the following distribution: 

| Item                   | Stack Size  [A] |      |     | Weight   [B]     |                  |                 | Chance   [C] | Avg.per chest   [D] | Avg. # cheststo search   [E] |
|------------------------|-----------------|------|-----|------------------|------------------|-----------------|--------------|---------------------|------------------------------|
|                        | 1–3×            | 1–4× | 3×  | 1–3×             | 1–4×             | 3×              |              |                     |                              |
| Bone                   | —               | —    | 1–8 | —                | —                | $\frac{10}{40}$ | 57.8%        | 3.375               | 1.7                          |
| Gunpowder              | —               | —    | 1–8 | —                | —                | $\frac{10}{40}$ | 57.8%        | 3.375               | 1.7                          |
| Rotten Flesh           | —               | —    | 1–8 | —                | —                | $\frac{10}{40}$ | 57.8%        | 3.375               | 1.7                          |
| String                 | —               | —    | 1–8 | —                | —                | $\frac{10}{40}$ | 57.8%        | 3.375               | 1.7                          |
| Wheat                  | —               | 1–4  | —   | —                | $\frac{20}{125}$ | —               | 34.1%        | 1.000               | 2.9                          |
| Bread                  | —               | 1    | —   | —                | $\frac{20}{125}$ | —               | 34.1%        | 0.400               | 2.9                          |
| Name Tag               | 1               | —    | —   | $\frac{20}{129}$ | —                | —               | 27.9%        | 0.310               | 3.6                          |
| Saddle                 | 1               | —    | —   | $\frac{20}{129}$ | —                | —               | 27.9%        | 0.310               | 3.6                          |
| Coal                   | —               | 1–4  | —   | —                | $\frac{15}{125}$ | —               | 26.6%        | 0.750               | 3.8                          |
| Redstone Dust          | —               | 1–4  | —   | —                | $\frac{15}{125}$ | —               | 26.6%        | 0.750               | 3.8                          |
| Music Disc (13)        | 1               | —    | —   | $\frac{15}{129}$ | —                | —               | 21.5%        | 0.233               | 4.6                          |
| Music Disc (cat)       | 1               | —    | —   | $\frac{15}{129}$ | —                | —               | 21.5%        | 0.233               | 4.6                          |
| Iron Horse Armor       | 1               | —    | —   | $\frac{15}{129}$ | —                | —               | 21.5%        | 0.233               | 4.6                          |
| Golden Apple           | 1               | —    | —   | $\frac{15}{129}$ | —                | —               | 21.5%        | 0.233               | 4.6                          |
| Beetroot Seeds         | —               | 2–4  | —   | —                | $\frac{10}{125}$ | —               | 18.5%        | 0.600               | 5.4                          |
| Melon Seeds            | —               | 2–4  | —   | —                | $\frac{10}{125}$ | —               | 18.5%        | 0.600               | 5.4                          |
| Pumpkin Seeds          | —               | 2–4  | —   | —                | $\frac{10}{125}$ | —               | 18.5%        | 0.600               | 5.4                          |
| Iron Ingot             | —               | 1–4  | —   | —                | $\frac{10}{125}$ | —               | 18.5%        | 0.500               | 5.4                          |
| Bucket                 | —               | 1    | —   | —                | $\frac{10}{125}$ | —               | 18.5%        | 0.200               | 5.4                          |
| Enchanted Book[F]      | 1               | —    | —   | $\frac{10}{129}$ | —                | —               | 14.7%        | 0.155               | 6.8                          |
| Golden Horse Armor     | 1               | —    | —   | $\frac{10}{129}$ | —                | —               | 14.7%        | 0.155               | 6.8                          |
| Gold Ingot             | —               | 1–4  | —   | —                | $\frac{5}{125}$  | —               | 9.6%         | 0.250               | 10.4                         |
| Diamond Horse Armor    | 1               | —    | —   | $\frac{5}{129}$  | —                | —               | 7.6%         | 0.078               | 13.2                         |
| Music Disc (otherside) | 1               | —    | —   | $\frac{2}{129}$  | —                | —               | 3.1%         | 0.031               | 32.6                         |
| Enchanted Golden Apple | 1               | —    | —   | $\frac{2}{129}$  | —                | —               | 3.1%         | 0.031               | 32.6                         |



↑ The size of stacks (or for unstackable items, number) of this item on any given roll.

↑ The weight of this item relative to other items in the pool.

↑ The odds of finding any of this item in a single chest.

↑ The number of items expected per chest, averaged over a large number of chests.

↑ The average number of chests the player should expect to search to find any of this item.

↑ All enchantments are equally probable, including treasure enchantments (except Soul Speed, and Swift Sneak), and any level of the enchantment is equally probable.



## Data values
### ID
Java Edition:

| Feature type        | Identifier     |
|---------------------|----------------|
| [No displayed name] | `monster_room` |

| Configured feature  | Identifier     |
|---------------------|----------------|
| [No displayed name] | `monster_room` |

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
  "type": "minecraft:monster_room",
  "config": {}
}



## Notes


| Terrain features |                                                                                                                                                                                          |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Overworld        | Terrain   Floating island Hill Mountain Noise cave   Surface   Erosion Hoodoo Strip Surface layer   Carver   Canyon Carver cave   Water bodies   Aquifer Ocean River   Others   Ore vein |
| Terrain          | Floating island<br/>Hill<br/>Mountain<br/>Noise cave<br/>                                                                                                                                |
| Surface          | Erosion<br/>Hoodoo<br/>Strip<br/>Surface layer<br/>                                                                                                                                      |
| Carver           | Canyon<br/>Carver cave<br/>                                                                                                                                                              |
| Water bodies     | Aquifer<br/>Ocean<br/>River<br/>                                                                                                                                                         |
| Others           | Ore vein<br/>                                                                                                                                                                            |
| The Nether       | Carver cave<br/>Lava sea<br/>                                                                                                                                                            |
| The End          | Central island<br/>Obsidian platform<br/>Outer islands<br/>                                                                                                                              |
| Removed          | Beach (world feature) Gravel<br/>Gravel<br/>Clay blob<br/>Far Lands<br/>Underwater cave<br/>Underwater ravine<br/>Java Edition only   Monolith                                           |
| Java Editiononly | Monolith<br/>                                                                                                                                                                            |

| Terrain      | Floating island Hill Mountain Noise cave            |
|--------------|-----------------------------------------------------|
| Surface      | Erosion<br/>Hoodoo<br/>Strip<br/>Surface layer<br/> |
| Carver       | Canyon<br/>Carver cave<br/>                         |
| Water bodies | Aquifer<br/>Ocean<br/>River<br/>                    |
| Others       | Ore vein<br/>                                       |

| Java Edition only | Monolith |
|-------------------|----------|

| Structures       |                                                                                                                                                                                                                                                                                        |  |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| Overworld        | Ruined Portal<br/>Surface   Desert Pyramid Igloo Jungle Pyramid Pillager Outpost Swamp Hut Woodland Mansion Village Farm   Underwater   Ocean Monument Ocean Ruins Shipwreck   Underground   Ancient City Buried Treasure Mineshaft Stronghold Trail Ruins   Upcoming   Trial Chambers |  |
| Surface          | Desert Pyramid<br/>Igloo<br/>Jungle Pyramid<br/>Pillager Outpost<br/>Swamp Hut<br/>Woodland Mansion<br/>Village Farm<br/>Farm<br/>                                                                                                                                                     |  |
| Underwater       | Ocean Monument<br/>Ocean Ruins<br/>Shipwreck<br/>                                                                                                                                                                                                                                      |  |
| Underground      | Ancient City<br/>Buried Treasure<br/>Mineshaft<br/>Stronghold<br/>Trail Ruins<br/>Upcoming   Trial Chambers                                                                                                                                                                            |  |
| Upcoming         | Trial Chambers<br/>                                                                                                                                                                                                                                                                    |  |
| The Nether       | Bastion Remnant<br/>Nether Fortress<br/>Nether Fossil<br/>Ruined Portal<br/>                                                                                                                                                                                                           |  |
| The End          | End City<br/>                                                                                                                                                                                                                                                                          |  |
| Utility          | Jigsaw<br/>                                                                                                                                                                                                                                                                            |  |
| Joke             | 9x9.nbt<br/>Bonus barrel<br/>Bridge<br/>Colosseum<br/>command.com.nbt<br/>content.nbt<br/>desire.nbt<br/>house_of_bob.nbt<br/>library.nbt<br/>llama.nbt<br/>Lunar Base<br/>Potato Mineshaft<br/>Potato Village<br/>Ruined Portatol<br/>Shapes<br/>                                     |  |
| Removed          | Village (old)<br/>Java Edition only   Brick pyramid Glass Pillars Obsidian wall Starting house                                                                                                                                                                                         |  |
| Java Editiononly | Brick pyramid<br/>Glass Pillars<br/>Obsidian wall<br/>Starting house<br/>                                                                                                                                                                                                              |  |

| Surface     | Desert Pyramid Igloo Jungle Pyramid Pillager Outpost Swamp Hut Woodland Mansion Village Farm                |
|-------------|-------------------------------------------------------------------------------------------------------------|
| Underwater  | Ocean Monument<br/>Ocean Ruins<br/>Shipwreck<br/>                                                           |
| Underground | Ancient City<br/>Buried Treasure<br/>Mineshaft<br/>Stronghold<br/>Trail Ruins<br/>Upcoming   Trial Chambers |
| Upcoming    | Trial Chambers<br/>                                                                                         |

| Upcoming | Trial Chambers |
|----------|----------------|

| Java Edition only | Brick pyramid Glass Pillars Obsidian wall Starting house |
|-------------------|----------------------------------------------------------|

| Features                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|--------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Overworld                      | Lava lake<br/>Spring<br/>Surface   Bonus Chest Desert well Disk Iceberg Blue Ice Ice Patch Ice spike Freeze top layer Forest rock Pile   Underground   Amethyst geode Pointed Dripstone Dripstone cluster Large dripstone Monster room Fossil Ore Underwater magma   Vegetation   Patched vegetations Bamboo Coral reef Kelp Sea Pickle Seagrass Glow Lichen Sculk Vein Sculk patch Huge mushroom Root system Tree Oak Spruce Birch Jungle Jungle Bush Acacia Dark oak Azalea tree Mangrove Cherry Vines Cave Vines Vegetation patch   Java EditionSuperflat only   Void start platform Fill layer |
| Surface                        | Bonus Chest<br/>Desert well<br/>Disk<br/>Iceberg<br/>Blue Ice<br/>Ice Patch<br/>Ice spike<br/>Freeze top layer<br/>Forest rock<br/>Pile<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Underground                    | Amethyst geode<br/>Pointed Dripstone Dripstone cluster Large dripstone<br/>Dripstone cluster<br/>Large dripstone<br/>Monster room<br/>Fossil<br/>Ore<br/>Underwater magma<br/>                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Vegetation                     | Patched vegetations<br/>Bamboo<br/>Coral reef<br/>Kelp<br/>Sea Pickle<br/>Seagrass<br/>Glow Lichen<br/>Sculk Vein<br/>Sculk patch<br/>Huge mushroom<br/>Root system<br/>Tree Oak Spruce Birch Jungle Jungle Bush Acacia Dark oak Azalea tree Mangrove Cherry<br/>Oak<br/>Spruce<br/>Birch<br/>Jungle<br/>Jungle Bush<br/>Acacia<br/>Dark oak<br/>Azalea tree<br/>Mangrove<br/>Cherry<br/>Vines<br/>Cave Vines<br/>Vegetation patch<br/>                                                                                                                                                            |
| Java Edition<br/>Superflatonly | Void start platform<br/>Fill layer<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| The Nether                     | Basalt columns<br/>Basalt pillar<br/>Blob<br/>Delta<br/>Glowstone blob<br/>Lava spring<br/>Fire patch<br/>Vegetation   Nether forest vegetation Twisting Vines Weeping Vines Huge fungus                                                                                                                                                                                                                                                                                                                                                                                                           |
| Vegetation                     | Nether forest vegetation<br/>Twisting Vines<br/>Weeping Vines<br/>Huge fungus<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| The End                        | Chorus plant<br/>Exit portal<br/>End gateway<br/>End spike<br/>Small island<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Utility                        | no_op<br/>Random boolean selector<br/>Random selector<br/>Replace single block<br/>Simple block<br/>Simple random selector<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Joke                           | Hash Well<br/>Potato Geode<br/>Potato Tree<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Removed                        | Water lake<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

| Surface                        | Bonus Chest Desert well Disk Iceberg Blue Ice Ice Patch Ice spike Freeze top layer Forest rock Pile                                                                                                                                                                                                                                                                                                                                     |
|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Underground                    | Amethyst geode<br/>Pointed Dripstone Dripstone cluster Large dripstone<br/>Dripstone cluster<br/>Large dripstone<br/>Monster room<br/>Fossil<br/>Ore<br/>Underwater magma<br/>                                                                                                                                                                                                                                                          |
| Vegetation                     | Patched vegetations<br/>Bamboo<br/>Coral reef<br/>Kelp<br/>Sea Pickle<br/>Seagrass<br/>Glow Lichen<br/>Sculk Vein<br/>Sculk patch<br/>Huge mushroom<br/>Root system<br/>Tree Oak Spruce Birch Jungle Jungle Bush Acacia Dark oak Azalea tree Mangrove Cherry<br/>Oak<br/>Spruce<br/>Birch<br/>Jungle<br/>Jungle Bush<br/>Acacia<br/>Dark oak<br/>Azalea tree<br/>Mangrove<br/>Cherry<br/>Vines<br/>Cave Vines<br/>Vegetation patch<br/> |
| Java Edition<br/>Superflatonly | Void start platform<br/>Fill layer<br/>                                                                                                                                                                                                                                                                                                                                                                                                 |

| Vegetation | Nether forest vegetation Twisting Vines Weeping Vines Huge fungus |
|------------|-------------------------------------------------------------------|

