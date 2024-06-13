# Explorer Map
Explorer maps are special maps used to aid in finding ocean monuments, woodland mansions, trial chambers‌[upcoming: JE 1.21 & BE 1.21.0], and buried treasures.

If the experiment for the Villager Trade Rebalance is enabled, the following structures can also be located by explorer maps: jungle pyramids, swamp huts, and desert, plains, savanna, snowy and taiga villages.

## Contents
- 1 Obtaining
	- 1.1 Trading
	- 1.2 Chest loot
- 2 Usage
	- 2.1 Locating structures
	- 2.2 Cloning
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Metadata
	- 4.3 Item data
- 5 Achievements
- 6 History
- 7 Issues
- 8 Trivia
- 9 Gallery
	- 9.1 Screenshots
- 10 See also
- 11 References
- 12 External links

## Obtaining
### Trading
Cartographer villagers sell various explorer maps depending on their level. Each explorer map costs 1 compass, and a number of emeralds. The emerald cost can vary, but the compass cost is fixed.

| Map               | Structure                                           | Trading level | Cost                      |
|-------------------|-----------------------------------------------------|---------------|---------------------------|
| Ocean Explorer    | Ocean Monument                                      | Apprentice    | 13 emeralds<br/>1 compass |
| Woodland Explorer | Woodland Mansion                                    | Journeyman    | 14 emeralds<br/>1 compass |
| Trial Chambers    | Trial Chambers<br/>‌[upcoming: JE 1.21 & BE 1.21.0] | Journeyman    | 12 emeralds<br/>1 compass |

| Map               | Structure                                           | Trading level      | Cost                      |
|-------------------|-----------------------------------------------------|--------------------|---------------------------|
| Plains Village    | Plains Village                                      | Apprentice[note 1] | 8 emeralds<br/>1 compass  |
| Desert Village    | Desert Village                                      |                    |                           |
| Savanna Village   | Savanna Village                                     |                    |                           |
| Snowy Village     | Snowy Village                                       |                    |                           |
| Taiga Village     | Taiga Village                                       |                    |                           |
| Swamp Explorer    | Witch Hut                                           |                    |                           |
| Jungle Explorer   | Jungle Temple                                       |                    |                           |
| Trial Chambers    | Trial Chambers<br/>‌[upcoming: JE 1.21 & BE 1.21.0] | Journeyman         | 12 emeralds<br/>1 compass |
| Ocean Explorer    | Ocean Monument                                      | Journeyman         | 13 emeralds<br/>1 compass |
| Woodland Explorer | Woodland Mansion                                    | Master             | 14 emeralds<br/>1 compass |

1. ↑The types of map sold by a villager depend on the biome it spawned it. More information in Trading.

If the cartographer is in the Nether or the End, either spawned or transported, the trades for the map do not unlock. If the world does not generate a particular structure, trades for the map for that structure also do not unlock.

In Java Edition, each cartographer sells its own unique explorer map that points to a different location than other cartographers. Purchasing another explorer map from the same cartographer results in the same explorer map. In Bedrock Edition, a cartographer sells an explorer map that points to the nearest location,[more information needed] regardless of whether it has been explored or previously mapped by another cartographer.

In Bedrock Edition, if cartographer map trades are unlocked in an old world, the game stops ticking.

### Chest loot
In contrast to explorer maps, buried treasure maps (Java Edition) or treasure maps (Bedrock Edition) generate in underwater ruins or in shipwrecks.

| Item                | Structure        | Container         | Quantity | Chance                         |
|---------------------|------------------|-------------------|----------|--------------------------------|
|                     |                  |                   |          | Java EditionandBedrock Edition |
| Buried Treasure Map | Shipwreck        | Map chest         | 1        | 100%                           |
|                     | Underwater Ruins | Small ruins chest | 1        | 41.7%                          |
|                     |                  | Big ruins chest   | 1        | 43.5%                          |

## Usage
Unexplored and partially explored maps.
See also: Map § Mapping and Map § Map content

### Locating structures
There are three types of explorer maps: ocean, woodland, trial chambers,‌[upcoming: JE 1.21 & BE 1.21.0] and buried treasure. The maps differ from a normal map, in that it shows the area's land-water outline, with an orange striated (striped) texture for water[1], and the blank map texture for land. The maps show a section of land that contains an ocean monument, woodland mansion, trial chambers, or buried treasure respectively.

In the experimental "Villager Trade Rebalance" data pack, there are seven additional explorer maps: jungle maps that show a jungle pyramid, swamp maps that show a swamp hut, as well as maps for desert, plains, savanna, snowy and taiga villages.

The structure shown may not be the nearest such structure to the player. The structures are displayed as a small icon. If the player icon is smaller than it would be on a normal map, that means the player is a great distance away. When the player is less than 1027 blocks away from the map border, the icon returns to the proper size. When the player reaches the map's area of land (512×512), the map fills in like a normal map.

The basic functions of a buried treasure explorer map are similar to that of the others. However, instead of showing the structure icon on the map, it shows a red X instead. The buried treasure chest is located on the same X and Z coordinates as the middle of the X (the player marker may need to be aligned with the bottom of the middle 2×2 pixel square of the X). To locate the chest spot, hold the treasure map with both hands, not in the offhand slot.

### Cloning

  

This section needs to be updated. 
Please update this section to reflect recent updates or newly available information.Reason: Change pattern to reflect new maps.


| Ingredients                                                                             | Crafting recipe | Description                                                                                                                                   |
|-----------------------------------------------------------------------------------------|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Empty Map+<br/>Ocean Explorer Mapor<br/>Woodland Explorer Mapor<br/>Buried Treasure Map | 23456789        | The output has the same map center as the input map, and the samemonument,woodland mansionorburied treasuremarker. Cloned maps are stackable. |

The parts of the world that have already been explored and mapped are copied, and newly explored areas appear on both instances. In Creative mode, cloned explorer maps can be obtained by pick blocking on the explorer map displayed on item frames (the map needs to be out of the player's inventory when using pick block, or else that map moves into the active hotbar slot).

## Data values
### ID
Java Edition:

| Name | Identifier   | Form | Translation key                                                                                                                                                                                                                                                                                                                                                                 |
|------|--------------|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Map  | `filled_map` | Item | `item.minecraft.filled_map`<br/>`filled_map.monument`<br/>`filled_map.mansion`<br/>`filled_map.explorer_jungle`<br/>`filled_map.explorer_swamp`<br/>`filled_map.village_desert`<br/>`filled_map.village_plains`<br/>`filled_map.village_savanna`<br/>`filled_map.village_snowy`<br/>`filled_map.village_taiga`<br/>`filled_map.buried_treasure`<br/>`filled_map.trial_chambers` |

Bedrock Edition:

| Name | Identifier   | Alias ID | Numeric ID | Form | Translation key                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|------|--------------|----------|------------|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Map  | `filled_map` | `map`    | `358`      | Item | `item.map.name`<br/>`item.map.exploration.monument.name`<br/>`item.map.exploration.mansion.name`<br/>`item.map.exploration.jungle_temple.name`<br/>`item.map.exploration.swamp_hut.name`<br/>`item.map.exploration.village_desert.name`<br/>`item.map.exploration.village_plains.name`<br/>`item.map.exploration.village_savanna.name`<br/>`item.map.exploration.village_snowy.name`<br/>`item.map.exploration.village_taiga.name`<br/>`item.map.exploration.buried_treasure.name`<br/>`item.map.exploration.trial_chambers.name` |

### Metadata
See also: Bedrock Edition data values

In Bedrock Edition, the item Data value distinguishes explorer maps from one another:



|  | DV | Description                                                            |
|--|----|------------------------------------------------------------------------|
|  | 0  | Map                                                                    |
|  | 2  | Map (locator)                                                          |
|  | 3  | Ocean Explorer Map                                                     |
|  | 4  | Woodland Explorer Map                                                  |
|  | 5  | Treasure Map                                                           |
|  | 6  | Locked Map                                                             |
|  | 7  | Snowy Village Map<br/>[only experimental "Villager Trade Rebalance"]   |
|  | 8  | Taiga Village Map<br/>[only experimental "Villager Trade Rebalance"]   |
|  | 9  | Plains Village Map<br/>[only experimental "Villager Trade Rebalance"]  |
|  | 10 | Savanna Village Map<br/>[only experimental "Villager Trade Rebalance"] |
|  | 11 | Desert Village Map<br/>[only experimental "Villager Trade Rebalance"]  |
|  | 12 | Jungle Explorer Map<br/>[only experimental "Villager Trade Rebalance"] |
|  | 13 | Swamp Explorer Map<br/>[only experimental "Villager Trade Rebalance"]  |
|  | 14 | Trial Chambers Map<br/>[only experimental "Update 1.21"]               |



### Item data
An explorer map differs from a map in that its display tag is set, which includes a Mapcolor and a LocName; also its Decorations list includes an entry for its target monument, mansion or buried treasure. Its map item entry is identical to that of a normal map, except that by the time the player sees it, its colors byte array is pre-filled with explorer maps' characteristic land-water boundary lines and water shading.

- Item data
	- tag:
		- display: How the map looks in an item slot. See alsoPlayer.dat_format#Display Properties.
			- Name: The name the map is given. In this case, they are localized strings:{"translate":"translation key"}.
			- MapColor: Color codes are calculated from the Red, Green and Blue components using this formula:Red<<16 + Green<<8 + Blue.[note 1]Monument maps use 3830373, which isrgb(58,114,101). Mansion maps use 5393476, which isrgb(82,76,68). Jungle pyramid, swamp hut, and all village maps use 10066329, which isrgb(153,153,153).[only experimental "Villager Trade Rebalance"]Buried treasure explorer maps do not use a color code.
		- Decorations:
			- : One of these for each icon on the map. Explorer maps always have at least one representing their target.
				- id: An arbitrary unique string identifying the decoration. For explorer map target structures, this is "+".
				- rot: The rotation of the icon. For explorer map target structures, this is always 180.
				- type: The ID of themap icon: 8 for a mansion map, 9 for a monument map, 26 for a treasure map, 27 for a desert village map[only experimental "Villager Trade Rebalance"], 28 for a plains village map[only experimental "Villager Trade Rebalance"], 29 for a savanna village map[only experimental "Villager Trade Rebalance"], 30 for a snowy village map[only experimental "Villager Trade Rebalance"], 31 for a taiga village map[only experimental "Villager Trade Rebalance"], 32 for a jungle pyramid map[only experimental "Villager Trade Rebalance"], 33 for a swamp hut map[only experimental "Villager Trade Rebalance"].
				- x: The world x-coordinate of the target structure icon.
				- z: The world z-coordinate of the target structure icon.

** Notes **
1. ↑For positive values larger than 0x00FFFFFF, the top byte is ignored. All negative values produce white.

