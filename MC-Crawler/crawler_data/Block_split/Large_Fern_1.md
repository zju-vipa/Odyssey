## Data values
### ID
Java Edition:

| Name       | Identifier | Form         | Block tags | Translation key            |
|------------|------------|--------------|------------|----------------------------|
| Large Fern | large_fern | Block & Item | None       | block.minecraft.large_fern |

Bedrock Edition:

| Name       | Identifier   | Numeric ID | Form                       | Item ID[i 1]   | Translation key             |
|------------|--------------|------------|----------------------------|----------------|-----------------------------|
| Large Fern | double_plant | 175        | Block & Giveable Item[i 2] | Identical[i 3] | tile.double_plant.fern.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


### Block states
See also: Block states

Java Edition:
Tall grass and large fern

| Name | Default value | Allowed values | Description                                    |
|------|---------------|----------------|------------------------------------------------|
| half | lower         | lowerupper     | The half of the plant contained in this block. |

Bedrock Edition:
Tall grass and large fern

| Name              | Metadata Bits | Default value | Allowed values                       | Values forMetadata Bits | Description                                               |
|-------------------|---------------|---------------|--------------------------------------|-------------------------|-----------------------------------------------------------|
| double_plant_type | 0x10x20x4     | sunflower     | sunflowersyringagrassfernrosepaeonia | 012345                  | The flower type.                                          |
| upper_block_bit   | 0x8           | false         | falsetrue                            | 01                      | If it is the upper half of the plant. For items, it is 0. |



## See also
- Shrub


