# Distance
In Minecraft, the distance between two points is the measurement of how far apart the two points are. The sides of a block are considered to be 1 meter (3.28084 feet or 1250⁄381 feet) in length. Distance in the game is measured in one of three ways, Euclidean distance, taxicab distance, or Chebyshev distance, depending on whether geometric accuracy or calculation efficiency is required.

In the following formulas, let two points in three dimensions have coordinates (x1,y1,z1) and (x2,y2,z2) and let d be the distance between them.

## Contents
- 1 Euclidean distance
	- 1.1 Spherical distance
	- 1.2 Usages
- 2 Taxicab distance
	- 2.1 Usages
- 3 Chebyshev distance
	- 3.1 Usages
- 4 See also

## Euclidean distance
Euclidean distance, also known as straight-line distance, measures the distance between two points using the length of the line segment between them. It is calculated via the Pythagorean theorem and is found by:

d=(x1−x2)2+(y1−y2)2+(z1−z2)2
### Spherical distance
The set of points within a given euclidian distance, d, of some point, form a sphere with radius d centered at that point. This sphere is also reffered to as a Euclidian sphere.

### Usages
Minecraft uses Euclidean distance calculations in cases that are relatively infrequent or when accuracy is required. This is geometrically the most accurate calculation. However, the square root calculation is processor intensive, particularly on mobile devices that may have slow processors. Too many processor-intensive operations performed during a game tick can introduce lag in the game.

Situations in which Minecraft calculates Euclidean distance:

- The detection range of most mobs, if they have a line of sight to the target.
- The attenuation range of most sounds forms a Euclidean sphere with a radius of 16 blocks, centered on the source of the sound.
- Mobdespawning rangeinJava Edition.
- Disksin rivers and lakes generate as blocks within a Euclidean distance from a central block. (Small disks with a radius of up to three blocks including the center will appear identical to a taxicab diamond, however larger sizes correctly reveal a more circular morphology.)
- Effects ofexplosions.
- ALightning rodredirects lightning within a Euclidean sphere with a radius of 128‌[JE  only]/64‌[BE  only]blocks, centered on the rod.
- The/locatecommand prints the Euclidian distance from the caller to the located object in chat.
- Nether portalsearches for destination portals.
- Sculk sensorsand calibrated sculk sensors detect vibration emission in a spherical region.
- Splash potionsaffect mobs inside a Euclidean sphere with a radius of 4 blocks.
- Target selectorsused incommandsuse Euclidean distances.
- Azombie siegeis started based on Euclidean distance between a player and the village center.

- Map of silverfish damage from splash potion shows damage in a Euclidean distance from the potion.
- Visualization in Java Edition of various ranges related to mob spawning and despawning.
- A piglin's detection range of a player opening a chest.
- The detection range of a sculk catalyst.

## Taxicab distance
Taxicab distance as represented by Minecraft blocks rather than city streets.
Taxicab distance, also known as rectilinear distance, city block distance, Manhattan distance, and other names, is a metric in taxicab geometry for measuring distance, as an alternative to Euclidean distance. It eliminates the square root and squaring operations by simply calculating the absolute value (positive value) of the difference between each coordinate value and is defined as:

d=|x1−x2|+|y1−y2|+|z1−z2|
### Usages
Minecraft uses taxicab distance as an efficient range measurement in several elements of the game as it is a less accurate but faster calculation that can be done many times during a game tick. An obvious consequence of this calculation is that a taxicab "circle" drawn with a constant taxicab radius appears as a square whose vertices are in the directions of the axes (such as torch illumination), in which the taxicab radius equals the Euclidean radius only in the four cardinal directions (north, south, east, west), and the radius is shorter in all other directions. Similarly, in three dimensions, a taxicab "sphere" appears as an octahedron.

Situations in which Minecraft calculates taxicab distance:

- Lightfrom light sources such astorches,campfires,lanterns,glowstone, etc. illuminate surfaces according to taxicab distance.
	- As a direct result of this,torchesmeltsnowlayers within 2 blocks and ice within 3 blocks taxicab distance. Several other light-emitting blocks also melt snow in a taxicab radius; seeSnow § Melting.
	- Heat blocks‌[Minecraft Education  only]melt snow layers and ice within 2 blocks taxicab distance, but do not emit light.
- Liquid(waterorlava) flowing horizontally on a flat surface flows from the source in taxicab distance. For example, if flowing water is forced into a 1-block-wide stream and turns corners, it travels 7 blocks. If it is allowed to flow freely on a surface, it also travels 7 blocks taxicab distance.
- Redstone wiresignals spread this way, as can be seen if a large plane of the substance is laid out.
- Leversandbuttonsemit a redstone signal in a 1-block planar taxicab distance around them.
- InBedrock Edition,simulation distanceis the distance from the player at which blocks get tick updates (such as lightning strikes), and beyond which mobs despawn; this also uses taxicab distance.
- InBedrock Edition, amonster spawnerspawns mobs within a 4-block taxicab horizontal range from the monster spawner.
- Aspongeabsorbs water up to 7 blocks away in taxicab distance (an octahedral volume centered on the sponge).
- Leavesandscaffoldingdetermine their distance from the center via a "distance" block state determined by taxicab distance.
- PhantomsinJava Editionspawn 20–34 blocks above the player, and off to the side by a taxicab distance of up to 10 blocks.
- Usingbone mealonsea picklesthat are oncoral blockscreates more sea pickles on nearby coral blocks out to a horizontal taxicab distance of 2.
- Ablock of copperis oxidized according to a taxicab distance search for unwaxed copper blocks within 4 blocks of the block being considered for oxidation.
- Shulkerscan move along only one of the three grid axes at a time and on integer steps, meaning that they move according to taxicab geometry.
- Someredstonecomponents produceblock updatesup to two blocks away by taxicab distance, including up and down.

- Horizontal spread of water.
- Horizontal spread of lava.
- Taxicab illumination from various light-emitting blocks.
- The effect of simulation distance (the diamond area) on lightning strikes around a lightning rod.
- Redstone lamps melting snow.

