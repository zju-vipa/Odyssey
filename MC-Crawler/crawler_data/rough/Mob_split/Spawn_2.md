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

