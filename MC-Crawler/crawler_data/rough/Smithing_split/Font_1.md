## Providers

  

This feature is exclusive to  Java Edition. 


A font is constructed from a list of providers, sources that provide characters to use. Different providers use different formats and methods of constructing characters. The default font uses all except for 1, ttf.

### Bitmap provider
The bitmap provider defines simple bitmap glyphs – glyphs from textures. It references a single PNG file, a list of the characters it applies to, an optional height, and an ascent.

Textures may be any size, and glyphs may be any color. White glyphs can be colored any other color in-game. Other colors retain that tint when re-colored. Black glyphs always appear black. The glyph's widths are automatically determined based on the last right-most column of pixels containing any alpha value above 0. Glyphs themselves must not be larger than 512×512 pixels. The chars field is a list of strings. The characters inside each string entry inside this list are mapped to the corresponding positions in the referenced file. The texture is divided evenly according to the number of strings in the list, and the length of the longest string in that list.

Since Java Edition 1.16 Pre-release 7, UTF-16 codepoints encoded in UTF-8 sequences can be used by use of surrogate pairs. To convert a character into a surrogate pair, one can use the following equations, where C is the codepoint in decimal:

- High Surrogate (first codepoint):((C - 65536) - (C % 1024))  ÷  1024 + 55296
- Low Surrogate (second codepoint):(C % 1024) + 56320

When the length of either the list or the strings is not a divisor of the resource's dimensions, it can result in an unexpected division of glyphs. The Unicode escape \u0000 can be used to add padding in the list. Padding acts as a "dummy character", so that the glyph data at that corresponding position in the file is not assigned a character. 

The height field is the scale of the resulting glyph. This scale should generally match the a glyph's individual height, or be a power of it. While heights outside of this recommended range are allowed and are valid, the resulting glyphs declared inside the provider appears warped when rendered in-game. The height field is optional. When not defined, it defaults to 8, regardless of the underlying texture resolution. 

The ascent field is the amount of vertical shifting is applied to the glyph. In typography, the ascent is the distance above the baseline to the cap height (top of glyph). The baseline in a glyph is the line where the descender begins. For example, in the lowercase letter y, the bottom end of the y extends past the baseline. In Vanilla, when the height is 8, the ascent is most often 7, as the descender is 1. 

### Space provider
The space provider defines the width of a character's glyph. It is the most simple provider: it contains only the character widths.

The keys of the advances are the characters, and the values are the widths. The keys must be only 1 grapheme long (multi-byte character still count as one character, like U+1F525 🔥 FIRE, which is encoded as 0xF0 0x9F 0x94 0xA5). Values must be an integer whose absolute value is less than or equal to 256. Negative values are forced to 0 when typed in chat. Although it is intended to be used for whitespace characters (characters that have "WSpace=Y" in Unicode), it can be used for any character, as long as there is no prior definition of that character's glyph.

By default, the game has two widths defined:

- U+0020 <SPACE> SPACE is 4
- U+200C <ZWNJ> ZERO WIDTH NON-JOINER is 0

### TTF provider
The ttf provider embeds already-compiled TrueType and OpenType fonts.[b] It contains 5 fields.

The file field is a resource location to a file ending in .ttf. Path is relative from /assets/minecraft/font/.

The shift field is an array of two integers. It defines how much each glyph contained in this TrueType font is to be moved horizontally and vertically, respectively. The first element controls the horizontal shifting (positive is leftward, negative is rightward). The second element controls the vertical shifting (positive is downward, negative is upward).

The size field is similar to a bitmap provider's height field. This is a divisor by which the em-size of the font's glyphs are to be divided and then fitted into the bitmap grid. This value can vary greatly across different fonts.

The oversample field is the resolution to render at. Values that don't match the glyph's native em sizing division or DPI cause it to be anti-aliased.

The skip field is either a list of strings, or a string of the characters to which this font has no assignment. If it is a list of strings, the strings are concatenated together and then act as if it were originally a string. This allows the same input as a bitmap provider's chars.

### Legacy Unicode provider

  

This section describes content that exists only in outdated versions of Minecraft. 
This feature used to be in the game but has since been removed.


The legacy_unicode provider is similar to the bitmap provider in that it loads glyphs from only textures. This format is deprecated, and is prioritized only when the "Force Unicode Font" option is turned on. It acts as a "fallback" for glyphs that no other provider has defined a texture for.

It uses a system of templates to create and add high amounts of characters. Templates are name-based, and are all PNG files. Each template file must have equal width and height. The template numbering scheme works based off of the Unicode BMP. The number used is equal to a BMP codepoint's high byte.[c][d] These template textures are called "pages". Template page "22" must cover characters U+2200 to U+22FF. Page numbers go from 00 to FF. Characters beyond U+FFFF cannot be changed through this provider. By default, each glyph is 16×16 pixels wide, so each individual template page is 256×256 pixels (16 glyphs on each line, 16 lines). Its default textures are an outdated version of GNU Unifont.[3]

The template field is a string that references a set of files. The string %s must be included in this field. %s is replaced with every valid page number, in hexadecimal. 

The sizes field references a binary resource that contains the widths of each glyph. Most often, this file is called glyph_sizes.bin; this is its default name.
Each character width is one byte large. The high nibble[e] records the starting position, while the lower nibble records the ending position in the 16×16 glyph grid. For this reason, the file must be 0xFFFF bytes long (65535 in decimal).
A specific character's width is determined by finding its codepoints byte. The character 'A' has a codepoint of U+0041, so byte offset 0x41 (65 in decimal) would be addressed. A square character occupying the entire grid (pixel width #1 [0, 0x0] through #16 [15, 0xF]) would have a value of 0x0F (15 in decimal).
Widths cannot extend past 16 pixels, and characters whose codepoints are greater than U+FFFF are not handled. 

Some codepoints are invalid on their own. These are the surrogate pairs; they are used to encode codepoints higher than U+FFFF in UTF-8.
This means that the template pages D8 D9 DA DB DC DD DE DF are invalid and cannot be used. 

It was removed in 23w17a.

