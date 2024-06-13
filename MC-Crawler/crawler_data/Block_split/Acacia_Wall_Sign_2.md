### Block states
See also: Block states

Java Edition:

Standing
| Name        | Default value | Allowed values | Description                                                  |
|-------------|---------------|----------------|--------------------------------------------------------------|
| rotation    | 0             | 0              | The block is facing south.                                   |
|             |               | 1              | The block is facing south-southwest.                         |
|             |               | 2              | The block is facing southwest.                               |
|             |               | 3              | The block is facing west-southwest.                          |
|             |               | 4              | The block is facing west.                                    |
|             |               | 5              | The block is facing west-northwest.                          |
|             |               | 6              | The block is facing northwest.                               |
|             |               | 7              | The block is facing north-northwest.                         |
|             |               | 8              | The block is facing north.                                   |
|             |               | 9              | The block is facing north-northeast.                         |
|             |               | 10             | The block is facing northeast.                               |
|             |               | 11             | The block is facing east-northeast.                          |
|             |               | 12             | The block is facing east.                                    |
|             |               | 13             | The block is facing east-southeast.                          |
|             |               | 14             | The block is facing southeast.                               |
|             |               | 15             | The block is facing south-southeast.                         |
| waterlogged | false         | falsetrue      | Whether or not there's water in the same place as this sign. |

Wall
| Name        | Default value | Allowed values     | Description                                                                                                                                                               |
|-------------|---------------|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing      | north         | eastnorthsouthwest | The direction the block is facing. For example, a block facing east is attached to a block to its west.Opposite from the direction a player faces when placing the block. |
| waterlogged | false         | falsetrue          | Whether or not there's water in the same place as this sign.                                                                                                              |

Bedrock Edition:

Standing
| Name                  | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                          |
|-----------------------|---------------|---------------|----------------|-------------------------|--------------------------------------|
| ground_sign_direction | 0x10x20x40x8  | 0             | 0              | 0                       | The block is facing south.           |
|                       |               |               | 1              | 1                       | The block is facing south-southwest. |
|                       |               |               | 2              | 2                       | The block is facing southwest.       |
|                       |               |               | 3              | 3                       | The block is facing west-southwest.  |
|                       |               |               | 4              | 4                       | The block is facing west.            |
|                       |               |               | 5              | 5                       | The block is facing west-northwest.  |
|                       |               |               | 6              | 6                       | The block is facing northwest.       |
|                       |               |               | 7              | 7                       | The block is facing north-northwest. |
|                       |               |               | 8              | 8                       | The block is facing north.           |
|                       |               |               | 9              | 9                       | The block is facing north-northeast. |
|                       |               |               | 10             | 10                      | The block is facing northeast.       |
|                       |               |               | 11             | 11                      | The block is facing east-northeast.  |
|                       |               |               | 12             | 12                      | The block is facing east.            |
|                       |               |               | 13             | 13                      | The block is facing east-southeast.  |
|                       |               |               | 14             | 14                      | The block is facing southeast.       |
|                       |               |               | 15             | 15                      | The block is facing south-southeast. |

Wall
| Name             | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                                                                                                              |
|------------------|---------------|---------------|----------------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| facing_direction | 0x10x20x4     | 2             | 2345           | 2345                    | The direction the block is facing. For example, a block facing east is attached to a block to its west.2: north 3: south 4: west 5: east |
|                  |               |               | 01             | 01                      | Unused                                                                                                                                   |



### Block data
A sign has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format


 Block entity data
Tags common to all block entities
 is_waxed: 1 or 0 (true/false) - true if the text is locked with honeycomb.
 front_text: A compound that discribes front text.
 has_glowing_text: 1 or 0 (true/false) - true if the sign has been dyed with a glow ink sac.
 color: The color that has been used to dye the sign. The default value is black One of white, orange, magenta, light_blue, yellow, lime, pink, gray, light_gray, cyan, purple, blue, brown, green, red, and black.
 filtered_messages: Only in Realms. The lines of text shown to players with the profanity filter turned on instead of the regular lines. This tag is automatically set to "" for lines containing blocked words and to the line's normal contents for the other lines when a player with the profanity filter turned off edits the sign, so players with the filter on cannot see the blocked words. If a player with the filter on tries to use blocked words in one or more lines, the line(s) in  messages containing blocked words are set to "", which makes them render completely blank, and this tag is also given the same contents. If multiple lines have been edited before the sign editing GUI is closed, only the lines containing blocked words are blanked.
 messages: A list of text for each line.
: Text for each line. Must be Raw JSON text format. The character limit for the Text tags depends on the width of the characters.
 back_text: A compound that discribes back text.
The same structure as  front_text.


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

See Bedrock Edition level format/Block entity format.
