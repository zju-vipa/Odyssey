# Spawn
Spawning refers to the creation and placement of players and mobs in the Minecraft world.

## Contents
- 1 Player spawning
	- 1.1 World spawn
		- 1.1.1 Bedrock world spawn search
		- 1.1.2 Adventure mode
		- 1.1.3 Location
	- 1.2 Individual spawn
- 2 Natural generation
	- 2.1 Animals
	- 2.2 Monsters
	- 2.3 Other mobs
- 3 Spawn cycle
	- 3.1 Java Edition
		- 3.1.1 Java Edition mob cap
		- 3.1.2 Pack spawning
		- 3.1.3 Spawn conditions
	- 3.2 Bedrock Edition
		- 3.2.1 Bedrock Edition mob cap
		- 3.2.2 Bedrock spawn conditions
		- 3.2.3 Cluster spawning
		- 3.2.4 Structure spawning
- 4 Other types of spawning
	- 4.1 General
	- 4.2 Passive mobs
	- 4.3 Hostile mobs
- 5 Despawning
	- 5.1 Java Edition
	- 5.2 Bedrock Edition
- 6 History
- 7 Issues
- 8 Trivia
- 9 Gallery
	- 9.1 Screenshots
- 10 References
- 11 External links

## Player spawning
### World spawn
World spawning area. White represents the extent of singleplayer, blue represents multiplayer, and yellow represents the world spawn point.
See also: Multiplayer spawning details

New players initially spawn within a small area surrounding the world spawn point when the server is not in Adventure mode. Upon death or return from the End dimension, the player respawns within this area unless the player's individual spawn point changed (by using a bed, respawn anchor, or /spawnpoint ).

This area is 21×21 blocks by default in Java Edition or 5×5 in Bedrock Edition, but can be changed by the spawnRadius gamerule in both single and multiplayer.

Bedrock Edition's Respawn Radius setting interface.
When set to 0, the player spawns in the crosshair of four blocks. When set to 1, the player always spawns on the northwest of those four blocks. The maximum spawn radius is 99999999 blocks but when rejoining the world, it resets to 128 blocks. However, in Bedrock Edition on the discontinued "Old" world type, the maximum spawn radius in 256 blocks instead.

Bedrock Edition's new respawn radius interface.
When the player first loads into the world or respawns, the game searches within the world spawn area and tries to place the player on a random grass block. Upon spawning, the player is placed on the highest valid spawn point block of the X and Z spawn coordinates, regardless of elevation. If a grass block that was invalid, due to being obstructed by a block above it, the game checks the closest two free spaces from below the grass block and the player spawns there. However, if there are no valid grass blocks, the player spawns directly at the world spawn point. The player is still placed at the highest valid block at the world spawn point. This can result in players falling into the void after spawning if there are no blocks at that location.

The world spawn point is also the center of the permanent spawn chunks.

The world spawn point can be changed using the /setworldspawn command.

#### Bedrock world spawn search

  

This section needs to be updated. 
Please update this section to reflect recent updates or newly available information.Reason: Spawn search rules have changed in 1.18; more biomes are available to spawn in.


In Bedrock Edition, when a player creates a new world, the world spawn point is restricted to specific biomes. The algorithm starts searching from coordinate 0,0, continuing outward until an acceptable biome is found for the world spawn point. Using add-ons, a rare biome can be designated to cause the player to spawn at a distant location, but the game crashes if the biome does not exist or cannot generate.

The algorithm searches for these biomes:

- Plains
	- At main plains biome
	- Small islands in anocean(islands are usually a plains biome)
	- Patch of plains next todesert,badlands, orsnowy plains
- Forest
	- At main forest biome
	- Small islands in anocean(islands can also be a forest biome)
- Dark Forest
- Taiga
	- At main taiga biome
	- Patch of taiga next toold growth pine taiga
	- Nearbeach,snowy taiga, orwindswept hills
- Jungle
- Savanna(only regular variants)

The player spawns within a 5-block radius of the point selected in the chosen biome, sometimes resulting in the player spawning outside the intended spawn biome, ending up in a beach, river, or swamp biome. It is also possible (but rare) for a player to spawn initially underwater and start drowning.[1]

A search for a valid world spawn biome is not performed for Flat and Old world-types.

#### Adventure mode
When the server's settings specify the default game mode as Adventure (using the server.properties), then the normal spawning mechanic is ignored, and players are spawned directly on the world spawn point. This includes the X, Y, and Z coordinates, even if there is no block there, and even if there are blocks above it.

If the Y coordinate is not within a valid spawning area, then the server looks up until it finds one, up to a maximum of Y=256. If there is space to spawn, but it is in mid-air, the player spawns in mid-air, even falling into the void if there is a hole.

#### Location
There are several ways to determine the world spawn point:

- Acompass(that hasn't been assigned to alodestone) always points to the world spawn point.
- Doing thecommands/gamerule spawnRadius 0then/kill.
- If commands are disabled, remove all thegrass blocksin the 21×21 spawn area (or place a block above them to make them invalid), make sure the individual spawn point is disabled, and die.
- Entities, other than players, falling into theexit portalinthe Endland exactly at the world spawn point. Items thrown in mark the spot in theOverworld. Players spawn like they normally do, allowing this action to be used to perform the above without dying, and thus can be performed inhardcore mode.
- Mods or external programs, such asNBTExplorerorMCEdit, can also be used to find and set the world spawn point.

