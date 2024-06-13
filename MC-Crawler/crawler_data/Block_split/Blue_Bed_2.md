### Bouncing
Falling onto a bed bounces the player with 66% strength – the bouncing-up velocity is 66% of the impact velocity. The player also takes 50% of normal fall damage.

Baby villagers bounce on beds during the day.

If the player is falling while sleeping requirements are met, and presses use on a bed within reach before hitting the ground, the fall damage is delayed until the player wakes.

A player can bounce on a bed while another player or villager is sleeping on it without waking the player or the villager up.

Villagers can be pushed onto beds, as the bed is half a block tall.

### Curing
Each bed in the vicinity of a zombie villager has a chance to speed up the process of curing the zombie villager. Iron bars (such as in a prison cell) also have this effect.

### Placement
Beds require two blocks of floor space. Placement requires at least 2 blocks from the player's facing direction. When placed, the foot of the bed is placed on the block selected and the head of the bed on the block farther away from the player. In Bedrock Edition, beds require solid blocks below them when placed. However, the bed remains in place if its supporting blocks are later removed. In Java Edition, beds do not require supporting blocks and can be placed anywhere, provided there is enough room.

## Data values
### ID
Java Edition:

| Name           | Identifier     | Form         | Block tags | Item tags | Translation key                |
|----------------|----------------|--------------|------------|-----------|--------------------------------|
| White Bed      | white_bed      | Block & Item | beds       | beds      | block.minecraft.white_bed      |
| Orange Bed     | orange_bed     | Block & Item | beds       | beds      | block.minecraft.orange_bed     |
| Magenta Bed    | magenta_bed    | Block & Item | beds       | beds      | block.minecraft.magenta_bed    |
| Light Blue Bed | light_blue_bed | Block & Item | beds       | beds      | block.minecraft.light_blue_bed |
| Yellow Bed     | yellow_bed     | Block & Item | beds       | beds      | block.minecraft.yellow_bed     |
| Lime Bed       | lime_bed       | Block & Item | beds       | beds      | block.minecraft.lime_bed       |
| Pink Bed       | pink_bed       | Block & Item | beds       | beds      | block.minecraft.pink_bed       |
| Gray Bed       | gray_bed       | Block & Item | beds       | beds      | block.minecraft.gray_bed       |
| Light Gray Bed | light_gray_bed | Block & Item | beds       | beds      | block.minecraft.light_gray_bed |
| Cyan Bed       | cyan_bed       | Block & Item | beds       | beds      | block.minecraft.cyan_bed       |
| Purple Bed     | purple_bed     | Block & Item | beds       | beds      | block.minecraft.purple_bed     |
| Blue Bed       | blue_bed       | Block & Item | beds       | beds      | block.minecraft.blue_bed       |
| Brown Bed      | brown_bed      | Block & Item | beds       | beds      | block.minecraft.brown_bed      |
| Green Bed      | green_bed      | Block & Item | beds       | beds      | block.minecraft.green_bed      |
| Red Bed        | red_bed        | Block & Item | beds       | beds      | block.minecraft.red_bed        |
| Black Bed      | black_bed      | Block & Item | beds       | beds      | block.minecraft.black_bed      |

| Name         | Identifier |
|--------------|------------|
| Block entity | bed        |

Bedrock Edition:

| Bed   | Identifier | Numeric ID | Form                         | Item ID[i 1] | Translation key                                                                                                                                                                                                                                                                                 |
|-------|------------|------------|------------------------------|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Block | bed        | 26         | Block & Ungiveable Item[i 2] | item.bed     | tile.bed.name                                                                                                                                                                                                                                                                                   |
| Item  | bed        | 418        | Item                         | —            | item.bed.black.nameitem.bed.red.nameitem.bed.green.nameitem.bed.brown.nameitem.bed.blue.nameitem.bed.cyan.nameitem.bed.silver.nameitem.bed.gray.nameitem.bed.pink.nameitem.bed.lime.nameitem.bed.yellow.nameitem.bed.lightBlue.nameitem.bed.magenta.nameitem.bed.orange.nameitem.bed.white.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Unavailable with /give command


| Name         | Savegame ID |
|--------------|-------------|
| Block entity | Bed         |

### Metadata
See also: Data values

In Bedrock Edition, bed items use the following data values:

|  | DV | Description    |
|--|----|----------------|
|  | 0  | White Bed      |
|  | 1  | Orange Bed     |
|  | 2  | Magenta Bed    |
|  | 3  | Light Blue Bed |
|  | 4  | Yellow Bed     |
|  | 5  | Lime Bed       |
|  | 6  | Pink Bed       |
|  | 7  | Gray Bed       |
|  | 8  | Light Gray Bed |
|  | 9  | Cyan Bed       |
|  | 10 | Purple Bed     |
|  | 11 | Blue Bed       |
|  | 12 | Brown Bed      |
|  | 13 | Green Bed      |
|  | 14 | Red Bed        |
|  | 15 | Black Bed      |

### Block states
See also: Block states

Java Edition:

| Name     | Default value | Allowed values     | Description                                                                                             |
|----------|---------------|--------------------|---------------------------------------------------------------------------------------------------------|
| facing   | north         | eastnorthsouthwest | The direction the head of the bed is pointing.The same direction the player faces when placing the bed. |
| occupied | false         | falsetrue          | True when a player or villager is using the bed.                                                        |
| part     | foot          | foothead           | The half of the bed in the current block.                                                               |

Bedrock Edition:

| Name           | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                                                                                                 |
|----------------|---------------|---------------|----------------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| direction      | 0x10x2        | 0             | 0123           | 0123                    | The direction the head of the bed is pointing.0:Head facing South 1:Head facing West 2:Head facing North 3:Head facing East |
| head_piece_bit | 0x8           | true          | falsetrue      | 01                      | If the current block is the head part.                                                                                      |
| occupied_bit   | 0x4           | false         | falsetrue      | 01                      | True when a player or villager is using the bed.                                                                            |



