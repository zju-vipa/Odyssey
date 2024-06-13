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


