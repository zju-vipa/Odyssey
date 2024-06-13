# Commands/locatebiome
Displays the coordinates for the closest biome of a given biome ID or a biome tag in the chat for the player who executed the command.

## Contents
- 1 Syntax
- 2 Arguments
- 3 Note
- 4 Result
- 5 Output
- 6 Example
- 7 History
- 8 References

## Syntax
locatebiome <biome>
## Arguments
<biome>: resource_or_tag

Specifies the biome(s) to be located. SeeBiome/IDfor a list of available biome IDs.
Must be an existing registeredresource locationortagin correct registry.
## Note
The horizonal search resolution is 32 blocks, and vertical resolution is 64 blocks, which means biomes that are too narrow may not be found.

If successful, the following message is sent to chat: "The nearest <biome name> is at [<x> ~ <z>] (<distance> blocks away)"/"The nearest <biome tag> (<biome name>) is at [<x> ~ <z>] (<distance> blocks away)", in which <distance> is the horizontal distance between the executor and the biome. The coordinates can be clicked, which can put the command /tp @s <x> ~ <z> in the chat box. The command can then be executed, and the player will be sent to those coordinates.

## Result




| Command | Trigger                                                                                      | Java Edition                                                                 |
|---------|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| Any     | the arguments are not specified correctly                                                    | Unparseable                                                                  |
|         | unable to locate the requested biome or biome tag within a square of 12801×12801 blocks area | Failed                                                                       |
|         | Otherwise                                                                                    | Displays the coordinates for the closest biome of the given type in the chat |

## Output



| Command | Edition      | Situation  | Success Count | /execute store success ... | /execute store result ...                              |
|---------|--------------|------------|---------------|----------------------------|--------------------------------------------------------|
| Any     | Java Edition | On fail    | 0             | 0                          | 0                                                      |
|         |              | On success | 1             | 1                          | horizontal distance between the executor and the biome |

## Example
- To obtain the coordinates of the nearest desert:/locatebiome desert


