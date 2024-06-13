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

