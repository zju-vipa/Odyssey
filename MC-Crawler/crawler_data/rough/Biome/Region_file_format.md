# Region file format
The Region file format is the binary file format for storing Java Edition chunks from Beta 1.3 to release 1.2. Each file stores a group of 32×32 chunks called a region.[a] The format took the place of the Alpha level format, which had been in use since the Infdev development phase, where chunks were stored in individual files on the file system. The file does not begin with a magic number, unlike other file formats, and begins directly with the header. The format has been superseded by the Anvil file format; however, the Anvil file format made changes only to the chunk format and changed the region file extensions from ".mcr" to ".mca".

The system is based on McRegion,[2] a mod by Scaevolus, also known for his development of the Optimine project. The McRegion format was adopted nearly unchanged, except for the addition of a table of chunk update timestamps. JahKob has claimed that this format is up to 7 times faster than the previous system.[3] The difference in a world's total file size between the Region file format and the Alpha level format is negligible.



## Contents
- 1 Location
- 2 Structure
	- 2.1 Header
		- 2.1.1 Chunk location
		- 2.1.2 Chunk timestamps
	- 2.2 Payload
- 3 Migration and level.dat
- 4 See also
- 5 External links
- 6 References
- 7 Notes
- 8 Software

## Location
Region files have names in the form r.x.z.mcr, where x and z are the region's coordinates. The dimension of the region data dictates the sub-directory in which the region files are stored:

- Overworld:save_directory/region
- Nether:save_directory/DIM-1/region
- The End:save_directory/DIM1/region

The coordinates for the region a chunk belongs to can be found by taking the floor of dividing the chunk coordinates by 32, or by bit shifting 5 bits to the right. For example, a chunk at (30, -3) would be in the region (0, -1), and one at (1500, -600) would be at (46, -19).

// division
int regionX = (int) floor(chunkX / 32.0f);
int regionZ = (int) floor(chunkZ / 32.0f);

// bit shifts
int regionX = chunkX >> 5;
int regionZ = chunkZ >> 5;

Reciprocally, the starting block coordinate of a region can be calculated by multiplying the x and z region values (as defined by the region file's name) by 512. Likewise, each chunk's starting block coordinate can be calculated by performing either modulo or floor/integer division to the chunk's index in the header table (0 through 1023) and adding the result to the region's x and z values:

// get region x, z
let region_x: i32 = x * 512;
let region_z: i32 = z * 512;

// get chunk x, z
let chunk_x: i32 = region_x + (header_index % 32 * 16);
let chunk_z: i32 = region_z + (header_index / 32 * 16); // floor or int division, language dependent

## Structure
### Header
Region files begin with an 8KiB header, split into two 4KiB tables. The first containing the offsets of chunks in the region file itself, the second providing timestamps for the last updates of those chunks. 

The offset of a chunk [x, z] (in chunk coordinates) in the first table can be found by using this formula: 4 * ((x mod 32) + (z mod 32) * 32). When using certain languages (such as Java/C/C++), the values of x mod 32 and z mod 32 can be negative. To prevent this, use the AND operator (&) instead of modulo: 4 * ((x & 31) + (z & 31) * 32). Its timestamp can be found 4096 bytes later in the file. 

| byte        | 0x00 - 0x0FFF                          | 0x1000 - 0x1FFF                         | 0x2000...               |
|-------------|----------------------------------------|-----------------------------------------|-------------------------|
| description | locations (1024 entries; 4 bytes each) | timestamps (1024 entries; 4 bytes each) | chunks and unused space |

#### Chunk location
Location information for a chunk consists of four bytes split into two fields: the first three bytes are a (big-endian) offset in 4KiB sectors from the start of the file, and a remaining byte that gives the length of the chunk (also in 4KiB sectors, rounded up). Chunks are always less than 1MiB in size. If a chunk isn't present in the region file (e.g. because it hasn't been generated or migrated yet), both fields are zero.

| byte        | 0 | 1 | 2      | 3            |
|-------------|---|---|--------|--------------|
| description |   |   | offset | sector count |

A chunk with an offset of 2 begins right after the timestamps table.

#### Chunk timestamps
The entries in the timestamp table are individual four-byte big-endian integers, representing the last modification time of a chunk in epoch seconds.

| byte        | 0 | 1 | 2 | 3         |
|-------------|---|---|---|-----------|
| description |   |   |   | timestamp |

### Payload
Chunk data begins with a (big-endian) four-byte signed length field that indicates the exact length of the remaining chunk data in bytes. The following byte indicates the compression scheme used for chunk data, and the remaining (length-1) bytes are the compressed chunk data.

Minecraft always pads the last chunk's data to be a multiple-of-4096B in length (so that the entire file has a size that is a multiple of 4KiB). Minecraft does not accept files in which the last chunk is not padded. Note that this padding is not included in the length field.

| byte        | 0 | 1 | 2 | 3                 | 4                | 5...                             |
|-------------|---|---|---|-------------------|------------------|----------------------------------|
| description |   |   |   | length (in bytes) | compression type | compressed data (length-1 bytes) |

There are currently five defined compression schemes:

| value                          | method                                                                                                                                                       |
|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1                              | GZip (RFC1952) (unused in practice)                                                                                                                          |
| 2                              | Zlib (RFC1950)                                                                                                                                               |
| 3since a version before 1.15.1 | Uncompressed                                                                                                                                                 |
| 4                              | LZ4(since24w04a, enabled inserver.properties)                                                                                                                |
| 127                            | Custom compression algorithm (since24w05a, for third-party servers)A namespaced string must follow representing the algorithm used.[more information needed] |

The uncompressed data is in NBT format and follows the information detailed on the chunk format article; if compressed with compression scheme 1, the compressed data would be the same as the on-disk content of an Alpha chunk file. Note that chunks are always saved using compression scheme 2 by the official client.

If the value of compression scheme increases by 128, the compressed data is saved in a file called c.x.z.mcc, where x and z are the chunk's coordinates, instead of the usual position.

## Migration and level.dat
How Minecraft looks when converting to the new format.
Beta 1.3 converts any "old" chunks into region files before loading the world, rather than incrementally, as they are loaded during play. As part of the conversion, level.dat is updated with TAG_Int("version") (note case) set to 19132. Beta 1.3 also introduces a new level name field, TAG_String("LevelName"). A new TAG_Byte("Sleeping") was introduced in player TAG_Compounds - level.dat in singleplayer, [player name].dat in multiplayer that indicates whether the player is in a bed. It has value of 1 (true) or 0 (false). In Beta 1.8, TAG_Int("GameType") was added. In 1.0.0, TAG_byte("hardcore") was added.

The format of level.dat is otherwise unchanged.

## Notes
1. ↑A total of 1024 chunks can be stored in the format, covering an area of 512×512 blocks.[1]

## Software
The community has developed programs to work with region files:

| Name                   | Description                                                                                                                                                                                                                                                                                                                                    | Screenshot |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| McRegion               | This mod optimizes how chunks are stored on the disk, meaning pauses to load or save a chunk as the player moves around a world become much shorter and less noticeable.                                                                                                                                                                       |            |
| Minecraft Region Fixer | This tool is a python script that tries to fix problems in region files. It can find some typical errors (corrupted chunks, wrong located chunks, too many entities problems), and can fix these errors in various ways (deleting the chunks, replacing them with a backup copy, or relocating the chunk). This is a command-line application. |            |
| MCA2NBT                | A simple Unix command-line utility to convert aMinecraft.mca region file (in anvil format) to a directory with the same basename containing an uncompressed NBT file for each of its chunks.                                                                                                                                                   |            |
| Region Scanner         | AJava Edition 1.7.10(only) Java command line utility to analyze and mass edit region files                                                                                                                                                                                                                                                     |            |

| Version history | Pre-Classic Classic Early Classic Creative Multiplayer Test  Survival Test Late Classic Creative Indev  Infdev Alpha Beta Full Release Development versions |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|

| .minecraft | client.jar version.json client.json launcher_profiles.json options.txt version_manifest.json |
|------------|----------------------------------------------------------------------------------------------|

| Development resources        | Anvil file format Chunk format Command storage format Entity format Generated structures format hotbar.nbt format Item format JSON Level format Map item format Model NBT format Obfuscation map ops.json format Pack format Player format raids.dat format Random sequence format Raw JSON text format Structure file format Schematic file format Scoreboard format Server list format sounds.json Subtitles |
|------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Legacy development resources | Classic level format<br/>Classic server protocol<br/>Indev level format<br/>Alpha level format Infdev 20100624 level format<br/>Infdev 20100624 level format<br/>Region file format<br/>server_level.dat<br/>villages.dat format<br/>                                                                                                                                                                          |

