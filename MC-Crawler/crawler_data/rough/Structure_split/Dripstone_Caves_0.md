# Dripstone Caves
The dripstone caves are an Overworld cave biome found in inland areas, filled with clusters and pillars of pointed dripstone and dripstone blocks.

## Contents
- 1 Description
- 2 Sounds
	- 2.1 Music
- 3 Data values
	- 3.1 ID
- 4 History
- 5 Issues
- 6 Trivia
- 7 Gallery
	- 7.1 Screenshots
	- 7.2 In other media
- 8 See also
- 9 References
- 10 External links

## Description
A dripstone cluster.
Dripstone caves generate underground at any altitude. This biome generates beneath areas with high continentalness values, which means they are usually found far inland, and are essentially never found under ocean biomes or bordering a coast. While dark forests, old growth taigas, bamboo jungles, wooded badlands, and taigas at temperatures of -0.450 and below are almost guaranteed to have lush caves under them, dripstone caves may generate under them instead of lush caves when they're far inland. 

Dripstone blocks and pointed dripstone both hanging as stalactites and growing from the ground as stalagmites, small water wells of 1×1 blocks are generated in the ground. They mostly appear like regular caves, except with patches of dripstone blocks and pointed dripstone. Large dripstone clusters structures generate occasionally inside ravines. This biome also generates larger copper ore blobs compared to other biomes. In Java Edition, drowned are able to spawn in aquifers.

When exposed to the surface, the surface is made entirely out of stone with occasional patches of dripstone.

The following mobs are naturally spawned here:

| Mob             | Spawn weight      | Group size                          |
|-----------------|-------------------|-------------------------------------|
|                 |                   | Underground water creature category |
| Glow Squid      | 1                 | 4–6                                 |
|                 |                   | Ambient category                    |
| Bat             | 1                 | 8                                   |
|                 |                   | Monster category                    |
| Creeper         | $\frac{100}{610}$ | 4                                   |
| Skeleton        | $\frac{100}{610}$ | 4                                   |
| Slime[note 1]   | $\frac{100}{610}$ | 4                                   |
| Spider          | $\frac{100}{610}$ | 4                                   |
| Drowned         | $\frac{95}{610}$  | 4                                   |
| Zombie          | $\frac{95}{610}$  | 4                                   |
| Enderman        | $\frac{10}{610}$  | 1–4                                 |
| Witch           | $\frac{5}{610}$   | 1                                   |
| Zombie Villager | $\frac{5}{610}$   | 1                                   |

1. ↑Spawn attempt succeeds only in slime chunks.

{ "underground": { "mobs": [ { "size": "4&ndash;6", "mob": "Glow Squid", "weight": 10 } ], "totalWeight": 10 }, "ambient": { "mobs": [ { "size": "8", "mob": "Bat", "weight": 10 } ], "totalWeight": 10 }, "monster": { "mobs": [ { "size": "4", "mob": "Creeper", "weight": 100 }, { "size": "4", "mob": "Skeleton", "weight": 100 }, { "size": "4", "note": "Spawn attempt succeeds only in slime chunks.", "mob": "Slime", "weight": 100 }, { "size": "4", "mob": "Spider", "weight": 100 }, { "size": "4", "mob": "Drowned", "weight": 95 }, { "size": "4", "mob": "Zombie", "weight": 95 }, { "size": "1&ndash;4", "mob": "Enderman", "weight": 10 }, { "size": "1", "mob": "Witch", "weight": 5 }, { "size": "1", "mob": "Zombie Villager", "weight": 5 } ], "totalWeight": 610 } }
| Mob             | Spawn weight      | Group size        |
|-----------------|-------------------|-------------------|
|                 |                   | Monster category  |
| Creeper         | $\frac{100}{595}$ | 1                 |
| Drowned         | $\frac{100}{595}$ | 2–4               |
| Slime[note 1]   | $\frac{100}{595}$ | 1                 |
| Spider          | $\frac{100}{595}$ | 1                 |
| Zombie          | $\frac{95}{595}$  | 2–4               |
| Skeleton        | $\frac{80}{595}$  | 1–2               |
| Enderman        | $\frac{10}{595}$  | 1–2               |
| Witch           | $\frac{5}{595}$   | 1                 |
| Zombie Villager | $\frac{5}{595}$   | 2–4               |
|                 |                   | Creature category |
| Glow Squid      | 1                 | 2–4               |

1. ↑Spawn attempt succeeds only in slime chunks.

{ "monster": { "mobs": [ { "size": "1", "mob": "Creeper", "weight": 100 }, { "size": "2&ndash;4", "mob": "Drowned", "weight": 100 }, { "size": "1", "note": "Spawn attempt succeeds only in slime chunks.", "mob": "Slime", "weight": 100 }, { "size": "1", "mob": "Spider", "weight": 100 }, { "size": "2&ndash;4", "mob": "Zombie", "weight": 95 }, { "size": "1&ndash;2", "mob": "Skeleton", "weight": 80 }, { "size": "1&ndash;2", "mob": "Enderman", "weight": 10 }, { "size": "1", "mob": "Witch", "weight": 5 }, { "size": "2&ndash;4", "mob": "Zombie Villager", "weight": 5 } ], "totalWeight": 595 }, "creature": { "mobs": [ { "size": "2&ndash;4", "mob": "Glow Squid", "weight": 10 } ], "totalWeight": 10 } }

## Data values
### ID
Java Edition:

| Name            | Identifier        | Translation key                   |
|-----------------|-------------------|-----------------------------------|
| Dripstone Caves | `dripstone_caves` | `biome.minecraft.dripstone_caves` |

Bedrock Edition:

| Name                | Identifier        | Numeric ID |
|---------------------|-------------------|------------|
| [No displayed name] | `dripstone_caves` | `188`      |


