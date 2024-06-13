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
