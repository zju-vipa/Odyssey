# Resource pack
The resource pack system provides a way for players to customize textures, models, music, sounds, languages, texts such as the end poem, splashes, credits, and fonts without any code modification.

## Contents
- 1 Java Edition
	- 1.1 Behavior
		- 1.1.1 Default resource packs
	- 1.2 Folder structure
	- 1.3 Contents
		- 1.3.1 Pack format
		- 1.3.2 Language
		- 1.3.3 Models
		- 1.3.4 Sounds
		- 1.3.5 Textures
		- 1.3.6 Atlases
		- 1.3.7 Animation
		- 1.3.8 Villagers
		- 1.3.9 GUI
		- 1.3.10 Colormaps
		- 1.3.11 Properties
		- 1.3.12 Texts
		- 1.3.13 Fonts
		- 1.3.14 Texture sheets
		- 1.3.15 Shaders
		- 1.3.16 Regional compliancies warnings
- 2 Bedrock Edition
	- 2.1 Behavior
		- 2.1.1 Default packs
	- 2.2 Folder Structure
- 3 History
- 4 Trivia
- 5 Gallery
- 6 See also
- 7 External links
- 8 References

## Java Edition
### Behavior
The default resource pack settings.
Resource packs can be placed in the folder resourcepacks within the .minecraft folder. Each resource pack is either a sub-folder or a .zip file within the resourcepacks folder. Once in the folder, a resource pack can be added from the options, where resource packs can be moved between "Available resource packs" and "Selected resource packs". "Selected resource packs" also contain the default assets on the bottom, which cannot be removed.

Resource packs load their assets based on the order of the packs on the list. The bottom-most pack loads first, then each pack placed above it replaces assets of the same name with its assets.

#### Default resource packs
A resource pack can be bundled with a world by saving it as a .zip file under the name resources.zip and placing it directly in the world's folder. When playing the world, that resource pack appears as the default right above the default resource pack.
A resource pack can be set on a server by adding a link to a .zip file download after the line resource-pack= in the server.properties file. Users then have an option of whether to download the resource pack or not. Resource packs can also be forced on a server using resource-pack-required=true in the server.properties file. Rejecting the resource pack disconnects the player from the server.

The old (pre-1.14) textures are available in a resource pack titled "Programmer Art". These textures are not updated when the game receives new textures.

### Folder structure
Resource packs use the following folder structure:

- (resource pack name)
	- pack.mcmeta
	- pack.png
	- assets
		- iconsicon_16x16.png
icon_32x32.png
icon_48x48.png
icon_128x128.png
icon_256x256.png
minecraft.icns
			- icon_16x16.png
			- icon_32x32.png
			- icon_48x48.png
			- icon_128x128.png
			- icon_256x256.png
			- minecraft.icns
		- (namespace)sounds.json
blockstates
(blockstate).json
gpu_warnlist.json
font
(font)
icons
icon_16x16.png
icon_32x32.png
minecraft.icns
lang
(lang).json
models 
block
(model).json
item
(model).json
particles
(particle).json
regional_compliancies.json
sounds
(sound).ogg
shaders 
post
(post).json
program
(fragment shader).fsh
(program).json
(vertex shader).vsh
texts
(text).txt
textures 
block
(texture).png
colormap
(texture).png
effect
(texture).png
entity
(texture).png
(entity type)
(texture).png
environment
(texture).png
font
(texture).png
gui 
(texture).png
sprites
advancements
(texture).png
widget
(texture).png
backgrounds
(texture).png
container
(texture).png
creative_inventory
(texture).png
presets
(texture).png
title
(texture).png
background
(texture).png
item
(texture).png
map
(texture).png
misc
(texture).png
mob_effect
(texture).png
models
armor
(texture).png
painting
(texture).png
particle
(texture).png
			- sounds.json
			- blockstates
				- (blockstate).json
			- gpu_warnlist.json
			- font
				- (font)
			- icons
				- icon_16x16.png
				- icon_32x32.png
				- minecraft.icns
			- lang
				- (lang).json
			- modelsblock
(model).json
item
(model).json
				- block
					- (model).json
				- item
					- (model).json
			- particles
				- (particle).json
			- regional_compliancies.json
			- sounds
				- (sound).ogg
			- shaderspost
(post).json
program
(fragment shader).fsh
(program).json
(vertex shader).vsh
				- post
					- (post).json
				- program
					- (fragment shader).fsh
					- (program).json
					- (vertex shader).vsh
			- texts
				- (text).txt
			- texturesblock
(texture).png
colormap
(texture).png
effect
(texture).png
entity
(texture).png
(entity type)
(texture).png
environment
(texture).png
font
(texture).png
gui 
(texture).png
sprites
advancements
(texture).png
widget
(texture).png
backgrounds
(texture).png
container
(texture).png
creative_inventory
(texture).png
presets
(texture).png
title
(texture).png
background
(texture).png
item
(texture).png
map
(texture).png
misc
(texture).png
mob_effect
(texture).png
models
armor
(texture).png
painting
(texture).png
particle
(texture).png
				- block
					- (texture).png
				- colormap
					- (texture).png
				- effect
					- (texture).png
				- entity
					- (texture).png
					- (entity type)
						- (texture).png
				- environment
					- (texture).png
				- font
					- (texture).png
				- gui(texture).png
sprites
advancements
(texture).png
widget
(texture).png
backgrounds
(texture).png
container
(texture).png
creative_inventory
(texture).png
presets
(texture).png
title
(texture).png
background
(texture).png
					- (texture).png
					- sprites
						- advancements
							- (texture).png
						- widget
							- (texture).png
						- backgrounds
							- (texture).png
					- container
						- (texture).png
						- creative_inventory
							- (texture).png
					- presets
						- (texture).png
					- title
						- (texture).png
						- background
							- (texture).png
				- item
					- (texture).png
				- map
					- (texture).png
				- misc
					- (texture).png
				- mob_effect
					- (texture).png
				- models
					- armor
						- (texture).png
				- painting
					- (texture).png
				- particle
					- (texture).png

More than one directory for different namespaces may exist under the assets directory.

### Contents
A resource pack is identified by Minecraft based on the presence of the file pack.mcmeta in the root directory, which contains a JSON file with the following information:

- The root tag
	- pack: Holds the resource pack information
		- pack_format: Pack version. If this number does not match the current required number, the resource pack displays an error and requires additional confirmation to load the pack. SeePack formatfor a full list of pack format numbers.
		- supported_formats: Section for describing the range ofPack formatsthe resource pack supports, from the first number to the second. If the resource pack is loaded in a version out of the specified range, it is displayed as unsupported.
		- supported_formats: Section for describing the range ofPack formatsthe resource pack supports, fromtomax_inclusive.
			- min_inclusive: The minimum format which should display as supported.
			- max_inclusive: The maximum format which should display as supported.
		- description: Text shown below the pack name in the resource pack menu. The text is shown on two lines. If the text is too long it is truncated.
		- description: Contains araw JSON textobject that is shown instead as the pack description in the resource pack menu. Same behavior as thestringversion of thedescriptiontag, but they cannot exist together.
	- language: Contains additional languages to add to the language menu
		- Language code for a language, corresponding to a.jsonfile with the same name in the folderassets/<namespace>/lang.
			- name: The full name of the language
			- region: The country or region name
			- bidirectional: If true, the language reads right to left.
	- filter: Section for filtering out files from resource packs applied below this one. Any file that matches one of the patterns insideblockis treated as if it was not present in the pack at all.
		- block: List of patterns
			- Pattern entry.
				- namespace: Aregular expressionfor the namespace of files to be filtered out. If unspecified, it applies to every namespace.
				- path: Aregular expressionfor the paths of files to be filtered out. If unspecified, it applies to every file.
	- overlays: Holds the resource pack overlays information.
		- entries: List of resource pack overlays, which is read from the bottom to top by the game.
			- : Resource pack overlay entry.
				- directory: The directory where the overlay pack is located relative to the resource packs root directory. In this directory,pack.mcmetaandpack.pngwould be ignored.
				- formats: Section for describing the range ofPack formatsin which the overlay should be applied, from the first number to the second.
				- formats: Section for describing the range ofPack formatsin which the overlay should be applied, frommin_inclusivetomax_inclusive.
					- min_inclusive: The minimum format in which the overlay should be applied.
					- max_inclusive: The maximum format in which the overlay should be applied.

The root directory also contains an optional image called pack.png, which appears as the thumbnail for the pack on the resource pack selection menu.

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

#### Villagers
Textures from assets/minecraft/textures/entity/villager and assets/minecraft/textures/entity/zombie_villager support a .mcmeta file in JSON format containing additional effects to apply to the hat layer. The file is contained in the same directory as the texture, and has the same name as the texture, except appended with .mcmeta. For example, the file profession/farmer.png can have a properties file called profession/farmer.png.mcmeta

- The root tag
	- villager: Contains data for the texture
		- hat: Can befull,partial, or default (no.mcmetafile). Determines whether the villager's 'profession' hat layer should allow the 'type' hat layer to render or not.[more information needed]

If the .mcmeta file does not exist in the pack and the texture does, the game loads the default settings, rather than loading a .mcmeta file from a pack below that pack.

#### GUI
Textures from assets/minecraft/textures/gui/sprites support a .mcmeta file in JSON format containing scaling behavior of the texture. For example, the file button.png can have a properties file called button.png.mcmeta

- The root tag
	- gui: Contains data for the texture
		- scaling: Scaling behavior of the texture.
			- type: Can bestretch(default),tile, ornine_slice. Determines the type of scaling method of the texture.
			- width: Number of pixels for this sprite to cover on-screen across its width. Only required iftypeis set totileornine_slice.
			- height: Number of pixels for this sprite to cover on-screen across its height. Only required iftypeis set totileornine_slice.
			- border: The size in pixels that the border slices should cover on-screen. Only required iftypeis set tonine_slice.
			- border: The size in pixels that the border slices should cover on-screen, respectively. Only required iftypeis set tonine_slice.
				- left: Number of pixels of the left border.
				- top: Number of pixels of the top border.
				- right: Number of pixels of the right border.
				- bottom: Number of pixels of the bottom border.

#### Colormaps
Colormaps are 256×256 pixel images which tell the game which color to use in each biome. They are located in assets/minecraft/textures/colormap. The game contains two colormaps: foliage.png colors plants such as leaves (except birch and spruce) and vines, and grass.png colors grass and grass blocks. Colormaps can be disabled on individual blocks by removing the tintindex tag from the block model.

#### Properties
Textures from assets/minecraft/textures/misc support a .mcmeta file in JSON format containing additional effects to apply to the texture. The file is contained in the same directory as the texture, and has the same name as the texture, except appended with .mcmeta. For example, the file pumpkinblur.png can have a properties file called pumpkinblur.png.mcmeta

- The root tag
	- texture: Contains data for the texture
		- blur: Causes the texture to blur when viewed from close up. Defaults tofalse
		- clamp: Causes the texture to stretch instead of tiling in cases where it otherwise would, such as on the shadow. Defaults tofalse
		- mipmaps: Custom mipmap values for the texture

If the .mcmeta file does not exist in the pack and the texture does, the game loads the default settings, rather than loading a .mcmeta file from a pack below that pack.

#### Texts
Two .txt files in UTF-8 format and one .json file exist in assets/minecraft/texts. They are used by the game to determine the text to display.

The file end.txt contains the text of the end poem, using formatting codes to apply the colors to the two speakers, and with the text PLAYERNAME being replaced with the player's name. After that file is shown, the contents of credits.json are shown.[more information needed]

The file splashes.txt contains lines of text separated using line breaks to determine the splashes to display in-game. Any splash can be replaced with different text.

#### Fonts
Main article: Font
A font file is a JSON file located at assets/<namespace>/font within a resource pack and contains a list of providers that each define how different characters appear. The default font is defined by the font minecraft:default while the default font used by enchantment tables is defined by the font minecraft:alt.

The resource locations referenced in font providers should also include the file extensions, as there is no sole file extension used throughout.

- The root tag.
	- providers: A list of providers that make up this font.
		- A font provider. The contents depend on the value of that provider's"type"tag.
			- type: The type of the font provider. Can be one of the following:
				- bitmap: A bitmap font.
					- file: The resource location of the used file, starting fromassets/minecraft/texturesby default. Prefacing the location with<namespace>:changes the location toassets/<namespace>/textures.
					- height: Optional. The height of the character, measured in pixels. Can be negative. This tag is separate from the area used in the source texture and just re-scales the displayed result. Default is 8.
					- ascent: The ascent of the character, measured in pixels. This value adds a vertical shift to the displayed result.
					- chars: A list of strings containing the characters replaced by this provider, as well as their order within the texture. All elements must describe the same number of characters. The texture is split into one equally sized row for each element of this list. Each row is split into one equally sized character for each character within one list element.
				- legacy_unicode: A legacy unicode font. This format is deprecated, prioritized only when the "Force Unicode Font" option is turned on.
					- sizes: The resource location of a binary file describing the horizontal start and end positions for each character from 0 to 15. The file extension of the target file should be.bin. The resource location path is relative to the namespace root.
					- template: The resource location insideassets/<namespace>/texturesthat leads to the texture files that should be used for this provider. The game replaces%sfrom the value of this tag with the first two characters of the hex code of the replaced characters, so a single provider of this type can point into multiple texture files.
				- ttf: ATrueType fontorOpenType font. Despite its name, it supports both TTF and OTF.
					- file: The resource location of the TrueType/OpenType font file withinassets/<namespace>/font.
					- shift: The distance by which the characters of this provider are shifted.
						- Left shift, negative values are allowed.
						- Downward shift, negative values are allowed.
					- size: Font size to render at.
					- oversample: Resolution to render at, increasing anti-aliasing factor.
					- skip: String of characters or array of characters to exclude.
				- space: Show chosen characters as spaces.
					- advances
						- A character: The amount of pixels that the following characters are moved to the right. Can be negative. Decimal numbers can be used for precise movement on higher GUI scales.
				- unihex: Replacement forlegacy_unicode. Uses theGNU Unifont .hexformat.
					- hex_file: Path to a ZIP archive containing one or more *.hex files at the root (files in ZIP archive with different extensions are ignored). Does not walk recursively inside archive.
					- size_overrides: List of compounds that contain character ranges that should have widths different than auto-detected.
						- A size override.
							- from: 1-character wide string of the character to start override range at. Inclusive.
							- to: 1-character wide string of the character to end override range at. Inclusive.
							- left: Position of left-most column of glyphs in override range.
							- right: Position of right-most column of glyphs in override range.
				- reference: Links to another font file to be copied and included in this font. Guarantees the referenced provider is loaded only once. Inclusion is performed after all fonts are loaded.
					- id:Resource locationto another font provider.

All font providers also have an optional  filter object.‌[upcoming: JE 1.20.5]

- filter: An object defining when this provider will be active. When the button's state and filter's state are equal, that provider will be included.
	- uniform: Linked to "Force Uniform" button.
	- jp: Linked to "Japanese Glyph Variants" button.

#### Texture sheets
Main article: Texture atlas
Minecraft generally does not store multiple different textures on sheets and instead stores them on separate files. Two current exceptions are map icons[1] and experience orbs.[2]

#### Shaders
Main article: Shaders
Shaders are a way for resource packs to change how the game renders. They are written in OpenGL Shading Language (GLSL).

#### Regional compliancies warnings
Regional compliancies warnings can be customized at assets/<namespace>/regional_compliancies.json.

- The root tag
	- Region: Contains a list of warnings. Note that the key itself is anISO 3166-1 alpha-3region code determined by the device's locale setting.
		- delay: Optional. Defines how long should the game wait until showing this message in minutes. This can not be zero.
		- period: The time interval this message should be shown in minutes. This can not be zero.
		- title: The translation identifier of the title of the message. A slot is provided for the translation string, containing how many times this warning has been shown.
		- message: The translation identifier of the message. A slot is provided for the translation string, how many times this warning has been shown.

## Bedrock Edition

  

This section needs expansion. 
You can help by expanding it.


### Behavior
Similarly to skins, resource packs can be bought or made in Bedrock Edition. Users can download resource packs on the system itself with the .mcpack file names, if the game platform allows file importation. When these files are opened, they are automatically imported into the game without any need for file system access. Resource packs can also be put manually in the resource_packs folder in the com.mojang folder. Each resource pack must either be a sub-folder or a .zip file.

Resource packs can be applied on the Global Resources option from the settings menu from the main menu screen. Resource packs can be moved between "Active" and "My Packs". "Active" also contains the default assets at the bottom, and cannot be removed.

Resource packs load their assets based on the order of the packs on the list. The bottom-most pack loads first, then each pack placed above it replaces assets of the same name with its assets.

#### Default packs
One or more resource packs can be bundled with a world in the world settings. When playing the world, that resource pack appears as the default right above the default resource pack. A resource pack can be set on a server by bundling the resource pack in the world, and then re-uploading the world folder to the server. Users then have an option whether to use the resource pack or not if the texturepack-required option is disabled in the server settings and if the world has the "Require players to accept resource packs to join" option disabled. Resource packs can also be forced on a server by using the texturepack-required=true property on the server settings.

### Folder Structure
Resource packs use the following folder structure:

- (resource pack name)
	- biomes_client.json
	- blocks.json
	- manifest.json
	- pack_icon.png
	- sounds.json
	- animation_controllers
		- <entity>.animation_controllers.json
	- animations
		- <entity>.animation.json
	- attachables
		- <attachable>.json
	- entities
		- <entity>.entity.json
	- fogs
		- <biome>_fog_settings.json
	- models
		- mobs.json
		- <model>.geo.json[a]
	- particles
		- <particle>.json
	- render_controllers
		- <entity>.render_controllers.json
	- sounds
		- music_definitions.json
		- sound_definitions.json
		- <sound>.fsb[a]
		- <sound>.ogg[a]
		- <sound>.wav[a]
		- <sound>.mp3[a][b]
	- texts
		- languages.json
		- language_names.json
		- <languagecode>_<COUNTRYCODE>.lang
		- <languagecode>_<COUNTRYCODE>[c]
			- font
				- glyph_<code>.png
	- texture_sets[d]
	- textures
		- flipbook_textures.json
		- item_texture.json
		- terrain_texture.json
		- <texture>.png[a]
		- <texture>.tga[a]
	- ui
		- <ui>.json[a]

1. ↑ a b c d e f g hFile may be inside a folder.
2. ↑.mp3 files aren't fully supported.
3. ↑For languages using a different font.
4. ↑Unused.

