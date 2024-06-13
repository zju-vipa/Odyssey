# Biome/Before 1.18
In Java Edition 1.18 and Bedrock Edition 1.18.0, Overworld terrain generation was rewritten to become more varied and independent of biome generation. This made many biome variants that were in the game redundant, as the only difference between their regular counterparts was the way terrain generated in them. As a result, most variant biomes were removed from the generator. In Java Edition, these biomes were merged with their normal variants, while in Bedrock Edition, these biomes still exist, but remain unused.

## Contents
- 1 Generation
	- 1.1 Earlier stages
	- 1.2 Generation of biomes and biome variants
	- 1.3 Generation of rivers
	- 1.4 Java Edition oceanic temperature generation
	- 1.5 Other information
- 2 Removed/Unused biomes
	- 2.1 Badlands
		- 2.1.1 Badlands Plateau
		- 2.1.2 Modified Badlands Plateau
		- 2.1.3 Modified Wooded Badlands Plateau
	- 2.2 Birch forest
		- 2.2.1 Birch Forest Hills
		- 2.2.2 Tall Birch Hills
	- 2.3 Dark Forest Hills
	- 2.4 Deep Warm Ocean
	- 2.5 Desert
		- 2.5.1 Desert Hills
		- 2.5.2 Desert Lakes
	- 2.6 Giant Taiga
		- 2.6.1 Giant Spruce Taiga Hills
		- 2.6.2 Giant Tree Taiga Hills
	- 2.7 Jungle
		- 2.7.1 Bamboo Jungle Hills
		- 2.7.2 Jungle Hills
		- 2.7.3 Modified Jungle
		- 2.7.4 Modified Jungle Edge
	- 2.8 Mountains
		- 2.8.1 Gravelly Mountains+
		- 2.8.2 Mountain Edge
	- 2.9 Mushroom Field Shore
	- 2.10 Shattered Savanna Plateau
	- 2.11 Snowy Mountains
	- 2.12 Snowy Taiga
		- 2.12.1 Snowy Taiga Hills
		- 2.12.2 Snowy Taiga Mountains
	- 2.13 Swamp Hills
	- 2.14 Taiga
		- 2.14.1 Taiga Hills
		- 2.14.2 Taiga Mountains
	- 2.15 Wooded Hills
- 3 Data values
	- 3.1 ID
- 4 History
- 5 References

## Generation
Minecraft biomes were generated in layer stacks. These layers generated specific aspects of Minecraft biomes, such as scale, rivers, varieties, and biome categories.

### Earlier stages
Biome generation was initialized as a 1 to 4096 scale of ocean, with a few spots of landmasses scattered throughout. This map was then scaled and additional landmasses shuffled around to decrease the amount of ocean, twice, to reach a scale of 1 to 1024. Additional layers that decrease the amount of ocean were repeatedly applied until the ratio of land to ocean was about 50-50. Snowy biome categories were then assigned to a few spots of land, which was then shuffled around a final time to obtain a ratio of 33% ocean and 67% landmass.

At this stage of biome generation, the final climate zones were applied as follows. Areas of dry landmasses were assigned to be a normal biome if it bordered a cold or frozen landmass. Areas of snowy landmasses were assigned to the cold temperature category if it bordered a normal or dry temperature zone. 1 out of every 13 landmasses was then marked as "Special", which would be used to place some of the rarer biomes in later stages of biome generation. This map was then scaled twice, until a scale of 1 to 256. An additional layer was applied to create a more jagged coastline, creating areas of large islands and lakes around the coastline. 1 out of 100 areas of oceans were assigned as mushroom biomes and areas of ocean far from the coast converted into deep ocean.

The final areas of climate areas were as follows: 31% oceanic, which consisted of 22% deep ocean and 9% ocean, 0.07% mushroom, 13% dry, 22% medium, 23% cold, and 6% frozen. Areas of rare biomes made up 4% of the total area.

The biome generation was then split into 3 separate stacks.

### Generation of biomes and biome variants
One stack of biome generation generated the actual biomes in-game. The biome categories generated the following biomes as follows. Some biomes were weighed more and as such generated more commonly than other biomes. Snowy biomes had an unused rare biome variant and as such generated as normal snowy biomes.

- Dry biome clusters: desert (3 times), savanna (2 times), plains
- Rare dry biome clusters: 2/3 badlands (0.9% of the final map)
- Medium biome clusters: forest, dark forest, birch forest, windswept hills, swamp, plains
- Rare medium biome clusters: jungle (1.5% of the final map)
- Cold biome clusters: forest, windswept hills, taiga, plains
- Rare cold biome clusters:giant tree taiga(1.6% of the final map)
- Frozen biome clusters: snowy plains (3 times), snowy taiga

Forest and mountain biomes could generate in both cold biome clusters in addition to normal temperature clusters. Plains biomes could generate in all temperature clusters except in frozen biomes.

Bamboo jungles overwrote certain areas of jungle biomes since Village and Pillage.

This map is scaled twice until a scale of 1 to 64 in both Java and Bedrock Editions. In Legacy Console Edition, the map is not scaled at all at this stage of biome generation unless biome size was set to medium or large. To ensure a smooth transition between biomes, some biomes generate an "edge biome" as follows. These edge biomes can also generate hills and modified biome variants:

- Badlands plateau and wooded badlands plateau generate regular badlands on all edges.
- Giant tree taiga generates the regular taiga on all edges, unless there is a pre-existing snowy Taiga or taiga bordering it.
- If a desert borders a snowy tundra, a wooded mountain generates.
- If a swamp borders a jungle, a jungle edge generates. If a swamp borders a desert, snowy taiga, or snowy tundra, a plains biome generates.

Modified and hill biomes are then merged into the biome generation. Most biomes have a "hills" variant but some biomes use other biomes as their "hills" variant, which are listed below. This stage also allows islands to generate in areas of Deep Ocean:

- Dark forest -> plains
- Plains -> 1/3 wooded hills, 2/3 forest
- Snowy tundra -> snowy mountains
- Ocean -> deep ocean
- Savanna -> savanna plateau
- Deep ocean -> 1/2 plains, 1/2 forest
- Wooded badlands plateau and badlands plateau -> regular badlands

Swamps and regular badlands do not generate a hills biome variant. Oceans do not have a "modified" biome variant. While most biomes have a "modified" variant, few biomes generate a unique "modified hills" variant, such as birch forests and mountain biomes. Some other biomes use another existing biome as a "modified hills" variant. If a biome does not have a "modified hills" variant, such as swamps or snowy taigas, the regular biome variant generates instead.

Additional areas of sunflower plains were generated separately to the modified biome stage of biome generation, covering 1/57 of normal plains biome.

The map was then scaled and the coastline made more jagged, then scaled again and beaches are generated. The generation of shorelines and beaches were as follows, this also added a few additional biome edge biomes for jungles and badlands, without biome variants:

- Beaches generated on all coastlines except the regular swamp and regular badlands biomes.
- Stone shores generated on the coastline of the standard mountains andwooded mountainbiomes.
- Snowy beaches generated on the coastline of all frozen biomes.
- Mushroom shores generates on the coastline of all mushroom fields biomes.
- A regular desert generates on the edge of all badlands biomes, excluding eroded badlands. The desert border does not generate next to oceans.

This also creates unique quirks in generation, where gravelly mountains and swamp hills generate a beach biome, and swamp hills bordering a regular jungle edge, with a modified jungle edge bordering jungles.

This biome map was scaled two more times (scaled 4x) until a scale of 1 to 4. River generation was merged with the regular biomes, then ocean climate zones merged.

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

#### Modified Badlands Plateau
| Structures    | Badlands mineshafts                                         |
|---------------|-------------------------------------------------------------|
| Blocks        | Red SandTerracottaStained TerracottaCactusDead BushGold Ore |
| Temperature   | 2.0                                                         |
| Grass color   | #90814D                                                     |
| Foliage color | #9E814D                                                     |
| Water color   | #3F76E4‌[JE  only] #55809E‌[BE  only]                       |

{
    "title": "Modified Badlands Plateau",
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
        "Modified Badlands Plateau.png"
    ]
}
The modified badlands plateau featured smaller plateaus and somewhat harsher terrain than the badlands plateau, mimicking large plateaus that have weathered more over time. Eroded badlands replaced the usual thin desert border that this biome variant shared with other biomes. The modified badlands plateau was the second rarest biome in Minecraft, after modified jungle edge, and was only present in about 1/5 of the badlands biomes, and almost always (98% chance) came with an eroded badlands bordering the edges and modified wooded badlands plateaus surrounding it at the center.

Modified badlands plateaus used the same mob spawning chances as badlands.


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

#### Modified Wooded Badlands Plateau
| Structures    | Badlands mineshafts                                                                                     |
|---------------|---------------------------------------------------------------------------------------------------------|
| Blocks        | Red Sand‌[JE  only]TerracottaStained TerracottaCactusDead BushGrassCoarse DirtOak LogOak LeavesGold Ore |
| Temperature   | 2.0                                                                                                     |
| Grass color   | #90814D                                                                                                 |
| Foliage color | #9E814D                                                                                                 |
| Water color   | #3F76E4‌[JE  only] #497F99‌[BE  only]                                                                   |

{
    "title": "Modified Wooded Badlands Plateau",
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
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #3F76E4; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #3F76E4</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Java Edition\">(link to Java Edition article, displayed as JE)  only</span></i>]</sup><br><span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #497F99; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #497F99</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Bedrock Edition\">(link to Bedrock Edition article, displayed as BE)  only</span></i>]</sup>",
            "label": "Water color"
        }
    ],
    "invimages": [],
    "images": [
        "Modified Wooded Badlands Plateau.png"
    ]
}
Similar to the modified badlands plateau, the modified wooded badlands plateau had a weathered appearance and featured smaller plateaus with more erratic terrain, allowing for significantly fewer oak trees to grow at the highest layers. Eroded badlands replaced the usual thin desert border that this biome variant shared with other biomes.

Modified wooded badlands plateaus used the same mob spawning chances as badlands.


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

### Birch forest
#### Birch Forest Hills
| Blocks        | Grass BlockBirch LogBirch LeavesBee NestRose BushLilacPeonyLily of the Valley |
|---------------|-------------------------------------------------------------------------------|
| Temperature   | 0.6                                                                           |
| Grass color   | #88BB67                                                                       |
| Foliage color | #6BA941                                                                       |
| Water color   | #3F76E4‌[JE  only] #0A74C4‌[BE  only]                                         |

{
    "title": "Birch Forest Hills",
    "rows": [
        {
            "field": "(values exceeds 1000 characters...)",
            "label": "Blocks"
        },
        {
            "field": "0.6",
            "label": "(link to Biome#Temperature article, displayed as Temperature)"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #88BB67; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #88BB67</span>",
            "label": "Grass color"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #6BA941; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #6BA941</span>",
            "label": "Foliage color"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #3F76E4; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #3F76E4</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Java Edition\">(link to Java Edition article, displayed as JE)  only</span></i>]</sup><br><span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #0A74C4; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #0A74C4</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Bedrock Edition\">(link to Bedrock Edition article, displayed as BE)  only</span></i>]</sup>",
            "label": "Water color"
        }
    ],
    "invimages": [],
    "images": [
        "Birch Forest Hills.png"
    ]
}
Birch forest hills featured hillier terrain than regular birch forests, being identical to them in every other aspect. It was fairly common due to its wide spread.

Birch forest hills used the same mob spawning chances as birch forests.


In Java Edition:
| Mob             | Spawn weight      | Group size        |
|-----------------|-------------------|-------------------|
|                 |                   | Creature category |
| Sheep           | $\frac{12}{40}$   | 4                 |
| Pig             | $\frac{10}{40}$   | 4                 |
| Chicken         | $\frac{10}{40}$   | 4                 |
| Cow             | $\frac{8}{40}$    | 4                 |
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

{ "passive": { "mobs": [ { "size": "4", "mob": "Sheep", "weight": 12 }, { "size": "4", "mob": "Pig", "weight": 10 }, { "size": "4", "mob": "Chicken", "weight": 10 }, { "size": "4", "mob": "Cow", "weight": 8 } ], "totalWeight": 40 }, "hostile": { "mobs": [ { "size": "4", "mob": "Spider", "weight": 100 }, { "size": "4", "mob": "Zombie", "weight": 95 }, { "size": "1", "mob": "Zombie Villager", "weight": 5 }, { "size": "4", "mob": "Skeleton", "weight": 100 }, { "size": "4", "mob": "Creeper", "weight": 100 }, { "size": "4", "note": "Spawn attempt succeeds only in slime chunks.", "mob": "Slime", "weight": 100 }, { "size": "1&ndash;4", "mob": "Enderman", "weight": 10 }, { "size": "1", "mob": "Witch", "weight": 5 } ], "totalWeight": 515 }, "ambient": { "mobs": [ { "size": "8", "mob": "Bat", "weight": 10 } ], "totalWeight": 10 } }
In Bedrock Edition:
| Mob             | Spawn weight           | Group size        |
|-----------------|------------------------|-------------------|
|                 |                        | Creature category |
| Sheep           | $\frac{12}{40}$        | 2–3               |
| Pig             | $\frac{10}{40}$        | 1–3               |
| Chicken         | $\frac{10}{40}$        | 2–4               |
| Cow             | $\frac{8}{40}$         | 2–3               |
|                 |                        | Monster category  |
| Spider          | $\frac{99}{493.25}$    | 1                 |
| Zombie          | $\frac{94.25}{493.25}$ | 2–4               |
| Zombie Villager | $\frac{5}{493.25}$     | 2–4               |
| Skeleton        | $\frac{80}{493.25}$    | 1–2               |
| Creeper         | $\frac{100}{493.25}$   | 1                 |
| Slime[note 1]   | $\frac{100}{493.25}$   | 1                 |
| Enderman        | $\frac{10}{493.25}$    | 1–2               |
| Witch           | $\frac{5}{493.25}$     | 1                 |
|                 |                        | Ambient category  |
| Bat             | 1                      | 2                 |

1. ↑Spawn attempt succeeds only in slime chunks.

{ "passive": { "mobs": [ { "size": "2&ndash;3", "mob": "Sheep", "weight": 12 }, { "size": "1&ndash;3", "mob": "Pig", "weight": 10 }, { "size": "2&ndash;4", "mob": "Chicken", "weight": 10 }, { "size": "2&ndash;3", "mob": "Cow", "weight": 8 } ], "totalWeight": 40 }, "hostile": { "mobs": [ { "size": "1", "mob": "Spider", "weight": 99 }, { "size": "2&ndash;4", "mob": "Zombie", "weight": 94.25 }, { "size": "2&ndash;4", "mob": "Zombie Villager", "weight": 5 }, { "size": "1&ndash;2", "mob": "Skeleton", "weight": 80 }, { "size": "1", "mob": "Creeper", "weight": 100 }, { "size": "1", "note": "Spawn attempt succeeds only in slime chunks.", "mob": "Slime", "weight": 100 }, { "size": "1&ndash;2", "mob": "Enderman", "weight": 10 }, { "size": "1", "mob": "Witch", "weight": 5 } ], "totalWeight": 493.25 }, "ambient": { "mobs": [ { "size": "2", "mob": "Bat", "weight": 10 } ], "totalWeight": 10 } }

#### Tall Birch Hills
| Blocks        | Grass BlockBirch LogBirch LeavesBee NestRose BushLilacPeonyLily of the Valley |
|---------------|-------------------------------------------------------------------------------|
| Temperature   | 0.6‌[JE  only]0.7‌[BE  only]                                                  |
| Grass color   | #88BB67‌[JE  only] #79C05A‌[BE  only]                                         |
| Foliage color | #6BA941‌[JE  only] #59AE30‌[BE  only]                                         |
| Water color   | #3F76E4‌[JE  only] #0A74C4‌[BE  only]                                         |

{
    "title": "Tall Birch Hills",
    "rows": [
        {
            "field": "(values exceeds 1000 characters...)",
            "label": "Blocks"
        },
        {
            "field": "0.6‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Java Edition\">(link to Java Edition article, displayed as JE)  only</span></i>]</sup><br>0.7‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Bedrock Edition\">(link to Bedrock Edition article, displayed as BE)  only</span></i>]</sup>",
            "label": "(link to Biome#Temperature article, displayed as Temperature)"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #88BB67; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #88BB67</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Java Edition\">(link to Java Edition article, displayed as JE)  only</span></i>]</sup><br><span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #79C05A; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #79C05A</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Bedrock Edition\">(link to Bedrock Edition article, displayed as BE)  only</span></i>]</sup>",
            "label": "Grass color"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #6BA941; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #6BA941</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Java Edition\">(link to Java Edition article, displayed as JE)  only</span></i>]</sup><br><span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #59AE30; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #59AE30</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Bedrock Edition\">(link to Bedrock Edition article, displayed as BE)  only</span></i>]</sup>",
            "label": "Foliage color"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #3F76E4; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #3F76E4</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Java Edition\">(link to Java Edition article, displayed as JE)  only</span></i>]</sup><br><span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #0A74C4; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #0A74C4</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Bedrock Edition\">(link to Bedrock Edition article, displayed as BE)  only</span></i>]</sup>",
            "label": "Water color"
        }
    ],
    "invimages": [],
    "images": [
        "Tall Birch Hills.png"
    ]
}
Like the other hills biomes, the tall birch hills biome had hillier, rougher terrain, along with the taller-than-normal birch trees of the tall birch forest variant. The hills were steep in this biome, comparable to the windswept hills biome.

Tall birch hills used the same mob spawning chances as birch forests.


In Java Edition:
| Mob             | Spawn weight      | Group size        |
|-----------------|-------------------|-------------------|
|                 |                   | Creature category |
| Sheep           | $\frac{12}{40}$   | 4                 |
| Pig             | $\frac{10}{40}$   | 4                 |
| Chicken         | $\frac{10}{40}$   | 4                 |
| Cow             | $\frac{8}{40}$    | 4                 |
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

{ "passive": { "mobs": [ { "size": "4", "mob": "Sheep", "weight": 12 }, { "size": "4", "mob": "Pig", "weight": 10 }, { "size": "4", "mob": "Chicken", "weight": 10 }, { "size": "4", "mob": "Cow", "weight": 8 } ], "totalWeight": 40 }, "hostile": { "mobs": [ { "size": "4", "mob": "Spider", "weight": 100 }, { "size": "4", "mob": "Zombie", "weight": 95 }, { "size": "1", "mob": "Zombie Villager", "weight": 5 }, { "size": "4", "mob": "Skeleton", "weight": 100 }, { "size": "4", "mob": "Creeper", "weight": 100 }, { "size": "4", "note": "Spawn attempt succeeds only in slime chunks.", "mob": "Slime", "weight": 100 }, { "size": "1&ndash;4", "mob": "Enderman", "weight": 10 }, { "size": "1", "mob": "Witch", "weight": 5 } ], "totalWeight": 515 }, "ambient": { "mobs": [ { "size": "8", "mob": "Bat", "weight": 10 } ], "totalWeight": 10 } }
In Bedrock Edition:
| Mob             | Spawn weight           | Group size        |
|-----------------|------------------------|-------------------|
|                 |                        | Creature category |
| Sheep           | $\frac{12}{40}$        | 2–3               |
| Pig             | $\frac{10}{40}$        | 1–3               |
| Chicken         | $\frac{10}{40}$        | 2–4               |
| Cow             | $\frac{8}{40}$         | 2–3               |
|                 |                        | Monster category  |
| Spider          | $\frac{99}{493.25}$    | 1                 |
| Zombie          | $\frac{94.25}{493.25}$ | 2–4               |
| Zombie Villager | $\frac{5}{493.25}$     | 2–4               |
| Skeleton        | $\frac{80}{493.25}$    | 1–2               |
| Creeper         | $\frac{100}{493.25}$   | 1                 |
| Slime[note 1]   | $\frac{100}{493.25}$   | 1                 |
| Enderman        | $\frac{10}{493.25}$    | 1–2               |
| Witch           | $\frac{5}{493.25}$     | 1                 |
|                 |                        | Ambient category  |
| Bat             | 1                      | 2                 |

1. ↑Spawn attempt succeeds only in slime chunks.

{ "passive": { "mobs": [ { "size": "2&ndash;3", "mob": "Sheep", "weight": 12 }, { "size": "1&ndash;3", "mob": "Pig", "weight": 10 }, { "size": "2&ndash;4", "mob": "Chicken", "weight": 10 }, { "size": "2&ndash;3", "mob": "Cow", "weight": 8 } ], "totalWeight": 40 }, "hostile": { "mobs": [ { "size": "1", "mob": "Spider", "weight": 99 }, { "size": "2&ndash;4", "mob": "Zombie", "weight": 94.25 }, { "size": "2&ndash;4", "mob": "Zombie Villager", "weight": 5 }, { "size": "1&ndash;2", "mob": "Skeleton", "weight": 80 }, { "size": "1", "mob": "Creeper", "weight": 100 }, { "size": "1", "note": "Spawn attempt succeeds only in slime chunks.", "mob": "Slime", "weight": 100 }, { "size": "1&ndash;2", "mob": "Enderman", "weight": 10 }, { "size": "1", "mob": "Witch", "weight": 5 } ], "totalWeight": 493.25 }, "ambient": { "mobs": [ { "size": "2", "mob": "Bat", "weight": 10 } ], "totalWeight": 10 } }

### Dark Forest Hills
| Structures    | Woodland mansions                                                                                                                |
|---------------|----------------------------------------------------------------------------------------------------------------------------------|
| Blocks        | Grass BlockDark Oak LogDark Oak LeavesOak LogOak LeavesBirch LogBirch LeavesMushroom BlocksRose BushPeonyLilacLily of the Valley |
| Temperature   | 0.7                                                                                                                              |
| Grass color   | #507A32                                                                                                                          |
| Foliage color | #59AE30                                                                                                                          |
| Water color   | #3F76E4‌[JE  only] #3B6CD1‌[BE  only]                                                                                            |

{
    "title": "Dark Forest Hills",
    "rows": [
        {
            "field": "<span class=\"nowrap\"><span class=\"sprite-file\" style=\"\">(link to File:EnvSprite woodland-mansion.png article, displayed as 16x16px|link=Woodland mansion|alt=EnvSprite woodland-mansion.png: Sprite image for woodland-mansion in Minecraft linking to Woodland mansion|class=pixel-image|)</span>(link to Woodland mansion article, displayed as <span class=\"sprite-text\">Woodland mansion</span>)</span>s",
            "label": "(link to Structures article, displayed as Structures)"
        },
        {
            "field": "(values exceeds 1000 characters...)",
            "label": "Blocks"
        },
        {
            "field": "0.7",
            "label": "(link to Biome#Temperature article, displayed as Temperature)"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #507A32; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #507A32</span>",
            "label": "Grass color"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #59AE30; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #59AE30</span>",
            "label": "Foliage color"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #3F76E4; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #3F76E4</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Java Edition\">(link to Java Edition article, displayed as JE)  only</span></i>]</sup><br><span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #3B6CD1; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #3B6CD1</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Bedrock Edition\">(link to Bedrock Edition article, displayed as BE)  only</span></i>]</sup>",
            "label": "Water color"
        }
    ],
    "invimages": [],
    "images": [
        "Dark Forest Hills.png"
    ]
}
Dark forest hills broke the leaf canopy, increasing visibility and decreasing the chance of daytime hostile mob spawning, though the hills were steep compared to other hill biomes. Hills generated near rivers led to cliffs. Small plains-biome clearings didn't generate within the dark forest hills variant.

Dark forest hills used the same mob spawning chances as dark forests.


In Java Edition:
| Mob             | Spawn weight      | Group size        |
|-----------------|-------------------|-------------------|
|                 |                   | Creature category |
| Sheep           | $\frac{12}{40}$   | 4                 |
| Pig             | $\frac{10}{40}$   | 4                 |
| Chicken         | $\frac{10}{40}$   | 4                 |
| Cow             | $\frac{8}{40}$    | 4                 |
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

{ "passive": { "mobs": [ { "size": "4", "mob": "Sheep", "weight": 12 }, { "size": "4", "mob": "Pig", "weight": 10 }, { "size": "4", "mob": "Chicken", "weight": 10 }, { "size": "4", "mob": "Cow", "weight": 8 } ], "totalWeight": 40 }, "hostile": { "mobs": [ { "size": "4", "mob": "Spider", "weight": 100 }, { "size": "4", "mob": "Zombie", "weight": 95 }, { "size": "1", "mob": "Zombie Villager", "weight": 5 }, { "size": "4", "mob": "Skeleton", "weight": 100 }, { "size": "4", "mob": "Creeper", "weight": 100 }, { "size": "4", "note": "Spawn attempt succeeds only in slime chunks.", "mob": "Slime", "weight": 100 }, { "size": "1&ndash;4", "mob": "Enderman", "weight": 10 }, { "size": "1", "mob": "Witch", "weight": 5 } ], "totalWeight": 515 }, "ambient": { "mobs": [ { "size": "8", "mob": "Bat", "weight": 10 } ], "totalWeight": 10 } }
In Bedrock Edition:
| Mob             | Spawn weight      | Group size        |
|-----------------|-------------------|-------------------|
|                 |                   | Creature category |
| Sheep           | $\frac{12}{40}$   | 2–3               |
| Pig             | $\frac{10}{40}$   | 1–3               |
| Chicken         | $\frac{10}{40}$   | 2–4               |
| Cow             | $\frac{8}{40}$    | 2–3               |
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

{ "passive": { "mobs": [ { "size": "2&ndash;3", "mob": "Sheep", "weight": 12 }, { "size": "1&ndash;3", "mob": "Pig", "weight": 10 }, { "size": "2&ndash;4", "mob": "Chicken", "weight": 10 }, { "size": "2&ndash;3", "mob": "Cow", "weight": 8 } ], "totalWeight": 40 }, "hostile": { "mobs": [ { "size": "1", "mob": "Spider", "weight": 100 }, { "size": "2&ndash;4", "mob": "Zombie", "weight": 95 }, { "size": "2&ndash;4", "mob": "Zombie Villager", "weight": 5 }, { "size": "1&ndash;2", "mob": "Skeleton", "weight": 80 }, { "size": "1", "mob": "Creeper", "weight": 100 }, { "size": "1", "note": "Spawn attempt succeeds only in slime chunks.", "mob": "Slime", "weight": 100 }, { "size": "1&ndash;2", "mob": "Enderman", "weight": 10 }, { "size": "1", "mob": "Witch", "weight": 5 } ], "totalWeight": 495 }, "ambient": { "mobs": [ { "size": "2", "mob": "Bat", "weight": 10 } ], "totalWeight": 10 } }

### Deep Warm Ocean
| Structures           | Ocean MonumentsShipwrecksUnderwater ruins         |
|----------------------|---------------------------------------------------|
| Blocks               | WaterSandBubble columnMagma BlockObsidianSeagrass |
| Temperature          | 0.5                                               |
| Grass color          | #8EB971                                           |
| Foliage color        | #71A74D                                           |
| Water color          | #43D5EE‌[JE  only] #02B0E5‌[BE  only]             |
| Underwater fog color | #041F33‌[JE  only] #0A74C4‌[BE  only]             |

{
    "title": "Deep Warm Ocean",
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
            "field": "0.5",
            "label": "(link to Biome#Temperature article, displayed as Temperature)"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #8EB971; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #8EB971</span>",
            "label": "Grass color"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #71A74D; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #71A74D</span>",
            "label": "Foliage color"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #43D5EE; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #43D5EE</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Java Edition\">(link to Java Edition article, displayed as JE)  only</span></i>]</sup><br><span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #02B0E5; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #02B0E5</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Bedrock Edition\">(link to Bedrock Edition article, displayed as BE)  only</span></i>]</sup>",
            "label": "Water color"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #041F33; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #041F33</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Java Edition\">(link to Java Edition article, displayed as JE)  only</span></i>]</sup><br><span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #0A74C4; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #0A74C4</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Bedrock Edition\">(link to Bedrock Edition article, displayed as BE)  only</span></i>]</sup>",
            "label": "Underwater fog color"
        }
    ],
    "invimages": [],
    "images": [
        "Deep_Warm_Ocean.png"
    ]
}
The deep warm ocean was similar to the warm ocean, but twice as deep and without coral reefs or sea pickles. Since they were a deep ocean variant, tall seagrass was more frequent and ocean monuments could generate as well. Unlike shallow warm oceans, pufferfish could not spawn in deep warm oceans.

This biome did not naturally generate in any non-snapshot or beta version.


In Java Edition, deep warm oceans used the same mob spawning chances as oceans for hostile and ambient categories, and had different chances for water creature and water ambient categories:
| Mob             | Spawn weight      | Group size              |
|-----------------|-------------------|-------------------------|
|                 |                   | Water creature category |
| Dolphin         | $\frac{2}{7}$     | 1–2                     |
| Squid           | $\frac{5}{7}$     | 1–4                     |
|                 |                   | Ambient category        |
| Bat             | 1                 | 8                       |
|                 |                   | Monster category        |
| Spider          | $\frac{100}{520}$ | 4                       |
| Zombie          | $\frac{95}{520}$  | 4                       |
| Drowned         | $\frac{5}{520}$   | 1                       |
| Zombie Villager | $\frac{5}{520}$   | 1                       |
| Skeleton        | $\frac{100}{520}$ | 4                       |
| Creeper         | $\frac{100}{520}$ | 4                       |
| Slime[note 1]   | $\frac{100}{520}$ | 4                       |
| Enderman        | $\frac{10}{520}$  | 1–4                     |
| Witch           | $\frac{5}{520}$   | 1                       |
|                 |                   | Water ambient category  |
| Tropical Fish   | 1                 | 8                       |

1. ↑Spawn attempt succeeds only in slime chunks.

{ "watercreature": { "mobs": [ { "size": "1&ndash;2", "mob": "Dolphin", "weight": 2 }, { "size": "1&ndash;4", "mob": "Squid", "weight": 5 } ], "totalWeight": 7 }, "ambient": { "mobs": [ { "size": "8", "mob": "Bat", "weight": 10 } ], "totalWeight": 10 }, "hostile": { "mobs": [ { "size": "4", "mob": "Spider", "weight": 100 }, { "size": "4", "mob": "Zombie", "weight": 95 }, { "size": "1", "mob": "Drowned", "weight": 5 }, { "size": "1", "mob": "Zombie Villager", "weight": 5 }, { "size": "4", "mob": "Skeleton", "weight": 100 }, { "size": "4", "mob": "Creeper", "weight": 100 }, { "size": "4", "note": "Spawn attempt succeeds only in slime chunks.", "mob": "Slime", "weight": 100 }, { "size": "1&ndash;4", "mob": "Enderman", "weight": 10 }, { "size": "1", "mob": "Witch", "weight": 5 } ], "totalWeight": 520 }, "waterambient": { "mobs": [ { "size": "8", "mob": "Tropical Fish", "weight": 25 } ], "totalWeight": 25 } }
In Bedrock Edition, deep warm oceans used the same mob spawning chances as warm oceans:
| Mob             | Spawn weight           | Group size        |
|-----------------|------------------------|-------------------|
|                 |                        | Monster category  |
| Spider          | $\frac{99}{593.25}$    | 1                 |
| Zombie          | $\frac{94.25}{593.25}$ | 2–4               |
| Drowned         | $\frac{100}{593.25}$   | 2–4               |
| Zombie Villager | $\frac{5}{593.25}$     | 2–4               |
| Skeleton        | $\frac{80}{593.25}$    | 1–2               |
| Creeper         | $\frac{100}{593.25}$   | 1                 |
| Slime[note 1]   | $\frac{100}{593.25}$   | 1                 |
| Enderman        | $\frac{10}{593.25}$    | 1–2               |
| Witch           | $\frac{5}{593.25}$     | 1                 |
|                 |                        | Creature category |
| Dolphin         | $\frac{7}{15}$         | 3–5               |
| Squid           | $\frac{8}{15}$         | 2–4               |

1. ↑Spawn attempt succeeds only in slime chunks.

{ "hostile": { "mobs": [ { "size": "1", "mob": "Spider", "weight": 99 }, { "size": "2&ndash;4", "mob": "Zombie", "weight": 94.25 }, { "size": "2&ndash;4", "mob": "Drowned", "weight": 100 }, { "size": "2&ndash;4", "mob": "Zombie Villager", "weight": 5 }, { "size": "1&ndash;2", "mob": "Skeleton", "weight": 80 }, { "size": "1", "mob": "Creeper", "weight": 100 }, { "size": "1", "note": "Spawn attempt succeeds only in slime chunks.", "mob": "Slime", "weight": 100 }, { "size": "1&ndash;2", "mob": "Enderman", "weight": 10 }, { "size": "1", "mob": "Witch", "weight": 5 } ], "totalWeight": 593.25 }, "passive": { "mobs": [ { "size": "3&ndash;5", "mob": "Dolphin", "weight": 7 }, { "size": "2&ndash;4", "mob": "Squid", "weight": 8 } ], "totalWeight": 15 } }

### Desert
#### Desert Hills
| Structures    | Desert Pyramids‌[BE  only]            |
|---------------|---------------------------------------|
| Features      | Fossils Desert Wells                  |
| Blocks        | SandSandstoneCactusDead Bush          |
| Temperature   | 2.0                                   |
| Grass color   | #BFB755                               |
| Foliage color | #AEA42A                               |
| Water color   | #3F76E4‌[JE  only] #1A7AA1‌[BE  only] |

{
    "title": "Desert Hills",
    "rows": [
        {
            "field": "<span class=\"nowrap\"><span class=\"sprite-file\" style=\"\">(link to File:EnvSprite desert-pyramid.png article, displayed as 16x16px|link=Desert Pyramid|alt=EnvSprite desert-pyramid.png: Sprite image for desert-pyramid in Minecraft linking to Desert Pyramid|class=pixel-image|)</span>(link to Desert Pyramid article, displayed as <span class=\"sprite-text\">Desert Pyramid</span>)</span>s‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Bedrock Edition\">(link to Bedrock Edition article, displayed as BE)  only</span></i>]</sup>",
            "label": "(link to Structures article, displayed as Structures)"
        },
        {
            "field": "<span class=\"nowrap\"><span class=\"sprite-file\" style=\"\">(link to File:EnvSprite fossil.png article, displayed as 16x16px|link=Fossil|alt=EnvSprite fossil.png: Sprite image for fossil in Minecraft linking to Fossil|class=pixel-image|)</span>(link to Fossil article, displayed as <span class=\"sprite-text\">Fossil</span>)</span>s<br>\n<span class=\"nowrap\"><span class=\"sprite-file\" style=\"\">(link to File:EnvSprite desert-well.png article, displayed as 16x16px|link=Desert well|alt=EnvSprite desert-well.png: Sprite image for desert-well in Minecraft linking to Desert well|class=pixel-image|)</span>(link to Desert well article, displayed as <span class=\"sprite-text\">Desert Well</span>)</span>s<br>",
            "label": "(link to Features article, displayed as Features)"
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
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #BFB755; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #BFB755</span>",
            "label": "Grass color"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #AEA42A; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #AEA42A</span>",
            "label": "Foliage color"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #3F76E4; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #3F76E4</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Java Edition\">(link to Java Edition article, displayed as JE)  only</span></i>]</sup><br><span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #1A7AA1; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #1A7AA1</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Bedrock Edition\">(link to Bedrock Edition article, displayed as BE)  only</span></i>]</sup>",
            "label": "Water color"
        }
    ],
    "invimages": [],
    "images": [
        "Desert Hills.png"
    ]
}
Desert hills variants featured hillier terrain, just like all other hills biomes in the game. Desert hills reached slightly higher elevations than other hills, and were comprised mostly of sand and sandstone like the rest of the desert. No structures[verify] other than fossils, desert pyramids,‌[Bedrock Edition  only] and desert wells generated within the hills, making this variant overall more difficult. Desert hills didn't generate if their base desert is a thin border around a badlands biome.

Desert hills used the same mob spawning chances as deserts.


In Java Edition:
| Mob             | Spawn weight      | Group size        |
|-----------------|-------------------|-------------------|
|                 |                   | Creature category |
| Rabbit[note 1]  | 1                 | 2–3               |
|                 |                   | Monster category  |
| Spider          | $\frac{100}{515}$ | 4                 |
| Skeleton        | $\frac{100}{515}$ | 4                 |
| Creeper         | $\frac{100}{515}$ | 4                 |
| Slime[note 2]   | $\frac{100}{515}$ | 4                 |
| Husk            | $\frac{80}{515}$  | 4                 |
| Zombie          | $\frac{19}{515}$  | 4                 |
| Enderman        | $\frac{10}{515}$  | 1–4               |
| Witch           | $\frac{5}{515}$   | 1                 |
| Zombie Villager | $\frac{1}{515}$   | 1                 |
|                 |                   | Ambient category  |
| Bat             | 1                 | 8                 |

1. ↑All spawned rabbits are gold.
2. ↑Spawn attempt succeeds only in slime chunks.

{ "passive": { "mobs": [ { "size": "2&ndash;3", "note": "All spawned rabbits are gold.", "mob": "Rabbit", "weight": 4 } ], "totalWeight": 4 }, "hostile": { "mobs": [ { "size": "4", "mob": "Spider", "weight": 100 }, { "size": "4", "mob": "Skeleton", "weight": 100 }, { "size": "4", "mob": "Creeper", "weight": 100 }, { "size": "4", "note": "Spawn attempt succeeds only in slime chunks.", "mob": "Slime", "weight": 100 }, { "size": "4", "mob": "Husk", "weight": 80 }, { "size": "4", "mob": "Zombie", "weight": 19 }, { "size": "1&ndash;4", "mob": "Enderman", "weight": 10 }, { "size": "1", "mob": "Witch", "weight": 5 }, { "size": "1", "mob": "Zombie Villager", "weight": 1 } ], "totalWeight": 515 }, "ambient": { "mobs": [ { "size": "8", "mob": "Bat", "weight": 10 } ], "totalWeight": 10 } }
In Bedrock Edition:
| Mob             | Spawn weight      | Group size        |
|-----------------|-------------------|-------------------|
|                 |                   | Monster category  |
| Spider          | $\frac{100}{735}$ | 1                 |
| Zombie          | $\frac{95}{735}$  | 2–4               |
| Zombie Villager | $\frac{5}{735}$   | 2–4               |
| Husk            | $\frac{240}{735}$ | 2–4               |
| Skeleton        | $\frac{80}{735}$  | 1–2               |
| Creeper         | $\frac{100}{735}$ | 1                 |
| Slime[note 1]   | $\frac{100}{735}$ | 1                 |
| Enderman        | $\frac{10}{735}$  | 1–2               |
| Witch           | $\frac{5}{735}$   | 1                 |
|                 |                   | Creature category |
| Rabbit[note 2]  | 1                 | 2–3               |

1. ↑Spawn attempt succeeds only in slime chunks.
2. ↑All spawned rabbits are gold.

{ "hostile": { "mobs": [ { "size": "1", "mob": "Spider", "weight": 100 }, { "size": "2&ndash;4", "mob": "Zombie", "weight": 95 }, { "size": "2&ndash;4", "mob": "Zombie Villager", "weight": 5 }, { "size": "2&ndash;4", "mob": "Husk", "weight": 240 }, { "size": "1&ndash;2", "mob": "Skeleton", "weight": 80 }, { "size": "1", "mob": "Creeper", "weight": 100 }, { "size": "1", "note": "Spawn attempt succeeds only in slime chunks.", "mob": "Slime", "weight": 100 }, { "size": "1&ndash;2", "mob": "Enderman", "weight": 10 }, { "size": "1", "mob": "Witch", "weight": 5 } ], "totalWeight": 735 }, "passive": { "mobs": [ { "size": "2&ndash;3", "note": "All spawned rabbits are gold.", "mob": "Rabbit", "weight": 4 } ], "totalWeight": 4 } }

#### Desert Lakes
| Features      | Fossils Desert Well          |
|---------------|------------------------------|
| Blocks        | SandSandstoneCactusDead Bush |
| Temperature   | 2.0                          |
| Grass color   | #BFB755                      |
| Foliage color | #AEA42A                      |
| Water color   | #3F76E4‌[JE  only]           |

{
    "title": "Desert Lakes",
    "rows": [
        {
            "field": "<span class=\"nowrap\"><span class=\"sprite-file\" style=\"\">(link to File:EnvSprite fossil.png article, displayed as 16x16px|link=Fossil|alt=EnvSprite fossil.png: Sprite image for fossil in Minecraft linking to Fossil|class=pixel-image|)</span>(link to Fossil article, displayed as <span class=\"sprite-text\">Fossil</span>)</span>s<br>\n<span class=\"nowrap\"><span class=\"sprite-file\" style=\"\">(link to File:EnvSprite desert-well.png article, displayed as 16x16px|link=Desert well|alt=EnvSprite desert-well.png: Sprite image for desert-well in Minecraft linking to Desert well|class=pixel-image|)</span>(link to Desert well article, displayed as <span class=\"sprite-text\">Desert Well</span>)</span><br>",
            "label": "(link to Features article, displayed as Features)"
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
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #BFB755; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #BFB755</span>",
            "label": "Grass color"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #AEA42A; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #AEA42A</span>",
            "label": "Foliage color"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #3F76E4; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #3F76E4</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Java Edition\">(link to Java Edition article, displayed as JE)  only</span></i>]</sup>",
            "label": "Water color"
        }
    ],
    "invimages": [],
    "images": [
        "Desert Lakes.png"
    ]
}
The rare desert lakes variant featured slightly rougher and hillier terrain than the base desert biome, though not as much as the desert hills. This made them more likely to have oases of water across its landscape. No structures other than fossils and desert wells generated here.

Desert lakes used the same mob spawning chances as deserts.


In Java Edition:
| Mob             | Spawn weight      | Group size        |
|-----------------|-------------------|-------------------|
|                 |                   | Creature category |
| Rabbit[note 1]  | 1                 | 2–3               |
|                 |                   | Monster category  |
| Spider          | $\frac{100}{515}$ | 4                 |
| Skeleton        | $\frac{100}{515}$ | 4                 |
| Creeper         | $\frac{100}{515}$ | 4                 |
| Slime[note 2]   | $\frac{100}{515}$ | 4                 |
| Husk            | $\frac{80}{515}$  | 4                 |
| Zombie          | $\frac{19}{515}$  | 4                 |
| Enderman        | $\frac{10}{515}$  | 1–4               |
| Witch           | $\frac{5}{515}$   | 1                 |
| Zombie Villager | $\frac{1}{515}$   | 1                 |
|                 |                   | Ambient category  |
| Bat             | 1                 | 8                 |

1. ↑All spawned rabbits are gold.
2. ↑Spawn attempt succeeds only in slime chunks.

{ "passive": { "mobs": [ { "size": "2&ndash;3", "note": "All spawned rabbits are gold.", "mob": "Rabbit", "weight": 4 } ], "totalWeight": 4 }, "hostile": { "mobs": [ { "size": "4", "mob": "Spider", "weight": 100 }, { "size": "4", "mob": "Skeleton", "weight": 100 }, { "size": "4", "mob": "Creeper", "weight": 100 }, { "size": "4", "note": "Spawn attempt succeeds only in slime chunks.", "mob": "Slime", "weight": 100 }, { "size": "4", "mob": "Husk", "weight": 80 }, { "size": "4", "mob": "Zombie", "weight": 19 }, { "size": "1&ndash;4", "mob": "Enderman", "weight": 10 }, { "size": "1", "mob": "Witch", "weight": 5 }, { "size": "1", "mob": "Zombie Villager", "weight": 1 } ], "totalWeight": 515 }, "ambient": { "mobs": [ { "size": "8", "mob": "Bat", "weight": 10 } ], "totalWeight": 10 } }
In Bedrock Edition:
| Mob             | Spawn weight      | Group size        |
|-----------------|-------------------|-------------------|
|                 |                   | Monster category  |
| Spider          | $\frac{100}{735}$ | 1                 |
| Zombie          | $\frac{95}{735}$  | 2–4               |
| Zombie Villager | $\frac{5}{735}$   | 2–4               |
| Husk            | $\frac{240}{735}$ | 2–4               |
| Skeleton        | $\frac{80}{735}$  | 1–2               |
| Creeper         | $\frac{100}{735}$ | 1                 |
| Slime[note 1]   | $\frac{100}{735}$ | 1                 |
| Enderman        | $\frac{10}{735}$  | 1–2               |
| Witch           | $\frac{5}{735}$   | 1                 |
|                 |                   | Creature category |
| Rabbit[note 2]  | 1                 | 2–3               |

1. ↑Spawn attempt succeeds only in slime chunks.
2. ↑All spawned rabbits are gold.

{ "hostile": { "mobs": [ { "size": "1", "mob": "Spider", "weight": 100 }, { "size": "2&ndash;4", "mob": "Zombie", "weight": 95 }, { "size": "2&ndash;4", "mob": "Zombie Villager", "weight": 5 }, { "size": "2&ndash;4", "mob": "Husk", "weight": 240 }, { "size": "1&ndash;2", "mob": "Skeleton", "weight": 80 }, { "size": "1", "mob": "Creeper", "weight": 100 }, { "size": "1", "note": "Spawn attempt succeeds only in slime chunks.", "mob": "Slime", "weight": 100 }, { "size": "1&ndash;2", "mob": "Enderman", "weight": 10 }, { "size": "1", "mob": "Witch", "weight": 5 } ], "totalWeight": 735 }, "passive": { "mobs": [ { "size": "2&ndash;3", "note": "All spawned rabbits are gold.", "mob": "Rabbit", "weight": 4 } ], "totalWeight": 4 } }

### Giant Taiga
#### Giant Spruce Taiga Hills
| Structures    | Forest rocks                                                                                                          |
|---------------|-----------------------------------------------------------------------------------------------------------------------|
| Blocks        | Grass BlockPodzolCoarse DirtMossy CobblestoneSpruce LogSpruce LeavesFernLarge FernDead BushSweet Berry Bush Mushrooms |
| Temperature   | 0.25‌[JE  only]0.3‌[BE  only]                                                                                         |
| Grass color   | #86B783‌[JE  only] #86B87F‌[BE  only]                                                                                 |
| Foliage color | #68A464‌[JE  only] #68A55F‌[BE  only]                                                                                 |
| Water color   | #3F76E4‌[JE  only] #2D6D77‌[BE  only]                                                                                 |

{
    "title": "Giant Spruce Taiga hills",
    "rows": [
        {
            "field": "<span class=\"nowrap\"><span class=\"sprite-file\" style=\"\">(link to File:EnvSprite forest-rock.png article, displayed as 16x16px|link=Forest rock|alt=EnvSprite forest-rock.png: Sprite image for forest-rock in Minecraft linking to Forest rock|class=pixel-image|)</span>(link to Forest rock article, displayed as <span class=\"sprite-text\">Forest rock</span>)</span>s",
            "label": "(link to Structures article, displayed as Structures)"
        },
        {
            "field": "(values exceeds 1000 characters...)",
            "label": "Blocks"
        },
        {
            "field": "0.25‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Java Edition\">(link to Java Edition article, displayed as JE)  only</span></i>]</sup><br>0.3‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Bedrock Edition\">(link to Bedrock Edition article, displayed as BE)  only</span></i>]</sup>",
            "label": "(link to Biome#Temperature article, displayed as Temperature)"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #86B783; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #86B783</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Java Edition\">(link to Java Edition article, displayed as JE)  only</span></i>]</sup><br><span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #86B87F; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #86B87F</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Bedrock Edition\">(link to Bedrock Edition article, displayed as BE)  only</span></i>]</sup>",
            "label": "Grass color"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #68A464; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #68A464</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Java Edition\">(link to Java Edition article, displayed as JE)  only</span></i>]</sup><br><span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #68A55F; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #68A55F</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Bedrock Edition\">(link to Bedrock Edition article, displayed as BE)  only</span></i>]</sup>",
            "label": "Foliage color"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #3F76E4; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #3F76E4</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Java Edition\">(link to Java Edition article, displayed as JE)  only</span></i>]</sup><br><span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #2D6D77; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #2D6D77</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Bedrock Edition\">(link to Bedrock Edition article, displayed as BE)  only</span></i>]</sup>",
            "label": "Water color"
        }
    ],
    "invimages": [],
    "images": [
        "Giant Spruce Taiga Hills.png"
    ]
}
Giant spruce taiga hills were a variant intended to be a more mountainous version of the giant spruce taiga. However, in Java Edition, due to a likely error in the way terrain height is calculated, there was no difference in the terrain between giant spruce taiga and giant spruce taiga hills. Specifically, the game used internal values known as setBaseHeight and setHeightVariation when generating hills biomes, but these values were the same for both giant spruce taiga and giant spruce taiga hills, resulting in no actual difference between the two. This was the only hills biome in the game with this issue.[1]

In Bedrock Edition, this biome generated as a hillier version of the giant spruce taiga, however, this biome generated the same trees as the giant tree taiga hills tree type (not giant spruce tree type) resulting in no actual difference between giant tree taiga hills and giant spruce taiga hills (except in water color).

Giant spruce taiga hills used the same mob spawning chances as giant spruce taigas.


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

1. ↑50% of spawned rabbits are brown, 40% are salt and pepper, and 10% are black.
2. ↑The foxes are red foxes.
3. ↑Spawn attempt succeeds only in slime chunks.

{ "passive": { "mobs": [ { "size": "4", "mob": "Sheep", "weight": 12 }, { "size": "4", "mob": "Pig", "weight": 10 }, { "size": "4", "mob": "Chicken", "weight": 10 }, { "size": "4", "mob": "Cow", "weight": 8 }, { "size": "4", "mob": "Wolf", "weight": 8 }, { "size": "2&ndash;3", "note": "50% of spawned rabbits are brown, 40% are salt and pepper, and 10% are black.", "mob": "Rabbit", "weight": 4 }, { "size": "2&ndash;4", "note": "The foxes are red foxes.", "mob": "Fox", "weight": 8 } ], "totalWeight": 60 }, "hostile": { "mobs": [ { "size": "4", "mob": "Spider", "weight": 100 }, { "size": "4", "mob": "Zombie", "weight": 95 }, { "size": "1", "mob": "Zombie Villager", "weight": 5 }, { "size": "4", "mob": "Skeleton", "weight": 100 }, { "size": "4", "mob": "Creeper", "weight": 100 }, { "size": "4", "note": "Spawn attempt succeeds only in slime chunks.", "mob": "Slime", "weight": 100 }, { "size": "1&ndash;4", "mob": "Enderman", "weight": 10 }, { "size": "1", "mob": "Witch", "weight": 5 } ], "totalWeight": 515 }, "ambient": { "mobs": [ { "size": "8", "mob": "Bat", "weight": 10 } ], "totalWeight": 10 } }
In Bedrock Edition:
| Mob             | Spawn weight      | Group size        |
|-----------------|-------------------|-------------------|
|                 |                   | Creature category |
| Sheep           | $\frac{12}{56}$   | 2–3               |
| Pig             | $\frac{10}{56}$   | 1–3               |
| Chicken         | $\frac{10}{56}$   | 2–4               |
| Cow             | $\frac{8}{56}$    | 2–3               |
| Wolf            | $\frac{8}{56}$    | 4                 |
| Fox[note 1]     | $\frac{8}{56}$    | 2–4               |
|                 |                   | Monster category  |
| Spider          | $\frac{100}{495}$ | 1                 |
| Zombie          | $\frac{95}{495}$  | 2–4               |
| Zombie Villager | $\frac{5}{495}$   | 2–4               |
| Skeleton        | $\frac{80}{495}$  | 1–2               |
| Creeper         | $\frac{100}{495}$ | 1                 |
| Slime[note 2]   | $\frac{100}{495}$ | 1                 |
| Enderman        | $\frac{10}{495}$  | 1–2               |
| Witch           | $\frac{5}{495}$   | 1                 |
|                 |                   | Ambient category  |
| Bat             | 1                 | 2                 |

1. ↑The foxes are red foxes.
2. ↑Spawn attempt succeeds only in slime chunks.

{ "passive": { "mobs": [ { "size": "2&ndash;3", "mob": "Sheep", "weight": 12 }, { "size": "1&ndash;3", "mob": "Pig", "weight": 10 }, { "size": "2&ndash;4", "mob": "Chicken", "weight": 10 }, { "size": "2&ndash;3", "mob": "Cow", "weight": 8 }, { "size": "4", "mob": "Wolf", "weight": 8 }, { "size": "2&ndash;4", "note": "The foxes are red foxes.", "mob": "Fox", "weight": 8 } ], "totalWeight": 56 }, "hostile": { "mobs": [ { "size": "1", "mob": "Spider", "weight": 100 }, { "size": "2&ndash;4", "mob": "Zombie", "weight": 95 }, { "size": "2&ndash;4", "mob": "Zombie Villager", "weight": 5 }, { "size": "1&ndash;2", "mob": "Skeleton", "weight": 80 }, { "size": "1", "mob": "Creeper", "weight": 100 }, { "size": "1", "note": "Spawn attempt succeeds only in slime chunks.", "mob": "Slime", "weight": 100 }, { "size": "1&ndash;2", "mob": "Enderman", "weight": 10 }, { "size": "1", "mob": "Witch", "weight": 5 } ], "totalWeight": 495 }, "ambient": { "mobs": [ { "size": "2", "mob": "Bat", "weight": 10 } ], "totalWeight": 10 } }

#### Giant Tree Taiga Hills
| Structures    | Forest rocks                                                                                                          |
|---------------|-----------------------------------------------------------------------------------------------------------------------|
| Blocks        | Grass BlockPodzolCoarse DirtMossy CobblestoneSpruce LogSpruce LeavesFernLarge FernDead BushSweet Berry Bush Mushrooms |
| Temperature   | 0.3                                                                                                                   |
| Grass color   | #86B87F                                                                                                               |
| Foliage color | #68A55F                                                                                                               |
| Water color   | #3F76E4‌[JE  only] #286378‌[BE  only]                                                                                 |

{
    "title": "Giant Tree Taiga Hills",
    "rows": [
        {
            "field": "<span class=\"nowrap\"><span class=\"sprite-file\" style=\"\">(link to File:EnvSprite forest-rock.png article, displayed as 16x16px|link=Forest rock|alt=EnvSprite forest-rock.png: Sprite image for forest-rock in Minecraft linking to Forest rock|class=pixel-image|)</span>(link to Forest rock article, displayed as <span class=\"sprite-text\">Forest rock</span>)</span>s",
            "label": "(link to Structures article, displayed as Structures)"
        },
        {
            "field": "(values exceeds 1000 characters...)",
            "label": "Blocks"
        },
        {
            "field": "0.3",
            "label": "(link to Biome#Temperature article, displayed as Temperature)"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #86B87F; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #86B87F</span>",
            "label": "Grass color"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #68A55F; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #68A55F</span>",
            "label": "Foliage color"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #3F76E4; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #3F76E4</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Java Edition\">(link to Java Edition article, displayed as JE)  only</span></i>]</sup><br><span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #286378; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #286378</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Bedrock Edition\">(link to Bedrock Edition article, displayed as BE)  only</span></i>]</sup>",
            "label": "Water color"
        }
    ],
    "invimages": [],
    "images": [
        "Giant Tree Taiga Hills.png"
    ]
}
Like all other hills biomes, giant tree taiga hills featured elevated, hillier terrain compared to the normal giant tree taiga, making the landscape less suitable for shelter. Podzol, coarse dirt, and rocks all still generated on the hills. Wolves, foxes and rabbit‌[Java Edition  only] spawned here.

Giant tree taiga hills used the same mob spawning chances as giant tree taigas.


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
| Spider          | $\frac{100}{540}$ | 4                 |
| Zombie          | $\frac{100}{540}$ | 4                 |
| Skeleton        | $\frac{100}{540}$ | 4                 |
| Zombie Villager | $\frac{25}{540}$  | 1                 |
| Creeper         | $\frac{100}{540}$ | 4                 |
| Slime[note 3]   | $\frac{100}{540}$ | 4                 |
| Enderman        | $\frac{10}{540}$  | 1–4               |
| Witch           | $\frac{5}{540}$   | 1                 |
|                 |                   | Ambient category  |
| Bat             | 1                 | 8                 |

1. ↑50% of spawned rabbits are brown, 40% are salt and pepper, and 10% are black.
2. ↑The foxes are red foxes.
3. ↑Spawn attempt succeeds only in slime chunks.

{ "passive": { "mobs": [ { "size": "4", "mob": "Sheep", "weight": 12 }, { "size": "4", "mob": "Pig", "weight": 10 }, { "size": "4", "mob": "Chicken", "weight": 10 }, { "size": "4", "mob": "Cow", "weight": 8 }, { "size": "4", "mob": "Wolf", "weight": 8 }, { "size": "2&ndash;3", "note": "50% of spawned rabbits are brown, 40% are salt and pepper, and 10% are black.", "mob": "Rabbit", "weight": 4 }, { "size": "2&ndash;4", "note": "The foxes are red foxes.", "mob": "Fox", "weight": 8 } ], "totalWeight": 60 }, "hostile": { "mobs": [ { "size": "4", "mob": "Spider", "weight": 100 }, { "size": "4", "mob": "Zombie", "weight": 100 }, { "size": "4", "mob": "Skeleton", "weight": 100 }, { "size": "1", "mob": "Zombie Villager", "weight": 25 }, { "size": "4", "mob": "Creeper", "weight": 100 }, { "size": "4", "note": "Spawn attempt succeeds only in slime chunks.", "mob": "Slime", "weight": 100 }, { "size": "1&ndash;4", "mob": "Enderman", "weight": 10 }, { "size": "1", "mob": "Witch", "weight": 5 } ], "totalWeight": 540 }, "ambient": { "mobs": [ { "size": "8", "mob": "Bat", "weight": 10 } ], "totalWeight": 10 } }
In Bedrock Edition:
| Mob             | Spawn weight      | Group size        |
|-----------------|-------------------|-------------------|
|                 |                   | Creature category |
| Sheep           | $\frac{12}{56}$   | 2–3               |
| Pig             | $\frac{10}{56}$   | 1–3               |
| Chicken         | $\frac{10}{56}$   | 2–4               |
| Cow             | $\frac{8}{56}$    | 2–3               |
| Wolf            | $\frac{8}{56}$    | 4                 |
| Fox[note 1]     | $\frac{8}{56}$    | 2–4               |
|                 |                   | Monster category  |
| Spider          | $\frac{100}{495}$ | 1                 |
| Zombie          | $\frac{95}{495}$  | 2–4               |
| Zombie Villager | $\frac{5}{495}$   | 2–4               |
| Skeleton        | $\frac{80}{495}$  | 1–2               |
| Creeper         | $\frac{100}{495}$ | 1                 |
| Slime[note 2]   | $\frac{100}{495}$ | 1                 |
| Enderman        | $\frac{10}{495}$  | 1–2               |
| Witch           | $\frac{5}{495}$   | 1                 |
|                 |                   | Ambient category  |
| Bat             | 1                 | 2                 |

1. ↑The foxes are red foxes.
2. ↑Spawn attempt succeeds only in slime chunks.

{ "passive": { "mobs": [ { "size": "2&ndash;3", "mob": "Sheep", "weight": 12 }, { "size": "1&ndash;3", "mob": "Pig", "weight": 10 }, { "size": "2&ndash;4", "mob": "Chicken", "weight": 10 }, { "size": "2&ndash;3", "mob": "Cow", "weight": 8 }, { "size": "4", "mob": "Wolf", "weight": 8 }, { "size": "2&ndash;4", "note": "The foxes are red foxes.", "mob": "Fox", "weight": 8 } ], "totalWeight": 56 }, "hostile": { "mobs": [ { "size": "1", "mob": "Spider", "weight": 100 }, { "size": "2&ndash;4", "mob": "Zombie", "weight": 95 }, { "size": "2&ndash;4", "mob": "Zombie Villager", "weight": 5 }, { "size": "1&ndash;2", "mob": "Skeleton", "weight": 80 }, { "size": "1", "mob": "Creeper", "weight": 100 }, { "size": "1", "note": "Spawn attempt succeeds only in slime chunks.", "mob": "Slime", "weight": 100 }, { "size": "1&ndash;2", "mob": "Enderman", "weight": 10 }, { "size": "1", "mob": "Witch", "weight": 5 } ], "totalWeight": 495 }, "ambient": { "mobs": [ { "size": "2", "mob": "Bat", "weight": 10 } ], "totalWeight": 10 } }

### Jungle
#### Bamboo Jungle Hills
| Structures    | Jungle pyramids‌[JE  only] N/A‌[Bedrock Edition and Minecraft Education  only] |
|---------------|--------------------------------------------------------------------------------|
| Blocks        | Grass BlockPodzolBambooVinesJungle LogJungle LeavesOak LogOak LeavesMelon      |
| Temperature   | 0.95                                                                           |
| Grass color   | #59C93C                                                                        |
| Foliage color | #30BB0B                                                                        |
| Water color   | #3F76E4‌[JE  only] #1B9ED8‌[BE  only]                                          |

{
    "title": "Bamboo Jungle Hills",
    "rows": [
        {
            "field": "<span class=\"nowrap\"><span class=\"sprite-file\" style=\"\">(link to File:EnvSprite jungle-pyramid.png article, displayed as 16x16px|link=Jungle pyramid|alt=EnvSprite jungle-pyramid.png: Sprite image for jungle-pyramid in Minecraft linking to Jungle pyramid|class=pixel-image|)</span>(link to Jungle pyramid article, displayed as <span class=\"sprite-text\">Jungle pyramid</span>)</span>s‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Java Edition\">(link to Java Edition article, displayed as JE)  only</span></i>]</sup> N/A‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Bedrock Edition and Minecraft Education\">(link to Bedrock Edition article, displayed as Bedrock Edition) and (link to Minecraft Education article, displayed as Minecraft Education)  only</span></i>]</sup>",
            "label": "(link to Structures article, displayed as Structures)"
        },
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
        "Bamboo Jungle Hills.png"
    ]
}
The bamboo jungle hills variant was similar to the bamboo jungle, though with steeper terrain just like the regular jungle hills variant. Large amounts of bamboo covered the landscape, and patches of podzol replaced most grass blocks. Naturally-generated trees were always large variants, and pandas spawned here, like in the bamboo jungle. Jungle pyramids also spawned here in Java Edition.
In Java Edition, bamboo jungle hills used the same mob spawning chances as jungle hills for hostile and ambient categories, and had different chances for passive categories:
| Mob             | Spawn weight      | Group size        |
|-----------------|-------------------|-------------------|
|                 |                   | Creature category |
| Sheep           | $\frac{12}{130}$  | 4                 |
| Pig             | $\frac{10}{130}$  | 4                 |
| Chicken         | $\frac{10}{130}$  | 4                 |
| Cow             | $\frac{8}{130}$   | 4                 |
| Parrot          | $\frac{10}{130}$  | 1                 |
| Panda           | $\frac{80}{130}$  | 1–2               |
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

{ "passive": { "mobs": [ { "size": "4", "mob": "Sheep", "weight": 12 }, { "size": "4", "mob": "Pig", "weight": 10 }, { "size": "4", "mob": "Chicken", "weight": 10 }, { "size": "4", "mob": "Cow", "weight": 8 }, { "size": "1", "mob": "Parrot", "weight": 10 }, { "size": "1&ndash;2", "mob": "Panda", "weight": 80 } ], "totalWeight": 130 }, "hostile": { "mobs": [ { "size": "1", "mob": "Spider", "weight": 100 }, { "size": "2&ndash;4", "mob": "Zombie", "weight": 95 }, { "size": "2&ndash;4", "mob": "Zombie Villager", "weight": 5 }, { "size": "1&ndash;2", "mob": "Skeleton", "weight": 80 }, { "size": "1", "mob": "Creeper", "weight": 100 }, { "size": "1", "note": "Spawn attempt succeeds only in slime chunks.", "mob": "Slime", "weight": 100 }, { "size": "1&ndash;2", "mob": "Enderman", "weight": 10 }, { "size": "1", "mob": "Witch", "weight": 5 } ], "totalWeight": 495 }, "ambient": { "mobs": [ { "size": "2", "mob": "Bat", "weight": 10 } ], "totalWeight": 10 } }
In Bedrock Edition, bamboo jungle hills used the same mob spawning chances as bamboo jungles:
| Mob             | Spawn weight      | Group size        |
|-----------------|-------------------|-------------------|
|                 |                   | Creature category |
| Sheep           | $\frac{12}{150}$  | 2–3               |
| Pig             | $\frac{10}{150}$  | 1–3               |
| Chicken         | $\frac{10}{150}$  | 2–4               |
| Cow             | $\frac{8}{150}$   | 2–3               |
| Parrot          | $\frac{40}{150}$  | 1–2               |
| Panda           | $\frac{40}{150}$  | 1–2               |
| Ocelot          | $\frac{30}{150}$  | 1–2               |
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

{ "passive": { "mobs": [ { "size": "2&ndash;3", "mob": "Sheep", "weight": 12 }, { "size": "1&ndash;3", "mob": "Pig", "weight": 10 }, { "size": "2&ndash;4", "mob": "Chicken", "weight": 10 }, { "size": "2&ndash;3", "mob": "Cow", "weight": 8 }, { "size": "1&ndash;2", "mob": "Parrot", "weight": 40 }, { "size": "1&ndash;2", "mob": "Panda", "weight": 40 }, { "size": "1&ndash;2", "mob": "Ocelot", "weight": 30 } ], "totalWeight": 150 }, "hostile": { "mobs": [ { "size": "1", "mob": "Spider", "weight": 100 }, { "size": "2&ndash;4", "mob": "Zombie", "weight": 95 }, { "size": "2&ndash;4", "mob": "Zombie Villager", "weight": 5 }, { "size": "1&ndash;2", "mob": "Skeleton", "weight": 80 }, { "size": "1", "mob": "Creeper", "weight": 100 }, { "size": "1", "note": "Spawn attempt succeeds only in slime chunks.", "mob": "Slime", "weight": 100 }, { "size": "1&ndash;2", "mob": "Enderman", "weight": 10 }, { "size": "1", "mob": "Witch", "weight": 5 } ], "totalWeight": 495 }, "ambient": { "mobs": [ { "size": "2", "mob": "Bat", "weight": 10 } ], "totalWeight": 10 } }

#### Jungle Hills
| Structures    | Jungle pyramids                                                          |
|---------------|--------------------------------------------------------------------------|
| Blocks        | Grass BlockVinesJungle LogJungle LeavesCocoaOak LogOak LeavesMelonBamboo |
| Temperature   | 0.95                                                                     |
| Grass color   | #59C93C                                                                  |
| Foliage color | #30BB0B                                                                  |
| Water color   | #3F76E4‌[JE  only] #1B9ED8‌[BE  only]                                    |

{
    "title": "Jungle Hills",
    "rows": [
        {
            "field": "<span class=\"nowrap\"><span class=\"sprite-file\" style=\"\">(link to File:EnvSprite jungle-pyramid.png article, displayed as 16x16px|link=Jungle pyramid|alt=EnvSprite jungle-pyramid.png: Sprite image for jungle-pyramid in Minecraft linking to Jungle pyramid|class=pixel-image|)</span>(link to Jungle pyramid article, displayed as <span class=\"sprite-text\">Jungle pyramid</span>)</span>s",
            "label": "(link to Structures article, displayed as Structures)"
        },
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
        "Jungle Hills.png"
    ]
}
Similar to the wooded hills biome, the jungle hills biome featured steeper terrain, making it a more difficult variant of the already difficult jungle for survival purposes. Ocelots, parrots, and pandas spawned here and jungle pyramids generated here.
In Java Edition, jungle hills used the same mob spawning chances as jungles for ambient categories, and had different chances for the others:
| Mob             | Spawn weight      | Group size        |
|-----------------|-------------------|-------------------|
|                 |                   | Creature category |
| Sheep           | $\frac{12}{63}$   | 4                 |
| Pig             | $\frac{10}{63}$   | 4                 |
| Chicken         | $\frac{10}{63}$   | 4                 |
| Cow             | $\frac{8}{63}$    | 4                 |
| Parrot          | $\frac{10}{63}$   | 1                 |
| Panda           | $\frac{1}{63}$    | 1–2               |
| Chicken         | $\frac{10}{63}$   | 4                 |
| Ocelot          | $\frac{2}{63}$    | 1–1               |
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

{ "passive": { "mobs": [ { "size": "4", "mob": "Sheep", "weight": 12 }, { "size": "4", "mob": "Pig", "weight": 10 }, { "size": "4", "mob": "Chicken", "weight": 10 }, { "size": "4", "mob": "Cow", "weight": 8 }, { "size": "1", "mob": "Parrot", "weight": 10 }, { "size": "1&ndash;2", "mob": "Panda", "weight": 1 }, { "size": "4", "mob": "Chicken", "weight": 10 }, { "size": "1&ndash;1", "mob": "Ocelot", "weight": 2 } ], "totalWeight": 63 }, "hostile": { "mobs": [ { "size": "4", "mob": "Spider", "weight": 100 }, { "size": "4", "mob": "Zombie", "weight": 95 }, { "size": "1", "mob": "Zombie Villager", "weight": 5 }, { "size": "4", "mob": "Skeleton", "weight": 100 }, { "size": "4", "mob": "Creeper", "weight": 100 }, { "size": "4", "note": "Spawn attempt succeeds only in slime chunks.", "mob": "Slime", "weight": 100 }, { "size": "1&ndash;4", "mob": "Enderman", "weight": 10 }, { "size": "1", "mob": "Witch", "weight": 5 } ], "totalWeight": 515 }, "ambient": { "mobs": [ { "size": "8", "mob": "Bat", "weight": 10 } ], "totalWeight": 10 } }
In Bedrock Edition, jungle hills used the same mob spawning chances as jungles:
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

### Mountains
#### 
| Blocks        | GravelGrass BlockSnowStoneEmerald OreCoal OreIron OreInfested Stone |
|---------------|---------------------------------------------------------------------|
| Temperature   | 0.2                                                                 |
| Grass color   | #8AB689                                                             |
| Foliage color | #6DA36B                                                             |
| Water color   | #3F76E4‌[JE  only] #0E63AB‌[BE  only]                               |

{
    "title": "Gravelly Mountains+",
    "rows": [
        {
            "field": "(values exceeds 1000 characters...)",
            "label": "Blocks"
        },
        {
            "field": "0.2",
            "label": "(link to Biome#Temperature article, displayed as Temperature)"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #8AB689; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #8AB689</span>",
            "label": "Grass color"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #6DA36B; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #6DA36B</span>",
            "label": "Foliage color"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #3F76E4; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #3F76E4</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Java Edition\">(link to Java Edition article, displayed as JE)  only</span></i>]</sup><br><span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #0E63AB; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #0E63AB</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Bedrock Edition\">(link to Bedrock Edition article, displayed as BE)  only</span></i>]</sup>",
            "label": "Water color"
        }
    ],
    "invimages": [],
    "images": [
        "Gravelly Mountains Plus.png"
    ]
}
Gravelly mountains+, also referred to as modified gravelly mountains in code, was a rare variant of the wooded hill biome that had the exact same features as the regular gravelly mountains, making this biome almost indistinct from the former.[3] with the only difference being the fact that it can rarely generate standalone as a thick separation when a desert lakes biome borders a snowy biome.

Gravelly mountains+ had the same mob spawning chances as windswept hills.


In Java Edition:
| Mob             | Spawn weight      | Group size        |
|-----------------|-------------------|-------------------|
|                 |                   | Creature category |
| Sheep           | $\frac{12}{45}$   | 4                 |
| Pig             | $\frac{10}{45}$   | 4                 |
| Chicken         | $\frac{10}{45}$   | 4                 |
| Cow             | $\frac{8}{45}$    | 4                 |
| Llama           | $\frac{5}{45}$    | 4–6               |
|                 |                   | Monster category  |
| Spider          | $\frac{100}{515}$ | 4                 |
| Zombie          | $\frac{95}{515}$  | 4                 |
| Zombie villager | $\frac{5}{515}$   | 1                 |
| Skeleton        | $\frac{100}{515}$ | 4                 |
| Creeper         | $\frac{100}{515}$ | 4                 |
| Slime[note 1]   | $\frac{100}{515}$ | 4                 |
| Enderman        | $\frac{10}{515}$  | 1–4               |
| Witch           | $\frac{5}{515}$   | 1                 |
|                 |                   | Ambient category  |
| Bat             | 1                 | 8                 |

1. ↑Only on slime chunks

{ "passive": { "mobs": [ { "size": "4", "mob": "Sheep", "weight": 12 }, { "size": "4", "mob": "Pig", "weight": 10 }, { "size": "4", "mob": "Chicken", "weight": 10 }, { "size": "4", "mob": "Cow", "weight": 8 }, { "size": "4&ndash;6", "mob": "Llama", "weight": 5 } ], "totalWeight": 45 }, "hostile": { "mobs": [ { "size": "4", "mob": "Spider", "weight": 100 }, { "size": "4", "mob": "Zombie", "weight": 95 }, { "size": "1", "mob": "Zombie villager", "weight": 5 }, { "size": "4", "mob": "Skeleton", "weight": 100 }, { "size": "4", "mob": "Creeper", "weight": 100 }, { "size": "4", "note": "Only on slime chunks", "mob": "Slime", "weight": 100 }, { "size": "1&ndash;4", "mob": "Enderman", "weight": 10 }, { "size": "1", "mob": "Witch", "weight": 5 } ], "totalWeight": 515 }, "ambient": { "mobs": [ { "size": "8", "mob": "Bat", "weight": 10 } ], "totalWeight": 10 } }
In Bedrock Edition:
| Mob                | Spawn weight      | Group size        |
|--------------------|-------------------|-------------------|
|                    |                   | Creature category |
| Goat               | $\frac{20}{83}$   | 2–3               |
| Sheep              | $\frac{12}{83}$   | 2–3               |
| Pig                | $\frac{10}{83}$   | 1–3               |
| Chicken            | $\frac{10}{83}$   | 2–4               |
| Glow Squid[note 1] | $\frac{10}{83}$   | 2–4               |
| Cow                | $\frac{8}{83}$    | 2–3               |
| Axolotl[note 2]    | $\frac{8}{83}$    | 1–4               |
| Llama              | $\frac{5}{83}$    | 4–6               |
|                    |                   | Monster category  |
| Spider             | $\frac{100}{495}$ | 1                 |
| Zombie             | $\frac{95}{495}$  | 2–4               |
| Zombie villager    | $\frac{5}{495}$   | 2–4               |
| Skeleton           | $\frac{80}{495}$  | 1–2               |
| Creeper            | $\frac{100}{495}$ | 1                 |
| Slime[note 3]      | $\frac{100}{495}$ | 1                 |
| Enderman           | $\frac{10}{495}$  | 1–2               |
| Witch              | $\frac{5}{495}$   | 1                 |
|                    |                   | Ambient category  |
| Bat                | 1                 | 2                 |

1. ↑Only underwater and underground.
2. ↑Only underwater and underground.
3. ↑Only on slime chunks.

{ "passive": { "mobs": [ { "size": "2&ndash;3", "mob": "Goat", "weight": 20 }, { "size": "2&ndash;3", "mob": "Sheep", "weight": 12 }, { "size": "1&ndash;3", "mob": "Pig", "weight": 10 }, { "size": "2&ndash;4", "mob": "Chicken", "weight": 10 }, { "size": "2&ndash;4", "note": "Only underwater and underground.", "mob": "Glow Squid", "weight": 10 }, { "size": "2&ndash;3", "mob": "Cow", "weight": 8 }, { "size": "1&ndash;4", "note": "Only underwater and underground.", "mob": "Axolotl", "weight": 8 }, { "size": "4&ndash;6", "mob": "Llama", "weight": 5 } ], "totalWeight": 83 }, "hostile": { "mobs": [ { "size": "1", "mob": "Spider", "weight": 100 }, { "size": "2&ndash;4", "mob": "Zombie", "weight": 95 }, { "size": "2&ndash;4", "mob": "Zombie villager", "weight": 5 }, { "size": "1&ndash;2", "mob": "Skeleton", "weight": 80 }, { "size": "1", "mob": "Creeper", "weight": 100 }, { "size": "1", "note": "Only on slime chunks.", "mob": "Slime", "weight": 100 }, { "size": "1&ndash;2", "mob": "Enderman", "weight": 10 }, { "size": "1", "mob": "Witch", "weight": 5 } ], "totalWeight": 495 }, "ambient": { "mobs": [ { "size": "2", "mob": "Bat", "weight": 10 } ], "totalWeight": 10 } }

#### Mountain Edge
| Blocks        | Grass BlockOak LogOak LeavesSpruce LogSpruce LeavesSnowStoneEmerald OreCoal OreIron OreInfested Stone |
|---------------|-------------------------------------------------------------------------------------------------------|
| Temperature   | 0.2                                                                                                   |
| Grass color   | #8AB689                                                                                               |
| Foliage color | #6DA36B                                                                                               |
| Water color   | #3F76E4‌[JE  only]                                                                                    |

{
    "title": "Mountain Edge",
    "rows": [
        {
            "field": "(values exceeds 1000 characters...)",
            "label": "Blocks"
        },
        {
            "field": "0.2",
            "label": "(link to Biome#Temperature article, displayed as Temperature)"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #8AB689; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #8AB689</span>",
            "label": "Grass color"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #6DA36B; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #6DA36B</span>",
            "label": "Foliage color"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #3F76E4; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #3F76E4</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Java Edition\">(link to Java Edition article, displayed as JE)  only</span></i>]</sup>",
            "label": "Water color"
        }
    ],
    "invimages": [],
    "images": [
        "Mountain Edge.png"
    ]
}
The mountain edge variant used to generate before Java Edition 1.7.2. Similarly to the sparse jungle biome, it was a technical biome intended to provide a smooth transition from other biomes to the windswept hills. It was nearly identical to the wooded mountain biome, but with gentler slopes.

Mountain edges had the same mob spawning chances as windswept hills.


In Java Edition:
| Mob             | Spawn weight      | Group size        |
|-----------------|-------------------|-------------------|
|                 |                   | Creature category |
| Sheep           | $\frac{12}{45}$   | 4                 |
| Pig             | $\frac{10}{45}$   | 4                 |
| Chicken         | $\frac{10}{45}$   | 4                 |
| Cow             | $\frac{8}{45}$    | 4                 |
| Llama           | $\frac{5}{45}$    | 4–6               |
|                 |                   | Monster category  |
| Spider          | $\frac{100}{515}$ | 4                 |
| Zombie          | $\frac{95}{515}$  | 4                 |
| Zombie villager | $\frac{5}{515}$   | 1                 |
| Skeleton        | $\frac{100}{515}$ | 4                 |
| Creeper         | $\frac{100}{515}$ | 4                 |
| Slime[note 1]   | $\frac{100}{515}$ | 4                 |
| Enderman        | $\frac{10}{515}$  | 1–4               |
| Witch           | $\frac{5}{515}$   | 1                 |
|                 |                   | Ambient category  |
| Bat             | 1                 | 8                 |

1. ↑Only on slime chunks

{ "passive": { "mobs": [ { "size": "4", "mob": "Sheep", "weight": 12 }, { "size": "4", "mob": "Pig", "weight": 10 }, { "size": "4", "mob": "Chicken", "weight": 10 }, { "size": "4", "mob": "Cow", "weight": 8 }, { "size": "4&ndash;6", "mob": "Llama", "weight": 5 } ], "totalWeight": 45 }, "hostile": { "mobs": [ { "size": "4", "mob": "Spider", "weight": 100 }, { "size": "4", "mob": "Zombie", "weight": 95 }, { "size": "1", "mob": "Zombie villager", "weight": 5 }, { "size": "4", "mob": "Skeleton", "weight": 100 }, { "size": "4", "mob": "Creeper", "weight": 100 }, { "size": "4", "note": "Only on slime chunks", "mob": "Slime", "weight": 100 }, { "size": "1&ndash;4", "mob": "Enderman", "weight": 10 }, { "size": "1", "mob": "Witch", "weight": 5 } ], "totalWeight": 515 }, "ambient": { "mobs": [ { "size": "8", "mob": "Bat", "weight": 10 } ], "totalWeight": 10 } }
In Bedrock Edition:
| Mob                | Spawn weight      | Group size        |
|--------------------|-------------------|-------------------|
|                    |                   | Creature category |
| Goat               | $\frac{20}{83}$   | 2–3               |
| Sheep              | $\frac{12}{83}$   | 2–3               |
| Pig                | $\frac{10}{83}$   | 1–3               |
| Chicken            | $\frac{10}{83}$   | 2–4               |
| Glow Squid[note 1] | $\frac{10}{83}$   | 2–4               |
| Cow                | $\frac{8}{83}$    | 2–3               |
| Axolotl[note 2]    | $\frac{8}{83}$    | 1–4               |
| Llama              | $\frac{5}{83}$    | 4–6               |
|                    |                   | Monster category  |
| Spider             | $\frac{100}{495}$ | 1                 |
| Zombie             | $\frac{95}{495}$  | 2–4               |
| Zombie villager    | $\frac{5}{495}$   | 2–4               |
| Skeleton           | $\frac{80}{495}$  | 1–2               |
| Creeper            | $\frac{100}{495}$ | 1                 |
| Slime[note 3]      | $\frac{100}{495}$ | 1                 |
| Enderman           | $\frac{10}{495}$  | 1–2               |
| Witch              | $\frac{5}{495}$   | 1                 |
|                    |                   | Ambient category  |
| Bat                | 1                 | 2                 |

1. ↑Only underwater and underground.
2. ↑Only underwater and underground.
3. ↑Only on slime chunks.

{ "passive": { "mobs": [ { "size": "2&ndash;3", "mob": "Goat", "weight": 20 }, { "size": "2&ndash;3", "mob": "Sheep", "weight": 12 }, { "size": "1&ndash;3", "mob": "Pig", "weight": 10 }, { "size": "2&ndash;4", "mob": "Chicken", "weight": 10 }, { "size": "2&ndash;4", "note": "Only underwater and underground.", "mob": "Glow Squid", "weight": 10 }, { "size": "2&ndash;3", "mob": "Cow", "weight": 8 }, { "size": "1&ndash;4", "note": "Only underwater and underground.", "mob": "Axolotl", "weight": 8 }, { "size": "4&ndash;6", "mob": "Llama", "weight": 5 } ], "totalWeight": 83 }, "hostile": { "mobs": [ { "size": "1", "mob": "Spider", "weight": 100 }, { "size": "2&ndash;4", "mob": "Zombie", "weight": 95 }, { "size": "2&ndash;4", "mob": "Zombie villager", "weight": 5 }, { "size": "1&ndash;2", "mob": "Skeleton", "weight": 80 }, { "size": "1", "mob": "Creeper", "weight": 100 }, { "size": "1", "note": "Only on slime chunks.", "mob": "Slime", "weight": 100 }, { "size": "1&ndash;2", "mob": "Enderman", "weight": 10 }, { "size": "1", "mob": "Witch", "weight": 5 } ], "totalWeight": 495 }, "ambient": { "mobs": [ { "size": "2", "mob": "Bat", "weight": 10 } ], "totalWeight": 10 } }

### Mushroom Field Shore
| Structures    | Huge Mushroom Shipwreck‌[BE  only][4] Buried Treasure‌[BE  only][4] |
|---------------|---------------------------------------------------------------------|
| Blocks        | MyceliumMushroom BlocksMushrooms                                    |
| Temperature   | 0.9                                                                 |
| Grass color   | #55C93F                                                             |
| Foliage color | #2BBB0F                                                             |
| Water color   | #3F76E4‌[JE  only] #818193‌[BE  only]                               |

{
    "title": "Mushroom Field Shore",
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
            "field": "0.9",
            "label": "(link to Biome#Temperature article, displayed as Temperature)"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #55C93F; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #55C93F</span>",
            "label": "Grass color"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #2BBB0F; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #2BBB0F</span>",
            "label": "Foliage color"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #3F76E4; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #3F76E4</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Java Edition\">(link to Java Edition article, displayed as JE)  only</span></i>]</sup><br><span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #818193; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #818193</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Bedrock Edition\">(link to Bedrock Edition article, displayed as BE)  only</span></i>]</sup>",
            "label": "Water color"
        }
    ],
    "invimages": [],
    "images": [
        "Mushroom Field Shore.png"
    ]
}
The mushroom field shore was a technical biome that represented both the shores and the rivers of the mushroom fields. It generated when a river cut through it as well as when it bordered an ocean, unless the ocean was a deep variant, in which case a steep cliff generated instead. The terrain of this biome was much flatter and shallower in elevation, similar to beaches, though it was equal to the mushroom fields in every other way. Buried treasure and shipwrecks generated here.

Mushroom field shores used the same mob spawning chances as mushroom fields.


In Java Edition:
| Mob       | Spawn weight | Group size        |
|-----------|--------------|-------------------|
|           |              | Ambient category  |
| Bat       | 1            | 8                 |
|           |              | Creature category |
| Mooshroom | 1            | 4–8               |

{ "ambient": { "mobs": [ { "size": "8", "mob": "Bat", "weight": 10 } ], "totalWeight": 10 }, "passive": { "mobs": [ { "size": "4&ndash;8", "mob": "Mooshroom", "weight": 8 } ], "totalWeight": 8 } }
In Bedrock Edition:
| Mob       | Spawn weight | Group size        |
|-----------|--------------|-------------------|
|           |              | Creature category |
| Mooshroom | 1            | 4–8               |

{ "passive": { "mobs": [ { "size": "4&ndash;8", "mob": "Mooshroom", "weight": 8 } ], "totalWeight": 8 } }

### Shattered Savanna Plateau
| Blocks        | Grass BlockCoarse DirtStoneTall GrassAcacia LogAcacia Leaves Oak LogOak Leaves |
|---------------|--------------------------------------------------------------------------------|
| Temperature   | 1.0                                                                            |
| Grass color   | #BFB755‌[JE  only] #55C93F‌[BE  only]                                          |
| Foliage color | #AEA42A‌[JE  only] #2BBB0F‌[BE  only]                                          |
| Water color   | #3F76E4‌[JE  only] #2590A8‌[BE  only]                                          |

{
    "title": "Shattered Savanna Plateau",
    "rows": [
        {
            "field": "(values exceeds 1000 characters...)",
            "label": "Blocks"
        },
        {
            "field": "1.0",
            "label": "(link to Biome#Temperature article, displayed as Temperature)"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #BFB755; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #BFB755</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Java Edition\">(link to Java Edition article, displayed as JE)  only</span></i>]</sup><br><span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #55C93F; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #55C93F</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Bedrock Edition\">(link to Bedrock Edition article, displayed as BE)  only</span></i>]</sup>",
            "label": "Grass color"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #AEA42A; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #AEA42A</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Java Edition\">(link to Java Edition article, displayed as JE)  only</span></i>]</sup><br><span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #2BBB0F; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #2BBB0F</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Bedrock Edition\">(link to Bedrock Edition article, displayed as BE)  only</span></i>]</sup>",
            "label": "Foliage color"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #3F76E4; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #3F76E4</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Java Edition\">(link to Java Edition article, displayed as JE)  only</span></i>]</sup><br><span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #2590A8; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #2590A8</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Bedrock Edition\">(link to Bedrock Edition article, displayed as BE)  only</span></i>]</sup>",
            "label": "Water color"
        }
    ],
    "invimages": [],
    "images": [
        "Shattered Savanna Plateau.png"
    ]
}
Like the normal windswept savanna, the shattered savanna plateau variant featured steep mountains, cliffs, and overhangs, which made it a treacherous place to explore. Though it was nearly indistinguishable from the regular shattered savanna at first glance, the shattered plateau's terrain was slightly gentler, though often risked fatal fall damage if not above water. The giant lakes characteristic of the regular shattered savanna did not generate here either. In Bedrock Edition, the foliage was a more vibrant green color, and rain would often occur in it.[5]

Shattered savanna plateaus used the same mob spawning chances as savannas.


In Java Edition:
| Mob             | Spawn weight      | Group size        |
|-----------------|-------------------|-------------------|
|                 |                   | Creature category |
| Sheep           | $\frac{12}{42}$   | 4                 |
| Pig             | $\frac{10}{42}$   | 4                 |
| Chicken         | $\frac{10}{42}$   | 4                 |
| Cow             | $\frac{8}{42}$    | 4                 |
| Horse           | $\frac{1}{42}$    | 2–6               |
| Donkey          | $\frac{1}{42}$    | 1                 |
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

{ "passive": { "mobs": [ { "size": "4", "mob": "Sheep", "weight": 12 }, { "size": "4", "mob": "Pig", "weight": 10 }, { "size": "4", "mob": "Chicken", "weight": 10 }, { "size": "4", "mob": "Cow", "weight": 8 }, { "size": "2&ndash;6", "mob": "Horse", "weight": 1 }, { "size": "1", "mob": "Donkey", "weight": 1 } ], "totalWeight": 42 }, "hostile": { "mobs": [ { "size": "4", "mob": "Spider", "weight": 100 }, { "size": "4", "mob": "Zombie", "weight": 95 }, { "size": "1", "mob": "Zombie Villager", "weight": 5 }, { "size": "4", "mob": "Skeleton", "weight": 100 }, { "size": "4", "mob": "Creeper", "weight": 100 }, { "size": "4", "note": "Spawn attempt succeeds only in slime chunks.", "mob": "Slime", "weight": 100 }, { "size": "1&ndash;4", "mob": "Enderman", "weight": 10 }, { "size": "1", "mob": "Witch", "weight": 5 } ], "totalWeight": 515 }, "ambient": { "mobs": [ { "size": "8", "mob": "Bat", "weight": 10 } ], "totalWeight": 10 } }
In Bedrock Edition:
| Mob             | Spawn weight      | Group size        |
|-----------------|-------------------|-------------------|
|                 |                   | Creature category |
| Sheep           | $\frac{12}{49}$   | 2–3               |
| Pig             | $\frac{10}{49}$   | 1–3               |
| Chicken         | $\frac{10}{49}$   | 2–4               |
| Cow             | $\frac{8}{49}$    | 2–3               |
| Horse           | $\frac{1}{49}$    | 2–6               |
| Llama           | $\frac{8}{49}$    | 4                 |
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

{ "passive": { "mobs": [ { "size": "2&ndash;3", "mob": "Sheep", "weight": 12 }, { "size": "1&ndash;3", "mob": "Pig", "weight": 10 }, { "size": "2&ndash;4", "mob": "Chicken", "weight": 10 }, { "size": "2&ndash;3", "mob": "Cow", "weight": 8 }, { "size": "2&ndash;6", "mob": "Horse", "weight": 1 }, { "size": "4", "mob": "Llama", "weight": 8 } ], "totalWeight": 49 }, "hostile": { "mobs": [ { "size": "1", "mob": "Spider", "weight": 100 }, { "size": "2&ndash;4", "mob": "Zombie", "weight": 95 }, { "size": "2&ndash;4", "mob": "Zombie Villager", "weight": 5 }, { "size": "1&ndash;2", "mob": "Skeleton", "weight": 80 }, { "size": "1", "mob": "Creeper", "weight": 100 }, { "size": "1", "note": "Spawn attempt succeeds only in slime chunks.", "mob": "Slime", "weight": 100 }, { "size": "1&ndash;2", "mob": "Enderman", "weight": 10 }, { "size": "1", "mob": "Witch", "weight": 5 } ], "totalWeight": 495 }, "ambient": { "mobs": [ { "size": "2", "mob": "Bat", "weight": 10 } ], "totalWeight": 10 } }

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

#### Snowy Taiga Mountains
| Blocks        | Grass BlockSnowGrassFernSweet Berry Bush Large FernSpruce LogSpruce Leaves |
|---------------|----------------------------------------------------------------------------|
| Temperature   | -0.5                                                                       |
| Grass color   | #80B497                                                                    |
| Foliage color | #60A17B                                                                    |
| Water color   | #3D57D6‌[JE  only] #205E83‌[BE  only]                                      |

{
    "title": "Snowy Taiga Mountains",
    "rows": [
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
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #3D57D6; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #3D57D6</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Java Edition\">(link to Java Edition article, displayed as JE)  only</span></i>]</sup><br><span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #205E83; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #205E83</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Bedrock Edition\">(link to Bedrock Edition article, displayed as BE)  only</span></i>]</sup>",
            "label": "Water color"
        }
    ],
    "invimages": [],
    "images": [
        "Snowy Taiga Mountains.png"
    ]
}
The very rare snowy taiga mountains featured much steeper terrain than the hills. Similarly to the taiga mountains, this variant reached high elevations. The steep elevations made this biome difficult for survival. Buildings didn't generate here. This biome was the third rarest in the game, behind modified badlands plateau and modified jungle edge.

Snowy taiga mountains used the same mob spawning chances as snowy taigas.


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

### Swamp Hills
| Structures           | FossilsSwamp Huts‌[BE  only] Huge Mushrooms‌[BE  only]                  |
|----------------------|-------------------------------------------------------------------------|
| Blocks               | Grass BlockWaterLily PadClayVinesOak LogOak LeavesBlue Orchid Mushrooms |
| Temperature          | 0.8 (default; varies within swamp)                                      |
| Grass color          | #6A7039 #4C763C (temperature < 0.1)                                     |
| Foliage color        | #6A7039                                                                 |
| Water color          | #617B64‌[JE  only] #4C6156‌[BE  only]                                   |
| Underwater fog color | #232317‌[JE  only] #4C6156‌[BE  only]                                   |

{
    "title": "Swamp Hills",
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
            "field": "0.8 (default; varies within swamp)",
            "label": "(link to Biome#Temperature article, displayed as Temperature)"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #6A7039; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #6A7039</span><br><span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #4C763C; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #4C763C</span> (temperature < 0.1)",
            "label": "Grass color"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #6A7039; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #6A7039</span>",
            "label": "Foliage color"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #617B64; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #617B64</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Java Edition\">(link to Java Edition article, displayed as JE)  only</span></i>]</sup><br><span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #4C6156; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #4C6156</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Bedrock Edition\">(link to Bedrock Edition article, displayed as BE)  only</span></i>]</sup>",
            "label": "Water color"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #232317; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #232317</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Java Edition\">(link to Java Edition article, displayed as JE)  only</span></i>]</sup><br><span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #4C6156; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #4C6156</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Bedrock Edition\">(link to Bedrock Edition article, displayed as BE)  only</span></i>]</sup>",
            "label": "Underwater fog color"
        }
    ],
    "invimages": [],
    "images": [
        "Swamp Hills.png"
    ]
}
The swamp hills variant featured hillier terrain rising up between the flat marshes. These hills would tower over the otherwise low-elevation swamp. Additionally, flooded areas in swamp hills tended to reach lower depths than the rest of the swamp, sometimes deep enough to have a gravel floor in place of a dirt floor, like normal oceans. Swamp huts did not generate in swamp hills‌[Java Edition  only], nor did slimes spawn, but fossils did still generate underground. Additionally, seagrass did not generate in flooded areas of swamp hills. If it connected to a jungle edge it had a chance to create a modified jungle edge biome.

Swamp hills used the same mob spawning chances as regular swamps.


In Java Edition:
| Mob             | Spawn weight      | Group size        |
|-----------------|-------------------|-------------------|
|                 |                   | Creature category |
| Sheep           | $\frac{12}{40}$   | 4                 |
| Pig             | $\frac{10}{40}$   | 4                 |
| Chicken         | $\frac{10}{40}$   | 4                 |
| Cow             | $\frac{8}{40}$    | 4                 |
|                 |                   | Monster category  |
| Spider          | $\frac{100}{516}$ | 4                 |
| Zombie          | $\frac{95}{516}$  | 4                 |
| Zombie Villager | $\frac{5}{516}$   | 1                 |
| Skeleton        | $\frac{100}{516}$ | 4                 |
| Creeper         | $\frac{100}{516}$ | 4                 |
| Slime[note 1]   | $\frac{100}{516}$ | 4                 |
| Enderman        | $\frac{10}{516}$  | 1–4               |
| Witch           | $\frac{5}{516}$   | 1                 |
| Slime[note 1]   | $\frac{1}{516}$   | 1                 |
|                 |                   | Ambient category  |
| Bat             | 1                 | 8                 |

1. ↑ a bSpawning is greatly affected by moon phase

{ "passive": { "mobs": [ { "size": "4", "mob": "Sheep", "weight": 12 }, { "size": "4", "mob": "Pig", "weight": 10 }, { "size": "4", "mob": "Chicken", "weight": 10 }, { "size": "4", "mob": "Cow", "weight": 8 } ], "totalWeight": 40 }, "hostile": { "mobs": [ { "size": "4", "mob": "Spider", "weight": 100 }, { "size": "4", "mob": "Zombie", "weight": 95 }, { "size": "1", "mob": "Zombie Villager", "weight": 5 }, { "size": "4", "mob": "Skeleton", "weight": 100 }, { "size": "4", "mob": "Creeper", "weight": 100 }, { "size": "4", "note": "Spawning is greatly affected by moon phase", "mob": "Slime", "weight": 100 }, { "size": "1&ndash;4", "mob": "Enderman", "weight": 10 }, { "size": "1", "mob": "Witch", "weight": 5 }, { "size": "1", "note": "Spawning is greatly affected by moon phase", "mob": "Slime", "weight": 1 } ], "totalWeight": 516 }, "ambient": { "mobs": [ { "size": "8", "mob": "Bat", "weight": 10 } ], "totalWeight": 10 } }
In Bedrock Edition:
| Mob             | Spawn weight      | Group size        |
|-----------------|-------------------|-------------------|
|                 |                   | Creature category |
| Sheep           | $\frac{12}{40}$   | 2–3               |
| Pig             | $\frac{10}{40}$   | 1–3               |
| Chicken         | $\frac{10}{40}$   | 2–4               |
| Cow             | $\frac{8}{40}$    | 2–3               |
|                 |                   | Monster category  |
| Spider          | $\frac{100}{595}$ | 1                 |
| Zombie          | $\frac{95}{595}$  | 2–4               |
| Zombie Villager | $\frac{5}{595}$   | 2–4               |
| Skeleton        | $\frac{80}{595}$  | 1–2               |
| Creeper         | $\frac{100}{595}$ | 1                 |
| Slime[note 1]   | $\frac{100}{595}$ | 1                 |
| Enderman        | $\frac{10}{595}$  | 1–2               |
| Witch           | $\frac{5}{595}$   | 1                 |
| Slime[note 1]   | $\frac{100}{595}$ | 1                 |
|                 |                   | Ambient category  |
| Bat             | 1                 | 2                 |

1. ↑ a bSpawning is greatly affected by moon phase

{ "passive": { "mobs": [ { "size": "2&ndash;3", "mob": "Sheep", "weight": 12 }, { "size": "1&ndash;3", "mob": "Pig", "weight": 10 }, { "size": "2&ndash;4", "mob": "Chicken", "weight": 10 }, { "size": "2&ndash;3", "mob": "Cow", "weight": 8 } ], "totalWeight": 40 }, "hostile": { "mobs": [ { "size": "1", "mob": "Spider", "weight": 100 }, { "size": "2&ndash;4", "mob": "Zombie", "weight": 95 }, { "size": "2&ndash;4", "mob": "Zombie Villager", "weight": 5 }, { "size": "1&ndash;2", "mob": "Skeleton", "weight": 80 }, { "size": "1", "mob": "Creeper", "weight": 100 }, { "size": "1", "note": "Spawning is greatly affected by moon phase", "mob": "Slime", "weight": 100 }, { "size": "1&ndash;2", "mob": "Enderman", "weight": 10 }, { "size": "1", "mob": "Witch", "weight": 5 }, { "size": "1", "note": "Spawning is greatly affected by moon phase", "mob": "Slime", "weight": 100 } ], "totalWeight": 595 }, "ambient": { "mobs": [ { "size": "2", "mob": "Bat", "weight": 10 } ], "totalWeight": 10 } }

### Taiga
#### Taiga Hills
| Structures    | Villages‌[BE  only] Pillager Outposts‌[BE  only]                      |
|---------------|-----------------------------------------------------------------------|
| Blocks        | Grass BlockGrassFernLarge FernSweet Berry BushSpruce LogSpruce Leaves |
| Temperature   | 0.25                                                                  |
| Grass color   | #86B783                                                               |
| Foliage color | #68A464                                                               |
| Water color   | #3F76E4‌[JE  only] #236583‌[BE  only]                                 |

{
    "title": "Taiga Hills",
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
            "field": "0.25",
            "label": "(link to Biome#Temperature article, displayed as Temperature)"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #86B783; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #86B783</span>",
            "label": "Grass color"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #68A464; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #68A464</span>",
            "label": "Foliage color"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #3F76E4; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #3F76E4</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Java Edition\">(link to Java Edition article, displayed as JE)  only</span></i>]</sup><br><span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #236583; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #236583</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Bedrock Edition\">(link to Bedrock Edition article, displayed as BE)  only</span></i>]</sup>",
            "label": "Water color"
        }
    ],
    "invimages": [],
    "images": [
        "Taiga Hills.png"
    ]
}
Taiga hills, like all other hills biomes in the game, featured steeper terrain compared to the base taiga biome. Villages and outposts didn't generate in this biome‌[Java Edition  only], though wolves and foxes still spawned.

Taiga hills used the same mob spawning chances as taigas.


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

1. ↑50% of spawned rabbits are brown, 40% are salt and pepper, and 10% are black.
2. ↑The foxes spawn as red foxes.
3. ↑Spawn attempt succeeds only in slime chunks.

{ "passive": { "mobs": [ { "size": "4", "mob": "Sheep", "weight": 12 }, { "size": "4", "mob": "Pig", "weight": 10 }, { "size": "4", "mob": "Chicken", "weight": 10 }, { "size": "4", "mob": "Cow", "weight": 8 }, { "size": "4", "mob": "Wolf", "weight": 8 }, { "size": "2&ndash;3", "note": "50% of spawned rabbits are brown, 40% are salt and pepper, and 10% are black.", "mob": "Rabbit", "weight": 4 }, { "size": "2&ndash;4", "note": "The foxes spawn as red foxes.", "mob": "Fox", "weight": 8 } ], "totalWeight": 60 }, "hostile": { "mobs": [ { "size": "4", "mob": "Spider", "weight": 100 }, { "size": "4", "mob": "Zombie", "weight": 95 }, { "size": "1", "mob": "Zombie Villager", "weight": 5 }, { "size": "4", "mob": "Skeleton", "weight": 100 }, { "size": "4", "mob": "Creeper", "weight": 100 }, { "size": "4", "note": "Spawn attempt succeeds only in slime chunks.", "mob": "Slime", "weight": 100 }, { "size": "1&ndash;4", "mob": "Enderman", "weight": 10 }, { "size": "1", "mob": "Witch", "weight": 5 } ], "totalWeight": 515 }, "ambient": { "mobs": [ { "size": "8", "mob": "Bat", "weight": 10 } ], "totalWeight": 10 } }
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

1. ↑50% of spawned rabbits are brown, 40% are salt and pepper, and 10% are black.
2. ↑The foxes spawn as red foxes.
3. ↑Spawn attempt succeeds only in slime chunks.

{ "passive": { "mobs": [ { "size": "2&ndash;3", "mob": "Sheep", "weight": 12 }, { "size": "1&ndash;3", "mob": "Pig", "weight": 10 }, { "size": "2&ndash;4", "mob": "Chicken", "weight": 10 }, { "size": "2&ndash;3", "mob": "Cow", "weight": 8 }, { "size": "4", "mob": "Wolf", "weight": 8 }, { "size": "2&ndash;3", "note": "50% of spawned rabbits are brown, 40% are salt and pepper, and 10% are black.", "mob": "Rabbit", "weight": 4 }, { "size": "2&ndash;4", "note": "The foxes spawn as red foxes.", "mob": "Fox", "weight": 8 } ], "totalWeight": 60 }, "hostile": { "mobs": [ { "size": "1", "mob": "Spider", "weight": 100 }, { "size": "2&ndash;4", "mob": "Zombie", "weight": 95 }, { "size": "2&ndash;4", "mob": "Zombie Villager", "weight": 5 }, { "size": "1&ndash;2", "mob": "Skeleton", "weight": 80 }, { "size": "1", "mob": "Creeper", "weight": 100 }, { "size": "1", "note": "Spawn attempt succeeds only in slime chunks.", "mob": "Slime", "weight": 100 }, { "size": "1&ndash;2", "mob": "Enderman", "weight": 10 }, { "size": "1", "mob": "Witch", "weight": 5 } ], "totalWeight": 495 }, "ambient": { "mobs": [ { "size": "2", "mob": "Bat", "weight": 10 } ], "totalWeight": 10 } }

#### Taiga Mountains
| Blocks        | Grass BlockGrassFernLarge FernSweet Berry BushSpruce LogSpruce Leaves |
|---------------|-----------------------------------------------------------------------|
| Temperature   | 0.25                                                                  |
| Grass color   | #86B783                                                               |
| Foliage color | #68A464                                                               |
| Water color   | #3F76E4‌[JE  only] #1E6B82‌[BE  only]                                 |

{
    "title": "Taiga Mountains",
    "rows": [
        {
            "field": "(values exceeds 1000 characters...)",
            "label": "Blocks"
        },
        {
            "field": "0.25",
            "label": "(link to Biome#Temperature article, displayed as Temperature)"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #86B783; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #86B783</span>",
            "label": "Grass color"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #68A464; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #68A464</span>",
            "label": "Foliage color"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #3F76E4; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #3F76E4</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Java Edition\">(link to Java Edition article, displayed as JE)  only</span></i>]</sup><br><span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #1E6B82; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #1E6B82</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Bedrock Edition\">(link to Bedrock Edition article, displayed as BE)  only</span></i>]</sup>",
            "label": "Water color"
        }
    ],
    "invimages": [],
    "images": [
        "Taiga Mountains.png"
    ]
}
The rare taiga mountains variant was much steeper than the taiga hills, with peaks occasionally crossing the snowfall line. The steep terrain made this a more difficult version of the regular taiga. Like the hills, villages and outposts didn't generate here, though wolves and foxes still spawned.

Taiga mountains used the same mob spawning chances as taigas.


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

1. ↑50% of spawned rabbits are brown, 40% are salt and pepper, and 10% are black.
2. ↑The foxes spawn as red foxes.
3. ↑Spawn attempt succeeds only in slime chunks.

{ "passive": { "mobs": [ { "size": "4", "mob": "Sheep", "weight": 12 }, { "size": "4", "mob": "Pig", "weight": 10 }, { "size": "4", "mob": "Chicken", "weight": 10 }, { "size": "4", "mob": "Cow", "weight": 8 }, { "size": "4", "mob": "Wolf", "weight": 8 }, { "size": "2&ndash;3", "note": "50% of spawned rabbits are brown, 40% are salt and pepper, and 10% are black.", "mob": "Rabbit", "weight": 4 }, { "size": "2&ndash;4", "note": "The foxes spawn as red foxes.", "mob": "Fox", "weight": 8 } ], "totalWeight": 60 }, "hostile": { "mobs": [ { "size": "4", "mob": "Spider", "weight": 100 }, { "size": "4", "mob": "Zombie", "weight": 95 }, { "size": "1", "mob": "Zombie Villager", "weight": 5 }, { "size": "4", "mob": "Skeleton", "weight": 100 }, { "size": "4", "mob": "Creeper", "weight": 100 }, { "size": "4", "note": "Spawn attempt succeeds only in slime chunks.", "mob": "Slime", "weight": 100 }, { "size": "1&ndash;4", "mob": "Enderman", "weight": 10 }, { "size": "1", "mob": "Witch", "weight": 5 } ], "totalWeight": 515 }, "ambient": { "mobs": [ { "size": "8", "mob": "Bat", "weight": 10 } ], "totalWeight": 10 } }
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

1. ↑50% of spawned rabbits are brown, 40% are salt and pepper, and 10% are black.
2. ↑The foxes spawn as red foxes.
3. ↑Spawn attempt succeeds only in slime chunks.

{ "passive": { "mobs": [ { "size": "2&ndash;3", "mob": "Sheep", "weight": 12 }, { "size": "1&ndash;3", "mob": "Pig", "weight": 10 }, { "size": "2&ndash;4", "mob": "Chicken", "weight": 10 }, { "size": "2&ndash;3", "mob": "Cow", "weight": 8 }, { "size": "4", "mob": "Wolf", "weight": 8 }, { "size": "2&ndash;3", "note": "50% of spawned rabbits are brown, 40% are salt and pepper, and 10% are black.", "mob": "Rabbit", "weight": 4 }, { "size": "2&ndash;4", "note": "The foxes spawn as red foxes.", "mob": "Fox", "weight": 8 } ], "totalWeight": 60 }, "hostile": { "mobs": [ { "size": "1", "mob": "Spider", "weight": 100 }, { "size": "2&ndash;4", "mob": "Zombie", "weight": 95 }, { "size": "2&ndash;4", "mob": "Zombie Villager", "weight": 5 }, { "size": "1&ndash;2", "mob": "Skeleton", "weight": 80 }, { "size": "1", "mob": "Creeper", "weight": 100 }, { "size": "1", "note": "Spawn attempt succeeds only in slime chunks.", "mob": "Slime", "weight": 100 }, { "size": "1&ndash;2", "mob": "Enderman", "weight": 10 }, { "size": "1", "mob": "Witch", "weight": 5 } ], "totalWeight": 495 }, "ambient": { "mobs": [ { "size": "2", "mob": "Bat", "weight": 10 } ], "totalWeight": 10 } }

### Wooded Hills
| Blocks        | Grass BlockOak LogOak LeavesBirch LogBirch LeavesBee NestRose BushLilacPeony Lily of the Valley |
|---------------|-------------------------------------------------------------------------------------------------|
| Temperature   | 0.7                                                                                             |
| Grass color   | #79C05A                                                                                         |
| Foliage color | #59AE30                                                                                         |
| Water color   | #3F76E4‌[JE  only] #056BD1‌[BE  only]                                                           |

{
    "title": "Wooded Hills",
    "rows": [
        {
            "field": "(values exceeds 1000 characters...)",
            "label": "Blocks"
        },
        {
            "field": "0.7",
            "label": "(link to Biome#Temperature article, displayed as Temperature)"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #79C05A; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #79C05A</span>",
            "label": "Grass color"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #59AE30; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #59AE30</span>",
            "label": "Foliage color"
        },
        {
            "field": "<span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #3F76E4; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #3F76E4</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Java Edition\">(link to Java Edition article, displayed as JE)  only</span></i>]</sup><br><span style=\"display: inline-block; white-space: nowrap;\"><span style=\"display: inline-block; background-color: #056BD1; border: 1px solid #888; border-radius: 0.3em; width: 1em; height: 1em; vertical-align: -0.4em; margin-right: -0.1em\"><br></span> #056BD1</span>‌<sup class=\"noprint nowrap Inline-Template \" title=\"\">[<i><span title=\"This statement only applies to Bedrock Edition\">(link to Bedrock Edition article, displayed as BE)  only</span></i>]</sup>",
            "label": "Water color"
        }
    ],
    "invimages": [],
    "images": [
        "Wooded Hills.png"
    ]
}
Wooded hills were similar to forests, though the terrain was hillier and generally more erratic, making it less suitable for shelter. Wolves spawned here.

Wooded hills used the same mob spawning chances as forests.


In Java Edition:
| Mob             | Spawn weight      | Group size        |
|-----------------|-------------------|-------------------|
|                 |                   | Creature category |
| Sheep           | $\frac{12}{45}$   | 4                 |
| Pig             | $\frac{10}{45}$   | 4                 |
| Chicken         | $\frac{10}{45}$   | 4                 |
| Cow             | $\frac{8}{45}$    | 4                 |
| Wolf            | $\frac{5}{45}$    | 4                 |
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

{ "passive": { "mobs": [ { "size": "4", "mob": "Sheep", "weight": 12 }, { "size": "4", "mob": "Pig", "weight": 10 }, { "size": "4", "mob": "Chicken", "weight": 10 }, { "size": "4", "mob": "Cow", "weight": 8 }, { "size": "4", "mob": "Wolf", "weight": 5 } ], "totalWeight": 45 }, "hostile": { "mobs": [ { "size": "4", "mob": "Spider", "weight": 100 }, { "size": "4", "mob": "Zombie", "weight": 95 }, { "size": "1", "mob": "Zombie Villager", "weight": 5 }, { "size": "4", "mob": "Skeleton", "weight": 100 }, { "size": "4", "mob": "Creeper", "weight": 100 }, { "size": "4", "note": "Spawn attempt succeeds only in slime chunks.", "mob": "Slime", "weight": 100 }, { "size": "1&ndash;4", "mob": "Enderman", "weight": 10 }, { "size": "1", "mob": "Witch", "weight": 5 } ], "totalWeight": 515 }, "ambient": { "mobs": [ { "size": "8", "mob": "Bat", "weight": 10 } ], "totalWeight": 10 } }
In Bedrock Edition:
| Mob             | Spawn weight      | Group size        |
|-----------------|-------------------|-------------------|
|                 |                   | Creature category |
| Sheep           | $\frac{12}{45}$   | 2–3               |
| Pig             | $\frac{10}{45}$   | 1–3               |
| Chicken         | $\frac{10}{45}$   | 2–4               |
| Cow             | $\frac{8}{45}$    | 2–3               |
| Wolf            | $\frac{5}{45}$    | 4                 |
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

{ "passive": { "mobs": [ { "size": "2&ndash;3", "mob": "Sheep", "weight": 12 }, { "size": "1&ndash;3", "mob": "Pig", "weight": 10 }, { "size": "2&ndash;4", "mob": "Chicken", "weight": 10 }, { "size": "2&ndash;3", "mob": "Cow", "weight": 8 }, { "size": "4", "mob": "Wolf", "weight": 5 } ], "totalWeight": 45 }, "hostile": { "mobs": [ { "size": "1", "mob": "Spider", "weight": 100 }, { "size": "2&ndash;4", "mob": "Zombie", "weight": 95 }, { "size": "2&ndash;4", "mob": "Zombie Villager", "weight": 5 }, { "size": "1&ndash;2", "mob": "Skeleton", "weight": 80 }, { "size": "1", "mob": "Creeper", "weight": 100 }, { "size": "1", "note": "Spawn attempt succeeds only in slime chunks.", "mob": "Slime", "weight": 100 }, { "size": "1&ndash;2", "mob": "Enderman", "weight": 10 }, { "size": "1", "mob": "Witch", "weight": 5 } ], "totalWeight": 495 }, "ambient": { "mobs": [ { "size": "2", "mob": "Bat", "weight": 10 } ], "totalWeight": 10 } }

## Data values
### ID
Java Edition:
| Name                             | Identifier                    | Translation key                               |
|----------------------------------|-------------------------------|-----------------------------------------------|
| Badlands Plateau                 | `badlands_plateau`            | `biome.minecraft.badlands_plateau`            |
| Bamboo Jungle Hills              | `bamboo_jungle_hills`         | `biome.minecraft.bamboo_jungle_hills`         |
| Birch Forest Hills               | `birch_forest_hills`          | `biome.minecraft.birch_forest_hills`          |
| Dark Forest Hills                | `dark_forest_hills`           | `biome.minecraft.dark_forest_hills`           |
| Deep Warm Ocean                  | `deep_warm_ocean`             | `biome.minecraft.deep_warm_ocean`             |
| Desert Hills                     | `desert_hills`                | `biome.minecraft.desert_hills`                |
| Desert Lakes                     | `desert_lakes`                | `biome.minecraft.desert_lakes`                |
| Giant Spruce Taiga Hills         | `giant_spruce_taiga_hills`    | `biome.minecraft.giant_spruce_taiga_hills`    |
| Giant Tree Taiga Hills           | `giant_tree_taiga_hills`      | `biome.minecraft.giant_tree_taiga_hills`      |
| Gravelly Mountains+              | `modified_gravelly_mountains` | `biome.minecraft.modified_gravelly_mountains` |
| Jungle Hills                     | `jungle_hills`                | `biome.minecraft.jungle_hills`                |
| Modified Badlands Plateau        | `modified_badlands_plateau`   | `biome.minecraft.modified_badlands_plateau`   |
| Modified Jungle                  | `modified_jungle`             | `biome.minecraft.modified_jungle`             |
| Modified Jungle Edge             | `modified_jungle_edge`        | `biome.minecraft.modified_jungle_edge`        |
| Modified Wooded Badlands Plateau | `giant_tree_taiga_hills`      | `biome.minecraft.giant_tree_taiga_hills`      |
| Mountain Edge                    | `mountain_edge`               | `biome.minecraft.mountain_edge`               |
| Mushroom Field Shore             | `mushroom_field_shore`        | `biome.minecraft.mushroom_field_shore`        |
| Shattered Savanna Plateau        | `shattered_savanna_plateau`   | `biome.minecraft.shattered_savanna_plateau`   |
| Snowy Mountains                  | `snowy_mountains`             | `biome.minecraft.snowy_mountains`             |
| Snowy Taiga Hills                | `snowy_taiga_hills`           | `biome.minecraft.snowy_taiga_hills`           |
| Snowy Taiga Mountains            | `snowy_taiga_mountains`       | `biome.minecraft.snowy_taiga_mountains`       |
| Swamp Hills                      | `swamp_hills`                 | `biome.minecraft.swamp_hills`                 |
| Taiga Hills                      | `taiga_hills`                 | `biome.minecraft.taiga_hills`                 |
| Taiga Mountains                  | `taiga_mountains`             | `biome.minecraft.taiga_mountains`             |
| Tall Birch Hills                 | `tall_birch_hills`            | `biome.minecraft.tall_birch_hills`            |
| Wooded Hills                     | `wooded_hills`                | `biome.minecraft.wooded_hills`                |

Bedrock Edition:
| Name                | Identifier                         | Translation key                               |
|---------------------|------------------------------------|-----------------------------------------------|
| [No displayed name] | `mesa_plateau`                     | `biome.mesa_plateau.name`                     |
| [No displayed name] | `bamboo_jungle_hills`              | `biome.bamboo_jungle_hills.name`              |
| [No displayed name] | `birch_forest_hills`               | `biome.birch_forest_hills.name`               |
| [No displayed name] | `roofed_forest_mutated`            | `biome.roofed_forest_mutated.name`            |
| [No displayed name] | `deep_warm_ocean`                  | `biome.deep_warm_ocean.name`                  |
| [No displayed name] | `desert_hills`                     | `biome.desert_hills.name`                     |
| [No displayed name] | `desert_mutated`                   | `biome.desert_mutated.name`                   |
| [No displayed name] | `redwood_taiga_hills_mutated`      | `biome.redwood_taiga_hills_mutated.name`      |
| [No displayed name] | `mega_taiga_hills`                 | `biome.mega_taiga_hills.name`                 |
| [No displayed name] | `extreme_hills_plus_trees_mutated` | `biome.extreme_hills_plus_trees_mutated.name` |
| [No displayed name] | `jungle_hills`                     | `biome.jungle_hills.name`                     |
| [No displayed name] | `mesa_plateau_mutated`             | `biome.mesa_plateau_mutated.name`             |
| [No displayed name] | `jungle_mutated`                   | `biome.jungle_mutated.name`                   |
| [No displayed name] | `jungle_edge_mutated`              | `biome.jungle_edge_mutated.name`              |
| [No displayed name] | `mesa_plateau_stone_mutated`       | `biome.mesa_plateau_stone_mutated.name`       |
| [No displayed name] | `extreme_hills_edge`               | `biome.extreme_hills_edge.name`               |
| [No displayed name] | `mushroom_island_shore`            | `biome.mushroom_island_shore.name`            |
| [No displayed name] | `savanna_plateau_mutated`          | `biome.savanna_plateau_mutated.name`          |
| [No displayed name] | `ice_mountains`                    | `biome.ice_mountains.name`                    |
| [No displayed name] | `cold_taiga_hills`                 | `biome.cold_taiga_hills.name`                 |
| [No displayed name] | `cold_taiga_mutated`               | `biome.cold_taiga_mutated.name`               |
| [No displayed name] | `swampland_mutated`                | `biome.swampland_mutated.name`                |
| [No displayed name] | `taiga_hills`                      | `biome.taiga_hills.name`                      |
| [No displayed name] | `taiga_mutated`                    | `biome.taiga_mutated.name`                    |
| [No displayed name] | `birch_forest_hills_mutated`       | `biome.birch_forest_hills_mutated.name`       |
| [No displayed name] | `forest_hills`                     | `biome.forest_hills.name`                     |

