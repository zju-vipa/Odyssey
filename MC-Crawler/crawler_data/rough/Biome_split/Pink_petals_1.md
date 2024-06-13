## Data values
### ID
Java Edition:

| Name        | Identifier    | Form         | Block tags                                                  | Item tags | Translation key               |
|-------------|---------------|--------------|-------------------------------------------------------------|-----------|-------------------------------|
| Pink Petals | `pink_petals` | Block & Item | `mineable/hoe`<br/>`flowers`<br/>`inside_step_sound_blocks` | `flowers` | `block.minecraft.pink_petals` |

Bedrock Edition:

| Name        | Identifier    | Numeric ID | Form                       | Item ID[i 1]   | Translation key         |
|-------------|---------------|------------|----------------------------|----------------|-------------------------|
| Pink Petals | `pink_petals` | `-549`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.pink_petals.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

Java Edition:

| Name          | Default value | Allowed values                            | Description                                                                                                                   |
|---------------|---------------|-------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| facing        | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the pink petals are facing.<br/>The opposite from the direction the player faces while placing the pink petals. |
| flower_amount | `1`           | `1`<br/>`2`<br/>`3`<br/>`4`               | The amount of pink petals in the block.                                                                                       |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values                                              | Values forMetadata Bits | Description                                                                                                                   |
|------------------------------|---------------|---------------|-------------------------------------------------------------|-------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| growth                       | Not Supported | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7` | `Unsupported`           | The amount of pink petals in the block. A value greater than 3 can only be obtained via commands.                             |
| minecraft:cardinal_direction | Not Supported | `south`       | `east`<br/>`north`<br/>`south`<br/>`west`                   | `Unsupported`           | The direction the pink petals are facing.<br/>The opposite from the direction the player faces while placing the pink petals. |




