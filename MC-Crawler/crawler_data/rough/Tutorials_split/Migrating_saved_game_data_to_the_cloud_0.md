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

