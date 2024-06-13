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


