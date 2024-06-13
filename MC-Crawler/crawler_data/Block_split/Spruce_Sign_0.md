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


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


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
| Ingredients          | Crafting recipe |
|----------------------|-----------------|
| MatchingPlanks+Stick | 33333333333     |

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

Example: /data merge block ~ ~1 ~ {front_text: {color: "green", messages: ['{"selector": "@p", "bold": false, "italic": false, "underlined": false, "strikethrough": false, "obfuscated": false, "text": "First Line"}', '"Second Line"', '""', '""']}}
Signs can post the success count of JSON text hover and click events to scoreboard objectives. The objectives to be used can be specified by running the /execute store command or by modifying the sign's NBT data directly with the /data merge block command.

