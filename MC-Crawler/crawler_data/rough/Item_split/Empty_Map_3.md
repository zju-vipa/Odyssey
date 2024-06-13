### Locking
Locking a map in a cartography table
Maps can be locked when using a glass pane in a cartography table. This creates a new map containing the same data and locks it. All new copies of this new map are also locked. A locked map never changes, even when the depicted terrain changes. In Bedrock Edition, locked maps have a unique texture.

Stained glass panes cannot be used to lock maps.

| Condition    | Newly created map | Map after terrain alteration |
|--------------|-------------------|------------------------------|
| Unlocked map |                   |                              |
| Locked map   |                   |                              |

### Renaming

  

This feature is exclusive to  Bedrock Edition. 


Renaming a map in a cartography table
In Bedrock Edition, a map or an empty map can be renamed at a cartography table. A renamed empty map keeps its name when activated. Unlike renaming items at an anvil, this does not cost any experience.

### Crafting ingredient
| Name                      | Ingredients                                                                             | Crafting recipe | Description                                                                                                                                   |
|---------------------------|-----------------------------------------------------------------------------------------|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Explorer Map<br/>(cloned) | Empty Map+<br/>Ocean Explorer Mapor<br/>Woodland Explorer Mapor<br/>Buried Treasure Map | 23456789        | The output has the same map center as the input map, and the samemonument,woodland mansionorburied treasuremarker. Cloned maps are stackable. |


## Data values
### ID
Java Edition:

| Name      | Identifier   | Form | Translation key                                                                                                                                                                                                                                                                                                                                                          |
|-----------|--------------|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Empty Map | `map`        | Item | `item.minecraft.map`                                                                                                                                                                                                                                                                                                                                                     |
| Map       | `filled_map` | Item | `item.minecraft.filled_map`<br/>`filled_map.buried_treasure`<br/>`filled_map.explorer_jungle`<br/>`filled_map.explorer_swamp`<br/>`filled_map.mansion`<br/>`filled_map.monument`<br/>`filled_map.unknown`<br/>`filled_map.village_desert`<br/>`filled_map.village_plains`<br/>`filled_map.village_savanna`<br/>`filled_map.village_snowy`<br/>`filled_map.village_taiga` |

Bedrock Edition:

| Name      | Identifier   | Alias ID   | Numeric ID | Form | Translation key                                                                                                                           |
|-----------|--------------|------------|------------|------|-------------------------------------------------------------------------------------------------------------------------------------------|
| Empty Map | `empty_map`  | `emptymap` | `515`      | Item | `item.emptyMap.name`<br/>`item.emptyLocatorMap.name`                                                                                      |
| Map       | `filled_map` | `map`      | `420`      | Item | `item.map.name`<br/>`item.map.exploration.mansion.name`<br/>`item.map.exploration.monument.name`<br/>`item.map.exploration.treasure.name` |

### Metadata
See also: Bedrock Edition data values

In Bedrock Edition, maps use the following data values:

Empty map:

|  | DV | Description       |
|--|----|-------------------|
|  | 0  | Empty Map         |
|  | 2  | Empty Locator Map |

Filled map:

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
Java Edition:

Main article: Item format
- tag: The item'stagtag.

- 
	- map: The map number.
	- map_scale_direction: Only internally used when scaling a map, after that directly removed: The amount to increase the current map scale by when crafting. Always 1.
	- map_to_lock: 1 or 0 (true/false) - true if the map should be locked after being taken out of the cartography table. Only internally used when locking a map, after that directly removed.
	- Decorations: A list of optional icons to display on the map. Decorations that are removed or modified do not update until the world is reloaded.
		- An individual decoration.
			- id: An arbitrary unique string identifying the decoration.
			- type: The ID of themap iconto display.
			- x: The world X position of the decoration.
			- z: The world Z position of the decoration.
			- rot: The rotation of the symbol, ranging from 0.0 to 360.0, measured clockwise. A rotation of 0 displays the icon upside-down compared to its appearance in the icon texture.
	- display: Thedisplaytag.
		- MapColor: The color of the markings on the item's texture.

Bedrock Edition:

SeeBedrock Edition level format/Item format.
### Map icons

  

This section needs to be updated. 
Please update this section to reflect recent updates or newly available information.Reason: New structure icons and changed structure icons in Bedrock Edition (Java Edition ones have been updated).


See also: Player.dat format, Map item format and map_icons.png

Map icons are 8×8 in Java Edition, but 16×16 in Bedrock Edition. As such, there are minor misalignment issues in Java Edition.[1]

Map icons texture in Java Edition
Map icons texture in Bedrock Edition
| Java ID | Bedrock ID | Text ID             | Appearance                                              | Purpose                                                                                                                    | Shown in item frames? |
|---------|------------|---------------------|---------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|-----------------------|
| 0       |            | `player`            | White marker                                            | Players (on map); inBedrock Edition, dynamically recolored for other players or players in the Nether or End               | No                    |
| 1       | 1          | `frame`             | Green marker                                            | The current map in an item frame                                                                                           | Yes                   |
| 2       |            | `red_marker`        | Red marker                                              | Unused                                                                                                                     | No                    |
| 3       |            | `blue_marker`       | Blue marker                                             | Unused                                                                                                                     | No                    |
| 4       |            | `target_x`          | White X                                                 | Unused                                                                                                                     | Yes                   |
| 5       | 5          | `target_point`      | Red triangle                                            | Unused                                                                                                                     | Yes                   |
| 6       | 6          | `player_off_map`    | Large white dot                                         | Players off map, nearby‌[Java Edition  only]                                                                               | No                    |
| 7       | 13         | `player_off_limits` | Small white dot                                         | Players off map, far away‌[Java Edition  only]                                                                             | No                    |
| 8       | 14         | `mansion`           | Woodland mansion                                        | Woodland mansion                                                                                                           | Yes                   |
| 9       | 15         | `monument`          | Ocean monument                                          | Ocean monument                                                                                                             | Yes                   |
| 10 - 25 |            | `banner_*`          | <br/>Banners in all 16 wool colors‌[Java Edition  only] | Banner markers                                                                                                             | Yes                   |
| 26      | 4          | `red_x`             | Red X                                                   | Buried treasure                                                                                                            | Yes                   |
|         | 8          |                     | Magenta marker                                          | Unused                                                                                                                     | No                    |
|         | 9          |                     | Orange marker                                           | Unused                                                                                                                     | Yes                   |
|         | 10         |                     | Yellow marker                                           | Unused                                                                                                                     | No                    |
|         | 11         |                     | Cyan marker                                             | Unused                                                                                                                     | No                    |
| -       | 12         |                     | Green triangle                                          | Other structure such as stronghold, fortress, end city, etc. when used as explorer map destination‌[Bedrock Edition  only] | Yes                   |
| 27      |            | `desert_village`    | Desert village                                          | Desert village                                                                                                             | Yes                   |
| 28      |            | `plains_village`    | Plains village                                          | Plains village                                                                                                             | Yes                   |
| 29      |            | `savanna_village`   | Savanna village                                         | Savanna village                                                                                                            | Yes                   |
| 30      |            | `snowy_village`     | Snowy village                                           | Snowy village                                                                                                              | Yes                   |
| 31      |            | `taiga_village`     | Taiga village                                           | Taiga village                                                                                                              | Yes                   |
| 32      |            | `jungle_pyramid`    | Jungle pyramid                                          | Jungle pyramid                                                                                                             | Yes                   |
| 33      |            | `swamp_hut`         | Swamp hut                                               | Swamp hut                                                                                                                  | Yes                   |

It should be noted that even if the player used a NBT editor to add an additional icon on the map, Minecraft shows only the first one listed when the player loads up their world.


