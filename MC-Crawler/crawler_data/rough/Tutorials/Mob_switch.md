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

#### Nether portals

  

This section needs expansion. 
You can help by expanding it.


Main article: Nether portal § Chunk loading
Another alternative to the spawn chunks is loading the area with nether portals. This section will not describe how nether portal chunk loaders work; for more information, please see the article above.

The best place to store the mobs used in the mob switch is on the border of the 7×7-chunk loaded area: When mobs are placed in the 3×3 chunks centered on the portal, their AI is constantly loaded, which adds a lot of lag to the server. When they are stored in the outermost ring of chunks in the 7×7-chunk area, their AI is no longer processed, but they still count towards the mob cap.

To turn the mob switch off, simply turn off the chunk loader. The mobs will be unloaded, and hostile mobs are again able to spawn in the dimension they are located in.

##### Advantages
- Can be placed anywhere in the world, meaning it can be strategically built in an area not visited frequently by players, saving them from the lag, and preventing them from accidentally despawning the mobs in a lazy mob switch.
- Easier to turn on or off, as it doesn't involve moving mobs physically, allowing shulkers (and withers) to be used.
- Works in both the Overworld and the Nether, depending on the dimension the mobs are stored in. This makes it the only way to build a mob switch in the Nether.

##### Disadvantages
- Nether portal chunk loaders are banned on certain servers.
- There is a chance for the chunk loader to fail, especially during server restarts, or when a singleplayer world is closed and opened again.

### Choice of mob
As mentioned above, most hostile mobs are removed from the mob cap once they are marked persistent, meaning they can't be used for the mob switch. However, some mobs are an exception to this rule, and can therefore be used in a mob switch. They are zombie villagers, shulkers, wardens and withers.

#### Zombie villager

  

This section needs expansion. 
You can help by expanding it.


Normally, zombie villagers despawn like other hostile mobs do. However, due to the bug MC-182304, zombie villagers that have been traded with do not despawn, but count towards the mob cap.

To build such a mob switch, you will need a villager breeder, a job site block, and a zombie to zombify the villagers. Make sure to put blocks over the head of zombie villagers, so they do not burn in the sun (unless they are stored in water). 

A zombie villager mob switch usually consists of a large room to contain at least 70 zombie villagers. If built around the spawn chunks, there needs to be a system that pushes the zombie villagers in and out of the spawn chunks; water is usually the best method, as zombie villagers don't drown unlike normal zombies, and the water additionally prevents them from burning in the sun. Once the first zombie villager is put into the holding chamber, it is typically faster to move more villagers directly into the holding chamber, so that they can be zombified by the zombie villagers already there.

##### Precautions
- Make sure the game is in Hard difficulty while building the mob switch, so that villagers have a 100% chance of being zombified.
- Boats and minecarts can be used to transport the villagers or zombie villagers during the mob switch's construction, but make sure that they arenotin any boats or minecarts when the mob switch is in its finished state, as that removes them from the mob cap.
- Donotuse name tags on any villagers or zombie villagers. This removes them from the mob cap.
- Donotlet the zombie villagers pick up any items, as that removes them from the mob cap.
	- To be safe, once the mob switch is finished, do not break any blocks around the holding chamber, as doing so might risk some zombie villagers picking up the dropped items.

##### Advantages
- Easy to set up, especially if the player already has the infrastructure for breeding and zombifying villagers.
- Works for both the spawn chunk method and the nether portal method.
- Zombie villagers are the least dangerous out of all four types of mobs, as they only deal melee damage to the player.
- Zombie villagers are much easier to transport than the other three types of mobs.

##### Disadvantages
- At least 70 villagers have to be used, which can take a lot of time and food for the villager breeder to produce.
- Utilizes a bug unlike other mob switch designs, meaning it might be patched in future updates.
- The sound can be somewhat annoying, but this can easily be fixed by using resource packs.

#### Shulker

  

This section needs expansion. 
You can help by expanding it.


Main article: Tutorials/Shulker farming
Shulkers are special in that they count towards the hostile mob cap, but do not despawn naturally. This makes them perfect for mob switches. A shulker-based mob switch usually consists of a large chamber where at least 70 shulkers are stored, enclosed on all sides so they do not see nearby players.

To set up a shulker mob switch, one has to transport at least one shulker from the End to the Overworld, transport them to the location where the mob switch will be built, and duplicate them in a shulker farm. More information about transporting and duplicating shulkers can be obtained from the shulker farming tutorial mentioned above.

As with other mobs used in mob switches, make sure not to name tag the shulkers, or keep them in boats or minecarts when the mob switch is finished.

##### Advantages
- Can be set up as a by-product of a portal-based shulker farm, even loaded with the same portal chunk loader that loads the farm.
- Does not utilize a glitch unlike the zombie villager design, so is unlikely to be patched soon, as shulkers have been behaving this way since they were added to the game.
- Works in both the Overworld and the Nether.

##### Disadvantages
- Takes a lot of effort to set up, as shulkers need to be transported from the End and duplicated before the mob switch can be built.
- Shulkers can start shooting and killing each other if the player isn't careful.

#### Warden

  

This section needs expansion. 
You can help by expanding it.


Main article: Tutorials/Warden farming
Wardens are another type of mob that counts toward the hostile mob cap, but can be prevented from despawning. The way to do so is to constantly distract them: when a warden does not detect any vibrations, it despawns after one minute; however, when a vibration is detected nearby, the warden refreshes its despawn timer, and will not despawn for another minute. This behavior can be utilized to create a mob switch.

A warden-based mob switch typically involves a warden farm that produces wardens, a way to transport the warden away so new wardens may spawn, and a holding chamber where a vibration source (such as a note block or a piston) is constantly triggered to distract the wardens and keep them from despawning. The wardens can then be loaded with a nether portal chunk loader. For more information on creating a warden farm, see the warden farm tutorial mentioned above.

An essential component of a warden-based mob switch is a way to remotely turn off the vibration source and kill the wardens, if the player wishes to get rid of the wardens and repurpose the area for something else. It also ensures that if something goes wrong in the building process, the player can safely remove the wardens and rebuild the mob switch without risking getting killed by wardens.

##### Advantages
- Can take a very small amount of effort to set up, if the player knows what they are doing.
- When set up correctly, the player simply needs to AFK on top of the sculk shrieker for long enough until there are enough wardens.

##### Disadvantages
- Wardens are extremely dangerous mobs, so building the mobs switch doesn't allow for much room for error.
- Vibration source may be loud and/or laggy.
- Can only be built in and around a deep dark biome, unless the player intends to transport wardens for long distances.
- Wardens cannot be transported by minecarts, so water streams and bubble columns have to be used.

#### Wither

  

This section of the article is empty. 
You can help by adding to it.


### Lazy mob switch
This variant of a mob switch is unique, since it uses silverfish, which was a fairly useless and annoying mob because of their ability to hide in blocks. This means that this version requires a stronghold.

Advantages

- Requires only a few materials
- Fairly easy to build

Disadvantages

- One must not visit the switch or else all the silverfish will despawn
- Because one must not visit the switch, it must be built to a faraway stronghold, one that won't be visited frequently, which means a lot of exploring is required.
- This mob switch turns off once the player leaves the game, so one must turn it on every single time and travel a long way to have it working again.

## Bedrock Edition

  

This section needs expansion. 
You can help by expanding it.


Unlike in Java Edition, there is not a global mob cap in Bedrock Edition, and it is not possible to load chunks permanently[needs testing], meaning a global mob switch cannot be created. However, by trapping a certain amount of mobs in an area, the local mob cap can be filled, preventing more mobs from spawning nearby.

| Introductory      |                                                                                                                                                                           |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Basics            | Menu screen<br/>Game terms<br/>                                                                                                                                           |
| Newcomer survival | The first day/beginner's guide<br/>The second day<br/>The third day<br/>Hunger management<br/>Things not to do<br/>Simple tips and tricks<br/>Your first ten minutes<br/> |
| Shelters          | Best biomes for homes<br/>Best building materials<br/>Building and construction<br/>Navigation<br/>Shelters<br/>Shelter types<br/>                                        |

| General                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| General                    | Achievement guide<br/>Advancement guide<br/>Best enchantments guide<br/>Breaking a fall<br/>Breaking bedrock<br/>Combat<br/>Complete main adventure<br/>Creating a village<br/>Downgrading<br/>Dual wielding<br/>End survival<br/>Exploring caverns<br/>Gathering resources on peaceful difficulty<br/>Getting food quickly<br/>Headless pistons<br/>Hitboxes<br/>Horses<br/>Indestructible end crystals<br/>Mapping<br/>Measuring distance<br/>Minecraft in education<br/>Mining Diamonds Fossils Ancient Debris<br/>Diamonds<br/>Fossils<br/>Ancient Debris<br/>Nether hub<br/>Nether portals<br/>Nether survival<br/>Organization<br/>Pillar jumping<br/>Playing with a controller<br/>PvP PvP bases<br/>PvP bases<br/>Spawn-proofing<br/>Summoning jockeys<br/>The Void<br/>Time-saving tips<br/>Thunderstorm survival<br/>Units of measure<br/>Village mechanics Trading<br/>Trading<br/>X-ray glitches<br/> |
| Enchanting<br/>andsmelting | Enchanting mechanics<br/>Anvil mechanics<br/>Automatic smelting<br/>Manual smelting<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

| Challenges                |                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| General                   | Acquiring a conduit<br/>Curing a zombie villager<br/>Defeating temples<br/>Defeating a village raid<br/>Defeating a Nether fortress<br/>Defeating a bastion remnant<br/>Defeating a monster room<br/>Defeating a pillager outpost<br/>Defeating a woodland mansion<br/>Defeating a monument<br/>Defeating an End city<br/>Defeating the Ender dragon<br/>Defeating the Wither<br/>Exploring an ancient city<br/>Obtaining every music disc<br/> |
| Non-standard<br/>survival | Adventure survival<br/>Half hearted hardcore<br/>Hardcore mode<br/>Surviving in a single area indefinitely<br/>Infinite desert survival<br/>Island survival<br/>Manhunt<br/>Mob switch<br/>Nomadic experience<br/>Skywars survival<br/>Superflat survival<br/>Flat survival<br/>Ultra hardcore survival<br/>                                                                                                                                    |
| Challenge maps            | Beating a challenge map<br/>Creating a challenge map<br/>                                                                                                                                                                                                                                                                                                                                                                                       |

| Constructions |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Constructions | Adding beauty to constructions<br/>Airlock<br/>Architectural terms<br/>Building a cruise ship<br/>Building a metropolis<br/>Building a rollercoaster<br/>Building safe homes<br/>Building water features<br/>Color palette<br/>Creating shapes<br/>Defense<br/>Desert shelter<br/>Elevators<br/>Endless circling pool<br/>Furniture<br/>Glazed terracotta patterns<br/>Making nice floors<br/>Pixel art<br/>Ranches<br/>Roof types Curved roofs Roof construction guidelines Roof decorations<br/>Curved roofs<br/>Roof construction guidelines<br/>Roof decorations<br/>Secret door<br/>Settlement guide<br/>Underwater home<br/>Walls and buttresses<br/>Water gate<br/>Water-powered boat transportation<br/> |
| Blockbreaking | Blast chamber<br/>Igniting TNT underwater<br/>Wither cage<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

| Farming        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Blocksanditems | Amethyst<br/>Armor<br/>Azalea<br/>Bamboo<br/>Basalt<br/>Bedrock<br/>Blaze rod<br/>Bone meal<br/>Cactus<br/>Chorus fruit<br/>Clay and mud<br/>Cobblestone<br/>Cocoa bean<br/>Copper<br/>Crops (Beetroot, Carrot, Potato, Wheat)<br/>Dirt<br/>Dragon's Breath<br/>Dripstone<br/>Egg<br/>Fern<br/>Fish<br/>Flower<br/>Froglight<br/>Glow berries<br/>Glow ink sac<br/>Glow lichen<br/>Goat horn<br/>Gold<br/>Hanging roots<br/>Honey<br/>Ice<br/>Iron<br/>Kelp<br/>Lava<br/>Meat<br/>Moss block<br/>Mushroom<br/>Music disc<br/>Nautilus shell<br/>Nether growth<br/>Nether vine<br/>Nether wart<br/>Obsidian<br/>Powder snow<br/>Pumpkin, Melon<br/>Rooted dirt<br/>Sculk growths<br/>Scute<br/>Seagrass<br/>Sea pickle<br/>Snow<br/>Soul soil<br/>Sugar cane<br/>Sweet berries<br/>Tree<br/>Trident<br/>Vine<br/>Villager trading hall<br/>Wither rose<br/>Wool<br/>Duplication<br/> |
| Mobs           | Mob farming<br/>Mob grinding<br/>Monster spawner traps<br/>Allay<br/>Animals<br/>Axolotl<br/>Blaze<br/>Cat<br/>Cave spider<br/>Creeper<br/>Drowned<br/>Ender dragon<br/>Enderman<br/>Frog<br/>Goat<br/>Guardian<br/>Hoglin<br/>Iron golem<br/>Magma cube<br/>Phantom<br/>Piglin bartering farm<br/>Raid<br/>Shulker<br/>Slime<br/>Squid<br/>Turtle<br/>Villager<br/>Wandering trader<br/>Warden<br/>Witch<br/>Wither<br/>Wither skeleton<br/>Zombie<br/>Zombie villager<br/>Zombified piglin<br/>                                                                                                                                                                                                                                                                                                                                                                                   |

| Mechanisms            |                                                                                                                                                                                                                                                                                                                                                                  |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Basicredstone         | Automatic respawn anchor recharger<br/>Basic logic gates<br/>Combination locks<br/>Command block<br/>Flying machines<br/>Hopper<br/>Item sorting<br/>Item transportation<br/>Mechanisms<br/>Observer stabilizer<br/>Randomizers<br/>Redstone music<br/>Redstone tips<br/>Rube Goldberg machine<br/>Shulker box storage<br/>Villager trading hall*Water tram<br/> |
| Detectors             | Block update detector<br/>Comparator update detector<br/>Daylight detector<br/>                                                                                                                                                                                                                                                                                  |
| Minecarts             | Train station<br/>Minecarts Storage Storage system<br/>Storage<br/>Storage system<br/>                                                                                                                                                                                                                                                                           |
| Traps                 | Snow golems<br/>TNT cannons<br/>Trapdoor uses<br/>Trap design<br/>Traps<br/>                                                                                                                                                                                                                                                                                     |
| Pistons               | Piston uses<br/>Piston circuits<br/>Quasi-connectivity<br/>Zero-ticking<br/>Instant repeaters<br/>                                                                                                                                                                                                                                                               |
| Advanced<br/>redstone | Advanced redstone circuits<br/>Arithmetic logic<br/>Calculator<br/>Command stats<br/>Hourly clock<br/>Morse code<br/>Printer<br/>Redstone computers<br/>Redstone telegraph<br/>                                                                                                                                                                                  |

| Servers      |                                                                                                                                                                                                                                                                      |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| General      | Playing on servers<br/>Multiplayer Survival<br/>Spawn jail<br/>Griefing prevention<br/>Joining a LAN world with alternate accounts<br/>                                                                                                                              |
| Server setup | Setting up a server<br/>Server startup script<br/>FreeBSD startup script<br/>OpenBSD startup script<br/>Ubuntu startup script<br/>Setting up a Hamachi server<br/>Setting up a Minecraft Forge server<br/>Setting up a Spigot server<br/>Ramdisk enabled server<br/> |

| Technical                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Technical                   | Improving frame rate<br/>Minecraft help FAQ (IRC channel)<br/>Running the data generator<br/>Update Java<br/>                                                                                                                                                                                                                                                                                                                                            |
| Maps                        | Custom maps<br/>Map downloads<br/>Command NBT tags<br/>Falling blocks<br/>Updating old terrain using MCEdit<br/>                                                                                                                                                                                                                                                                                                                                         |
| Resource packs              | Creating a resource pack<br/>Loading a resource pack<br/>Sound directory<br/>                                                                                                                                                                                                                                                                                                                                                                            |
| Data packs                  | Creating a data pack<br/>Installing a data pack<br/>Custom world generation<br/>                                                                                                                                                                                                                                                                                                                                                                         |
| Creating<br/>Minecraftmedia | Creating videos<br/>Livestreaming<br/>                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Game installation           | Installing snapshots<br/>Installing Minecraft Preview and beta versions<br/>How to get a crash report<br/>Installing Forge mods<br/>Custom Minecraft directory<br/>Playing and saving Minecraft on a thumb drive<br/>Playing and saving Minecraft on a thumb drive with the old launcher<br/>Recover corrupted saved world data<br/>Run Minecraft through Google Drive<br/>Save game data to Dropbox (world data only)<br/>Saved data Dropbox guide<br/> |

| Outdated |                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Outdated | Building micro shelters<br/>Custom texture packs<br/>Door-based iron golem farming<br/>End of light mob farms<br/>Far Lands<br/>How to get a crash report<br/>Installing mods<br/>Man-made lake<br/>Managing slimes in superflat mode<br/>Minecart booster<br/>Potion farming<br/>Repeater reboot system<br/>Survival with no enabled data packs<br/>Update LWJGL<br/>Update Minecraft<br/>Village chaining<br/>Water ladder<br/> |

