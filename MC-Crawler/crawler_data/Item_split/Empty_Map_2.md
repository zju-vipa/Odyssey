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

