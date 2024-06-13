# Tutorials/Run Minecraft through Google Drive
This tutorial explains how to run Minecraft through Google Drive. It is useful if you want to keep your game data (worlds, resource packs, mods...) when switching computers and to automatically backup the game. (Last test: version 1.14.1)

## Contents
- 1 What you will need
- 2 Procedure
	- 2.1 Preparations
		- 2.1.1 Download Drive
		- 2.1.2 Create folders
		- 2.1.3 The client
		- 2.1.4 The data files
	- 2.2 Setting up
- 3 All done
- 4 Sources

## What you will need
- A Google Account (preferably with all 15GB of storage)
- A computer that runs Windows
- A Minecraft Account
- The Minecraft Client (minecraft.exe)
- A .minecraft folder (run Minecraft at least once to make one)

## Procedure
### Preparations
#### Download Drive
To start, we will need Google Drive installed on your PC.

- First, go tohttps://www.google.com/drive/downloadto download Google Drive.
- Click the blue "Download" button.
- Click "Agree and Download."
- Run the .exe file.
- Login to the Google Drive program we just installed with the account you want to use to store Minecraft.

A folder will be created under Favorites that will mirror all files place in drive.google.com

#### Create folders
- Locate your new Google Drive folder and open it.
- Right-click > New > Folder
- Name itMinecraft Portable(or whatever you want) and double-click it.
- Create two new folders inside ofMinecraft Portablenamedbinanddata.
	- These two folders must have those EXACT names, as we will be using them in a code.

There are now three new folders on your Google Drive: bin and data, both located in Minecraft Portable.

#### The client
Now to copy the launcher to Google Drive.

- Locate your Minecraft client and copy it. (It should be in your Downloads folder as minecraft.exe. If it's not, download it herehttps://www.minecraft.net/en-us/download/alternative.)
	- You need the .exe file, NOT the shortcut. If you're not sure, the shortcut's icon has a blue arrow on it.
	- If you can't find minecraft.exe, just download it again from minecraft.net. and copy it.
- Paste minecraft.exe into thebinfolder that you have created on Google Drive.

#### The data files
Our new Minecraft still has no data; here's how to find it:

- PressWindows+R.
	- type %APPDATA%.
	- hit ENTER.
- Locate your.minecraftfolder and copy it.
- Navigate back toMinecraft Portableand double-clickdata.
- Paste your.minecraftfolder intodata.(If you don't want to copy all your data just make an empty folder and call it.minecraft)
	- If you have many saves, large saves, or a lousy Internet connection, this could take awhile.
	- Don't get too excited once it pastes. Now Google Drive will start to sync all the files. This can take up to 5 hours in addition to the hour it will take to paste the files. Let it do it's thing overnight. It's much less stressful.

All saves, resource packs, and mods you might have are now in your Google Drive.

### Setting up
Now that all the data files are there, we need to tell Windows how to handle them Google Drive and for that, we will create a batch file.

- PressWindows+R
	- type Notepad
	- hit ENTER
- Copy and paste this code into Notepad or a similar text editor. (Note: If your .exe is located in the bin folder, replace drive with bin):

"%CD%\bin\MinecraftLauncher.exe" --workDir "%CD%\data\.minecraft"

- For whatever reason, if you use minecraft.jar, type this:

"%CD%\bin\Minecraft.jar" --workDir "%CD%\data\.minecraft"

- Now click File > Save As ...
- Locate yourMinecraft portablefolder (not bin or data) and double-click it.
- Name this file "Launcher.bat"
	- Note: Make sure to include the "" - or else Notepad will correct it to Launcher.bat.txt and it will not work.

## All done
That's it, all should work perfectly. A simple double click on the newly created Launcher.bat will start the launcher and you can play as usual. Minecraft may take a little longer to launch, but that's expected, it's just the batch file working. 

A few things to note:

- Should you ever want to download a resource pack, map, or mod, place the files into the respective folders in the.minecraftfolder on your Google Drive. However, said packs, maps, or mods will then of course be integrated in your cloud version.
- To connect to your synced Minecraft on another computer, download Google Drive, log in and double-clickLauncher.batinsideMinecraft Portable
- Minecraft Portable can run alongside regular Minecraft. To run regular Minecraft, just run it the way you normally would. Your saves will not be synced.
- Using the above settings, you will not be able to change the allocated RAM (add more memory) to your synced Minecraft. This should be one of the first things to troubleshoot if your Minecraft does not work.

