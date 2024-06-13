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




