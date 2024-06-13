#### Idle timeout
Each dimension has its own idle timeout. It increases 1 every game tick. If there are players or forceloaded chunks in the dimension, the timeout is reset to 0 and disabled. When entity leaves or enters this dimension, the timeout is reset to 0.

If the timeout reaches 300 game ticks, the dimension stops processing certain actions. These include entity and block entity ticking, ender dragon fight, and global entities (lightning).

#### Others
Some game aspects don't always get processed in loading chunks because there may be other conditions for their progress, which includes the following:

- Chunk tick (including mob spawning)
	- Only chunks with centers within 128 blocks of a player are ticked on every game tick. See alsoTick.
- Entities
	- Hostile mobs instantly despawn if they spawn more than 128 blocks from all players.
		- This includeszombified piglinsatNether portalsandwitchesinwitch huts.
	- Passive mobs do not spawn naturally outside a 240 block X 240 block area around a player.
		- The passive mob spawn cap is limited by the number of friendly mobs loaded into memory, which means that any passive mobs present in the spawn chunks count toward the mob cap and usually prevents friendly mobs from naturally spawning anywhere else in the world. The only exception is when passive mobs spawn as part of a newly generated chunk.
	- See alsoSpawn.

### Exceptions
Events in a chunk may affect blocks in outside chunks. If the outside chunk is inactive, the effects are suspended in most cases. Specifically,

- Block changing on the edge of a block ticking chunk can spread updates to blocks outside the block ticking chunk and make them respond appropriately. The update may be propagated block by block until outside the border chunks, at which time it creates an unknown ticket to continue propagation.
- Block in a chunk with a 33 level can request a scheduled tick, but it does not get processed until the chunk gets a load level of 32 or below.
- Flowing water or lava can spread to the first adjacent block outside a block ticking chunk, but the flow becomes suspended there until the border chunk has a greater load level.
- Fire can spread to the first adjacent flammable block outside the block ticking chunk. Like water and lava, it becomes suspended there. It cannot spread further until the outside chunk gets a level of 32 or below.
- Grass and mycelium can spread to the first adjacent block outside an entity ticking chunk.
- Pumpkin and melon stem growing on the edge of an entity ticking chunk can place their fruits on an adjacent block outside the entity ticking chunk.
- An entity (mob, minecart, arrow, etc.) that attempts to move into a block ticking chunk from an entity ticking chunk becomes suspended as soon as it leaves the entity ticking chunk. When the block ticking chunk gets a greater level, the entity resumes moving.
- Exploding TNT in entity ticking chunks can damage or destroy blocks in a non-entity-ticking chunk.

## Bedrock Edition chunk loading
Main article: Ticking area
All game aspects are active in loading chunks, including chunks within a player's simulation distance and chunks loaded by Commands/tickingarea. Unloaded chunks are unprocessed by the game and do not process any of the game aspects.

Visualization of chunks loaded around a player-occupied chunk (colored magenta).
### Player loaded chunks
Chunks are loaded around the player in a circle with a taxicab distance radius equal to one plus the simulation distance, except for the edges in cardinal directions, where the radius is equal to the simulation distance (see image).

If your simulation distance is set to 4, chunks around the player will be loaded in a taxicab "circle" with a radius of 5 centered on the chunk occupied by the player, but the north, east, south, and west edges will be cut off and have a taxicab radius of 4.

Loaded chunks can also be created with the /tickingarea command.

### Limit
- Entities
	- Mob spawning is evaluated for every chunk within a 6 chunk cylindrical radius of the player that is loaded.

### Exception
Events in a ticking area may affect blocks in outside chunks. If the outside chunk is inactive, the effects are suspended in most cases. Specifically,

- Block changing on the edge of a ticking area can spread updates to blocks outside the ticking area and respond appropriately.
- Flowing water or lava can spread to the first adjacent block in an outside chunk, but the flow becomes suspended there until the outside chunk becomes active.
- Fire can spread to the first adjacent flammable block outside the ticking area. Like water and lava, it becomes suspended there; although visible, its animation does not run, and it cannot spread further until the outside chunk becomes active.
- Grass and mycelium can spread to the first adjacent block in an outside chunk, but the affected block does not actually change its appearance until its chunk becomes active; it then changes instantly. Grass and mycelium cannot spread beyond the first such block, nor from such a block into the ticking area until the outside chunk becomes active.
- Pumpkin and melon stem growing on the edge of a ticking area can place their fruits on an adjacent block in an outside chunk.
- An entity (mob, minecart, arrow, etc.) that attempts to move into an outside chunk becomes suspended as soon as it leaves the ticking area. It remains visible but motionless. When the outside block becomes active, the entity resumes moving.
- Exploding TNT can damage or destroy blocks in an inactive chunk, and unlike other events, its effects are not limited to adjacent blocks. However, secondary effects in the outside chunk are suspended until the chunk becomes active. For instance, if an explosion destroys a block that supported sand or gravel, the sand or gravel does not fall immediately. The same thing happens with items that were attached to destroyed blocks, such as item frames and redstone torches; they do not drop until the chunk is activated.
- Primed TNT launched into an inactive chunk is suspended in mid-air within the first outside block it enters. It disappears until the outer chunk becomes active, at which time it resumes its flight and countdown.

