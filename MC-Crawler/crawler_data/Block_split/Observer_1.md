### Note blocks
The observer can be placed under note blocks to produce bass drum sounds.

## Data values
### ID
Java Edition:

| Name     | Identifier | Form         | Translation key          |
|----------|------------|--------------|--------------------------|
| Observer | observer   | Block & Item | block.minecraft.observer |

Bedrock Edition:

| Name     | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key    |
|----------|------------|------------|----------------------------|----------------|--------------------|
| Observer | observer   | 251        | Block & Giveable Item[i 2] | Identical[i 3] | tile.observer.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


### Block states
See also: Block states

Java Edition:

| Name    | Default value | Allowed values           | Description                                                                                          |
|---------|---------------|--------------------------|------------------------------------------------------------------------------------------------------|
| facing  | south         | downeastnorthsouthupwest | The direction the observer is observing. The same direction the player faces when placing the block. |
| powered | false         | falsetrue                | True while the observer is observing a change and emitting a pulse.                                  |

Bedrock Edition:

| Name                       | Metadata Bits | Default value | Allowed values           | Values forMetadata Bits | Description                                                                                          |
|----------------------------|---------------|---------------|--------------------------|-------------------------|------------------------------------------------------------------------------------------------------|
| minecraft:facing_direction | Not Supported | down          | downeastnorthsouthupwest | Unsupported             | The direction the observer is observing. The same direction the player faces when placing the block. |
| powered_bit                | 0x8           | false         | falsetrue                | 01                      | True while the observer is observing a change and emitting a pulse.                                  |



## See also
- Tutorials/Block update detector
- Redstone Comparator


