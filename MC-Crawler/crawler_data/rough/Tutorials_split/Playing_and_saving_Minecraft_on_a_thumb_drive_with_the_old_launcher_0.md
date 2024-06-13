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

