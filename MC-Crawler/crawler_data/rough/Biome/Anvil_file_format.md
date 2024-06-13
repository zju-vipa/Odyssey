# Anvil file format
Anvil[1] is a file storage format. It brings a list of changes and improvements over from the previous file format, Region. It was implemented in snapshot 12w07a for release in Java Edition 1.2.1.

## Contents
- 1 Changes from MCRegion
	- 1.1 Further information
- 2 World size reduction post-conversion
- 3 History
- 4 See also
- 5 References

## Changes from MCRegion
Converting a world from MCRegion format to Anvil.
The only changes from MCRegion to Anvil were in the Chunk format; the Region file format is still used, but labeled as Anvil. The Anvil format introduced these changes to the Chunk format:

- Maximum build height has been increased to 256 (from 128).
- Empty sections of the world are not loaded into memory or saved to disk.
- The maximum Block ID has been increased to 4096 (was 256) by adding a 4-bit data layer (similar to how metadata is stored). The rest of Minecraft's code was not prepared to take advantage of this, however mods made use of this.
- Block ordering has been changed from XZY to YZX in order to improve compression.
- Packets for sendingchunkshave been optimized (a chunk withoutairis smaller than in the same chunk in the old format, and a chunk with lots of air is even smaller).
- Biomesare saved per X,Z column, rather than being calculated on the fly, which means they can be altered by tools; this is useful formap makers. It also prevents issues where features within previously generated chunks don't match the biome after the way biomes generate change, usually due to updates or mods. (Also known as "Biome shifting")

### Further information
Versions from 12w07a to 1.17.1 automatically convert worlds to the new format, but a copy of the world files is created in the previous formats for compatibility with older game versions. Previously generated chunks have not been changed, so there is an additional 128 blocks of air above existing terrain, making 192 blocks from sea level to the height limit.

- The 16×128×16 "Blocks", "Data", "SkyLight" and "BlockLight" tags were moved and repurposed. (see below)
- A "Sections" List tag containing Compound tags has been added with up to 16 Compound tags.
- Each section has 16×16×16 "Blocks", "Data", "SkyLight" and "BlockLight" tags.
- Each section has a "Y" Byte tag saying which section it is (note that some Y positions can be skipped). 0 is at the bottom of the world and 15 is the topmost section.
- Each section also has an optional "Add" tag, which is a DataLayer byte array just like "Data". The "Add" tag is not included in the converter since the old format never had block ids above 255. This extra tag is created whenever a block requires it, so thegetTile()method needs to check if the array exists and then combine it with the default block data. In other words,blockId = (add << 8) + baseId.
- Each chunk has a 16×16 byte array withbiome IDscalled "Biomes". If this array is missing it is filled when the game starts, as well any -1 values in the array. The converter source provided for developers doesn't include any biome sources, however.
- Note that the old format is XZY ((x * 16 + z) * 128 + y) and the new format is YZX ((y * 16 + z) * 16 + x) (see the difference between DataLayer and OldDataLayer).
- The new format uses the extension ".mca" instead of ".mcr" (the old format is kept for safety, with the level.dat backed up as "level.dat_mcr").
- A new NBT tag type called IntArray was added to theNBT Format(With ID 11) and is used by the "Heightmap" tag.

Additional information may be found on the Chunk format page.

## World size reduction post-conversion
Anvil world data uses a .mca file extension, while McRegion uses .mcr. The game leaves the old McRegion files after converting a world to Anvil, despite the game never using them again. To reduce the file size of backups, the old McRegion files may be deleted. To do this, perform the following steps:

- Windows:
	1. Open the command prompt (press⊞ WinandRtogether, typecmd, and pressEnter)
	2. Run the following command:del /f /q "[path to world folder]\region\*.mcr"

- Linux and macOS:
	1. Open the terminal
	2. Run the following command:rm -f "[path to world folder]"/region/*.mcr

