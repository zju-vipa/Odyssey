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

