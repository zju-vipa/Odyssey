##### Exceptions
- Rails: as long as they remain on top of a solid face of a block in their new position, and that block isn't moving at the same time.
	- An exception is when the rail and block supporting it are on two parallelextendedpistons at which the rail remains attached. InJava Edition, in order for the rail to successfully move without breaking, the piston moving the block must be powered 1 block event after the piston moving the rail. Trying to move both on the same piston usingslime blocksdoes not work, nor does moving them on perpendicular pistons (although the latter temporarilyappearsto work because of the bugMC-75716).
	- Rails re-orient themselves after being pushed, similar to when placed manually.



## Technical components
Main article: Piston/Technical components
Sticky pistons have 2 technical blocks that cannot be obtained. These include the piston head and moving piston blocks.

## Data values
### ID
Java Edition:

| Name          | Identifier    | Form         | Block tags | Translation key               |
|---------------|---------------|--------------|------------|-------------------------------|
| Sticky Piston | sticky_piston | Block & Item | None       | block.minecraft.sticky_piston |

| Name         | Identifier |
|--------------|------------|
| Block entity | piston     |

Bedrock Edition:

| Name          | Identifier    | Alias ID | Numeric ID | Form                       | Item ID[i 1]   | Translation key         |
|---------------|---------------|----------|------------|----------------------------|----------------|-------------------------|
| Sticky Piston | sticky_piston | None     | 29         | Block & Giveable Item[i 2] | Identical[i 3] | tile.sticky_piston.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


| Name                | Savegame ID |
|---------------------|-------------|
| Piston block entity | PistonArm   |

### Block states
See also: Block states

The sticky_piston block uses following block states:

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
A sticky piston has a block entity associated with it that holds additional data about the block.
Java Edition:

See also: Block entity format


 Block entity data
Tags common to all block entities
 blockState: The moving block represented by this block entity.
Block state
 extending: 1 or 0 (true/false) – true if the piston is extending instead of withdrawing.
 facing: Direction that the piston pushes (0=down, 1=up, 2=north, 3=south, 4=west, 5=east).
 progress: How far the block has been moved. Starts at 0.0, and increments by 0.5 each tick. If the value is 1.0 or higher at the start of a tick (before incrementing), then the block transforms into the stored blockState. Negative values can be used to increase the time until transformation.
 source: 1 or 0 (true/false) – true if the block represents the piston head itself, false if it represents a block being pushed.

Bedrock Edition:

See Bedrock Edition level format/Block entity format.
## See also
- Piston
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



