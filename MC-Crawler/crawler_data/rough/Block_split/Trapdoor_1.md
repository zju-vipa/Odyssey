### Redstone component
All types of trapdoors can be controlled with redstone power.

A trapdoor is a redstone mechanism and can be activated by:

- an adjacent activepower component, including above or below: for example, aredstone torch, ablock of redstone, adaylight sensor, etc.
- an adjacentpowered block(for example, a block with an active redstone torch under it), including above or below
- a poweredredstone comparatororredstone repeaterfacing the trapdoor
- poweredredstone dustconfigured to point at the trapdoor or a single redstone "cross" next to it; a trapdoor isnotactivated by adjacent powered redstone dust that is configured to point in another direction, or a single redstone "dot" next to it.

When activated, a trapdoor immediately rotates around its hinge side to its open state. When deactivated, a trapdoor immediately returns to its closed state. Each change of state takes one game tick.

An activated wooden or copper trapdoor can still be closed by a player, and does not re-open until it receives a new activation signal (if a trapdoor has been closed "by hand", it still needs to be deactivated and then reactivated to open by redstone).

## Block states
See also: Block states

Java Edition:

| Name        | Default value | Allowed values                            | Description                                                                                      |
|-------------|---------------|-------------------------------------------|--------------------------------------------------------------------------------------------------|
| facing      | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the trapdoor swings open.<br/>The opposite from the side its hinge is attached to. |
| half        | `bottom`      | `bottom`<br/>`top`                        | Whether the trapdoor occupies the top or bottom part of a block.                                 |
| open        | `false`       | `false`<br/>`true`                        | True if the trapdoor is currently open (may differ from`powered`).                               |
| powered     | `false`       | `false`<br/>`true`                        | True if the trapdoor is currently powered (may differ from`open`).                               |
| waterlogged | `false`       | `false`<br/>`true`                        | Whether or not there's water in the same place as this trapdoor.                                 |

Bedrock Edition:

| Name            | Metadata Bits   | Default value | Allowed values              | Values forMetadata Bits     | Description                                                                                                                                                                                                             |
|-----------------|-----------------|---------------|-----------------------------|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| direction       | `0x1`<br/>`0x2` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3` | `0`<br/>`1`<br/>`2`<br/>`3` | The direction the trapdoor is facing.0: Trapdoor on the west side of a block<br/>1: Trapdoor on the east side of a block<br/>2: Trapdoor on the north side of a block<br/>3: Trapdoor on the south side of a block<br/> |
| open_bit        | `0x8`           | `false`       | `false`<br/>`true`          | `0`<br/>`1`                 | True if the trapdoor is currently open.                                                                                                                                                                                 |
| upside_down_bit | `0x4`           | `false`       | `false`<br/>`true`          | `0`<br/>`1`                 | Whether the trapdoor occupies the top or bottom part of a block.                                                                                                                                                        |


