### Snowy Mountains
| Blocks        | SnowGrass BlockIceSpruce LogSpruce Leaves |
|---------------|-------------------------------------------|
| Temperature   | 0.0                                       |
| Grass color   | #80B497                                   |
| Foliage color | #60A17B                                   |
| Water color   | #3F76E4‌[JE  only] #1156A7‌[BE  only]     |

{
    "title": "Snowy Mountains",
    "rows": [
        {
            "field": "(values exceeds 1000 characters...)",
            "label": "Blocks"
        },
        {
            "field": "0.0",
            "label": "(link to Biome#Temperature article, displayed as Temperature)"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #80B497; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #80B497</span>",
            "label": "Grass color"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #60A17B; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #60A17B</span>",
            "label": "Foliage color"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #3F76E4; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #3F76E4</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Java Edition\">(link to Java Edition article, displayed as JE)  only</span></i>]</sup><br><span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #1156A7; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #1156A7</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Bedrock Edition\">(link to Bedrock Edition article, displayed as BE)  only</span></i>]</sup>",
            "label": "Water color"
        }
    ],
    "invimages": [],
    "images": [
        "Snowy Mountains.png"
    ]
}
These hills were no taller than most other hill biomes in the game, despite the name 'mountains'. No structures generated in this biome, though polar bears, rabbits and strays spawned. Caves frequently generated on the sides of the mountains. In Bedrock Edition, no hostile mobs other than strays and skeletons spawned here.

Snowy mountains used the same mob spawning chances as snowy plains.


In Java Edition:
| Mob             | Spawn weight      | Group size        |
|-----------------|-------------------|-------------------|
|                 |                   | Creature category |
| Rabbit[note 1]  | $\frac{10}{11}$   | 2–3               |
| Polar Bear      | $\frac{1}{11}$    | 1–2               |
|                 |                   | Monster category  |
| Spider          | $\frac{100}{515}$ | 4                 |
| Zombie          | $\frac{95}{515}$  | 4                 |
| Stray           | $\frac{80}{515}$  | 4                 |
| Creeper         | $\frac{100}{515}$ | 4                 |
| Slime[note 2]   | $\frac{100}{515}$ | 4                 |
| Skeleton        | $\frac{20}{515}$  | 4                 |
| Enderman        | $\frac{10}{515}$  | 1–4               |
| Witch           | $\frac{5}{515}$   | 1                 |
| Zombie Villager | $\frac{5}{515}$   | 1                 |
|                 |                   | Ambient category  |
| Bat             | 1                 | 8                 |

1. ↑80% of spawned rabbits are white and 20% are black and white.
2. ↑Spawn attempt succeeds only in slime chunks.

{ "passive": { "mobs": [ { "size": "2&ndash;3", "note": "80% of spawned rabbits are white and 20% are black and white.", "mob": "Rabbit", "weight": 10 }, { "size": "1&ndash;2", "mob": "Polar Bear", "weight": 1 } ], "totalWeight": 11 }, "hostile": { "mobs": [ { "size": "4", "mob": "Spider", "weight": 100 }, { "size": "4", "mob": "Zombie", "weight": 95 }, { "size": "4", "mob": "Stray", "weight": 80 }, { "size": "4", "mob": "Creeper", "weight": 100 }, { "size": "4", "note": "Spawn attempt succeeds only in slime chunks.", "mob": "Slime", "weight": 100 }, { "size": "4", "mob": "Skeleton", "weight": 20 }, { "size": "1&ndash;4", "mob": "Enderman", "weight": 10 }, { "size": "1", "mob": "Witch", "weight": 5 }, { "size": "1", "mob": "Zombie Villager", "weight": 5 } ], "totalWeight": 515 }, "ambient": { "mobs": [ { "size": "8", "mob": "Bat", "weight": 10 } ], "totalWeight": 10 } }
In Bedrock Edition:
| Mob            | Spawn weight      | Group size        |
|----------------|-------------------|-------------------|
|                |                   | Monster category  |
| Stray          | $\frac{96}{220}$  | 1–2               |
| Skeleton       | $\frac{24}{220}$  | 1–2               |
| Slime[note 1]  | $\frac{100}{220}$ | 1                 |
|                |                   | Creature category |
| Rabbit[note 2] | $\frac{4}{5}$     | 2–3               |
| Polar Bear     | $\frac{1}{5}$     | 1–2               |

1. ↑Spawn attempt succeeds only in slime chunks.
2. ↑80% of spawned rabbits are white and 20% are black and white.

{ "hostile": { "mobs": [ { "size": "1&ndash;2", "mob": "Stray", "weight": 96 }, { "size": "1&ndash;2", "mob": "Skeleton", "weight": 24 }, { "size": "1", "note": "Spawn attempt succeeds only in slime chunks.", "mob": "Slime", "weight": 100 } ], "totalWeight": 220 }, "passive": { "mobs": [ { "size": "2&ndash;3", "note": "80% of spawned rabbits are white and 20% are black and white.", "mob": "Rabbit", "weight": 4 }, { "size": "1&ndash;2", "mob": "Polar Bear", "weight": 1 } ], "totalWeight": 5 } }

### Snowy Taiga
#### Snowy Taiga Hills
| Structures    | Villages‌[BE  only]Pillager Outposts‌[BE  only]                            |
|---------------|----------------------------------------------------------------------------|
| Blocks        | Grass BlockSnowGrassFernSweet Berry Bush Large FernSpruce LogSpruce Leaves |
| Temperature   | -0.5                                                                       |
| Grass color   | #80B497                                                                    |
| Foliage color | #60A17B                                                                    |
| Water color   | #3D57D6‌[JE  only] #245B78‌[BE  only]                                      |

{
    "title": "Snowy Taiga Hills",
    "rows": [
        {
            "field": "(values exceeds 1000 characters...)",
            "label": "(link to Structures article, displayed as Structures)"
        },
        {
            "field": "(values exceeds 1000 characters...)",
            "label": "Blocks"
        },
        {
            "field": "-0.5",
            "label": "(link to Biome#Temperature article, displayed as Temperature)"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #80B497; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #80B497</span>",
            "label": "Grass color"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #60A17B; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #60A17B</span>",
            "label": "Foliage color"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #3D57D6; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #3D57D6</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Java Edition\">(link to Java Edition article, displayed as JE)  only</span></i>]</sup><br><span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #245B78; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #245B78</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Bedrock Edition\">(link to Bedrock Edition article, displayed as BE)  only</span></i>]</sup>",
            "label": "Water color"
        }
    ],
    "invimages": [],
    "images": [
        "Snowy Taiga Hills.png"
    ]
}
Like all other hills biomes, snowy taiga hills featured hillier, more erratic terrain. These hills were somewhat steep, making this variant difficult for survival mode. Pillager outposts and villages generated in this biome‌[BE  only], however, unlike the regular snowy taiga, igloos didn't generate here.

Snowy taiga hills used the same mob spawning chances as snowy taigas.


In Java Edition:
| Mob             | Spawn weight      | Group size        |
|-----------------|-------------------|-------------------|
|                 |                   | Creature category |
| Sheep           | $\frac{12}{60}$   | 4                 |
| Pig             | $\frac{10}{60}$   | 4                 |
| Chicken         | $\frac{10}{60}$   | 4                 |
| Cow             | $\frac{8}{60}$    | 4                 |
| Wolf            | $\frac{8}{60}$    | 4                 |
| Rabbit[note 1]  | $\frac{4}{60}$    | 2–3               |
| Fox[note 2]     | $\frac{8}{60}$    | 2–4               |
|                 |                   | Monster category  |
| Spider          | $\frac{100}{515}$ | 4                 |
| Zombie          | $\frac{95}{515}$  | 4                 |
| Zombie Villager | $\frac{5}{515}$   | 1                 |
| Skeleton        | $\frac{100}{515}$ | 4                 |
| Creeper         | $\frac{100}{515}$ | 4                 |
| Slime[note 3]   | $\frac{100}{515}$ | 4                 |
| Enderman        | $\frac{10}{515}$  | 1–4               |
| Witch           | $\frac{5}{515}$   | 1                 |
|                 |                   | Ambient category  |
| Bat             | 1                 | 8                 |

1. ↑80% of spawned rabbits are white and 20% are black and white.
2. ↑The foxes are snowy foxes.
3. ↑Spawn attempt succeeds only in slime chunks.

{ "passive": { "mobs": [ { "size": "4", "mob": "Sheep", "weight": 12 }, { "size": "4", "mob": "Pig", "weight": 10 }, { "size": "4", "mob": "Chicken", "weight": 10 }, { "size": "4", "mob": "Cow", "weight": 8 }, { "size": "4", "mob": "Wolf", "weight": 8 }, { "size": "2&ndash;3", "note": "80% of spawned rabbits are white and 20% are black and white.", "mob": "Rabbit", "weight": 4 }, { "size": "2&ndash;4", "note": "The foxes are snowy foxes.", "mob": "Fox", "weight": 8 } ], "totalWeight": 60 }, "hostile": { "mobs": [ { "size": "4", "mob": "Spider", "weight": 100 }, { "size": "4", "mob": "Zombie", "weight": 95 }, { "size": "1", "mob": "Zombie Villager", "weight": 5 }, { "size": "4", "mob": "Skeleton", "weight": 100 }, { "size": "4", "mob": "Creeper", "weight": 100 }, { "size": "4", "note": "Spawn attempt succeeds only in slime chunks.", "mob": "Slime", "weight": 100 }, { "size": "1&ndash;4", "mob": "Enderman", "weight": 10 }, { "size": "1", "mob": "Witch", "weight": 5 } ], "totalWeight": 515 }, "ambient": { "mobs": [ { "size": "8", "mob": "Bat", "weight": 10 } ], "totalWeight": 10 } }
In Bedrock Edition:
| Mob             | Spawn weight      | Group size        |
|-----------------|-------------------|-------------------|
|                 |                   | Creature category |
| Sheep           | $\frac{12}{60}$   | 2–3               |
| Pig             | $\frac{10}{60}$   | 1–3               |
| Chicken         | $\frac{10}{60}$   | 2–4               |
| Cow             | $\frac{8}{60}$    | 2–3               |
| Wolf            | $\frac{8}{60}$    | 4                 |
| Rabbit[note 1]  | $\frac{4}{60}$    | 2–3               |
| Fox[note 2]     | $\frac{8}{60}$    | 2–4               |
|                 |                   | Monster category  |
| Spider          | $\frac{100}{495}$ | 1                 |
| Zombie          | $\frac{95}{495}$  | 2–4               |
| Zombie Villager | $\frac{5}{495}$   | 2–4               |
| Skeleton        | $\frac{80}{495}$  | 1–2               |
| Creeper         | $\frac{100}{495}$ | 1                 |
| Slime[note 3]   | $\frac{100}{495}$ | 1                 |
| Enderman        | $\frac{10}{495}$  | 1–2               |
| Witch           | $\frac{5}{495}$   | 1                 |
|                 |                   | Ambient category  |
| Bat             | 1                 | 2                 |

1. ↑80% of spawned rabbits are white and 20% are black and white.
2. ↑The foxes are snowy foxes
3. ↑Spawn attempt succeeds only in slime chunks.

{ "passive": { "mobs": [ { "size": "2&ndash;3", "mob": "Sheep", "weight": 12 }, { "size": "1&ndash;3", "mob": "Pig", "weight": 10 }, { "size": "2&ndash;4", "mob": "Chicken", "weight": 10 }, { "size": "2&ndash;3", "mob": "Cow", "weight": 8 }, { "size": "4", "mob": "Wolf", "weight": 8 }, { "size": "2&ndash;3", "note": "80% of spawned rabbits are white and 20% are black and white.", "mob": "Rabbit", "weight": 4 }, { "size": "2&ndash;4", "note": "The foxes are snowy foxes", "mob": "Fox", "weight": 8 } ], "totalWeight": 60 }, "hostile": { "mobs": [ { "size": "1", "mob": "Spider", "weight": 100 }, { "size": "2&ndash;4", "mob": "Zombie", "weight": 95 }, { "size": "2&ndash;4", "mob": "Zombie Villager", "weight": 5 }, { "size": "1&ndash;2", "mob": "Skeleton", "weight": 80 }, { "size": "1", "mob": "Creeper", "weight": 100 }, { "size": "1", "note": "Spawn attempt succeeds only in slime chunks.", "mob": "Slime", "weight": 100 }, { "size": "1&ndash;2", "mob": "Enderman", "weight": 10 }, { "size": "1", "mob": "Witch", "weight": 5 } ], "totalWeight": 495 }, "ambient": { "mobs": [ { "size": "2", "mob": "Bat", "weight": 10 } ], "totalWeight": 10 } }

