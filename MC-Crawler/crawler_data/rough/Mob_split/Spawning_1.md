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

