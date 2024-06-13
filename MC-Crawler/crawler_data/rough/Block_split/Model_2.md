## Uses of models
Non-hardcoded models are used in-game in the following contexts:

| Use case                                                                                         | Uses                                  | Image | Respects shade=false? |
|--------------------------------------------------------------------------------------------------|---------------------------------------|-------|-----------------------|
|                                                                                                  |                                       |       | Blocks                |
| Placed blocks                                                                                    | All blocks excluding those listedhere |       | Yes                   |
| Falling blocks                                                                                   | All blocks excluding those listedhere |       | Yes                   |
| Piston-moved blocks                                                                              | All blocks excluding those listedhere |       | Yes                   |
| LitTNT                                                                                           | TNT                                   |       | No                    |
|                                                                                                  |                                       |       | Items                 |
| Items in the inventory                                                                           | All items excluding air               |       | No                    |
| Items in the player's hand (first person)                                                        | All items excluding air[verify]       |       | No                    |
| Items in the player's hand (third person)<br/>Items held by other players<br/>Items held by mobs | All items excluding air[verify]       |       | No                    |
| Items on the ground                                                                              | All items excluding air               |       | No                    |
| Items in item frames                                                                             | All items excluding air               |       | No                    |
| Totem of undyinganimation                                                                        | Totem of undying                      |       | No[verify]            |

## Objects that cannot be remodelled

  

This section is missing information about Objects needing testing:
Trident
Bell
Is the shield model hardcoded and non-customizable, even if the shield item definition isn't required to point to it?. 
Please expand the section to include this information. Further details may exist on the talk page.


While most blocks and items can have their model changed, there are a multitude of things that cannot.

For example, no entities (with the exception of item frames and glow item frames) can have their model changed in Java Edition with resource packs alone.

### Blocks and fluids
| Block                                                                                                                                                                        | Reason                                                                                                                           |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Air<br/>Cave Air<br/>Void Air<br/>Barrier<br/>Light<br/>Structure Void<br/>                                                                                                  | The block is hardcoded to beinvisible. Despite having empty physical model data, defining such a model does not change it.       |
| Beds<br/>Shulker Boxes<br/>Signs<br/>Wall Signs<br/>Hanging Sign<br/>Wall Hanging Sign<br/>Heads<br/>Wall Heads<br/>Chest<br/>Trapped Chest<br/>Ender Chest<br/>Conduit<br/> | The block renders as an entity would. As of 1.20.1, all entity models besides item frames and glow item frames remain hardcoded. |
| Banners<br/>Wall Banners<br/>                                                                                                                                                | In addition to using an entity model, these blocks use a layering system to define textures.                                     |
| Moving Piston<br/>                                                                                                                                                           | This is a highly technical block which is only used in specific circumstances, with its own special rendering method.            |
| End Gateway<br/>End Portal<br/>                                                                                                                                              | These blocks utilize a "starfield" effect which is incompatible with the functionality of models.                                |
| Bubble Column<br/>Lava<br/>Water<br/>                                                                                                                                        | Fluid rendering is hardcoded and their handling differs significantly from blocks.                                               |

Even these blocks (with the exception of the three air variants)[2] have particle textures defined in dedicated model files, however it still stands that actual visual models cannot be changed.

Sub-elements of blocks, such as passively emitted particles and the book on top of the enchanting table, cannot be modified, even though the base block can.


