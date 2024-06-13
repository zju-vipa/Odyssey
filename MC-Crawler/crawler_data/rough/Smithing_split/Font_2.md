### Unihex provider
The unihex provider is a replacement for the Legacy Unicode provider, introduced in 23w17a. It uses the GNU Unifont .hex format. It references a ZIP archive that contains a number of .hex files. 

The hex_file field is a resource location to a .ZIP archive file. It must be openable by Java's ZipFile. Inside, there must be at least 1 .hex file at the root of the archive. Subdirectories are not walked through and filenames with an extension different from ".hex" are ignored. Filenames must follow normal file resource name rules.
In each .hex file is 1 or more glyph definitions. A glyph definitions is 1 line only, and follows the format codepoint:data. The codepoint is the Unicode codepoint, without the U+ or 0x. It must have 4, 5, or 6 digits. The data is a hexadecimal number that encodes the glyph data. Glyphs are always 16 pixels high. Glyphs can be 8, 16, 24, or 32 pixels wide.[f]

The size_overrides field is a list of compounds that define custom widths for a range of characters. Each element in this list must be a compound. Inside of each compound are 4 fields. from is the starting character for the range at which this size override applies to. to is the ending character for this range. Both from and to must be 1 character. left is the position of the left-most column of glyphs in range. right is the position of the right-most column of glyphs in range. Both left and right cannot be less than 0 or greater than 32. 

### Reference provider
The reference provider serves one purpose: to include another provider only once. It can be used to include providers from other fonts in other resource packs.

Referenced providers are guaranteed to be loaded only once, no matter how many times they are included.

The id field is a resource location to another font file.

### Filters

  

This section describes content that may be included in Java Edition. 
This content has appeared in Java Edition 1.20.5 development versions, but the full update containing it has not been released yet.


All font providers can be selectively included depending upon toggle-able buttons in-game.

Right now, these buttons are hardcoded, preventing the extension of these font filtering capabilities beyond the preset options provided.
Two buttons exist, located in Language -> Font Settings.
They are "Force Uniform" and "Japanese Glyph Variants".

## Emoji support
Emoji and their associated items.
Minecraft has included textures for a number of emojis. The earliest emoji textures were for ☺☻.

Since 1.15, this support has expanded. Emojis are monochromatic and behave just as any other character. The game does not support modifiers, such as skin tone, joining, or emoji presentation. The skin tone modifiers U+1F3FB..U+1F3FF 🏻 🏼 🏽 🏾 🏿 do not apply colored skin tones to their applicable emojis, and instead show tones as their Unifont glyphs. Joining multiple emojis via U+200D ‍ ZERO WIDTH JOINER to create 1 single emoji is not supported; multi-sequence emoji such as 👨‍👩‍👧 instead show as 👨‌👩‌👧 with dotted boxes showing ZWJ between them. Variation selectors, which control presentation, are displayed as dotted boxes with VSnumber.

As of 1.20.2, Minecraft has support for 43 emoji.


List of characters (unordered):
☀ ☁ ☂ ☃ ☄ ☑ ☔ ☠ ☮ ☯ ☹ ☺ ♀ ♂ ♠ ♣ ♥ ♦ ⚓ ⚔ ⚗ ⚠ ⚡ ⛄ ⛈ ⛏ ✉ ✔ ❣ ❄ 🔥 🌊 🗡 🏹 🪓 🔱 🎣 🧪 ✂ 🍖 🪣 🔔 ⏳



Bedrock Edition does not support any character above U+FFFF, which includes many modern emoji. It does not include any textures for emojis below that either; only those provided by GNU Unifont below U+FFFF are included and visible.

## Special characters
In Java Edition, there are 2 characters that are accessible only through technical means.
The first is U+FFFD � REPLACEMENT CHARACTER, which appears when either the U+FFFD character is typed, or there is an invalid UTF-8 multi-byte sequence.
The second is the "notdef" character,[g] seen when a character that has no texture in the currently-used font is typed. It is hardcoded and cannot be modified through resource packs. It is sometimes called "tofu" in the typographical community because of its similarity in shape to a block of tofu.

In Bedrock Edition, a character with no texture data appears as a blank space. The U+FFFD � REPLACEMENT CHARACTER shown belongs to GNU Unifont.

## Bold text

  

This section of the article is empty. 
You can help by adding to it.


## Experience bar text

  

This section of the article is empty. 
You can help by adding to it.


## Shadow
In most places text is rendered, a shadow appears beneath every character.
This shadow is a copy of the character's glyph, with the red, green, and blue values divided by 4 and positioned 12.5% south-east of the character, relative to its spacing.
Regardless of the resolution of the character's texture, the shadow is always moved by 12.5%.
In the default font (assets/minecraft/textures/font/ascii.png), the shadow position is moved 1 pixel down and to the right.

For pixels where the glyph overlaps with the shadow, the above glyph's channels have 1 subtracted from them. For example, in areas where a white (#FFFFFF) glyph's pixel overlaps a shadow's, the white pixel becomes #FEFEFE.

