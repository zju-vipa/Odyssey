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
| Ingredients        | Crafting recipe | Description                                                                                                                            |
|--------------------|-----------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Paper+<br/>Compass |                 | This map is called an "Empty Locator Map" inBedrock Edition, and an "Empty Map" inJava Edition. It has the same uses in both editions. |
| Paper              |                 | ‌[Bedrock Edition  only]This map is called an "Empty Map". It only records terrain and does not show location markers.                 |

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

1. ↑Named unknown map, but changed to map 0, the scale level is 1:4, Maps from the same stack are stackable, but maps that are not stacked are unstackable despite looking identical.

### Trading
Novice-level cartographer villagers sell a single empty map for 7 emeralds as their trades.

In Java Edition, cartographer villagers may give players with the Hero of the Village effect an empty map.

## Usage
### Mapping
Crafting a map creates an empty map. The map is drawn for the first time when it is held and used (by pressing the use item control). After conversion to a drawn map item, it starts to draw a top-down view of the player's surroundings, with North pointing to the top of the map. A pointed oval pointer indicates the player's position on the map, and moves in real-time as the player moves across the terrain shown on the map. In Bedrock Edition, this pointer is displayed exclusively on locator maps.

The map grid at different zoom levels
The map does not center on the player when created; rather, the world is broken up into large invisible grid squares, and the map displays the area of whichever grid square it was in when it was first used. For example, if a player uses a new map in a certain grid square, and then moves a distance away and uses another fresh map but is still within the same grid square, both maps still have the exact same boundary. To make a map with different bounds than the first one, the player would have to move outside of the edges of the first map (because then they would be in a new grid square). This way, no two maps of the same size can ever partially overlap.

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

