# Setting up a Minecraft Forge server
This page will teach the player how to install a Forge server.

## Contents
- 1 1.6 and later
	- 1.1 Information
- 2 1.5 and prior
	- 2.1 Information
	- 2.2 Notice


  

The contents of this page are not supported by Mojang Studios or the Minecraft Wiki. 


This page will teach the player how to install a Forge server.

- 1 1.6 and later
	- 1.1 Information
- 2 1.5 and prior
	- 2.1 Information
	- 2.2 Notice

1.6 and later[edit | edit source]
Firstly, you need the Forge installer, which can be downloaded from the official Forge download page. Once downloaded, launch it and choose option "Install server". If you're installing Forge on a headless server with no graphical interface, run the following command in the directory where you downloaded the jar installer (replace "x.xx.x" with the correct version number for the installer you downloaded):

java -jar forge-x.xx.x-installer.jar --installServer

If you get an error about "Downloading Minecraft server failed, invalid e-tag checksum.", you will need to install a vanilla Minecraft server and then run Forge installer. The vanilla server can be downloaded in its respective page.

If you get an error about "There are already files at the target directory", click on the three dots to choose the current location of your Minecraft server (the video shows this).

Once you started vanilla server (don't forget to change EULA), install Forge and you are done. Now you can launch Forge server by double clicking "forge-version-xx.xx.x.xxxx-version.universal.jar" or using the command below.

### Information
- Minecraft Forge page from video
- Minecraft Forge Files/Releases
- Minecraft Forge website
- Server start text used in the video:

java -Xmx1024M -Xms1024M -jar FORGE_FILE_NAME.jar --nogui
PAUSE

1.5 and prior[edit | edit source]
This tutorial is intended for Windows users, but may be of some use to users who use other operating systems (Mac, Linux)




### Information
- Latest Minecraft Server
- Minecraft Forge 1.5.2
- Minecraft Forge 1.5.1
- Minecraft Forge 1.5
- Minecraft Forge 1.4.7
- Minecraft Forge website
- Server start text:

java -Xmx1024M -Xms1024M -jar SERVER_FILE_NAME.jar --nogui
PAUSE

you can give the server more memory by changing the 1024 to a multiple of 1024

### Notice
If the server start text doesn't work then try renaming the SERVER_FILE_NAME to 'SERVER_FILE_NAME.jar' without the apostrophes.
Or you could use this server start text instead:

java -Xmx1024M -Xms1024M -jar SERVER_FILE_NAME.jar --nogui
PAUSE

If you receive the "Java is not recognized" message, replace "java" with its file location. (e.g.: "C:\Program Files (x86)\Java\jre7\bin\javaw.exe")
The full string would be:

"C:\Program Files (x86)\Java\jre7\bin\java.exe" -Xmx1G -Xms1G -jar FORGE_FILE_NAME.jar --nogui
PAUSE




If you receive the "A problem occured running the Server launcher.java.lang.reflect.InvocationTargetException" message, try downloading and installing JRE 8 and point to it's destination on run. This would look like: 
"C:\Program Files (x86)\Java\jre1.8.0_321\bin\java.exe" -Xmx1G -Xms1G -jar FORGE_FILE_NAME.jar --nogui



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


