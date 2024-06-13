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

