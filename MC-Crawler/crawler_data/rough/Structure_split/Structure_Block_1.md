### Corner
Corner Mode GUI for Java Edition.
Corner Mode GUI for Bedrock Edition.
 Corner mode allows for an easier and automatic size calculation while saving or loading structures.

To use, place on the opposite corner of a save structure block or a second corner structure block. Then, using a save block, press "DETECT".
When successful, a bounding outline appears.
** Structure Name **
The name of the structure on which to calculate the size and position.
Name is case sensitive; it must match exactly with the name provided by the complementary save or corner structure block.
### Data
Data mode GUI
 Data mode is a deprecated mode, which is superseded by jigsaw block, but still used in some certain vanilla structures (igloo, end city, woodland mansion, ocean ruin, shipwreck). Structure block in data mode can be used only during natural generation. They mark the location to run a specified hardcoded function, which can be used only for relevant structures. In Java Edition, this mode is hidden unless the Alt key is held while switching from Corner mode. In Bedrock Edition, data mode structure block cannot be obtained with commands.

** Custom Data Tag Name **
The name of the function to run.Igloo
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

** Structure Name **
Enter the name of the structure. Case sensitive. The player must enter a file name in order to export.
** Relative Position **
Enter the X, Y, and Z values for the structure here, based on the position of the structure block. Sets the origin of the structure outline.
Maximum allowed distance from the structure block is 64 blocks in any direction.
** Structure Size **
Enter the X, Y, and Z values to set the distance from the Relative Position coordinates. This sets the opposite corner of the structure, and defines its size.
Maximum structure size is 64×256×64.
** Remove Blocks **
While exporting the structure, doesn't include any blocks within saved structure.
## Data values
### ID
Java Edition:

| Name            | Identifier        | Form         | Block tags                          | Translation key                   |
|-----------------|-------------------|--------------|-------------------------------------|-----------------------------------|
| Structure Block | `structure_block` | Block & Item | `dragon_immune`<br/>`wither_immune` | `block.minecraft.structure_block` |

| Name         | Identifier        |
|--------------|-------------------|
| Block entity | `structure_block` |

Bedrock Edition:

| Name            | Identifier        | Numeric ID | Form                       | Item ID[i 1]   | Translation key             |
|-----------------|-------------------|------------|----------------------------|----------------|-----------------------------|
| Structure Block | `structure_block` | `252`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.structure_block.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

| Name         | Savegame ID      |
|--------------|------------------|
| Block entity | `StructureBlock` |

### Block states
Export Structure Block

See also: Block states

Java Edition:

| Name | Default value | Allowed values | Description            |
|------|---------------|----------------|------------------------|
| mode | `data`        | `corner`       | Corner Structure Block |
|      |               | `data`         | Data Structure Block   |
|      |               | `load`         | Load Structure Block   |
|      |               | `save`         | Save Structure Block   |

Bedrock Edition:

| Name                 | Metadata Bits             | Default value | Allowed values | Values forMetadata Bits | Description               |
|----------------------|---------------------------|---------------|----------------|-------------------------|---------------------------|
| structure_block_type | `0x1`<br/>`0x2`<br/>`0x4` | `data`        | `corner`       | `3`                     | Corner Structure Block    |
|                      |                           |               | `data`         | `0`                     | Data Structure Block      |
|                      |                           |               | `export`       | `5`                     | Export Structure Block    |
|                      |                           |               | `invalid`      | `4`                     | Inventory Structure Block |
|                      |                           |               | `load`         | `2`                     | Load Structure Block      |
|                      |                           |               | `save`         | `1`                     | Save Structure Block      |



