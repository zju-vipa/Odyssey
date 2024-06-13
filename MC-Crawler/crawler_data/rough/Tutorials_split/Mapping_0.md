# Tutorials/Mapping

The map page explains how to craft maps and how they automatically draw themselves as you move through the world. That page also explains maps' limitations and pitfalls. For example, crafting a batch of maps all at once (using shift-click) is generally not helpful because they'll all be duplicates of one another.

## Contents
- 1 Map sets
- 2 Map basics
- 3 Mapping step-by-step
- 4 Track maps' relative positions
- 5 Avoiding overlaps
- 6 Changes in Bountiful Update

## Map sets
3 zoom levels of maps shown side-by-side: levels 0, 1, and 2.
When crafting sets of maps, there are two approaches. The first is to travel well outside the current map's edge before crafting a new map, which will conserve map-crafting resources and keep confusingly redundant map space to a minimum. The other method is to deliberately ensure an overlap so that it's easier to find the same landmarks on multiple maps.

The zoom-levels introduced in the Pretty Scary Update make the 'overlap' technique of little benefit on any map at zoom level 0 (none) through 3, because an overview map at the next zoom level 'stitches' the maps together.

## Map basics
Regardless of which technique is used, it's helpful to be systematic in the order you craft the maps. For example, you might make Map #0 (prior to the Pretty Scary Update this was designated "map_0") at the center of the area you want to cover.  When maps are crafted (eight paper surrounding a compass) they are initially "Empty Maps" (data value 395).  Holding an empty map and right clicking with it will activate it (data value 358) and draw the current terrain to a radius of 100-120 blocks.  The map will be centered on a block that is a multiple of 128 on the x & z axis and will cover an area of 128×128 blocks.  Thus, if you are at or near the center block, a zoom-level 0 map is nearly complete when crafted from an empty map.  

If you want to keep that map, you should duplicate it at that point by placing it and an "Empty Map" on your crafting area or table.  If one of those is then placed in the center of a crafting table and surrounded by eight paper, a zoom-level 1 map is crafted.  This map will cover an area 256×256 blocks and would be labeled "Map #1" (assuming no other maps were created in the meantime).

This "zoom-out" step can be repeated three more times with each resultant map, yielding Map #2 (512×512), Map #3 (1024×1024), and Map #4 (2048×2048).

## Mapping step-by-step
(The numbering below assumes that you create only the maps discussed here and that no one else is creating maps.)

To start, move to a spot within 64 blocks of 0,0 (x and z coordinates should each be between -64 and 64) and activate an Empty Map (Map #0).  Duplicate it and use the duplicate to craft a zoom-level 1 (Map #1).  Use Map #1 to create a zoom-level 2 map (Map #2), and use that to craft a zoom-level 3 map (Map #3).  Duplicate Map #3 and use one to craft a zoom-level 4 map (Map #4) which will provide you with an overview map.  This zoom-level 4 map will provide you with a good general orientation—there is a lot of territory to explore within a 2048×2048-block area.  

To create a set of zoom-level 3 maps which will better show structures  you should then move north to a spot approximately (within 64 blocks) of 0,y,1024.  Here, craft a new zoom-level 0 map (Map #5) from an Empty Map.  Zoom it out to a zoom-level 3 map (Map #8) which will be retained.  Then travel east to a spot within 64 blocks of 1024,y,1024.  Craft a zoom-level 0 map (Map #9) and zoom out to a zoom-level 3 map (Map #12) which will be retained.  Continuing clockwise, you would proceed south repeat the craft-and-zoom process at:

| map #   | x-coord | z-coord | relative position |
|---------|---------|---------|-------------------|
| Map #16 | 1024    | 0       | E, 3:00           |
| Map #20 | 1024    | 1024    | SE, 4:30          |
| Map #24 | 0       | 1024    | S, 6:00           |
| Map #28 | -1024   | 1024    | SW, 7:30          |
| Map #32 | -1024   | 0       | W, 9:00           |
| Map #36 | -1024   | -1024   | NW, 10:30         |

You will now have nine zoom-level 3 maps which cover completely the territory shown by the zoom-level 4 overview map.  The set of 9 zoom-level 3 maps actually cover 512 blocks beyond the zoom-level 4 map.  Each will be centered on the border of the zoom-level 4 map (and four of which will be centered on the corners of the level-4 map).  You can, of course, retain any of the intermediate maps by duplicating them before you zoom them.  If you don't duplicate before zooming, you won't be able to obtain them again without using server commands (e.g., "/give <player> 358 1 <map#>", where "358" is the data value for a map and 1 is the number of maps to give) or inventory editors.

## 
It's helpful to keep track of the relative positions of the maps. A useful method of displaying the map set is to craft 10 item frames and place them on a wall in a 3-by-3 square with the tenth atop or beside the square.  Place the zoom-level 4 overview in the tenth item frame.  Place the nine maps in their appropriate positions in the 3×3 square.  A sign can be added which identifies the origin and perhaps the corner coordinates.  You could also duplicate any of these which you wish to carry with you while fully exploring an area.  Information added to one copy will be automatically updated to all other copies.  (Note that crafting a second map of the same area—not duplicating, but crafting anew—will create a map that is NOT linked to the original version, and it will thus NOT be updated even though it covers exactly the same area.)

Set of maps in item frames before 1.8
In the illustration, the sign provides the map # of each of the maps shown.  Map #127 is the center map. Map #185 is the map to the north, #189 to the right of that, and the numbering continues clockwise.

As another option, use a chest, and store the maps in slots in the chest that correspond with their in-world positions. If you use this trick, be careful to put them back in the right place once done with them.

You could also craft a Book & Quill (data value 386) in which you can write descriptions of what the map-set covers.  This is a useful place to make notes of interesting spots found on those maps.  That Book & Quill can be placed in an item frame next to the map set.

Another trick is to name maps on an anvil. You can name a map for its center or its position relative to other maps, i.e. (0,0) at the origin of your mapping, (0,1) one map east of the origin.

