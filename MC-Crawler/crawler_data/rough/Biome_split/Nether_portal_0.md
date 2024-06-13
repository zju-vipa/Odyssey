# Nether portal
A nether portal is a manufactured structure that acts as a gateway between the Overworld and the Nether dimensions.

## Contents
- 1 Creation
- 2 Behavior
	- 2.1 Chunk loading
	- 2.2 Portal linkage between Overworld and Nether
		- 2.2.1 Coordinate conversion
		- 2.2.2 Portal search
		- 2.2.3 Portal creation
- 3 Sounds
- 4 Achievements
- 5 Advancements
- 6 Video
- 7 History
	- 7.1 History of the structure itself
	- 7.2 Other historical info
- 8 Issues
- 9 Trivia
	- 9.1 Publicity
- 10 Gallery
	- 10.1 Screenshots
	- 10.2 In other media
- 11 References

## Creation
|  |  |  |  |
|--|--|--|--|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

|  |  |  |  |
|--|--|--|--|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

A nether portal is built as a vertical, rectangular frame of obsidian (4×5 minimum, 23×23 maximum). The four corners of the frame are not required, but portals created by the game always include them, resulting in 4 free/extra obsidian. The obsidian can be placed in any manner, e.g. by placing mined obsidian, by completing a ruined portal, or by casting it in place using lava and water. Adjacent portals can share obsidian blocks. A nether portal cannot be built horizontally like an end portal.

Once a frame is constructed, it is activated by fire placed inside the frame. This creates portal blocks inside the frame, resembling a vortex. The fire can be placed in any manner, including use of flint and steel or a fire charge, the impact of a fireball or small fireball, a lightning strike, or natural spread of fire to flammable material adjacent to the portal. Nether portals can be activated only in the Overworld or the Nether; they cannot be activated in the End and custom dimensions.

The fire must be the last placed block in the structure—a fire on an incomplete frame does not result in the portal activating upon the placement of the last obsidian block.

When a portal is used by a player, if no corresponding portal within range exists in the other dimension, one is created there; see § Portal search and § Portal creation. There is an infinitesimal chance of failure for the corresponding portal to generate in the Nether, leaving the player trapped until death or until another portal can be constructed, either in the Nether or by another player in the Overworld.

## Behavior
Main article: Nether Portal (block)
When a player in the Overworld or the Nether stands in a nether portal block for 4 seconds, the player is taken to the other dimension. The player can step out of a portal before it completes its animation to abort the teleport. However, in Creative, the wait time is one game tick (1⁄20 second) for the player to transfer between dimensions. If there is already an active portal within range (about 128 blocks) in the other dimension, the player appears in that portal. Otherwise, a portal is created at or near the corresponding coordinates. If a portal is deactivated, and the matching portal in the other dimension is used before it is re-activated, a new portal may be created (unless there is another active portal within range). The usual cause for this is when the player's Nether-side portal is deactivated by a ghast, and then the player dies in the Nether, spawns, and then re-enters the Nether through the Overworld-side portal. However, multiple portals can be exploited to farm obsidian.

Most entities can travel through portals, including mobs (except the wither and ender dragon), thrown items, and transportation without passengers (neither mobs nor player)[1], including boats, minecarts and horses. Unlike players, other entities travel through portals instantly, and once they reach the other side, there is a cool-down time for 300 game ticks (15 seconds), in which they cannot go through any nether portals. Therefore, an entity can travel though nether portals again after not touching any nether portal for 15 seconds. In Bedrock Edition, a parrot on the player's shoulder prevents the player from going through the portal.[2]

Zombified piglins have a chance to spawn on the bottom frame of the portal in the Overworld in Java Edition if any nether portal block above receives a block tick. In Bedrock Edition they spawn in certain squares adjacent to the portals in the Overworld, not inside them. Zombified piglins spawned in this way have a full 15-second portal cooldown, meaning they can't go through the portal they are spawned in unless they leave the portal for a while. They spawn twice as often on Normal difficulty as on Easy, and three times as often on Hard difficulty as on Easy. No other mobs can be spawned by nether portals in this way, in any dimension.

Active portals also repel hoglins.

### Chunk loading

  

This feature is exclusive to  Java Edition. 


Main article: Chunk § Chunk loading
Whenever an entity is teleported through a nether portal, the chunk at the linked portal gets load ticked with load level of 30, meaning that it is fully loaded and can process entities. This load level also spreads to adjacent chunks but they get lower for each chunk. This results in 8 more fully loaded "entity ticking" chunks with gradually fewer loaded chunks further out.

These chunks remain loaded for 15 seconds but this timer gets refreshed each time the entity passes through the portal (including mobs wandering through it from either direction). This can be used to permanently load chunks, creating a "chunk loader". Permanently-loaded chunks created using chunk loaders create a considerable amount of lag.

### Portal linkage between Overworld and Nether
See also: Tutorials/Nether portals

The closest portal to the corresponding location receives the player.
A new portal is generated in the closest empty area if no portal is found in range.
