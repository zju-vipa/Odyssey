# Wheat Seeds/Asset history


## Contents
- 1 Assets
	- 1.1 Java Edition
		- 1.1.1 Block texture and model history
	- 1.2 Bedrock Edition
		- 1.2.1 Block texture and model history

## Assets
#### Java Edition
##### Block texture and model history
| Yellow | The block was introduced in this version.                                                                      |
|--------|----------------------------------------------------------------------------------------------------------------|
| Green  | The block's texture was changed in this version.                                                               |
| Blue   | The block's model was changed in this version.                                                                 |
| Purple | The block's texture and model were both changed in this version.                                               |
| Orange | Another visual change was made to the block in this version which does not fit in any of the above categories. |
| Red    | The block was either removed in this version, no longer exists, or did not yet exist.                          |



** Intentional data values **

  

This section is missing information about Incorporate lighting changes under the orange color:
inf-20100618(?)
a1.0.1(?)
a1.2.0(?)
b1.8-pre1(?)
21w11a
21w39a ("Changed lighting."). 
Please expand the section to include this information. Further details may exist on the talk page.


| From version    |          | Age |   |   |   |   |   |   |   | Textures used |       | Further info                                                                                                                                                |
|-----------------|----------|-----|---|---|---|---|---|---|---|---------------|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                 |          | 0   | 1 | 2 | 3 | 4 | 5 | 6 | 7 | Before        | After |                                                                                                                                                             |
| Minecraft Indev | 20100206 |     |   |   |   |   |   |   |   | -             |       | Introduction                                                                                                                                                |
| 1.8             | 14w06a   |     |   |   |   |   |   |   |   | -             | -     | Crops have been converted over to block models, however this model has not been adjusted to move the texture planes down one pixel to fit in with farmland. |
|                 | 14w10a   |     |   |   |   |   |   |   |   |               |       | Model no longer works.                                                                                                                                      |
|                 | 14w10b   |     |   |   |   |   |   |   |   |               |       | Model now works again, and is correctly shifted downwards one pixel.                                                                                        |
|                 | 14w25a   |     |   |   |   |   |   |   |   | -             | -     | Model is now subject to directional shading much like full blocks are.                                                                                      |
|                 | 14w27a   |     |   |   |   |   |   |   |   | -             | -     | Model is no longer subject to directional shading.                                                                                                          |
| 1.14            | 18w43a   |     |   |   |   |   |   |   |   |               |       | Texture Update                                                                                                                                              |
|                 | 18w44a   |     |   |   |   |   |   |   |   |               |       | Texture Update                                                                                                                                              |
|                 | 18w47a   |     |   |   |   |   |   |   |   |               |       | Texture Update                                                                                                                                              |
| 1.17            | 21w13a   |     |   |   |   |   |   |   |   | -             | -     | The "crop" template model has changed such that pixels appear in the same physical positions on opposite sides of texture planes.                           |

** Extreme data values **

  

This section is missing information about Incorporate lighting changes under the orange color:
inf-20100618(?)
a1.0.1(?)
a1.2.0(?)
b1.8-pre1(?). 
Please expand the section to include this information. Further details may exist on the talk page.


While blocks have four bits assigned for metadata, only the bottom three are used by crops. As the eight textures for crops were all arranged in a straight line in terrain.png, crops with metadata values 8-15 would overflow and start reading textures from the next line. As the textures in these positions were changed multiple times, this also resulted in wheat with extreme metadata changing visually, often displaying the placeholder texture as a result.

| From version     |                       | Age |   |    |    |    |    |    |    | Textures used |       | Further info                                                                                                                                                              |
|------------------|-----------------------|-----|---|----|----|----|----|----|----|---------------|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                  |                       | 8   | 9 | 10 | 11 | 12 | 13 | 14 | 15 | Before        | After |                                                                                                                                                                           |
| Minecraft Indev  | 20100206              |     |   |    |    |    |    |    |    |               |       | Introduction; ages 11 and 12 borrow from the otherwise-unused chair and table textures.                                                                                   |
| Minecraft Infdev | 20100607              |     |   |    |    |    |    |    |    |               |       | Wheat with age values of 9 and 10 now use theoak doortextures.                                                                                                            |
|                  | 20100618              |     |   |    |    |    |    |    |    |               |       | The door textures as well as the unused chair texture are now darker.                                                                                                     |
|                  | 20100624              |     |   |    |    |    |    |    |    |               |       | The right-hinge oak door texture has been removed and re-replaced with the placeholder texture                                                                            |
|                  | 20100629              |     |   |    |    |    |    |    |    |               |       | The unused "chair and table" textures have been removed from the game.                                                                                                    |
|                  | Alpha v1.0.1          |     |   |    |    |    |    |    |    |               |       | Addedlevers,redstone wire,redstone torchesand iron doors.                                                                                                                 |
| Alpha v1.2.0     | preview               |     |   |    |    |    |    |    |    |               |       | Addedpumpkinsandnetherrack.                                                                                                                                               |
|                  | Beta 1.3              |     |   |    |    |    |    |    |    |               |       | Redstone wire's coloring is now handled differently, and the old textures have been removed.                                                                              |
| Beta 1.8         | Pre-release           |     |   |    |    |    |    |    |    |               |       | Addedmossy stone bricksandcracked stone bricks.                                                                                                                           |
| 1.0.0            | Beta 1.9 Prerelease 5 |     |   |    |    |    |    |    |    |               |       | Slightly changed the texture of netherrack.                                                                                                                               |
| 1.5              | 13w02a                | -   | - | -  | -  | -  | -  | -  | -  |               |       | Texture handling has been overhauled in this version.<br/>These blocks do not have any assigned textures, and therefore cause the game to crash.[more information needed] |
|                  | 13w09c                |     |   |    |    |    |    |    |    |               |       | Crops with data values 8-15 now always appears as fully grown wheat.                                                                                                      |
| 1.8              | 14w06a                |     |   |    |    |    |    |    |    |               |       | Crops have been converted over to block models, however this model has not been adjusted to move the texture planes down one pixel to fit in with farmland.               |
|                  | 14w10a                |     |   |    |    |    |    |    |    |               |       | No model is defined for these blocks.                                                                                                                                     |

