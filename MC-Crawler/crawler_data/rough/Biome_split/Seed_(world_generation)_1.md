## Technical
### Realms
In Java Edition, a player can type /seed in the chat. In Bedrock Edition, the seed is not visible when playing on Realms.

### General
If the seed contains characters other than numbers or is greater than or equal to 20 characters in length, the Java String.hashCode() function is used to generate a number seed. This restricts Minecraft to a subset of the possible worlds to 232 (or 4,294,967,296), due to the int datatype used. Number seeds or a default world seed must be used to access the full set of possible worlds (264, or 18,446,744,073,709,551,616).

### Overlap between editions
All Java and Bedrock Edition seeds in the range from -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807, generate the same terrain and biomes in both Java and Bedrock editions, although with differing structures, decorator placements, carver caves, and mob spawns.

### Generation quirks

  

This section is missing information about Explain these phenomena considerably more in depth. 
Please expand the section to include this information. Further details may exist on the talk page.


Through certain seeds, it is possible to observe interesting effects.

#### Changing terrain without changing some structures
Only certain sections of the seed are used to generate specific features within the world. It is possible to generate multiple worlds with identical cave systems, Nether biomes and other arrangements of generated structures simply by converting the seed into binary and tweaking the desired bits.[5] An example is the seed generator using only the first 48 bits to generate cave systems and badlands clay banding layers.

#### Repetition

  

This section needs to be updated. 
Please update this section to reflect recent updates or newly available information.Reason: Was this fixed in Caves & Cliffs: Part II? If not, please replace the seeds with the new one.


Seed 164311266871034 in spectator mode. Caves are repetitive along the Z axis.
Seed 1669320484 in Bedrock Edition, with repeating canyons.
Certain seeds return 0 in the internal code,[6] causing infinite arrays of caves and other structures to generate.[7] In Java Edition, the seed 107038380838084 returns 0 on the first call and 164311266871034 returns 0 on the second call, causing mineshafts, caves and underwater ravines to loop on the X and Z axes respectively.[8]

Features in seeds can repeat, such as decorations. These generate diagonally.[9]

In Bedrock Edition, diagonal cave, ravine, dungeon, and decoration repetition occur with the seeds 289849025 and 1669320484.[10] Mineshaft generation repeats vertically in the seeds -1171867832 and 1000686894.[11]

Any seed calculated as 4294967296 × n + 1669320484 also generate maps with repeating features.[10]


