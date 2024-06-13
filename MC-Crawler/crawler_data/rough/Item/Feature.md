# Feature
Features (also known as generated features) are small decorators generated in each chunk after terrain generation. This page lists generated features in a Minecraft world.

## Contents
- 1 Overworld
	- 1.1 Aboveground
	- 1.2 Underground
- 2 The Nether
- 3 The End
- 4 Plant-like
	- 4.1 Composed features
- 5 Generation
- 6 History
- 7 References

## Overworld
### Aboveground
| Feature             | Description                                                                                                                                                |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Forest rock         | Boulder made entirely of mossy cobblestone found in old growth taiga.                                                                                      |
| Iceberg             | Small island-like ice features made out of blue ice or packed ice, and snow found in frozen ocean and deep frozen ocean.                                   |
| Blue ice            | Small blobs ofblue iceadjacent topacked iceblocks, generating at or below the ocean surface.                                                               |
| Freeze top layer    | Ice on water and snow on blocks. InBedrock Edition, technically it is not a feature.                                                                       |
| Ice spike           | Tall spires made of packed ice found in theice spikesbiome.                                                                                                |
| Ice patch           | Disk-like feature of packed ice.                                                                                                                           |
| Lava lake           | A small, widespread feature that contains a volume oflava.                                                                                                 |
| Disk                | Small circular patches of clay, sand (sandstone if above air), grass (dirt if under solid-material block or water), and gravel found throughout the world. |
| Bonus Chest         | Chestgenerated near the player's spawn if the "Bonus chest" option is toggled on.                                                                          |
| Void start platform | A 33 by 33 platform ofstonecentered on a block ofcobblestone. Only generates in thevoid biomeor theVoid superflat presetat coordinates 8, 3, 8.            |
| Desert well         | A structure-like built ofsandstoneblocks andslabswith awatersource inside.                                                                                 |
| Spring              | Awaterorlavasource block that generates on the side of a hill, cave or ravine.                                                                             |
| Pile                | A pile of blocks that can only generate in villages. There are 5 variants of pile: Hay, Ice, Melon, Pumpkin and Snow.                                      |

### Underground
| Feature           | Description                                                                                    |
|-------------------|------------------------------------------------------------------------------------------------|
| Lava lake         | A small, widespread feature that contains a volume oflava.                                     |
| Monster room      | A structure-like feature that contains a monster spawner.                                      |
| Fossil            | A rarely-occurring skeletal feature composed of bone blocks, coal ore, or diamond ore.         |
| Dripstone cluster | Somepointed dripstoneblocks generates hanging from the ceiling.                                |
| Large dripstone   | Stalagnate composed entirely ofdripstone blocks.                                               |
| Pointed dripstone | A single stalagmite or stalactite composed ofpointed dripstoneblocks.                          |
| Underwater magma  | Magmas found underwater.                                                                       |
| Amethyst geode    | Geodes of amethyst also consist of calcite and smooth basalt as outer layer found underground. |
| Ore               | A feature consisting of a natural deposit of ores or other blocks.                             |

## The Nether
| Feature                   | Description                                                           |
|---------------------------|-----------------------------------------------------------------------|
| Delta                     | One-block-deep sheets of constrained lava.                            |
| Basalt column             | Vertical clusters of basalt blocks found within basalt delta biomes   |
| Basalt pillar             | A tall features made up of basalt block.                              |
| Glowstone blob            | Piles of glowstone.                                                   |
| Ore                       | A feature consisting of a natural deposit of ores or other blocks.    |
| Blob‌[Java Edition  only] | A feature consisting of a natural deposit ofbasaltsorblackstones.     |
| Spring                    | A singlelavasource block that generates inside blocks or open to air. |
| Fire patch                | A patch offireorsoul fire.                                            |

## The End
| Feature     | Description                               |
|-------------|-------------------------------------------|
| End podium  | The exit portal inthe End.                |
| End spike   | Tall spikes made ofobsidian.              |
| End gateway | End gateway blocksurrounded with bedrock. |
| End island  | Hemispherical clusters ofend stoneblocks. |

## Plant-like
| Feature       | Description                                                                                                                                                                                 |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Vines         | A single vine block found injunglebiomes andlush cavebiomes.                                                                                                                                |
| Bamboo        | Bamboo plant with optionalpodzolfound injunglebiomes.                                                                                                                                       |
| Glow lichen   | A singleglow lichenblock found underground.                                                                                                                                                 |
| Sculk patch   | A feature that placessculk catalystsandsculk shriekers.                                                                                                                                     |
| Huge mushroom | Tree-like features that consist ofmushroom blocks.                                                                                                                                          |
| Tree          | A feature consisting oflogsand appropriateleaves.                                                                                                                                           |
| Coral reef    | Coral reefs are features that consist ofcoral,coral fans,coral blocksandsea pickles. InBedrock  Edition, the coral reefs can also consist ofdead coral,dead coral fansanddead coral blocks. |
| Chorus plant  | A plant-like feature ofchorus flowerinthe End. InBedrock Edition. Technically, it is not a feature.                                                                                         |
| Vegetation    | Patches of vegetation likeflowersandgrass.                                                                                                                                                  |

### Composed features
The following features are composed of multiple plant-like features mentioned above.

Java Edition:

| Configured feature ID    | Included configured features                                   |
|--------------------------|----------------------------------------------------------------|
| `bamboo_vegetation`      | patch_grass_junglefancy_oakjungle_bushmega_jungle_tree         |
| `dark_forest_vegetation` | oakhuge_brown_mushroomhuge_red_mushroomdark_oakbirch	fancy_oak |

Bedrock Edition:

| Feature ID                                                                                                            | Included features                                                                                                                                                                         |
|-----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `legacy:flower_forest_foliage_feature`<br/>`legacy:forest_foliage_feature`<br/>`legacy:roofed_forest_foliage_feature` | huge_mushroom_featurescatter_tall_grass_around_forest_foliage_featuredouble_plant_featureselect_roofed_tree_featureselect_birch_tree_featurefancy_oak_tree_featureselect_oak_tree_feature |
| `legacy:swamp_foliage_feature`                                                                                        | seagrass_featurescatter_tall_grass_around_tree_featurehuge_mushroom_featureswamp_tree_feature                                                                                             |

## Generation
Main article: World generation § Features and structures
Features are generated for a given chunk after the terrain has been formed. When features are generated, they can spill over into neighboring chunks that have been previously generated. Thus, a tree at the edge of the generated world may be overwritten by a village before the player reaches it. It is also theoretically possible for two worlds generated with the same seed, from the same version of Minecraft, to differ slightly depending on the players' travel routes, because the chunk generation order may determine which of two conflicting features overwrite or suppress the other.

