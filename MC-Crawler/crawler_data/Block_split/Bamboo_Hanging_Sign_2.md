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
: Text for each line. Must be Raw JSON text format.
 back_text: A compound that discribes back text.　The same structure as  front_text.

The character limit for the Text tags depends on the width of the characters. Although the Text tags are string objects, they should contain JSON text, which are evaluated as compound objects. 

Bedrock Edition:

See Bedrock Edition level format/Block entity format.
## See also
- Chalkboard
- Sign


