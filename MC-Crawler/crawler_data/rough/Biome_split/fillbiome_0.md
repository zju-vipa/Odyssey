# Commands/fillbiome
Fills a specified area of a region with a specific biome.

## Contents
- 1 Usage
- 2 Syntax
- 3 Arguments
- 4 Result
- 5 Output
- 6 History

## Usage
Because biomes in a world are stored in cells of 4×4×4 blocks, this command is applied on each selected cell instead of each block.

Although biomes are stored in cells, biome boundaries are slightly fiddled with to make them smooth. So the shape of the region whose biome is actually changed is irregular.

The command only changes the biome, but not the blocks in it. For example, changing a forest to a desert with this command does not change the grass blocks to sand and does not plant cacti, but rabbits spawn in the new "desert" that still looks like a forest.

- This command is used to attempt to change the biome between the two stone blocks to desert.
- As shown here, the biome changes are not applied at the exact coordinates specified.

## Syntax
/fillbiome <from> <to> <biome>
The fillbiome command also has an optional alternate syntax when using the replace option:

/fillbiome <from> <to> <biome> replace <filter>
## Arguments
<from>: block_pos and <to>: block_pos

The two corners to fill the biome between.
Must be ablock positioncomposed of<X>,<Y>and<Z>, each of which must be an integer or atilde and caret notation.
<biome>: resource

Specifies the biome to fill the specified area with. SeeBiome § Biome IDsfor a list of vanilla biome IDs.
Must be an existing registeredresource locationinminecraft:worldgen/biomeregistry.
<filter>: resource_or_tag

Specifies the biomes in the fill region to be replaced. If not specified, replaces all biomes in the fill region.
Must be an existing registeredresource locationortaginminecraft:worldgen/biomeregistry.
## Result





| Command | Trigger                                                                                    | Java Edition |
|---------|--------------------------------------------------------------------------------------------|--------------|
| Any     | The command is incomplete, or any argument is not specified correctly.                     | Unparseable  |
|         | The specified region is unloaded or out of the world.                                      | Failed       |
|         | The volume of the specified region is greater than`commandModificationBlockLimit`gamerule. |              |
|         | Otherwise                                                                                  | Successful   |

## Output



| Command | Edition      | Situation  | Success Count | /execute store success ... | /execute store result ...                     |
|---------|--------------|------------|---------------|----------------------------|-----------------------------------------------|
| Any     | Java Edition | On fail    | 0             | 0                          | 0                                             |
|         |              | On success | 1             | 1                          | the number of cells whose biomes are replaced |


