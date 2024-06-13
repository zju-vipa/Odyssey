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


