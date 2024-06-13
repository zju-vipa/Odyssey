### Block states
See also: Block states

The piston block uses following block states:

Java Edition:

| Name     | Default value | Allowed values           | Description                                                                                                          |
|----------|---------------|--------------------------|----------------------------------------------------------------------------------------------------------------------|
| extended | false         | falsetrue                | If true, the piston is extended.                                                                                     |
| facing   | north         | downeastnorthsouthupwest | The direction the piston head is pointing.The opposite from the direction the player faces while placing the piston. |

Bedrock Edition:

| Name             | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                                                                                                    |
|------------------|---------------|---------------|----------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| facing_direction | 0x10x20x4     | 0             | 012345         | 012345                  | The direction the piston is pointing.0: facing down 1: facing up 2: facing south 3: facing north 4: facing east 5: facing west |

### Block data

  

This feature is exclusive to  Bedrock Edition. 


In Bedrock Edition, a piston has a block entity associated with it that holds additional data about the block.

See Bedrock Edition level format/Block entity format.
## See also
- Slime block
- Redstone
- Tutorials/Piston uses
- Tutorials/Headless pistons
- Mechanics/Redstone/Piston circuits

## Notes

↑  Dragon eggs can be pushed, when in a falling state.

↑ In Java Edition, item frames are entities, 
not blocks. In Bedrock Edition, they are blocks.

↑ In Java Edition, if the "Fixed" NBT tag is set to "1", the item frame does not break when attempting to push it using a piston, but it still does not push. If the "Invulnerable" NBT tag is set to "1", the item frame breaks when pushed.

↑ Paintings are technically entities, not blocks.



