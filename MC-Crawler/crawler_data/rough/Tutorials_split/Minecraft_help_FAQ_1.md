#### Update instructions
- AMD users: Use theAMD Driver Autodetectutility to automatically find your driver. Alternatively, use AMD'sGPU supportwebpage to find the appropriate driver.
- Intel users: Use theIntel Driver Update Utilityto automatically find your driver. Alternatively, use Intel'sDownload Centerto find the appropriate driver.
- Nvidia users: Use Nvidia'sSmart Scanutility (Java required) to automatically find your driver. Alternatively, use Nvidia'sDownload driverswebpage to find the appropriate driver.

## Common Questions
### How to Back Up Minecraft Worlds
While in Minecraft, select the world you wish to backup and click edit. You will then have the option to create a backup, which will be saved in /.minecraft/backups as a .zip file.

### Setting up a Server
Go here for information on setting up a server.

### 
Download this script and run the following commands in a terminal:

sudo chmod 755 ~/Downloads/minecraft_installer.sh
sudo sh ~/Downloads/minecraft_installer.sh --install_client

### 
Install proxychains and use a configuration file such as:

$ cat ~/.proxychains/proxychains.conf
strict_chain
[ProxyList]
http <proxyHost> <proxyPort>

Then run Minecraft through proxychains:

$ proxychains java -jar Minecraft.jar

### Syncing worlds across multiple computers
All of your single-player worlds are stored in the saves folder within your installation folder. There is a subfolder for each world.

#### Using a USB stick
Main article: Tutorials/Playing and saving Minecraft on a thumb drive
#### Automatic syning using Google Drive
Main article: Tutorials/Run Minecraft through Google Drive
#### Automatic syncing via Dropbox
Main article: Tutorials/Saved data Dropbox guide

  

This section needs to be updated. 
Please update this section to reflect recent updates or newly available information.Reason: Windows 10 instructions



  

It has been suggested that this section be merged with Tutorials/Saved data Dropbox guide. [discuss]
If this merge affects many pages or may potentially be controversial, do not merge the page until a consensus is reached.


The following steps will link your .minecraft/saves folder with a Dropbox account. The way in which you do this depends on your OS. Please note that dropbox provides 2GB of free storage, after which you will have to pay a monthly subscription fee to expand your storage. Google Drive gives you 15GB of free storage.

The following steps assume that you have set Dropbox up to use the default folder and that you have not changed the .minecraft folder. Make sure that Minecraft and the Minecraft Launcher are closed before proceeding.

##### 
1. Open a terminal window.
2. Paste the following into your terminal:

mv ~/.minecraft/saves ~/Dropbox/Minecraft; ln -s $HOME/Dropbox/Minecraft $HOME/.minecraft/saves

1. Close the terminal

##### macOS
This takes advantage of some of the UNIX underpinnings of the OS. 

1. Open a terminal window.
2. Paste the following into your terminal:

mv ~/Library/"Application Support"/minecraft/saves ~/Dropbox/Minecraft;ln -s $HOME/Dropbox/Minecraft $HOME/Library/"Application Support"/minecraft/saves

1. Close the terminal.

##### 
This uses symbolic links so you will need to get under the hood a little bit.

1. Open File Explorer, and navigate to%AppData%\.minecraft
2. Open a second File Explorer window with theMy Dropboxfolder open
3. Move thesavesfolder in the .minecraft window to the My Dropbox window
4. Rename thesavesfolder toMinecraft
5. Close both Fie Explorer windows
6. Go to Start → Run and type CMD and hit enter. (You may need to run the command prompt as an administrator.)
7. Type the following: (Be sure to double-check the path to your Dropbox folder.)

mklink /d %AppData%\.minecraft\saves %HomePath%\Documents\Dropbox\Minecraft

1. Close the Command Prompt window.

##### Windows 2000 and XP

  


The contents of this section are not supported by Mojang Studios or the Minecraft Wiki.


This uses symbolic links so you will need to get under the hood a little bit.

1. DownloadJunctionfrom Microsoft's site and install it.
2. Open a new File Explorer window
3. Go to %AppData%\.minecraft
4. Open a second File Explorer window with theDropboxfolder open
5. Move thesavesFolder in the .minecraft window to the Dropbox window
6. Rename thesavesFolder toMinecraft
7. Close both windows
8. Open the Start Menu, typecmdand hit enter.
9. Type the following:

junction -d %AppData%\.minecraft\saves "%HomePath%\My Documents\Dropbox\Minecraft"

1. Close the Command Prompt window.

#### Manual Syncing
If you want to simply manually back them up for later use, you can either copy out the whole saves folder or just the world folder that you want to backup.  If you want to move the order to the worlds in the saved menu, just change the number at the end of the world folder name to adjust the order as you would like.


