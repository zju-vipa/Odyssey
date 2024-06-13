### Ticket types
There are different ticket types, which come from various sources.

** Player ticket **
This ticket is caused by the player and is assigned level 31. A player ticket is given to each chunk within a square region surrounding the chunk where the player is located, as defined by the formulas described below, and propagates as described in the table above.

In singleplayer, "Render Distance" in options decides the side length of the square. It follows the formula l=2r+1, where r is the selected render distance, and l is the side length (in chunks) of the square.

In multiplayer, "view-distance" configured in server.properties decides the side length of the square. It also follows the same formula l=2r+1 where r is the configured "view-distance" and l is the side length of the square region.

For example, in a single-player game with a "Render Distance" of 5 chunks, a region of 11×11 chunks centered around the player has a load type of entity ticking (level 31). The strip of chunks at the outer edge of a 13×13 perimeter surrounding the player have block ticking (level 32), and the next enclosing chunks (15×15 perimeter) are border chunks (level 33).

** Forced ticket **
A ticket can also be created by using the /forceload command. It has a level of 31, so its propagation can be seen in the table above.

Chunks remain force-loaded even after exiting and re-entering the level.

** Start ticket **
Propagation of start ticket‌[until JE 1.20.5]
Ticket created by the world spawn for the chunk it is located at, loading a 23 by 23 chunk area known as the "spawn chunks". Its position can be changed by a /setworldspawn command. It has a level of 22, the lowest in the game.

**  Portal ticket **
Ticket created when an entity is teleported through a nether portal, given to the chunk at the other side of the portal. It has a level of 30, so it is stronger than the player/force loaded ticket.

It expires after 300 game ticks (equivalent to 15 seconds). Because they are created each time an entity passes through the portal, it is possible to create a "chunk loader". Perpetually keeping chunks loaded without the player being near, which can be used for various in-game mechanics such as farms, but can create lag.

**  Dragon ticket **
Ticket created at the start of the battle with the ender dragon and is given to the 0,0 chunk. It has a level of 24.

It expires if there are no players within a Euclidean distance of 192 blocks from (0.0, 128, 0.0), or the dragon dies.

** Post-teleport ticket **
Ticket created when entity is teleported either by going through the end portal or using /teleport or /spreadplayers commands. The /spreadplayers and /teleport command has a level of 32, whereas, for the end portal, it has a level of 33.

It expires after 5 game ticks.

** Unknown ticket **
When the game needs to immediately use the data of a chunk, but the chunk has not yet been created or generated to required step, the game automatically gives a ticket named "unknown" to the chunk. It expires after 1 game tick (0.05 seconds). The load level depends on the step to which the game needs the chunk to generate, and it is always greater than 32. It is in various game calculations, such as mob AI, mob spawning, etc.

It expires after 1 game tick.

For example, when a generic mob wandering AI is executing, it asks if a certain block has a solid top surface. As part of that check, that chunk has an "unknown" ticket with level 33 placed on it. Similarly, commands such as /clone, /data, /execute (if|unless) (block|blocks|predicate), /fill and /setblock generate an unknown ticket when reading data from or writing it to a previously loaded chunk; if run every tick, they can prevent the chunk from unloading until the world is reloaded.[1]

** Light ticket **
The light ticket is only used for world generation, and has a level of 33. A chunk gets a light ticket when starting the light step of chunk generation, to ensure that it is accessible to calculate light. After the light calculation is completed, this ticket is removed.

### Limitations
#### Ticking
Though respective game aspects are available if a chunk is loaded to a certain level, whether these game aspects are processed depends not only on chunk loading. It is also subject to some other restrictions.

Chunk loading caused by a player ticket allows entities to be ticked only if the chunk is in a square around the chunk which has the player ticket, as defined by the formulas described below. Entity despawning is not affected by this.

In singleplayer, "Simulation Distance" in options decides the side length of the square. It follows the formula l=min(2s+1,63), where s is the selected simulation distance, and l is the side length (in chunks) of the square.

In multiplayer, "simulation-distance" configured in server.properties decides the side length of the square. It also follows the same formula l=min(2s+1,63) where s is the configured "simulation-distance" and l is the side length of the square region.

Chunk loading caused by a player ticket allows block entities to be ticked and scheduled tick and chunk tick (without mob spawning) to be processed only if the chunk is in the aforementioned square region along with a one-chunk-thick square frame surrounding this region. That is, a square region with side length of l=min(2s+3,65).

For example,

- With a simulation distance of 5 and a render distance of 10, entities move normally within a 11×11 chunk column around the player chunk. One more chunk out, within a one-chunk-thick square frame surrounding this region, redstone and command blocks still run, fluids flow, and crops grow. Zombies stop despawning naturally beyond 21×21 chunks.
- With a simulation distance of 5 and a render distance of 5, entities move normally within a 11×11 chunk column around the player chunk. One more chunk out, within a one-chunk-thick square frame surrounding this region, redstone and command blocks still run and fluids still flow, but crops stop growing. Zombies won't despawn because they are unloaded before being 128 blocks away from the player.
- With a simulation distance of 5 and a render distance of 2, entities move normally within a 5×5 chunk column around the player chunk. One more chunk out, within a one-chunk-thick square frame surrounding this region, redstone and command blocks still run and fluids still flow, but crops stop growing. Zombies won't despawn.

Technically, the above game aspects are controlled by another different ticket system named ticking ticket.

