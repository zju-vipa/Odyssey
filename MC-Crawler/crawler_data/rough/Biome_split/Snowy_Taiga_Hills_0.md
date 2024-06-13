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

