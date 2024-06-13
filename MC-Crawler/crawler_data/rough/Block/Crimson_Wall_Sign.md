# Sign
A sign is a non-solid block that can display text, and can be placed on the top or side of other blocks. The text of signs can be customized with dyes and glow ink sacs, and they can be waxed to prevent edits.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Chest loot
	- 1.4 Crafting
- 2 Usage
	- 2.1 Placement
	- 2.2 Text
	- 2.3 Interaction
	- 2.4 Fuel
	- 2.5 Note blocks
- 3 Sounds
	- 3.1 Generic
		- 3.1.1 Normal wood
		- 3.1.2 Cherry wood
		- 3.1.3 Bamboo wood
		- 3.1.4 Nether wood
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
	- 4.3 Block data
- 5 Achievements
- 6 Advancements
- 7 History
- 8 Gallery
	- 8.1 Renders
		- 8.1.1 Block
		- 8.1.2 Item
	- 8.2 Screenshots
- 9 Issues
- 10 See also
- 11 References
- 12 External links

## Obtaining
### Breaking
Signs can be broken with any tool or without a tool, but an axe is fastest.

| Block     | Sign                  |
|-----------|-----------------------|
| Hardness  | 1                     |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 1.5                   |
| Wooden    | 0.75                  |
| Stone     | 0.4                   |
| Iron      | 0.25                  |
| Diamond   | 0.2                   |
| Netherite | 0.2                   |
| Golden    | 0.15                  |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

A sign also breaks and drops itself as an item if the block the sign is attached to is moved, removed or destroyed.

### Natural generation
An oak sign can be found in igloo basements. Spruce signs can be found in taiga village houses, as part of a chair.

### Chest loot
| Item        | Structure | Container         | Quantity | Chance          |
|-------------|-----------|-------------------|----------|-----------------|
|             |           |                   |          | Java Edition    |
| Spruce Sign | Village   | Taiga house chest | 1        | 9.7%            |
|             |           |                   |          | Bedrock Edition |
| Oak Sign    | Village   | Taiga house chest | 1        | 10.7%           |

### Crafting
| Ingredients               | Crafting recipe |
|---------------------------|-----------------|
| MatchingPlanks+<br/>Stick | 33333333333     |

## Usage
Signs can be used to display text; they can be used to label storage, display information to other players or note areas of interest. Signs are also not destroyed by water or lava and therefore may be used to control the flow of these fluids.

### Placement
Signs may be placed on the top or side of other blocks (including semi-solid and non-solid blocks such as fences, trapdoors and other signs). To place a sign, use a sign item while pointing at the block the sign should be attached to, enter the desired text (or none), and click the "Done" button or press "escape" on a keyboard (or press × in Bedrock Edition,  on an Xbox controller,  on a PlayStation controller, or  on a Nintendo Switch controller. Closing the virtual keyboard on a mobile device also exits the typing menu). To place a sign on a block that can be interacted with by the use control (for example, chests, note blocks, etc.), sneak while placing the sign.

Signs on the top of a block stand on a short post and face toward the player who placed it, in any of 16 different directions. Signs placed on the side of a block simply float there, even if the block doesn't make contact with the sign.

Even if placed on a vertical surface, a sign may not co-exist in the same block of air as any other item, despite not necessarily visibly obstructing eachother.

For more information about the blocks signs can be placed on, see Opacity/Placement.

### Text
Oak Sign editing.
Placing a sign opens an editor interface resembling a magnified view of the sign. Up to four lines of text can then be entered using a keyboard (hardware or on-screen). The editor supports limited editing, including moving the cursor and inserting and deleting characters. In Bedrock Edition, formatting codes can also be used to apply decorative effects such as color, bold, italic and underline to various bits of the text. Depending on the edition and platform in use, copy and paste operations may be supported and the editor may also support keyboard entry of Alt-codes for displaying Unicode characters.

Text can be added to the back side of a sign by interacting with that side of the sign after placing it and editing the front.

Signs can be waxed by using a honeycomb on it. Once waxed, a sign cannot be unwaxed or edited.

After placing and affixing text on a sign, a player can change the text color by using a dye on it. When colored with dye, the text color may differ from any color specified by formatting codes. These values are hard-coded in the game's code, each dye color maps to one of these. The dye color on the sign's face is applied to all 4 lines of text. Any text that has been colored with JSON Text formatting overwrites this color. Effectively making the 'dye' color be used as a base color for any unstyled text.

Oak sign with glow ink and orange dye applied in Java Edition.
A player can use a glow ink sac on a sign to make its text glow. The glowing text is not affected by lighting. The player can use a regular black ink sac on the sign to remove the glowing effect.

| Name       | Main color | Edge color |
|------------|------------|------------|
| Black      | #000000    | #F0EBCC    |
| Red        | #FF0000    | #660000    |
| Green      | #00FF00    | #006600    |
| Brown      | #8B4513    | #371B07    |
| Blue       | #0000FF    | #000066    |
| Purple     | #A020F0    | #400C60    |
| Cyan       | #00FFFF    | #006666    |
| Light gray | #D3D3D3    | #545454    |
| Gray       | #808080    | #333333    |
| Pink       | #FF69B4    | #662A48    |
| Lime       | #BFFF00    | #4C6600    |
| Yellow     | #FFFF00    | #666600    |
| Light blue | #9AC0CD    | #3D4C52    |
| Magenta    | #FF00FF    | #660066    |
| Orange     | #FF681F    | #66290C    |
| White      | #FFFFFF    | #666666    |

In Creative mode, the combination Ctrl + pick block on Windows/Linux, or ⌘ Cmd + pick block on macOS, can be used to copy an already-placed sign, including its text (with decorations), into the player's inventory.

A dyed sign facing east or west has text that appears more saturated and bright than a sign facing north or south. However, it is actually the sign that is dimmer, because Minecraft's lighting engine uses side lighting to make the world appear less flat, but the text on signs is not affected by this.

In Bedrock Edition, inappropriate words or phrases in a sign's text are displayed as hashtags.

In Java Edition, signs can be created with JSON text, which allows complex formatting (colors, bold, italic, etc.), hover and click events, localized translation (for Minecraft technical terms, like "Redstone Repeater", otherwise translations must be provided in language files in resource packs), and the incorporation of scoreboard values into text. Use the /data merge block command to create or alter JSON signs.

Example:/data merge block ~ ~1 ~ {front_text: {color: "green", messages: ['{"selector": "@p", "bold": false, "italic": false, "underlined": false, "strikethrough": false, "obfuscated": false, "text": "First Line"}', '"Second Line"', '""', '""']}}
Signs can post the success count of JSON text hover and click events to scoreboard objectives. The objectives to be used can be specified by running the /execute store command or by modifying the sign's NBT data directly with the /data merge block command.

### Interaction
Signs can be edited after being placed by using them, which opens the edit sign message GUI.

Signs are destroyed and drop as an item when pushed by a piston.‌[Bedrock Edition  only]

Signs are non-solid and have no collision, so items and mobs can move through sign blocks. Other blocks (including other signs) can be placed on any edge of a sign.

Water and lava flow around signs. Lava can create fire in air blocks next to signs as if the signs were flammable, but the signs do not burn (and cannot be burned by other methods either, except in Bedrock Edition).

### Fuel
Overworld signs can be used as a fuel in furnaces, smelting an item per sign. Nether signs (crimson and warped), cannot be used as fuel in a furnace.

### Note blocks
Signs can be placed under note blocks to produce a "bass" sound.

## Data values
### ID
Java Edition:

| Name               | Identifier           | Form         | Block tags                                            | Item tags                        | Translation key                      |
|--------------------|----------------------|--------------|-------------------------------------------------------|----------------------------------|--------------------------------------|
| Oak Sign           | `oak_sign`           | Block & Item | `signs`<br/>`standing_signs`<br/>`wall_post_override` | `signs`                          | `block.minecraft.oak_sign`           |
| Spruce Sign        | `spruce_sign`        | Block & Item | `signs`<br/>`standing_signs`<br/>`wall_post_override` | `signs`                          | `block.minecraft.spruce_sign`        |
| Birch Sign         | `birch_sign`         | Block & Item | `signs`<br/>`standing_signs`<br/>`wall_post_override` | `signs`                          | `block.minecraft.birch_sign`         |
| Jungle Sign        | `jungle_sign`        | Block & Item | `signs`<br/>`standing_signs`<br/>`wall_post_override` | `signs`                          | `block.minecraft.jungle_sign`        |
| Acacia Sign        | `acacia_sign`        | Block & Item | `signs`<br/>`standing_signs`<br/>`wall_post_override` | `signs`                          | `block.minecraft.acacia_sign`        |
| Dark Oak Sign      | `dark_oak_sign`      | Block & Item | `signs`<br/>`standing_signs`<br/>`wall_post_override` | `signs`                          | `block.minecraft.dark_oak_sign`      |
| Mangrove Sign      | `mangrove_sign`      | Block & Item | `signs`<br/>`standing_signs`<br/>`wall_post_override` | `signs`                          | `block.minecraft.mangrove_sign`      |
| Cherry Sign        | `cherry_sign`        | Block & Item | `signs`<br/>`standing_signs`<br/>`wall_post_override` | `signs`                          | `block.minecraft.cherry_sign`        |
| Bamboo Sign        | `bamboo_sign`        | Block & Item | `signs`<br/>`standing_signs`<br/>`wall_post_override` | `signs`                          | `block.minecraft.bamboo_sign`        |
| Crimson Sign       | `crimson_sign`       | Block & Item | `signs`<br/>`standing_signs`<br/>`wall_post_override` | `non_flammable_wood`<br/>`signs` | `block.minecraft.crimson_sign`       |
| Warped Sign        | `warped_sign`        | Block & Item | `signs`<br/>`standing_signs`<br/>`wall_post_override` | `non_flammable_wood`<br/>`signs` | `block.minecraft.warped_sign`        |
| Oak Wall Sign      | `oak_wall_sign`      | Block        | `signs`<br/>`wall_signs`                              | —                                | `block.minecraft.oak_wall_sign`      |
| Spruce Wall Sign   | `spruce_wall_sign`   | Block        | `signs`<br/>`wall_signs`                              | —                                | `block.minecraft.spruce_wall_sign`   |
| Birch Wall Sign    | `birch_wall_sign`    | Block        | `signs`<br/>`wall_signs`                              | —                                | `block.minecraft.birch_wall_sign`    |
| Jungle Wall Sign   | `jungle_wall_sign`   | Block        | `signs`<br/>`wall_signs`                              | —                                | `block.minecraft.jungle_wall_sign`   |
| Acacia Wall Sign   | `acacia_wall_sign`   | Block        | `signs`<br/>`wall_signs`                              | —                                | `block.minecraft.acacia_wall_sign`   |
| Dark Oak Wall Sign | `dark_oak_wall_sign` | Block        | `signs`<br/>`wall_signs`                              | —                                | `block.minecraft.dark_oak_wall_sign` |
| Mangrove Wall Sign | `mangrove_wall_sign` | Block        | `signs`<br/>`wall_signs`                              | —                                | `block.minecraft.mangrove_wall_sign` |
| Cherry Wall Sign   | `cherry_wall_sign`   | Block        | `signs`<br/>`wall_signs`                              | —                                | `block.minecraft.cherry_wall_sign`   |
| Bamboo Wall Sign   | `bamboo_wall_sign`   | Block        | `signs`<br/>`wall_signs`                              | —                                | `block.minecraft.bamboo_wall_sign`   |
| Crimson Wall Sign  | `crimson_wall_sign`  | Block        | `signs`<br/>`wall_signs`                              | —                                | `block.minecraft.crimson_wall_sign`  |
| Warped Wall Sign   | `warped_wall_sign`   | Block        | `signs`<br/>`wall_signs`                              | —                                | `block.minecraft.warped_wall_sign`   |

| Name         | Identifier |
|--------------|------------|
| Block entity | `sign`     |

Bedrock Edition:

| Sign              | Identifier               | Alias ID       | Numeric ID | Form                         | Item ID[i 1]   | Item tags        | Translation key                   |
|-------------------|--------------------------|----------------|------------|------------------------------|----------------|------------------|-----------------------------------|
| Oak standing      | `standing_sign`          | None           | `63`       | Block & Ungiveable Item[i 2] | Identical[i 3] | —                | `tile.standing_sign.name`         |
| Spruce standing   | `spruce_standing_sign`   | None           | `436`      | Block & Ungiveable Item[i 2] | Identical[i 3] | —                | `tile.spruce_standing_sign.name`  |
| Birch standing    | `birch_standing_sign`    | None           | `441`      | Block & Ungiveable Item[i 2] | Identical[i 3] | —                | `tile.birch_standing_sign.name`   |
| Jungle standing   | `jungle_standing_sign`   | None           | `443`      | Block & Ungiveable Item[i 2] | Identical[i 3] | —                | `tile.jungle_standing_sign.name`  |
| Acacia standing   | `acacia_standing_sign`   | None           | `445`      | Block & Ungiveable Item[i 2] | Identical[i 3] | —                | `tile.acacia_standing_sign.name`  |
| Dark Oak standing | `darkoak_standing_sign`  | None           | `447`      | Block & Ungiveable Item[i 2] | Identical[i 3] | —                | `tile.darkoak_standing_sign.name` |
| Mangrove standing | `mangrove_standing_sign` | None           | `-494`     | Block & Ungiveable Item[i 2] | Identical[i 3] | —                | —                                 |
| Cherry standing   | `cherry_standing_sign`   | None           | `-542`     | Block & Ungiveable Item[i 2] | Identical[i 3] | —                | —                                 |
| Bamboo standing   | `bamboo_standing_sign`   | None           | `-518`     | Block & Ungiveable Item[i 2] | Identical[i 3] | —                | —                                 |
| Crimson standing  | `crimson_standing_sign`  | None           | `505`      | Block & Ungiveable Item[i 2] | Identical[i 3] | —                | `tile.crimson_standing_sign.name` |
| Warped standing   | `warped_standing_sign`   | None           | `506`      | Block & Ungiveable Item[i 2] | Identical[i 3] | —                | `tile.warped_standing_sign.name`  |
| Oak wall          | `wall_sign`              | None           | `68`       | Block & Ungiveable Item[i 2] | Identical[i 3] | —                | —                                 |
| Spruce wall       | `spruce_wall_sign`       | None           | `437`      | Block & Ungiveable Item[i 2] | Identical[i 3] | —                | —                                 |
| Birch wall        | `birch_wall_sign`        | None           | `442`      | Block & Ungiveable Item[i 2] | Identical[i 3] | —                | —                                 |
| Jungle wall       | `jungle_wall_sign`       | None           | `444`      | Block & Ungiveable Item[i 2] | Identical[i 3] | —                | —                                 |
| Acacia wall       | `acacia_wall_sign`       | None           | `446`      | Block & Ungiveable Item[i 2] | Identical[i 3] | —                | —                                 |
| Dark Oak wall     | `darkoak_wall_sign`      | None           | `448`      | Block & Ungiveable Item[i 2] | Identical[i 3] | —                | —                                 |
| Mangrove wall     | `mangrove_wall_sign`     | None           | `-495`     | Block & Ungiveable Item[i 2] | Identical[i 3] | —                | —                                 |
| Cherry wall       | `cherry_wall_sign`       | None           | `-544`     | Block & Ungiveable Item[i 2] | Identical[i 3] | —                | —                                 |
| Bamboo wall       | `bamboo_wall_sign`       | None           | `-519`     | Block & Ungiveable Item[i 2] | Identical[i 3] | —                | —                                 |
| Crimson wall      | `crimson_wall_sign`      | None           | `507`      | Block & Ungiveable Item[i 2] | Identical[i 3] | —                | `tile.crimson_wall_sign.name`     |
| Warped wall       | `warped_wall_sign`       | None           | `508`      | Block & Ungiveable Item[i 2] | Identical[i 3] | —                | `tile.warped_wall_sign.name`      |
| Oak item          | `oak_sign`               | `sign`         | `360`      | Item                         | —              | `minecraft:sign` | `item.sign.name`                  |
| Spruce item       | `spruce_sign`            | None           | `576`      | Item                         | —              | `minecraft:sign` | `item.spruce_sign.name`           |
| Birch item        | `birch_sign`             | None           | `577`      | Item                         | —              | `minecraft:sign` | `item.birch_sign.name`            |
| Jungle item       | `jungle_sign`            | None           | `578`      | Item                         | —              | `minecraft:sign` | `item.jungle_sign.name`           |
| Acacia item       | `acacia_sign`            | None           | `579`      | Item                         | —              | `minecraft:sign` | `item.acacia_sign.name`           |
| Dark Oak item     | `dark_oak_sign`          | `darkoak_sign` | `587`      | Item                         | —              | `minecraft:sign` | `item.darkoak_sign.name`          |
| Mangrove item     | `mangrove_sign`          | None           | `642`      | Item                         | —              | `minecraft:sign` | `item.mangrove_sign.name`         |
| Cherry item       | `cherry_sign`            | None           | `659`      | Item                         | —              | `minecraft:sign` | `item.cherry_sign.name`           |
| Bamboo item       | `bamboo_sign`            | None           | `660`      | Item                         | —              | `minecraft:sign` | `item.bamboo_sign.name`           |
| Crimson item      | `crimson_sign`           | None           | `614`      | Item                         | —              | `minecraft:sign` | `item.crimson_sign.name`          |
| Warped item       | `warped_sign`            | None           | `615`      | Item                         | —              | `minecraft:sign` | `item.warped_sign.name`           |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑ a b c d e f g h i j k l m n o p q r s t u vUnavailable with /give command
3. ↑ a b c d e f g h i j k l m n o p q r s t u vThe block's direct item form has the same id as the block.

| Name         | Savegame ID |
|--------------|-------------|
| Block entity | `Sign`      |

### Block states
See also: Block states

Java Edition:

** Standing **
| Name        | Default value | Allowed values     | Description                                                  |
|-------------|---------------|--------------------|--------------------------------------------------------------|
| rotation    | `0`           | `0`                | The block is facing south.                                   |
|             |               | `1`                | The block is facing south-southwest.                         |
|             |               | `2`                | The block is facing southwest.                               |
|             |               | `3`                | The block is facing west-southwest.                          |
|             |               | `4`                | The block is facing west.                                    |
|             |               | `5`                | The block is facing west-northwest.                          |
|             |               | `6`                | The block is facing northwest.                               |
|             |               | `7`                | The block is facing north-northwest.                         |
|             |               | `8`                | The block is facing north.                                   |
|             |               | `9`                | The block is facing north-northeast.                         |
|             |               | `10`               | The block is facing northeast.                               |
|             |               | `11`               | The block is facing east-northeast.                          |
|             |               | `12`               | The block is facing east.                                    |
|             |               | `13`               | The block is facing east-southeast.                          |
|             |               | `14`               | The block is facing southeast.                               |
|             |               | `15`               | The block is facing south-southeast.                         |
| waterlogged | `false`       | `false`<br/>`true` | Whether or not there's water in the same place as this sign. |

** Wall **
| Name        | Default value | Allowed values                            | Description                                                                                                                                                                    |
|-------------|---------------|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing      | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the block is facing. For example, a block facing east is attached to a block to its west.<br/>Opposite from the direction a player faces when placing the block. |
| waterlogged | `false`       | `false`<br/>`true`                        | Whether or not there's water in the same place as this sign.                                                                                                                   |

Bedrock Edition:

** Standing **
| Name                  | Metadata Bits                       | Default value | Allowed values | Values forMetadata Bits | Description                          |
|-----------------------|-------------------------------------|---------------|----------------|-------------------------|--------------------------------------|
| ground_sign_direction | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8` | `0`           | `0`            | `0`                     | The block is facing south.           |
|                       |                                     |               | `1`            | `1`                     | The block is facing south-southwest. |
|                       |                                     |               | `2`            | `2`                     | The block is facing southwest.       |
|                       |                                     |               | `3`            | `3`                     | The block is facing west-southwest.  |
|                       |                                     |               | `4`            | `4`                     | The block is facing west.            |
|                       |                                     |               | `5`            | `5`                     | The block is facing west-northwest.  |
|                       |                                     |               | `6`            | `6`                     | The block is facing northwest.       |
|                       |                                     |               | `7`            | `7`                     | The block is facing north-northwest. |
|                       |                                     |               | `8`            | `8`                     | The block is facing north.           |
|                       |                                     |               | `9`            | `9`                     | The block is facing north-northeast. |
|                       |                                     |               | `10`           | `10`                    | The block is facing northeast.       |
|                       |                                     |               | `11`           | `11`                    | The block is facing east-northeast.  |
|                       |                                     |               | `12`           | `12`                    | The block is facing east.            |
|                       |                                     |               | `13`           | `13`                    | The block is facing east-southeast.  |
|                       |                                     |               | `14`           | `14`                    | The block is facing southeast.       |
|                       |                                     |               | `15`           | `15`                    | The block is facing south-southeast. |

** Wall **
| Name             | Metadata Bits             | Default value | Allowed values              | Values forMetadata Bits     | Description                                                                                                                                               |
|------------------|---------------------------|---------------|-----------------------------|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing_direction | `0x1`<br/>`0x2`<br/>`0x4` | `2`           | `2`<br/>`3`<br/>`4`<br/>`5` | `2`<br/>`3`<br/>`4`<br/>`5` | The direction the block is facing. For example, a block facing east is attached to a block to its west.2: north<br/>3: south<br/>4: west<br/>5: east<br/> |
|                  |                           |               | `0`<br/>`1`                 | `0`<br/>`1`                 | Unused                                                                                                                                                    |



### Block data
A sign has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format

- Block entity data
	- 
	- Tags common to all block entities
	- is_waxed: 1 or 0 (true/false) - true if the text is locked withhoneycomb.
	- front_text: A compound that discribes front text.
		- has_glowing_text: 1 or 0 (true/false) - true if the sign has been dyed with aglow ink sac.
		- color: The color that has been used to dye the sign. The default value isblackOne ofwhite,orange,magenta,light_blue,yellow,lime,pink,gray,light_gray,cyan,purple,blue,brown,green,red, andblack.
		- filtered_messages: Only inRealms. The lines of text shown to players with the profanity filter turned on instead of the regular lines. This tag is automatically set to""for lines containing blocked words and to the line's normal contents for the other lines when a player with the profanity filter turnedoffedits the sign, so players with the filteroncannot see the blocked words. If a player with the filterontries to use blocked words in one or more lines, the line(s) inmessagescontaining blocked words are set to"", which makes them render completely blank, and this tag is also given the same contents. If multiple lines have been edited before the sign editing GUI is closed, only the lines containing blocked words are blanked.
		- messages: A list of text for each line.
			- : Text for each line. Must beRaw JSON text format. The character limit for the Text tags depends on the width of the characters.
	- back_text: A compound that discribes back text.
		- The same structure asfront_text.


Before 1.20:


 Block entity data
Tags common to all block entities
 GlowingText: 1 or 0 (true/false) - true if the sign has been dyed with a glow ink sac.
 Color: The color that has been used to dye the sign. The default value is "black". One of "white", "orange", "magenta", "light_blue", "yellow", "lime", "pink", "gray", "light_gray", "cyan", "purple", "blue", "brown", "green", "red", or "black".
 Text1: First row of text.
 Text2: Second row of text.
 Text3: Third row of text.
 Text4: Fourth row of text.



Bedrock Edition:

SeeBedrock Edition level format/Block entity format.
