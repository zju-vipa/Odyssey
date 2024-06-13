#### Passing the night
Sleeping changes the time of day to sunrise and resets the weather cycle, changing the weather to clear conditions. In Java Edition, the weather cycle resets only during rainy or snowy weather. The player wakes up next to the bed, facing the bed.

Sleeping does not accelerate processes that take place over time such as the growth of crops or smelting. If /gamerule doDaylightCycle is false, the player instead wakes up in the night.

To skip the night in multiplayer, all players in the Overworld must be in bed at the same time. Pressing the Leave Bed button is not necessary in this case. The percentage of players that need to sleep to skip the night can be customized with the game rule playersSleepingPercentage.

Villagers are unable to skip the night by sleeping in beds, unlike players.

If the bed is destroyed while the player is in it, due to for example an explosion or by another player, the player wakes prematurely and the night does not pass.

#### Setting the spawn point
Once a player has entered a bed (or right clicked the bed during daytime), their spawn point is set to the location of that bed. In Java Edition, multiple players can set their spawn point on a single bed. In Bedrock Edition, the last player to use a specific bed is the only player who can respawn there, and players who had previously slept there respawn at the world spawn.

Using a bed in the daytime likewise sets the spawn point, without actually entering the bed. 

When a bed explodes, it does not set the spawn point. 

The message "Respawn point set" is displayed in chat when the respawn point is successfully changed.

The check for a bed is made only when the player respawns. This means that the bed can be destroyed and replaced or even reoriented, but as long as there is a bed present in the same location, the player can respawn there. If a player's bed is absent, or if the area around the bed is made unsuitable for respawning (see below), a message is displayed saying "You have no home bed or respawn anchor, or it was obstructed" in Java Edition or "Your home bed was missing or obstructed" in Bedrock Edition, and the player respawns at the world spawn point. 

When choosing where to respawn the player, the northwesternmost (lowest X- and Z-coordinates) location of the seven blocks adjacent to the head of the bed is chosen first. If this location is obstructed, the next choice is to its south (+Z), rather than the east (+X). Only when all seven locations around the head are obstructed are the three remaining ones adjacent to the foot then to be considered. 

For a location to be unobstructed, the block at the level of the bed must be air or non-solid (e.g. torches, but not glass) and there must be a space with a solid block below it and two non-colliding blocks for the player to stand in 0-2 blocks below the bed. It does not matter if the bed itself has blocks above it. Putting a slab one block above a bed can act as a two block tall space, as the bed is half a block tall. The bed never spawns the player on or directly below itself even if all other locations are obstructed. If a bed is obstructed, the player's spawn point is cleared after they respawn. That is, even if the bed is subsequently made usable again, the player continues to respawn at the world spawn until interacting with the bed again. 

Specifically, when interacting with it, the location of the head of the bed is saved as the spawn point, and if a bed is in that space (whether it is the foot or the head) then the respawn works. This can be observed by reorienting the bed with its head in the same location. Interacting with it does not produce a "Respawn point set" message as the game doesn't change the saved spawn point. If a bed is reoriented so that its foot is in this space, it still functions on the next respawn, but it can also be interacted with to update the spawn point to the new head of the bed and cause a "Respawn point set" message. Attempting the reverse, reorienting the bed so that it overlaps the original location of the foot, results in a respawn at world spawn. However, the location of the foot of the bed is also saved. If the bed is moved so that part of it overlaps the original location of the head, it can be observed that the same locations need to be obstructed to stop spawning. It is possible to respawn 2 blocks away from the bed this way.

