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



