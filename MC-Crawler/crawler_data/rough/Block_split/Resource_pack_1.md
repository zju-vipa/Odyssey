#### Pack format
For the full list of pack formats in all versions, see Pack format § List of resource pack formats.

#### Language
Resource packs can create language files of the type .json in the folder assets/<namespace>/lang. Each file either replaces information from a file of the same name in the default or a lower pack, or it creates a new language as defined by pack.mcmeta.

Each line in the .json file is in the standard json format of "identifier":"name" followed by a comma in case it is followed by another value in the next line. identifier is what the game uses to look up the name for something, and as such it should not be translated or changed. name is the name that is displayed. For example, stone in the default language file is "block.minecraft.stone":"Stone", with block.minecraft.stone being the identifier, and Stone being the displayed name.  Blank lines are ignored. The file needs to be valid JSON syntax, meaning it starts with a {, has a comma after every key value pair except the last one, and ends with a }.

Language files need to add only those lines that are changed by the pack. Any names that are not in the pack are loaded from the pack below, or default if no pack changes the names.

#### Models
Main article: Model
Models are files in JSON format with the extension .json, which determine the shape and textures of blocks and items.

Blocks use a block state file from assets/minecraft/blockstates to determine which model is loaded for each variant from the folder assets/minecraft/models/block. Meanwhile, each item has an item model in assets/minecraft/models/item to determine its model, which either loads from a block's model, contains data for its own custom model, or uses the default "flat" or "entity" model.

Models and block states used in packs below the top one are still loaded unless overridden in the top pack, which may cause some textures and models used by the top pack to no longer be loaded.

#### Sounds
Resource packs load additional sounds with the file type of .ogg. Each sound placed in the pack overrides the sounds from packs below, and packs also contain a file called sounds.json, which is placed within assets/minecraft. Unlike most other files in resource packs, sounds.json merges sound information from packs below the top pack, rather than each sounds.json file overriding the previous completely.

#### Textures
The "missing model" for invalid or missing models, prominently using the black and magenta "missing texture".
For block or item textures to function, they must have equal width and height (or height that is a multiple of the width if animated); otherwise it appears as a magenta and black checkerboard. For most other textures, the file is stretched to fit the required dimensions.

Most solid blocks turn any transparent area fully opaque. Some other blocks, which have "cutout" transparency (like glass) turn all pixels that are less than 10% opaque fully transparent and all other pixels completely opaque. Every other block renders textures with semi-transparency as-is. All items and any blocks or entities that are semi-transparent by default support semi-transparency.

If a file does not exist in any resource pack, including the default, the missing texture appears in its place. As of 1.19.1, six such cases exist in the vanilla resource pack, all particle-related.

#### Atlases
Main article: Atlas
Atlases are configuration files, located in atlases directory, that control which textures are included in the atlases.

#### Animation
Block, item, particle, painting, item frame, and status effect icon (assets/minecraft/textures/mob_effect) textures support animation by placing each additional frame below the last. The animation is then controlled using a .mcmeta file in JSON format with the same name and .png at the end of the filename, in the same directory. For example, the .mcmeta file for stone.png would be stone.png.mcmeta.

- The root tag
	- animation: Contains data for the animation
		- interpolate: If true,Minecraftgenerates additional frames between frames with a frame time greater than 1 between them. Defaults tofalse.
		- width: The width of the tile, as a direct ratio rather than in pixels. This is unused in vanilla's files but can be used by resource packs to have frames that are not perfect squares.
		- height: The height of the tile as a ratio rather than in pixels. This is unused in vanilla's files but can be used by resource packs to have frames that are not perfect squares.
		- frametime: Sets the default time for each frame in increments of one game tick. Defaults to1.
		- frames: Contains a list of frames. Defaults to displaying all the frames from top to bottom.
			- A number corresponding to position of a frame from the top, with the top frame being 0.
			- A frame specifies a frame with additional data.
				- index: A number corresponding to position of a frame from the top, with the top frame being 0.
				- time: The time in ticks to show this frame, overriding "frametime" above.

If the .mcmeta file does not exist in the pack and the texture does, the game assumes the texture is not animated, rather than loading a .mcmeta file from a pack below that pack. If no .mcmeta file exists for a texture with unequal dimensions, the texture appears as a purple and black checkerboard.

