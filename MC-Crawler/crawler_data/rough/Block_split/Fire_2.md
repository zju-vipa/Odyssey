### Eternal fire
When lit, netherrack and magma blocks maintain fire forever, unless extinguished by any method except rain. Bedrock in the End also burns eternally. Eternal fire cannot exist on the sides of these blocks.

The blocks that can support eternal fire are defined per-dimension, in the #infiniburn_overworld, #infiniburn_nether, and #infiniburn_end block tags.

If /gamerule doFireTick is false, fire lasts forever until it is put out by the player, and does not spread or affect flammable blocks.

### Bees
Setting fire to a beehive or bee nest causes the contained bees to be ejected from the block.

## Data values
### ID
Java Edition:

| Name | Identifier | Form  | Block tags | Translation key        |
|------|------------|-------|------------|------------------------|
| Fire | `fire`     | Block | `fire`     | `block.minecraft.fire` |

Bedrock Edition:

| Name | Identifier | Numeric ID | Form                         | Item ID[i 1]   | Translation key  |
|------|------------|------------|------------------------------|----------------|------------------|
| Fire | `fire`     | `51`       | Block & Ungiveable Item[i 2] | Identical[i 3] | `tile.fire.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Unavailable with /give command
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

Java Edition:
Fire:

| Name  | Default value | Allowed values                                                                                                                    | Description                                                                                                                                             |
|-------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| age   | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | $Newly placed fire has an age of 0, and has a\frac{1}{3}$chance of incrementing with eachblock tick.<br/>This factor affects how the fire extinguishes. |
| east  | `false`       | `false`<br/>`true`                                                                                                                | When true, fire texture shows on that face of the block to the east; false if there's a block below this fire.                                          |
| north | `false`       | `false`<br/>`true`                                                                                                                | When true, fire texture shows on that face of the block to the north; false if there's a block below this fire.                                         |
| south | `false`       | `false`<br/>`true`                                                                                                                | When true, fire texture shows on that face of the block to the south; false if there's a block below this fire.                                         |
| up    | `false`       | `false`<br/>`true`                                                                                                                | When true, fire texture shows on that face of the block above; false if there's a block below this fire.                                                |
| west  | `false`       | `false`<br/>`true`                                                                                                                | When true, fire texture shows on that face of the block to the west; false if there's a block below this fire.                                          |

Bedrock Edition:
Fire and Soul Fire:

| Name | Metadata Bits                       | Default value | Allowed values                                                                                                                    | Values forMetadata Bits                                                                                                           | Description                                                                           |
|------|-------------------------------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| age  | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | Newly placed fire has an age of 0.<br/>This factor affects how the fire extinguishes. |




