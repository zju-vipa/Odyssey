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
