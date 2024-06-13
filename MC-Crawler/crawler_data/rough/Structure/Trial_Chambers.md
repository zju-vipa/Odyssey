# Trial Chambers
Trial chambers are underground structures that serve as a mid-game combat challenge.[1] They consist mostly of copper blocks and tuff bricks, and are the only place where trial spawners and vaults naturally generate. Trial chambers are also the only place where breeze spawn, whose breeze rods can be used to craft wind charges. Various materials such as heavy cores and certain armor trims are obtained exclusively by unlocking vaults in trial chambers.

Ominous trials can also take place here through Bad Omen, where Trial Omen can cause all trial spawners to become ominous, making them more difficult and providing greater rewards.

## Contents
- 1 Generation
- 2 Structure
	- 2.1 File structure
	- 2.2 Components
		- 2.2.1 Entrance
		- 2.2.2 Corridors
		- 2.2.3 Atriums
		- 2.2.4 Hallways
		- 2.2.5 Intersections
		- 2.2.6 Chambers
	- 2.3 Trial spawners
	- 2.4 Vault generation
- 3 Mobs
- 4 Loot
	- 4.1 Vaults
	- 4.2 Chests
	- 4.3 Barrels
	- 4.4 Decorated pots
	- 4.5 Dispensers
	- 4.6 Trial spawners
		- 4.6.1 Ominous trial spawner
- 5 Data values
	- 5.1 ID
- 6 Advancements
- 7 Video
- 8 History
- 9 Issues
- 10 Gallery
	- 10.1 Renders
	- 10.2 Screenshots
	- 10.3 Development images
- 11 References

## Generation
Trial chambers generate underground in the Overworld. The starting room generates at an altitude of between Y = -40 and -20, but the structure is not restricted to those Y levels. In fact, the majority of the structure's rooms tend to generate between Y = -20 and 0.

The generation of trial chambers follows a grid of 32×32 chunk regions centered on the world origin (X=0, Z=0). There is always one trial chambers structure generated in each region at a random location.

Trial chambers can be located using trial chambers maps, which are sold by journeyman-level cartographer villagers for 12 emeralds and a compass. The maps do not always point to the nearest structure.

## Structure
Main article: /Structure
The trial chambers is a procedurally generated structure made mainly of tuff bricks, copper, and their variants. The chambers consist of a number of different rooms, some of which contain trial spawners and vaults. Some trial spawners may contain the breeze, a playful hostile mob.

### File structure
All trial chambers structures found below are located in the folder client.jar/data/minecraft/structures/trial_chambers‌[JE  only].

| List                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| trial_chambers chamber chamber_1.nbt chamber_2.nbt chamber_4.nbt assembly.nbt chamber_8.nbt entrance_cap.nbt eruption.nbt pedestal.nbt slanted.nbt addon 10x15_pathway_3.nbt 10x15_rise.nbt 10x15_stacked_pathway.nbt c1_breeze.nbt c3_side_walkway_1.nbt c3_side_walkway_2.nbt c6_chest.nbt c6_column_full.nbt c6_column_tall.nbt c6_column_tall_wide.nbt c6_cover.nbt c6_cover_long.nbt c6_cover_short.nbt c6_cover_small.nbt c6_cover_small_1.nbt c6_cover_small_2.nbt c6_cover_small_3.nbt c6_melee_spawner.nbt c6_ranged_column_short.nbt c6_ranged_column_short_wide.nbt c6_stairs.nbt c6_wide_platform.nbt closed_side_walkway.nbt corner_room_1.nbt full_column_ranged_spawner.nbt full_corner_column.nbt full_stacked_walkway.nbt full_stacked_walkway_2.nbt grate_bridge.nbt hanging_platform.nbt lower_staircase_down.nbt lower_walkway_platform.nbt middle_column_ranged_spawner.nbt middle_walkway.nbt platform_with_space.nbt short_grate_platform.nbt short_platform.nbt side_walkway.nbt stairs_with_space.nbt stairs_with_space_2.nbt walkway_extension.nbt walkway_with_bridge_1.nbt eruption breeze_slice_1.nbt center_1.nbt quadrant_1.nbt quadrant_2.nbt quadrant_3.nbt quadrant_4.nbt quadrant_5.nbt slice_1.nbt slice_2.nbt slice_3.nbt pedestal center_1.nbt ominous_slice_1.nbt quadrant_1.nbt quadrant_2.nbt quadrant_3.nbt slice_1.nbt slice_2.nbt slice_3.nbt slice_4.nbt slice_5.nbt slanted center.nbt hallway_1.nbt hallway_2.nbt hallway_3.nbt hallway_4.nbt hallway_5.nbt ominous_upper_arm_1.nbt quadrant_1.nbt quadrant_2.nbt quadrant_3.nbt quadrant_4.nbt ramp_1.nbt ramp_2.nbt ramp_3.nbt ramp_4.nbt chests supply.nbt connectors supply.nbt corridor atrium_1.nbt end_1.nbt end_2.nbt entrance_1.nbt first_plate.nbt second_plate.nbt straight_1.nbt straight_2.nbt straight_3.nbt straight_4.nbt straight_5.nbt straight_6.nbt straight_7.nbt straight_8.nbt addon arrow_dispenser.nbt bridge_lower.nbt chandelier_upper.nbt decoration_upper.nbt head_upper.nbt ladder_to_middle.nbt open_walkway.nbt open_walkway_upper.nbt reward_upper.nbt staircase.nbt wall.nbt walled_walkway.nbt atrium bogged_relief.nbt breeze_relief.nbt grand_staircase_1.nbt grand_staircase_2.nbt grand_staircase_3.nbt spider_relief.nbt spiral_relief.nbt decor barrel.nbt candle_1.nbt candle_2.nbt candle_3.nbt candle_4.nbt dead_bush_pot.nbt empty_pot.nbt flow_pot.nbt guster_pot.nbt scrape_pot.nbt undecorated_pot.nbt dispensers chamber.nbt hallway cache_1.nbt corner_staircase.nbt corner_staircase_down.nbt corridor_connector_1.nbt left_corner.nbt long_straight_staircase.nbt long_straight_staircase_down.nbt lower_hallway_connector.nbt right_corner.nbt rubble.nbt rubble_chamber.nbt rubble_chamber_thin.nbt rubble_thin.nbt straight.nbt straight_staircase.nbt straight_staircase_down.nbt upper_hallway_connector.nbt intersection intersection_1.nbt intersection_2.nbt reward ominous_vault.nbt vault.nbt spawner breeze breeze.nbt connectors breeze.nbt melee.nbt ranged.nbt slow_ranged.nbt small_melee.nbt melee husk.nbt slime.nbt zombie.nbt ranged poison_skeleton.nbt skeleton.nbt stray.nbt slow_ranged poison_skeleton.nbt skeleton.nbt stray.nbt small_melee baby_zombie.nbt cave_spider.nbt silverfish.nbt spider.nbt |

### Components
All trial chambers follow a common structure. A trial chambers structure is composed of 5 main components: hallways, corridors, intersections, atriums, and chambers. There is always 1 entrance chamber, which is used as the starting point when the game generates a trial chambers structure. However, the entrance chamber is not necessarily the first part of the structure a player finds while exploring.

The entrance chamber leads to an atrium that connects to a corridor. This corridor is followed by an intersection leading to another corridor on one side and a combat chamber on the other. The second corridor leads to another combat chamber. More combat chambers may generate from the sides of the corridors.

The trial chambers structure, like all other structures, is limited to having to generate all of its rooms in a large area centered at the entrance chamber. Due to this limit, long corridors may cause the structure to generate with missing parts or chambers, on rare occasions.

#### Entrance
The entrance chamber corridor/entrance_1 generates in every trial chamber and contains an oak tree next to two chests with entrance loot, a vault up on a ledge, and a hidden room containing a bed and a reward chest. A staircase leads down to the lower area of the room. Additionally, located behind the tree and in-between the two chests is a copper trapdoor over a ventilation shaft-like tunnel. This tunnel allows the player to crawl through to the lower area, acting as a shortcut.

#### Corridors
Both corridors are three stories tall and may contain trial spawners of any category (except breeze) as well as supply chests, decorated pots and tripwire traps. The length of the corridor can vary in multiples of four segments. Each segment may contain a side copper door from any of the floors connecting to a combat chamber through hallways.

There are two types of corridor ends connecting the second corridor to a combat chamber:

- corridor/end_1contains multiple stairs converging from all corridor entrances to the chamber exit.
- corridor/end_2containswaterfilling the bottom layer and a chest behind the stairs containing intersection loot.

Each type of corridor end contains an ominous vault.

#### Atriums
There are two types of atriums connecting the first corridor to the entrance chamber:

- corridor/atrium_1contains a grand staircase and a fountain in the center. On the far walls to either side is a mural depicting one of several different images.
- corridor/atrium_2contains a large wall with two opposite staircases.

Each type of atrium contains an ominous vault.

#### Hallways
Some hallways end at a dead end, which is hallway/rubble. This dead end has a reward chest at the end.

#### Intersections
There are two types of intersections, both connecting two corridors with a combat chamber and containing a room with four beds and a barrel with loot:

- intersection/intersection_1connects the corridors through the bottom floor and has a staircase up to the bedroom.
- intersection/intersection_2connects the corridors through the top floor and has an underwater bedroom accessible via a ladder.

Each type of intersection contains an ominous vault.

#### Chambers
There are a variety of combat chambers, each containing multiple trial spawners, vaults, and one ominous vault. Most chambers have several dispensers along the walls triggered by stone buttons.

- chamber/chamber_1is a tall room with a central pillar that can be reached by crossingcopper grateplatforms hanging onchainsor narrowcopper blockbridges. A gap in the pillar has a breeze trial spawner, and one or more corners may have an upper ledge with a ranged trial spawner and possibly a vault. Some obstacles may be placed at random on the bottom level.
- chamber/chamber_2is similar to the above room, but with the floor covered inpowder snowand some obstacles made oftuff bricks. The breeze trial spawner is replaced with a ranged trial spawner, and one of the corner ledges (if present) has a dispenser beneath it with no buttons or contents.
- chamber/chamber_4is a small room with wide bridges, three small melee trial spawners, and two vaults, but no dispensers. Copper grates under one of the bridges leave a 1-block high gap that the small mobs can easily pass through.
- chamber/assemblyis a large square room with a platform along one wall, which has a vault and two trial spawners (1 ranged and 1 breeze). The center of the chamber is filled with random structures and may include additional vaults, ranged trial spawners, and dispensers, as well as other obstacles.
- chamber/chamber_8is a tall, narrow room with five ranged trial spawners on three successively higher ledges. Under each ledge is a row of oxidizedcopper trapdoors. There are two vaults at the bottom and two more vaults on the highest ledge.
- chamber/eruptionis a large, round room withmagma blocksaround a central platform, at least three trial spawners(1 melee, 1 ranged, and 1 breeze), and at least one vault. Atop the central platform is a fountain-like structure with oak buttons and an upward-facing dispenser containing awater bucket. The room has two levels, with melee trial spawners and various obstacles being on the lower level. On the upper level, ranged trial spawners can be found sitting on ledges in the various corners of the room. A small room housing a vault is also found on the upper level. These and any additional vaults, trial spawners, and obstacles may be placed around the room at random.
- chamber/pedestalis a two-story room with a large, tall pedestal in the center topped by four trial spawners (1 breeze and 3 random others). Additional melee trial spawners are on the upper floor, and a large number of vaults are scattered throughout the chamber, but there are no dispensers. Several passageways are blocked by walls of copper grates.
- chamber/slantedis a two-story room with ledges of varying heights on the upper floor, some of which have 1-block high tunnels of copper grates hidden underneath. The upper floor also has a breeze trial spawner in the center and several melee trial spawners, and a large number of vaults are scattered throughout the chamber, but there are no dispensers.

### Trial spawners


Main article: Trial Spawner
When a trial chamber structure generates, one mob from each category is randomly selected for the trial spawners in that structure. Every mob within the same category has an equal chance to be selected. The breeze is in its own category and is thus guaranteed to be found in certain combat chambers of every structure. Every type of room generates the same trial spawner category in the same location, with the exceptions of the corridors and the center of the pedestal combat chamber.

Each trial spawner is centered above a 3×3 square of blocks in the floor that indicates which mob it can spawn.

|  |  |  |
|--|--|--|
|  |  |  |
|  |  |  |

|  |  |  |
|--|--|--|
|  |  |  |
|  |  |  |

|  |  |  |
|--|--|--|
|  |  |  |
|  |  |  |

|  |  |  |
|--|--|--|
|  |  |  |
|  |  |  |

|  |  |  |
|--|--|--|
|  |  |  |
|  |  |  |

|  |  |  |
|--|--|--|
|  |  |  |
|  |  |  |

|  |  |  |
|--|--|--|
|  |  |  |
|  |  |  |

|  |  |  |
|--|--|--|
|  |  |  |
|  |  |  |

|  |  |  |
|--|--|--|
|  |  |  |
|  |  |  |

|  |  |  |
|--|--|--|
|  |  |  |
|  |  |  |

|  |  |  |
|--|--|--|
|  |  |  |
|  |  |  |

|  |  |  |
|--|--|--|
|  |  |  |
|  |  |  |

|  |  |  |
|--|--|--|
|  |  |  |
|  |  |  |

|  |  |  |
|--|--|--|
|  |  |  |
|  |  |  |

### Vault generation
Vaults generate throughout the trial chambers. One vault can be found on the highest platform of the entrance room, and many more vaults can be found in the various combat chambers in the structure.

See also: § Vaults.

## Mobs


Main article: Trial Spawner § Mob spawning
Natural hostile mob spawning is disabled within a trial chamber. Mobs spawn only from the trial spawners. The number of mobs spawned scales with the number of players in range of each spawner, and breezes are spawned less per spawner and per player than other mobs. See § Trial Spawners above for information on which mobs spawn in which spawners.



## Loot
See also: Chest loot

Loot is available from vaults, chests, barrels, dispensers and decorated pots from within the chambers. Players who defeat a trial spawner each receive rewards; this loot scales depending on the amount of people who defeat the trial spawner.

### Vaults


Main article: Vault § Loot
In Java Edition and Bedrock Edition, each trial chambers reward container contains  items drawn from 3 pools,  with the following distribution: 

| Item                              | Stack Size  [A] |      |    | Weight   [B]     |                |                 | Chance   [C] | Avg.per container   [D] | Avg. # containersto loot   [E] |
|-----------------------------------|-----------------|------|----|------------------|----------------|-----------------|--------------|-------------------------|--------------------------------|
|                                   | 1×              | 1–3× | 1× | 1×               | 1–3×           | 1×              |              |                         |                                |
| Nothing[F]                        | —               | —    | 1  | —                | —              | $\frac{36}{48}$ | 75.0%        | 0.750                   | 1.3                            |
| Emerald                           | 2–4             | 2–4  | —  | $\frac{12}{110}$ | $\frac{4}{22}$ | —               | 39.6%        | 1.418                   | 2.5                            |
| Arrow                             | 2–8             | 2–8  | —  | $\frac{4}{110}$  | $\frac{4}{22}$ | —               | 34.6%        | 2.000                   | 2.9                            |
| Arrow of Poison                   | 2–8             | 2–8  | —  | $\frac{4}{110}$  | $\frac{4}{22}$ | —               | 34.6%        | 2.000                   | 2.9                            |
| Iron Ingot                        | 1–4             | 1–4  | —  | $\frac{3}{110}$  | $\frac{3}{22}$ | —               | 26.9%        | 0.750                   | 3.7                            |
| Honey Bottle                      | 1–2             | 1–2  | —  | $\frac{3}{110}$  | $\frac{3}{22}$ | —               | 26.9%        | 0.450                   | 3.7                            |
| Ominous Bottle I - II[G]          | 1               | 1    | —  | $\frac{2}{110}$  | $\frac{2}{22}$ | —               | 18.6%        | 0.200                   | 5.4                            |
| Golden Apple                      | —               | —    | 1  | —                | —              | $\frac{6}{48}$  | 12.5%        | 0.125                   | 8.0                            |
| Damaged Shield[H]                 | 1               | —    | —  | $\frac{12}{110}$ | —              | —               | 10.9%        | 0.109                   | 9.2                            |
| Enchanted Bow[I]                  | 1               | —    | —  | $\frac{12}{110}$ | —              | —               | 10.9%        | 0.109                   | 9.2                            |
| Wind Charge                       | 4–12            | 4–12 | —  | $\frac{1}{110}$  | $\frac{1}{22}$ | —               | 9.6%         | 0.800                   | 10.4                           |
| Diamond                           | 1–2             | 1–2  | —  | $\frac{1}{110}$  | $\frac{1}{22}$ | —               | 9.6%         | 0.150                   | 10.4                           |
| Golden Carrot                     | 1–2             | —    | —  | $\frac{8}{110}$  | —              | —               | 7.3%         | 0.109                   | 13.7                           |
| Enchanted Book[J]                 | 1               | —    | —  | $\frac{8}{110}$  | —              | —               | 7.3%         | 0.073                   | 13.7                           |
| Enchanted Book[K]                 | 1               | —    | —  | $\frac{8}{110}$  | —              | —               | 7.3%         | 0.073                   | 13.7                           |
| Enchanted Crossbow[L]             | 1               | —    | —  | $\frac{8}{110}$  | —              | —               | 7.3%         | 0.073                   | 13.7                           |
| Enchanted Iron Axe[I]             | 1               | —    | —  | $\frac{8}{110}$  | —              | —               | 7.3%         | 0.073                   | 13.7                           |
| Enchanted Iron Chestplate[I]      | 1               | —    | —  | $\frac{8}{110}$  | —              | —               | 7.3%         | 0.073                   | 13.7                           |
| Bolt Armor Trim Smithing Template | —               | —    | 1  | —                | —              | $\frac{3}{48}$  | 6.2%         | 0.062                   | 16.0                           |
| Guster Banner Pattern             | —               | —    | 1  | —                | —              | $\frac{2}{48}$  | 4.2%         | 0.042                   | 24.0                           |
| Enchanted Diamond Axe[I]          | 1               | —    | —  | $\frac{4}{110}$  | —              | —               | 3.6%         | 0.036                   | 27.5                           |
| Enchanted Diamond Chestplate[I]   | 1               | —    | —  | $\frac{4}{110}$  | —              | —               | 3.6%         | 0.036                   | 27.5                           |
| Trident                           | —               | —    | 1  | —                | —              | $\frac{1}{48}$  | 2.1%         | 0.021                   | 48.0                           |



↑ The size of stacks (or for unstackable items, number) of this item on any given roll.

↑ The weight of this item relative to other items in the pool.

↑ The odds of finding any of this item in a single chest.

↑ The number of items expected per chest, averaged over a large number of chests.

↑ The average number of chests the player should expect to search to find any of this item.

↑ 'Nothing' does not refer to the chance of an empty chest.  Instead, it refers to the chance that the random loot generator does not add any loot on a single roll.

↑ Ominous bottle level between I and II

↑ The item has between 50% and 100% of its total durability.

↑ a b c d e Enchantment probabilities are the same as a level-5 to level-15 enchantment would be on an enchantment table that was able to apply treasure enchantments (except Soul Speed, and Swift Sneak), and where the chance of multiple enchantments is not reduced.

↑ Enchanted with a random level of Mending, Riptide, Loyalty, Channeling, or Impaling.

↑ Enchanted with a random level of Sharpness, Bane of Arthropods, Efficiency, Fortune, Silk Touch, or Feather Falling.

↑ Enchantment probabilities are the same as a level-5 to level-20 enchantment would be on an enchantment table that was able to apply treasure enchantments (except Soul Speed, and Swift Sneak), and where the chance of multiple enchantments is not reduced.



Main article: Ominous Vault § Loot
In Java Edition 1.21, each trial chambers ominous vault contains  items drawn from 3 pools,  with the following distribution: 

| Item                              | Stack Size  [A] |      |    | Weight   [B]     |                |                | Chance   [C] | Avg.per container   [D] | Avg. # containersto loot   [E] |
|-----------------------------------|-----------------|------|----|------------------|----------------|----------------|--------------|-------------------------|--------------------------------|
|                                   | 1×              | 1–3× | 1× | 1×               | 1–3×           | 1×             |              |                         |                                |
| Emerald                           | 4–10            | 4–10 | —  | $\frac{5}{132}$  | $\frac{5}{15}$ | —              | 54.9%        | 4.932                   | 1.8                            |
| Wind Charge                       | 8–12            | 8–12 | —  | $\frac{4}{132}$  | $\frac{4}{15}$ | —              | 46.2%        | 5.636                   | 2.2                            |
| Arrow of Slowness IV              | 4–12            | 4–12 | —  | $\frac{3}{132}$  | $\frac{3}{15}$ | —              | 36.4%        | 3.382                   | 2.7                            |
| Diamond                           | 2–3             | 2–3  | —  | $\frac{2}{132}$  | $\frac{2}{15}$ | —              | 25.5%        | 0.705                   | 3.9                            |
| Nothing[F]                        | —               | —    | 1  | —                | —              | $\frac{3}{12}$ | 25.0%        | 0.250                   | 4.0                            |
| Flow Armor Trim Smithing Template | —               | —    | 1  | —                | —              | $\frac{3}{12}$ | 25.0%        | 0.250                   | 4.0                            |
| Enchanted Golden Apple            | —               | —    | 1  | —                | —              | $\frac{3}{12}$ | 25.0%        | 0.250                   | 4.0                            |
| Block of Emerald                  | 1               | —    | —  | $\frac{24}{132}$ | —              | —              | 18.2%        | 0.182                   | 5.5                            |
| Flow Banner Pattern               | —               | —    | 1  | —                | —              | $\frac{2}{12}$ | 16.7%        | 0.167                   | 6.0                            |
| Ominous Bottle III - V[G]         | 1               | 1    | —  | $\frac{1}{132}$  | $\frac{1}{15}$ | —              | 13.4%        | 0.141                   | 7.5                            |
| Enchanted Crossbow[H]             | 1               | —    | —  | $\frac{16}{132}$ | —              | —              | 12.1%        | 0.121                   | 8.2                            |
| Block of Iron                     | 1               | —    | —  | $\frac{16}{132}$ | —              | —              | 12.1%        | 0.121                   | 8.2                            |
| Golden Apple                      | 1               | —    | —  | $\frac{16}{132}$ | —              | —              | 12.1%        | 0.121                   | 8.2                            |
| Enchanted Diamond Axe[I]          | 1               | —    | —  | $\frac{12}{132}$ | —              | —              | 9.1%         | 0.091                   | 11.0                           |
| Enchanted Diamond Chestplate[I]   | 1               | —    | —  | $\frac{12}{132}$ | —              | —              | 9.1%         | 0.091                   | 11.0                           |
| Heavy Core                        | —               | —    | 1  | —                | —              | $\frac{1}{12}$ | 8.3%         | 0.083                   | 12.0                           |
| Enchanted Book[J]                 | 1               | —    | —  | $\frac{8}{132}$  | —              | —              | 6.1%         | 0.061                   | 16.5                           |
| Enchanted Book[K]                 | 1               | —    | —  | $\frac{8}{132}$  | —              | —              | 6.1%         | 0.061                   | 16.5                           |
| Enchanted Book[L]                 | 1               | —    | —  | $\frac{4}{132}$  | —              | —              | 3.0%         | 0.030                   | 33.0                           |
| Block of Diamond                  | 1               | —    | —  | $\frac{1}{132}$  | —              | —              | 0.8%         | 0.008                   | 132.0                          |



↑ The size of stacks (or for unstackable items, number) of this item on any given roll.

↑ The weight of this item relative to other items in the pool.

↑ The odds of finding any of this item in a single chest.

↑ The number of items expected per chest, averaged over a large number of chests.

↑ The average number of chests the player should expect to search to find any of this item.

↑ 'Nothing' does not refer to the chance of an empty chest.  Instead, it refers to the chance that the random loot generator does not add any loot on a single roll.

↑ Ominous bottle level between III and V

↑ Enchantment probabilities are the same as a level-5 to level-20 enchantment would be on an enchantment table that was able to apply treasure enchantments (except Soul Speed, and Swift Sneak), and where the chance of multiple enchantments is not reduced.

↑ a b Enchantment probabilities are the same as a level-5 to level-15 enchantment would be on an enchantment table that was able to apply treasure enchantments (except Soul Speed, and Swift Sneak), and where the chance of multiple enchantments is not reduced.

↑ Enchanted with a random level of Breach, or Density.

↑ Enchanted with a random level of Sharpness, Bane of Arthropods, Efficiency, Fortune, Silk Touch, or Feather Falling.

↑ Enchanted with a random level of Wind Charge.



### Chests
In Java Edition and Bedrock Edition, each trial chambers entrance chest contains 2–3 item stacks,  with the following distribution: 

| Item       | Stack Size  [A] | Weight   [B]    | Chance   [C] | Avg.per chest   [D] | Avg. # cheststo search   [E] |
|------------|-----------------|-----------------|--------------|---------------------|------------------------------|
| Arrow      | 5–10            | $\frac{10}{36}$ | 55.1%        | 5.208               | 1.8                          |
| Honeycomb  | 2–8             | $\frac{10}{36}$ | 55.1%        | 3.472               | 1.8                          |
| Wooden Axe | 1               | $\frac{10}{36}$ | 55.1%        | 0.694               | 1.8                          |
| Stick      | 2–5             | $\frac{5}{36}$  | 31.0%        | 1.215               | 3.2                          |
| Trial Key  | 1               | $\frac{1}{36}$  | 6.8%         | 0.069               | 14.7                         |



↑ The size of stacks (or for unstackable items, number) of this item on any given roll.

↑ The weight of this item relative to other items in the pool.

↑ The odds of finding any of this item in a single chest.

↑ The number of items expected per chest, averaged over a large number of chests.

↑ The average number of chests the player should expect to search to find any of this item.



In Java Edition, each trial chambers corridor chest contains 1–3 item stacks,  with the following distribution: 

| Item                     | Stack Size  [A] | Weight   [B]   | Chance   [C] | Avg.per chest   [D] | Avg. # cheststo search   [E] |
|--------------------------|-----------------|----------------|--------------|---------------------|------------------------------|
| Tuff                     | 8–20            | $\frac{3}{19}$ | 28.4%        | 4.421               | 3.5                          |
| Scaffolding              | 2–10            | $\frac{2}{19}$ | 19.6%        | 1.263               | 5.1                          |
| Bamboo Planks            | 3–6             | $\frac{2}{19}$ | 19.6%        | 0.947               | 5.1                          |
| Torch                    | 3–6             | $\frac{2}{19}$ | 19.6%        | 0.947               | 5.1                          |
| Bamboo Hanging Sign      | 1–4             | $\frac{2}{19}$ | 19.6%        | 0.526               | 5.1                          |
| Ender Pearl              | 1–2             | $\frac{2}{19}$ | 19.6%        | 0.316               | 5.1                          |
| Damaged Stone Axe[F]     | 1               | $\frac{2}{19}$ | 19.6%        | 0.211               | 5.1                          |
| Damaged Stone Pickaxe[F] | 1               | $\frac{2}{19}$ | 19.6%        | 0.211               | 5.1                          |
| Honeycomb                | 2–8             | $\frac{1}{19}$ | 10.2%        | 0.526               | 9.8                          |
| Damaged Iron Axe[G]      | 1               | $\frac{1}{19}$ | 10.2%        | 0.105               | 9.8                          |

In Bedrock Edition, each trial chambers corridor chest contains 1–3 item stacks,  with the following distribution: 

| Item                     | Stack Size  [A] | Weight   [B]   | Chance   [C] | Avg.per chest   [D] | Avg. # cheststo search   [E] |
|--------------------------|-----------------|----------------|--------------|---------------------|------------------------------|
| Tuff                     | 8–20            | $\frac{3}{19}$ | 28.4%        | 4.421               | 3.5                          |
| Scaffolding              | 2–10            | $\frac{2}{19}$ | 19.6%        | 1.263               | 5.1                          |
| Bamboo Planks            | 3–6             | $\frac{2}{19}$ | 19.6%        | 0.947               | 5.1                          |
| Torch                    | 3–6             | $\frac{2}{19}$ | 19.6%        | 0.947               | 5.1                          |
| Bamboo Hanging Sign      | 1–4             | $\frac{2}{19}$ | 19.6%        | 0.526               | 5.1                          |
| Ender Pearl              | 1–2             | $\frac{2}{19}$ | 19.6%        | 0.316               | 5.1                          |
| Damaged Stone Axe[F]     | 1               | $\frac{2}{19}$ | 19.6%        | 0.211               | 5.1                          |
| Damaged Stone Pickaxe[F] | 1               | $\frac{2}{19}$ | 19.6%        | 0.211               | 5.1                          |
| Honeycomb                | 2–8             | $\frac{1}{19}$ | 10.2%        | 0.526               | 9.8                          |
| Enchanted Iron Axe[H][G] | 1               | $\frac{1}{19}$ | 10.2%        | 0.105               | 9.8                          |



↑ a b The size of stacks (or for unstackable items, number) of this item on any given roll.

↑ a b The weight of this item relative to other items in the pool.

↑ a b The odds of finding any of this item in a single chest.

↑ a b The number of items expected per chest, averaged over a large number of chests.

↑ a b The average number of chests the player should expect to search to find any of this item.

↑ a b c d The item has between 15% and 80% of its total durability.

↑ a b The item has between 40% and 90% of its total durability.

↑ All enchantments are equally probable, including treasure enchantments (except Soul Speed, and Swift Sneak), and any level of the enchantment is equally probable.



In Java Edition and Bedrock Edition, each trial chambers intersection chest contains 1–3 item stacks,  with the following distribution: 

| Item                       | Stack Size  [A] | Weight   [B]    | Chance   [C] | Avg.per chest   [D] | Avg. # cheststo search   [E] |
|----------------------------|-----------------|-----------------|--------------|---------------------|------------------------------|
| Amethyst Shard             | 8–20            | $\frac{20}{86}$ | 39.7%        | 6.512               | 2.5                          |
| Cake                       | 1–4             | $\frac{20}{86}$ | 39.7%        | 1.163               | 2.5                          |
| Block of Iron              | 1–2             | $\frac{20}{86}$ | 39.7%        | 0.698               | 2.5                          |
| Diamond                    | 1–2             | $\frac{10}{86}$ | 21.5%        | 0.349               | 4.6                          |
| Block of Emerald           | 1–3             | $\frac{5}{86}$  | 11.2%        | 0.233               | 8.9                          |
| Damaged Diamond Axe[F]     | 1               | $\frac{5}{86}$  | 11.2%        | 0.116               | 8.9                          |
| Damaged Diamond Pickaxe[F] | 1               | $\frac{5}{86}$  | 11.2%        | 0.116               | 8.9                          |
| Block of Diamond           | 1               | $\frac{1}{86}$  | 2.3%         | 0.023               | 43.3                         |



↑ The size of stacks (or for unstackable items, number) of this item on any given roll.

↑ The weight of this item relative to other items in the pool.

↑ The odds of finding any of this item in a single chest.

↑ The number of items expected per chest, averaged over a large number of chests.

↑ The average number of chests the player should expect to search to find any of this item.

↑ a b The item has between 10% and 50% of its total durability.



In Java Edition and Bedrock Edition, each trial chambers supply chest contains 3–5 item stacks,  with the following distribution: 

| Item                     | Stack Size  [A] | Weight   [B]   | Chance   [C] | Avg.per chest   [D] | Avg. # cheststo search   [E] |
|--------------------------|-----------------|----------------|--------------|---------------------|------------------------------|
| Arrow                    | 4–14            | $\frac{2}{18}$ | 37.3%        | 4.000               | 2.7                          |
| Glow Berries             | 2–10            | $\frac{2}{18}$ | 37.3%        | 2.667               | 2.7                          |
| Baked Potato             | 2–4             | $\frac{2}{18}$ | 37.3%        | 1.333               | 2.7                          |
| Damaged Stone Pickaxe[F] | 1               | $\frac{2}{18}$ | 37.3%        | 0.444               | 2.7                          |
| Tuff                     | 5–10            | $\frac{1}{18}$ | 20.4%        | 1.667               | 4.9                          |
| Arrow of Poison          | 4–8             | $\frac{1}{18}$ | 20.4%        | 1.333               | 4.9                          |
| Arrow of Slowness        | 4–8             | $\frac{1}{18}$ | 20.4%        | 1.333               | 4.9                          |
| Acacia Planks            | 3–6             | $\frac{1}{18}$ | 20.4%        | 1.000               | 4.9                          |
| Torch                    | 3–6             | $\frac{1}{18}$ | 20.4%        | 1.000               | 4.9                          |
| Bone Meal                | 2–5             | $\frac{1}{18}$ | 20.4%        | 0.778               | 4.9                          |
| Moss Block               | 2–5             | $\frac{1}{18}$ | 20.4%        | 0.778               | 4.9                          |
| Potion of Regeneration   | 2               | $\frac{1}{18}$ | 20.4%        | 0.444               | 4.9                          |
| Potion of Strength       | 2               | $\frac{1}{18}$ | 20.4%        | 0.444               | 4.9                          |
| Milk Bucket              | 1               | $\frac{1}{18}$ | 20.4%        | 0.222               | 4.9                          |



↑ The size of stacks (or for unstackable items, number) of this item on any given roll.

↑ The weight of this item relative to other items in the pool.

↑ The odds of finding any of this item in a single chest.

↑ The number of items expected per chest, averaged over a large number of chests.

↑ The average number of chests the player should expect to search to find any of this item.

↑ The item has between 15% and 80% of its total durability.



The trial chambers reward chest has the same loot that a vault gives when a single trial key is used.

### Barrels
In Java Edition and Bedrock Edition, each trial chambers intersection barrel contains 1–3 item stacks,  with the following distribution: 

| Item                                   | Stack Size  [A] | Weight   [B]    | Chance   [C] | Avg.per barrel   [D] | Avg. # barrelsto open   [E] |
|----------------------------------------|-----------------|-----------------|--------------|----------------------|-----------------------------|
| Bamboo Planks                          | 5–15            | $\frac{10}{33}$ | 49.3%        | 6.061                | 2.0                         |
| Baked Potato                           | 6–10            | $\frac{10}{33}$ | 49.3%        | 4.848                | 2.0                         |
| Damaged Enchanted Golden Axe[F][G]     | 1               | $\frac{4}{33}$  | 22.3%        | 0.242                | 4.5                         |
| Damaged Enchanted Golden Pickaxe[F][G] | 1               | $\frac{4}{33}$  | 22.3%        | 0.242                | 4.5                         |
| Diamond                                | 1–3             | $\frac{1}{33}$  | 5.9%         | 0.121                | 16.8                        |
| Bucket                                 | 1–2             | $\frac{1}{33}$  | 5.9%         | 0.091                | 16.8                        |
| Compass                                | 1               | $\frac{1}{33}$  | 5.9%         | 0.061                | 16.8                        |
| Damaged Diamond Pickaxe[H]             | 1               | $\frac{1}{33}$  | 5.9%         | 0.061                | 16.8                        |
| Enchanted Diamond Axe[F][I]            | 1               | $\frac{1}{33}$  | 5.9%         | 0.061                | 16.8                        |



↑ The size of stacks (or for unstackable items, number) of this item on any given roll.

↑ The weight of this item relative to other items in the pool.

↑ The odds of finding any of this item in a single chest.

↑ The number of items expected per chest, averaged over a large number of chests.

↑ The average number of chests the player should expect to search to find any of this item.

↑ a b c All enchantments are equally probable, including treasure enchantments (except Soul Speed, and Swift Sneak), and any level of the enchantment is equally probable.

↑ a b The item has between 15% and 80% of its total durability.

↑ The item has between 10% and 50% of its total durability.

↑ The item has between 40% and 90% of its total durability.



### Decorated pots
In Java Edition, each trial chambers corridor pot contains 1 item stack,  with the following distribution: 

| Item             | Stack Size  [A] | Weight   [B]      | Chance   [C] | Avg.per pot   [D] | Avg. # potsto break   [E] |
|------------------|-----------------|-------------------|--------------|-------------------|---------------------------|
| Emerald          | 1–8             | $\frac{100}{551}$ | 18.1%        | 0.817             | 5.5                       |
| Amethyst Shard   | 1–4             | $\frac{100}{551}$ | 18.1%        | 0.454             | 5.5                       |
| Arrow            | 1–4             | $\frac{100}{551}$ | 18.1%        | 0.454             | 5.5                       |
| Lapis Lazuli     | 1–4             | $\frac{100}{551}$ | 18.1%        | 0.454             | 5.5                       |
| Iron Ingot       | 1–6             | $\frac{50}{551}$  | 9.1%         | 0.318             | 11.0                      |
| Gold Ingot       | 1–6             | $\frac{20}{551}$  | 3.6%         | 0.127             | 27.6                      |
| Trial Key        | 1–3             | $\frac{20}{551}$  | 3.6%         | 0.073             | 27.6                      |
| Diamond          | 1–4             | $\frac{5}{551}$   | 0.9%         | 0.023             | 110.2                     |
| Block of Emerald | 1–3             | $\frac{5}{551}$   | 0.9%         | 0.018             | 110.2                     |
| Block of Diamond | 1–2             | $\frac{1}{551}$   | 0.2%         | 0.003             | 551.0                     |



↑ The size of stacks (or for unstackable items, number) of this item on any given roll.

↑ The weight of this item relative to other items in the pool.

↑ The odds of finding any of this item in a single chest.

↑ The number of items expected per chest, averaged over a large number of chests.

↑ The average number of chests the player should expect to search to find any of this item.



### Dispensers
In Java Edition, each trial chambers chamber dispenser contains 1 item stack,  with the following distribution: 

| Item                         | Stack Size  [A] | Weight   [B]   | Chance   [C] | Avg.per dispenser   [D] | Avg. # dispensersto open   [E] |
|------------------------------|-----------------|----------------|--------------|-------------------------|--------------------------------|
| Fire Charge                  | 4–8             | $\frac{6}{29}$ | 20.7%        | 1.241                   | 4.8                            |
| Snowball                     | 4–8             | $\frac{6}{29}$ | 20.7%        | 1.241                   | 4.8                            |
| Arrow                        | 4–8             | $\frac{4}{29}$ | 13.8%        | 0.828                   | 7.2                            |
| Water Bucket                 | 1               | $\frac{4}{29}$ | 13.8%        | 0.138                   | 7.2                            |
| Egg                          | 4–8             | $\frac{2}{29}$ | 6.9%         | 0.414                   | 14.5                           |
| Lingering Potion of Healing  | 2–5             | $\frac{1}{29}$ | 3.4%         | 0.121                   | 29.0                           |
| Lingering Potion of Poison   | 2–5             | $\frac{1}{29}$ | 3.4%         | 0.121                   | 29.0                           |
| Lingering Potion of Slowness | 2–5             | $\frac{1}{29}$ | 3.4%         | 0.121                   | 29.0                           |
| Lingering Potion of Weakness | 2–5             | $\frac{1}{29}$ | 3.4%         | 0.121                   | 29.0                           |
| Splash Potion of Poison      | 2–5             | $\frac{1}{29}$ | 3.4%         | 0.121                   | 29.0                           |
| Splash Potion of Slowness    | 2–5             | $\frac{1}{29}$ | 3.4%         | 0.121                   | 29.0                           |
| Splash Potion of Weakness    | 2–5             | $\frac{1}{29}$ | 3.4%         | 0.121                   | 29.0                           |



↑ The size of stacks (or for unstackable items, number) of this item on any given roll.

↑ The weight of this item relative to other items in the pool.

↑ The odds of finding any of this item in a single chest.

↑ The number of items expected per chest, averaged over a large number of chests.

↑ The average number of chests the player should expect to search to find any of this item.



In Java Edition, each trial chambers corridor dispenser contains 1 item stack,  with the following distribution: 

| Item  | Stack Size  [A] | Weight   [B]  | Chance   [C] | Avg.per dispenser   [D] | Avg. # dispensersto open   [E] |
|-------|-----------------|---------------|--------------|-------------------------|--------------------------------|
| Arrow | 4–8             | $\frac{1}{1}$ | 100.0%       | 6.000                   | 1.0                            |



↑ The size of stacks (or for unstackable items, number) of this item on any given roll.

↑ The weight of this item relative to other items in the pool.

↑ The odds of finding any of this item in a single chest.

↑ The number of items expected per chest, averaged over a large number of chests.

↑ The average number of chests the player should expect to search to find any of this item.



In Java Edition, each trial chambers water dispenser contains 1 item stack,  with the following distribution: 

| Item         | Stack Size  [A] | Weight   [B]  | Chance   [C] | Avg.per dispenser   [D] | Avg. # dispensersto open   [E] |
|--------------|-----------------|---------------|--------------|-------------------------|--------------------------------|
| Water Bucket | 1               | $\frac{1}{1}$ | 100.0%       | 1.000                   | 1.0                            |



↑ The size of stacks (or for unstackable items, number) of this item on any given roll.

↑ The weight of this item relative to other items in the pool.

↑ The odds of finding any of this item in a single chest.

↑ The number of items expected per chest, averaged over a large number of chests.

↑ The average number of chests the player should expect to search to find any of this item.



### Trial spawners
When all mobs have been killed, the spawner has a 50% chance of picking the trial key, in which case it drops for all players. The other 50% of the time it drops one of the other items for each player.

In Java Edition, each trial spawner contains 1 item stack,  with the following distribution: 

| Item                   | Stack Size  [A] | Weight   [B]    | Chance   [C] | Avg.per spawner   [D] | Avg. # spawnersto defeat   [E] |
|------------------------|-----------------|-----------------|--------------|-----------------------|--------------------------------|
| Trial Key              | 1               | $\frac{13}{26}$ | 50.0%        | 0.500                 | 2.0                            |
| Glow Berries           | 2–10            | $\frac{3}{26}$  | 11.5%        | 0.692                 | 8.7                            |
| Emerald                | 1–6             | $\frac{3}{26}$  | 11.5%        | 0.404                 | 8.7                            |
| Baked Potato           | 1–3             | $\frac{3}{26}$  | 11.5%        | 0.231                 | 8.7                            |
| Golden Carrot          | 1–3             | $\frac{1}{26}$  | 3.8%         | 0.077                 | 26.0                           |
| Ender Pearl            | 1               | $\frac{1}{26}$  | 3.8%         | 0.038                 | 26.0                           |
| Potion of Regeneration | 1               | $\frac{1}{26}$  | 3.8%         | 0.038                 | 26.0                           |
| Potion of Strength     | 1               | $\frac{1}{26}$  | 3.8%         | 0.038                 | 26.0                           |



↑ The size of stacks (or for unstackable items, number) of this item on any given roll.

↑ The weight of this item relative to other items in the pool.

↑ The odds of finding any of this item in a single chest.

↑ The number of items expected per chest, averaged over a large number of chests.

↑ The average number of chests the player should expect to search to find any of this item.



#### Ominous trial spawner
When all mobs have been killed, the ominous trial spawner has a 30% chance of picking the ominous trial key, in which case it drops for all players. The other 70% of the time it drops one of the other items for each player.
In Java Edition 1.21, each trial chambers trial spawner ominous contains 1 item stack,  with the following distribution: 

| Item                   | Stack Size  [A] | Weight   [B]     | Chance   [C] | Avg.per spawner   [D] | Avg. # spawnersto defeat   [E] |
|------------------------|-----------------|------------------|--------------|-----------------------|--------------------------------|
| Ominous Trial Key      | 1               | $\frac{33}{110}$ | 30.0%        | 0.300                 | 3.3                            |
| Baked Potato           | 2–4             | $\frac{21}{110}$ | 19.1%        | 0.573                 | 5.2                            |
| Steak                  | 1–2             | $\frac{21}{110}$ | 19.1%        | 0.286                 | 5.2                            |
| Golden Carrot          | 1–2             | $\frac{14}{110}$ | 12.7%        | 0.191                 | 7.9                            |
| Rotten Flesh           | 1–4             | $\frac{7}{110}$  | 6.4%         | 0.159                 | 15.7                           |
| Potion of Regeneration | 1               | $\frac{7}{110}$  | 6.4%         | 0.064                 | 15.7                           |
| Potion of Strength     | 1               | $\frac{7}{110}$  | 6.4%         | 0.064                 | 15.7                           |



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
| Jigsaw         | `jigsaw`   |

| Structure      | Identifier       |
|----------------|------------------|
| Trial Chambers | `trial_chambers` |

Bedrock Edition:

| Structure      | Identifier       | Translation key          |
|----------------|------------------|--------------------------|
| Trial Chambers | `trial_chambers` | `feature.trial_chambers` |

