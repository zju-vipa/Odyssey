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

