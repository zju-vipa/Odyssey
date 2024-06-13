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

** Structure Name **
The name of the structure is entered into this text box. Capital letters‌[JE  only]and special characters are not allowed. Underscores (_) and hyphens (-) are allowed. InBedrock Edition, it has "mystructure:" prefix on default.
** Relative Position **
Enter the X, Y, and Z values for the structure here, based on the position of the structure block. Sets the origin of the structure outline.
Maximum allowed distance from the structure block inJava Editionis 48 blocks in any direction and 64 on horizontal direction and 256 on vertical direction inBedrock Edition.
All invisible blocks shown by structure blocks
** Show invisible blocks ‌[JE  only] **

  

This section is missing information about What color was used for structure voids prior to 21w20a? And were there any other changers since their introduction in 1.10 (ignoring the old dark outlines)?. 
Please expand the section to include this information. Further details may exist on the talk page.


Displaysinvisible blocksas small colored cubes. Off by default.
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



** Structure Size **
Enter the X, Y, and Z values to set the distance from the Relative Position coordinates. This sets the opposite corner of the structure, and defines its size.
Maximum structure size is 48x48x48 inJava Editionand 64x256x64 inBedrock Edition.
When successful, generates a white outline surrounding the structure.‌[JE  only]InBedrock Edition, the outline is green, blue, or red (depending on the axis) and the preview design can be used to see every layer of fragmented structure and to change the structure size to be saved.
** Detect structure size and position **
Automatically calculates the size and position of the structure using a corner block placed on the opposite corner of the structure.
The name of the structure in the save blockmustmatch the name within the corner block, or the size calculation fails.
Two corner blocks can also be used. It uses the second corner block instead of the structure block.
** Remove blocks ‌[BE  only] **
While saving the structure and when enabled, this doesn't include anyblockswithin the structure.
** Include entities **
While saving the structure and when enabled, this saves anyentitieswithin the structure as well.
** Save **
When all coordinates and a structure name have been entered, press this button to save the structure.
InJava Edition, this saves the structure to a file. The name of the structure is the name of the file.Structures can be saved to a file only by manually pressing this button. If a structure block in Save mode is instead powered by redstone, the structure is saved only in memory by default. This is the case even if a file for that structure already exists on disk. Reloading the world clears any structures stored in memory. This is for unspecified security reasons.[2]
By default, structure blocks are saved in the minecraft namespace. This can be changed by prefixing the structure name with <namespace>: in the structure block.
Structures are saved in .minecraft/saves/(WorldName)/generated/(namespace)/structures. [note 1]
InBedrock Edition, this saves the structure into level database file rather than a standalone file. And the player can set up the structure block so that it can save into the memory or the disk (level file) when automated with redstone.
** Export ‌[BE  only] **
Used to export a structure into a.mcstructurefile, which can be used to load from thestructuresfolder of a behavior pack. If the structure contains a custom block from a behavior pack, then the block is also saved on the structure block. This option is available only on Android and Windows 10 devices.
### Load
Load Mode GUI for Java Edition
Load Mode GUI for Bedrock Edition
 Load mode allows the player to load and rotate saved structures.

** Structure Name **
The name of the structure to load.
InJava Edition, it can load structures saved to memory or a file (.minecraft/saves/<World Name>/generated/<namespace>/structures/), structures in data pack and inminecraft.jar.To load a structure from a file, simply type <namespace>:<structure_path>.
Structures saved only to memory have a higher priority than structures of the same name that were saved to a file. Structures saved to a file have a higher priority than structures of the same name that is in data pack, which have a higher priority than structures in minecraft.jar.
InBedrock Edition, it can load structures saved to memory or disk (level database), and structures in behavior pack.Structures saved only to memory have a higher priority than structures of the same name that were saved to disk. Structures saved to disk have a higher priority than structures of the same name that is in behavior pack.
Vanilla NBT structure files cannot be loaded with structure block.
** Relative Position **
The X, Y, and Z coordinates of the corner in which to generate the structure, based on the position of the structure block. Coordinates may be defined as numbers between -48 and 48 InJava Edition, or between -64 and 64 InBedrock Edition.
** Show bounding box **
Highlights the outline of the structure; on by default.
** Structure Integrity and Seed **
Removes random blocks that compose the structure based on a user-defined seed.
Lower integrity values result in more blocks being removed. The integrity value must be between 0.0 and 1.0‌[JE  only]/ 100.00‌[BE  only].
** Include entities **
Include any entities saved in the structure file when loading the structure. Off by default.
** Waterlog blocks ‌[BE  only] **
While loading the structure in water, it allows the blocks to bewaterloggedinstead of being replaced with air.
** Remove blocks ‌[BE  only] **
While loading the structure, doesn't include anyblockswithin saved structure.
** Rotation (0, 90, 180, 270) **
Sets the rotation of the structure to 0° (no rotation), 90° clockwise, 180° clockwise, and 270° clockwise (or 90° counter-clockwise).
** Mirror (¦, <>, ^v) **
Sets the mirroring of the structure to none (¦), left to right (< >), or front to back (^ v). At 0° rotation< >mirrors across the X-axis and^ vmirrors across the Z-axis.
InBedrock Edition, the options are x and z, which can be toggled to set mirroring.
** Animation mode ‌[BE  only] **
Select the animation to show how structure is loaded. Place by layer make structure loaded layer by layer, place by block make structure loaded one block by block. Default to none.
Once the loading has started, breaking the structure block can not stop the loading process.
Loading with animation may break blocks in structures that contain multiple parts (such as beds, doors, or tall grass), or need to be attached to other blocks (such as torches), and may cause water, lava, and fire to spread out.
** Animation time ‌[BE  only] **
Adjust the animation time for loading the structure.
** Load **
Load the structure.
InJava Edition, press this button once to prepare the outline preview of the structure. When satisfied with the position, press again to generate the structure.
Structures may also be loaded with the use of redstone.
