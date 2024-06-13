### Curing
Each bed in the vicinity of a zombie villager has a chance to speed up the process of curing the zombie villager. Iron bars (such as in a prison cell) also have this effect.

### Placement
Beds require two blocks of floor space. Placement requires at least 2 blocks from the player's facing direction. When placed, the foot of the bed is placed on the block selected and the head of the bed on the block farther away from the player. In Bedrock Edition, beds require solid blocks below them when placed. However, the bed remains in place if its supporting blocks are later removed. In Java Edition, beds do not require supporting blocks and can be placed anywhere, provided there is enough room.

## Data values
### ID
Java Edition:

| Name           | Identifier       | Form         | Block tags | Item tags | Translation key                  |
|----------------|------------------|--------------|------------|-----------|----------------------------------|
| White Bed      | `white_bed`      | Block & Item | `beds`     | `beds`    | `block.minecraft.white_bed`      |
| Orange Bed     | `orange_bed`     | Block & Item | `beds`     | `beds`    | `block.minecraft.orange_bed`     |
| Magenta Bed    | `magenta_bed`    | Block & Item | `beds`     | `beds`    | `block.minecraft.magenta_bed`    |
| Light Blue Bed | `light_blue_bed` | Block & Item | `beds`     | `beds`    | `block.minecraft.light_blue_bed` |
| Yellow Bed     | `yellow_bed`     | Block & Item | `beds`     | `beds`    | `block.minecraft.yellow_bed`     |
| Lime Bed       | `lime_bed`       | Block & Item | `beds`     | `beds`    | `block.minecraft.lime_bed`       |
| Pink Bed       | `pink_bed`       | Block & Item | `beds`     | `beds`    | `block.minecraft.pink_bed`       |
| Gray Bed       | `gray_bed`       | Block & Item | `beds`     | `beds`    | `block.minecraft.gray_bed`       |
| Light Gray Bed | `light_gray_bed` | Block & Item | `beds`     | `beds`    | `block.minecraft.light_gray_bed` |
| Cyan Bed       | `cyan_bed`       | Block & Item | `beds`     | `beds`    | `block.minecraft.cyan_bed`       |
| Purple Bed     | `purple_bed`     | Block & Item | `beds`     | `beds`    | `block.minecraft.purple_bed`     |
| Blue Bed       | `blue_bed`       | Block & Item | `beds`     | `beds`    | `block.minecraft.blue_bed`       |
| Brown Bed      | `brown_bed`      | Block & Item | `beds`     | `beds`    | `block.minecraft.brown_bed`      |
| Green Bed      | `green_bed`      | Block & Item | `beds`     | `beds`    | `block.minecraft.green_bed`      |
| Red Bed        | `red_bed`        | Block & Item | `beds`     | `beds`    | `block.minecraft.red_bed`        |
| Black Bed      | `black_bed`      | Block & Item | `beds`     | `beds`    | `block.minecraft.black_bed`      |

| Name         | Identifier |
|--------------|------------|
| Block entity | `bed`      |

Bedrock Edition:

| Bed   | Identifier | Numeric ID | Form                         | Item ID[i 1] | Translation key                                                                                                                                                                                                                                                                                                                                                                                     |
|-------|------------|------------|------------------------------|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Block | `bed`      | `26`       | Block & Ungiveable Item[i 2] | `item.bed`   | `tile.bed.name`                                                                                                                                                                                                                                                                                                                                                                                     |
| Item  | `bed`      | `418`      | Item                         | —            | `item.bed.black.name`<br/>`item.bed.red.name`<br/>`item.bed.green.name`<br/>`item.bed.brown.name`<br/>`item.bed.blue.name`<br/>`item.bed.cyan.name`<br/>`item.bed.silver.name`<br/>`item.bed.gray.name`<br/>`item.bed.pink.name`<br/>`item.bed.lime.name`<br/>`item.bed.yellow.name`<br/>`item.bed.lightBlue.name`<br/>`item.bed.magenta.name`<br/>`item.bed.orange.name`<br/>`item.bed.white.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Unavailable with /give command

| Name         | Savegame ID |
|--------------|-------------|
| Block entity | `Bed`       |

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

| Name     | Default value | Allowed values                            | Description                                                                                                  |
|----------|---------------|-------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| facing   | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the head of the bed is pointing.<br/>The same direction the player faces when placing the bed. |
| occupied | `false`       | `false`<br/>`true`                        | True when a player or villager is using the bed.                                                             |
| part     | `foot`        | `foot`<br/>`head`                         | The half of the bed in the current block.                                                                    |

Bedrock Edition:

| Name           | Metadata Bits   | Default value | Allowed values              | Values forMetadata Bits     | Description                                                                                                                                  |
|----------------|-----------------|---------------|-----------------------------|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| direction      | `0x1`<br/>`0x2` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3` | `0`<br/>`1`<br/>`2`<br/>`3` | The direction the head of the bed is pointing.0:Head facing South<br/>1:Head facing West<br/>2:Head facing North<br/>3:Head facing East<br/> |
| head_piece_bit | `0x8`           | `true`        | `false`<br/>`true`          | `0`<br/>`1`                 | If the current block is the head part.                                                                                                       |
| occupied_bit   | `0x4`           | `false`       | `false`<br/>`true`          | `0`<br/>`1`                 | True when a player or villager is using the bed.                                                                                             |



