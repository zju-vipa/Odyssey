# Commands/locate
Displays the coordinates for the closest generated structure or biomes of a given type in the chat for the player who executed the command. In Java Edition, it can also display for the closest points of interest.

## Contents
- 1 Usage
- 2 Syntax
- 3 Arguments
- 4 Result
- 5 Output
- 6 Examples
- 7 History
- 8 References

## Usage
For /locate structure ..., the vertical coordinate of structure is ignored when finding. In Java Edition, the horizonal search range is 201x201 units of the Structure's spacing (see Default structure sets for values). For example, Mansions have a spacing of 80 chunks, so it can search out ±128,000 blocks before failure. For concentric ring structures like Strongholds, there is no set max distance. Structures in the Anvil chunk region of the command's execution are prioritized over others due to a bug, meaning the found structure is not necessarily the closest.[1]

For /locate biome ..., the horizonal search resolution is 32 blocks, and vertical resolution is 64 blocks, which means biomes that are too narrow may not be found. The horizonal search range is 12801×12801 blocks in Java Edition.[more information needed]

In Java Edition, for /locate poi ..., the search range is a ball with a radius of 256 blocks.

When locating structure or POI, if successful, the following message is sent to chat: "The nearest <requested thing(s)> is at [<x> ~ <z>] (<distance> blocks away)", in which <distance> is the horizontal distance from the executor. 

When locating biome, if successful, the following message is sent to chat: "The nearest <requested biome(s)> is at [<x> <y> <z>] (<distance> blocks away)", in which <distance> is the distance from the executor to the biome. 

In Java Edition, the coordinates in these messages can be clicked, which can put the command /tp @s <x> ~ <z> in the chat box. The command can then be executed, and the player is sent to those coordinates.

## Syntax
- Java Edition

/locate structure <structure>
/locate biome <biome>
/locate poi <poi>
- Bedrock Edition

/locate structure <structure: Structure> [useNewChunksOnly: Boolean]
/locate biome <biome: Biome>
## Arguments
JE : <biome>: resource_or_tag
BE: biome: Biome: enum

Specifies thebiometo locate. InJava Edition, this argument also supports biometags.
InJava Edition, must be an existing registeredresource locationortaginminecraft:worldgen/biomeregistry. InBedrock Edition, must be an ID of abiome(without namespace)
JE (case-sensitive): <structure>: resource_or_tag_key
BE: structure: Structure: enum

Specifies the structure to locate. SeeGenerated structures#Data values.
InJava Edition, must be aresource locationor atag, which is resolved during command execution into an entry or tag inminecraft:worldgen/structureregistry. InBedrock Edition, must be an ID of agenerated structure(without namespace)
BE: useNewChunksOnly: Boolean: enum

Specifies if a structure of any type wants to be located in new chunks only (true) or not (false), and it'sfalseby default.
Must be aBoolean (eithertrueorfalse).
JE : <poi>: resource_or_tag

Specifies the point of interest to locate.
Must be an existing registeredresource locationortaginminecraft:point_of_interest_typeregistry.
The following are resource locations of POIs:


Point of Interest
ID


Blast Furnace

armorer


Bee nest

bee_nest


Beehive

beehive


Smoker

butcher


Cartography Table

cartographer


Brewing Stand

cleric


Composter

farmer


Barrel

fisherman


Fletching Table

fletcher


Bed

home


Cauldron

leatherworker


Lectern

librarian


Lightning Rod

lightning_rod


Lodestone

lodestone


Stonecutter

mason


Bell

meeting


Nether Portal

nether_portal


Loom

shepherd


Smithing Table

toolsmith


Grindstone

weaponsmith

This argument also supports point of interest type tags, as following:


Tag

Includes


#acquirable_job_site

armorer
butcher
cartographer
cleric
farmer
fisherman
fletcher
leatherworker
librarian
mason
shepherd
toolsmith
weaponsmith



#bee_home

bee_nest
beehive



#village

#acquirable_job_site
home
meeting


## Result








| Command                | Trigger                                                                                                                                  | Java Edition | Bedrock Edition |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------------|--------------|-----------------|
| Any                    | The command is incomplete, or any argument is not specified correctly.                                                                   | Unparseable  | Unparseable     |
| `locate structure ...` | The specified resource location or tag is not a valid structure or structure tag.                                                        | Failed       | N/A             |
|                        | The requested structure doesn't generate in this dimension.                                                                              |              | Failed          |
|                        | Unable to locate the requested structure within a square of 201×201 units of the Structure's Spacing.[needs testing in Bedrock Edition]. |              |                 |
| `locate biome ...`     | Unable to locate the requested biome within a square of 12801×12801 blocks[needs testing in Bedrock Edition].                            |              |                 |
| `locate poi ...`       | Unable to locate the requested poi within a ball with a radius of 256 blocks.                                                            |              | N/A             |
| Any                    | Otherwise                                                                                                                                |              | Successful      |

## Output






| Command                              | Edition         | Situation  | Success Count | /execute store success ... | /execute store result ...                                                       |
|--------------------------------------|-----------------|------------|---------------|----------------------------|---------------------------------------------------------------------------------|
| Any                                  | Java Edition    | On fail    | 0             | 0                          | 0                                                                               |
| `locate structure ...locate poi ...` |                 | On success | 1             | 1                          | horizontal distance<br/>between the executor and the requested structure or POI |
| `locate biome ...`                   |                 | On success | 1             | 1                          | distance between the executor and the requested biome                           |
| Any                                  | Bedrock Edition | On fail    | 0             | N/A                        | N/A                                                                             |
|                                      |                 | On success | 1             | N/A                        | N/A                                                                             |

## Examples
- To obtain the coordinates of the nearest woodland mansion:/locate structure mansion
- To obtain the coordinates of the nearest pillager outpost in new chunks only:/locate structure pillager_outpost true‌[Bedrock Edition  only]
- To obtain the coordinates of the nearest village of any kind:/locate structure #village‌[Java Edition  only]//locate structure village‌[Bedrock Edition  only]
- To obtain the coordinates of the nearest desert biome:/locate biome desert
- To obtain the coordinates of the nearest point of interest used by villagers:/locate poi #village‌[Java Edition  only]


