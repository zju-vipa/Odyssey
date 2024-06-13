# Potato Hanging Sign
A potato hanging sign is a variant of a hanging sign made of potato planks in 24w14potato.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Crafting
- 2 Usage
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
	- 4.3 Block data
- 5 History

## Obtaining
### Breaking
| Block     | Potato Hanging Sign   |
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

### Crafting
| Ingredients            | Crafting recipe |
|------------------------|-----------------|
| Chain+<br/>Potato Stem |                 |

## Usage
For information about all hanging signs, see Hanging Sign § Usage.

## Data values
### ID
| Name                                                                                                                | Identifier                 | Block tags                                                                         | Translation key                            |
|---------------------------------------------------------------------------------------------------------------------|----------------------------|------------------------------------------------------------------------------------|--------------------------------------------|
| Potato Hanging Sign                                                                                                 | `potato_hanging_sign`      | `all_signs`<br/>`ceiling_hanging_signs`<br/>`mineable/axe`<br/>`all_hanging_signs` | `block.minecraft.potato_hanging_sign`      |
| BlockSprite potato-wall-hanging-sign.png: Sprite image for potato-wall-hanging-sign in MinecraftPotato Hanging Sign | `potato_wall_hanging_sign` | `all_signs`<br/>`mineable/axe`<br/>`wall_hanging_signs`<br/>`all_hanging_signs`    | `block.minecraft.potato_wall_hanging_sign` |

### Block states
See also: Block states

** Hanging **
| Name        | Default value | Allowed values     | Description                                                                                   |
|-------------|---------------|--------------------|-----------------------------------------------------------------------------------------------|
| attached    | `false`       | `false`<br/>`true` | Whether or not this hanging sign's chains are connected to the same point on the block above. |
| rotation    | `0`           | `0`                | The block is facing south.                                                                    |
|             |               | `1`                | The block is facing south-southwest.                                                          |
|             |               | `2`                | The block is facing southwest.                                                                |
|             |               | `3`                | The block is facing west-southwest.                                                           |
|             |               | `4`                | The block is facing west.                                                                     |
|             |               | `5`                | The block is facing west-northwest.                                                           |
|             |               | `6`                | The block is facing northwest.                                                                |
|             |               | `7`                | The block is facing north-northwest.                                                          |
|             |               | `8`                | The block is facing north.                                                                    |
|             |               | `9`                | The block is facing north-northeast.                                                          |
|             |               | `10`               | The block is facing northeast.                                                                |
|             |               | `11`               | The block is facing east-northeast.                                                           |
|             |               | `12`               | The block is facing east.                                                                     |
|             |               | `13`               | The block is facing east-southeast.                                                           |
|             |               | `14`               | The block is facing southeast.                                                                |
|             |               | `15`               | The block is facing south-southeast.                                                          |
| waterlogged | `false`       | `false`<br/>`true` | Whether or not there's water in the same place as this hanging sign.                          |

** Wall **
| Name        | Default value | Allowed values                            | Description                                                          |
|-------------|---------------|-------------------------------------------|----------------------------------------------------------------------|
| facing      | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the block is facing.                                   |
| waterlogged | `false`       | `false`<br/>`true`                        | Whether or not there's water in the same place as this hanging sign. |

### Block data
A potato hanging sign has a block entity associated with it that holds additional data about the block.

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


