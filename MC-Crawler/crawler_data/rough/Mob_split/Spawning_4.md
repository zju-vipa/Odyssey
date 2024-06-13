### Bedrock Edition
Environmental spawning in Bedrock Edition shares broad similarities to natural spawning in Java Edition: mobs spawn in a radius around the player subject to block conditions, lighting conditions, biome conditions, naturally generated structure conditions, and caps. Many mobs spawn in groups (called "packs" in Java and "herds" in Bedrock). One notable difference from Java Edition is that most animals can spawn at light level 7 or higher rather than 9 or higher. 

There are two types of environmental spawns: cluster spawns and structure spawns. Structure spawns reproduce specific types of mobs at specific locations within certain naturally generated structures, such as nether fortresses, swamp huts, etc. Cluster spawns account for all other types of environmental spawns, including mobs that spawn individually (i.e. not in a herd of 2 or more). Both types of environmental spawns follow the same rules for spawn conditions and mob caps, except that structure spawns can exceed the monster population cap by 1 (see below). 

Mob spawning in bedrock edition happens within a spherical shell 24-44 blocks away from the player on simulation distance 4. It happens a quasi-spherical shell 24-128 blocks away from the player, restricted by a simulation distance and/or to roughly 96 blocks horizontally, on simulation distances 6 and higher. This means that mobs can spawn directly above or below the player (for example, phantoms in the sky or zombies underground). Mobs can spawn only in chunks that are being ticked. There is a 11⁄2000 chance of the mob spawning algorithm attempting to run per chunk, per tick.

#### Bedrock Edition mob cap
There are three mob caps that affect environmental spawning: a global mob cap, population control caps for general mob types, and density caps for specific mob types. The global mob cap is set at 200 regardless of difficulty. The global mob cap affects only environmental mob spawning, and does not affect mobs spawned through breeding, spawn eggs, the /summon command, monster spawners, or any other type of mob spawning. Chickens created by thrown or dispensed eggs are counted in the global mob cap. Only mobs that have spawn rules count toward the global cap (i.e. armor stands and minecarts do not take up cap space). In addition, mobs that are within ticking areas (both those around players and those set manually using the /tickingarea command) count toward the global mob cap; mobs not ticked do not count toward the global mob cap.

The population control caps limit how many mobs of each type and category can spawn within a 9 chunk by 9 chunk square region surrounding the chunk in which the spawn attempt is made. Mobs in chunks outside a ticking area still count toward population control counts as long as they were previously loaded (i.e. within simulation distance at some time) after relogging. The population control caps are split up into two distinct categories: a cap for surface mobs, and a cap for cave mobs. Cave mobs do not count toward the surface mob cap, and surface mobs do not count toward the cave mob cap. Whether a mob counts as a surface mob or a cave mob is determined by where or how it spawned, not where it happens to be at the moment. For cluster spawns, those that spawn on the highest spawnable block at a given coordinate count toward the surface cap, and any that spawn below the highest solid or non-solid but spawnable (e.g. ice or upper slab with air above) block count toward the cave cap. Structure-spawned mobs and converted mobs (i.e. drowned converted from zombies, witches from villagers, zombified piglins from pigs, and medium and small slimes from killed larger slimes) always count toward the cave cap, and monster-spawner-spawned mobs always count toward the surface cap.

There are five categories of mobs: ambient, animal, monster, pillager, and water_animal. The population control cap for each category and location of mob in each dimension is as follows (* denotes values that are coded in the game but not actually used by any mobs):

| Category     | Location | Overworld | Nether | The End |
|--------------|----------|-----------|--------|---------|
| Ambient      | Surface  | 0         | 0      | 0       |
|              | Cave     | 2         | 0      | 2*      |
| Animal       | Surface  | 4         | 0      | 4*      |
|              | Cave     | 0         | 4      | 0       |
| Monster      | Surface  | 8         | 0      | 10      |
|              | Cave     | 16        | 16     | 8*      |
| Pillager     | Surface  | 8         | 0      | 8*      |
|              | Cave     | 8         | 0      | 8*      |
| Water_Animal | Surface  | 36        | 0      | 36*     |
|              | Cave     | 0         | 0      | 0       |

Some specific mobs types also have their own density caps. The density caps limit the number of those mobs to some amount below the applicable population control cap. Density caps are checked in the same manner as the population control caps. Caps are below (n/a indicates that the mob does not spawn in that environment at all).

| Mob           | Surface cap                                     | Cave cap                                         |
|---------------|-------------------------------------------------|--------------------------------------------------|
| Cod           | 20                                              | n/a                                              |
| Creeper       | 5                                               | unlimited (population control cap still applies) |
| Dolphin       | 5                                               | n/a                                              |
| Drowned       | 5 in ocean<br/>2 in river                       | n/a                                              |
| Ghast         | n/a                                             | 2                                                |
| Phantom       | 5                                               | n/a                                              |
| Pufferfish    | 3                                               | n/a                                              |
| Salmon        | 10 in ocean<br/>4 in river                      | n/a                                              |
| Squid         | 4 in ocean<br/>2 in river                       | n/a                                              |
| Tropical Fish | 20 for preset pattern<br/>20 for random pattern | n/a                                              |

#### Bedrock spawn conditions
See also: Simulation Distance

The following rules apply to most mobs:

- Mobs spawn at a distance from the player that depends on the world'ssimulation distance:
	- Simulation distance 4: between 24 and 44 blocks spherical radius from the player.
	- Simulation distance 6 and up: between 24 and 128 blocks spherical radius from the player, but limited horizontally by simulation distance and coding that restricts the spawning algorithm from running in chunks whose center exceeds 96 blocks from the player.[5]
- The bottom part of the mob (i.e. the feet of a standing mob) can spawn onlyinan air block, or for water mobsina water block. A few naturally-generated, non-motion-blocking blocks such as grass and flowers are ignored for this rule. If the mob spawns in a flower the block above the flower must be air.
- The bounding box of the mob must not intersect any solid blocks. Mobs can spawn intersecting leaves, glass, and other transparent blocks.
- There must be a block with a full, solid top surface under the spawn location for the mob to spawnon. (I.e. mobs cannot spawn on carpets, lower slabs, fences, right-side-up stairs, redstone repeaters, chests, etc.)
- Mobs cannot spawn on transparent full blocks like glass and leaves.
- For mobs that can spawn floating in water or flying in air, the block that is checked for spawning is the water or air block immediately above the first solid top surface block below the spot where the mob would spawn. (So for example, phantoms cannot spawn over a field covered in carpet, and fish cannot spawn in an ocean where bottom slabs cover the ocean floor.)
- Most overworld monsters cannot spawn if the sky light level is greater than or equal to 7 or the block light level is greater than 0.
- Most overworld animals cannot spawn if the (combined) light level is less than 7.

