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


