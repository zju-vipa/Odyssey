# Tutorials/Migrating saved game data to the cloud
Here is a quick tutorial on how to migrate your saved games to the cloud so you can play your levels wherever you may be.

## Contents
- 1 NOTE
- 2 Download and Install Dropbox
- 3 Copy your Minecraft saved data to your Dropbox folder
	- 3.1 Windows
	- 3.2 MacOS
	- 3.3 Linux
- 4 Create the Symbolic Links
	- 4.1 Windows
	- 4.2 MacOS
	- 4.3 Linux

## NOTE
This guide assumes that you only want one integrated Minecraft save directory. If you wish to have separate directories (e.g., for other machines: Minecraft/Linux, Minecraft/Windows, Minecraft/Toaster, etc.), then you should create them on Dropbox and change the instructions here as needed. This guide also will only sync your saved game files, not any .jar customizations (such as mods) or texture packs. If you don't know what those are, then you're probably safe. Note also that you should be careful only to play on one machine (as server) at a time using the shared save folder, otherwise you risk corrupting your saved worlds. (This warning is applicable if, for example, you and your friend share a save directory from different machines. It is unlikely to be a problem if you are only using the machines yourself.)

## Download and Install Dropbox
The first step is to download Dropbox. Dropbox is a nifty little tool that automatically syncs content to their servers and allows you to access it both online and through a client on your PC. The good thing about Dropbox is that it is cross-platform, plus available on the web and web-enabled smartphones. (Note: you can also use another cloud storage program that has a downloadable client [folder that syncs to the web], such as Google Drive, etc.)

Go to https://www.dropbox.com. You get 2GB for free automatically.

Once you have installed Dropbox, you'll need to know where the Dropbox folder is:

- On Windows XP, the Dropbox folder is located inside the user's "My Documents" folder. The easiest way to reference this is using the environmental variables, as follows:"%UserProfile%\My Documents\Dropbox". Because "My Documents" contains a space, the quotation marks are required.
- On Windows 7 and 8, the default Dropbox folder location isC:\Users\username\Dropbox. Use the environmental variables%UserProfile%\Dropbox.
- On Linux, the default location is in the user's home folder. For example, in Ubuntu, that folder is located at~/Dropbox
- On MacOS, it should also be in the user's home folder.

Whichever operating system you are using, Dropbox has very good documentation and can assist you in finding help: http://www.dropbox.com/help

## Copy your Minecraft saved data to your Dropbox folder
Next, we will need to make a copy of your Minecraft saved game data on the cloud Dropbox server. For the purposes of this tutorial, we will be copying the saves folder from the .minecraft folder into a folder called Minecraft inside your Dropbox folder. You can store it elsewhere in your Dropbox if you choose.

### Windows
On Windows, your Minecraft data folder is in your application data folder. You can access this by holding Windows+R or hitting Start > Run and then typing %AppData%\.minecraft in the box. This will open your minecraft folder. Copy the folder named saves to the desired location in your Dropbox. In this tutorial, we will be creating a folder called Minecraft in the main Dropbox folder and storing the saves folder inside that.

Once these files are done copying, navigate back up to your .minecraft folder, and rename the saves folder to saves-backup. This step ensures that you 1) Have a backup of your files in case of a catastrophe, and 2) allows us to make the symbolic link to the correct location in a later step.

### MacOS
In MacOS, the Minecraft data folder is located in your Username > Library > Application Support folder. You can get here quickly by opening Finder → Go → Go To Folder → type ~/Library/Application Support/minecraft. For future reference, it's best to make an alias for this folder and copy it to your desktop.

Now, copy the saves folder to the desired location in your Dropbox.  It is a good idea to rename the original saves folder (in your minecraft Application Support folder) to saves-backup, to be saved as a backup in case something goes haywire. It also allows us to make the symbolic link to the correct location in a later step.

### Linux
In Linux, your Minecraft data folder is located in your user home folder. However, it may be hidden from view. If you are using a GUI, ensure that you choose View > Show Hidden Files.

Copy the contents of the save folder to your Dropbox. As mentioned above, in this tutorial we create a folder inside the dropbox called Minecraft to store the saves folder in.

Once the copy is complete, rename the saves folder to saves-backup.

If you're command line savvy, here are the above steps in command line format.


mkdir -p ~/Dropbox/Minecraft
cp -r ~/.minecraft/saves ~/Dropbox/Minecraft/saves
mv ~/.minecraft/saves ~/Dropbox/saves-backup



## Create the Symbolic Links
This is the final step that will allow users to use the cloud versions of their files.

### Windows
** GUI **
Creating symbolic links in Windows is easy thanks to a free application calledLink Shell Extension, which will allow you to create a symbolic link via right-click in Explorer.
Note:If you are running Windows XP, you may need to install the Server 2003 resource pack in order to enable symbolic links, which is availablehere.
1. Move your Minecraft saves folder (located in%appdata%\.minecraft) to a folder in your Dropbox.
2. Right-click on this new folder and choosePick Link Source.
3. Go back to your Minecraft folder's original location, then Right-click somewhere blank and clickDrop As… → Junction,
4. and you are all set to pull your game data off the cloud.

** Command Prompt **
1. right click on cmd.exe and press run as administrator.
2. In cmd.exe, type:cd %appdata%\.minecraft\
3. In cmd.exe, type:mklink /d /j "saves" "<dropbox_path>\Minecraft\saves"
4. The console will output “Symbolic link created” if everything succeeded.

### MacOS
** GUI **
Creating symbolic links in MacOS is also easy thanks to a free application calledSymbolicLinker, which will allow you to create a symbolic link via right-click in the Finder. If you'd rather use the command line, instructions are below.
1. Download and install SymbolicLinker.
2. Once installed, move your Minecraft saves folder (located in '~/Library/Application Support/minecraft) to a folder in your Dropbox.
3. Right-click on this new folder and chooseMake symbolic link. This will create a symbolic link in the same folder.
4. Move this back to your Minecraft folder's original destination (make sure it has the same name as the original),
5. and you are all set to pull your game data off the cloud.

** Terminal **
1. Open the Terminal
2. Type in:ln -s ~/Dropbox/Minecraft/saves ~/Library/Application\ Support/minecraft/saves

If you moved your Dropbox to something other than the default location you’ll need to modify that first path.

### Linux
** GUI **
Open two file browser windows, one showing your Dropbox folder and the other showing the minecraft folder.
After you dragged and dropped thesavesfolder over to Dropbox, drag it back and hold Alt while dropping it. This should create a symlink.
** Terminal **
To create the symbolic links in a terminal, type the following into a Terminal:
ln -s ~/Dropbox/Minecraft/saves ~/.minecraft/saves
Now your saved worlds should all be there when you start Minecraft.
In order to link any additional computers you wish to play on, you just need to follow these steps: install Dropbox, and create the symbolic links. Voilà!

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

