## Data values
### ID
Java Edition:

| Name  | Identifier | Form         | Block tags                                | Translation key        |
|-------|------------|--------------|-------------------------------------------|------------------------|
| Vines | `vine`     | Block & Item | `climbable`<br/>`lush_plants_replaceable` | `block.minecraft.vine` |

Bedrock Edition:

| Name  | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key  |
|-------|------------|------------|----------------------------|----------------|------------------|
| Vines | `vine`     | `106`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.vine.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block state

Java Edition:

| Name  | Default value | Allowed values     | Description                                          |
|-------|---------------|--------------------|------------------------------------------------------|
| east  | `false`       | `false`<br/>`true` | When true, a vine texture is displayed on the east.  |
| north | `false`       | `false`<br/>`true` | When true, a vine texture is displayed on the north. |
| south | `false`       | `false`<br/>`true` | When true, a vine texture is displayed on the south. |
| up    | `false`       | `false`<br/>`true` | When true, a vine texture is displayed on the top.   |
| west  | `false`       | `false`<br/>`true` | When true, a vine texture is displayed on the west.  |

Bedrock Edition:

| Name                | Metadata Bits                       | Default value | Allowed values                                                                                                                    | Values forMetadata Bits                                                                                                           | Description                                                                                                                                                                                                                                                                            |
|---------------------|-------------------------------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| vine_direction_bits | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | The directions the vine exists, excluding up. Each bit determines one direction:0x1: Vines at the south<br/>0x2: Vines at the west<br/>0x4: Vines at the north<br/>0x8: Vines at the east<br/>Note: Vines gain the ceiling vines if there's a block above, block state doesn't change. |




