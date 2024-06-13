# World generation
World generation (sometimes abbreviated as worldgen) is the procedural generation process Minecraft uses to algorithmically generate terrain, biomes, features, and decides which blocks are placed where. Minecraft worlds are made of 16×16 blocks wide chunks stretching the full height of the dimension. Because there are more than 18 quintillion (18×1018) possible worlds, the game generates them using randomness, algorithms, and some manually built decorations. The benefits of procedural world generation include smaller game file size and practically infinite possibilities of gameplay.

## Contents
- 1 Randomness
- 2 Steps
- 3 Biomes
	- 3.1 Overworld
	- 3.2 The Nether
	- 3.3 The End
- 4 Terrain
	- 4.1 3D noise
	- 4.2 Splines
	- 4.3 Noise caves
	- 4.4 Aquifers
	- 4.5 Ore veins
- 5 Surface
	- 5.1 Overworld
	- 5.2 The Nether
	- 5.3 The End
- 6 Carvers
- 7 Structures
- 8 Features
	- 8.1 Decoration steps
	- 8.2 Generation
- 9 Lighting
- 10 Mob spawning
- 11 Heightmaps
- 12 Video
- 13 History
- 14 External links
- 15 References

## Randomness
In order to generate a different world every time, the game uses random numbers generated from a seed. However pure randomness makes terrain and biomes too chaotic with no continuity.[1]

To solve this problem, the game makes use of gradient noise algorithms, like Perlin noise.[2] This makes sure blocks and chunks fit with its neighbors and gives the world both continuity and randomness. 

Even though noise looks random and continuous, using it to generate terrain still lacks variation like hills and valleys that stand out and have a large height difference. To solve this, multiple noise functions are generated with different frequencies and amplitudes and then added up, which gives a more natural result. These noise functions are called octaves.

- Pure randomness (also known as white noise) is too chaotic.
- Perlin noise makes it random and continuous.
- Multiple octaves are combined to create variation.

## Steps
Chunk colormap in Java Edition, which is a square that visualizes the status of 43×43 chunks.
World generation happens in multiple steps. The game may freeze some chunks that are far from players at an early generation step for better performance, as shown on the graph. As the player approaches these chunks, the chunks advance through the generation steps again until they finish generating. Incomplete chunks that are temporarily frozen at a step are called proto-chunks, while chunks that are ready and accessible to players are called level chunks. In Java Edition, the steps of world generation are sorted into:

- empty: The chunk is not yet loaded or generated.
- structures_starts: This step calculates the starting points for structure pieces. For structures that are the starting in this chunk, the position of all pieces are generated and stored.
- structures_references: A reference to nearby chunks that have a structures' starting point are stored.
- biomes: Biomes are determined and stored. No terrain is generated at this stage.
- noise: The base terrain shape and liquid bodies are placed.
- surface: The surface of the terrain is replaced with biome-dependent blocks.
- carvers: Carvers carve certain parts of the terrain and replace solid blocks with air.
- features: Features and structure pieces are placed and heightmaps are generated.
- initialize_light: The lighting engine is initialized and light sources are identified.
- light: The lighting engine calculates the light level for blocks.
- spawn: Mobs are spawned.
- full: Generation is done and a chunk can now be loaded. The proto-chunk is now converted to a level chunk and allblock updatesdeferred in the above steps are executed.

## Biomes
Top-down maps of biomes and density functions.
In Java Edition, the climate parameters can be found in the debug screen.
For an overview of biomes, see Biome.

### Overworld
Biome generation in the Overworld is based on 6 parameters: temperature, humidity (aka. vegetation), continentalness (aka. continents), erosion, weirdness (aka. ridges), and depth. Except for "depth", the other 5 parameters are based only on horizontal coordinates.

They can be thought of as a six-dimensional (6D) space, where multiple intervals are defined for each biome, as described below. If the 6 parameters at a location fall outside all the defined biome intervals, the game uses the closest biome interval in the 6D space.

Temperature is a noise parameter used only in biome generation and does not affect terrain generation. Temperature values are divided into 5 levels. The corresponding ranges from level 0 to level 4 are: -1.0~-0.45, -0.45~-0.15, -0.15~0.2, 0.2~0.55, 0.55~1.0.

Note that the temperature parameter is not the same as the temperature property of a biome, but they roughly correspond each other, e.g. if a location's temperature parameter is level 0, the base temperature of the biome here is usually low enough or the terrain is high enough, that the surface is covered in snow and ice.

Humidity (also known as vegetation) is a noise parameter used only in biome generation and does not affect terrain generation. Humidity values are also divided into 5 levels. The corresponding ranges from level 0 to level 4 are: -1.0~-0.35, -0.35~-0.1, -0.1~0.1, 0.1~0.3, 0.3~1.0.

Continentalness (also known as continents) is used to decide between ocean/beach/land biomes. Higher values correspond to more inland biomes.

- If -1.2~-1.05: Mushroom fields
- If -1.05~-0.455: Deep ocean
- If -0.455~-0.19: Ocean
- If -0.19~-0.11: Coast
- If -0.11~0.03: Near-inland
- If 0.03~0.3: Mid-inland
- If 0.3~1.0: Far-inland

Erosion is mainly used to decide between flat and mountainous biomes. When erosion is high the landscape is generally flat. Erosion values are divided into 7 levels. The corresponding ranges from level 0 to level 6 are: -1.0~-0.78, -0.78~-0.375, -0.375~-0.2225, -0.2225~0.05, 0.05~0.45, 0.45~0.55, 0.55~1.0.

Weirdness (also known as ridges) affects whether to generate a biome variant or not. If the weirdness value is greater than 0, the generated biome becomes weirder. For example, using the variant of the Jungle biome — Bamboo Jungle. Additionally, weirdness also affects where peaks and valleys generate. Because of this, a biome and its variant often do not appear on the same bank of a river.

A diagram of peaks and valleys (Y-axis) calculated from weirdness (X-axis).
The PV (peaks and valleys, aka. ridges folded) value is calculated through the formula 1−|(3|weirdness|)−2|.

- If -1.0~-0.85: Valleys
- If -0.85~-0.6: Low
- If -0.6~0.2: Mid
- If 0.2~0.7: High
- If 0.7~1.0: Peaks

Depth is a parameter not based directly on noise, instead it corresponds approximately to the terrain height. It is roughly 0 at the surface and increases by 1⁄128 (0.0078125) for every 1 block down. The depth parameter affects whether a surface biome or a cave biome is placed.

The table below lists the defined depth values for Overworld biomes, and any additional noise values required for cave biomes to generate. Any other values result in the closest biome interval being used instead. Note that regions of lush caves and dripstone caves overlap.[3]

| Depth     | Additional requirement  | Biomes          |
|-----------|-------------------------|-----------------|
| D=0.0     | N/A                     | Surface biomes  |
| D=0.2~0.9 | Continentalness=0.8~1.0 | Dripstone Caves |
| D=0.2~0.9 | Humidity=0.7~1.0        | Lush Caves      |
| D=1.0     | N/A                     | Surface biomes  |
| D=1.1     | Erosion=-1.0~-0.375     | Deep Dark       |

The generation of non-inland biomes is not based on humidity, erosion and weirdness. The following table lists the relation between non-inland surface biomes and continentalness and temperature. 

| Temperature | Oceans         | Deep oceans         | Mushroom fields |
|-------------|----------------|---------------------|-----------------|
| T=0         | Frozen Ocean   | Deep Frozen Ocean   | Mushroom Fields |
| T=1         | Cold Ocean     | Deep Cold Ocean     |                 |
| T=2         | Ocean          | Deep Ocean          |                 |
| T=3         | Lukewarm Ocean | Deep Lukewarm Ocean |                 |
| T=4         |                | Warm Ocean          |                 |

The following table lists the relation between inland surface biomes and continentalness, erosion and PV.

| PV      | Erosion | Coast                                                                                                 | Near-inland                                                                                            | Mid-inland                                                                                        | Far-inland                                                                                             |
|---------|---------|-------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| Valleys | E=0~1   | Frozen River（T=0）<br/>River（T>0)                                                                      | Frozen River（T=0）<br/>River（T>0）                                                                       |                                                                                                   | Middle biomes（T<4）<br/>Badland biomes（T=4）                                                             |
|         | E=2~5   |                                                                                                       |                                                                                                        |                                                                                                   | Frozen River（T=0）<br/>River（T>0）                                                                       |
|         | E=6     |                                                                                                       |                                                                                                        |                                                                                                   | Frozen River（T=0）<br/>Swamp（T=1,2）<br/>Mangrove Swamp（T=3,4）                                           |
| Low     | E=0~1   | Stony Shore                                                                                           | Middle biomes（T<4）<br/>Badland biomes（T=4）                                                             |                                                                                                   | Snowy Slopes（T=0; H=0,1）<br/>Grove（T=0; H=2,3,4）<br/>Middle biomes（0<T<4）<br/>Badland biomes（T=4）      |
|         | E=2     |                                                                                                       | Middle biomes                                                                                          |                                                                                                   | Middle biomes（T<4）<br/>Badland biomes（T=4）                                                             |
|         | E=3     | Beach biomes                                                                                          |                                                                                                        |                                                                                                   |                                                                                                        |
|         | E=4     |                                                                                                       |                                                                                                        |                                                                                                   | Middle biomes                                                                                          |
|         | E=5     | Beach biomes（W<0）<br/>Middle biomes（W>0; T=0,1 OR H=4）<br/>Windswept Savanna（W>0; T=2,3,4; H=0,1,2,3） | Middle biomes（W<0 OR T=0,1 OR H=4）<br/>Windswept Savanna（W>0; T=2,3,4; H=0,1,2,3）                      |                                                                                                   |                                                                                                        |
|         | E=6     | Beach biomes                                                                                          |                                                                                                        |                                                                                                   | Middle biomes（T=0）<br/>Swamp（T=1,2）<br/>Mangrove Swamp（T=3,4）                                          |
| Mid     | E=0     | Stony Shore                                                                                           |                                                                                                        |                                                                                                   | Snowy Slopes（T<3; H=0,1）<br/>Grove（T<3; H=2,3,4）<br/>Plateau biomes（T=3,4）                             |
|         | E=1     |                                                                                                       |                                                                                                        | Snowy Slopes（T=0; H=0,1）<br/>Grove（T=0; H=2,3,4）<br/>Middle biomes（0<T<4）<br/>Badland biomes（T=4） | Snowy Slopes（T=0; H=0,1）<br/>Grove（T=0; H=2,3,4）<br/>Plateau biomes（T>0）                               |
|         | E=2     |                                                                                                       | Middle biomes                                                                                          | Middle biomes（T<4）<br/>Badland biomes（T=4）                                                        | Plateau biomes                                                                                         |
|         | E=3     | Middle biomes                                                                                         |                                                                                                        |                                                                                                   | Middle biomes（T<4）<br/>Badland biomes（T=4）                                                             |
|         | E=4     | Beach biomes（W<0）<br/>Middle biomes（W>0）                                                              |                                                                                                        |                                                                                                   | Middle biomes                                                                                          |
|         | E=5     | Beach biomes（W<0）<br/>Middle biomes（W>0; T=0,1 OR H=4）<br/>Windswept Savanna（W>0; T=2,3,4; H=0,1,2,3） | Middle biomes（W<0 OR T=0,1 OR H=4）<br/>Windswept Savanna（W>0; T=2,3,4; H=0,1,2,3）                      |                                                                                                   | Shattered biomes                                                                                       |
|         | E=6     | Beach biomes（W<0）<br/>Middle biomes（W>0）                                                              |                                                                                                        |                                                                                                   | Middle biomes（T=0）<br/>Swamp（T=1,2）<br/>Mangrove Swamp（T=3,4）                                          |
| High    | E=0     | Middle biomes                                                                                         | Snowy Slopes（T<3; H=0,1）<br/>Grove（T<3; H=2,3,4）<br/>Plateau biomes（T=3,4）                             |                                                                                                   | Jagged Peaks（T=0,1,2; W<0）<br/>Frozen Peaks（T=0,1,2; W>0）<br/>Stony Peaks（T=3）<br/>Badland biomes（T=4） |
|         | E=1     |                                                                                                       | Snowy Slopes（T=0; H=0,1）<br/>Grove（T=0; H=2,3,4）<br/>Middle biomes（0<T<4）<br/>Badland biomes（T=4）      |                                                                                                   | Snowy Slopes（T<3; H=0,1）<br/>Grove（T<3; H=2,3,4）<br/>Plateau biomes（T=3,4）                             |
|         | E=2     |                                                                                                       | Middle biomes                                                                                          | Plateau biomes                                                                                    | Plateau biomes                                                                                         |
|         | E=3     |                                                                                                       |                                                                                                        | Middle biomes（T<4）<br/>Badland biomes（T=4）                                                        |                                                                                                        |
|         | E=4     |                                                                                                       |                                                                                                        |                                                                                                   | Middle biomes                                                                                          |
|         | E=5     |                                                                                                       | Middle biomes（W<0 OR T=0,1 OR H=4）<br/>Windswept Savanna（W>0; T=2,3,4; H=0,1,2,3）                      |                                                                                                   | Shattered biomes                                                                                       |
|         | E=6     |                                                                                                       |                                                                                                        |                                                                                                   | Middle biomes                                                                                          |
| Peaks   | E=0     |                                                                                                       | Jagged Peaks（T=0,1,2; W<0）<br/>Frozen Peaks（T=0,1,2; W>0）<br/>Stony Peaks（T=3）<br/>Badland biomes（T=4） |                                                                                                   | Jagged Peaks（T=0,1,2; W<0）<br/>Frozen Peaks（T=0,1,2; W>0）<br/>Stony Peaks（T=3）<br/>Badland biomes（T=4） |
|         | E=1     |                                                                                                       | Snowy Slopes（T=0; H=0,1）<br/>Grove（T=0; H=2,3,4）<br/>Middle biomes（0<T<4）<br/>Badland biomes（T=4）      |                                                                                                   |                                                                                                        |
|         | E=2     |                                                                                                       | Middle biomes                                                                                          | Plateau biomes                                                                                    | Plateau biomes                                                                                         |
|         | E=3     |                                                                                                       |                                                                                                        | Middle biomes（T<4）<br/>Badland biomes（T=4）                                                        |                                                                                                        |
|         | E=4     |                                                                                                       |                                                                                                        |                                                                                                   | Middle biomes                                                                                          |
|         | E=5     |                                                                                                       | Shattered biomes（W<0 OR T=0,1 OR H=4）<br/>Windswept Savanna（W>0; T=2,3,4; H=0,1,2,3）                   |                                                                                                   | Shattered biomes                                                                                       |
|         | E=6     |                                                                                                       |                                                                                                        |                                                                                                   | Middle biomes                                                                                          |

In which, the specific biome generation of beach biomes, badland biomes, middle biomes, plateau biomes, and shattered biomes is determined by the temperature, humidity, and weirdness values.

Beach biomes generate in low lying terrain along the coast, and the specific biome generation is related only to the temperature value.

| Temperature | Biomes      |
|-------------|-------------|
| T=0         | Snowy Beach |
| T=1,2,3     | Beach       |
| T=4         | Desert      |

Badland biomes usually generate inland with low erosion value, and can also generate along the coast with high terrain and low erosion. The specific biome generation is related to humidity and weirdness.

| Humidity | Biomes                                 |
|----------|----------------------------------------|
| H=0,1    | Badlands（W<0）<br/>Eroded Badlands（W>0） |
| H=2      | Badlands                               |
| H=3,4    | Wooded Badlands                        |

Middle biomes are the most extensive biomes inland. The specific biome generation depends on temperature, humidity, and weirdness.

| TemperatureHumidity | T=0                                    | T=1                                                         | T=2                                                | T=3                                | T=4    |
|---------------------|----------------------------------------|-------------------------------------------------------------|----------------------------------------------------|------------------------------------|--------|
| H=0                 | Snowy Plains（W<0）<br/>Ice Spikes（W>0）  | Plains                                                      | Flower Forest（W<0）<br/>Sunflower Plains（W>0）       | Savanna                            | Desert |
| H=1                 | Snowy Plains                           |                                                             | Plains                                             |                                    |        |
| H=2                 | Snowy Plains（W<0）<br/>Snowy Taiga（W>0） |                                                             | Forest                                             | Forest（W<0）<br/>Plains（W>0）        |        |
| H=3                 | Snowy Taiga                            | Taiga                                                       | Birch Forest（W<0）<br/>Old Growth Birch Forest（W>0） | Jungle（W<0）<br/>Sparse Jungle（W>0） |        |
| H=4                 | Taiga                                  | Old Growth Spruce Taiga（W<0）<br/>Old Growth Pine Taiga（W>0） | Dark Forest                                        | Jungle（W<0）<br/>Bamboo Jungle（W>0） |        |

Plateau biomes generate at inland high terrain with moderate erosion, which results in biomes like meadows and savanna plateaus. The specific biome generation depends on temperature, humidity, and weirdness.

| TemperatureHumidity | T=0                                   | T=1                                                         | T=2                               | T=3             | T=4                                    |
|---------------------|---------------------------------------|-------------------------------------------------------------|-----------------------------------|-----------------|----------------------------------------|
| H=0                 | Snowy Plains（W<0）<br/>Ice Spikes（W>0） | Meadow（W<0）<br/>Cherry Grove（W>0）                           | Meadow（W<0）<br/>Cherry Grove（W>0） | Savanna Plateau | Badlands（W<0）<br/>Eroded Badlands（W>0） |
| H=1                 | Snowy Plains                          | Meadow                                                      |                                   |                 |                                        |
| H=2                 |                                       | Forest（W<0）<br/>Meadow（W>0）                                 | Meadow（W<0）<br/>Forest（W>0）       | Forest          | Badlands                               |
| H=3                 | Snowy Taiga                           | Taiga（W<0）<br/>Meadow（W>0）                                  | Meadow（W<0）<br/>Birch Forest（W>0） |                 | Wooded Badlands                        |
| H=4                 |                                       | Old Growth Spruce Taiga（W<0）<br/>Old Growth Pine Taiga（W>0） | Dark Forest                       | Jungle          |                                        |

Shattered biomes are generated at inland places with high erosion. The specific biome generation depends on temperature, humidity, and weirdness.

| TemperatureHumidity | T=0~1                    | T=2              | T=3                                | T=4    |
|---------------------|--------------------------|------------------|------------------------------------|--------|
| H=0~1               | Windswept Gravelly Hills | Windswept Hills  | Savanna                            | Desert |
| H=2                 | Windswept Hills          |                  | Forest（W<0）<br/>Plains（W>0）        |        |
| H=3                 |                          | Windswept Forest | Jungle（W<0）<br/>Sparse Jungle（W>0） |        |
| H=4                 |                          |                  | Jungle（W<0）<br/>Bamboo Jungle（W>0） |        |



### The Nether
An intersection of four different Nether biomes.
The Nether uses 3 parameters to generate biomes: temperature, humidity and offset. Unlike the Overworld, the Nether specifies biomes with a single point.

The offset parameter is not a noise, instead it is always 0 at any location in a world. This means that the parameter point of a location is always in the temperature-humidity-plane. The closer the offset (of a biome point) is to 0, the closer the point is to the T-H-plane and the greater the advantage it has during biome generation.

| Biomes           | Temperature | Humidity | Offset |
|------------------|-------------|----------|--------|
| Basalt Deltas    | -0.5        | 0        | 0.175  |
| Crimson Forest   | 0.4         | 0        | 0      |
| Nether Wastes    | 0           | 0        | 0      |
| Soul Sand Valley | 0           | -0.5     | 0      |
| Warped Forest    | 0           | 0.5      | 0.375  |

### The End
The End islands contain multiple biomes in Java Edition. In Bedrock Edition, there is always a single biome on all the islands.
In Java Edition, the End uses only one noise parameter: erosion. If the horizontal distance from the chunk origin of a chunk to the world origin is less than 1024, the blocks in the chunk are in The End. Otherwise, the biome is determined by erosion.

| Biome             | Erosion          |
|-------------------|------------------|
| Small End Islands | -1~-0.21875      |
| End Barrens       | -0.21875~-0.0625 |
| End Midlands      | -0.0625~0.25     |
| End Highlands     | 0.25~1           |

In Bedrock Edition, the End has only one biome: The End.

## Terrain
The Overworld after the "noise" step, which generates the base terrain.
For an overview of terrain features, see Terrain features.

For the terrain customization in Java Edition, see Custom noise settings.

Terrain shaping determines which blocks should be solid and which blocks should be filled with air.

### 3D noise
For customization of density functions in Java Edition, see Density function.

If the noise is in two dimensions, it controls only surface height and it is impossible to add terrain above the surface. To add overhangs and 3D shapes, the game uses 3D Perlin noise function that gives an output called density for every single block. A density > 0 means it is filled with solid block, otherwise it is filled with air.

Density is then given a height bias and a base height. Height bias "squeezes" the blocks. Base height is the base of the squeezing process where the density is left unchanged. Changing base height moves the ground up and down.

- In the Overworld, there is a single pair of height bias and base height, meaning the higher the block is, the less density it has and vice versa. Height bias and base height are both configured by a couple of different noises. Notably,amplifiedworlds are generated by tuning height bias to be lower than default, so that terrain stretch in the vertical direction more.
- In the Nether, there are two pairs of base heights that create the thick, solid ceiling and ground, and the hollow space between them.
- In the End, these parameters are configured to squeeze the map into a big island located relatively at the bottom of the dimension.

- The side view of a world using a single noise
- The side view of a world using 3D noise, creating overhangs

### Splines
To give the world some dramatic terrain shapes like cliffs, fjords and plateaus, the game uses three 2D noise maps. These noises are mapped using splines to calculate the height offset and a vertical stretch factor. The same noises are also used in biome generation, which creates a soft link between biome and terrain. For example a mountainous area generates mountainous biome and plains biomes are generally flatter.

The larger the continentalness, the higher the average terrain height. Continentalness is used mainly for differentiating ocean and land.

The erosion parameter affect inland terrain during terrain generation. Erosion is mainly used to create large area of flat ground. The higher the erosion at a location, the lower the terrain height and the flatter the terrain.

The peaks and valleys (PV) value is calculated from weirdness. As the name suggests, it is mainly used for generating better peaks and valleys. The higher the PV value, the higher the terrain. Usually, at places with low continentalness or high erosion, when the PV level is "Valleys", the terrain is low enough to generate rivers. At high terrain, negative weirdness values lead to taller and more jagged and point peaks. When the erosion level is approximately 5, positive weirdness values result in weird inland terrain that is shattered and extremely precipitous and craggy.

- Continentalness creates distinction between land and ocean
- Large area of flat plains is created by high erosion.
- PV creates peaks and valleys like this fjord.

### Noise caves
Main article: Cave § Noise caves
The mechanics of noise cave generation.[4]
Noise caves are part of the base terrain generation and are generated using 3D Perlin noises. They come in the form of cheese caves, spaghetti caves, and noodle caves. Three noise maps, frequency, hollowness, and thickness, are parameters that control this process. Frequency controls the frequency of the cave generation.

- Cheese caves are pocket areas of the underground that come in various sizes. They are generated by taking the white area in a Perlin noise map. Hollowness controls the size of cheese caves.
- Spaghetti caves are long, narrow caves that wind their way through the underground. When generating, the edge of black and white part of noise image becomes air, making it look like long and wide spaghetti. Thickness controls the thickness of spaghetti caves.
- Noodle caves are a thinner and squigglier variant of spaghetti caves. They consist of tunnels usually 1 to 5 blocks in width. Its generating mechanism is similar to that of spaghetti caves. Thickness controls the thickness of noodle caves.

Additionally, noise pillars generate inside big cheese cave chambers. Frequency controls the frequency of the pillar generation while thickness control the thickness of them.

- Inside of a cheese cave.
- Inside of a spaghetti cave.
- Inside of a noodle cave.

### Aquifers
A cross section showing caves and aquifers.
Aquifers are liquid systems used in the Overworld to determine the fluid in all empty areas. Without aquifers all empty areas between sea-level and y=-54 would be filled with water. Areas below y=-55 are always filled with lava. To avoid all caves being flooded, aquifers are used to determine the fluid state of each position instead. Aquifers don't change the lava below y=-55. An aquifer can be in 3 different states, with a state selected for each position:

- Empty: Always filled with air
- Flooded: As if aquifers didn't exist: filled with air above the sea-level and a fluid below.
- Local fluid level: Picks a local liquid level and fills areas below with a liquid and areas above with air.

For positions above the preliminary surface, the aquifer state is "Flooded". In areas of the deep dark (Erosion < -0.22 and Depth > 0.9) the state is always "Empty". Otherwise the state is determined bases on a noise. Values below 0.4 are "Empty", values above 0.8 are "Flooded", otherwise a local fluid level is used. 

In positions near areas where the preliminary surface is below the sea-level the area of the "Flooded" aquifer state reaches slightly below the preliminary surface. In these areas the cutoff values for the noise are linearly decreased from 64 blocks below the preliminary surface upward. At the surface they are below -0.8 for "Empty" and above -0.3 for "Flooded". This causes the "Flooded" state to be much more common directly below rivers and oceans.

The local water level is determined in cells of size 16x40x16 blocks using a different noise. Whether to place water or lava is determined in cells of 64x40x64 blocks based on a third noise. Areas above y=-10 always use water.

Barriers are used to separate areas of different liquids and to separate liquids from air. The height of the barriers is dependent on a forth noise, causing water or lava to sometimes spill over the barrier.

### Ore veins
A fully exposed copper ore vein
Ore veins generate only in the Overworld. Three noises are used for vein generation: toggle, ridge, and gap.

Toggle is always 0 outside Y=-60 to Y=51 and can be negative or positive inside the range. The game attempts to generate an iron or a copper vein depending on whether toggle is < 0 or > 0. The attempts might fail because veins have a configured generating height.

Ridge is always -0.08 if Y level is outside the range. If ridge is > 0, the game skips the block.

Gap determines the ratio of ore-to-filler material, between 10% and 30% for any given vein. For non-filler blocks, 98% generate as normal ore blocks, while 2% are generated as raw ore blocks (Block of Raw Copper and Block of Raw Iron, respectively).

The blocks used in vein generation are hardcoded, though their size can be changed with datapacks.

## Surface
For customization of surface in Java Edition, see Surface rule.

The Overworld after the "surface" step.
After the base terrain is generated, the game replaces some blocks with grass blocks, sand, dirt, etc., depending on the biome and other conditions.

### Overworld
| Conditions   |                                                      |                                                       |                        |                                         | Result block      |
|--------------|------------------------------------------------------|-------------------------------------------------------|------------------------|-----------------------------------------|-------------------|
|              |                                                      |                                                       |                        | Gradient Y=-64 → Y=-59                  | Bedrock           |
| Surface[s 1] | Floor[s 2]                                           | Wooded Badlands                                       | Above Y=97             | Noise[s 3]                              | Coarse Dirt       |
|              |                                                      |                                                       |                        | No water above                          | Grass Block       |
|              |                                                      |                                                       |                        | Otherwise                               | Dirt              |
|              |                                                      | Swamp                                                 | At Y=63                | Noise[s 4]                              | Water             |
|              |                                                      | Mangrove Swamp                                        | Between Y=61 and Y=63  |                                         |                   |
|              | Badlands<br/>Eroded Badlands<br/>Wooded Badlands     | Floor[s 2]                                            |                        | Above Y=256                             | Orange Terracotta |
|              |                                                      |                                                       | Above Y=74             | Noise[s 3]                              | Terracotta        |
|              |                                                      |                                                       |                        | Otherwise                               | Hoodoo[s 5]       |
|              |                                                      |                                                       | Water no deeper than 1 | Ceiling[s 6]                            | Red Sandstone     |
|              |                                                      |                                                       |                        | Otherwise                               | Red Sand          |
|              |                                                      |                                                       |                        | Erosion[s 7]                            | Orange Terracotta |
|              |                                                      |                                                       |                        | Water[more information needed]          | White Terracotta  |
|              |                                                      |                                                       |                        | Ceiling[s 6]                            | Stone             |
|              |                                                      |                                                       |                        | Otherwise                               | Gravel            |
|              |                                                      | Surface is above Y=63                                 |                        | Above Y=63 and surface is below Y=74    | Orange Terracotta |
|              |                                                      |                                                       |                        | Otherwise                               | Hoodoo[s 5]       |
|              |                                                      | Floor[s 2]                                            |                        | Water no deeper than 6 blocks           | White Terracotta  |
|              | Floor[s 2]and water<br/>no deeper than 1             | Frozen Ocean<br/>Deep Frozen Ocean                    | Erosion[s 7]           | No water above                          | Air               |
|              |                                                      |                                                       |                        | Cold[s 8]                               | Ice               |
|              |                                                      |                                                       |                        | Otherwise                               | Water             |
|              |                                                      | Frozen Peaks                                          |                        | Steep face[s 9]or noise[s 10]           | Packed Ice        |
|              |                                                      |                                                       |                        | Ice noise within 0~0.025                | Ice               |
|              |                                                      |                                                       |                        | No water above                          | Snow Block        |
|              |                                                      | Snowy Slopes                                          |                        | Steep face[s 9]                         | Stone             |
|              |                                                      |                                                       | Noise[s 11]            | No water above                          | Powder Snow       |
|              |                                                      |                                                       |                        | No water above                          | Snow Block        |
|              |                                                      | Jagged Peaks                                          |                        | Steep face[s 9]                         | Stone             |
|              |                                                      |                                                       |                        | No water above                          | Snow Block        |
|              |                                                      | Grove                                                 | Noise[s 11]            | No water above                          | Powder Snow       |
|              |                                                      |                                                       |                        | No water above                          | Snow Block        |
|              |                                                      | Stony Peaks                                           |                        | Calcite noise within -0.0125~0.0125     | Calcite           |
|              |                                                      |                                                       |                        | Otherwise                               | Stone             |
|              |                                                      | Stony Shore                                           | Noise[s 12]            | Ceiling[s 6]                            | Stone             |
|              |                                                      |                                                       |                        | Otherwise                               | Gravel            |
|              |                                                      |                                                       |                        | Otherwise                               | Stone             |
|              |                                                      | Windswept Hills                                       |                        | Surface noise ≥ 4/33                    | Stone             |
|              |                                                      | Warm Ocean<br/>Beach<br/>Snowy Beach<br/>Desert       |                        | Ceiling[s 6]                            | Sandstone         |
|              |                                                      |                                                       |                        | Otherwise                               | Sand              |
|              |                                                      |                                                       |                        | Dripstone Caves                         | Stone             |
|              |                                                      | Windswept Savanna                                     |                        | Surface noise ≥ 7/33                    | Stone             |
|              |                                                      |                                                       |                        | Surface noise ≥ -2/33                   | Coarse Dirt       |
|              |                                                      | Windswept Gravelly Hills                              | Surface noise ≥ 8/33   | Ceiling                                 | Stone             |
|              |                                                      |                                                       |                        | Otherwise                               | Gravel            |
|              |                                                      |                                                       |                        | Surface noise ≥ 4/33                    | Stone             |
|              |                                                      |                                                       | Surface noise ≥ -4/33  | No water above                          | Grass Block       |
|              |                                                      |                                                       |                        | Otherwise                               | Dirt              |
|              |                                                      |                                                       |                        | Ceiling                                 | Stone             |
|              |                                                      |                                                       |                        | Otherwise                               | Gravel            |
|              |                                                      | Old Growth Pine Taiga<br/>Old Growth Spruce Taiga     |                        | Surface noise ≥ 7/33                    | Coarse Dirt       |
|              |                                                      |                                                       |                        | Surface noise ≥ 19/165                  | Podzol            |
|              |                                                      | Ice Spikes                                            |                        | No water above                          | Snow Block        |
|              |                                                      |                                                       |                        | Mangrove Swamp                          | Mud               |
|              |                                                      |                                                       |                        | Mushroom Fields                         | Mycelium          |
|              |                                                      |                                                       |                        | No water above                          | Grass Block       |
|              |                                                      |                                                       |                        | Otherwise                               | Dirt              |
|              | Floor[s 2]and<br/>water no deeper than 6             | Frozen Ocean<br/>Deep Frozen Ocean                    |                        | Erosion[s 7]                            | Water             |
|              | Floor with depth[s 13]and<br/>water no deeper than 6 | Frozen Peaks                                          |                        | Steep face[s 9]or noise[s 14]           | Packed ice        |
|              |                                                      |                                                       |                        | Ice noise within -0.0625~0.025          | Ice               |
|              |                                                      |                                                       |                        | No water above                          | Snow Block        |
|              |                                                      | Snowy Slopes                                          |                        | Steep face[s 9]                         | Stone             |
|              |                                                      |                                                       | Noise[s 15]            | No water above                          | Powder Snow       |
|              |                                                      |                                                       |                        | No water above                          | Snow Block        |
|              |                                                      |                                                       |                        | Jagged Peaks                            | Stone             |
|              |                                                      | Grove                                                 | Noise[s 15]            | Above water                             | Powder Snow       |
|              |                                                      |                                                       |                        | Otherwise                               | Dirt              |
|              |                                                      | Stony Peaks                                           |                        | Calcite noise within -0.0125~0.0125     | Calcite           |
|              |                                                      |                                                       |                        | Otherwise                               | Stone             |
|              |                                                      | Stony Shore                                           | Noise[s 12]            | Ceiling[s 6]                            | Stone             |
|              |                                                      |                                                       |                        | Otherwise                               | Gravel            |
|              |                                                      |                                                       |                        | Otherwise                               | Stone             |
|              |                                                      | Windswept Hills                                       |                        | Surface noise ≥ 4/33                    | Stone             |
|              |                                                      | Warm Ocean<br/>Beach<br/>Snowy Beach<br/>Desert       |                        | Ceiling[s 6]                            | Sandstone         |
|              |                                                      |                                                       |                        | Otherwise                               | Sand              |
|              |                                                      |                                                       |                        | Dripstone Caves                         | Stone             |
|              |                                                      | Windswept Savanna                                     |                        | Surface noise ≥ 7/33                    | Stone             |
|              |                                                      | Windswept Gravelly Hills                              | Surface noise ≥ 8/33   | Ceiling                                 | Stone             |
|              |                                                      |                                                       |                        | Otherwise                               | Gravel            |
|              |                                                      |                                                       |                        | Surface noise ≥ 4/33                    | Stone             |
|              |                                                      |                                                       |                        | Surface noise ≥ -4/33                   | Dirt              |
|              |                                                      |                                                       |                        | Ceiling                                 | Stone             |
|              |                                                      |                                                       |                        | Otherwise                               | Gravel            |
|              |                                                      |                                                       |                        | Mangrove Swamp                          | Mud               |
|              |                                                      |                                                       |                        | Otherwise                               | Dirt              |
|              | Warm Ocean<br/>Beach<br/>Snowy Beach                 |                                                       |                        | Floor with depth and secondary depth 6  | Sandstone         |
|              | Desert                                               |                                                       |                        | Floor with depth and secondary depth 30 |                   |
|              | Floor[s 2]                                           |                                                       |                        | Frozen Peaks<br/>Jagged Peaks           | Stone             |
|              |                                                      | Warm Ocean<br/>Lukewarm Ocean<br/>Deep Lukewarm Ocean |                        | Ceiling                                 | Sandstone         |
|              |                                                      |                                                       |                        | Otherwise                               | Sand              |
|              |                                                      |                                                       |                        | Ceiling                                 | Stone             |
|              |                                                      |                                                       |                        | Otherwise                               | Gravel            |
|              |                                                      |                                                       |                        | Below Y=0 and gradient Y=0 → Y=8        | Deepslate         |
|              |                                                      |                                                       |                        | Otherwise                               | Stone             |

### The Nether
| Conditions       |                        |                                       |                             |                               | Result block      |
|------------------|------------------------|---------------------------------------|-----------------------------|-------------------------------|-------------------|
|                  |                        |                                       |                             | Gradient Y=0 → Y=5            | Bedrock           |
|                  |                        |                                       |                             | Gradient Y=127 → Y=122        |                   |
|                  |                        |                                       |                             | Above Y=122                   | Netherrack        |
| Basalt Deltas    |                        |                                       |                             | Ceiling[s 6]                  | Basalt            |
|                  | Floor[s 2]             | Patch noise ≥ -0.012                  |                             | Surface between Y=30 and Y=35 | Gravel            |
|                  |                        |                                       |                             | Nether noise ≥ 0              |                   |
|                  |                        |                                       |                             | Otherwise                     | Blackstone        |
| Soul Sand Valley | Ceiling[s 6]           |                                       |                             | Nether noise ≥ 0              | Soul Sand         |
|                  |                        |                                       |                             | Otherwise                     | Soul Soil         |
|                  | Floor[s 2]             | Patch noise ≥ -0.012                  |                             | Surface between Y=30 and Y=35 | Soul Sand         |
|                  |                        |                                       |                             | Nether noise ≥ 0              | Soul Sand         |
|                  |                        |                                       |                             | Otherwise                     | Soul Soil         |
| Floor[s 2]       | Below Y=33             |                                       |                             | Erosion[s 7]                  | Lava              |
|                  | Warped Forest          | Netherack noise ≥ 0.54                | Above Y=31                  | Nether wart noise ≥ 1.17      | Warped Wart Block |
|                  |                        |                                       |                             | Otherwise                     | Warped Nylium     |
|                  | Crimson Forest         | Netherack noise ≥ 0.54                | Above Y=31                  | Nether wart noise ≥ 1.17      | Nether Wart Block |
|                  |                        |                                       |                             | Otherwise                     | Crimson Nylium    |
| Nether Wastes    | Floor with depth[s 13] | Soul sand noise ≥ -0.012              | Not erosion[s 7]            | Surface between Y=30 and Y=35 | Soul Sand         |
|                  |                        |                                       |                             | Otherwise                     | Netherrack        |
|                  | Floor[s 2]             | Above Y=31 and<br/>surface below Y=35 | Gravel layer noise ≥ -0.012 | Above Y=32                    | Gravel            |
|                  |                        |                                       |                             | Not erosion[s 7]              |                   |
|                  |                        |                                       |                             | Otherwise                     | Netherrack        |

### The End
| Conditions |  |  |  |        | Result block |
|------------|--|--|--|--------|--------------|
|            |  |  |  | Always | End Stone    |

1. ↑Above preliminary surface (aka. not in noise caves)
2. ↑ a b c d e f g h i jOnly the top layer of the floor surface
3. ↑ a bSurface noise within -0.909~-0.5454, -0.1818~0.1818, or 0.5454~0.909
4. ↑Swamp surface noise ≥ 0
5. ↑ a bSpecial hardcoded rule that places terracorra bands
6. ↑ a b c d e f g hOnly the top layer of the ceiling surface
7. ↑ a b c d e fA hole in the terrain, where the surface noise is 0
8. ↑Whether it is cold enough to snow here
9. ↑ a b c d eThe vertical gradient of the north and south side is greater than 2
10. ↑Packed ice noise within 0~0.2
11. ↑ a bPowder snow noise within 0.35~0.6
12. ↑ a bGravel noise within -0.05~0.05
13. ↑ a bThe top few layers of the floor surface
14. ↑Packed ice noise within -0.5~0.2
15. ↑ a bPowder snow noise within 0.45~0.58

## Carvers
For customization of carvers in Java Edition, see Custom carver.

The Overworld after the "carvers" step.
Carvers include carver caves and carver canyons. As the name suggest, they "carve" through the ground.

Carver caves and carver canyons are configured to have different probability to be generated in each chunk. If the carver generates, it carves through the ground in random directions starting at the configured start Y level:

- Carver caves generate from Y=-56 to Y=180. The probability of cave generation is higher at Y=-56 to Y=47. Carver caves sometimes including a main room and can have branches.
	- Nether carver caves generate Y=0 to Y=126.
- Canyons can start at levels 10 to 72.

- A carver cave in the Overworld with a main room.
- Soul Sand Valley with a Nether carver cave.
- A canyon in the Overworld.

## Structures
Main article: Structure
For the customization of structures in Java Edition, see Structure/JSON format, Structure set, Template pool, and Processor list.

Structures are grouped into structure sets. A structure set determines the placement positions of the structures and places a structure at these positions based on the biome. If no structure matches the biome, then no structure is placed at a given position. The structure positions are usually calculated based on the spacing, separation, and frequency parameters of the structure set. Spacing determines the average distance between structure placement position in chunks, and separation determines the minimum distance. Frequency controls the probability that a determined position is used. If the biome at the placement attempt does not match the requirement, the structure is not placed. An exception are strongholds in Java Edition, which are placed as concentric rings, see Stronghold#Generation. 

The following table gives the placement parameters for each structure set, as they are in Java Edition.

| Structure Set     | Spacing | Separation | Frequency | Structure              | Weight | Required Biomes                                                                                                       |
|-------------------|---------|------------|-----------|------------------------|--------|-----------------------------------------------------------------------------------------------------------------------|
| Ancient Cities    | 24      | 8          | 100%      | Ancient City           | 1      | Deep dark                                                                                                             |
| Buried Treasures  | 1       | 0          | 1%        | Buried Treasure        | 1      | Beach,Snowy Beach                                                                                                     |
| Desert Pyramids   | 32      | 8          | 100%      | Desert Pyramid         | 1      | Desert                                                                                                                |
| End Cities        | 20      | 11         | 100%      | End City               | 1      | End Midlands,End Highlands                                                                                            |
| Igloos            | 32      | 8          | 100%      | Igloo                  | 1      | Snowy Taiga,Snowy Plains,Snowy Slopes                                                                                 |
| Jungle Temples    | 32      | 8          | 100%      | Jungle Pyramid         | 1      | Jungle,Bamboo Jungle                                                                                                  |
| Mineshafts        | 1       | 0          | 0.4%      | Mineshaft              | 1      | many biomes                                                                                                           |
|                   |         |            |           | Badlands Mineshaft     | 1      | Badlands,Eroded Badlands,Wooded Badlands                                                                              |
| Nether Complexes  | 27      | 4          | 100%      | Fortress               | 2      | AnyNetherbiome                                                                                                        |
|                   |         |            |           | Bastion Remnant        | 3      | Crimson Forest,Nether Wastes,Soul Sand Valley,Warped Forest                                                           |
| Nether Fossils    | 2       | 1          | 100%      | Nether Fossil          | 1      | Soul Sand Valley                                                                                                      |
| Ocean Monuments   | 32      | 5          | 100%      | Ocean Monument         | 1      | Deep Oceans[st 1]                                                                                                     |
| Ocean Ruins       | 20      | 8          | 100%      | Cold Ocean Ruins       | 1      | Frozen Ocean,Frozen Ocean,Cold Ocean,Ocean,Deep Frozen Ocean,Deep Cold Ocean,Deep Ocean                               |
|                   |         |            |           | Warm Ocean Ruins       | 1      | Lukewarm Ocean,Warm Ocean,Deep Lukewarm Ocean                                                                         |
| Pillager Outposts | 32      | 8          | 20%[st 2] | Pillager Outpost       | 1      | Desert,Plains,Savanna,Snowy Plains,Taiga,Grove,Meadow,Frozen Peaks,Jagged Peaks,Stony Peaks,Snowy Slopes,Cherry Grove |
| Ruined Portals    | 40      | 15         | 100%      | Ruined Portal          | 1      | SeeRuined Portal#Generation<br/>Together: AllOverworldbiomes                                                          |
|                   |         |            |           | Desert Ruined Portal   | 1      |                                                                                                                       |
|                   |         |            |           | Jungle Ruined Portal   | 1      |                                                                                                                       |
|                   |         |            |           | Swamp Ruined Portal    | 1      |                                                                                                                       |
|                   |         |            |           | Mountain Ruined Portal | 1      |                                                                                                                       |
|                   |         |            |           | Ocean Ruined Portal    | 1      |                                                                                                                       |
|                   |         |            |           | Nether Ruined Portal   | 1      | AllNetherbiomes                                                                                                       |
| Shipwrecks        | 24      | 4          | 100%      | Shipwreck              | 1      | Any ocean                                                                                                             |
|                   |         |            |           | Beached Shipwreck      | 1      | Beach,Snowy Beach                                                                                                     |
| Strongholds       |         | N/A[st 3]  | 100%      | Stronghold             | 1      | AllOverworldbiomes[st 4]                                                                                              |
| Swamp Huts        | 32      | 8          | 100%      | Swamp Hut              | 1      | Swamp                                                                                                                 |
| Trail Ruins       | 34      | 8          | 100%      | Trail Ruins            | 1      | Taiga,Snowy Taiga,Old Growth Pine Taiga,Old Growth Spruce Taiga,Old Growth Birch Forest,Jungle                        |
| Villages          | 34      | 8          | 100%      | Plains Village         | 1      | Plains,Meadow                                                                                                         |
|                   |         |            |           | Desert Village         | 1      | Desert                                                                                                                |
|                   |         |            |           | Savanna Village        | 1      | Savanna                                                                                                               |
|                   |         |            |           | Snowy Village          | 1      | Snowy Plains                                                                                                          |
|                   |         |            |           | Taiga Village          | 1      | Taiga                                                                                                                 |
| Woodland Mansions | 80      | 20         | 100%      | Woodland Mansion       | 1      | Dark Forest                                                                                                           |

1. ↑Also requires surrounding to be river and ocean biomes only.
2. ↑Can't be placed within 10 chunks of any placement position of the "Villages" structure set.
3. ↑Strongholds are placed using concentric rings, see Stronghold#Generation.
4. ↑The placement position is biased toward most land biomes, away from river and ocean biomes.

Once a structure start has been determined, the structure itself is generated. First, the layout of the pieces is determined. This also happens in the structure_starts generation step. Since structures can spread across many chunks, the entire structure has to be generated as soon as any chunk the structure could reach is fully generated. The resulting piece positions are stored in the chunk of the structure start. Other chunks store a reference to the chunk that stores the structure pieces. When a chunk is generating its decoration in the features step, the stored pieces are placed in the world (see #Features).

## Features
The Overworld after the "features" step.
Main article: Feature
For the customization of features in Java Edition, see Configured feature and Placed feature.

The generation of features and placement of structure pieces (see #Structures) happens in the same step and are called decorations collectively. Each biome has a list of allowed features and structures that are possible to generate in them.

### Decoration steps
Features and structures generate in 11 steps after each other called decoration steps.

1. raw_generation:Small end islands
2. lakes:Lava lakes
3. local_modifications:Amethyst geodesandicebergs
4. underground_structures: Trial chambers, buried treasure, mineshafts, trail ruins,monster roomsandfossils
5. surface_structures: All other structures,desert wellsandblue ice patches
6. strongholds: Unused, strongholds use thesurface_structuresstep
7. underground_ores:Ore blobsand sand/gravel/claydisks
8. underground_decoration: Infested block blobs, nether gravel and blackstone blobs, and all nether ore blobs
9. fluid_springs: Water and lavasprings
10. vegetal_decoration:Trees,bamboo, cacti,kelp, and other ground and ocean vegetation
11. top_layer_modification:Freeze top layerfeature

### Generation
Trees and villages are a type of feature and structure respectively.
To generate features in a chunk, the game first determines a list of biomes that appear in that chunk or the 8 surrounding chunks. Using that biome list the game constructs a list of features that are possible to generate in those biomes. For each decoration step, first the matching structure pieces are placed, followed by the features. When a structure piece crosses a chunk border, only the part in the current chunk is placed. Each feature has its own placement rules including the number of placement attempts and where in the chunk should the feature try to be placed. The game follows the rules to select a block in the chunk then checks if the biome, block and its surroundings at the current position allows that feature to spawn, and if so places the feature. Features can place block outside the current chunk's boundaries but are limited in the nearby 3×3 area.

When features are generated, they can spill over into neighboring chunks that have already had their features generated. Thus, the feature order specified above is not always adhered to. It is therefore also possible for two worlds generated with the same seed, from the same version of Minecraft, to differ slightly depending on the players' travel routes, because the chunk generation order may determine which of two conflicting features overwrite or suppress the other.

## Lighting
Main article: Light
As one of the last steps of chunk generation, the light levels for each block are calculated. Before this step, no block placement updates light, and light updates are instead deferred to this step.

## Mob spawning
These glow squids spawn upon world generation in Java Edition.
Main article: Spawn § Natural generation
In Java Edition many animals generate upon initial chunk creation. One in ten newly-generated chunks attempts to generate animal mobs, usually in packs of up to 4 of the same species.

In Bedrock Edition animals do not spawn during chunk generation, but they continually attempt to spawn as part of the environmental spawning algorithm.

Notably, mobs that spawn with a structure (e.g. elder guardian in ocean monuments) are immediately spawned when the structure is placed and are not spawned in this step.

## Heightmaps
Main article: Heightmap
In Java Edition, heightmaps are technically calculated at every step of world generation. Before features are placed, there are only 2 heightmaps – OCEAN_FLOOR_WG and WORLD_SURFACE_WG. After feature placement, OCEAN_FLOOR, WORLD_SURFACE, MOTION_BLOCKING and MOTION_BLOCKING_NO_LEAVES are calculated.

