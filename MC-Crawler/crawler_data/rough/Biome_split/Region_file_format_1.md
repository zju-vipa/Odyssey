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


