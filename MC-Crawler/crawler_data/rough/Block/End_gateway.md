# End gateway
End gateways are intradimensional portals generated in the End: some are spawned around the central island after each death of the ender dragon; others are randomly generated throughout the outer islands.

On the central island, up to 20 gateways can be spawned. These can send the player far away to the outer islands, each of which has a corresponding gateway that returns the player back to the central island. There are other randomly-generated gateways that always lead the player back to the obsidian platform. They provide quick access to the different parts of the End dimension.

## Contents
- 1 Generation
	- 1.1 By defeating the dragon
		- 1.1.1 On the central island
		- 1.1.2 On the outer islands
	- 1.2 By natural generation
- 2 Construction
- 3 Behavior
- 4 Sounds
- 5 Data values
	- 5.1 ID
	- 5.2 Config
- 6 Advancements
- 7 History
- 8 Issues
- 9 Trivia
- 10 Gallery
	- 10.1 Screenshots
- 11 See also
- 12 References

## Generation
20 End gateways with beacons to mark their positions.
An example of End gateway generation shown on a graph in X-Z coordinates.Blue dots: gateways on the central island.Red dots: gateways on the outer islands.Lines: the connections between gateways.
### By defeating the dragon
#### On the central island
A group of 20 End gateways can be spawned around the edge of the central island, one at a time by defeating the dragon. Their configuration resembles a perfect circle, equally distributed, surrounding the island at Y-level 75, at a distance of 96 blocks (regardless of angle) away from the center (0,0) in random order. 

These gateways are referred in the game as END_GATEWAY_DELAYED. They function by sending the player far away to the outer islands, in the exact direction that that gateway is located relative to the island center (0,0).

They do not regenerate after the ender dragon has been defeated 20 times.

The position of these gateways are always fixed, as is shown below:

| Number | Position         |
|--------|------------------|
| 1      | x:96 y:75 z:0    |
| 2      | x:91 y:75 z:29   |
| 3      | x:77 y:75 z:56   |
| 4      | x:56 y:75 z:77   |
| 5      | x:29 y:75 z:91   |
| 6      | x:-1 y:75 z:96   |
| 7      | x:-30 y:75 z:91  |
| 8      | x:-57 y:75 z:77  |
| 9      | x:-78 y:75 z:56  |
| 10     | x:-92 y:75 z:29  |
| 11     | x:-96 y:75 z:-1  |
| 12     | x:-92 y:75 z:-30 |
| 13     | x:-78 y:75 z:-57 |
| 14     | x:-57 y:75 z:-78 |
| 15     | x:-30 y:75 z:-92 |
| 16     | x:0 y:75 z:-96   |
| 17     | x:29 y:75 z:-92  |
| 18     | x:56 y:75 z:-78  |
| 19     | x:77 y:75 z:-57  |
| 20     | x:91 y:75 z:-30  |

The order in which these gateways are created as dragons are killed depends on the world seed.

#### On the outer islands
Each of the 20 gateways on the central island spawns an additional gateway that is connected to itself, after having been activated once. These gateways are located much further away, reaching out in all directions to the outer islands in the End dimension. They still arrange in a circular way, but the distances of them to the central island varies, depending on how far is the first land that they contact.

Their function is to send the player back to the original gateway in the central island that it links itself.

** Details **
The game first draws a line with a length of 1024 blocks from the center (0,0) through the north-west corner of the activated gateway. If the chunk at the end of the line contains any blocks above Y=15, the line is progressively shortened by 16 blocks until a chunk is found with no such blocks or the line reaches a length of 768. Then, if the chunk at the end of the line has no blocks above Y=15, the line is progressively lengthened by 16 blocks until a chunk is found with any such block or the line reaches a length of 1280.

Once a chunk is selected, it is scanned for any End stone blocks at or above Y=30 that have two non-full blocks[1] above. If such a block exists the south-east corner of the chunk is selected,[2] or if no such block exists in the chunk then a small island is generated at the end of the line at Y=75 and that position is selected. The position is then moved to the highest full block within ±16 on the X and Z axes (favoring the north and west in case of ties) and a gateway structure is generated 10 blocks above that position.

Knowing this, the position of the exit gateway can be manipulated. However, once an End gateway on the central island has been activated, it is indefinitely linked to the position of the generated gateway on the outer island. Changing the position of the outer gateway is then no longer possible.

### By natural generation
Another group of gateways are generated randomly throughout the outer End islands (in the End Highlands in Java Edition), where there are an unlimited number of them. They are referred in the game as end_gateway_return.

Their function is similar to the ones that teleport the player back to the central island, but instead they always send them back to the obsidian platform, allowing for an easy and quick travel back to the central island. Unlike through end portals, entities that teleport through end gateways in this fashion do not cause the obsidian platform to regenerate.

## Construction
Main article: /Structure
The end gateway is composed of an end gateway block confined within a vaguely octahedral formation made up of twelve bedrock.

## Behavior
Main article: End Gateway (block)
A magenta   beam shoots out vertically from the top and bottom of the gateway when it is generated. The beam disappears after 10 seconds. When an entity enters the gateway, the gateway emits a purple   beam instead for 2 seconds. In addition, this purple beam also emits automatically every 2 minutes (2400 game ticks).[3]

The bedrock arrangement prevents the player from entering the gateway directly. Throwing an ender pearl or flying with elytra straight into the end gateway block teleports the player to the outer End islands. Players can also access the inside of an end gateway by constructing a water channel leading into it and sprint-swimming through the channel and into the gateway, or by crawling.‌[Java Edition  only]

Once the gateway is activated, another end gateway generates in the outer end islands near to where the player is teleported; this gateway teleports the player back to the original gateway, providing a way to return to the main island. 





















































































































































11 × 11 horizontal teleportation range



In Java Edition, the position where the player or entity lands after teleporting is determined by a systematic algorithm: the gateway searches for a full block that isn't bedrock, starting from the north-west corner at the topmost height (Y=255) within a 5 block radius around the gateway block (shown as the block of gold in the image on the right). If there is a block at that position, then the entity is teleported onto that block. If there is no block, then the next position along the Z-axis is searched (shown as the block of lapis lazuli in the image on the right). This continues along each column in an 11×11 area at the same Y-level with the exception of blocks above, below, or directly adjacent (including diagonals) to the gateway block. If there are no blocks, it moves one Y-level down and repeats the sequence from the north-west corner again. It continues doing this until every height is checked, and if there are no blocks within any of these points it always teleports the entity exactly two blocks above the gateway block.

In Bedrock Edition, end gateways teleport the player using a different algorithm, but the exact details are not known.[more information needed] A few notable differences are:

- Entities can land onto slabs and other partial blocks. Converesely, there seem to be certain situations where a teleport location is not considered valid.
- Entities can land considerably farther away from the gateway than an 11×11 area.
- If there are no valid locations, the game generates a small floating island near the gateway, and the entity lands on this island.

Unlike nether portals or end portals, end gateways allow entities with passengers (e.g. a player in a boat, a shulker in a minecart) to go through it.

## Data values
### ID
Java Edition:

| Feature type        | Identifier    |
|---------------------|---------------|
| [No displayed name] | `end_gateway` |

| Configured feature  | Identifier            |
|---------------------|-----------------------|
| [No displayed name] | `end_gateway_delayed` |
| [No displayed name] | `end_gateway_return`  |

Bedrock Edition:

| Feature             | Identifier |
|---------------------|------------|
| [No displayed name] | `[No ID]`  |

### Config
Main article: Configured feature
Java Edition:

- config
	- exactWhether the gateway should teleport entities in the exact exit position.
	- exit(optional) The block position where the gateway should exit.
		- X coordinate.
		- Y coordinate.
		- Z coordinate.




An example

{
  "type": "minecraft:end_gateway",
  "config": {
    "exact": true,
    "exit": [
      100,
      50,
      0
    ]
  }
}



