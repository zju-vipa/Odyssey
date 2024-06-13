# Spawn
Spawning refers to the creation and placement of players and mobs in the Minecraft world.

## Contents
- 1 Player spawning
	- 1.1 World spawn
		- 1.1.1 Bedrock world spawn search
		- 1.1.2 Adventure mode
		- 1.1.3 Location
	- 1.2 Individual spawn
- 2 Natural generation
	- 2.1 Animals
	- 2.2 Monsters
	- 2.3 Other mobs
- 3 Spawn cycle
	- 3.1 Java Edition
		- 3.1.1 Java Edition mob cap
		- 3.1.2 Pack spawning
		- 3.1.3 Spawn conditions
	- 3.2 Bedrock Edition
		- 3.2.1 Bedrock Edition mob cap
		- 3.2.2 Bedrock spawn conditions
		- 3.2.3 Cluster spawning
		- 3.2.4 Structure spawning
- 4 Other types of spawning
	- 4.1 General
	- 4.2 Passive mobs
	- 4.3 Hostile mobs
- 5 Despawning
	- 5.1 Java Edition
	- 5.2 Bedrock Edition
- 6 History
- 7 Issues
- 8 Trivia
- 9 Gallery
	- 9.1 Screenshots
- 10 References
- 11 External links

## Player spawning
### World spawn
World spawning area. White represents the extent of singleplayer, blue represents multiplayer, and yellow represents the world spawn point.
See also: Multiplayer spawning details

New players initially spawn within a small area surrounding the world spawn point when the server is not in Adventure mode. Upon death or return from the End dimension, the player respawns within this area unless the player's individual spawn point changed (by using a bed, respawn anchor, or /spawnpoint ).

This area is 21×21 blocks by default in Java Edition or 5×5 in Bedrock Edition, but can be changed by the spawnRadius gamerule in both single and multiplayer.

Bedrock Edition's Respawn Radius setting interface.
When set to 0, the player spawns in the crosshair of four blocks. When set to 1, the player always spawns on the northwest of those four blocks. The maximum spawn radius is 99999999 blocks but when rejoining the world, it resets to 128 blocks. However, in Bedrock Edition on the discontinued "Old" world type, the maximum spawn radius in 256 blocks instead.

Bedrock Edition's new respawn radius interface.
When the player first loads into the world or respawns, the game searches within the world spawn area and tries to place the player on a random grass block. Upon spawning, the player is placed on the highest valid spawn point block of the X and Z spawn coordinates, regardless of elevation. If a grass block that was invalid, due to being obstructed by a block above it, the game checks the closest two free spaces from below the grass block and the player spawns there. However, if there are no valid grass blocks, the player spawns directly at the world spawn point. The player is still placed at the highest valid block at the world spawn point. This can result in players falling into the void after spawning if there are no blocks at that location.

The world spawn point is also the center of the permanent spawn chunks.

The world spawn point can be changed using the /setworldspawn command.

#### Bedrock world spawn search

  

This section needs to be updated. 
Please update this section to reflect recent updates or newly available information.Reason: Spawn search rules have changed in 1.18; more biomes are available to spawn in.


In Bedrock Edition, when a player creates a new world, the world spawn point is restricted to specific biomes. The algorithm starts searching from coordinate 0,0, continuing outward until an acceptable biome is found for the world spawn point. Using add-ons, a rare biome can be designated to cause the player to spawn at a distant location, but the game crashes if the biome does not exist or cannot generate.

The algorithm searches for these biomes:

- Plains
	- At main plains biome
	- Small islands in anocean(islands are usually a plains biome)
	- Patch of plains next todesert,badlands, orsnowy plains
- Forest
	- At main forest biome
	- Small islands in anocean(islands can also be a forest biome)
- Dark Forest
- Taiga
	- At main taiga biome
	- Patch of taiga next toold growth pine taiga
	- Nearbeach,snowy taiga, orwindswept hills
- Jungle
- Savanna(only regular variants)

The player spawns within a 5-block radius of the point selected in the chosen biome, sometimes resulting in the player spawning outside the intended spawn biome, ending up in a beach, river, or swamp biome. It is also possible (but rare) for a player to spawn initially underwater and start drowning.[1]

A search for a valid world spawn biome is not performed for Flat and Old world-types.

#### Adventure mode
When the server's settings specify the default game mode as Adventure (using the server.properties), then the normal spawning mechanic is ignored, and players are spawned directly on the world spawn point. This includes the X, Y, and Z coordinates, even if there is no block there, and even if there are blocks above it.

If the Y coordinate is not within a valid spawning area, then the server looks up until it finds one, up to a maximum of Y=256. If there is space to spawn, but it is in mid-air, the player spawns in mid-air, even falling into the void if there is a hole.

#### Location
There are several ways to determine the world spawn point:

- Acompass(that hasn't been assigned to alodestone) always points to the world spawn point.
- Doing thecommands/gamerule spawnRadius 0then/kill.
- If commands are disabled, remove all thegrass blocksin the 21×21 spawn area (or place a block above them to make them invalid), make sure the individual spawn point is disabled, and die.
- Entities, other than players, falling into theexit portalinthe Endland exactly at the world spawn point. Items thrown in mark the spot in theOverworld. Players spawn like they normally do, allowing this action to be used to perform the above without dying, and thus can be performed inhardcore mode.
- Mods or external programs, such asNBTExplorerorMCEdit, can also be used to find and set the world spawn point.

### Individual spawn
The individual spawn point of the player can be changed by sleeping in a bed, using a respawn anchor, or using the /setworldspawn or /spawnpoint command. If the individual spawning area of the player is obstructed upon death, the player respawns at the world spawn.

Sleeping in a bed allows for leniency in obstruction, in that the player respawns on other blocks near the bed if the original point becomes blocked. The same is true for the respawn anchor. If the spawn point set via /setworldspawn or /spawnpoint becomes obstructed, the player is not given this leniency in respawning.

## Natural generation
### Animals
A cow that generated with the map inside a tree's leaves and could not escape, a common sight in forested hill areas.
In Java Edition many animals generate upon initial chunk creation. These spawns occur only once per chunk. They are not affected by the /gamerule doMobSpawning command.

One in ten newly-generated chunks attempts to generate animal mobs, usually in packs of up to 4 of the same species. The spawn attempt always starts on top of the highest available block in a randomly chosen column within the chunk. The chosen position must not be a solid block for the animals to generate. Once the starting position is chosen for a chunk, a second position is chosen in a 9×9 block area around the starting position. Blocks toward the center of the 9×9 area are more likely to be chosen than blocks toward the edge. The block does not need to be a grass block nor does it need to be illuminated as it does with mob spawning. If an animal can spawn at the second position, it does so. The second position becomes the first position, and a new second position is chosen like before in a 9×9 area. This process can repeat until each chunk has attempted to spawn 1–4 mobs.

In Bedrock Edition animals do not spawn during chunk generation, but they continually attempt to spawn everywhere as part of the environmental spawning algorithm, according to their spawn weights, biome tags, and block requirements (see Bedrock Edition under Spawn Cycle, below).

There are 2 types of animals: common animals and biome-specific animals.

** Common animals **
Common animal mobs do not spawn in desert, badlands, beach, snowy plains, river, ocean, or mushroom fields biomes. 

| Mobs    | Weight | Group size |
|---------|--------|------------|
| Sheep   | 6      | 4          |
| Chicken | 5      | 4          |
| Pig     | 5      | 4          |
| Cow     | 4      | 4          |



** Biome-specific animals **
Some animal mobs spawn only in specific biomes.[more information needed]

| Mobs                         | Biome                                                                                                                                          | Weight                                           |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|
| Axolotl                      | Lush Caves                                                                                                                                     | 4                                                |
| Cod                          | Ocean<br/>Lukewarm Ocean<br/>Cold Ocean<br/>Frozen Ocean                                                                                       | 75                                               |
| Dolphin                      | Ocean<br/>Warm Ocean<br/>Lukewarm Ocean<br/>Cold Ocean                                                                                         | 7                                                |
| Donkey                       | Plains                                                                                                                                         | 1                                                |
| Frog                         | Swamp<br/>Mangrove Swamp                                                                                                                       | 2 to 5 in swamps and mangrove swamps             |
| Fox                          | Taiga<br/>Snowy Taiga<br/>Old Growth Pine Taiga                                                                                                | 8                                                |
| Glow Squid                   | Ocean[more information needed]                                                                                                                 | 2-4                                              |
| Goat                         | Frozen Peaks<br/>Jagged Peaks<br/>Snowy Slopes                                                                                                 | 3                                                |
| Hoglin‌[BE  only]            | Crimson Forest                                                                                                                                 | 20                                               |
| Horse                        | Savanna<br/>Plains                                                                                                                             | 4 in plains<br/>1 in savanna                     |
| Llama                        | Savanna<br/>Windswept Hills                                                                                                                    | 8 in savanna<br/>5 in windswept hills            |
| Mooshroom                    | Mushroom Fields                                                                                                                                | 8                                                |
| Ocelot<br/>Parrot            | Jungle<br/>Bamboo Jungle                                                                                                                       | 30 for ocelots<br/>40 for parrots                |
| Panda                        | Jungle<br/>Bamboo Jungle                                                                                                                       | 10 in regular jungle<br/>40 in bamboo jungle     |
| Polar Bear                   | Snowy Plains<br/>Frozen Ocean<br/>Frozen River                                                                                                 | 1 (5 in frozen oceans)                           |
| Pufferfish<br/>Tropical Fish | Warm Ocean<br/>Lukewarm Ocean<br/>Deep Lukewarm Ocean                                                                                          | 25 for pufferfish<br/>75 for tropical fish       |
| Rabbit                       | Desert<br/>Taiga<br/>Old Growth Pine Taiga<br/>Snowy Taiga<br/>Snowy PlainsFrozen OceanFrozen RiverSnowy BeachLegacy Frozen OceanFlower Forest | 4 (20 in flower forests)                         |
| Salmon                       | River<br/>Cold Ocean<br/>Frozen Ocean<br/>Lukewarm Ocean                                                                                       | 26 in oceans<br/>16 in rivers                    |
| Squid                        | Ocean<br/>River                                                                                                                                | 8                                                |
| Strider                      | Nether Wastes<br/>Crimson Forest<br/>Soul Sand Valley<br/>Basalt Deltas<br/>Warped Forest                                                      | 20                                               |
| Turtle                       | Beach                                                                                                                                          | 8                                                |
| Wolf                         | Taiga(all variants)<br/>Forest(all variants)<br/>Windswept Hills(all variants)                                                                 | 8 in taigas<br/>5 in forests and windswept hills |

Randomness for animal spawning is derived from the world seed, which means that worlds with the same seed always generate chunks with the same animals in the same places.

### Monsters
Monsters cannot spawn when the difficulty is set to Peaceful (except for piglins and hoglins). At any higher setting they spawn when block light level is 0. The player cannot sleep when a monster (other than hoglins, slimes‌[JE  only] magma cubes‌[JE  only] and non-hostile zombified piglins‌[JE  only]) is nearby, even if the monster has no path to the player.

** Common monsters **
Common monster mobs can spawn in almost any biome in the Overworld (except for mushroom fields or deep dark). They can spawn on the surface and underground. The weight determines the spawn rate in the Bedrock Codebase. 

| Mobs            | Weight | Group size   |
|-----------------|--------|--------------|
| Zombie          | 100    | 2-4          |
| Creeper         | 100    | Individually |
| Skeleton        | 80     | 1-2          |
| Spider          | 100    | Individually |
| Enderman        | 10     | 1-2          |
| Witch           | 5      | Individually |
| Zombie Villager | 5      | Individually |

** Biome-specific monsters **
Some monsters spawn only in specific biomes.

| Mobs                        | Biome                                                                       |
|-----------------------------|-----------------------------------------------------------------------------|
| Bogged                      | Swamp<br/>Mangrove swamp                                                    |
| Drowned                     | Ocean(all variants)<br/>River(all variants)<br/>Dripstone Caves             |
| Ghast                       | Nether Wastes<br/>Soul Sand Valley<br/>Basalt Deltas                        |
| Hoglin‌[JE  only]           | Crimson Forest                                                              |
| Husk                        | Desert(all variants)                                                        |
| Magma Cube                  | Nether Wastes<br/>Basalt Deltas                                             |
| Slime                       | Swamp                                                                       |
| Stray                       | Snowy Plains<br/>Ice Spikes<br/>Frozen River<br/>Frozen Ocean(all variants) |
| Piglin<br/>Zombified Piglin | Nether Wastes<br/>Crimson Forest                                            |

### Other mobs
In Java Edition these mobs still spawn if the /gamerule doMobSpawning command is set to false, because they spawn as part of structure generation. In Bedrock Edition nothing spawns if the /gamerule doMobSpawning command is set to false.

** Passive and neutral mobs **
| Mob                                               | Structure generation                                                                                                                                                                                                                                     |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Allay                                             | Allays can spawn up to in 1-3 groups in apillager outpostand awoodland mansion.                                                                                                                                                                          |
| Black Cat                                         | A single black cat spawns within or around aswamp hutupon generation.                                                                                                                                                                                    |
| Camel<br/>Cat<br/>Cow<br/>Horse<br/>Pig<br/>Sheep | Generate as part of thevillagegeneration.<br/>Specific animals spawn as part of specificvillage structures: Animal pens (cow, sheep, pig, or horse), stables (horse, cow, or pig), butcher's houses (pig, cow, or sheep), and shepherd's houses (sheep). |
| Iron Golem                                        | Spawn frompillager outposts.<br/>Generate as part of thevillagegeneration.                                                                                                                                                                               |
| Villager                                          | Generate as part of thevillagegeneration.<br/>Each villager spawns in a house with a bed.                                                                                                                                                                |

** Hostile mobs **
| Mob                         | Structure generation                                                                                                                               |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Drowned                     | Generate as part of someunderwater ruins.‌[JE  only]                                                                                               |
| Elder Guardian<br/>Guardian | Generate as part of anocean monument.                                                                                                              |
| Ender Dragon                | Created inthe Endwhen the dimension is created. The ender dragon can also be respawned by placingend crystalson theexit portal.                    |
| Evoker<br/>Vindicator       | Generate as part of awoodland mansion.                                                                                                             |
| Pillager                    | Spawn frompillager outposts.                                                                                                                       |
| Shulker                     | Generate as part ofend cities.                                                                                                                     |
| Witch                       | A single witch spawns within aswamp hutupon generation.                                                                                            |
| Zombie Villager             | Generate as a part of aniglooif it generates with abasement.<br/>Can spawn as part ofzombie villagegeneration, where they never despawn naturally. |

## Spawn cycle
### Java Edition
Mobs are broadly divided into seven categories: hostile, passive, water creature (squids and dolphins), underground water creature (glow squids), axolotls, water ambient (all 4 types of fish), and ambient (bat). Most mobs have a spawning cycle once every game tick (1⁄20 of a second), but passive mobs have only one spawning cycle every 400 game ticks (20 seconds). Because of this, where conditions permit, hostile mobs spawn frequently, but passive mobs (animals) spawn rarely. Most animals spawn within chunks when they are generated.

Mobs spawn naturally within chunks that have a player horizontally within 128 blocks of the chunk center. When there are multiple players, mobs can spawn within the given distance of any of them. However, hostile mobs (and some others) that move farther than 128 blocks from the nearest player despawn instantly, so the mob spawning area for such mobs is more-or-less limited to spheres with a radius of 128 blocks, centered at each player.

#### Java Edition mob cap
There are two caps, a global cap and a per-player cap. Note the spawn density mechanism may also be considered a "cap" of sorts, but takes effect later in the spawning process.

The mob caps are checked once for each spawn-eligible chunk. Spawn for the chunk may take the total number of mobs over the cap.

The caps for each mob category are as follows:

| Mob category                             | Cap |
|------------------------------------------|-----|
| Monster                                  | 70  |
| Creature                                 | 10  |
| Ambient (bats)                           | 15  |
| Axolotls                                 | 5   |
| Underground water creature (glow squids) | 5   |
| Water creature (squids, dolphins)        | 5   |
| Misc                                     | -1  |

The "misc" category is used only by entities that are not mobs, do not spawn naturally, and/or following different spawning rules than other mobs. As such the mob cap has no bearing on mobs of this category.

** Global mob cap **
All non-persistent loaded mobs are counted against the global cap, including those in chunks not in range of a player or eligible for spawns. The cap is scaled by the total number of chunks within a 17×17 chunk square around any player. The cap is then scaled as globalCap = mobCap × chunks ÷ 289. Because chunks that are in the range of multiple players are counted once, more chunks and higher mob caps result from the players spreading out.

** Per-player mob cap **
Each non-persistent mob in a chunk that has its center within 128 blocks horizontally of a player is counted toward that player's per-player mob cap. For each chunk, spawns are only allowed if at least one player has that chunk in range and has not reached their per-player mob cap.

#### Pack spawning
Example of a mob pack spawning. The mob spawning area is shaded blue. The yellow figures represent the actual positions that mobs could spawn in after checking the environment. Note that the mobs can spawn inside torch and ladder blocks. But they can't spawn on top of glass because it is not opaque. The red cube is the center of the pack.
Requirements for the spawning location of individual mobs.
For each spawning cycle, attempts are made to spawn packs of mobs per each eligible chunk. An eligible chunk is determined by the same check for which chunks are random ticked. A random location in the chunk is chosen to be the center point of the pack. If the block in which a pack spawn occurs is an opaque full cube, further pack spawn attempts are canceled. There are a maximum of 3 pack spawn attempts per mob category.

Before the attempt to spawn each mob in the pack, the position is offset by ±5 (triangular distribution) on the X and Z axes. Thus, while the pack can be spread out up to 40 blocks from the initial position for a pack size of 4, it's much more likely they'll be closer to the center. Approximately 85% of spawns are within 5 blocks of the pack center, and 99% within 10 blocks of the center. Mobs spawn with the lowest part of their body inside this area.

All mobs within a pack are the same species. The species for the entire pack is chosen randomly, but based on a weight system from those eligible to spawn at the location of the first spawn attempt in the pack. For later mob spawn attempts in the pack, if the selected species cannot spawn at the location (e.g. due to being in a different biome or structure) then that attempt fails.

The game checks on each spawn if the number of mobs that have been spawned for the pack is equal to the max spawn attempts, as well as the location's spawn potential.

** Pack spawn size **
Pack spawn attempts max out at:

- 8 wolves, cod, and tropical fish
- 6 horses and donkeys
- 1 ghast
- 4 for any other mob

When the max pack size is less than the number of possible spawn attempts, some spawns attempts fail, but are seen more commonly in practice. Based on the number of mobs that have been successfully spawned. If the max pack size is greater than the number of spawn attempts, one gets only the number of spawns from the spawn attempts. Some mobs have a minimum and max pack size, meaning there is an even chance for any number of spawn attempts between them occurring.

- Forzombie villagers,drowned,pillagers,donkeysinsavannabiomes,parrotsinjunglesexcludingbamboo jungleand jungle, cats inswamp hutsandwitches, it is 1.
- For parrots inbamboo junglesandjungles,polar bears,squidsinlukewarm oceans,pandasanddolphins, it is 1-2.
- For donkeys inplainsbiomes, ocelots and pufferfish, it is 1-3.
- Forendermenexcept inthe Endand innether wastes, andsquidsexcept inlukewarm oceans, it is 1-4.
- Forrabbitsandblazes, it is 2-3.
- Forguardians,foxes,zombified piglinsincrimson forestsandstriders, it is 2-4.
- Forturtles, it is 2-5.
- Forhorses, it is 2-6.
- Forpiglinsandhoglinsincrimson forests, it is 3-4.
- Forcodit is 3-6.
- Forllamas, it is 4-6.
- Formooshrooms, it is 4-8.
- Forwither skeletonsandskeletons, in nether fortresses, it is 5.
- Forbatsandtropical fish, it is 8.
- For every other mob, it is 4.

** Pack spawn location **
For all dimensions, structure-based spawns take priority over biome for hostile spawns. This means that in a swamp hut, pillager outpost, nether fortress (outer bounding box only when there is nether bricks below it‌[JE  only]), and ocean monument, one sees only the corresponding hostile mobs for that structure within that structure.

In the Overworld, this depends on the location:

- Junglebiomes have a higher chance to spawnchickens.‌[Java Edition  only]
- Badlandsbiomes spawn only hostile mobs andbats.
- Riverandfrozen rivercan spawn onlydrowned, squid, and salmon underwater.
- Oceanbiomes do not spawn passive mobs. They spawndrowned, and the other hostile mobs.Frozen oceansdo not spawn dolphins, but do spawnpolar bears.
- Snowy plainsbiomes do not spawn animals other thanpolar bearsandrabbits.
- Swamp hutsspawn onlywitches,cats, and bats.
- Ocean monumentsspawnguardians, other water mobs and bats.
- Pillager outpostsspawnpillagers, other passive mobs and bats.
- All other overworld biomes spawns common animals and common monsters, as well as slimes, dependent on spawn conditions.

In the Nether:

- Skeletons,wither skeletons,magma cubes,zombified piglins, andblazesspawn withinnether fortresses.
- Ghastsspawn innether wastes,soul sand valleyandbasalt deltas.
- Zombified piglins and piglins can spawn in nether wastes, while magma cubes spawn primarily inbasalt deltasand sometimes in nether wastes.
- Ghasts, magma cubes and hoglins spawn regardless of light level.
- Hoglinsandpiglinsspawn at a higher rate anywhere in thecrimson forestbiome.
- Endermenspawn more frequently in thewarped forestbiome, but not in the crimson forest.
- Skeletonsandghastsspawn more frequently in thesoul sand valleybiome.

#### Spawn conditions
Whether a spawn condition fails differs from the above determination if the game tries to spawn them in that biome. For example, dolphins can have pack spawns that occur inside of frozen ocean and deep frozen ocean biomes, but no other biomes. These rules apply to variants of the same mob, such as baby zombies and jockeys.

Each individual spawn attempt succeeds only if all of the following conditions are met:

- There must be no players or the world spawn point within a 24 radius block distance (spherical) of the spawning block
- The number of loaded mobs of that type must be less than the mob cap for that type. (I.e. the corresponding mobcap must not be full)
- The mob's collision box upon spawning must not collide with another collision box. A mob cannot spawn inside of anything that would collide with it upon spawning.
- The mob's collision box must not intersect with a solid block.
- For all mob types excluding passives and fish, spawns fail unless within a 128 radius block sphere around the player. For fish, spawns fail unless within a 64 block radius of the player.[2]
- /gamerule doMobSpawningistrue
- For non-aquatic mobs, the spawning block and the block above that cannot berails,powered rails,detector rails,activator rails,redstone power components, wither roses (except for wither skeletons) or sweet berry bushes (except for foxes).

** Hostile mobs **
- The difficulty must not be Peaceful, excluding piglins and hoglins
	- This also affects ocelots[3]
- For all hostiles other than guardians, drowned, and phantoms:
	- the block directly below it must have a solid, opaque, top surface (this includes upside downslabs, upside downstairs, and others) or besoul sandor aslime block.
	- the block directly below it must not bebedrock,barrier, or any type of trapdoor or glass.
	- The mob's collision box must not collide with any liquid.
	- The block above the spawning block must betransparent.
	- The mob must be immune to the damaging effects of the spawning block and the block directly below it. For instance, if the block directly below the spawning block is amagma block, the mob must be immune to fire damage. If the spawning block contains awither rose, the mob must be immune to wither damage. (Currently, this is only true for wither skeletons).

The basic rules for spawning are as follows:

- In the Overworld, block light level must be 0 and sky light must be 7 or below (which it always is inside a cave).
- In the Nether, block light level must be 11 or less. Sky light is always 0 in the Nether.
- In the End, block light level must be 0. Sky light is always 0 in the End.

When doing the light check in the Overworld and End, the spawn chances are randomized and a spawn only occurs if the light level is less than or equal to a random number between 0 and 7. In the Nether, as long as the light level is below 11, the spawn is allowed.

Some mobs have some additional rules in addition to the ones above.

| Mob                       | Rules                                                                                                                                                                                      |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Blaze                     | Spawns only in nether fortresses<br/>                                                                                                                                                      |
| Drowned                   | Spawning block and block below must be water<br/>In rivers, has 1⁄15 chance to spawn<br/>In oceans, has 1⁄40 chance to spawn and must be 5 block below sea level<br/>                      |
| Ghast                     | 95% chance of spawn failure.<br/>                                                                                                                                                          |
| Guardian                  | The spawning block and the block below must be water, including waterlogged blocks and bubble columns.<br/>95% chance of failure if the spawning block has sky exposure (details).<br/>    |
| Hoglin                    | Cannot spawn on nether wart block<br/>                                                                                                                                                     |
| Husk                      | The location of the spawn must have sky access<br/>                                                                                                                                        |
| Magma Cube                | Cannot spawn on liquid<br/>                                                                                                                                                                |
| Ocelot                    | Spawn has a 1⁄3 chance of failure<br/>Can spawn on leaves<br/>                                                                                                                             |
| Piglin                    | Cannot spawn on nether wart block<br/>                                                                                                                                                     |
| Skeleton(nether fortress) | There is an 80% chance of spawning a wither skeleton instead[verify]<br/>                                                                                                                  |
| Slime(swamp biome)        | the spawning block must be in a swamp biome<br/>the spawning block be on level 51 through 69 inclusive<br/>chance of failure based on the phase of the moon<br/>50% chance of failure<br/> |
| Slime(slime chunks)       | the spawning block is below level 40.<br/>90% chance of failure.<br/>                                                                                                                      |
| Stray                     | The location of the spawn must have sky access<br/>                                                                                                                                        |
| Wither Skeleton           | Spawns only in Nether fortresses<br/>                                                                                                                                                      |
| Zombified Piglin          | Cannot spawn on nether wart block<br/>                                                                                                                                                     |

** Passive mobs **
- The mob's collision box must not collide with any liquid.
	- if it is not astrider, the light level of the spawning block must be 9 or brighter.
		- If it is amooshroom, then...
			- the block directly below the spawning block must bemycelium.
		- If it is aturtle, then...
			- the block directly below the spawning block must besand.
			- the spawning block must be y-level 66 or lower.
		- If it is aparrot, then...
			- the block directly below the spawning block must either begrass block,leaves,log, orair.
		- If it is arabbit, then...
			- the block directly below the spawning block must either begrass block,snow block,snow[4], orsand.
		- If it is awolf, then...
			- the block directly below the spawning block must either begrass block,snow block, orsnow[4].
		- If it is afox, then...
			- the block directly below the spawning block must either begrass block,snow block,snow[4],podzol, orcoarse dirt.
		- If it is apolar bearspawning in afrozen oceanor deep frozen ocean biome, then...
			- the block directly below the spawning block must beice.
		- If it is agoat, then...
			- the block directly below the spawning block must either bestone,snow block,snow[4],packed ice, orgravel.
		- For all others then...
			- the block directly below the spawning block must be agrass block.
	- If it is astrider, then...
		- Spawn attempts with lava above check upward as long as there is still lava for if they can successfully spawn in a lava block with air on top.

** Aquatic mobs **
- The spawning block must be water
	- Forcod,salmon,pufferfish,tropical fish,squidordolphin:
		- the block directly below the spawning block must be water
		- the block directly above the spawning block must be water and cannot be waterlogged
		- the spawning block must be between level 50 and 63, inclusive. This does not apply totropical fishspawning in lush caves
	- If it is aglow squid, then...
		- the light level must be 0
		- the spawning block must be level 30 or lower
	- If it is anaxolotl, then...
		- the block directly above the spawning block must not be a solid block
		- the block directly below the spawning block must beclay

** Ambient mobs **
- The mob's collision box must not collide with any liquid.
	- If it is abat, then...
		- the spawning block must be at level 62 or below.
		- the block directly below it must have a solid, opaque, top surface.
		- the block directly below it must not bebedrock,barrier, or any type of trapdoor or glass.
		- If the real-time day is between October 20 and November 3, then the light level must be 7 or darker. Otherwise, the light level must be 4 or darker.

If all of these conditions are met then the mob is spawned.

** Spawn costs **
Locations that do not have spawning potential reliant spawns are marked by wart blocks or netherrack
The warped forest and soul sand valley biomes introduced a new mechanic to limit the amount of mobs that naturally spawn in them. The spawn cost (also called spawn potential or spawn density) takes on a value for each block in the biome. Certain mobs increase that value by some number ("charge") divided by their distance to the block. If a new spawn attempt would bring the "potential" of the spawning block above a certain threshold, the spawn attempt is canceled. This results in mobs not spawning too close to one another in these biomes, and new spawns in the area are completely blocked long before the full mobcap of 70 hostile mobs is ever reached.

More specifically, a mob may be spawned at a location if sum( existing mob's charge ÷ distance to mob ) × new mob's charge < new mob's maximum potential. While the code allows for different mobs to have different charges and maximum potential, all checked mobs have the same charge and maximum potential within both the warped forest and the soul sand valley.

Which mobs contribute to the charge, how much they add, and what the maximum potential is are all biome-specific. Mobs carry charge according to their current biome, and affect spawning in an adjacent biome even if they would not contribute a charge if in that biome. For example, striders in a soul sand valley affect enderman spawns in an adjacent warped forest, even though striders in the warped forest itself do not.

Due to the limited total number of mobs in soul sand valleys and warped forests, a larger-than-usual amount of mobs spawn in any space outside of these biomes, including in nether fortresses.

** Notes **
- Buildings surrounded by air spawn more mobs inside than underground rooms because packs that spawn outside of the building can spawn mobs inside it. The mob caps tend to be reached in seconds.
- If the player's view distance or the server view distance in multiplayer is at 9 or below, mob spawning is severely reduced (or they despawn too quickly), and may result in the player encountering no mobs at all. Set the view distance to 10 or higher to ensure mobs spawn correctly.

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

#### Cluster spawning
Cluster spawning happens in two stages: first attempt to spawn surface mobs, then attempt to spawn cave mobs. Before spawning, the population control cap is calculated based on the 9 chunk x 9 chunk square area surrounding the current chunk. Spawning begins by picking a random X and Z location within the chunk currently being evaluated. The Y coordinate is determined by starting at the world height and searching downward for a solid-top-surface block with a non-spawn-blocking block above it. The first such block that is found is considered to be the surface, and the algorithm attempts to spawn a surface mob herd. However, if the algorithm finds a solid block before finding a spawnable solid-top-block (e.g. if it finds a tree trunk directly under leaves), it does not make any surface spawn attempt. The algorithm then continues to search downward for the next suitable block with a non-spawn-blocking block above it. When a block meeting the criteria is found, the algorithm attempts to spawn a cave mob herd at that block location. Cave spawn attempts continue until the Y coordinate reaches the world bottom, and do not stop even if a cave herd was spawned.

Surface and cave cluster spawn attempts then go through the following steps to figure out what mob to spawn and how many:

1. Picks a random mob.
	- If the current spawn location is in a liquid, pick a random water mob.
	- If the light level is 7 or higher, there are no other blocks above the current location, and the current location is a grass block, pick a random animal mob.
	- Otherwise, spawn a monster mob.
2. Picks a random number of mobs to spawn in the herd. Each mob can have its own min and max herd size, and the herd size can depend on difficulty and biome.
3. Make sure the spawn location has suitablespawn conditions.
4. Limit the number of mobs spawning based on the global mob cap. No mobs spawn if the mob count already meets or exceeds the mob cap.
5. For each mob to spawn, check that spawning it would not exceed the population control cap or mob density cap.
	- If spawning the mob would not exceed the population control or mob density caps, then the probability of a mob spawning can be calculated using the formula:(mob density cap - current mob density count) / mob density cap
6. Finally, attempt to spawn the mob in the world.
	- Spawning the mob can fail; for example, if spawning it would cause it to spawn inside of a block or part of a wall.

#### Structure spawning
Structure spawn attempts occur at specific relative X and Z coordinates in naturally generated structures, known as "hard-coded spawn spots". The structures that have hard-coded spawn spots include swamp huts, ocean monuments, pillager outposts, and nether fortresses. Whenever a successful cluster spawn attempt occurs within a chunk that contains a hard-coded spawn spot, the environmental spawning algorithm also attempts a structure spawn. (Note that a "successful attempt" here means that a spawnable block was found, even if the spawn was then blocked by light level check or mob cap check.) The structure spawn attempt follows the same rules and steps described above for cluster spawning, with the following changes:

- Instead of starting at world height and searching down to bedrock at the specific X and Z location, the search begins and ends at a specific Y values determined by the type of structure. Structure spawn attempts occur only on the first spawnable block found (i.e. the highest spawnable block) within that range.
- The mob picked depends on the structure: swamp huts spawn witches, ocean monuments spawn guardians, pillager outposts spawn pillagers (including patrol captains), and nether fortresses spawn skeletons, wither skeletons, blazes, and magma cubes.
- The population control caps are effectively 1 higher for structure spawn attempts.

## Other types of spawning
### General
- InCreativeor via a dispenser, the player can usespawn eggsto spawn most mobs. When mobs are spawned this way, all normal spawning requirements, such as light level and block type, are ignored (though monsters other than shulkers and the ender dragon still cannot be spawned in peaceful).
- Anyentitycan be spawned using the/summoncommand.

### Passive mobs
| Mob                                                                     | Spawning                                                                                                             |
|-------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| Agent                                                                   | An agent spawns when using a code connection.‌[Bedrock Edition and Minecraft Education  only]                        |
| Axolotl<br/>Cod<br/>Salmon<br/>Pufferfish<br/>Tadpole<br/>Tropical Fish | Spawn when using the correspondingbucket of aquatic mob.                                                             |
| Bee                                                                     | Spawn when abee nestor beehive is broken withoutSilk Touch.                                                          |
| Brown Mooshroom                                                         | Spawns when ared mooshroomis struck by lightning, and vice-versa.                                                    |
| Cat                                                                     | Spawns in the vicinity of a player near a village.                                                                   |
| Chicken                                                                 | A throwneggspawns baby chickens.                                                                                     |
| Iron Golem<br/>Snow Golem                                               | Can be made to spawn if a player builds the proper structure out of blocks. They can also be created by an enderman. |
| Mule                                                                    | Spawn when breeding a horse and a donkey.                                                                            |
| NPC                                                                     | Are part of Tutorial Worlds.‌[Minecraft Education  only]                                                             |
| Skeleton Horse                                                          | Can spawn during thunderstorms, trigger a skeleton trap.                                                             |
| Sniffer                                                                 | Sniffer eggshatch and spawn snifflets.                                                                               |
| Turtle                                                                  | Turtle eggshatch and spawn baby turtles.                                                                             |

### Hostile mobs
| Mob                                                                                    | Spawning                                                                                                                                                                                                                                          |
|----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Blaze<br/>Cave Spider<br/>Magma Cube<br/>Silverfish<br/>Skeleton<br/>Spider<br/>Zombie | Amonster spawnercauses mobs to spawn constantly in the area around it.                                                                                                                                                                            |
| Charged Creeper                                                                        | If acreepergets struck bylightning, it becomescharged.                                                                                                                                                                                            |
| Endermite                                                                              | Can spawn randomly when a player uses anender pearl.                                                                                                                                                                                              |
| Evoker<br/>Pillager<br/>Ravager<br/>Vindicator<br/>Witch                               | Can spawn as part ofraidsorpatrols.                                                                                                                                                                                                               |
| Phantom                                                                                | Can spawnafter player does not sleep or die for at least 3 days. (InBedrock Editionphantoms are spawned by the environmental spawning algorithm like other monsters. They are subject to the monster cap, and they count toward the monster cap). |
| Silverfish                                                                             | Aninfested blockspawns a silverfish if broken, or if a nearby silverfish is attacked.                                                                                                                                                             |
| Skeleton                                                                               | Skeletons spawn as 20% of naturally-spawning strays.                                                                                                                                                                                              |
| Skeleton Horseman                                                                      | Spawn from skeleton traps.                                                                                                                                                                                                                        |
| Slime                                                                                  | Killing medium and largeslimesandmagma cubesspawn more of them, but in a smaller size.                                                                                                                                                            |
| Warden                                                                                 | When a player activates a naturally generated sculk shrieker four times or more.                                                                                                                                                                  |
| Witch                                                                                  | When avillagergets struck by lightning, it is replaced by a newly spawnedwitch.                                                                                                                                                                   |
| Wither                                                                                 | Can be made to spawn if a player builds the proper structure out of blocks.                                                                                                                                                                       |
| Zombie                                                                                 | Zombies spawn as 20% of naturally-spawning husks.‌[JE  only]                                                                                                                                                                                      |
| Zombie<br/>Zombified Piglin<br/>Illager                                                | Can spawn reinforcement when hurt‌[JE  only].                                                                                                                                                                                                     |
| Zombie Villager                                                                        | Zombie villagers spawn as 5% of naturally-spawning zombies.<br/>A villager killed by a zombie has a 50% chance of becoming a zombie villager in normal difficulty, and 100% chance in hard difficulty.                                            |
| Zombified Piglin                                                                       | Can spawn fromnether portalsin the Overworld. Lighting and player proximity don't prevent this.<br/>When apiggets struck bylightning, it is replaced by a newly spawnedzombified piglin.                                                          |
| Zoglin<br/>Zombified Piglin                                                            | If apiglinorhoglinis transported to theOverworldorthe End, after 15 seconds they transform intozombified piglinsorzoglins, respectively.                                                                                                          |

## Despawning
This article is about Mob Despawning.  For Item Despawning, see Item § Behavior.
### Java Edition
Various mob spawning ranges, illustrated.
All monster, ambient, and aquatic mobs excluding shulkers, withers, elder guardians and ender dragons despawn unless they have been marked persistent. Other mobs that are not monster, ambient, or aquatic that do despawn include ocelots, stray cats, wandering traders, and untamed trader llamas.

- A mob that has had no player within 32 blocks of it for more than 30 seconds, or 10 seconds if in low light levels, has a1⁄800chance of despawning on each gametick(1⁄20of a second), which is a 2.47% chance per second. Therefore, the mob population declines so that half remains after 27.75 seconds, and the average lifetime of monsters not within 32 blocks of a player is 40 seconds (afterthe initial 30 seconds have elapsed).
- Mobs other than fish despawn immediately if no player is within 128 blocks of it, while fish despawn if no player is within 64 blocks.[6]
	- This is a Euclidean sphere, not a cylinder from map top to bottom and not ataxicabsphere (an octahedron). Example: A mob at 0/y/0 remains at least 10 seconds (as above) if the player moves to 65/y/65 (real distance 91.9), but despawns immediately if the player moves to 91/y/91 (real distance 128.7).
	- Thechunkthe mob is in must still be loaded for the mob to despawn. Otherwise, the mob is saved until thechunk is loadedagain. For example, if a player enters anether portalwhile being chased by a spider, the spider is saved, and it resumes chasing the player coming back through the same portal. In the case of a player reloading chunks, the loading happens before the player is added, meaning they may despawn.
- Ocelots and most monster mobs (including those that are holding items) despawn if the difficulty is set to Peaceful, regardless of where the player is located. Monster mobs that do not despawn include hoglins, piglins, and shulkers in all editions, as well as vindicators, zoglins, piglin brutes, and evokers inBedrock Edition.
- For despawning to occur, there must be at least one non-spectator player in the dimension.
- Chickens that originally spawned aschicken jockeysfollow zombie despawn rules, rather than chicken despawn rules.
- Wandering traders and trader llamas despawn after 40-60 minutes (2-3 in game days). They also despawn sooner if all the trades are locked.‌[Bedrock Edition  only][verify]
- Endermites despawn after 2 minutes unless named with a name tag or have persistent tag.
- Wardens despawn after 1 minute if they couldn't detect a vibration or smell by any mob or player.



Mobs are persistent, meaning they do not despawn and do not count toward the mob cap, when they:

- are a passenger to another mob.
- are riding aboator aminecart.[7]
- spawned as part of agenerated structure.
- have had something added to theirinventory, including having somethingdispensedupon them (such as asaddle) or something they have picked up, but never for anything they spawn with. This includes dolphins playing with items[verify].
- have been named with aname tag. However, one created from a renamedspawn eggdoes despawn as normal.
- have had the NBT tag{PersistenceRequired: 1b}set on them, whether by being summoned with it, or by being set manually with/data mergeor/data modify‌[JE  only]. This is also the only way to prevent wandering traders from despawning.

Following mobs also have another way to prevent despawning and do not count toward mob cap:

- Enderman: During the time that they hold a block
- Fish(all variants),axolotlsandtadpoles: Spawned as a result of placing out of abucket of mob.
- Zombie villagers: If they were converted from avillagerthat has been traded with. This still counts toward the hostile mob cap.[8]
- Zombified piglinsandwitches: If they were converted from apigorvillagerstruck by lightning.
- Hoglins: If acrimson fungusisusedon them.Zoglinsas a result of hoglins have crimson fungususedon them before they zombify also do not despawn.

### Bedrock Edition
In Bedrock Edition, like Java, despawning occurs based on distance and chance.

- On simulation distances 6 and higher, almost all environmentally spawned mobs immediately despawn when they are either (1) in a chunk at the edge of the simulation distance (technically, a chunk not fully surrounded by 8 chunks that were simulated on the last game tick), or (2) more than 128 blocks from the nearest player.
- On simulation distance 4, mobs immediately despawn when they are more than 44 blocks from the nearest player.
- Fishdespawn at a shorter distance, when they are more than 40 blocks from the nearest player on all simulation distances.
- Mobs more than 32 blocks from the nearest player have a 1 in 800 chance to despawn on each game tick if they have not taken damage for 30 seconds.

Mobs with persistence do not despawn. Mobs gain persistence in the following ways:

- The entity interacts with a player (except for attacking, which does not count as a persistence-inducing interaction):
	- Is ridden by the player.
	- Is named with aname tag.
	- Is tempted withfood.
	- Isbred, or born as a result of breeding (except for turtles hatched from eggs before 1.17.10[9]).
	- Is tamed by the player.
	- Is summoned using the/summoncommand or a spawn egg.
	- Iscured from being a zombie villager.
	- Is spawned by the player triggering askeleton trap(spawnsskeletonsandskeleton horses).
- The entity picks up an item.
- The entity is spawned during the generation of a certain kind ofstructure:
	- Shulkerspawned in anend city.
	- Witchspawned in aswamp hut.
	- Villagerorzombie villagerspawned in anigloo.
	- Villager or animals spawned in a village.
	- Zombie villager or animals spawned in azombie village.
	- Vindicatororevokerspawned in awoodland mansion.
- The entity is spawned in a raid.

The following entities always have persistence: 

- Ender Dragon
- Wither
- Elder Guardian
- Evoker
- Vindicator
- Iron Golem
- Snow Golem
- Villager
- Armor Stand
- Minecart
- Painting
- Agent‌[BE & edu  only]
- Camera‌[BE & edu  only]
- NPC‌[BE & edu  only]

