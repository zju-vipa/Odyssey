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


