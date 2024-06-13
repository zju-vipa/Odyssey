# Map
A map is an item used to view explored terrain and mark landmarks.

## Contents
- 1 Obtaining
	- 1.1 Crafting
	- 1.2 Cartography table
	- 1.3 Starting map
	- 1.4 Chest loot
	- 1.5 Trading
- 2 Usage
	- 2.1 Mapping
		- 2.1.1 Map content
		- 2.1.2 Other dimensions
	- 2.2 Zooming out
		- 2.2.1 Zoom details
	- 2.3 Cloning
	- 2.4 Player markers
		- 2.4.1 Java Edition
		- 2.4.2 Bedrock Edition
	- 2.5 Framing
	- 2.6 Banner markers
	- 2.7 Locking
	- 2.8 Renaming
	- 2.9 Crafting ingredient
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Metadata
	- 4.3 Item data
	- 4.4 Map icons
- 5 Achievements
- 6 History
- 7 Issues
- 8 Trivia
- 9 Gallery
	- 9.1 Screenshots
	- 9.2 In other media
- 10 See also
- 11 References

## Obtaining
### Crafting
| Ingredients   | Crafting recipe | Description                                                                                                                            |
|---------------|-----------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Paper+Compass |                 | This map is called an "Empty Locator Map" inBedrock Edition, and an "Empty Map" inJava Edition. It has the same uses in both editions. |
| Paper         |                 | ‌[Bedrock Edition  only]This map is called an "Empty Map". It only records terrain and does not show location markers.                 |

### Cartography table

  

This feature is exclusive to  Bedrock Edition. 


In Bedrock Edition, a map can also be created using a single paper in a cartography table to create an empty map, or a paper and a compass for an empty locator map.

- 
- 

### Starting map

  

This feature is exclusive to  Bedrock Edition. 


When creating a new world in Bedrock Edition, the player can enable the "Starting Map" option to spawn with an empty locator map in the hotbar. This option is not available in Hardcore mode.‌[upcoming: BE 1.21.0] The map's zoom scale is 1:8.

### Chest loot
| Item      | Structure  | Container            | Quantity | Chance          |
|-----------|------------|----------------------|----------|-----------------|
|           |            |                      |          | Java Edition    |
| Empty Map | Shipwreck  | Map chest            | 1        | 7.7%            |
|           | Stronghold | Library chest        | 1        | 10.9%           |
|           | Village    | Cartographer's chest | 1–3      | 46.2%           |
|           |            |                      |          | Bedrock Edition |
| Map[A]    | Shipwreck  | Map chest            | 1        | 7.7%            |
|           | Stronghold | Library chest        | 1        | 10.5%           |
|           | Village    | Cartographer's chest | 1–3      | 46.2%           |


↑ Named unknown map, but changed to map 0, the scale level is 1:4, Maps from the same stack are stackable, but maps that are not stacked are unstackable despite looking identical.


### Trading
Novice-level cartographer villagers sell a single empty map for 7 emeralds as their trades.

In Java Edition, cartographer villagers may give players with the Hero of the Village effect an empty map.

## Usage
### Mapping
Crafting a map creates an empty map. The map is drawn for the first time when it is held and used (by pressing the use item control). After conversion to a drawn map item, it starts to draw a top-down view of the player's surroundings, with North pointing to the top of the map. A pointed oval pointer indicates the player's position on the map, and moves in real-time as the player moves across the terrain shown on the map. In Bedrock Edition, this pointer is displayed exclusively on locator maps.

The map grid at different zoom levels
The map does not center on the player when created; rather, the world is broken up into large invisible grid squares, and the map displays the area of whichever grid square it was in when it was first used. For example, if a player uses a new map in a certain grid square, and then moves a distance away and uses another fresh map but is still within the same grid square, both maps will have the exact same boundary. To make a map with different bounds than the first one, the player would have to move outside of the edges of the first map (because then they would be in a new grid square). This way, no two maps of the same size can ever partially overlap.

To record the world on a map, that specific map must be held in either of the player's hands while the player moves around the world. The map records terrain within a 64 block radius (4 chunks) from a player in the Overworld or the End, or 32 blocks in the Nether. The map records the surface even as the player moves below the surface. The world is recorded as-is during exploration, meaning that if the world is modified, a player must revisit the area while holding the map to update the map's view.

Maps display as a mini-map when held in the off-hand, or if the off-hand slot is occupied; the map is full-sized only when held in the dominant hand with both hands free.

Maps can be cloned to synchronize them or framed for display.

To create a custom picture, a player can make a large piece of pixel art (128×128) facing upward, center a map on it, and place that map in an item frame. Locking is recommended. See Map item format#Map Pixel Art for details on the techniques.

#### Map content
Main article: Map item format
Maps consist of square pixels arranged in a 128×128 square grid, with each pixel representing a square portion of land. A standard map represents 128×128 blocks (1 block per pixel, 8×8 chunks), but it can be zoomed out to represent up to 2048×2048 blocks (16 square blocks per pixel, 128×128 chunks).

In Java Edition, the color of a map pixel generally matches the color of the most common opaque block in the corresponding area, as seen from the sky. 'Minority blocks' in the target area have no effect on the color of the pixel, thus small features tend to be undetectable on zoomed-out maps.

In Bedrock Edition, the color of a map pixel instead matches the single top-most opaque block in a grid sized by the map's scale factor. For example, a map with zoom level 3/4 has a pixel size of 8×8 blocks; this means the map reads only the top-most opaque blocks at the 0,0 coordinate, the 8,0 coordinate, the 0,8 coordinate, etcetera, ignoring all other blocks in the area. This means that in Bedrock Edition, map pixel art requires only one block per pixel regardless of map magnification.

In Bedrock Edition, grass, foliage and water colors that are biome-dependent are represented accurately on a map.

| Java Edition                 | Bedrock Edition                 |
|------------------------------|---------------------------------|
|                              |                                 |
| Biome colors inJava Edition. | Biome colors inBedrock Edition. |

On land above water, a block's color is darker if placed at a lower elevation than the block north of it, or brighter if placed at a higher elevation than the block north of it. Maps also show ground up to about 15 blocks below the surface of the water as slightly lighter blue, to show where the ground rises.

#### Other dimensions
While maps in the Nether work, they show only a red-and-gray pattern, regardless of the blocks placed. The only useful function is finding where the player is in relation to framed copies, which show as green pointers. Additionally, the player pointer rapidly spins and is not a good indicator of direction. In Java Edition, banner markers placed in the Nether still show on the map as usual. Despite its unreliability, having a mapped trail can still be useful in some cases, such as while riding a strider over lava. Maps in the End work as usual, mapping the terrain and showing the accurate location and direction of the player.

In Java Edition, holding a map from the Overworld in a different dimension shows the player's last position and direction in the Overworld. This effect is temporary, and the marker disappears after quitting and joining the world/server again.

In Bedrock Edition, an Overworld locator map in the Nether shows the player's relative location and direction in the Overworld. Similarly, a Nether locator map in the Overworld shows the player's relative location in the Nether, but the place marker spins. An Overworld locator map in the End shows the world spawn. A Nether locator map cannot be used in the End — the map appears, but the place marker is not shown anywhere — and similarly, an End locator map cannot be used in the Overworld or the Nether. The place marker changes color depending on the dimension that the player is currently in (white for the Overworld, red for the Nether, and magenta for the End).

### Zooming out
Zooming out a map in a cartography table
A map can be zoomed out up to 4 times, increasing the covered area from 128×128 blocks up to a maximum of 2048×2048 blocks. An empty map cannot be zoomed out; it needs to be activated for the zooming to be possible. Changing the zoom level of a map resets its contents, and terrain needs to be explored again to be drawn on the zoomed out map.

Locked maps cannot be zoomed out.

| Ingredients | Crafting recipe | Description                       |
|-------------|-----------------|-----------------------------------|
| Paper+Map   |                 | Locked maps cannot be zoomed out. |

| Name                            | Ingredients              | Anvil usage                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Description                                                                                       |
|---------------------------------|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| Map or Locator Map (zoomed out) | Mapor Locator Map +Paper | .mw-parser-output .template-Anvil-background{box-sizing:content-box;width:324px;height:128px}.mw-parser-output .template-Anvil-prompt{display:block;color:#3F3F3F;font-family:Minecraft;font-size:16px;text-align:left;margin-left:106px;margin-top:-3px;overflow:hidden;text-overflow:ellipsis}.mw-parser-output .template-Anvil-inputbox{position:absolute;top:32px;right:6px;width:220px;height:32px}.mw-parser-output .template-Anvil-inputtext{display:block;margin:5px 6px;color:#FCFCFC;text-shadow:0.125em 0.125em 0 #3E3E3E;font-family:Minecraft;font-size:16px;overflow:hidden;text-overflow:ellipsis;max-width:208px}.mw-parser-output .template-Anvil-slot{display:block;position:absolute;top:84px;left:44px}.mw-parser-output .template-Anvil-hammer{position:absolute;top:6px;left:26px;background-size:cover;width:60px;height:60px}.mw-parser-output .template-Anvil-plus{position:absolute;top:90px;left:98px;background-size:cover;width:26px;height:26px}.mw-parser-output .template-Anvil-arrow{display:block;position:absolute;top:88px;left:196px;width:44px;height:30px}.mw-parser-output .template-Anvil-cost{display:block;position:absolute;top:126px;right:8px;background:#898989;padding:0 4px 0 4px;font-family:Minecraft;font-size:16px;overflow:hidden;text-overflow:ellipsis;max-width:308px}.mw-parser-output .template-Anvil-cost-expensive{color:#FC5F5F;text-shadow:0.125em 0.125em #3E1818,0.125em 0 #3E1818,0 0.125em #3E1818}.mw-parser-output .template-Anvil-cost-normal{color:#7EFC20;text-shadow:0.125em 0.125em #203E08,0.125em 0 #203E08,0 0.125em #203E08}Repair & Name MapLocator Map8 | Bedrock Editiononly.Supplying 8 sheets of paper results in a zoomed-out version of the input map. |

#### Zoom details
The zooming function starts from when the map is created (zoom level 0/4) up to its fourth zoom step (zoom level 4/4).

|                                             |                                      | Zoom step 0    | Zoom step 1        | Zoom step 2         | Zoom step 3         | Zoom step 4                      |
|---------------------------------------------|--------------------------------------|----------------|--------------------|---------------------|---------------------|----------------------------------|
|                                             |                                      |                |                    |                     |                     |                                  |
|                                             | Zoom level                           | 0/4            | 1/4                | 2/4                 | 3/4                 | 4/4                              |
|                                             | 1 map pixel represents               | 1 block        | 4 blocks2×2 blocks | 16 blocks4×4 blocks | 64 blocks8×8 blocks | 256 blocks (1 chunk)16×16 blocks |
|                                             | Scaling ratio                        | 1:1            | 1:2                | 1:4                 | 1:8                 | 1:16                             |
|                                             | Map covers an area of                | 128×128 blocks | 256×256 blocks     | 512×512 blocks      | 1024×1024 blocks    | 2048×2048 blocks                 |
|                                             |                                      | 8×8 chunks     | 16×16 chunks       | 32×32 chunks        | 64×64 chunks        | 128×128 chunks                   |
| Total paper needed to zoom out from Level 0 | in anvil‌[BE  only]or crafting table | -              | 8                  | 16                  | 24                  | 32                               |
|                                             | in cartography table                 | -              | 1                  | 2                   | 3                   | 4                                |

Maps are always aligned to a grid at all zoom levels. That means zooming out any different map in a specific area covered by that map always has the same center. As such, maps are aligned by map width (1024 blocks for a level 3 map) minus 64. A level 3 map generated at X=0 Z=0 covers X and Z coordinates from -64 to 959. All maps generated in this area zoom out to the same coordinates, guaranteeing that they are always 'aligned' on a map wall. For a zoomed-out map to cover a new area, it must start with a base (level 0) map that is in that area.

At zoom level 0, a map created on the point (0,0) has (0,0) at the center of the map. At higher zoom levels of the same map, the coordinate (0,0) is in the top left square of the map.

In Java Edition, the zoom level and the scaling factor are displayed in the tooltip of a map by turning on advanced tooltips (a debug option that can be toggled by using the key combination F3 + H). In Bedrock Edition, the zoom level of a map is always displayed it its tooltip.

### Cloning
Cloning a map in a cartography table
A map can be cloned to create multiple synchronized copies linked to the same map data. Multiple players can hold clones of the same map to record different parts of the world simultaneously.

Upon cloning a map, the parts of the world that have already been explored and mapped are copied; thereafter, newly explored areas appear on all cloned instances automatically. The resulting copies have the same zoom level as the starting map. If one of the maps is later zoomed out, then that map loses its connection to the original and functions as a completely separate map that has to be individually filled by exploring.

All cloned maps stack with each other, unless renamed. Even if renamed, the mapped areas continue to remain in sync.

In Bedrock Edition, both empty maps and empty locator maps may be used to clone a map. Whether the cloned maps show position markers is dependent only on the input map. For this reason, using an empty locator map instead of an empty map for cloning is a waste of a compass.

A cartography table can also be used to clone a map.

| Ingredients   | Crafting recipe | Description                |
|---------------|-----------------|----------------------------|
| Empty Map+Map | 23456789        | Cloned maps are stackable. |

| Name                        | Ingredients                  | Anvil usage                                    | Description                                                                                                                                                                                                 |
|-----------------------------|------------------------------|------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Map or Locator Map (cloned) | Mapor Locator Map +Empty Map | Repair & Name MapLocator MapMapLocator Map2222 | Bedrock Editiononly.Only one copy can be made at a time.The non-empty input map must be a locator map for the output to be a locator map. An empty locator map is the same as an empty map for this recipe. |


In Creative mode, a map in an item frame may be cloned by using pick block on it, as long as that map is not also in the player's inventory.

### Player markers
#### Java Edition
In Java Edition, every map contains a white pointer that marks the position of the player, and points in the same direction as the player. When a player moves out of a map, the pointer turns into a white dot which moves along the edge relative to the player's position. The marker disappears if the player is too far from the mapped area; in explorer maps, the dot becomes smaller instead of fully disappearing. The distance on the X or Z axes from the map's edge required for the dot to vanish (regular maps) or to turn smaller (explorer maps) depends on the zoom level of the map:

- Level 0/4 :more than 256 blocks away
- Level 1/4 :more than 512 blocks away
- Level 2/4 :more than 1024 blocks away
- Level 3/4 :more than 2048 blocks away
- Level 4/4 :more than 4096 blocks away

In multiplayer, other players are displayed on the map only if they have a map in their inventory cloned from the one being looked at. Other players are marked using white pointers.

#### Bedrock Edition
In Bedrock Edition, position markers are displayed exclusively on locator maps. A map without position markers can be turned into a locator map at a later time by combining it with a compass on the crafting grid, on an anvil, or at a cartography table. When a player moves out of a locator map, the marker is displayed as an arrow no matter how far the player is from the center of the map.

| Ingredients              | Crafting recipe | Description                                                                                                                                                                                                                    |
|--------------------------|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Mapor Empty Map +Compass |                 | ‌[Bedrock Edition  only]Maps crafted from only paper do not show the location marker; to add it, a compass must be added to the map. The map keeps its current zoom level, and remembers all of the terrain it has mapped out. |

| Name        | Ingredients | Anvil usage      | Description                                                                                                                      |
|-------------|-------------|------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Locator Map | Map+Compass | Repair & NameMap | Bedrock Editiononly.Maps crafted with only paper do not show the location marker; to add it, a compass must be added to the map. |

Player markers in multiplayer
In multiplayer, a locator map contains markers for all players who are not in Spectator mode and are not wearing a head or a carved pumpkin, even if they don't have any maps in their inventory. In the Overworld, players see themselves as a white pointer, and other players are displayed in different colors depending on the order in which they joined: the first player who joined - or the host - is light gray (looking almost identical to the regular white pointer), the second player is cyan, the third player is orange, the fourth player is light green, and so on. All players in the Nether are displayed with a red pointer, and all players in the End use a magenta pointer.

If other players have a map in their inventory cloned from the one being looked at, they are displayed using white pointers. This also includes players wearing a head or a carved pumpkin and players in Spectator mode.

Players who are between 10 to 80 blocks away are displayed using the face of their skin instead of the pointer, with a border colored as described above.

### Framing
When placing a map into an item frame, the map displays a green pointer at the location of the item frame (it must be a locator map in Bedrock Edition). If the player leaves a map in an item frame and then views a clone of it, the green pointer is displayed on both copies. This can be used to track waypoints. If a player holds a map whose clone is on display in an item frame, then the map in the item frame updates along with the held map.

It is worth noting that the markers work only on copies of the same map. Other maps of the same area do not show the existing markers that the player(s) had placed.

The size of the item frame expands when displaying a map. This allows for combining multiple maps side-by-side to create a much larger map display that visually appears to be one continuous map. For example, a player could display four maps in a 2x2 grid on a wall; if each map is zoom level 2, the total area displayed would be 1024×1024 blocks (the same as a zoom level 3 map) but with a scaling ratio of 1:4 (the same as a zoom level 2 map), depicting much more detail than a zoom level 3 map.

Unexplored areas of a framed map are transparent, making the item frame visible.

- An item frame with a partially filled map
- Item frame markers on a held map

### Banner markers

  

This feature is exclusive to  Java Edition. 


All banners marked on a map, alongside a named banner.
In Java Edition, the player can also mark spots on a map by using a map on a placed-down banner. The mark takes the color of whatever the base color is for the banner, and if the banner has a name, the mark shows that name. Banner marks on a map are always oriented with their top facing north, regardless of the banner's actual orientation. If the banner is destroyed, the mark of the banner remains at first, but if the player gets closer to where the banner previously was, it disappears as the area is updated on the map.

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
| Name                 | Ingredients                                                              | Crafting recipe | Description                                                                                                                                   |
|----------------------|--------------------------------------------------------------------------|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Explorer Map(cloned) | Empty Map+Ocean Explorer MaporWoodland Explorer MaporBuried Treasure Map | 23456789        | The output has the same map center as the input map, and the samemonument,woodland mansionorburied treasuremarker. Cloned maps are stackable. |


## Data values
### ID
Java Edition:

| Name      | Identifier | Form | Translation key                                                                                                                                                                                                                                                                           |
|-----------|------------|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Empty Map | map        | Item | item.minecraft.map                                                                                                                                                                                                                                                                        |
| Map       | filled_map | Item | item.minecraft.filled_mapfilled_map.buried_treasurefilled_map.explorer_junglefilled_map.explorer_swampfilled_map.mansionfilled_map.monumentfilled_map.unknownfilled_map.village_desertfilled_map.village_plainsfilled_map.village_savannafilled_map.village_snowyfilled_map.village_taiga |

Bedrock Edition:

| Name      | Identifier | Alias ID | Numeric ID | Form | Translation key                                                                                                    |
|-----------|------------|----------|------------|------|--------------------------------------------------------------------------------------------------------------------|
| Empty Map | empty_map  | emptymap | 515        | Item | item.emptyMap.nameitem.emptyLocatorMap.name                                                                        |
| Map       | filled_map | map      | 420        | Item | item.map.nameitem.map.exploration.mansion.nameitem.map.exploration.monument.nameitem.map.exploration.treasure.name |

### Metadata
See also: Bedrock Edition data values

In Bedrock Edition, maps use the following data values:

Empty map:

|  | DV | Description       |
|--|----|-------------------|
|  | 0  | Empty Map         |
|  | 2  | Empty Locator Map |

Filled map:

|  | DV | Description                                                       |
|--|----|-------------------------------------------------------------------|
|  | 0  | Map                                                               |
|  | 2  | Map (locator)                                                     |
|  | 3  | Ocean Explorer Map                                                |
|  | 4  | Woodland Explorer Map                                             |
|  | 5  | Treasure Map                                                      |
|  | 6  | Locked Map                                                        |
|  | 7  | Snowy Village Map[only experimental "Villager Trade Rebalance"]   |
|  | 8  | Taiga Village Map[only experimental "Villager Trade Rebalance"]   |
|  | 9  | Plains Village Map[only experimental "Villager Trade Rebalance"]  |
|  | 10 | Savanna Village Map[only experimental "Villager Trade Rebalance"] |
|  | 11 | Desert Village Map[only experimental "Villager Trade Rebalance"]  |
|  | 12 | Jungle Explorer Map[only experimental "Villager Trade Rebalance"] |
|  | 13 | Swamp Explorer Map[only experimental "Villager Trade Rebalance"]  |
|  | 14 | Trial Chambers Map[only experimental "Update 1.21"]               |



### Item data
Java Edition:

Main article: Item format

 tag: The item's tag tag.
 map: The map number.
 map_scale_direction: Only internally used when scaling a map, after that directly removed: The amount to increase the current map scale by when crafting. Always 1.
 map_to_lock: 1 or 0 (true/false) - true if the map should be locked after being taken out of the cartography table. Only internally used when locking a map, after that directly removed.
 Decorations: A list of optional icons to display on the map. Decorations that are removed or modified do not update until the world is reloaded.
 An individual decoration.
 id: An arbitrary unique string identifying the decoration.
 type: The ID of the map icon to display.
 x: The world X position of the decoration.
 z: The world Z position of the decoration.
 rot: The rotation of the symbol, ranging from 0.0 to 360.0, measured clockwise. A rotation of 0 displays the icon upside-down compared to its appearance in the icon texture.
 display: The display tag.
 MapColor: The color of the markings on the item's texture.

Bedrock Edition:

See Bedrock Edition level format/Item format.
### Map icons

  

This section needs to be updated. 
Please update this section to reflect recent updates or newly available information.Reason: New structure icons and changed structure icons in Bedrock Edition (Java Edition ones have been updated).


See also: Player.dat format, Map item format and map_icons.png

Map icons are 8×8 in Java Edition, but 16×16 in Bedrock Edition. As such, there are minor misalignment issues in Java Edition.[1]

Map icons texture in Java Edition
Map icons texture in Bedrock Edition
| Java ID | Bedrock ID | Text ID           | Appearance                                         | Purpose                                                                                                                    | Shown in item frames? |
|---------|------------|-------------------|----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|-----------------------|
| 0       |            | player            | White marker                                       | Players (on map); inBedrock Edition, dynamically recolored for other players or players in the Nether or End               | No                    |
| 1       | 1          | frame             | Green marker                                       | The current map in an item frame                                                                                           | Yes                   |
| 2       |            | red_marker        | Red marker                                         | Unused                                                                                                                     | No                    |
| 3       |            | blue_marker       | Blue marker                                        | Unused                                                                                                                     | No                    |
| 4       |            | target_x          | White X                                            | Unused                                                                                                                     | Yes                   |
| 5       | 5          | target_point      | Red triangle                                       | Unused                                                                                                                     | Yes                   |
| 6       | 6          | player_off_map    | Large white dot                                    | Players off map, nearby‌[Java Edition  only]                                                                               | No                    |
| 7       | 13         | player_off_limits | Small white dot                                    | Players off map, far away‌[Java Edition  only]                                                                             | No                    |
| 8       | 14         | mansion           | Woodland mansion                                   | Woodland mansion                                                                                                           | Yes                   |
| 9       | 15         | monument          | Ocean monument                                     | Ocean monument                                                                                                             | Yes                   |
| 10 - 25 |            | banner_*          | Banners in all 16 wool colors‌[Java Edition  only] | Banner markers                                                                                                             | Yes                   |
| 26      | 4          | red_x             | Red X                                              | Buried treasure                                                                                                            | Yes                   |
|         | 8          |                   | Magenta marker                                     | Unused                                                                                                                     | No                    |
|         | 9          |                   | Orange marker                                      | Unused                                                                                                                     | Yes                   |
|         | 10         |                   | Yellow marker                                      | Unused                                                                                                                     | No                    |
|         | 11         |                   | Cyan marker                                        | Unused                                                                                                                     | No                    |
| -       | 12         |                   | Green triangle                                     | Other structure such as stronghold, fortress, end city, etc. when used as explorer map destination‌[Bedrock Edition  only] | Yes                   |
| 27      |            | desert_village    | Desert village                                     | Desert village                                                                                                             | Yes                   |
| 28      |            | plains_village    | Plains village                                     | Plains village                                                                                                             | Yes                   |
| 29      |            | savanna_village   | Savanna village                                    | Savanna village                                                                                                            | Yes                   |
| 30      |            | snowy_village     | Snowy village                                      | Snowy village                                                                                                              | Yes                   |
| 31      |            | taiga_village     | Taiga village                                      | Taiga village                                                                                                              | Yes                   |
| 32      |            | jungle_pyramid    | Jungle pyramid                                     | Jungle pyramid                                                                                                             | Yes                   |
| 33      |            | swamp_hut         | Swamp hut                                          | Swamp hut                                                                                                                  | Yes                   |

It should be noted that even if the player used a NBT editor to add an additional icon on the map, Minecraft shows only the first one listed when the player loads up their world.

## See also
- Explorer Map
- Clock
- Navigation

