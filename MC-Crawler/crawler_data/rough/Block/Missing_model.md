# Missing textures and models
Minecraft makes use of missing textures and missing models to handle potential errors present in the game's resources as well as resource packs.

## Contents
- 1 Missing texture
	- 1.1 History
		- 1.1.1 History of the texture itself
		- 1.1.2 General history
- 2 Missing model
	- 2.1 History
		- 2.1.1 History of the model itself
			- 2.1.1.1 Block
			- 2.1.1.2 Item
		- 2.1.2 General history
- 3 Notable bugs
	- 3.1 Examples of cases where the missing model is not used
	- 3.2 Translucency ordering
	- 3.3 Unloading the default resources
- 4 Trivia
- 5 Gallery
- 6 References
- 7 See also

## Missing texture

  

This section is missing information about A solid magenta texture may be possible somehow:
https://youtu.be/q1UC2-6vtIw?t=4m16s
https://github.com/rwtema/DietHopper/issues/4. 
Please expand the section to include this information. Further details may exist on the talk page.



The missing texture is a placeholder texture used by Minecraft for handling cases where a suitable texture cannot be found. Outside of its use in missing models, this is almost always due to a texture being referenced which simply does not exist under that name.

The texture uses a prominent black  #000000 and magenta  #f800f8 checkerboard in Java Edition or a black  #000000 and magenta  #fc00ff checkerboard in Bedrock Edition, in order to stand out as much as possible in most cases. Using bright colors is industry standard, and black and magenta is employed by other game development studios, notably Valve.[1]

The texture is not intended to appear in vanilla gameplay, and cases where it does are due to misconfigured resource packs.

As of Java Edition 21w42a, there are six ways in which the missing texture can appear without using a resource pack, all of which require commands:

- By creatingminecraft:block_markerparticles associated with eitherair,cave airorvoid air:[2]
	- /particle minecraft:block_marker minecraft:air
	- /particle minecraft:block_marker minecraft:cave_air
	- /particle minecraft:block_marker minecraft:void_air
- By creatingminecraft:itemparticles associated with either air or aspyglass:[3][4]
	- /particle minecraft:item minecraft:air
	- /particle minecraft:item minecraft:spyglass
- By summoning apandaeating a spyglass.[4]
	- /summon minecraft:panda ~ ~ ~ {HandItems:[{id:"minecraft:spyglass", Count:1b},{}]}

When the game has to use the missing texture, such uses are generally announced in the game's output log:

- References to nonexistent textures results inUsing missing texture, unable to load [NAMESPACE]:textures/[TEXTURE].png : java.io.FileNotFoundException: [NAMESPACE]:textures/[TEXTURE].png
- Absent texture references for model elements results inUnable to resolve texture reference: #texture in [NAMESPACE]:block/[MODEL]
- Cases where no particle texture is specified does not output anything to the log at all.[5]This is why the air and spyglass items' use of the missing texture for particles goes unreported in the game logs.

### History
For cases where the missing texture was used in-game, see Java Edition missing texture and model uses § Missing texture and Bedrock Edition missing texture and model uses § Missing texture.

#### History of the texture itself
| Java Edition Beta |         |  |  |         |                                                                                                                                                                                                                                                                                                                       |
|-------------------|---------|--|--|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                   |         |  |  | 1.4     | The missing texture has been implemented. It differs depending on the system - see the subsection below.                                                                                                                                                                                                              |
|                   |         |  |  |         | Java Edition                                                                                                                                                                                                                                                                                                          |
|                   | 1.5     |  |  | 13w02a  | The missing texture has changed to display more descriptive text.                                                                                                                                                                                                                                                     |
|                   | 1.6.1   |  |  | 13w18a  | The missing texture generated has changed to a magenta and black checkerboard texture.                                                                                                                                                                                                                                |
|                   | 1.7.2   |  |  | 13w38a  | When anisotropic filtering is enabled, the missing texture has a 4x4 checker instead of a 2x2 checker.[6][7][8]This is due to the option replacing each texture with a 3x3 grid of the texture and selecting the middle 32x32 of it, which for the missing texture specifically gives the appearance of a 4x4 tiling. |
|                   | 1.8     |  |  | 14w25a  | Removed the anisotropic filtering option, meaning that the 2x2 checker is once again the only missing texture.                                                                                                                                                                                                        |
|                   | 1.13    |  |  | 17w43a  | The missing texture generated has changed.                                                                                                                                                                                                                                                                            |
|                   |         |  |  |         | Pocket Edition Alpha                                                                                                                                                                                                                                                                                                  |
|                   | v0.16.0 |  |  | build 5 | The missing texture has been implemented.                                                                                                                                                                                                                                                                             |

** b1.4-13w17a platform differences **

  

This section is missing information about 
MC-7225 OS X
MC-5094 OS X
MC-8997 OS X
include info on the exact match
find out what the exact match actually is
(it's probably the thing from github). 
Please expand the section to include this information. Further details may exist on the talk page.


The missing texture used in these versions would be generated differently depending on the operating system and Java version.[9]

| Texture       |                 | Operating system      | Java version                                                                                                                   | Notes                                                                                                              |
|---------------|-----------------|-----------------------|--------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| b1.4 - 13w01b | 13w02a - 13w17a |                       |                                                                                                                                |                                                                                                                    |
|               |                 | Windows XP            | 6.0.370.6[10]<br/>                                                                                                             | Appears standard across all Windows versions.<br/>No smoothing.                                                    |
|               |                 | Windows 7[11]         | 7[12] Update 11[13] Update 13[14] r15[15] Update 17[16]<br/>Update 11[13]<br/>Update 13[14]<br/>r15[15]<br/>Update 17[16]<br/> |                                                                                                                    |
|               |                 | Windows 10            | 1.8.0_51[17]<br/>                                                                                                              |                                                                                                                    |
|               |                 | Solaris 10[18]        | * 1.6.0_37[19]                                                                                                                 |                                                                                                                    |
|               |                 | Windows 10            | 11.0.10[17]<br/>16.0.2<br/>                                                                                                    | Minor differences in the x and u. No smoothing.                                                                    |
|               |                 | MacOS 10.3.9[20]      | 4[20]<br/>                                                                                                                     | No smoothing - standard for non-Retina systems.[17]                                                                |
|               |                 | MacOS 10.5.8          | 1.5.0_30[21]<br/>                                                                                                              |                                                                                                                    |
|               |                 | MacOS 10.6.8[22]      | 6[22]<br/>                                                                                                                     |                                                                                                                    |
|               |                 | MacOS 10.14.6[17]     | Apple legacy Java runtime 1.6.0_65-b14-468[17]<br/>                                                                            |                                                                                                                    |
|               |                 | MacOS 10.14.6[17]     | Apple legacy Java runtime 1.6.0_65-b14-468[17]<br/>                                                                            | Monochromatic smoothing - standard for Retina systems.[17]                                                         |
|               |                 | MacOS 10.14.6         | Apple legacy Java runtime 1.6.0_65-b14-468[23]<br/>                                                                            | Uses polychromatic smoothing instead of monochromatic smoothing like above.                                        |
|               |                 | MacOS 10.3.9[24]      | 4[24]<br/>                                                                                                                     | Monochromatic smoothing. Almost identical to the above version, with almost unnoticeable single-pixel differences. |
|               |                 | MacOS 10.5.8[25]      | Unknown                                                                                                                        |                                                                                                                    |
|               |                 | MacOS 10.4.11         | 1.5.0_19[26]<br/>                                                                                                              | Polychromatic smoothing.                                                                                           |
|               |                 | MacOS 10.14.6[17]     | 1.7.0 80-b15[17]<br/>1.8.0_51[17]<br/>                                                                                         | No smoothing.                                                                                                      |
|               |                 | MacOS 10.14.6[17]     | 1.8.0_301, GraalVM EE 21.2.0<br/>11.0.12, GraalVM EE 21.2.0<br/>16.0.2, GraalVM EE 21.2.0<br/>                                 | Monochromatic smoothing.                                                                                           |
|               |                 | MacOS 12.3.0[27]      | 1.8.0_74 (64-bit)[27]<br/>                                                                                                     | Appears to have been smoothed monochromatically with all non-white pixels subsequently set to black.               |
|               |                 | Debian[28]            | 1.8.0_351<br/>                                                                                                                 | No smoothing.                                                                                                      |
|               |                 | Debian[28]            | Zulu OpenJDK 1.8.0_352<br/>                                                                                                    | No smoothing.                                                                                                      |
|               |                 | Debian under WSL2[29] | 11.0.11<br/>                                                                                                                   |                                                                                                                    |
|               |                 | Ubuntu                | 16.0.1[30]<br/>                                                                                                                |                                                                                                                    |
|               |                 | FreeBSD               | 16.0.2<br/>                                                                                                                    |                                                                                                                    |
|               |                 | OpenBSD               | 16.0.2<br/>                                                                                                                    |                                                                                                                    |
|               |                 | Solaris 11[31]        | * 1.8.0_311[32]                                                                                                                |                                                                                                                    |
|               |                 | Arch[33]              | Temurin-17.0.3+7<br/>                                                                                                          | No smoothing.                                                                                                      |
|               |                 | Arch 6.1.1[34]        | 1.8.0_352 (64-bit)<br/>                                                                                                        | No smoothing.                                                                                                      |

#### General history
| Java Edition Beta |         |  |  |               |                                                                                                                                                                                                                                                                                                                                                                                |
|-------------------|---------|--|--|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                   |         |  |  | 1.4           | The game now generates missing textures for absent assets.                                                                                                                                                                                                                                                                                                                     |
|                   |         |  |  |               | Prior to this version, the game would outright crash if a texture could not be loaded.                                                                                                                                                                                                                                                                                         |
|                   |         |  |  |               | The texture does not exist in the vanilla game files as an image, and must be induced through either modding (such as simply deleting existing texture files from the jar) or major glitches which cannot be reliably reproduced.[35][36][37][38]                                                                                                                              |
|                   |         |  |  |               | Java Edition                                                                                                                                                                                                                                                                                                                                                                   |
|                   | 1.5     |  |  | 13w02a        | The missing texture is now added to procedurally-generated block and item texture atlases (stitched_terrain.pngandstitched_items.png).                                                                                                                                                                                                                                         |
|                   | 1.8     |  |  | 14w25a        | With the merging ofblocks-atlasanditems-atlasintotextures-atlas, blocks and items now both reference the same missing texture.                                                                                                                                                                                                                                                 |
|                   | 1.14    |  |  | 19w06a        | Addedparticles.png-atlaswith the deprecation ofparticles.png, containing a missing particle texture.                                                                                                                                                                                                                                                                           |
|                   |         |  |  | 19w07a        | Addedpaintings.png-atlaswith the deprecation ofpaintings_kristoffer_zetterstrand.png, containing a missing painting texture.                                                                                                                                                                                                                                                   |
|                   |         |  |  | 19w08a        | Addedmob_effects.png-atlaswith the removal of effect icons frominventory.png, containing a missing effect texture.                                                                                                                                                                                                                                                             |
|                   | 1.15    |  |  | Pre-release 1 | Banner patterns, shield banner patterns, beds, chests, signs and shulker boxes have been split fromtextures-atlasintobanner_patterns.png-atlas,shield_patterns.png-atlas,beds.png-atlas,chest.png-atlas,signs.png-atlasandshulker_boxes.png-atlas, each with their own copy of the missing texture inside, rather than using the same missing texture as blocks and items did. |
|                   |         |  |  |               | Pocket Edition Alpha                                                                                                                                                                                                                                                                                                                                                           |
|                   | v0.16.0 |  |  | build 5       | Presumably the version that added the missing texture. It is predefined as an actual file, rather than generated by the game.                                                                                                                                                                                                                                                  |

## Missing model

  

This section is missing information about Console output when a model is missing or invalid. 
Please expand the section to include this information. Further details may exist on the talk page.



In an analogous fashion to the missing texture being used for instances where no texture is defined, the missing model is use in cases where no model is defined, or the model is invalid.

By default, the missing model is a full 16×16 cube which uses the missing texture on all six faces. These faces are culled accordingly where possible. Only two faces will have the same color at each vertex, rather than the three one may expect; Mojang have decided to not fix this.[39]

The missing model is obviously also never intended to appear in standard gameplay, and uses the missing texture again to appear prominent and highlight errors to fix.

Contrary to popular belief, no central "missing texture block" has ever existed in the game; all cases of blocks which use this model are due to another block simply having no assigned texture or model.

### History
For cases where the missing model was used in-game, see Java Edition missing texture and model uses § Missing model.

#### History of the model itself
##### Block
| Java Edition |      |  |  |        |                                                                                                                                                                                                                                                                                  |
|--------------|------|--|--|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|              | 1.8  |  |  | 14w06b | Added the missing model.                                                                                                                                                                                                                                                         |
|              |      |  |  |        | It is worth noting that despite being 8x8x8, it maps the entire 16x16 texture on each side as opposed to only the central 8x8 section. This results in no visual oddities for the 2x2 missing texture due to it already only having four distinct square regions at each corner. |
|              |      |  |  | 14w10a | The missing model has changed to be a full cube.                                                                                                                                                                                                                                 |
|              |      |  |  | 14w25a | Removed the anisotropic filtering option, meaning that the 2x2 checker is once again the only missing texture, and the missing model that uses it the only missing model.                                                                                                        |
|              | 1.13 |  |  | 17w43a | The missing texture's change has resulted in the appearance of the missing model also changing.                                                                                                                                                                                  |

##### Item

  

This section is missing information about "equipped on head" history. 
Please expand the section to include this information. Further details may exist on the talk page.


** Inventory **
| Java Edition |      |  |  |        |                                                                                                                                                                                                                                                                            |
|--------------|------|--|--|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|              | 1.8  |  |  | 14w25a | The missing model now also applies to items. Its "gui" display type appears equivalent to other cubes.                                                                                                                                                                     |
|              | 1.9  |  |  | 15w31a | In the inventory, the missing model visuallyappearsto be a 2D missing texture; this is due to its viewing angle defaulting to straight-on from a face instead of at an angle, due to changes in how item models can be rendered, and only one face is visible as a result. |
|              | 1.13 |  |  | 17w43a | The changes to the missing texture have modified the appearance of the missing model.                                                                                                                                                                                      |
|              | 1.15 |  |  | 19w39a | Major changes to rendering in this version have made the missing model appear very slightly darker by default.                                                                                                                                                             |
|              |      |  |  | 19w40a | Items in the inventory are now shaded far less than previously. As a result, the missing model now appears much brighter.                                                                                                                                                  |
|              |      |  |  | pre3   | Shading has returned to items. The missing model now appears far darker than before 19w40a.                                                                                                                                                                                |
|              |      |  |  | pre4   | Item shading has changed, resulting in the missing model appearing darker than in the prior pre-release.                                                                                                                                                                   |
|              | 1.17 |  |  | 21w10a | The missing model's shading has returned to the level of shading it had in 1.15-pre3.                                                                                                                                                                                      |

** Dropped **
| Java Edition |      |  |  |        |                                                                                                           |
|--------------|------|--|--|--------|-----------------------------------------------------------------------------------------------------------|
|              | 1.8  |  |  | 14w25a | The missing model now also applies to items. Its "ground" display type appears equivalent to other cubes. |
|              | 1.9  |  |  | 15w31a | The missing model now appears the size of a full block as a dropped item.                                 |
|              | 1.13 |  |  | 17w43a | The changes to the missing texture have modified the appearance of the missing model.                     |

** Fixed **
| Java Edition |      |  |  |        |                                                                                                          |
|--------------|------|--|--|--------|----------------------------------------------------------------------------------------------------------|
|              | 1.8  |  |  | 14w25a | The missing model now also applies to items. Its "fixed" display type appears equivalent to other cubes. |
|              |      |  |  | 14w31a | Changed lighting for the "fixed" model.                                                                  |
|              | 1.9  |  |  | 15w31a | The missing model now appears larger than before in an item frame.                                       |
|              | 1.13 |  |  | 17w43a | The changes to the missing texture have modified the appearance of the missing model.                    |

** Held, first person **
| Java Edition |      |  |  |        |                                                                                                                          |
|--------------|------|--|--|--------|--------------------------------------------------------------------------------------------------------------------------|
|              | 1.8  |  |  | 14w25a | The missing model now also applies to items. Its "firstperson_righthand" display type appears equivalent to other cubes. |
|              | 1.9  |  |  | 15w31a | The missing model now appears the size of a full block when held in first person.                                        |
|              |      |  |  |        | Objects can now be held in the player's left hand.                                                                       |
|              | 1.13 |  |  | 17w43a | The changes to the missing texture have modified the appearance of the missing model.                                    |

** Held, third person/other entity **
| Java Edition |      |  |  |        |                                                                                                                                                                                                                                                          |
|--------------|------|--|--|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|              | 1.8  |  |  | 14w25a | The missing model now also applies to items. Its "thirdperson_righthand" display type appears equivalent to other cubes.                                                                                                                                 |
|              |      |  |  |        | Translucent items with a missing model exhibit a particularly interesting visual bug in relation to entities (including its holder) and translucent objects.                                                                                             |
|              |      |  |  | 14w29a | The "thirdperson_righthand" model has changed.                                                                                                                                                                                                           |
|              |      |  |  | 14w30a | For most items, the missing model is now the size of a full block when held in third person or by a mob or another player. Some invalid data value items such as invalid data value chests still appear to use the normal size.[more information needed] |
|              | 1.9  |  |  | 15w31a | The remaining invalid data value items like chests now use the full-size missing model.                                                                                                                                                                  |
|              |      |  |  |        | Objects can now be held in the player's left hand.                                                                                                                                                                                                       |
|              | 1.13 |  |  | 17w43a | The changes to the missing texture have modified the appearance of the missing model.                                                                                                                                                                    |
|              | 1.15 |  |  | 19w39a | Fixed the rendering bug that caused translucent items with broken models to render very strangely around entities and translucent objects, likely as part of the fix toMC-9553.                                                                          |

#### General history
| Java Edition |     |  |  |        |                                                                                                                                                                                                                                                  |
|--------------|-----|--|--|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|              | 1.8 |  |  | 14w06b | The missing model has been added as a model file undermodels/block/missingno.json.                                                                                                                                                               |
|              |     |  |  |        | Prior to this version, the game would crash with a NullPointerException if it tried to render a block with no defined model.[40]                                                                                                                 |
|              |     |  |  | 14w18a | The missing model is now hardcoded and cannot be modified by resource packs, as to prevent a crash if the model is replaced by something invalid.[41]                                                                                            |
|              |     |  |  |        | As a result, it is also absent from the jar file from this point onwards.                                                                                                                                                                        |
|              |     |  |  | 14w25a | The block breaking animation now applies properly to the model; previously, blocks that used it would appear to light up when broken (similarly to the tops and bottoms ofbedsbefore 14w10a) without displaying the cracking animation properly. |

## Notable bugs

  

This section of the article is empty. 
You can help by adding to it.


### Examples of cases where the missing model is not used
By definition, any block which does not use a model does not use the cubic missing model. If a model is still not defined for the block, however, this will likely still reflect in the block's particles.

| Block                                                                                                                                                                        | Reason                                                                                                                           |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Air<br/>Cave Air<br/>Void Air<br/>Barrier<br/>Light<br/>Structure Void<br/>                                                                                                  | The block is hardcoded to beinvisible. Despite having empty physical model data, defining such a model will not change it.       |
| Beds<br/>Shulker Boxes<br/>Signs<br/>Wall Signs<br/>Hanging Sign<br/>Wall Hanging Sign<br/>Heads<br/>Wall Heads<br/>Chest<br/>Trapped Chest<br/>Ender Chest<br/>Conduit<br/> | The block renders as an entity would. As of 1.20.1, all entity models besides item frames and glow item frames remain hardcoded. |
| Banners<br/>Wall Banners<br/>                                                                                                                                                | In addition to using an entity model, these blocks use a layering system to define textures.                                     |
| Moving Piston<br/>                                                                                                                                                           | This is a highly technical block which is only used in specific circumstances, with its own special rendering method.            |
| End Gateway<br/>End Portal<br/>                                                                                                                                              | These blocks utilize a "starfield" effect which is incompatible with the functionality of models.                                |
| Bubble Column<br/>Lava<br/>Water<br/>                                                                                                                                        | Fluid rendering is hardcoded and their handling differs significantly from blocks.                                               |

The vast majority of entity models are also completely hardcoded. There are two notable exceptions in the item frame and glow item frame, which do in fact have customizable models. Therefore, the item frame and glow item frame are the only two entities which are capable of using the missing model; all other entities may lose their texture, but retain the same model shape.

Horses are a particularly interesting example of an entity which are discussed further in a later section. In multiple version ranges, certain invalid horses can either appear completely invisible or have a solid white texture, neither of which are the missing model.

### Translucency ordering
From 14w25a up to 19w38b, there existed a remarkable visual bug where missing models associated with blocks that used translucent rendering (such as ice, stained glass, stained glass panes and slime blocks) would interact anomalously with the rendering of transparent blocks in the world, as well as of entities, including the holder. Unlike normal missing models, translucent blocks and other entities would render in front of such a model when held, even if they were physically farther away from the camera. However, this only applies if the distant entity or transparent block in question is not first occluded by the player model. As a result, the held translucent block can form a player-shaped silhouette around the player model in front of a background made of entities (such as paintings) or translucent blocks.

This effect can be seen without the use of resource packs up to 17w46a simply by holding ice, stained glass, stained glass panes or slime blocks of an invalid data value. For versions 17w47a up to 19w38b a resource pack is required to break the model of an existing translucent item, and from 19w39a the bug is no longer present at all.

- Normal player model for shape reference
- Missing model belonging to a non-translucent item
- Missing model belonging to a translucent item, resulting in a player outline forming behind it

This effect also happened to particles and certain other objects in-game from 13w41a onwards.

### Unloading the default resources
If a sufficiently broken resource pack is loaded, the game will catch such resource packs and unload them automatically if errors were detected. From 17w43a up to the full release of 1.13, this also included the default resources, meaning that applying a flawed resource pack would result in all assets being unloaded, and as such the missing error assets appearing everywhere.

- 

From 18w30a onwards, the game was made to unload all resource packs except the default resources in cases like these.[42]

** Layered textures **
Certain game objects do not use textures in the standard way, instead layering them on top of each other. Horses use these for their pattern variants, and banners for each banner pattern. When there is no texture to pick from, these instead appear completely white. If the textures in question have already been loaded into the game, it is not possible to unload them even if all other textures are unloaded.

As shields use an item model, even though said item model points to an entity model, it appears as a missing model even though it makes use of texture layering.

Tropical fish, despite also using composite textures to distinguish variants, do not turn white if a texture cannot be loaded, and instead use the usual checkerboard (which is tinted in certain cases).

The screenshots below also demonstrate that player skins, despite not being layer-based, are also not unloaded due to not being resource pack dependent.

- Horses and banners with no textures loaded
- Horses and banners with textures persisting after everything else has been unloaded

** Main menu **
It is interesting to note how this bug highlights different changes to parts of the game through 1.13's development. Focusing on the main menu, for example, reveals multiple details:

- From 17w43a up to 18w22c, the menu appears as in the first image. The panorama cube is clearly visible, with each square replaced with the missing texture.
- From 1.13-pre1 up to 1.13-pre5, the main menu background is now a large missing texture itself, obscuring the view of the panorama cube. This is likely due to the introduction of thepanorama_overlay.pngtexture file in this version, which is responsible for the whitish gradient effect visible above the panorama; previously the gradient was hardcoded and unable to be changed with resource packs.
- In 1.13-pre6, font characters do not seem to load at all.
- In 1.13-pre7 and 1.13-pre8, font characters now use a rectangle shape which is commonly seen in many fonts as a placeholder for unsupported characters. Prior to 1.13-pre6, characters used the missing texture colors instead, of varying widths. This may imply that font character sizes were hardcoded prior to this version.
- From 1.13-pre9 up to the full release of 1.13, the rectangular placeholder font characters are now solid black on the inside, rather than being hollow as one would expect.

- 17w43a - 18w22c
- 1.13-pre1 - 1.13-pre5
- 1.13-pre6
- 1.13-pre7 - 1.13-pre8
- 1.13-pre9 - 1.13

** Enchantment glint **
Interestingly, the rendering of the enchantment glint on items to which it applies appears different when all assets are unloaded, compared to cases where the enchantment glint image file and its associated mcmeta are deleted instead. For the unloaded case, the texture is renderedmuch smaller and moved much slower. The exact underlying reason for this currently remains unknown.

|     | Unenchanted | Normal | Deleted | Unloaded |
|-----|-------------|--------|---------|----------|
| JE1 |             |        |         | ?        |
| JE2 |             |        |         | ?        |
| JE3 |             |        |         |          |

