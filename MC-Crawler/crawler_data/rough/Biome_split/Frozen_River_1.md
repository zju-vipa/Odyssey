### Frozen river
| Blocks        | IceWaterGrass BlockDirtClaySandGravel |
|---------------|---------------------------------------|
| Temperature   | 0.0                                   |
| Downfall      | 0.5                                   |
| Precipitation | Yes                                   |
| Grass color   | #80B497                               |
| Foliage color | #60A17B                               |
| Water color   | #3938C9‌[JE  only] #185390‌[BE  only] |

{
    "title": "Frozen River",
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
            "field": "0.5",
            "label": "(link to Biome#Downfall article, displayed as Downfall)"
        },
        {
            "field": "Yes",
            "label": "(link to Biome#Precipitation article, displayed as Precipitation)"
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
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #3938C9; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #3938C9</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Java Edition\">(link to Java Edition article, displayed as JE)  only</span></i>]</sup><br><span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #185390; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #185390</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Bedrock Edition\">(link to Bedrock Edition article, displayed as BE)  only</span></i>]</sup>",
            "label": "Water color"
        }
    ],
    "invimages": [],
    "images": [
        "Frozen River.png"
    ]
}
Frozen rivers replace regular rivers in regions with snowy biomes. As the name implies, the top layer of water is entirely frozen, although some non-frozen water can still remain under trees and overhangs. Seagrass does not generate on the riverbed. While sugar cane can generate alongside a frozen riverbank, it often quickly uproots itself after generation due to the water being frozen. Oak trees and grass can still generate here if this biome generates on land. Sometimes, frozen rivers can generate next to regular taiga biomes, as taiga biomes are able to generate in the same temperature range as frozen rivers. This results in weird, albeit intentional[1], generation.

The following mobs are naturally spawned here：

| Mob             | Spawn weight      | Group size                          |
|-----------------|-------------------|-------------------------------------|
|                 |                   | Monster category                    |
| Creeper         | $\frac{100}{516}$ | 4                                   |
| Skeleton        | $\frac{100}{516}$ | 4                                   |
| Slime[note 1]   | $\frac{100}{516}$ | 4                                   |
| Spider          | $\frac{100}{516}$ | 4                                   |
| Zombie          | $\frac{95}{516}$  | 4                                   |
| Enderman        | $\frac{10}{516}$  | 1–4                                 |
| Witch           | $\frac{5}{516}$   | 1                                   |
| Zombie Villager | $\frac{5}{516}$   | 1                                   |
| Drowned         | $\frac{1}{516}$   | 1                                   |
|                 |                   | Water ambient category              |
| Salmon          | 1                 | 1–5                                 |
|                 |                   | Water creature category             |
| Squid           | 1                 | 1–4                                 |
|                 |                   | Ambient category                    |
| Bat             | 1                 | 8                                   |
|                 |                   | Underground water creature category |
| Glow Squid      | 1                 | 4–6                                 |

1. ↑Spawn attempt succeeds only in slime chunks.

{ "monster": { "mobs": [ { "size": "4", "mob": "Creeper", "weight": 100 }, { "size": "4", "mob": "Skeleton", "weight": 100 }, { "size": "4", "note": "Spawn attempt succeeds only in slime chunks.", "mob": "Slime", "weight": 100 }, { "size": "4", "mob": "Spider", "weight": 100 }, { "size": "4", "mob": "Zombie", "weight": 95 }, { "size": "1&ndash;4", "mob": "Enderman", "weight": 10 }, { "size": "1", "mob": "Witch", "weight": 5 }, { "size": "1", "mob": "Zombie Villager", "weight": 5 }, { "size": "1", "mob": "Drowned", "weight": 1 } ], "totalWeight": 516 }, "waterambient": { "mobs": [ { "size": "1&ndash;5", "mob": "Salmon", "weight": 5 } ], "totalWeight": 5 }, "watercreature": { "mobs": [ { "size": "1&ndash;4", "mob": "Squid", "weight": 2 } ], "totalWeight": 2 }, "ambient": { "mobs": [ { "size": "8", "mob": "Bat", "weight": 10 } ], "totalWeight": 10 }, "underground": { "mobs": [ { "size": "4&ndash;6", "mob": "Glow Squid", "weight": 10 } ], "totalWeight": 10 } }
| Mob           | Spawn weight      | Group size              |
|---------------|-------------------|-------------------------|
|               |                   | Monster category        |
| Slime[note 1] | $\frac{100}{225}$ | 1                       |
| Stray         | $\frac{96}{225}$  | 1–2                     |
| Skeleton      | $\frac{24}{225}$  | 1–2                     |
| Drowned       | $\frac{5}{225}$   | 2–4                     |
|               |                   | Creature category       |
| Glow Squid    | $\frac{10}{23}$   | 2–4                     |
| Squid         | $\frac{8}{23}$    | 2–4                     |
| Rabbit        | $\frac{4}{23}$    | 2–3                     |
| Polar Bear    | $\frac{1}{23}$    | 1–2                     |
|               |                   | Water creature category |
| Salmon        | 1                 | 3–5                     |

1. ↑Spawn attempt succeeds only in slime chunks.

{ "monster": { "mobs": [ { "size": "1", "note": "Spawn attempt succeeds only in slime chunks.", "mob": "Slime", "weight": 100 }, { "size": "1&ndash;2", "mob": "Stray", "weight": 96 }, { "size": "1&ndash;2", "mob": "Skeleton", "weight": 24 }, { "size": "2&ndash;4", "mob": "Drowned", "weight": 5 } ], "totalWeight": 225 }, "creature": { "mobs": [ { "size": "2&ndash;4", "mob": "Glow Squid", "weight": 10 }, { "size": "2&ndash;4", "mob": "Squid", "weight": 8 }, { "size": "2&ndash;3", "mob": "Rabbit", "weight": 4 }, { "size": "1&ndash;2", "mob": "Polar Bear", "weight": 1 } ], "totalWeight": 23 }, "watercreature": { "mobs": [ { "size": "3&ndash;5", "mob": "Salmon", "weight": 16 } ], "totalWeight": 16 } }

