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

