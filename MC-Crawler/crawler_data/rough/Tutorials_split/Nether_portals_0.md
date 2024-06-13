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

