### Block states
See also: Block states

Java Edition:

| Name    | Default value | Allowed values                            | Description                                                                                                                      |
|---------|---------------|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| face    | `wall`        | `ceiling`<br/>`floor`<br/>`wall`          | The face of the block it's placed on.<br/>Floor is on top of a block, ceiling is on the bottom, and wall is on one of its sides. |
| facing  | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction it's facing.<br/>Opposite to the direction the player is facing if placed on the side of a block.                  |
| powered | `false`       | `false`<br/>`true`                        | If true, the button is currently activated.                                                                                      |

Bedrock Edition:

| Name               | Metadata Bits             | Default value | Allowed values                              | Values forMetadata Bits                     | Description                                                                                                                                                                                                                                                                 |
|--------------------|---------------------------|---------------|---------------------------------------------|---------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| button_pressed_bit | `0x8`                     | `false`       | `false`<br/>`true`                          | `0`<br/>`1`                                 | If the button is currently activated.                                                                                                                                                                                                                                       |
| facing_direction   | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | The direction it's facing.0: Button on block bottom facing down<br/>1: Button on block top facing up<br/>2: Button on block side facing north<br/>3: Button on block side facing south<br/>4: Button on block side facing west<br/>5: Button on block side facing east<br/> |




