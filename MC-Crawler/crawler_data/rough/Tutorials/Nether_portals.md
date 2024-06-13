# Tutorials/Nether portals
The creation of nether portals can be used for a variety of different means. This page lists some of the implications of these portal mechanics.

## Contents
- 1 First, portals are risky
	- 1.1 Portals can accumulate Overworld mobs
- 2 Making a portal
	- 2.1 Farming obsidian
	- 2.2 Creating a portal without getting obsidian
		- 2.2.1 A quick, simple method using a lava pool, water bucket, and some blocks
- 3 How portals work
	- 3.1 Pairing portals
	- 3.2 Zones of exclusion
	- 3.3 2-in-1 Nether portals
	- 3.4 Spawning a portal in the air or buried.
- 4 Using portals
	- 4.1 Portals can be built-in networks
	- 4.2 1-way long distance teleport
	- 4.3 Non-exploit water ladder replacement
- 5 References

## 
Portals try to avoid spawning over lava, in midair, or inside rock, but they do so by spawning nearby. Thus, a new portal from the Overworld has a disproportionate chance of being next to an abyss, lava lake, or netherrack wall. There is also no way to check whether a lava source (created with the landscape) is destined to send lava flowing over the portal. Furthermore, a portal can spawn on a one-block thick ledge or floor, or on a Soul Sand outcrop.

### Portals can accumulate Overworld mobs
Portals built in the Overworld should be secured in order to prevent wandering monsters from entering the portal. These creatures can accumulate over time in the Nether; not only is there no sunlight to burn undead, but without a player present, time barely passes for them (15 seconds for each new entry) so they may not have time to despawn. Mobs such as creepers are especially bad to handle in the Nether due to the soft nature of netherrack and the abundance of lava to fall into.

## Making a portal
### Farming obsidian
See Tutorials/Obsidian farming.

### Creating a portal without getting obsidian
Nether portals can be built without the use of a diamond or netherite pickaxe to mine obsidian by placing lava in a mold of other blocks, and then pouring water over it to turn it into obsidian.

| Dirty Nether Portal Guide (view on YouTube) |
|---------------------------------------------|
|                                             |

#### 
You need at least 6 blocks, a water bucket, a lava pool, and a flint and steel or other lighting method. A block breaking tool is recommended.

1. Start by placing a block at the edge of a lava pool.
2. Place water to the left of the block.
3. Destroy the block.
4. Pick up the water.
	- If the bottom two blocks are made of obsidian, then everything is going fine, as you need all 4 of the obsidian so far. Continue to step 5.
	- If the bottom two blocks are NOT made of obsidian, you need to destroy those blocks. After destroying those blocks, fill them with lava and use flowing water to solidify them with obsidian. Once you have all 4 obsidian blocks there, you can continue to step 5.
5. Place those two blocks.
6. Place those four blocks.
7. Place water.
8. Grab the water and light the nether portal with a flint and steel. To get that, you need gravel and iron.

## How portals work
Portals try to link up at their equivalent location calculated by Overworld (X,Y,Z) <=> Nether (X/8, Y, Z/8).  But as they say, the devil is in the details:

- First the game calculates the "ideal" destination coordinate as above, dividing or multiplying the traveler's X and Z coordinates by 8.  It then searches for existing portals (actual portal blocks) within nearby chunks.
	- If going to the Nether it searches a 33×33 block area (centered on the "ideal" coordinates).
	- If going to the Overworld, it searches a much larger area, 17×17 chunks (that is, up to 8 chunks away from the original point).
	- In either dimension, the entire vertical range of the world is scanned.
	- For any column of portal blocks (such as the two 3-high columns of a "standard" portal), only the bottom one is considered.
	- If any portals are found in this range, the traveler is teleported to theclosestof them, based on the Euclidean (nottaxicab) distance inall threecoordinates.  Differences in the Y coordinate can bypass the portal that's closest in only X and Z!
- If no portals are found within range, the game sets out tomakea portal:
	- It searches within 16 blocks horizontally (but any distance vertically) of the player's destination coordinates.
	- For the first pass, a valid location is 3×4 buildable blocks with air 4 high above all 12 blocks. When enough space is available, the orientation of the portal is random. The closest valid position in the 3D distance is always picked.
	- If no such space is found, it tries again looking for a narrower fit:  A1x4 area of buildable blocks, still with air 4 high above them.
	- If both of the above fail, the gameforcesa portal:
		- The ideal X and Z coordinates are used, but Y is clipped to be between 70, and 10 below the world height (i.e. 118 for the Nether or 246 for the Overworld).
		- A 2×3 platform of obsidian with air 3 high above is created at the target location, overwriting whatever might be there. This provides air space underground, or a small platform if high in the air. InBedrock Edition, the platform includes 4 more blocks of netherrack on each side, a total of 12 blocks of platform.
	- When creating a portal, the game always makes a 4×5 frame of obsidian, including corner blocks.

### Pairing portals
To set up pairs of Nether portals properly so that they reliably travel to each other, it is best to build both portals manually. Build at desired location X,Y,Z in the Overworld. Then travel to the Nether. And then dig your way to X/8, Y, Z/8, and build a portal there. 

As block coordinates are centered on the lower northwest corner of blocks, higher precision can be achieved by placing a portal in the nether where block coordinates are the least precise relative to the Overworld, recording the block coordinates, and adding 0.5 to each value before multiplying it by 8 to find the ideal Overworld coordinates. This can allow portals as close as 8 blocks to behave reliably in the Overworld, and can make adjacent portal blocks in the nether reliably teleport to different overworld portals as well.  Even greater precision can be achieved when considering that teleportation from the Nether to the Overworld uses the player's coordinates without rounding -- thereby making it possible to have reliable, if difficult to use, portals as close as 1 block. Precisely linked portals can also be stacked vertically without interfering with one another.  

A less precise method would be to temporarily deactivate all portals within a 128 block "radius" from within the Nether. Through death or with the aid of a second player, entering a new portal from the Overworld forces the creation of a new portal within the Nether which the overworld portal should prefer. This is not recommended as it limits how close overworld portals can be placed due to the zone of exclusions and can lead to unpredictable placement of the resulting portal.

The Y coordinate is not divided for pairings, however it does play a factor in mapping the portals. Therefore, two overworld portals could be built at the same x,z coordinates with one at a very low Y, e.g., 5, and one at a higher y, e.g. 160.  A Nether portal at these X and Z coordinates links to whichever portal is closest on the Y axis.

If this all sounds complicated to you, this website can help you in the process: https://gamertools.net/applications/nether.

### Zones of exclusion
The nether portal spawning algorithm can only spawn a portal within a 33×33 block column centered on the destination, but it does scan that width (and the height of the world) for open space to place the portal. This often causes it to spawn a portal at a location significantly different than the corresponding location in the other world. The larger the distance between a portal and its "ideal" destination, the larger the zone of exclusion. This zone is the area in each world where you cannot build another portal without breaking the link between the first two portals. One way to think of this zone is as spheres around each portal, each of a true radius equal to its distance to the equivalent location of the other. For example, if the overworld portal was at (0,50,0) and the Nether portal at (0,100,0), then the portals are 50 meters away from each other. In this (simple) case, if a nether portal was built closer than 50 meters to (0,50,0), then the Overworld portal links to it.  

Because of the coordinate change, portals created in the Nether are much more likely to have ideal coordinates that are horizontally distant from the overworld portal that created them. When going the other way, horizontal coordinates tend to be closer to ideal (because whatever space is found has a Nether-equivalent location closer to the original portal), but vertical displacement can still be an issue.   

If you wish to ensure that two portals link together, manually build portals as close as possible in all 3 coordinate axes. It doesn't have to be exact, or even all that close, if the player ensures that no other portals is constructed in the exclusion zone created by the difference.

### 2-in-1 Nether portals
It is possible to end up in a situation where a nether portal "randomly" places the player in 1 of 2 possible overworld destination portals. This is simply because the nether portal has two effective coordinates as it is 2 blocks wide, say (X, Y, Z) on the left, and (X+1, Y, Z) on the right. If the player entered on the left side, (X, Y, Z) translates to (X*8, Y, Z*8) in the overworld and the game picks the portal closest to that. If the player entered on the right side, (X+1, Y, Z) translates to (X*8+8, Y, Z*8) and the game picks a portal closest to that point instead. This situation occurs when the nether portal's location is roughly equidistant between the 2 overworld portals (within 8 blocks overworld distance difference). However, building 2 nether portals side by side is probably better for destination clarity than building a 2-in-1 portal. It is possible to span distances with pairs of portals in this way, though normally faster to simply walk through the Nether.[1]

### Spawning a portal in the air or buried.
It is possible for a destination portal (either in the Nether or in the Overworld) to spawn floating in the air, or buried in netherrack or stone. If your portal spawns in the air, it generates a 1×2×1 obsidian platform in the front and back of the portal.  If it spawns in rock, a 3-high airspace is cleared out for one block on each side of the portal. This can only occur if there there are no existing portals within range to link to, and there is no suitable spot to place a new portal within 16 blocks horizontally (at any height) of the target coordinates. This usually means that floating portals spawn over the ocean (in the Overworld) or lava ocean (in the Nether), and buried portals are much more likely in the Nether.

## Using portals
### Portals can be built-in networks
You should build portals at 64 Nether block intervals, even if you are not normally going to use these gates. (This is the maximum ideal distance, but they can be built as close to 8 Overworld blocks apart, if the coordinates are precise.) This is so that if you use nether portals for long-distance travel, and your usual Overworld destination portal becomes inaccessible for some reason, (due to large gravel cave-ins, lava, water, or you have an automated activation system and forgot to turn it on) you still have a reasonably close backup gate, which returns you into your gate network.

### 1-way long distance teleport

  

This section describes content that exists only in outdated versions of Minecraft. 
The portal search range has been changed in Java Edition 1.16.2.


The portal choosing algorithm can be used for long-distance travel by manual construction at carefully selected coordinates. If the player has a portal in the Overworld at (0,64,0) but makes a nether portal at (127,64,127) with its perfect Overworld pair at (1016, 64, 1016), then the portal at (0,64,0) goes to the nether portal correctly (1-way trip) because it is the only portal available within the 128 search distance along X and Z horizontal axes of the expected Nether portal position of (0,64,0). In about 15 seconds, the player can then travel 1436 meters in the Overworld. This specific form of fast travel by portal is one-way, since the nether portal cannot find this overworld portal. Given that a railway in the nether would need to span only 180 meters to go this distance, it is usually not worth making such portal links. However, it is theoretically possible to make a one-way ring of portals, with each Overworld to Nether jump going a long distance, but such a ring would easily be disrupted due to the huge exclusion zones created.[2]

### Non-exploit water ladder replacement
The Nether portal is an also entirely viable, two-way replacement for the water or conventional ladder.[3] Note that if you want to travel a vertical distance of h from a point (X, Y, Z) in the Overworld to (X/8, Y+h, Z/8) in the Nether, there must be no other Overworld portal at any point (x, y, z) within a distance of 8*h from (X, Y, Z) (i.e. within the spheroid ((x-X)/8)² + ((y-Y)/1)² + ((z-Z)/8)² = h², note that Y is not divided by 8). That is, if you want to travel large vertical distances, there must be no horizontally close portal. (This holds for a portal from the Overworld to the Nether. The reverse direction (Nether to Overworld) was not discussed here.)

