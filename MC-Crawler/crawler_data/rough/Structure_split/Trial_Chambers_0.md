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

