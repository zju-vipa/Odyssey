### Block states
See also: Block states

Java Edition:

| Name  | Default value | Allowed values     | Description                                                                                         |
|-------|---------------|--------------------|-----------------------------------------------------------------------------------------------------|
| east  | `true`        | `false`<br/>`true` | /If true, the east face has the cap/stem texture.<br/>If false, it has the pores texture instead.   |
| down  | `true`        | `false`<br/>`true` | /If true, the bottom face has the cap/stem texture.<br/>If false, it has the pores texture instead. |
| north | `true`        | `false`<br/>`true` | /If true, the north face has the cap/stem texture.<br/>If false, it has the pores texture instead.  |
| south | `true`        | `false`<br/>`true` | /If true, the south face has the cap/stem texture.<br/>If false, it has the pores texture instead.  |
| up    | `true`        | `false`<br/>`true` | /If true, the top face has the cap/stem texture.<br/>If false, it has the pores texture instead.    |
| west  | `true`        | `false`<br/>`true` | /If true, the west face has the cap/stem texture.<br/>If false, it has the pores texture instead.   |

Bedrock Edition:

| Name               | Metadata Bits                       | Default value | Allowed values         | Values forMetadata Bits | Description                                                                                         |
|--------------------|-------------------------------------|---------------|------------------------|-------------------------|-----------------------------------------------------------------------------------------------------|
| huge_mushroom_bits | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8` | `0`           | `0`                    | `0`                     | All six faces have the pores texture.                                                               |
|                    |                                     |               | `1`                    | `1`                     | Cap texture on top, west and north; pores on other sides.                                           |
|                    |                                     |               | `2`                    | `2`                     | Cap texture on top and north; pores on other sides.                                                 |
|                    |                                     |               | `3`                    | `3`                     | Cap texture on top, north and east; pores on other sides.                                           |
|                    |                                     |               | `4`                    | `4`                     | Cap texture on top and west; pores on other sides.                                                  |
|                    |                                     |               | `5`                    | `5`                     | Cap texture on top; pores on other sides.                                                           |
|                    |                                     |               | `6`                    | `6`                     | Cap texture on top and east; pores on other sides.                                                  |
|                    |                                     |               | `7`                    | `7`                     | Cap texture on top, south and west; pores on other sides.                                           |
|                    |                                     |               | `8`                    | `8`                     | Cap texture on top and south; pores on other sides.                                                 |
|                    |                                     |               | `9`                    | `9`                     | Cap texture on top, east and south; pores on other sides.                                           |
|                    |                                     |               | `10`                   | `10`                    | The four side faces have the stem texture,<br/>and the top and bottom faces have the pores texture. |
|                    |                                     |               | `11`<br/>`12`<br/>`13` | `11`<br/>`12`<br/>`13`  | All six faces have the pores texture.                                                               |
|                    |                                     |               | `14`                   | `14`                    | All six faces have the cap texture.                                                                 |
|                    |                                     |               | `15`                   | `15`                    | All six faces have the stem texture.                                                                |




