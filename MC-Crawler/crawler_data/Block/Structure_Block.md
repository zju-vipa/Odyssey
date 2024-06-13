# Structure Block
A structure block is used to generate structures manually. They can also be used to save and load structures, alongside structure void blocks.

## Contents
- 1 Obtaining
- 2 Usage
	- 2.1 Save
	- 2.2 Load
	- 2.3 Corner
	- 2.4 Data
	- 2.5 3D Export
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
	- 4.3 Block data
- 5 Video
- 6 History
- 7 Issues
- 8 Gallery
	- 8.1 Textures
	- 8.2 Screenshots
- 9 See also
- 10 Notes
- 11 References

## Obtaining
Structure blocks are available using the /setblock, /fill, or /give commands, and are available in the Creative inventory in Java Edition. When placed, structure blocks are unbreakable in Survival and have the same blast resistance as bedrock. In Bedrock Edition, only save-mode structure blocks are obtainable through commands.

## Usage
When placed, use the structure block to open its GUI. The GUI opens only if the player is in Creative mode, and has permission level 2 or higher.

Once a structure is named, its name appears above the structure block when highlighted, preceded by the block mode (e.g. "Save:House").‌[Java Edition  only]

Switching between modes preserves the settings of the structure block wherever possible.

Before being placed, the structure block uses a "blank" texture in the inventory, a texture that is not used when on a placed block.

A piston cannot move a structure block. They also cannot be pushed nor pulled by sticky pistons. Structure blocks cannot be destroyed by the ender dragon.

### Save
Save mode GUI for Java Edition
Save mode GUI for Bedrock Edition
 Save mode allows the player to highlight a structure in the world and save it to memory, level file‌[Bedrock Edition  only], or a separate file.

Structure Name
The name of the structure is entered into this text box. Capital letters‌[JE  only] and special characters are not allowed. Underscores (_) and hyphens (-) are allowed. In Bedrock Edition, it has "mystructure:" prefix on default.
Relative Position
Enter the X, Y, and Z values for the structure here, based on the position of the structure block. Sets the origin of the structure outline.
Maximum allowed distance from the structure block in Java Edition is 48 blocks in any direction and 64 on horizontal direction and 256 on vertical direction in Bedrock Edition.
All invisible blocks shown by structure blocks
Show invisible blocks ‌[JE  only]

  

This section is missing information about What color was used for structure voids prior to 21w20a? And were there any other changers since their introduction in 1.10 (ignoring the old dark outlines)?. 
Please expand the section to include this information. Further details may exist on the talk page.


Displays invisible blocks as small colored cubes. Off by default.
Invisible blocks as shown by the "Show invisible blocks" option


Block

Appearance

Color

Notes


Airminecraft:airCave Airminecraft:cave_airVoid Airminecraft:void_air



 rgb(127.5, 127.5, 255)

All air types look the same by design.[1]


Structure Voidminecraft:structure_void



 rgb(255, 191.25, 191.25)




Barrierminecraft:barrier



 rgb(255, 0, 0)




Light Blockminecraft:light



 rgb(255, 255, 0)



Structure Size
Enter the X, Y, and Z values to set the distance from the Relative Position coordinates. This sets the opposite corner of the structure, and defines its size.
Maximum structure size is 48x48x48 in Java Edition and 64x256x64 in Bedrock Edition.
When successful, generates a white outline surrounding the structure.‌[JE  only] In Bedrock Edition, the outline is green, blue, or red (depending on the axis) and the preview design can be used to see every layer of fragmented structure and to change the structure size to be saved.
Detect structure size and position
Automatically calculates the size and position of the structure using a corner block placed on the opposite corner of the structure.
The name of the structure in the save block must match the name within the corner block, or the size calculation fails.
Two corner blocks can also be used. It uses the second corner block instead of the structure block.
Remove blocks ‌[BE  only]
While saving the structure and when enabled, this doesn't include any blocks within the structure.
Include entities
While saving the structure and when enabled, this saves any entities within the structure as well.
Save
When all coordinates and a structure name have been entered, press this button to save the structure.
In Java Edition, this saves the structure to a file. The name of the structure is the name of the file.
Structures can be saved to a file only by manually pressing this button. If a structure block in Save mode is instead powered by redstone, the structure is saved only in memory by default. This is the case even if a file for that structure already exists on disk. Reloading the world clears any structures stored in memory. This is for unspecified security reasons.[2]
By default, structure blocks are saved in the minecraft namespace. This can be changed by prefixing the structure name with <namespace>: in the structure block.
Structures are saved in .minecraft/saves/(WorldName)/generated/(namespace)/structures. [note 1]
In Bedrock Edition, this saves the structure into level database file rather than a standalone file. And the player can set up the structure block so that it can save into the memory or the disk (level file) when automated with redstone.
Export ‌[BE  only]
Used to export a structure into a .mcstructure file, which can be used to load from the structures folder of a behavior pack. If the structure contains a custom block from a behavior pack, then the block is also saved on the structure block. This option is available only on Android and Windows 10 devices.
### Load
Load Mode GUI for Java Edition
Load Mode GUI for Bedrock Edition
 Load mode allows the player to load and rotate saved structures.

Structure Name
The name of the structure to load.
In Java Edition, it can load structures saved to memory or a file (.minecraft/saves/<World Name>/generated/<namespace>/structures/), structures in data pack and in minecraft.jar.
To load a structure from a file, simply type <namespace>:<structure_path>.
Structures saved only to memory have a higher priority than structures of the same name that were saved to a file. Structures saved to a file have a higher priority than structures of the same name that is in data pack, which have a higher priority than structures in minecraft.jar.
In Bedrock Edition, it can load structures saved to memory or disk (level database), and structures in behavior pack.
Structures saved only to memory have a higher priority than structures of the same name that were saved to disk. Structures saved to disk have a higher priority than structures of the same name that is in behavior pack.
Vanilla NBT structure files cannot be loaded with structure block.
Relative Position
The X, Y, and Z coordinates of the corner in which to generate the structure, based on the position of the structure block. Coordinates may be defined as numbers between -48 and 48 In Java Edition, or between -64 and 64 In Bedrock Edition.
Show bounding box
Highlights the outline of the structure; on by default.
Structure Integrity and Seed
Removes random blocks that compose the structure based on a user-defined seed.
Lower integrity values result in more blocks being removed. The integrity value must be between 0.0 and 1.0‌[JE  only] / 100.00‌[BE  only].
Include entities
Include any entities saved in the structure file when loading the structure. Off by default.
Waterlog blocks ‌[BE  only]
While loading the structure in water, it allows the blocks to be waterlogged instead of being replaced with air.
Remove blocks ‌[BE  only]
While loading the structure, doesn't include any blocks within saved structure.
Rotation (0, 90, 180, 270)
Sets the rotation of the structure to 0° (no rotation), 90° clockwise, 180° clockwise, and 270° clockwise (or 90° counter-clockwise).
Mirror (¦, <>, ^v)
Sets the mirroring of the structure to none (¦), left to right (< >), or front to back (^ v). At 0° rotation < > mirrors across the X-axis and ^ v mirrors across the Z-axis.
In Bedrock Edition, the options are x and z, which can be toggled to set mirroring.
Animation mode ‌[BE  only]
Select the animation to show how structure is loaded. Place by layer make structure loaded layer by layer, place by block make structure loaded one block by block. Default to none.
Once the loading has started, breaking the structure block can not stop the loading process.
Loading with animation may break blocks in structures that contain multiple parts (such as beds, doors, or tall grass), or need to be attached to other blocks (such as torches), and may cause water, lava, and fire to spread out.
Animation time ‌[BE  only]
Adjust the animation time for loading the structure.
Load
Load the structure.
In Java Edition, press this button once to prepare the outline preview of the structure. When satisfied with the position, press again to generate the structure.
Structures may also be loaded with the use of redstone.
### Corner
Corner Mode GUI for Java Edition.
Corner Mode GUI for Bedrock Edition.
 Corner mode allows for an easier and automatic size calculation while saving or loading structures.

To use, place on the opposite corner of a save structure block or a second corner structure block. Then, using a save block, press "DETECT".
When successful, a bounding outline appears.
Structure Name
The name of the structure on which to calculate the size and position.
Name is case sensitive; it must match exactly with the name provided by the complementary save or corner structure block.
### Data
Data mode GUI
 Data mode is a deprecated mode, which is superseded by jigsaw block, but still used in some certain vanilla structures (igloo, end city, woodland mansion, ocean ruin, shipwreck). Structure block in data mode can be used only during natural generation. They mark the location to run a specified hardcoded function, which can be used only for relevant structures. In Java Edition, this mode is hidden unless the Alt key is held while switching from Corner mode. In Bedrock Edition, data mode structure block cannot be obtained with commands.

Custom Data Tag Name
The name of the function to run.
Igloo
"chest" - sets the loot table for a chest beneath the structure block to "chests/igloo_chest" and sets the loot table seed dependent on the world seed.
End city
"Chest" - Sets the loot table for a chest beneath the structure block to "chests/end_city_treasure" and sets the loot table seed dependent on the world seed.
"Sentry" - Creates a shulker at the location of the structure block.
"Elytra" - Creates an item frame entity with an elytra item inside it at the location of the structure block.
Woodland mansion
"ChestSouth" - Sets the loot table for a chest that replaces the structure block to "chests/woodland_mansion" and sets the loot table seed dependent on the world seed.
"ChestNorth" - Sets the loot table for a chest that replaces the structure block to "chests/woodland_mansion" and sets the loot table seed dependent on the world seed.
"ChestEast" - Sets the loot table for a chest that replaces the structure block to "chests/woodland_mansion" and sets the loot table seed dependent on the world seed.
"ChestWest" - Sets the loot table for a chest that replaces the structure block to "chests/woodland_mansion" and sets the loot table seed dependent on the world seed.
"Mage" - Creates an evoker at the location of the structure block.
"Warrior" - Creates a vindicator at the location of the structure block.
Ocean ruins
"chest" - Creates a chest at the location of the structure block, setting its loot table to either "chests/underwater_ruin_big" or "chests/underwater_ruin_small", with seed dependent on the world seed.
"drowned" - Creates a drowned at the location of the structure block.
Shipwreck
"map_chest" - Sets the loot table for a chest that replaces the structure block to "chests/shipwreck_map" and sets the loot table seed dependent on the world seed.
"treasure_chest" - Sets the loot table for a chest that replaces the structure block to "chests/shipwreck_treasure" and sets the loot table seed dependent on the world seed.
"supply_chest" - Sets the loot table for a chest that replaces the structure block to "chests/shipwreck_supply" and sets the loot table seed dependent on the world seed.
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


