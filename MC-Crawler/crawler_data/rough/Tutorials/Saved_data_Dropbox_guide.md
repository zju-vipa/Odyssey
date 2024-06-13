# Tutorials/Saved data Dropbox guide
This tutorial explains how to migrate your saved games to Dropbox so you can play your levels on multiple computers. BE WARNED that you can only play on one computer at a time, and you must allow Dropbox to completely finish syncing before starting to play on a different computer.  If you do not, you risk losing your progress or possibly corrupting your save.

## Contents
- 1 Download and Install Dropbox
- 2 Move your Minecraft Saved Data to your Mega Folder
	- 2.1 Windows
		- 2.1.1 Alternate (command line) method
	- 2.2 macOS
		- 2.2.1 Alternate (command line) method
	- 2.3 Linux
		- 2.3.1 Alternate (command line) method
- 3 Create the Symbolic Links
	- 3.1 Windows
		- 3.1.1 Windows Vista, 7, 8, and 10
		- 3.1.2 Windows XP (after installing junction.exe)
	- 3.2 macOS
		- 3.2.1 Alternate (command line) method
	- 3.3 Linux
- 4 Note on Multiple Operating Systems
- 5 Alternate Method

## Download and Install Dropbox
The first step is to download Dropbox. Dropbox automatically syncs content to their servers and allows you to access it both online and through a client on your PC. Dropbox is cross-platform, plus available on the web and web-enabled smartphones.

Go to http://www.dropbox.com, register for a free account, download the application and install it. You automatically get 2GB for free.

Once you have installed Dropbox, you'll need to know where the Dropbox folder is:

- On Windows XP, the Dropbox folder is located inside the user's "My Documents" folder. The easiest way to reference this is using the environmental variables, as follows:"%HomeDrive%%HomePath%\My Documents\Dropbox". Because "My Documents" contains a space, the quotation marks are required.
- On Windows 7 and 8, the default Dropbox folder location isC:\Users\username\Dropbox. Use the environmental variables%HomeDrive%%HomePath%\Dropbox.
- On Windows 10, the Dropbox folder is labeled as its own item in the sidebar of the File Explorer window.
- On Linux, the default location is in the user's home folder. For example, in Ubuntu, that folder is located at ~/Dropbox
- On MacOS, it should also be in the user's home folder.

Whichever operating system you are using, Dropbox has very good documentation and can assist you in finding help: http://www.dropbox.com/help

## Move your Minecraft Saved Data to your Mega Folder
Next, we will need to make a copy of your Minecraft data on the Dropbox server and then rename the original.

### Windows
On Windows, your Minecraft data is saved in your application data (AppData) folder. You can access this by holding Windows+R or hitting Start > Run and then typing %AppData%\.minecraft in the box. If the folder doesn't open, click on the Tools menu on Windows Explorer, click the View tab, and under Advanced Settings, make sure "Show hidden files, folders and drives" is selected.

Copy all the files in this folder to your Dropbox folder. For organization sake, I usually create a subfolder inside my Dropbox folder and title it "Minecraft".

Once these files are done copying, navigate back up to your AppData folder, and rename the .minecraft folder to .minecraft2 (for files that begin with a "." such as ".minecraft" Windows may give an error message when renaming and refuse to rename. If this happens try to rename the file to ".minecraft2."; this will rename the file to ".minecraft2" without the previously typed period at the end of the title.)

This step ensures that you:

1. Have a backup of your files in case of a catastrophe, and
2. Allows us to make the symbolic link to the correct location in a later step.

#### 
xcopy /I /E %AppData%\.minecraft %HomeDrive%%HomePath%\Dropbox\Minecraft
cd %AppData%
rename .minecraft .minecraft2
Note: attempting to use rename %AppData%\.minecraft %AppData%\.minecraft2 will give the error The syntax of the command is incorrect., as should be: rename %AppData%\.minecraft .minecraft2 

### macOS
In macOS, the Minecraft data folder is located in your Username > Library > Application Support folder. You can get here quickly by opening Finder > Go > Go To Folder > type ~/Library/Application Support/minecraft. For future reference, it's best to make an alias for this folder and copy it to your desktop. NOTE: Mountain Lion hides the user's Library folder. Hold down the option key and see the Library item appear in the GO menu.

Now, copy the saves directory (~/Library/Application Support/minecraft/saves/) to your Dropbox's Minecraft folder (~/Dropbox/Minecraft/), unless you already have saves from Windows or Linux there.

#### 
mkdir ~/Dropbox/Minecraft/
cp -r ~/Library/Application\ Support/minecraft/saves ~/Dropbox/Minecraft/
mv ~/Library/Application\ Support/minecraft/saves ~/Library/Application\ Support/minecraft/saves.old

### Linux
In Linux, your Minecraft data folder is located in your user home folder. However, it may be hidden from view. If you are using a GUI, ensure that you choose View > Show Hidden Files.

Copy the contents of the .minecraft folder to your Dropbox folder. As mentioned above, I usually create a folder inside the Dropbox called "Minecraft".

Once the copy is complete, rename the .minecraft folder to .minecraft2

#### 
Open the Terminal and type in:

cp -r ~/.minecraft ~/Dropbox/Minecraft
mv ~/.minecraft ~/.minecraft2

## Create the Symbolic Links
This is the final step that will allow us to create links to the online versions of your files.

### Windows
Symbolic links are similar to shortcuts but are much more powerful. In Windows, the command mklink or junction will allow us to create a symbolic link. 

Open an elevated command prompt. In Windows 7 and 8, you can do this by searching for "Command Prompt", right-clicking it and selecting "Run as administrator." This is necessary even if you are the administrator on your machine. Otherwise, you will receive the response "You do not have sufficient privilege to perform this operation", and creation of the symbolic link will fail.

Type the following command to set up the symbolic link:

#### 
WARNING: Use caution when creating or deleting hardlinks on Vista and before! Hardlinks create an alias reference to file data. Deleting a hardlink on Vista or XP will also delete the associated data.

Java Edition:
mklink /d "%AppData%\.minecraft" "%HomeDrive%%HomePath%\Dropbox\Minecraft"

If you get the error Cannot create a file when that file already exists, make sure the .minecraft folder in %AppData% has been deleted or renamed. mklink tries to make a "folder" named .minecraft and, if a file or folder of the same name already exists, can't replace it.

Bedrock Edition:
mklink /J "%UserProfile%\AppData\Local\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\minecraftWorlds" "%HomeDrive%%HomePath%\Dropbox\Minecraft"

Deleting a Hardlink

To disconnect a hardlink on Vista or XP use this command instead of delete:

fsutil reparsepoint delete <path>

This will remove the link but leave an empty file of the same name in its place which you can then safely remove. (Verify the folder is empty before you delete it.)

On Windows 7 and 8 you can safely delete a hard link with windows explorer.

#### 
If you are running Windows XP, you first need to download junction.exe from SysInternals and place it in your root folder in order to enable symbolic links. http://download.sysinternals.com/files/Junction.zip

Open the command prompt and type in:

junction "%AppData%\.minecraft" "%HomeDrive%%HomePath%\My Documents\Dropbox\Minecraft"

If you are successful, the .minecraft folder should reappear in your AppData folder. When you start Minecraft after this, you should have all your previously generated worlds!

### macOS
Creating symbolic links in macOS is easy thanks to a free application called SymbolicLinker, which will allow you to create a symbolic link via right-click in the Finder. 

Download and install SymbolicLinker, available here: [1] (free). 

Once installed, move your Minecraft folder (located in ~/Library/Application Support/) to a folder in your Dropbox. Rightclick on this new folder and choose Make symbolic link. This will create a symbolic link in the same folder. Move this back to your Minecraft folder's original destination (make sure it has the same name as the original) and you are all set to pull your game data off the internet.

#### 
Open the Terminal and type in:

ln -s ~/Dropbox/Minecraft/saves ~/Library/Application\ Support/minecraft/saves

### Linux
To create the symbolic links in Linux, open up the terminal and type the following commands.

ln -s ~/Dropbox/Minecraft ~/.minecraft

Now, the .minecraft folder should be listed in your home directory and your saved worlds should all be there when you start Minecraft.

In order to link any additional computers you wish to play on, you just need to follow these steps: install Dropbox, and create the symbolic links. Voilà!

## Note on Multiple Operating Systems
If you wish to sync your Minecraft files between different operating systems, you need to add a few extra steps to the method above. This is because the bin folder inside your minecraft folder, which contains binary files which run the program (as opposed to data files, like your saved games) has different files depending on your operating system. These files, however, have no overlap, and you can have a fully operational Minecraft folder for all operating systems (Windows, Mac OS and Linux). There are no known problems arising from different versions of the same operating system.

To make this work, take a look at the subfolder bin/natives. It has different contents depending on your Operating System.

- Windows
	- OpenAL32.dll
	- jinput-dx8_64.dll
	- OpenAL64.dll
	- lwjgl64.dll
	- jinput-raw_64.dll
	- jinput-dx8.dll
	- lwjgl.dll
	- jinput-raw.dll
- Linux
	- libopenal64.so
	- liblwjgl64.so
	- libjinput-linux64.so
	- libopenal.so
	- liblwjgl.so
	- libjinput-linux.so
- macOS
	- liblwjgl.jnilib
	- libjinput-osx.jnilib
	- openal.dylib
	- libopenal.dylib

All you have to do is to go through your different installations (in the operating systems you use) and put these files all together in the same existing natives folder, like so:



Then sync it away with Dropbox, it works no problem! :)

If you use third-party mods to the game, you must install all desired mods only once, and then synchronize the patched result. In the unlikely (but possible) case that you run into problems, you should NOT share the bin folder (with its natives subfolder) anymore. Mods known to work cross-platform seamlessly include Zombe's modpack, Mine Little Pony, and MCPatcher.

## Alternate Method
Go to this link and follow the directions, but instead of putting the "minecraft" folder on the thumb drive, move it to your Dropbox folder. Just run the .bat file when you want to play, and you're done! To install mods, texture packs, or maps, you must use the .minecraft folder in the Dropbox folder. 

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

