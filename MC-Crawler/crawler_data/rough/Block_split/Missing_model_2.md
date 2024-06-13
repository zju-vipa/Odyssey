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


