#### Modified Jungle
| Blocks        | Grass BlockVinesJungle LogJungle LeavesCocoaOak LogOak LeavesMelonBamboo |
|---------------|--------------------------------------------------------------------------|
| Temperature   | 0.95                                                                     |
| Grass color   | #59C93C                                                                  |
| Foliage color | #30BB0B                                                                  |
| Water color   | #3F76E4‌[JE  only] #1B9ED8‌[BE  only]                                    |

{
    "title": "Modified Jungle",
    "rows": [
        {
            "field": "(values exceeds 1000 characters...)",
            "label": "Blocks"
        },
        {
            "field": "0.95",
            "label": "(link to Biome#Temperature article, displayed as Temperature)"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #59C93C; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #59C93C</span>",
            "label": "Grass color"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #30BB0B; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #30BB0B</span>",
            "label": "Foliage color"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #3F76E4; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #3F76E4</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Java Edition\">(link to Java Edition article, displayed as JE)  only</span></i>]</sup><br><span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #1B9ED8; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #1B9ED8</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Bedrock Edition\">(link to Bedrock Edition article, displayed as BE)  only</span></i>]</sup>",
            "label": "Water color"
        }
    ],
    "invimages": [],
    "images": [
        "Modified Jungle.png"
    ]
}
The rare modified jungle variant featured much more mountainous terrain, being taller and steeper than jungle hills. The heights, combined with the thick foliage, rendered the ground below almost entirely out of sight. Ocelots, parrots, and pandas spawned in this biome, but jungle pyramids didn't generate here.
In Java Edition, modified jungles used the same mob spawning chances as jungle hills for hostile and ambient categories, and had different chances for passive categories:
| Mob             | Spawn weight      | Group size        |
|-----------------|-------------------|-------------------|
|                 |                   | Creature category |
| Sheep           | $\frac{12}{60}$   | 4                 |
| Pig             | $\frac{10}{60}$   | 4                 |
| Chicken         | $\frac{10}{60}$   | 4                 |
| Cow             | $\frac{8}{60}$    | 4                 |
| Parrot          | $\frac{10}{60}$   | 1                 |
| Chicken         | $\frac{10}{60}$   | 4                 |
|                 |                   | Monster category  |
| Spider          | $\frac{100}{515}$ | 4                 |
| Zombie          | $\frac{95}{515}$  | 4                 |
| Zombie Villager | $\frac{5}{515}$   | 1                 |
| Skeleton        | $\frac{100}{515}$ | 4                 |
| Creeper         | $\frac{100}{515}$ | 4                 |
| Slime[note 1]   | $\frac{100}{515}$ | 4                 |
| Enderman        | $\frac{10}{515}$  | 1–4               |
| Witch           | $\frac{5}{515}$   | 1                 |
|                 |                   | Ambient category  |
| Bat             | 1                 | 8                 |

1. ↑Spawn attempt succeeds only in slime chunks.

{ "passive": { "mobs": [ { "size": "4", "mob": "Sheep", "weight": 12 }, { "size": "4", "mob": "Pig", "weight": 10 }, { "size": "4", "mob": "Chicken", "weight": 10 }, { "size": "4", "mob": "Cow", "weight": 8 }, { "size": "1", "mob": "Parrot", "weight": 10 }, { "size": "4", "mob": "Chicken", "weight": 10 } ], "totalWeight": 60 }, "hostile": { "mobs": [ { "size": "4", "mob": "Spider", "weight": 100 }, { "size": "4", "mob": "Zombie", "weight": 95 }, { "size": "1", "mob": "Zombie Villager", "weight": 5 }, { "size": "4", "mob": "Skeleton", "weight": 100 }, { "size": "4", "mob": "Creeper", "weight": 100 }, { "size": "4", "note": "Spawn attempt succeeds only in slime chunks.", "mob": "Slime", "weight": 100 }, { "size": "1&ndash;4", "mob": "Enderman", "weight": 10 }, { "size": "1", "mob": "Witch", "weight": 5 } ], "totalWeight": 515 }, "ambient": { "mobs": [ { "size": "8", "mob": "Bat", "weight": 10 } ], "totalWeight": 10 } }
In Bedrock Edition, modified jungles used the same mob spawning chances as jungles:
| Mob             | Spawn weight      | Group size        |
|-----------------|-------------------|-------------------|
|                 |                   | Creature category |
| Sheep           | $\frac{12}{120}$  | 2–3               |
| Pig             | $\frac{10}{120}$  | 1–3               |
| Chicken         | $\frac{10}{120}$  | 2–4               |
| Cow             | $\frac{8}{120}$   | 2–3               |
| Parrot          | $\frac{40}{120}$  | 1–2               |
| Panda           | $\frac{10}{120}$  | 1–2               |
| Ocelot          | $\frac{30}{120}$  | 1–2               |
|                 |                   | Monster category  |
| Spider          | $\frac{100}{495}$ | 1                 |
| Zombie          | $\frac{95}{495}$  | 2–4               |
| Zombie Villager | $\frac{5}{495}$   | 2–4               |
| Skeleton        | $\frac{80}{495}$  | 1–2               |
| Creeper         | $\frac{100}{495}$ | 1                 |
| Slime[note 1]   | $\frac{100}{495}$ | 1                 |
| Enderman        | $\frac{10}{495}$  | 1–2               |
| Witch           | $\frac{5}{495}$   | 1                 |
|                 |                   | Ambient category  |
| Bat             | 1                 | 2                 |

1. ↑Spawn attempt succeeds only in slime chunks.

{ "passive": { "mobs": [ { "size": "2&ndash;3", "mob": "Sheep", "weight": 12 }, { "size": "1&ndash;3", "mob": "Pig", "weight": 10 }, { "size": "2&ndash;4", "mob": "Chicken", "weight": 10 }, { "size": "2&ndash;3", "mob": "Cow", "weight": 8 }, { "size": "1&ndash;2", "mob": "Parrot", "weight": 40 }, { "size": "1&ndash;2", "mob": "Panda", "weight": 10 }, { "size": "1&ndash;2", "mob": "Ocelot", "weight": 30 } ], "totalWeight": 120 }, "hostile": { "mobs": [ { "size": "1", "mob": "Spider", "weight": 100 }, { "size": "2&ndash;4", "mob": "Zombie", "weight": 95 }, { "size": "2&ndash;4", "mob": "Zombie Villager", "weight": 5 }, { "size": "1&ndash;2", "mob": "Skeleton", "weight": 80 }, { "size": "1", "mob": "Creeper", "weight": 100 }, { "size": "1", "note": "Spawn attempt succeeds only in slime chunks.", "mob": "Slime", "weight": 100 }, { "size": "1&ndash;2", "mob": "Enderman", "weight": 10 }, { "size": "1", "mob": "Witch", "weight": 5 } ], "totalWeight": 495 }, "ambient": { "mobs": [ { "size": "2", "mob": "Bat", "weight": 10 } ], "totalWeight": 10 } }

#### Modified Jungle Edge
| Blocks        | Grass BlockVinesJungle LogJungle LeavesCocoaOak LogOak LeavesMelonPumpkin |
|---------------|---------------------------------------------------------------------------|
| Temperature   | 0.95                                                                      |
| Grass color   | #64C73F                                                                   |
| Foliage color | #3EB80F                                                                   |
| Water color   | #3F76E4‌[JE  only] #0D8AE3‌[BE  only]                                     |

{
    "title": "Modified Jungle Edge",
    "rows": [
        {
            "field": "(values exceeds 1000 characters...)",
            "label": "Blocks"
        },
        {
            "field": "0.95",
            "label": "(link to Biome#Temperature article, displayed as Temperature)"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #64C73F; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #64C73F</span>",
            "label": "Grass color"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #3EB80F; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #3EB80F</span>",
            "label": "Foliage color"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #3F76E4; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #3F76E4</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Java Edition\">(link to Java Edition article, displayed as JE)  only</span></i>]</sup><br><span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #0D8AE3; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #0D8AE3</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Bedrock Edition\">(link to Bedrock Edition article, displayed as BE)  only</span></i>]</sup>",
            "label": "Water color"
        }
    ],
    "invimages": [],
    "images": [
        "Modified Jungle Edge.png"
    ]
}
The rare modified jungle edge variant generated only in strict conditions, and it was the rarest biome in the game. If a jungle biome bordered a swamp hills biome,[2] then the modified jungle edge spawned as part of a double-layered transition, with a thin normal jungle edge bordering the swamp hills, and the modified jungle edge bordering the jungle. As both jungles and swamp hills were already rare, and even more rarely did they generate bordering each other, the conditions for a modified jungle edge to generate were rarely met. When they actually did manage to generate, they were often just a few hundred blocks in length, but in some cases were less than 10 blocks, making them one of the smallest biomes as well. Modified jungle edges featured the same smooth transition and lowered tree density that regular jungle edges had, though with much more mountainous terrain and occasional overhangs. Ocelots, parrots, and pandas spawned in this biome, but jungle pyramids didn't generate here. Modified jungle edges covered only a few millionths (0.00027%) of the overworld by area.

Modified jungle edges used the same mob spawning chances as jungle edges.


In Java Edition:
| Mob             | Spawn weight      | Group size        |
|-----------------|-------------------|-------------------|
|                 |                   | Creature category |
| Sheep           | $\frac{12}{50}$   | 4                 |
| Pig             | $\frac{10}{50}$   | 4                 |
| Chicken         | $\frac{10}{50}$   | 4                 |
| Cow             | $\frac{8}{50}$    | 4                 |
| Chicken         | $\frac{10}{50}$   | 4                 |
|                 |                   | Monster category  |
| Spider          | $\frac{100}{515}$ | 4                 |
| Zombie          | $\frac{95}{515}$  | 4                 |
| Zombie Villager | $\frac{5}{515}$   | 1                 |
| Skeleton        | $\frac{100}{515}$ | 4                 |
| Creeper         | $\frac{100}{515}$ | 4                 |
| Slime[note 1]   | $\frac{100}{515}$ | 4                 |
| Enderman        | $\frac{10}{515}$  | 1–4               |
| Witch           | $\frac{5}{515}$   | 1                 |
|                 |                   | Ambient category  |
| Bat             | 1                 | 8                 |

1. ↑Spawn attempt succeeds only in slime chunks.

{ "passive": { "mobs": [ { "size": "4", "mob": "Sheep", "weight": 12 }, { "size": "4", "mob": "Pig", "weight": 10 }, { "size": "4", "mob": "Chicken", "weight": 10 }, { "size": "4", "mob": "Cow", "weight": 8 }, { "size": "4", "mob": "Chicken", "weight": 10 } ], "totalWeight": 50 }, "hostile": { "mobs": [ { "size": "4", "mob": "Spider", "weight": 100 }, { "size": "4", "mob": "Zombie", "weight": 95 }, { "size": "1", "mob": "Zombie Villager", "weight": 5 }, { "size": "4", "mob": "Skeleton", "weight": 100 }, { "size": "4", "mob": "Creeper", "weight": 100 }, { "size": "4", "note": "Spawn attempt succeeds only in slime chunks.", "mob": "Slime", "weight": 100 }, { "size": "1&ndash;4", "mob": "Enderman", "weight": 10 }, { "size": "1", "mob": "Witch", "weight": 5 } ], "totalWeight": 515 }, "ambient": { "mobs": [ { "size": "8", "mob": "Bat", "weight": 10 } ], "totalWeight": 10 } }
In Bedrock Edition:
| Mob             | Spawn weight      | Group size        |
|-----------------|-------------------|-------------------|
|                 |                   | Creature category |
| Sheep           | $\frac{12}{120}$  | 2–3               |
| Pig             | $\frac{10}{120}$  | 1–3               |
| Chicken         | $\frac{10}{120}$  | 2–4               |
| Cow             | $\frac{8}{120}$   | 2–3               |
| Parrot          | $\frac{40}{120}$  | 1–2               |
| Panda           | $\frac{10}{120}$  | 1–2               |
| Ocelot          | $\frac{30}{120}$  | 1–2               |
|                 |                   | Monster category  |
| Spider          | $\frac{100}{495}$ | 1                 |
| Zombie          | $\frac{95}{495}$  | 2–4               |
| Zombie Villager | $\frac{5}{495}$   | 2–4               |
| Skeleton        | $\frac{80}{495}$  | 1–2               |
| Creeper         | $\frac{100}{495}$ | 1                 |
| Slime[note 1]   | $\frac{100}{495}$ | 1                 |
| Enderman        | $\frac{10}{495}$  | 1–2               |
| Witch           | $\frac{5}{495}$   | 1                 |
|                 |                   | Ambient category  |
| Bat             | 1                 | 2                 |

1. ↑Spawn attempt succeeds only in slime chunks.

{ "passive": { "mobs": [ { "size": "2&ndash;3", "mob": "Sheep", "weight": 12 }, { "size": "1&ndash;3", "mob": "Pig", "weight": 10 }, { "size": "2&ndash;4", "mob": "Chicken", "weight": 10 }, { "size": "2&ndash;3", "mob": "Cow", "weight": 8 }, { "size": "1&ndash;2", "mob": "Parrot", "weight": 40 }, { "size": "1&ndash;2", "mob": "Panda", "weight": 10 }, { "size": "1&ndash;2", "mob": "Ocelot", "weight": 30 } ], "totalWeight": 120 }, "hostile": { "mobs": [ { "size": "1", "mob": "Spider", "weight": 100 }, { "size": "2&ndash;4", "mob": "Zombie", "weight": 95 }, { "size": "2&ndash;4", "mob": "Zombie Villager", "weight": 5 }, { "size": "1&ndash;2", "mob": "Skeleton", "weight": 80 }, { "size": "1", "mob": "Creeper", "weight": 100 }, { "size": "1", "note": "Spawn attempt succeeds only in slime chunks.", "mob": "Slime", "weight": 100 }, { "size": "1&ndash;2", "mob": "Enderman", "weight": 10 }, { "size": "1", "mob": "Witch", "weight": 5 } ], "totalWeight": 495 }, "ambient": { "mobs": [ { "size": "2", "mob": "Bat", "weight": 10 } ], "totalWeight": 10 } }

