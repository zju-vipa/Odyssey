# Nether portal
A nether portal is a manufactured structure that acts as a gateway between the Overworld and the Nether dimensions.

## Contents
- 1 Creation
- 2 Behavior
	- 2.1 Chunk loading
	- 2.2 Portal linkage between Overworld and Nether
		- 2.2.1 Coordinate conversion
		- 2.2.2 Portal search
		- 2.2.3 Portal creation
- 3 Sounds
- 4 Achievements
- 5 Advancements
- 6 Video
- 7 History
	- 7.1 History of the structure itself
	- 7.2 Other historical info
- 8 Issues
- 9 Trivia
	- 9.1 Publicity
- 10 Gallery
	- 10.1 Screenshots
	- 10.2 In other media
- 11 References

## Creation
|  |  |  |  |
|--|--|--|--|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

|  |  |  |  |
|--|--|--|--|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

A nether portal is built as a vertical, rectangular frame of obsidian (4×5 minimum, 23×23 maximum). The four corners of the frame are not required, but portals created by the game always include them, resulting in 4 free/extra obsidian. The obsidian can be placed in any manner, e.g. by placing mined obsidian, by completing a ruined portal, or by casting it in place using lava and water. Adjacent portals can share obsidian blocks. A nether portal cannot be built horizontally like an end portal.

Once a frame is constructed, it is activated by fire placed inside the frame. This creates portal blocks inside the frame, resembling a vortex. The fire can be placed in any manner, including use of flint and steel or a fire charge, the impact of a fireball or small fireball, a lightning strike, or natural spread of fire to flammable material adjacent to the portal. Nether portals can be activated only in the Overworld or the Nether; they cannot be activated in the End and custom dimensions.

The fire must be the last placed block in the structure—a fire on an incomplete frame does not result in the portal activating upon the placement of the last obsidian block.

When a portal is used by a player, if no corresponding portal within range exists in the other dimension, one is created there; see § Portal search and § Portal creation. There is an infinitesimal chance of failure for the corresponding portal to generate in the Nether, leaving the player trapped until death or until another portal can be constructed, either in the Nether or by another player in the Overworld.

## Behavior
Main article: Nether Portal (block)
When a player in the Overworld or the Nether stands in a nether portal block for 4 seconds, the player is taken to the other dimension. The player can step out of a portal before it completes its animation to abort the teleport. However, in Creative, the wait time is one game tick (1⁄20 second) for the player to transfer between dimensions. If there is already an active portal within range (about 128 blocks) in the other dimension, the player appears in that portal. Otherwise, a portal is created at or near the corresponding coordinates. If a portal is deactivated, and the matching portal in the other dimension is used before it is re-activated, a new portal may be created (unless there is another active portal within range). The usual cause for this is when the player's Nether-side portal is deactivated by a ghast, and then the player dies in the Nether, spawns, and then re-enters the Nether through the Overworld-side portal. However, multiple portals can be exploited to farm obsidian.

Most entities can travel through portals, including mobs (except the wither and ender dragon), thrown items, and transportation without passengers (neither mobs nor player)[1], including boats, minecarts and horses. Unlike players, other entities travel through portals instantly, and once they reach the other side, there is a cool-down time for 300 game ticks (15 seconds), in which they cannot go through any nether portals. Therefore, an entity can travel though nether portals again after not touching any nether portal for 15 seconds. In Bedrock Edition, a parrot on the player's shoulder prevents the player from going through the portal.[2]

Zombified piglins have a chance to spawn on the bottom frame of the portal in the Overworld in Java Edition if any nether portal block above receives a block tick. In Bedrock Edition they spawn in certain squares adjacent to the portals in the Overworld, not inside them. Zombified piglins spawned in this way have a full 15-second portal cooldown, meaning they can't go through the portal they are spawned in unless they leave the portal for a while. They spawn twice as often on Normal difficulty as on Easy, and three times as often on Hard difficulty as on Easy. No other mobs can be spawned by nether portals in this way, in any dimension.

Active portals also repel hoglins.

### Chunk loading

  

This feature is exclusive to  Java Edition. 


Main article: Chunk § Chunk loading
Whenever an entity is teleported through a nether portal, the chunk at the linked portal gets load ticked with load level of 30, meaning that it is fully loaded and can process entities. This load level also spreads to adjacent chunks but they get lower for each chunk. This results in 8 more fully loaded "entity ticking" chunks with gradually fewer loaded chunks further out.

These chunks remain loaded for 15 seconds but this timer gets refreshed each time the entity passes through the portal (including mobs wandering through it from either direction). This can be used to permanently load chunks, creating a "chunk loader". Permanently-loaded chunks created using chunk loaders create a considerable amount of lag.

### Portal linkage between Overworld and Nether
See also: Tutorials/Nether portals

The closest portal to the corresponding location receives the player.
A new portal is generated in the closest empty area if no portal is found in range.
#### Coordinate conversion
Horizontal coordinates and distances in the Nether are proportional to the Overworld in a 1:8 ratio. That is, by moving 1 block horizontally in the Nether, players have moved the equivalent of 8 blocks on the Overworld. This does not apply to the Y-axis. Thus, for a given location (X, Y, Z) in the Overworld, the corresponding coordinates in the Nether are (floor(X ÷ 8), Y, floor(Z ÷ 8)), and conversely, for a location (X, Y, Z) in the Nether, the matching Overworld coordinates are (X × 8, Y, Z × 8).

The Java floor() method used in these conversions rounds down to the largest integer less than or equal to the argument (toward smaller positive values and toward larger negative values), so a coordinate of 29.9 rounds to 29, and one of −29.9 to −30.

Both the X and Z coordinates in this conversion are constrained to be within the world border (29,999,983 and -29,999,984 (inclusive)); this affects travel to the Overworld from the Nether at X or Z beyond ±3,749,998.

An interactive widget is being loaded. If this does not work for you, please reload the page or check if JavaScript is enabled.
#### Portal search
When an entity starts colliding with a nether portal block, the game records the coordinates of the entity.

The game then converts those coordinates into destination coordinates as above: The entry X- and Z-coordinates are multiplied by 8 if the entity is in the Nether or divided by 8 if the entity is in the overworld, while the Y-coordinate is not changed.

Starting at these destination coordinates, the game looks for all nearby portal points of interest (POI). The point of interest can be within 128×128 blocks in the Overworld and 33×33 blocks in the Nether[3] centered on the converted coordinate and the full map height.

If any candidate portal POI is found, then the game selects the closest one as determined by its distance in the new coordinate system (including the Y coordinate, which can cause seemingly more distant portals to be selected), and teleports the entity to the location in the new portal calculated by a special algorithm. Note that the calculated distance is Euclidean distance, not taxicab distance. The distance computation between portals in the range is a straight-line distance calculation, and the shortest path is chosen, counting the Y difference.

The algorithm used for determining the position of the entity inside the destination portal to teleport to is as follows: 

- Portal rectangle dimensions are determined for both source and destination portals. (Not counting the obsidian)
- Entityhitboxdimensions are subtracted from those rectangles' width and height, meaning that the entity can now be considered as a point, to avoid problems with preserving the hitbox dimensions in a goemetrical transformation.
- Distance between the bottom of the source portal and the bottom of the entity hitbox is measured, similar is done for distance to one of the sides of the portal.
- Those offsets are then multiplied by the ratio of the reduced sizes of the portals and used to get the position in the destination portal.
- If one of the dimensions of entity hitbox is larger than the portal, the corresponing dimension falls back to bottom-middle of the destination portal, the other dimension is still calculated using the algorithm.
- If the destination portal is at 90° to the source portal, entity yaw and velocity are rotated 90° clockwise, interestingly regardless of the direction of travel, meaning that if player travels there and back without touching their mouse, they get rotated 180°, but the coordinates remain the same, making it appear as if the player exited through the wrong side of the portal.

This way, if source and destination portals are of the same shape, have the same orientation, and no other portals are interfering with the linking, one can safely assume that entities can travel through them as if the portal frames were physically placed behind each other.

#### Portal creation
For players, if no portals exist in the search region, the game creates one by looking for the closest suitable location to place a portal, within 16 blocks horizontally (but any distance vertically) of the player's destination coordinates. A valid location is 3×4 buildable blocks with air 4 high above all 12 blocks, with the long axis matching the long axis of the source portal. The closest valid position in the 3D distance is always picked.

If the first check for valid locations fails entirely, the check is redone looking for a 1×4 expanse of buildable blocks with air 4 high above each. 

If that fails, too, a portal is forced at the target coordinates, but with Y constrained to be between 70 and 10 less than the world height (i.e. 118 for the Nether or 246 for the Overworld). When a portal is forced in this way, a 2×3 platform of obsidian with air 3 high above is created at the target location, overwriting whatever might be there. This provides air space underground or a small platform if high in the air. In Bedrock Edition, these obsidian blocks are flanked by 4 more blocks of netherrack on each side, resulting in 12 blocks of platform.

Once coordinates are chosen, a portal (always 4×5 and including the corners) including portal blocks is constructed at the target coordinates, replacing anything in the way.

If a portal is forced into water or lava, the liquid immediately flows into the generated air blocks, leaving the player with no airspace. However, a glitch can prevent this water from flowing into the portal: if the liquid would flow both vertically and horizontally into the air pocket, it instead flows only vertically, so the blocks on the platform's outer corners never become water source blocks.

