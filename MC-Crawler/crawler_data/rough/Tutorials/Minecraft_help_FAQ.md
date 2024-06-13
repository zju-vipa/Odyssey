# Tutorials/Minecraft help FAQ
Before anyone can help players in the Minecraft Discord channel or Minecraft Forums, please make sure that the following has been performed so that we can eliminate these as possibilities.  The player would be surprised how many problems these simple suggestions fix.

Note that no community channel is able to help players with account issues. For those, see the help website.

## Contents
- 1 Common fixes
	- 1.1 Reinstalling Minecraft
		- 1.1.1 Windows
		- 1.1.2 GNU/Linux
		- 1.1.3 MacOS
	- 1.2 Latest Version
	- 1.3 Reinstalling/Updating Java
	- 1.4 Updating video drivers ("Bad video card drivers!"... et alia)
		- 1.4.1 Update instructions
- 2 Common Questions
	- 2.1 How to Back Up Minecraft Worlds
	- 2.2 Setting up a Server
	- 2.3 Installing Client on Ubuntu GNU/Linux
	- 2.4 Playing through a proxy on GNU/Linux
	- 2.5 Syncing worlds across multiple computers
		- 2.5.1 Using a USB stick
		- 2.5.2 Automatic syning using Google Drive
		- 2.5.3 Automatic syncing via Dropbox
			- 2.5.3.1 GNU/Linux
			- 2.5.3.2 macOS
			- 2.5.3.3 Windows Vista, 7 and 8
			- 2.5.3.4 Windows 2000 and XP
		- 2.5.4 Manual Syncing
- 3 References

## Common fixes
### Reinstalling Minecraft
One of the common ways to fix an ailing Minecraft installation of various bugs is to simply re-install it.  Removing the launcher itself (the file you downloaded) however will not remove Minecraft.  The steps below should work for most people.
Important step: Be sure to do a forced update if you still have issues.

#### Windows
1. Navigate to your Application Data Folder: %AppData%
2. Double Click the.minecraftfolder
3. Copy out thesavesfolder to a different location
4. Go back one directory (to where you can see .minecraft)
5. Delete the.minecraftfolder (this may take a while)
6. Start the Minecraft.exe file to re-download Minecraft
7. Close Minecraft when you reach the title screen
8. Copy thesavesfolder back into the new.minecraftfolder.  You can safely overwrite any data that's currently in this folder

#### 
1. Open a terminal
2. Copy and Paste the following, one at a time, into the terminal to delete the current minecraft installation and retain the current saved worlds.
3. (Do not remove files to the /tmp directory, things can get randomly cleared. It is generally bad practice to do so)

$ mv -v ~/.minecraft/saves ~/saves.old/

Be careful, do not continue if your terminal gives you an error. The next command deletes your minecraft folder so if the prior command did not work all your hard work would be lost! Do NOT Run this under sudo or the root user

$ rm -rf ~/.minecraft/*
$ mv ~/saves.old/saves ~/.minecraft/saves
$ rm -rf ~/saves.old

1. Start Minecraft like you normally would. Your saves should be intact and the Minecraft client will re-download itself for you.

Alternatively, open up your Home folder and press Ctrl+H. This shows all hidden files and folders. Navigate down to .minecraft. From here, you can work in essentially the same way as outlined in the instructions for Windows above.

#### MacOS
1. Open a Finder window
2. Click theGoMenu item and ClickGo to Folder
3. Type~/Library/Application Support/minecraftinto the text field and clickGo
4. Drag thesavesfolder to your desktop
5. Drag everything else in the minecraft folder to the trash
6. Drag thesavesfolder back into theminecraftfolder
7. Close the Finder window and launch the Minecraft App just like you would normally.

### Latest Version
If you are having issues after a reinstall, or are having other client issues, you can try using forced update.

1. Open the Minecraft launcher
2. Click on the arrow (directly beside the version)
3. Click on "Latest Version!"
4. Click on "Play"
5. Soon, the client will re-download the game files

### 
- If Minecraft is not working due to an issue with Java, your Java install may be corrupt and/or out of date. To remedy a corrupt install, begin by uninstalling Java. After the uninstall is complete, you can then try reinstalling.
- For Windows users, it is sometimes (rarely) necessary to use an uninstaller program, such asRevo Uninstaller (free)to remove Java. Revo will search in-depth for all things Java, and remove the files.
- To re-download/update Java, visit Java's download pagehere. Download the correct version (of Java 8) for your machine, based on what operating system you have.
- Make sure you be careful with all instructions! (Anyone can edit this page)

### 
- If Minecraft has poor performance, has graphics that are distorted, or is simply not working, it's possible that you need a driver or an updated driver installed.
- Some graphics cards only accept drivers from the manufacturer of the computer (i.e. Dell, HP, Toshiba). Visit the support site of the company that affects you, if that ends up being the case for you.
- Windows Update isnota good method for updating video drivers. If a generic driver is installed, you should remove it before installing a new driver. Create a system restore point, orperform a driver rollbackif you experience issues after installing a new driver.
- If further help is needed,this videomay help you to fix this error.

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

