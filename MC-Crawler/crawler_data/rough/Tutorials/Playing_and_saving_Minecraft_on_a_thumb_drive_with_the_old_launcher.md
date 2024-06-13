# Tutorials/Playing and saving Minecraft on a thumb drive with the old launcher
This guide aims to make Minecraft on a portable USB drive with the 1.6 or lower version launcher. If you have the 2.0 launcher or above, please see this guide.

## Contents
- 1 Introduction
- 2 Instructions for Windows
	- 2.1 Setup
	- 2.2 Additional Notes
- 3 Instructions for Linux
	- 3.1 Setup
- 4 Instructions for OS X
	- 4.1 Setup
	- 4.2 Playing
- 5 Alternative Methods
	- 5.1 Cryshal's Method
	- 5.2 HiWiki's Method
		- 5.2.1 Portable Java Variant
- 6 Video Tutorial

## Introduction
You will need about 8 GB minimum of space in the directory/portable drive. A <8 GB drive/directory can be used, but this is not advised because you will quickly run out of space after saving a couple of worlds. You may need more space if there are mods, larger worlds or texture packs installed. 

## Instructions for Windows
WARNING: If anything in the following guides is not done correctly, Minecraft may crash or fail to start

#### Setup
All folder and file names in the Windows guide are case sensitive.

1. Insert your drive into your computer, and open it.
2. Create a folder, name itMinecraft Portableand enter the folder.
3. In  Minecraft Portable, create two new folders and name themLauncherandData. Use the exact names specified.
4. Download the Minecraft launcher.
	- You can download it from thisdirect link
5. Add the launcher/client to the portable drive:
6. Copy the Minecraft.exe to theLauncherfolder that you have created on the portable drive.

This section will guide you on copying your game data (worlds, saves data, resource packs, server list, etc.) onto the portable drive. If you do not want to copy your game data, you may skip this section.

The .minecraft folder contains all of your current game data.

- PressWindows+R
	- Type%appdata%and pressEnter.
- Locate your.minecraftfolder and copy it
- Copy the.minecraftfolder and paste it into theDatafolder

Now that all the data files are in the directory, a batch file will need to be created. 

1. Open Notepad.
2. Copy and paste the following:

@echo off
set APPDATA=%CD%\data
"%CD%\Launcher\Minecraft.exe"

3. Now click File > Save As...

4. Navigate into your Minecraft Portable folder (not Data).

5. Name this file "StartMinecraft.bat"

Note: Make sure to include the quotation marks ("") and choose "All Files" for the "Save As Type" field, or else Notepad will try to correct it to StartMinecraft.bat.txt and it will open as a text file rather than an executable script. 

If you are getting an error stating that the system cannot find Minecraft.exe/.jar, use this script if you are using Minecraft.exe.

set appdata= D:\Games\PortableMinecraft\Data\
cd /d "D:\Launcher"
start Minecraft.exe 
pause

Use this script if you are using Minecraft.jar.

set appdata= D:\Games\PortableMinecraft\Data\
cd /d "D:\Launcher"
java -jar Launcher\Minecraft.jar 
pause

#### Additional Notes
- To install resource packs or mods onto the portable drive, use the.minecraftfolder of that portable drive.
- If you would like to have multiple .minecraft ("Data") folders in order to quickly switch to an older version of Minecraft or play with mods, make multiple "Data" folders, with different names ("1.6.4", "Modded", and so forth) and a batch file for each one. You may have to make a second "Drive" folder if you want to use 1.5.2 or before, as that uses an older launcher.

## Instructions for Linux



Warning 
The following instructions may require administrative or superuser privileges, and can possibly cause damage to your system. Proceed with caution.


#### Setup
Assume that the portable drive is at /dev/sdb1 and that Minecraft is installed at ~/games/.minecraft.

- Note: You may need to use a different directory name depending on your distribution and set-up.

Run the following in a terminal:

- Note: The following commands require may require superuser privileges. Make sure you are running these as root or are using sudo.
- Note: Text following the#symbol are comments, and can be omitted for that line.
- Note: 'cd ~/.minecraft/' is the same as 'cd /home/user/.minecraft/'

umount /dev/sdb1
mkdir /media/minecraft
mount /dev/sdb1 /media/minecraft
mkdir /media/minecraft/games # If there is a folder called games in your portable drive, skip this command
cp -rn ~/games/.minecraft /media/minecraft/ # This might take a while
cd
umount /dev/sdb1
rm /media/minecraft # Check to make sure that your portable drive is not mounted!

After that, to launch Minecraft, enter the following in the terminal with superuser privileges.

umount /dev/sdb1
mkdir ~/games # If there is a folder called games in your home directory, skip this command
mount /dev/sdb1 ~/games # You will not be able to play any games that are saved in the ~/games directory

Run the Minecraft launcher to start playing.

Or use this script:

mv ~/.minecraft ~/.minecraft.bak
cp -a minecraft ~/.minecraft
java -jar minecraft.jar
mv minecraft minecraft.bak
cp -a ~/.minecraft minecraft
rm -r minecraft.bak
rm -r ~/.minecraft
mv ~/.minecraft.bak ~/.minecraft

## Instructions for OS X



Notice 
This guide does not make Minecraft truly portable, as it requires you to copy the game data from and to the portable drive each time you play.


#### Setup
- 
	- Locate your Minecraft files. Press Command+Shift+G while in finder and then paste ~/Library/application support/minecraft into the dialog.
	- Copy that minecraft folder in your application support folder.
	- Insert in your portable drive and make 2 folders in it, named Data and Launcher.
	- Paste your minecraft folder into the "data" folder in the portable drive.
	- Drag your launcher into the "launcher" folder
	- Remove your portable drive

#### Playing
Once you are done setting up, you can test if your Minecraft can start on another Mac.

- 
	- Insert your portable drive into another Mac to test
	- Open the launcher folder and move the Minecraft launcher into your Applications folder.
	- Double click the launcher to run it. Then after Minecraft loads, exit it.
	- Again, go to Users/USERNAME/Library/Application Support
	- In "Application Support", delete the minecraft folder.
	- Move the minecraft folder in your data folder on your portable drive to the desktop.
	- Then drag it from your desktop into application support.
	- Run Minecraft again.

Or use this script:

mv ~/Library/Application Support/.minecraft ~/Library/Application Support/.minecraft.bak
cp -a minecraft ~/Library/Application Support/.minecraft
open Minecraft.app
mv minecraft minecraft.bak
cp -a ~/Library/Application Support/.minecraft minecraft
rm -r minecraft.bak
rm -r ~/Library/Application Support/.minecraft
mv ~/Library/Application Support/.minecraft.bak ~/Library/Application Support/.minecraft

## Alternative Methods
WARNING: The following methods will only work in Windows.

### 
Doesn't work, minecraft still runs from the appdata folder, Minecraft Profile Manager is useless, and java will not run from the flash drive.

Instructions

- First, create a folder named, say, "Flash MC".  Then, go on over to getjPortablewhich lets you run Java right on your flash drive, without it being installed on the computer.

- You will want to install that onto your flash drive in a directory like \Flash MC\jPortable.

- Then, go toMinecraft Profile Manager's thread, and download it.
- Put it into your Portable MC folder.  Follow the instructions. (Put minecraft.exe into the same folder that it is in)
- You should now be able to launch MPM, make a profile and download all the needed Minecraft files to play.

### 
Instructions

1. Make two folders namedbinanddata
2. Place the Minecraft client insidebinfolder
3. If you use a .jar it will still be placed in thebinfolder
4. PressWindows+Rto open run and type in the dialog box %appdata% then copy the .minecraft folder (Also include other folders that also included in minecraft such as .aether)
5. Select those folders then pressCtrl+C(orCtrl+Xif you want to move the files rather than copy it)
6. Go into Notepad and copy\paste the following:

SET appdata=%CD%\data
bin\minecraft.exe

- But if you use a Jar, put this instead:

SET appdata=%CD%\data
bin\minecraft.jar

- And if you use a Jar/Exe with a different name such as Minecraft-launcher put this

SET appdata=%CD%\data
bin\<name of launcher>.<jar/exe>

- Then you are all done!

Additional notes

- You will need Java for this, but if you also want java in your Flash/Thumb/USB drive, see the section titledAdd Portable Javabelow.
- Any data you have in your .minecraft in appdata will also be in your Flash/Thumb/USB drive

#### Portable Java Variant
You will need an extra 500MB in your Drive for this to work!

Now you have done the above, time to add portable Java! 

1. Go to [[1]]
2. Then open PortableApps.com_Platform_Setup_11.2.exe then wait until you see the add apps section
	- Make sure you place the setup in the Flash/Thumb/USB drive!
3. Then in utilities find and tick the boxes jPortable, jPortable Launcher, jPortable Browser switch then press install
4. Then wait for it to install then after that, your'e done!

How to open jPortable

- First, find the folder PortableApps in your Flash/Thumb/USB drive
- Then double click start, Then press jPortable Launcher
- A window will open, then find the jar (Don't worry if it shows jar can be opened only change it to all files then find your exe)
- Then after that press open then your minecraft will open

Issues and how to fix them

- The minecraft directory is not there, if that happens then press edit profile then find and locate your data folder in file explorer then right click it then press properties
	- Also in the edit profile window tick theGame directorybox
	- Now a window should open, so you will Select the text by dragging in theLocationLine then paste it in theGame directorybox then include this \.minecraft or paste it in theGame directorybox

Credits

This part was made by HiWiki. If there are any issues in this guide, please PM that user. The original source can be found in this thread.

Changing the launcher file to use an autorun script

If you are using an autorun.inf instead of using

set appdata=%CD%\data
bin\minecraft.exe

or

set appdata=%CD%\data
bin\minecraft.jar

change the file to this:

set appdata="Minecraft portable\data"
cd "Minecraft portable\drive\"
Minecraft.jar

Save the file as "Autorun.inf" (do NOT save it as Autorun.inf.txt)

## Video Tutorial

A video tutorial showing the step-by-step procedure on how to make Minecraft portable and run it from a USB thumb drive without Java installed



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

