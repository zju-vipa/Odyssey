# Lush Caves
Lush caves are temperate Overworld cave biomes that have a unique fauna and flora and is found underground below humid biomes, indicated aboveground by azalea trees.

## Contents
- 1 Description
- 2 Sounds
	- 2.1 Music
- 3 Data values
	- 3.1 ID
- 4 Video
- 5 History
- 6 Issues
- 7 Trivia
- 8 Gallery
	- 8.1 Screenshots
	- 8.2 In other media
- 9 See also
- 10 References
- 11 External links

## Description
Lush caves generate underground at any altitude. They favor generating underneath biomes with high humidity values (H=3,4), which makes them most commonly found beneath dark forests, jungles, old growth taigas, wooded badlands, and taigas at temperatures of -0.450 and below, but may also generate under windswept forests, birch forests, taigas at temperatures of -0.150 to -0.450 and snowy taigas. Dark forests, old growth taigas, bamboo jungles, wooded badlands, and taigas at temperatures of -0.450 and below, in particular, are almost guaranteed to have lush caves generate below them, but when these biomes generate far inland, dripstone caves may generate underneath them instead. It is not possible for lush caves to generate beneath forests and grassland biomes like plains and savanna as they are not humid enough. Lush caves can sometimes generate beneath oceans and deserts, whose generation is independent of humidity values. They are also the only underground biome capable of generating beneath oceans. Forests, flower forests, and cherry groves are the only forested biomes where lush caves don’t generate at all, and deserts are the only non-forested biomes where lush caves can generate.

Azalea trees generate on any empty space above a lush cave, with roots consisting of rooted dirt and hanging roots that generate down until reaching the lush cave. This is most common at the surface, but they can sometimes generate inside caves if there is enough room. 

Underground, moss and ores cover the floors and ceilings, along with moss carpets, grass and azalea bushes on the floors. On the ceiling, vines and cave vines with glow berries grow down and light up the caves, and spore blossoms grow from the ceiling and drip water particles. Dripleaf plants grow up from shallow lakes lined with clay, which sometimes generate dry. Water can also generate here in the form of springs. 

Players cannot spawn in a lush caves biome during the world generation.

Bats, glow squid, tropical fish, and axolotls are the only passive mobs that spawn, with the latter being exclusive to the biome. While hostile mobs can spawn throughout the biome, many areas have a light level greater than 0 due to the pervasive glow berries. Most hostile mobs are therefore found in large caverns more than 10 blocks high and near borders with other cave biomes.

Lush caves contain copious amount of clay.

The following mobs are naturally spawned here：

| Mob             | Spawn weight      | Group size                          |
|-----------------|-------------------|-------------------------------------|
|                 |                   | Monster category                    |
| Creeper         | $\frac{100}{515}$ | 4                                   |
| Skeleton        | $\frac{100}{515}$ | 4                                   |
| Slime[note 1]   | $\frac{100}{515}$ | 4                                   |
| Spider          | $\frac{100}{515}$ | 4                                   |
| Zombie          | $\frac{95}{515}$  | 4                                   |
| Enderman        | $\frac{10}{515}$  | 1–4                                 |
| Witch           | $\frac{5}{515}$   | 1                                   |
| Zombie Villager | $\frac{5}{515}$   | 1                                   |
|                 |                   | Water ambient category              |
| Tropical Fish   | 1                 | 8                                   |
|                 |                   | Underground water creature category |
| Glow Squid      | 1                 | 4–6                                 |
|                 |                   | Axolotl category                    |
| Axolotl         | 1                 | 4–6                                 |
|                 |                   | Ambient category                    |
| Bat             | 1                 | 8                                   |

1. ↑Spawn attempt succeeds only in slime chunks.

{ "monster": { "mobs": [ { "size": "4", "mob": "Creeper", "weight": 100 }, { "size": "4", "mob": "Skeleton", "weight": 100 }, { "size": "4", "note": "Spawn attempt succeeds only in slime chunks.", "mob": "Slime", "weight": 100 }, { "size": "4", "mob": "Spider", "weight": 100 }, { "size": "4", "mob": "Zombie", "weight": 95 }, { "size": "1&ndash;4", "mob": "Enderman", "weight": 10 }, { "size": "1", "mob": "Witch", "weight": 5 }, { "size": "1", "mob": "Zombie Villager", "weight": 5 } ], "totalWeight": 515 }, "waterambient": { "mobs": [ { "size": "8", "mob": "Tropical Fish", "weight": 25 } ], "totalWeight": 25 }, "underground": { "mobs": [ { "size": "4&ndash;6", "mob": "Glow Squid", "weight": 10 } ], "totalWeight": 10 }, "axolotl": { "mobs": [ { "size": "4&ndash;6", "mob": "Axolotl", "weight": 10 } ], "totalWeight": 10 }, "ambient": { "mobs": [ { "size": "8", "mob": "Bat", "weight": 10 } ], "totalWeight": 10 } }
| Mob                   | Spawn weight      | Group size              |
|-----------------------|-------------------|-------------------------|
|                       |                   | Monster category        |
| Creeper               | $\frac{100}{495}$ | 1                       |
| Slime[note 1]         | $\frac{100}{495}$ | 1                       |
| Spider                | $\frac{100}{495}$ | 1                       |
| Zombie                | $\frac{95}{495}$  | 2–4                     |
| Skeleton              | $\frac{80}{495}$  | 1–2                     |
| Enderman              | $\frac{10}{495}$  | 1–2                     |
| Witch                 | $\frac{5}{495}$   | 1                       |
| Zombie Villager       | $\frac{5}{495}$   | 2–4                     |
|                       |                   | Creature category       |
| Glow Squid            | 1                 | 2–4                     |
|                       |                   | Water creature category |
| Tropical Fish[note 2] | $\frac{75}{110}$  | 3–5                     |
| Tropical Fish[note 2] | $\frac{25}{110}$  | 1–3                     |
| Axolotl               | $\frac{10}{110}$  | 4–6                     |

1. ↑Spawn attempt succeeds only in slime chunks.
2. ↑ a bTropical fish are spawned twice.

{ "monster": { "mobs": [ { "size": "1", "mob": "Creeper", "weight": 100 }, { "size": "1", "note": "Spawn attempt succeeds only in slime chunks.", "mob": "Slime", "weight": 100 }, { "size": "1", "mob": "Spider", "weight": 100 }, { "size": "2&ndash;4", "mob": "Zombie", "weight": 95 }, { "size": "1&ndash;2", "mob": "Skeleton", "weight": 80 }, { "size": "1&ndash;2", "mob": "Enderman", "weight": 10 }, { "size": "1", "mob": "Witch", "weight": 5 }, { "size": "2&ndash;4", "mob": "Zombie Villager", "weight": 5 } ], "totalWeight": 495 }, "creature": { "mobs": [ { "size": "2&ndash;4", "mob": "Glow Squid", "weight": 10 } ], "totalWeight": 10 }, "watercreature": { "mobs": [ { "size": "3&ndash;5", "note": "Tropical fish are spawned twice.", "mob": "Tropical Fish", "weight": 75 }, { "size": "1&ndash;3", "notename": "tropical fish", "mob": "Tropical Fish", "weight": 25 }, { "size": "4&ndash;6", "mob": "Axolotl", "weight": 10 } ], "totalWeight": 110 } }

## Data values
### ID
Java Edition:

| Name       | Identifier   | Translation key              |
|------------|--------------|------------------------------|
| Lush Caves | `lush_caves` | `biome.minecraft.lush_caves` |

Bedrock Edition:

| Name                | Identifier   | Numeric ID |
|---------------------|--------------|------------|
| [No displayed name] | `lush_caves` | `187`      |

