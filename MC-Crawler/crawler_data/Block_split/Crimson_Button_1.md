### Block states
See also: Block states

Java Edition:

| Name    | Default value | Allowed values     | Description                                                                                                                 |
|---------|---------------|--------------------|-----------------------------------------------------------------------------------------------------------------------------|
| face    | wall          | ceilingfloorwall   | The face of the block it's placed on.Floor is on top of a block, ceiling is on the bottom, and wall is on one of its sides. |
| facing  | north         | eastnorthsouthwest | The direction it's facing.Opposite to the direction the player is facing if placed on the side of a block.                  |
| powered | false         | falsetrue          | If true, the button is currently activated.                                                                                 |

Bedrock Edition:

| Name               | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                                                                                                                                                                                                                        |
|--------------------|---------------|---------------|----------------|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| button_pressed_bit | 0x8           | false         | falsetrue      | 01                      | If the button is currently activated.                                                                                                                                                                                                              |
| facing_direction   | 0x10x20x4     | 0             | 012345         | 012345                  | The direction it's facing.0: Button on block bottom facing down 1: Button on block top facing up 2: Button on block side facing north 3: Button on block side facing south 4: Button on block side facing west 5: Button on block side facing east |




