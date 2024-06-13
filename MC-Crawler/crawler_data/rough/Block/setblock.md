# Commands/setblock
Changes a block to another block.

## Contents
- 1 Syntax
- 2 Arguments
- 3 Result
- 4 Output
- 5 Examples
- 6 History
- 7 See also
- 8 References

## Syntax
- Java Edition

setblock <pos> <block> [destroy|keep|replace]
- Bedrock Edition

setblock <position: x y z> <tileName: Block> <blockStates: block states> [destroy|keep|replace]
setblock <position: x y z> <tileName: Block> [destroy|keep|replace]
## Arguments
JE: <pos>: block_posBE: position: x y z: CommandPosition

Specifies the position of the block to be changed.
InJava Edition, must be ablock positioncomposed of<X>,<Y>and<Z>, each of which must be an integer or atilde and caret notation. InBedrock Edition, must be a three-dimensional coordinates composed of<X>,<Y>and<Z>, each of which must be asingle-precision floating-point numberortilde and caret notation.
JE: <block>: block_stateBE: tileName: Block: enum

Specifies the new block.
InJava Edition, must be in the format ofblock_id[block_states]{data_tags}(does not accept block tags), in which block states and data tags can be omitted when they are not needed. InBedrock Edition, must be ablock id.
BE: blockStates: block states: BlockStateCommandParam

Specifies theblock statesto use for the block.
Must be a blockstate argument as["<state1>"=<value1>,"<state2>"=<value2>,...]. For example:["old_leaf_type"="birch","persistent_bit"=true].
destroy|keep|replace

Specifies how to handle the block change. Must be one of:
- destroy— The old blockdropsboth itself and its contents (as if destroyed by aplayer). Plays the appropriate block breaking noise.
- keep— Onlyairblocks are changed (non-air blocks are unchanged).
- replace— The old block drops neither itself nor any contents. Plays no sound.

If not specified, defaults toreplace.
## Result








| Command                                   | Trigger                                                                                                                                                        | Java Edition | Bedrock Edition |
|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|-----------------|
| Any                                       | The command is incomplete, or any argument is not specified correctly.                                                                                         | Unparseable  | Unparseable     |
|                                           | specified position is unloaded or out of the world.                                                                                                            | Failed       | Failed          |
|                                           | Trying to place block indebug mode.                                                                                                                            |              | N/A             |
| `/setblock ... keep`                      | Trying to change a non-air block.                                                                                                                              | Failed       |                 |
| `/setblock ... keep/setblock ... replace` | Trying to replace a block with an identical copy (ignoring the block entity).                                                                                  |              |                 |
|                                           | Trying to replace some kinds of redstone components with an unstable block (e.g. replacing one of two adjacent standing redstone torches with a TNT block)[1]. |              | Successful      |
| Any                                       | Otherwise                                                                                                                                                      |              | Successful      |

## Output





| Command | Edition         | Situation  | Success Count | /execute store success ... | /execute store result ... |
|---------|-----------------|------------|---------------|----------------------------|---------------------------|
| Any     | Java Edition    | On fail    | 0             | 0                          | 0                         |
|         |                 | On success | 1             | 1                          | 1                         |
|         | Bedrock Edition | On fail    | 0             | N/A                        | N/A                       |
|         |                 | On success | 1             | N/A                        | N/A                       |

## Examples
- Put a chest facing east at your feet
	- setblock ~ ~ ~ chest[facing=east]‌[Java Edition  only]
	- setblock ~ ~ ~ chest ["minecraft:cardinal_direction"="east"]‌[Bedrock Edition  only]
- Place a sign next to it inJava Edition
	- setblock ~ ~ ~-1 birch_sign{Text1:'"My chest"',Text2:'"Do not open!"'}(Note the two sets of quotes around the text. They are required.)
- Put a top quartz slab at the top of your head
	- setblock ~ ~2 ~ quartz_slab[type=top]‌[Java Edition  only]
	- setblock ~ ~2 ~ stone_block_slab ["stone_slab_type"="quartz","minecraft:vertical_half"="top"]‌[Bedrock Edition  only]

