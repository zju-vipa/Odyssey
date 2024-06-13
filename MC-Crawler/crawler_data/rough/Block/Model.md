# Model
Models are three-dimensional shapes used in Minecraft that are used to display objects encountered in the game.

The models pertaining to the vast majority of blocks and items can be configured, as well as those of a small selection of entities. Models are stored as JSON files in a resource pack in the assets/<namespace>/models folder.

## Contents
- 1 Block models
- 2 Item models
- 3 Uses of models
- 4 Objects that cannot be remodelled
	- 4.1 Blocks and fluids
- 5 History
- 6 References

## Block models
- The root tag
	- parent: Loads a different model from the given path, in form of aresource location. If both"parent"and"elements"are set, the"elements"tag overrides the"elements"tag from the previous model.
		- Can be set to"builtin/generated"to use a model that is created out of the specified icon. Note that only the first layer is supported, and rotation can be achieved only by using block states files.
	- ambientocclusion: Whether to useambient occlusion(true- default), or not (false). Note:only works on Parent file
	- display: Holds the different places where item models are displayed.
		- Position: Namedthirdperson_righthand,thirdperson_lefthand,firstperson_righthand,firstperson_lefthand,gui,head,ground, orfixed. Place where an item model is displayed. Holds its rotation, translation and scale for the specified situation.fixedrefers to item frames, while the rest are as their name states. Note that translations are applied to the model before rotations.
			- rotation: Specifies the rotation of the model according to the scheme[x, y, z].
			- translation: Specifies the position of the model according to the scheme[x, y, z]. The values are clamped between -80 and 80.
			- scale: Specifies the scale of the model according to the scheme[x, y, z]. If the value is greater than 4, it is displayed as 4.
	- textures: Holds the textures of the model, in form of aresource locationor can be another texture variable.
		- particle: What texture to load particles from. This texture is also used as an overlay if you are in anether portal, and used forwaterandlava's still textures.[1]This texture is also considered a texture variable that can be referenced as"#particle". Note: All breaking particles from non-model blocks are hard-coded, such as forbarriers.
		- Texture variable: Defines a texture variable and assigns a texture.
	- elements: Contains all the elements of the model. They can have only cubic forms. If both"parent"and"elements"are set, the"elements"tag overrides the"elements"tag from the previous model.
		- An element.
			- from: Start point of a cuboid according to the scheme[x, y, z]. Values must be between -16 and 32.
			- to: Stop point of a cuboid according to the scheme[x, y, z]. Values must be between -16 and 32.
			- rotation: Defines the rotation of an element.
				- origin: Sets the center of the rotation according to the scheme[x, y, z].
				- axis: Specifies the direction of rotation, can be"x","y"or"z".
				- angle: Specifies the angle of rotation. Can be 45 through -45 degrees in 22.5 degree increments.
				- rescale: Specifies whether or not to scale the faces across the whole block. Can be true or false. Defaults to false.
			- shade: Defines if shadows are rendered (true- default), not (false).
			- faces: Holds all the faces of the cuboid. If a face is left out, it does not render.
				- Face: Nameddown,up,north,south,westoreast. Contains the properties of the specified face.
					- uv:Defines the area of the texture to use according to the scheme[x1, y1, x2, y2]. The texture behavior is inconsistent if UV extends below 0 or above 16. If the numbers ofx1andx2are swapped (e.g. from0, 0, 16, 16to16, 0, 0, 16), the texture flips. UV is optional, and if not supplied it automatically generates based on the element's position.
					- texture:Specifies the texture in form of the texture variable prepended with a#.
					- cullface:Specifies whether a face does not need to be rendered when there is a block touching it in the specified position. The position can be:down,up,north,south,west, oreast. It also determines the side of the block to use the light level from for lighting the face, and if unset, defaults to the side.
					- rotation: Rotates the texture clockwise by the specified number of degrees. Can be 0, 90, 180, or 270. Defaults to 0. Rotation does not affect which part of the texture is used. Instead, it amounts to permutation of the selected texture vertexes (selected implicitly, or explicitly thoughuv).
					- tintindex: Determines whether to tint the texture using a hardcoded tint index. The default value, -1, indicates not to use the tint. Any other number is provided to BlockColors to get the tint value corresponding to that index. However, most blocks do not have a tint value defined (in which case white is used). Furthermore, no vanilla block currently uses multiple tint values, and thus the tint index value is ignored (as long as it is set to something other than -1); it could be used for modded blocks that need multiple distinct tint values in the same block though.

## Item models
- : The root tag
	- parent: Loads a different model from the given path, in form of aresource location. If both"parent"and"elements"are set, the"elements"tag overrides the"elements"tag from the previous model.
		- Can be set to"item/generated"to use a model that is created out of the specified icon.
		- Can be set to"builtin/entity"to load a model from an entity file. As you cannot specify the entity, this does not work for all items (only forchests,ender chests,mob heads,shields,bannersandtridents).
	- display: Holds the different places where item models are displayed.
		- Position: Namedthirdperson_righthand,thirdperson_lefthand,firstperson_righthand,firstperson_lefthand,gui,head,ground, orfixed. Place where an item model is displayed. Holds its rotation, translation and scale for the specified situation.fixedrefers to item frames, while the rest are as their name states. Note that translations are applied to the model before rotations. If this is specified but not all of translation, rotation and scale are in it, the others aren't inherited from the parent.
			- rotation: Specifies the rotation of the model according to the scheme[x, y, z].
			- translation: Specifies the position of the model according to the scheme[x, y, z]. If the value is greater than 80, it is displayed as 80. If the value is less than -80, it is displayed as -80.
			- scale: Specifies the scale of the model according to the scheme[x, y, z]. If the value is greater than 4, it is displayed as 4.
	- textures: Holds the textures of the model, in form of aresource locationor can be another texture variable.
		- layerN: Used only to specify the icon of the item used in the inventory. There can be more than just one layer (e.g. forspawn eggs), but the amount of possible layers is hardcoded for each item. Works only in combination with"item/generated".
		- particle: What texture to load particles from. Used to determine the "crumb" particles generated by food items, as well as to determine thebarrierparticle (but it always usesitems/barrier.pngas blockbreaking particle), which otherwise uses "layer0".
		- Texture variable: Defines a texture variable and assigns a texture.
	- gui_light: Can be"front"or"side". If set to"side", the model is rendered like a block. If set to"front", model is shaded like a flat item. Defaults to"side".
	- elements: Contains all the elements of the model. They can have only cubic forms. If both"parent"and"elements"are set, the"elements"tag overrides the"elements"tag from the parrent model.
		- An element.
			- from: Start point of a cuboid according to the scheme[x, y, z]. Values must be between -16 and 32.
			- to: Stop point of a cuboid according to the scheme[x, y, z]. Values must be between -16 and 32.
			- rotation: Defines the rotation of an element.
				- origin: Sets the center of the rotation according to the scheme[x, y, z].
				- axis: Specifies the direction of rotation, can be"x","y"or"z".
				- angle: Specifies the angle of rotation. Can be 45 through -45 degrees in 22.5 degree increments.
				- rescale: Specifies whether or not to scale the faces across the whole block. Can be true or false. Defaults to false.
			- shade: Defines if shadows are rendered (true- default), not (false).
			- faces: Holds all the faces of the cuboid. If a face is left out, it does not render.
				- Face: Nameddown,up,north,south,westoreast. Contains the properties of the specified face.
					- uv:Defines the area of the texture to use according to the scheme[x1, y1, x2, y2]. If unset, it defaults to values equal to xyz position of the element. The texture behavior is inconsistent if UV extends below 0 or above 16. If the numbers ofx1andx2are swapped (e.g. from0, 0, 16, 16to16, 0, 0, 16), the texture flips. UV is optional, and if not supplied it automatically generates based on the element's position.
					- texture:Specifies the texture in form of the texture variable prepended with a#.
					- cullface:Specifies whether a face does not need to be rendered when there is a block touching it in the specified position. The position can be:down,up,north,south,west, oreast. It also determines the side of the block to use the light level from for lighting the face, and if unset, defaults to the side.
					- rotation: Rotates the texture by the specified number of degrees. Can be 0, 90, 180, or 270. Defaults to 0. Rotation does not affect which part of the texture is used. Instead, it amounts to permutation of the selected texture vertexes (selected implicitly, or explicitly thoughuv).
					- tintindex: Determines whether to tint the texture using a hardcoded tint index. Tint indexes are hard coded into an item and each tint index represents a different color (as defined in the item class). Note that only certain blocks/items have a tint index; all others remain unaffected.
	- overrides: Determines cases in which a different model should be used based on item tags. All cases are evaluated in order from top to bottom and last predicate that matches overrides. However, overrides are ignored if it has been already overridden once, for example this avoids recursion on overriding to the same model.
		- A case.
			- predicate: Holds the cases.
				- CaseA single case tag. Seeitem predicatesfor a full list of available tags.
			- model: The path to the model to use if the case is met, in form of aresource location.

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

