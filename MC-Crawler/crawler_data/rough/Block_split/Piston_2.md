### Block states
See also: Block states

The piston block uses following block states:

Java Edition:

| Name     | Default value | Allowed values                                                | Description                                                                                                               |
|----------|---------------|---------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| extended | `false`       | `false`<br/>`true`                                            | If true, the piston is extended.                                                                                          |
| facing   | `north`       | `down`<br/>`east`<br/>`north`<br/>`south`<br/>`up`<br/>`west` | The direction the piston head is pointing.<br/>The opposite from the direction the player faces while placing the piston. |

Bedrock Edition:

| Name             | Metadata Bits             | Default value | Allowed values                              | Values forMetadata Bits                     | Description                                                                                                                                             |
|------------------|---------------------------|---------------|---------------------------------------------|---------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing_direction | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | The direction the piston is pointing.0: facing down<br/>1: facing up<br/>2: facing south<br/>3: facing north<br/>4: facing east<br/>5: facing west<br/> |

### Block data

  

This feature is exclusive to  Bedrock Edition. 


In Bedrock Edition, a piston has a block entity associated with it that holds additional data about the block.

SeeBedrock Edition level format/Block entity format.
## Notes
1. ↑Dragon eggs can be pushed, when in a falling state.
2. ↑In Java Edition, item frames are entities, 
not blocks. In Bedrock Edition, they are blocks.
3. ↑In Java Edition, if the "Fixed" NBT tag is set to "1", the item frame does not break when attempting to push it using a piston, but it still does not push. If the "Invulnerable" NBT tag is set to "1", the item frame breaks when pushed.
4. ↑Paintings are technically entities, not blocks.


