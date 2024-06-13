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

