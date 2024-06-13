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

