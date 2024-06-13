### Trading
Master-level fletcher villagers have a 2⁄3 chance to buy 8 tripwire hooks for an emerald as part of their trades in Java Edition, and always offer the trade in Bedrock Edition.

## Data values
### ID
Java Edition:

| Name          | Identifier      | Form         | Translation key                 |
|---------------|-----------------|--------------|---------------------------------|
| Tripwire Hook | `tripwire_hook` | Block & Item | `block.minecraft.tripwire_hook` |

Bedrock Edition:

| Name          | Identifier      | Numeric ID | Form                       | Item ID[i 1]   | Translation key           |
|---------------|-----------------|------------|----------------------------|----------------|---------------------------|
| Tripwire Hook | `tripwire_hook` | `131`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.tripwire_hook.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

Java Edition:

| Name     | Default value | Allowed values                            | Description                                                                                                                                                            |
|----------|---------------|-------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| attached | `false`       | `false`<br/>`true`                        | True if the tripwire hook is connected to a valid tripwire circuit.                                                                                                    |
| facing   | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction in which the tripwire hook juts out from the block it is attached to.<br/>For example, a tripwire hook facing north is attached to a block to its south. |
| powered  | `false`       | `false`<br/>`true`                        | True if the tripwire hook is active.                                                                                                                                   |

Bedrock Edition:

| Name         | Metadata Bits   | Default value | Allowed values              | Values forMetadata Bits     | Description                                                                                                                                                                                                                                                                       |
|--------------|-----------------|---------------|-----------------------------|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| attached_bit | `0x4`           | `false`       | `false`<br/>`true`          | `0`<br/>`1`                 | True if the tripwire hook is connected to a valid tripwire circuit.                                                                                                                                                                                                               |
| direction    | `0x1`<br/>`0x2` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3` | `0`<br/>`1`<br/>`2`<br/>`3` | The direction in which the tripwire hook juts out from the block it is attached to.0: Tripwire hook on block side facing south<br/>1: Tripwire hook on block side facing west<br/>2: Tripwire hook on block side facing north<br/>3: Tripwire hook on block side facing east<br/> |
| powered_bit  | `0x8`           | `false`       | `false`<br/>`true`          | `0`<br/>`1`                 | True if the tripwire hook is active.                                                                                                                                                                                                                                              |




