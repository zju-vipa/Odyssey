### Note blocks
The observer can be placed under note blocks to produce bass drum sounds.

## Data values
### ID
Java Edition:

| Name     | Identifier | Form         | Translation key            |
|----------|------------|--------------|----------------------------|
| Observer | `observer` | Block & Item | `block.minecraft.observer` |

Bedrock Edition:

| Name     | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key      |
|----------|------------|------------|----------------------------|----------------|----------------------|
| Observer | `observer` | `251`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.observer.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

Java Edition:

| Name    | Default value | Allowed values                                                | Description                                                                                          |
|---------|---------------|---------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| facing  | `south`       | `down`<br/>`east`<br/>`north`<br/>`south`<br/>`up`<br/>`west` | The direction the observer is observing. The same direction the player faces when placing the block. |
| powered | `false`       | `false`<br/>`true`                                            | True while the observer is observing a change and emitting a pulse.                                  |

Bedrock Edition:

| Name                       | Metadata Bits | Default value | Allowed values                                                | Values forMetadata Bits | Description                                                                                          |
|----------------------------|---------------|---------------|---------------------------------------------------------------|-------------------------|------------------------------------------------------------------------------------------------------|
| minecraft:facing_direction | Not Supported | `down`        | `down`<br/>`east`<br/>`north`<br/>`south`<br/>`up`<br/>`west` | `Unsupported`           | The direction the observer is observing. The same direction the player faces when placing the block. |
| powered_bit                | `0x8`         | `false`       | `false`<br/>`true`                                            | `0`<br/>`1`             | True while the observer is observing a change and emitting a pulse.                                  |




