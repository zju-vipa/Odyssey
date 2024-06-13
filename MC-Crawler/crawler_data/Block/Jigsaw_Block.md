# Jigsaw Block
Jigsaw blocks are technical blocks commonly used as a way to construct large structures from smaller sections.

## Contents
- 1 Obtaining
	- 1.1 Natural generation
- 2 Usage
	- 2.1 Jigsaw connections
	- 2.2 Debug generation
	- 2.3 Piston interactivity
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
	- 4.3 Block data
- 5 Video
- 6 History
- 7 Issues
- 8 Gallery
	- 8.1 Renders
	- 8.2 Screenshots
- 9 See also
- 10 References

## Obtaining
In Java Edition, jigsaw blocks are available in the creative inventory. Across both Java and Bedrock editions, they can also be obtained by using the pick block control, or by using various commands such as /give @s jigsaw. 

Jigsaw blocks are included when a player uses a structure block to spawn certain structures that use jigsaw blocks for generation.

### Natural generation
Jigsaw blocks do not naturally generate. Some structures rely on jigsaw blocks for generation (pillager outposts, villages and ancient cities), but these jigsaw blocks are replaced by other blocks during generation.

## Usage
Jigsaw Block interface in Java Edition
Jigsaw Block interface in Bedrock Edition
### Jigsaw connections
Main article: Jigsaw structure
Jigsaw blocks are function blocks used for the generation of jigsaw structures out of smaller templates.[1] Jigsaw structures are used for the generation of pillager outposts, villages, bastion remnants, ancient cities, trail ruins, and trial chambers‌[upcoming: JE 1.21 & BE 1.21]; other structures use hardcoded generation. The GUI of a jigsaw block can be used to configure its generation settings. Those are:

Target Pool
Refers to a template pool; or an alias of a template pool. The template pool is used to select the connecting structure piece.
Name
Name of the jigsaw block.
Defaults to minecraft:empty.
Target name
The desired name of the jigsaw block in the connecting piece to connect to this jigsaw block.
Defaults to minecraft:empty.
Turns into
What the jigsaw block turns into once the whole feature is generated.
Defaults to minecraft:air.
Selection Priority
Defines the order of jigsaw blocks in a template to generate the connecting piece. If the piece being generated contains multiple jigsaw blocks that are all valid connections to the parent block, the game will try to connect to the one with the highest Selection Priority first. In the case of a tie, the connecting block is selected randomly.
Placement Priority
Defines the order of in which the connecting piece is processed to handle its jigsaw blocks during the wider structure generation.
Joint type
Appears only when jigsaw block is placed facing up or down.
Contains two types of joints: Rollable and Aligned
Rollable: The connecting piece is placed with a random rotation. Defaults to this.
Aligned: The connecting piece is rotated such that the rotations of the jigsaw blocks match (marked by the white bar on the jigsaw block)
### Debug generation
See also: Commands/place


  

This feature is exclusive to  Java Edition. 


Jigsaw blocks can also be used to generate multiple levels of jigsaw blocks in the world. The settings in the 2nd to last row are only used for this purpose and are not saved when leaving the UI.

Levels
Determines how many jigsaw block "levels" it goes through. (ex. Piece>[Layer 1]>[Layer 2]).
Can be set to an integer from 0 to 20. Defaults to 0.
Keep Jigsaw
Determines if the placed pieces includes the jigsaw blocks it contains or become what its "Turns into" field is set to.
Defaults to ON
Generate
The button to start the generation.
### Piston interactivity
Jigsaw blocks cannot be pushed by pistons. They also cannot be pushed nor pulled by sticky pistons.

## Data values
### ID
Java Edition:

| Name         | Identifier | Form         | Translation key        |
|--------------|------------|--------------|------------------------|
| Jigsaw Block | jigsaw     | Block & Item | block.minecraft.jigsaw |

| Name         | Identifier |
|--------------|------------|
| Block entity | jigsaw     |

Bedrock Edition:

| Name         | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key  |
|--------------|------------|------------|----------------------------|----------------|------------------|
| Jigsaw Block | jigsaw     | 466        | Block & Giveable Item[i 2] | Identical[i 3] | tile.jigsaw.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


| Name         | Savegame ID |
|--------------|-------------|
| Block entity | JigsawBlock |

### Block states
See also: Block states

Java Edition:

| Name        | Default value | Allowed values                                                                                     | Description                               |
|-------------|---------------|----------------------------------------------------------------------------------------------------|-------------------------------------------|
| orientation | north_up      | down_eastdown_northdown_southdown_westeast_upnorth_upsouth_upup_eastup_northup_southup_westwest_up | The direction the jigsaw block is facing. |

Bedrock Edition:

| Name             | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                               |
|------------------|---------------|---------------|----------------|-------------------------|-------------------------------------------|
| facing_direction | Not Supported | 0             | 012345         | Unsupported             | The direction the jigsaw block is facing. |
| rotation         | Not Supported | 0             | 0123           | Unsupported             | The rotation around the axis.             |



### Block data
A jigsaw block has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format


 Block entity data
Tags common to all block entities
 final_state: The block that this jigsaw block becomes.
 joint: The joint option value, either "rollable" or "aligned".
 name: The jigsaw block's name. This jigsaw block gets aligned with another structure's jigsaw block that has this value in the target tag.
 pool: The jigsaw block's target pool to select a structure from.
 target: The jigsaw block's target name. This jigsaw block gets aligned with another structure's jigsaw block that has this value in the name tag.
 selection_priority: Priority of this jigsaw block being selected for generation. Jigsaw blocks with higher selection priority get selected first.
 placement_priority: Priority of the piece generated by this jigsaw block to place its children. Pieces with higher placement priority generate their children first.

Bedrock Edition:

See Bedrock Edition level format/Block entity format.
## See also
- Structure Block

