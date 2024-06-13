### Generation of rivers
A layer stack for river noise generation was used as a random number generator to generate areas of hills and mutated biomes, which was scaled twice before applied to the biome stage of biome generation at scale 1 to 64. Since Update Aquatic, modified biomes could conform to an entire biome or border a river. A separate layer stack to generate rivers throughout was scaled 4 times, before it was merged with the rest of the generation at scale 1 to 4.

Rivers generated across all land biomes excluding areas of oceans. Frozen rivers replaced rivers in regular snowy tundra.

Once the ocean temperature stack and river generation stack was merged with the biome generation stack, a final layer was applied to make the biome scale 1:1, which was the final biome generation used in Minecraft.

### Java Edition oceanic temperature generation
Ocean biomes generated their climate zones separately from land biome generation, to avoid changing existing Minecraft seeds/biome generation in its entirely. Ocean climate zones were initialized at a scale of 1 to 256, then scaled 6 times, before it was merged with the rest of the biome generation.

In Java Edition, ocean climate areas were done so warm oceans could not border frozen oceans. One must go incrementally from warm oceans, to lukewarm oceans, regular oceans, and cold oceans, before reaching frozen oceans.

If a frozen ocean or frozen deep ocean bordered a land biome, a regular cold ocean generated. If a warm ocean generated next to a land biome, a regular lukewarm ocean generated. Warm oceans overwrote deep oceans as warm deep oceans did not generate.

Ocean climate zones were based off the 48 bit seed, unlike the rest of the land biome generation, as such, shadow seeds in Java Edition contained entirely different ocean climate areas, even though common land biomes generated identically in Java Edition shadow seeds.

### Other information
In Java Edition, the possible shapes of biomes could use only the first 24 bits of the 64-bit world seed, and biome shapes within a world seed could repeat beginning around 229 blocks from 0,0. Biome generation overflowed at 231 blocks from 0,0. However, as biomes were generated in a zoomed out stage, before it was scaled upward, it technically means that biome generation could extend further out during earlier stages of biome generation as the integer overflow point is further out.

Even though there are 64-bit seeds on Java, there were only 263 unique noise maps for continental/ocean biome generation, because a quadratic equation was used, and quadratic equations always can be mirrored so that for every input except one to the quadratic equation, there is another that results in the same output (halving the number of truly distinct possibilities). For any seed, the other seed resulting in the same output to this equation was colloquially known as a shadow seed. In this case, land biome and general ocean biomes were exactly the same in a pair of seeds, but ocean biome temperatures, structures and hills differed in the shadow seed. A user could find a shadow seed by adding the constant -7379792620528906219 to the negative of their current world seed, to obtain the shadow seed. Shadow seeds were exclusive to Java Edition.

With Bedrock Edition using 32-bit seeds and a different world generation algorithm, there were few similarities between it and the 64-bit world generation. The positions of mutated biomes, oceans (and islands), rare biomes (jungles, badlands, mushroom fields, giant tree taiga), as well as specific biomes in cold, temperate, or dry biome clusters, bore some geographical relationship with the equivalent positive value seed of the 64-bit generation. The biome shapes deviated significantly. The specific generation of lush biomes and ocean variants was completely different on Bedrock.

| Java Edition biomes before 1.18 | Bedrock Edition biomes before 1.18 |
|---------------------------------|------------------------------------|

## 
### Badlands
#### Badlands Plateau
| Structures    | Badlands mineshafts                                         |
|---------------|-------------------------------------------------------------|
| Blocks        | Red SandTerracottaStained TerracottaCactusDead BushGold Ore |
| Temperature   | 2.0                                                         |
| Grass color   | #90814D                                                     |
| Foliage color | #9E814D                                                     |
| Water color   | #3F76E4‌[JE  only] #55809E‌[BE  only]                       |

{
    "title": "Badlands Plateau",
    "rows": [
        {
            "field": "<span class=\"nowrap\"><span class=\"sprite-file\" style=\"\">(link to File:EnvSprite badlands-mineshaft.png article, displayed as 16x16px|link=Badlands mineshaft|alt=EnvSprite badlands-mineshaft.png: Sprite image for badlands-mineshaft in Minecraft linking to Badlands mineshaft|class=pixel-image|)</span>(link to Badlands mineshaft article, displayed as <span class=\"sprite-text\">Badlands mineshaft</span>)</span>s",
            "label": "(link to Structures article, displayed as Structures)"
        },
        {
            "field": "(values exceeds 1000 characters...)",
            "label": "Blocks"
        },
        {
            "field": "2.0",
            "label": "(link to Biome#Temperature article, displayed as Temperature)"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #90814D; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #90814D</span>",
            "label": "Grass color"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #9E814D; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #9E814D</span>",
            "label": "Foliage color"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #3F76E4; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #3F76E4</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Java Edition\">(link to Java Edition article, displayed as JE)  only</span></i>]</sup><br><span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #55809E; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #55809E</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Bedrock Edition\">(link to Bedrock Edition article, displayed as BE)  only</span></i>]</sup>",
            "label": "Water color"
        }
    ],
    "invimages": [],
    "images": [
        "Badlands Plateau.png"
    ]
}
The badlands plateau featured large flat-topped hills composed of stratified colors of terracotta ranging in warm colors. Plateaus had steep edges that rose to within 20-30 blocks above sea level, where they quickly flatten. The top of these plateaus typically had scattered dead bushes. Occasional ponds appeared on plateau tops. The sides of the plateau occasionally revealed caverns and mineshafts. River biomes that passed through badlands plateau biomes cut steep grooves, giving off the appearance of narrow canyons. These posed a fall damage hazard if the player was not careful. Ravines also frequently spawned in badlands plateau biomes, which caused the same as above. This biome was not always present in the badlands biomes, but it was likely to appear.

Badlands plateaus used the same mob spawning chances as badlands.


In Java Edition:
| Mob             | Spawn weight      | Group size       |
|-----------------|-------------------|------------------|
|                 |                   | Monster category |
| Spider          | $\frac{100}{515}$ | 4                |
| Zombie          | $\frac{95}{515}$  | 4                |
| Zombie Villager | $\frac{5}{515}$   | 1                |
| Skeleton        | $\frac{100}{515}$ | 4                |
| Creeper         | $\frac{100}{515}$ | 4                |
| Slime[note 1]   | $\frac{100}{515}$ | 4                |
| Enderman        | $\frac{10}{515}$  | 1–4              |
| Witch           | $\frac{5}{515}$   | 1                |
|                 |                   | Ambient category |
| Bat             | 1                 | 8                |

1. ↑Spawn attempt succeeds only in slime chunks.

{ "hostile": { "mobs": [ { "size": "4", "mob": "Spider", "weight": 100 }, { "size": "4", "mob": "Zombie", "weight": 95 }, { "size": "1", "mob": "Zombie Villager", "weight": 5 }, { "size": "4", "mob": "Skeleton", "weight": 100 }, { "size": "4", "mob": "Creeper", "weight": 100 }, { "size": "4", "note": "Spawn attempt succeeds only in slime chunks.", "mob": "Slime", "weight": 100 }, { "size": "1&ndash;4", "mob": "Enderman", "weight": 10 }, { "size": "1", "mob": "Witch", "weight": 5 } ], "totalWeight": 515 }, "ambient": { "mobs": [ { "size": "8", "mob": "Bat", "weight": 10 } ], "totalWeight": 10 } }
In Bedrock Edition:
| Mob             | Spawn weight      | Group size       |
|-----------------|-------------------|------------------|
|                 |                   | Monster category |
| Spider          | $\frac{100}{495}$ | 1                |
| Zombie          | $\frac{95}{495}$  | 2–4              |
| Zombie Villager | $\frac{5}{495}$   | 2–4              |
| Skeleton        | $\frac{80}{495}$  | 1–2              |
| Creeper         | $\frac{100}{495}$ | 1                |
| Slime[note 1]   | $\frac{100}{495}$ | 1                |
| Enderman        | $\frac{10}{495}$  | 1–2              |
| Witch           | $\frac{5}{495}$   | 1                |

1. ↑Spawn attempt succeeds only in slime chunks.

{ "hostile": { "mobs": [ { "size": "1", "mob": "Spider", "weight": 100 }, { "size": "2&ndash;4", "mob": "Zombie", "weight": 95 }, { "size": "2&ndash;4", "mob": "Zombie Villager", "weight": 5 }, { "size": "1&ndash;2", "mob": "Skeleton", "weight": 80 }, { "size": "1", "mob": "Creeper", "weight": 100 }, { "size": "1", "note": "Spawn attempt succeeds only in slime chunks.", "mob": "Slime", "weight": 100 }, { "size": "1&ndash;2", "mob": "Enderman", "weight": 10 }, { "size": "1", "mob": "Witch", "weight": 5 } ], "totalWeight": 495 } }

