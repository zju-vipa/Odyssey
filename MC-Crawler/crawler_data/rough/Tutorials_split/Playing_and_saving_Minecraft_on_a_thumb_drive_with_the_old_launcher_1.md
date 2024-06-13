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

