## Data values
### ID
Java Edition:

| Name  | Identifier | Form         | Block tags                       | Translation key      |
|-------|------------|--------------|----------------------------------|----------------------|
| Vines | vine       | Block & Item | climbablelush_plants_replaceable | block.minecraft.vine |

Bedrock Edition:

| Name  | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key |
|-------|------------|------------|----------------------------|----------------|-----------------|
| Vines | vine       | 106        | Block & Giveable Item[i 2] | Identical[i 3] | tile.vine.name  |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


### Block states
See also: Block state

Java Edition:

| Name  | Default value | Allowed values | Description                                          |
|-------|---------------|----------------|------------------------------------------------------|
| east  | false         | falsetrue      | When true, a vine texture is displayed on the east.  |
| north | false         | falsetrue      | When true, a vine texture is displayed on the north. |
| south | false         | falsetrue      | When true, a vine texture is displayed on the south. |
| up    | false         | falsetrue      | When true, a vine texture is displayed on the top.   |
| west  | false         | falsetrue      | When true, a vine texture is displayed on the west.  |

Bedrock Edition:

| Name                | Metadata Bits | Default value | Allowed values         | Values forMetadata Bits | Description                                                                                                                                                                                                                                                           |
|---------------------|---------------|---------------|------------------------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| vine_direction_bits | 0x10x20x40x8  | 0             | 0123456789101112131415 | 0123456789101112131415  | The directions the vine exists, excluding up. Each bit determines one direction:0x1: Vines at the south 0x2: Vines at the west 0x4: Vines at the north 0x8: Vines at the eastNote: Vines gain the ceiling vines if there's a block above, block state doesn't change. |




