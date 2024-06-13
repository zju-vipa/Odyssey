# Chunk
A chunk is a 16×16 segment of a world. Chunks are the method used by the game to divide maps into manageable pieces. They are divided in 16-block tall sections, which are also often called "subchunks".

## Contents
- 1 Description
- 2 Chunk loading
- 3 Java Edition chunk loading
	- 3.1 Tickets
	- 3.2 Level and load type
	- 3.3 Level propagation
	- 3.4 Ticket types
	- 3.5 Limitations
		- 3.5.1 Ticking
		- 3.5.2 Idle timeout
		- 3.5.3 Others
	- 3.6 Exceptions
- 4 Bedrock Edition chunk loading
	- 4.1 Player loaded chunks
	- 4.2 Limit
	- 4.3 Exception
- 5 Finding chunk edges
- 6 Slime chunks
- 7 History
- 8 Trivia
- 9 See also
- 10 References

## Description
Chunks are 16 blocks wide, 16 blocks long. They extend from the bottom void of the world, all the way up to the top sky. In vanilla Overworld, their building height are 384 blocks, and they have 98,304 blocks total. In vanilla Nether and the End, building heights are 256 blocks.

Chunks generate around players when they first enter the world. The generating and loading progress are displayed on the loading world screen‌[Java Edition  only]. As they wander around the world, new chunks generate as needed.

Chunks generate with the help of the map seed, which means that the chunks are always the same if you would use the same seed again, as long as the map generator and version number remain the same.

## Chunk loading
Since Minecraft worlds are 30 million blocks in each cardinal direction and contain an extreme number of chunks, the game loads only certain chunks in order to make the game playable. Unloaded chunks are unprocessed by the game and do not process any of the game aspects.

The game always loads the entire chunk when it decides a chunk needs to be processed. The division into sections is only used for display purposes (e.g. to limit the amount of data to transfer to the game client) and certain game mechanics (e.g. village mechanics).

In Java Edition, the spawn chunks are always loaded. The spawn chunks make up a square, centered at the world spawn, which goes out a certain number of chunks in the 4 cardinal directions. This number is called spawn chunk radius, and can be set using the game rule spawnChunkRadius‌[upcoming: JE 1.20.5]. The default spawn chunk radius is 10 chunks‌[until JE 1.20.5] 2 chunks‌[upcoming: JE 1.20.5]. Spawn chunks can be used in many ways, such as for making automatic farms.

## Java Edition chunk loading
### Tickets
Loading starts when a chunk receives a ticket. All loaded chunks originate from the ticket. Each load ticket has three properties: Level, Ticket type and (optional) Time to Live.

### Level and load type
Levels are numbers that determine what load type the chunk is in. A lower level represents higher a load type. For a given chunk, it may get different level from different tickets, but only its lowest level matters.

Load levels range from 22 to 44 in regular gameplay, while only 22 to 33 are relevant to chunk loading. Load levels less than 22 are valid but possible only with a modded game. Load levels above 44 are instantly unloaded in vanilla.

There are four chunk load types; each load type has different properties. This excludes unloaded chunks.

| Load Type |                | Level        | Properties                                                                                                                                              |
|-----------|----------------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
|           | Entity Ticking | 31 and below | All game aspects are available.                                                                                                                         |
|           | Block Ticking  | 32           | All game aspects are available except that entities are not naturally spawned and not processed (but are still accessible) andchunk ticksaren't either. |
|           | Border         | 33           | No game aspects are available, but entities and blocks are still accessible (can be detected or modified).                                              |
|           | Inaccessible   | 34 and above | No game aspects are available nor accessible, butworld generationoccurs here.                                                                           |

### Level propagation
Load levels "propagate" or flow from source chunk with a ticket to neighboring chunks, but each time it increases its level by 1 until the maximum of 44.

The chunks that get load level from level propagation activate the assigned load type.

| 34 | 34 | 34 | 34 | 34 | 34 | 34 |
|----|----|----|----|----|----|----|
| 34 | 33 | 33 | 33 | 33 | 33 | 34 |
| 34 | 33 | 32 | 32 | 32 | 33 | 34 |
| 34 | 33 | 32 | 31 | 32 | 33 | 34 |
| 34 | 33 | 32 | 32 | 32 | 33 | 34 |
| 34 | 33 | 33 | 33 | 33 | 33 | 34 |
| 34 | 34 | 34 | 34 | 34 | 34 | 34 |

| IN | IN | IN | IN | IN | IN | IN |
|----|----|----|----|----|----|----|
| IN | BO | BO | BO | BO | BO | IN |
| IN | BO | BT | BT | BT | BO | IN |
| IN | BO | BT | ET | BT | BO | IN |
| IN | BO | BT | BT | BT | BO | IN |
| IN | BO | BO | BO | BO | BO | IN |
| IN | IN | IN | IN | IN | IN | IN |

