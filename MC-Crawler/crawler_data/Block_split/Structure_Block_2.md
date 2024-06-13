### 3D Export
Export Mode GUI
 3D Export mode‌[Bedrock Edition  only][note 2], is similar to save mode, but the structure is saved as a 3D render in the format of .glb rather than as an actual structure.[3] Therefore, structures saved this way can be viewed with 3D Viewer[4] or Paint 3D[5], but cannot be generated via load mode.

The 3D file exported is basically the same as the real-time rendering in the preview. End portal blocks, nether portal blocks, etc. in .glb file have only a static texture. Some blocks cannot be displayed properly, such as piston arms, chests, beds, etc. Including entities is not supported in this mode.

Structure blocks in 3D output mode cannot be activated by redstone.

Structure Name
Enter the name of the structure. Case sensitive. The player must enter a file name in order to export.
Relative Position
Enter the X, Y, and Z values for the structure here, based on the position of the structure block. Sets the origin of the structure outline.
Maximum allowed distance from the structure block is 64 blocks in any direction.
Structure Size
Enter the X, Y, and Z values to set the distance from the Relative Position coordinates. This sets the opposite corner of the structure, and defines its size.
Maximum structure size is 64×256×64.
Remove Blocks
While exporting the structure, doesn't include any blocks within saved structure.
## Data values
### ID
Java Edition:

| Name            | Identifier      | Form         | Block tags                 | Translation key                 |
|-----------------|-----------------|--------------|----------------------------|---------------------------------|
| Structure Block | structure_block | Block & Item | dragon_immunewither_immune | block.minecraft.structure_block |

| Name         | Identifier      |
|--------------|-----------------|
| Block entity | structure_block |

Bedrock Edition:

| Name            | Identifier      | Numeric ID | Form                       | Item ID[i 1]   | Translation key           |
|-----------------|-----------------|------------|----------------------------|----------------|---------------------------|
| Structure Block | structure_block | 252        | Block & Giveable Item[i 2] | Identical[i 3] | tile.structure_block.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


| Name         | Savegame ID    |
|--------------|----------------|
| Block entity | StructureBlock |

### Block states
Export Structure Block

See also: Block states

Java Edition:

| Name | Default value | Allowed values | Description            |
|------|---------------|----------------|------------------------|
| mode | data          | corner         | Corner Structure Block |
|      |               | data           | Data Structure Block   |
|      |               | load           | Load Structure Block   |
|      |               | save           | Save Structure Block   |

Bedrock Edition:

| Name                 | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description               |
|----------------------|---------------|---------------|----------------|-------------------------|---------------------------|
| structure_block_type | 0x10x20x4     | data          | corner         | 3                       | Corner Structure Block    |
|                      |               |               | data           | 0                       | Data Structure Block      |
|                      |               |               | export         | 5                       | Export Structure Block    |
|                      |               |               | invalid        | 4                       | Inventory Structure Block |
|                      |               |               | load           | 2                       | Load Structure Block      |
|                      |               |               | save           | 1                       | Save Structure Block      |



### Block data
A structure block also has a block entity associated with it.

Java Edition:

See also: Block entity format


 Block entity data
Tags common to all block entities
 author: Author of the structure; only set to "?" for most vanilla structures.
 ignoreEntities: 1 or 0 (true/false): Whether entities should be ignored in the structure.
 integrity: How complete the structure is that gets placed.
 metadata: Value of the data structure block field.
 mirror: How the structure is mirrored, one of "NONE", "LEFT_RIGHT" (mirrored over X axis when not rotated), or "FRONT_BACK" (mirrored over Z axis when not rotated).
 mode: The current mode of this structure block, one of "SAVE", "LOAD", "CORNER", or "DATA".
 name: Name of the structure.
 posX: X-position of the structure.
 posY: Y-position of the structure.
 posZ: Z-position of the structure.
 powered: 1 or 0 (true/false): Whether this structure block is being powered by redstone.
 rotation: Rotation of the structure, one of "NONE", "CLOCKWISE_90", "CLOCKWISE_180", or "COUNTERCLOCKWISE_90".
 seed: The seed to use for the structure integrity, 0 means random.
 showboundingbox: 1 or 0 (true/false): Whether to show the structure's bounding box to players in Creative mode.
 sizeX: X-size of the structure, its length.
 sizeY: Y-size of the structure, its height.
 sizeZ: Z-size of the structure, its depth.

Bedrock Edition:

See Bedrock Edition level format/Block entity format.
## See also
- Jigsaw block

## Notes

↑ Structures created in versions before 1.13 are saved in .minecraft/saves/(WorldName)/structures.

↑ Only available on Windows 10



