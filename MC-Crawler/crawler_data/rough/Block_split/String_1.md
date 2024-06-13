### Trading
Novice-level fisherman villagers have a 50% chance to buy 20 string as part of their first-tier trade.

Journeyman-level fletcher villagers buy 14 string for 1 emerald as part of their trade.

## Data values
### ID
Java Edition:

| Name     | Identifier | Form  | Block tags           | Translation key            |
|----------|------------|-------|----------------------|----------------------------|
| Tripwire | `tripwire` | Block | `wall_post_override` | `block.minecraft.tripwire` |
| String   | `string`   | Item  | —                    | `item.minecraft.string`    |

Bedrock Edition:

| Name     | Identifier  | Alias ID   | Numeric ID | Form                         | Item ID[i 1] | Translation key      |
|----------|-------------|------------|------------|------------------------------|--------------|----------------------|
| Tripwire | `trip_wire` | `tripWire` | `132`      | Block & Ungiveable Item[i 2] | `trip_wire`  | `tile.tripWire.name` |
| String   | `string`    | None       | `326`      | Item                         | —            | `item.string.name`   |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Unavailable with /give command

### Block states
See also: Block states

Java Edition:

| Name     | Default value | Allowed values     | Description                                                                     |
|----------|---------------|--------------------|---------------------------------------------------------------------------------|
| attached | `false`       | `false`<br/>`true` | True if the tripwire is connected to a valid tripwire circuit.                  |
| disarmed | `false`       | `false`<br/>`true` | True if the tripwire is disarmed, that is, broken usingshears.                  |
| east     | `false`       | `false`<br/>`true` | True if the tripwire connects to other tripwire or tripwire hooks to the east.  |
| north    | `false`       | `false`<br/>`true` | True if the tripwire connects to other tripwire or tripwire hooks to the north. |
| powered  | `false`       | `false`<br/>`true` | True if the tripwire is active.                                                 |
| south    | `false`       | `false`<br/>`true` | True if the tripwire connects to other tripwire or tripwire hooks to the south. |
| west     | `false`       | `false`<br/>`true` | True if the tripwire connects to other tripwire or tripwire hooks to the west.  |

Bedrock Edition:

| Name          | Metadata Bits | Default value | Allowed values     | Values forMetadata Bits | Description                                                                                      |
|---------------|---------------|---------------|--------------------|-------------------------|--------------------------------------------------------------------------------------------------|
| attached_bit  | `0x4`         | `false`       | `false`<br/>`true` | `0`<br/>`1`             | True if the tripwire is connected to a valid tripwire circuit.                                   |
| disarmed_bit  | `0x8`         | `false`       | `false`<br/>`true` | `0`<br/>`1`             | True if the tripwire is disarmed, that is, broken usingshears.                                   |
| powered_bit   | `0x1`         | `false`       | `false`<br/>`true` | `0`<br/>`1`             | True if the tripwire is active.                                                                  |
| suspended_bit | `0x2`         | `true`        | `false`<br/>`true` | `0`<br/>`1`             | True if the tripwire hasn't connected to a valid tripwire circuit. (makeshitboxlarger when true) |




