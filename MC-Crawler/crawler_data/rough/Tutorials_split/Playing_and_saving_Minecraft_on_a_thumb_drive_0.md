# Tutorials/Playing and saving Minecraft on a thumb drive
Before beginning this tutorial, note that the following guides are only for the 2.x launcher. If you want to make Minecraft portable for an older launcher version, please view this page instead. 

This tutorial explains how to run Minecraft on a portable location (e.g. on a thumb drive). Portable installation is, an installation that is not "integrated" with the computer, which is useful for managing multiple installations and generally keeping things organised. This is useful if you want to retain your game data (launcher profiles, worlds, resource packs, etc.) when switching computers. 

If you are not planning to play Minecraft on a thumb drive but on your main hard drive instead, it's highly recommended for you to make the game portable with this guide because this will give you some big advantages over standard installation. If you store different Minecraft versions (1.8, 1.12, modded 1.12, modded 1.7.10, latest, etc.) in one folder/launcher instance, mods/worlds/settings from other versions may conflict with version you are currently playing. If you want to separate them on standard installation, you will have to also keep each folder of each version in .minecraft directory and rename them every time you want to change version you are currently playing. On portable installation only a folder and launcher script file is needed to be created and after following this guide you can just play selected version just by double-clicking on its script file. 

Note: After this guide the game will be only 99% portable: the game data will be stored and used by game and its launcher where you want but launcher will create .minecraft directory anyway and will be placing there (just only) its log files (like update logs, logs with game messages and crashes, etc.) If you really care about it, you can combine this guide with the guide for the old launcher: the game will create .minecraft directory if it doesn't exist anyway but will just leave it empty[unverified]. 

## 
Note: The following Windows tutorial will guide you through installing the game to D:\Games\PortableMinecraft\. However, this guide can be used to install the game to any directory. When following this guide, replace this directory with the directory you actually want to install the game to. Please also note that while this guide was written for Windows, it is still largely applicable to other operating systems with minor changes.

Navigate to the portable drive in the file explorer, and create the D:\Games\PortableMinecraft\ directory. Next, create Launcher folder for launcher with its data and MyMinecraft folder (or another name of your choosing) for game data.

If you have existing game data, you can move it to the desired directory. Navigate to the .minecraft folder and copy all of its contents (but not the folder itself) into D:\Games\PortableMinecraft\MyMinecraft.

Now you need to move the launcher. Download Minecraft.exe (if you don't have it) and move it to D:\Games\PortableMinecraft\Launcher.

Create an empty text file called MyMinecraft.bat (or another name of your choosing) in the D:\Games\PortableMinecraft\ directory.


Open the batch file with notepad or another text editor and paste the following text into it before saving the file:
@echo off
start "" "%cd%\Launcher\Minecraft.exe" --workDir "%cd%\MyMinecraft"

Everything is now finished. When you want to play, just use the batch file to launch the game. Do not start the launcher directly (without using the batch file), or the game will just use the default directory in %APPDATA% as its working directory. It is recommended to set the launcher's executable to have the "hidden" attribute to avoid accidentally running it. You could also make a shortcut on the Desktop to run the bat file without having to find it.

## 
Note: The following tutorial assumes that the USB disk is located (and mounted) at /media/user/USBDisk, and that you would like to have portable Minecraft at /media/user/USBDisk/minecraft-portable. However, this guide can be used to install the game to any directory. When following this guide, replace this directory with the directory you actually want to install the game to.

Important preparation: You need to make sure that you have correct java version installed because linux launcher doesn't have its own java. If you want to play Minecraft versions less than 1.13, you should have Java 8 installed and selected as default in your system because Minecraft versions earlier than 1.13 don't support Java 11, they will just simply crash at launch.

Depending on the GNU/Linux disro commands may vary.

Firstly, check which version of java is currently used in your system:

java -version

If your java(or openjdk, doesn't matter) version in the first output line doesn't look like "1.8.0_xxx" (but instead looks like "1.7.0_xxx", "9", "11.x.x", "14", etc.), it means that Java 8 isn't installed or selected as default on your system.

Secondly, install Java 8 package on your system (depending on the distro the package name can be openjdk-8-jdk, jdk8-openjdk, java8-openjdk, java-1_8_0-openjdk, etc.) via terminal or graphical package manager. If your distro repositories don't have Java 8 package, maybe this can help.

Finally, run the following command and select the path containing previously installed Java 8 package name:

sudo update-alternatives --config java

Now, you are ready to install the game.


Start by creating directory for the game:

cd /media/user/USBDisk

mkdir minecraft-portable && cd minecraft-portable

Next, create myminecraft folder (or another name of your choosing) for your Minecraft game data:

mkdir myminecraft

Now, at this point, if you would like to copy all your existing game data, run the following command:

cp -r ~/.minecraft ./myminecraft

You now need to download the Minecraft Launcher. Do so by running the following command:

wget -O launcher.tar.gz https://piston-data.mojang.com/download/Minecraft.tar.gz

Next, extract the minecraft-launcher folder by using your favourite extraction utility. This tutorial assumes the extracted folder is located in /media/user/USBDisk/minecraft-portable.

All the basic setup is completed. You will find the launcher at /media/user/USBDisk/minecraft-portable/minecraft-launcher/minecraft-launcher

To open the launcher correctly, you can run the following command:

/media/user/USBDisk/minecraft-portable/minecraft-launcher/minecraft-launcher -w /media/user/USBDisk/minecraft-portable/myminecraft

But the better way is to use a shell script and run it when you want to play Minecraft. Create empty file called myminecraft.sh (or another name of your choosing) with the following text:

#!/bin/bash

"$(dirname "$(readlink -f "$0")")"/minecraft-launcher/minecraft-launcher -w "$(dirname "$(readlink -f "$0")")"/myminecraft
