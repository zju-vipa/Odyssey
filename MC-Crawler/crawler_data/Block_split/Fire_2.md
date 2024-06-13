### Eternal fire
When lit, netherrack and magma blocks maintain fire forever, unless extinguished by any method except rain. Bedrock in the End also burns eternally. Eternal fire cannot exist on the sides of these blocks.

The blocks that can support eternal fire are defined per-dimension, in the #infiniburn_overworld, #infiniburn_nether, and #infiniburn_end block tags.

If /gamerule doFireTick is false, fire lasts forever until it is put out by the player, and does not spread or affect flammable blocks.

### Bees
Setting fire to a beehive or bee nest causes the contained bees to be ejected from the block.

## Data values
### ID
Java Edition:

| Name | Identifier | Form  | Block tags | Translation key      |
|------|------------|-------|------------|----------------------|
| Fire | fire       | Block | fire       | block.minecraft.fire |

Bedrock Edition:

| Name | Identifier | Numeric ID | Form                         | Item ID[i 1]   | Translation key |
|------|------------|------------|------------------------------|----------------|-----------------|
| Fire | fire       | 51         | Block & Ungiveable Item[i 2] | Identical[i 3] | tile.fire.name  |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Unavailable with /give command

↑ The block's direct item form has the same id as the block.


### Block states
See also: Block states

Java Edition:
Fire:

| Name  | Default value | Allowed values         | Description                                                                                                                              |
|-------|---------------|------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| age   | 0             | 0123456789101112131415 | Newly placed fire has an age of 0, and has a1⁄3chance of incrementing with eachblock tick.This factor affects how the fire extinguishes. |
| east  | false         | falsetrue              | When true, fire texture shows on that face of the block to the east; false if there's a block below this fire.                           |
| north | false         | falsetrue              | When true, fire texture shows on that face of the block to the north; false if there's a block below this fire.                          |
| south | false         | falsetrue              | When true, fire texture shows on that face of the block to the south; false if there's a block below this fire.                          |
| up    | false         | falsetrue              | When true, fire texture shows on that face of the block above; false if there's a block below this fire.                                 |
| west  | false         | falsetrue              | When true, fire texture shows on that face of the block to the west; false if there's a block below this fire.                           |

Bedrock Edition:
Fire and Soul Fire:

| Name | Metadata Bits | Default value | Allowed values         | Values forMetadata Bits | Description                                                                      |
|------|---------------|---------------|------------------------|-------------------------|----------------------------------------------------------------------------------|
| age  | 0x10x20x40x8  | 0             | 0123456789101112131415 | 0123456789101112131415  | Newly placed fire has an age of 0.This factor affects how the fire extinguishes. |




