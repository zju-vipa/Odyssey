# Tutorials/Mob switch
Mob spawning can be irritating and dangerous; however, with the creation of a mob switch, you can disable mob spawning in a certain area without lighting anything up, or covering everything in slabs. In Java Edition, mob spawning can even be disabled in an entire dimension with the help of chunk loading. Without further ado, let's look into the mechanics of how to create one in your world or server!

## Contents
- 1 Java Edition
	- 1.1 Basic mechanics
	- 1.2 Options for chunk loading
		- 1.2.1 Spawn chunks
			- 1.2.1.1 Advantages
			- 1.2.1.2 Disadvantages
		- 1.2.2 Nether portals
			- 1.2.2.1 Advantages
			- 1.2.2.2 Disadvantages
	- 1.3 Choice of mob
		- 1.3.1 Zombie villager
			- 1.3.1.1 Precautions
			- 1.3.1.2 Advantages
			- 1.3.1.3 Disadvantages
		- 1.3.2 Shulker
			- 1.3.2.1 Advantages
			- 1.3.2.2 Disadvantages
		- 1.3.3 Warden
			- 1.3.3.1 Advantages
			- 1.3.3.2 Disadvantages
		- 1.3.4 Wither
	- 1.4 Lazy mob switch
- 2 Bedrock Edition

## Java Edition
### Basic mechanics

  

This section needs expansion. 
You can help by expanding it.


In Minecraft, there is a global mob cap for each dimension: in a singleplayer world, the mob cap for hostile mobs is at 70, meaning there can only be 70 hostile mobs loaded in a dimension, and no more hostile mobs may spawn until enough mobs despawn or die, so that number gets below 70; this is to ensure that the world is not flooded with mobs. On multiplayer servers, the mob cap increases by 70 for each player online, unless it is altered through commands. 

The basic premise of a mob switch is to keep a certain number of hostile mobs loaded in the world, so that the game fails to spawn more hostile mobs. This mechanic can already be demonstrated by passive mobs: In a singleplayer world, the mob cap for passive mobs is 10, but normally there are way more than 10 animals within the player's render distance, meaning it is practically impossible for passive mobs to spawn naturally after a chunk has been loaded. Passive mobs in Java Edition don't despawn, but count towards the mob cap, meaning their presence acts as a natural "mob switch" for passive mobs.

Unlike passive mobs, it is very difficult to create or find a hostile mob that doesn't despawn, but also counts towards the mob cap. This is because mobs no longer count toward the mob cap if they are marked persistent. The most common way to prevent a mob from despawning is to use a name tag on a mob, but doing so removes the mob from the mob cap, and therefore cannot be used in a mob switch. Similarly, a mob may pick up an item or enter a minecart or boat, all of which prevents it from despawning but also removes it from the mob cap. Only a few hostile mobs are exempt from this rule: for more information, see the "Choice of mob" section.

Note that the mob switch is specific to each dimension, depending on the dimension that the mobs are stored in. Mob switches can be built in both the Overworld and the Nether, but because there is no practical means to load chunks permanently in the End, a mob switch cannot be created in the End.

### Options for chunk loading
#### Spawn chunks

  

This section needs expansion. 
You can help by expanding it.


Main article: Spawn chunk
The spawn chunks is a 23×23-chunk area around the world spawn point, where the chunks are constantly loaded as long as the player is in the Overworld, or at all times on multiplayer servers. If enough persistent mobs are placed in the spawn chunks, mobs are prevented from spawning elsewhere in the Overworld. 

The extent of the spawn chunks.
The best place to store mobs in Overworld is on the edge of the spawn chunks, so that mobs can be moved in and out of the spawn chunks, turning the mob switch on or off. On the image to the right, the mobs need to be stored in the light blue colored chunks, and moved into the gray colored chunks to turn the mob switch off.

##### Advantages
- Can be easier to set up, especially if there is a village near the world spawn point (for the zombie villager method).
- More reliable than nether portal chunk loaders, as there is a chance for the latter to fail.
- Does not create more lag, as the spawn chunks are loaded by the game anyway.
- In servers that do not allow nether portal chunk loaders, this is the only viable method.

##### Disadvantages
- Only works for the Overworld, as there are no spawn chunks in the Nether.
- In servers with spawn protection, cannot be constructed by players without the admin's permission.
- Since the spawn chunks are frequently visited by players on a server, this can create a lot of lag.
- Mobs need to be physically moved in and out of the spawn chunks for the mob switch to be turned on or off, which is impossible for shulkers since they can't move, and difficult for dangerous mobs such as withers and wardens.

