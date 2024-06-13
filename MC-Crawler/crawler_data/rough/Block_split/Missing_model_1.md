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

