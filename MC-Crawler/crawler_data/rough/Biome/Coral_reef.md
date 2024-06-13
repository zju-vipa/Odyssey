# Coral reef
Coral reefs are features that generate in warm ocean biomes. They consist of multiple clusters of coral blocks, coral, and coral fans. These clusters come in a wide variety of shapes, sizes, and colors.

## Contents
- 1 Generation
	- 1.1 Java Edition
	- 1.2 Bedrock Edition
- 2 Structure
- 3 Data values
	- 3.1 ID
	- 3.2 Config
- 4 History
- 5 Issues
- 6 Gallery
	- 6.1 Screenshots
	- 6.2 In other media
- 7 References

## Generation
Coral reefs
### Java Edition
The distribution of coral reefs is noise-based, which means that in some places of warm ocean floor, the reefs are distributed densely, and in other places there's no coral reef at all.

There're three types of coral reefs: coral tree, coral claw, and coral mushroom. Coral tree has a main trunk and two to four branches that tend to point upward. Coral claw has two to three branches that tend to point horizontally. Coral mushroom looks like a small hut or a domed building.

All these three types consist of coral blocks, coral, coral fans and sea pickles.

Note that seagrass feature and sea pickle feature can generate on coral blocks because they are generated later than coral reefs. So coral reefs may have several sea pickles on them, but not all sea pickles on them belong to coral reef feature.

### Bedrock Edition
Unlike Java Edition, in Bedrock Edition coral features densely cover warm ocean's floor.

In Bedrock Edition, there're two types of coral features: huge coral and small coral.

There're two types of huge coral: coral (coral reefs) feature and coral crust feature. Coral feature comes in four varieties of shapes, including small clump, tree-like coral, craw-like coral, and coral spire. Coral crust feature is a huge pile of blocks including coral blocks, dead coral blocks, andesites, diorites, granites and sands. Both the two types of huge coral have some coral fans attached on them. Unlike Java Edition, there's no sea pickle in these feature, however, seagrass feature and sea pickle feature can also generate on them.

There're two types of small coral: sea anemone feature and coral hang feature. Sea anemone feature consists of coral and coral fans, generating attached to the top surface of blocks that are not lower than 16 blocks below the sea level (Y>=48). Coral hang feature consists of coral fans, generating attached to a side surface of blocks that are not lower than 14 blocks below the sea level (Y>=50).

## Structure

  

This feature is exclusive to  Bedrock Edition. 


In Bedrock Edition, coral crusts are generated with structure files, which are stored in the behavior_packs/vanilla/structures/coralcrust folder.

The structure blocks do not appear in the final generation.

| Structure name            | Consists of                           | Image |
|---------------------------|---------------------------------------|-------|
| `coralcrust/crust1`       | 31Sand20 Diorite10 Andesite12 Granite |       |
| `coralcrust/crust2`       | 22Granite19 Diorite16 Andesite11 Sand |       |
| `coralcrust/crust3`       | 17Sand14 Diorite13 Granite            |       |
| `coralcrust/crust4`       | 16Andesite11 Granite9 Sand            |       |
| `coralcrust/crust5`       | 33Andesite15 Diorite10 Sand           |       |
| `coralcrust/outcropping1` | 9Diorite8 Andesite                    |       |
| `coralcrust/outcropping2` | 12Granite11 Andesite8 Diorite         |       |
| `coralcrust/outcropping3` | 14Diorite                             |       |
| `coralcrust/outcropping4` | 14Granite                             |       |
| `coralcrust/outcropping5` | 12Andesite                            |       |
| `coralcrust/outcropping6` | 28Granite                             |       |

## Data values
### ID
Java Edition:

| Feature type        | Identifier       |
|---------------------|------------------|
| [No displayed name] | `coral_claw`     |
| [No displayed name] | `coral_mushroom` |
| [No displayed name] | `coral_tree`     |

| Configured feature  | Identifier              |
|---------------------|-------------------------|
| [No displayed name] | `warm_ocean_vegetation` |

Bedrock Edition:

| Feature             | Identifier            |
|---------------------|-----------------------|
| [No displayed name] | `coral_feature`       |
| [No displayed name] | `coral_crust_feature` |
| [No displayed name] | `coral_hang_feature`  |
| [No displayed name] | `sea_anemone_feature` |

### Config
Main article: Configured feature
Java Edition:

- config: Empty




An example

{
  "type": "minecraft:coral_claw",
  "config": {}
}



