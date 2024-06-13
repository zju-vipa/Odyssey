# Tutorials/Sound directory
This tutorial will help you locate and extract the sound directory, where the sounds and music for Java Edition are stored.

## Contents
- 1 Sound directory (after 1.7.2)
	- 1.1 Locating specific sound files
- 2 Extracting Minecraft sounds using Node.js
- 3 Extracting Minecraft sounds though changing file type
- 4 Extracting Minecraft sounds using Python
- 5 Extracting Minecraft music On Windows (via Windows Subsystem for Linux)
- 6 Extracting Minecraft music on Linux
- 7 Extracting Minecraft music On Mac
- 8 Old sound directory (pre-1.7.2)
	- 8.1 Legacy sub-folders
- 9 Warning
- 10 Video tutorials
- 11 See also

## 
The sound file for versions after 1.7.2 is located in the indexes directory:

1.8 macOS: ~/Library/Application Support/minecraft/assets/indexes/1.8.json

1.11 macOS: ~/Library/Application Support/minecraft/assets/indexes/1.11.json

The sound files in version 1.7.2 (specifically 13w42a) and above are scattered and hashed into different folders, which are located in:

- Windows:%AppData%\.minecraft\assets\objects
- macOS:~/Library/Application Support/minecraft/assets/objects
- Linux:~/.minecraft/assets/objects

### Locating specific sound files
Find the folder indexes, which is found under the same assets folder as objects, where the sound files are indexed and logged in the sounds.json file. Select the version you want and open the sounds.json file with a program that supports it, such as Notepad. Programs such as Notepad++ are recommended to help make the file more readable. Once opened, you may find something that looks like this:

"sounds/music/menu/menu1.ogg": {
    "hash": "c157c56846f0e50620f808fecd9d069423dd6c41",
    "size": 1744657
},
From this, we can determine that menu1.ogg is hashed (or labeled) as c157c56846f0e50620f808fecd9d069423dd6c41. Perform a search in the directory objects under assets and you should find a file with the same exact string; this is the file "menu1.ogg", one of the pieces of music that plays on the menu screen. The first two letters of the file name ("c1") will match the folder that the file is in as well; knowing this can help locate specific files faster.

After locating the file, you can test it to make sure it is the right one by playing it with a media player that is able to play .ogg sound files. If the media player you have cannot play the file, try renaming it with ".ogg" at the end. If this fails too, then it either means the media player you use does not have a proper .ogg extension to play the sound, or the file you found is not a sound file.

Note: If you accidentally edit or remove the file from the original directory, the launcher will automatically re-download it again the next time you launch the game. (You must be connected to the Internet when you launch the game. If not, then the sound directory will not be reset and could potentially lead to errors.)

## Extracting Minecraft sounds using Node.js
This is probably the simplest way to extract the sound files with original effections.

** Script 1 **
const fs = require('fs-extra')

const objects = require('./indexes/1.19.json').objects

for (let filePath in objects) {

	if (!/\/(?:sounds)\//.test(filePath)) continue
	if (!/\/(?:ambient|block|damage|dig|enchant|entity|event|fire|fireworks|item|liquid|minecart|mob|music|note|portal|random|records|step|title|ui)\//.test(filePath)) continue
	  
	let copyPath = filePath.replace('minecraft/', './')
	let hash = objects[filePath].hash
	let objectPath = './objects/' + hash.substring(0, 2) + '/' + hash
	console.log(objectPath, '->', copyPath)
	fs.copySync(objectPath, copyPath)
}

** Script 2 to run Script 1 **
@echo off
npm install fs-extra -y
node extract-music.js
pause

1. First of all, installNode.jsonto your computer.
2. Create a new text file inside.minecraft/assetscalledextract-music.jsand paste the first script into it.
3. Create another new text file inside.minecraft/assetscalledExtract.batand paste the second script into it.
4. Rename both text files by removing ".txt" from both of them.
5. Now you can run it by double clicking theExtract.batfile. It will create a newsoundsfolder with all the sounds in it.

- By default it will extract 1.19 files. To change the version, go into theextract-music.jsfile and on the 3rd line, change1.19.jsonto any version you want (you need to have actually played the version at least once).
- If the folder does not appear after runningExtract.bat, open the file again and remove line 2 entirely and runExtract.batagain.

** Note **
Make sure the file extensions are .js and .bat and not .txt when you rename it! In other words, remove your old file extension. You may be warned that changing a file name extension could make the file unusable. However, this actually indicates that you have renamed it correctly. It will work if you keep it .txt as example, but it's probably nicer to have it for what it is for.

If you are using Microsoft Windows and can't see file extensions, for Windows 10, you can turn them on by going to the View menu of the file explorer and checking the check box for file name extensions. For Windows beneath Windows 10, you can uncheck "hide extensions."




## Extracting Minecraft sounds though changing file type
This method may be by far the most simple and requires no third-party application, but may require admin permission on your computer to pull off. The instructions listed below apply for Windows systems only.

1. Open File Explorer on your system and select the view tab.
2. Locate the "File name extension" and check the box; this will make it so the file type can now be seen and even edited.
3. Go to the audio file you extracted and open the context menu by right clicking the file.
4. Select "Rename".
5. Add ".ogg" to the very end of the file name (no spaces) and save; this cause the file to become a .ogg format file.

- Important Note:putting MP4 or other media file types in place of ogg are not guaranteed to work and should only be done if you know what you are doing; failure to do so may result in the file becoming corrupted.

## Extracting Minecraft sounds using Python
import json, os, platform, shutil, sys

''' 
    Copies audio files from indescript hashed folders to named sorted folders.
    You may need to change output path.
'''

# This section should work on any system as well
print("Your OS is " + platform.system())
if platform.system() == "Windows":
    MC_ASSETS = os.path.expandvars(r"%APPDATA%/.minecraft/assets")
else:
    MC_ASSETS = os.path.expanduser(r"~/.minecraft/assets")

# Find the latest installed version of minecraft (choose the last element in assets/indexes)
MC_VERSION = os.listdir(MC_ASSETS+"/indexes/")[-1]
print("Your latest installed version of minecraft is " + MC_VERSION[:-5] + "\n")

# Change this if you want to put the sound files somewhere else
OUTPUT_PATH = os.path.normpath(os.path.expandvars(os.path.expanduser(f"~/Desktop/MC_Sounds/")))

# These are unlikely to change
MC_OBJECT_INDEX = f"{MC_ASSETS}/indexes/{MC_VERSION}"
MC_OBJECTS_PATH = f"{MC_ASSETS}/objects"
MC_SOUNDS = r"minecraft/sounds/"


with open(MC_OBJECT_INDEX, "r") as read_file:
    # Parse the JSON file into a dictionary
    data = json.load(read_file)

    # Find each line with MC_SOUNDS prefix, remove the prefix and keep the rest of the path and the hash
    sounds = {k[len(MC_SOUNDS):] : v["hash"] for (k, v) in data["objects"].items() if k.startswith(MC_SOUNDS)}

    print("File extraction :")

    for fpath, fhash in sounds.items():
        # Ensure the paths are good to go for Windows with properly escaped backslashes in the string
        src_fpath = os.path.normpath(f"{MC_OBJECTS_PATH}/{fhash[:2]}/{fhash}")
        dest_fpath = os.path.normpath(f"{OUTPUT_PATH}/sounds/{fpath}")

        # Print current extracted file
        print(fpath)

        # Make any directories needed to put the output file into as Python expects
        os.makedirs(os.path.dirname(dest_fpath), exist_ok=True)

        # Copy the file
        shutil.copyfile(src_fpath, dest_fpath)

## 
1. Create a new file (for example from the terminal): vi minecraft-music-extractor.sh
2. Paste the following into the file: (when you run the file, it'll ask you what your Windows username is and Minecraft version, the rest is automatic, and outputs to the desktop)
3. Update the variables (e.g. MINECRAFT_ASSETS_DIR) with your correct directory paths
4. If you want all sounds, replace "grep music" with "grep sounds", if you want the records, replace "grep music" with "grep records", these are shown commented out above the line of code.
5. Run the script from terminal with "bash minecraft-music-extractor.sh".

#!/bin/bash
#
# Description: Minecraft Music Extractor

echo -e "Enter your Windows username:"
read winusername
echo

USER_DIR="/mnt/c/Users/$winusername"

# Windows Profile doesn't exist = Can't run
if [ ! $(ls /mnt/c/Users/ | grep $winusername) ]; then
	echo -e "Unable to run, you entered an invalid user."
	echo -e "Make sure you entered everything correctly, spelled right with caps and lower case.\n"
	read -p "Press [Enter] key to continue..." && exit
fi

MINECRAFT_ASSETS_DIR="$USER_DIR/AppData/Roaming/.minecraft/assets"
OUTPUT_DIR="$USER_DIR/Desktop"

echo -e "Enter the Minecraft version you want to extract from:"
read version
echo

JSON_FILE=$(echo $MINECRAFT_ASSETS_DIR/indexes/$version.json | grep "/")

# Version doesn't exist = Can't run
if [ ! -f $JSON_FILE ]; then
	echo -e "Unable to extract because that version isn't downloaded or doesn't exist."
	echo -e "Make sure to open the launcher and download the version you need to create a pack for.\n"
	read -p "Press [Enter] key to continue..." && exit
fi

# for ENTRY in `cat "$JSON_FILE" | python -c 'import sys,json; from pprint import pprint; data = json.load(sys.stdin); pprint(data);' | grep music | awk -F\' '{print $2 "," $6}'`
# cat "$JSON_FILE" | python -c 'import sys,json; from pprint import pprint; data = json.load(sys.stdin); pprint(data);'
# cat "$JSON_FILE" | python -c 'import sys,json; from pprint import pprint; data = json.load(sys.stdin); pprint(data);' | grep sounds
# cat "$JSON_FILE" | python -c 'import sys,json; from pprint import pprint; data = json.load(sys.stdin); pprint(data);' | grep records

for ENTRY in `cat "$JSON_FILE" | python -c 'import sys,json; from pprint import pprint; data = json.load(sys.stdin); pprint(data);' | grep music | awk -F\' '{print $2 "," $6}'`
do
	echo "Processing $ENTRY..."
	echo $ENTRY | cut -d, -f1
	FILENAME=`echo $ENTRY | cut -d, -f1`
	FILEHASH=`echo $ENTRY | cut -d, -f2`

	#Locate the file in the assets directory structure
	FULLPATH_HASHFILE=`find "$MINECRAFT_ASSETS_DIR" -name $FILEHASH`

	#Copy the file

	mkdir -p  $OUTPUT_DIR/`echo $FILENAME | sed -E 's/\/[a-z0-9_]+\..+//'`
	cp "$FULLPATH_HASHFILE" "$OUTPUT_DIR/$FILENAME"

done

Alternatively, update USER_DIR to be "C:/Users/$winusername", then install Git for Windows, and open minecraft-music-extractor.sh directly. This, like the Python script, doesn't require WSL.

## Extracting Minecraft music on Linux
1. Create a new file (for example from the terminal): vi minecraft-music-extractor.sh
2. Paste the following into the file: (when you run the file, it'll ask you what Minecraft version, the rest is automatic, and outputs to the desktop)

#!/bin/bash
#
# Description: Minecraft Music Extractor

USER_DIR=$(echo ~ | grep "/")
MINECRAFT_ASSETS_DIR="$USER_DIR/.minecraft/assets"
OUTPUT_DIR="$USER_DIR/Desktop"

echo -e "Enter the Minecraft version you want to extract from:"
read version
echo

JSON_FILE="$MINECRAFT_ASSETS_DIR/indexes/$version.json"

# Version doesn't exist = Can't run
if [ ! -f $JSON_FILE ]; then
	echo -e "Unable to extract because that version isn't downloaded or doesn't exist without orgins."
	echo -e "Make sure to open the launcher and download the version you need to create a pack for.\n"
	read -p "Press [Enter] key to continue..." && exit
fi

#for ENTRY in `cat "$JSON_FILE" | python -c 'import sys,json; from pprint import pprint; data = json.load(sys.stdin); pprint(data);' | grep music | awk -F\' '{print $2 "," $6}'`
#cat "$JSON_FILE" | python -c 'import sys,json; from pprint import pprint; data = json.load(sys.stdin); pprint(data);'
#cat "$JSON_FILE" | python -c 'import sys,json; from pprint import pprint; data = json.load(sys.stdin); pprint(data);' | grep music


for ENTRY in `cat "$JSON_FILE" | python -c 'import sys,json; from pprint import pprint; data = json.load(sys.stdin); pprint(data);' | grep sounds | awk -F\' '{print $2 "," $6}'`
do
	echo "Processing $ENTRY..."
	echo $ENTRY | cut -d, -f1
	FILENAME=`echo $ENTRY | cut -d, -f1`
	FILEHASH=`echo $ENTRY | cut -d, -f2`

	#Locate the file in the assets directory structure
	FULLPATH_HASHFILE=`find "$MINECRAFT_ASSETS_DIR" -name $FILEHASH`

	#Copy the file

	mkdir -p  $OUTPUT_DIR/`echo $FILENAME | sed -E 's/\/[a-z0-9_]+\..+//'`
	cp "$FULLPATH_HASHFILE" "$OUTPUT_DIR/$FILENAME"

done

1. If you want all sounds, replace "grep music" with "grep sounds".
2. You may need to run `chmod u+x minecraft-music-extractor.sh` if the script isn't executing.
3. Run the script from terminal with "./minecraft-music-extractor.sh".

## Extracting Minecraft music On Mac
1. Create a new file (for example from the terminal), type in and hit enter: vi minecraft-music-extractor.sh
2. Paste the following into the file:

#!/bin/sh
#
# Description: Minecraft Music Extractor

MINECRAFT_ASSETS_DIR="/Users/YOURUSERNAMEHERE/Library/Application Support/minecraft/assets"
OUTPUT_DIR="/Users/YOURUSERNAMEHERE/Desktop"
JSON_FILE="/Users/YOURUSERNAMEHERE/Library/Application Support/minecraft/assets/indexes/YOURJSON.json"

#for ENTRY in `cat "$JSON_FILE" | python -c 'import sys,json; from pprint import pprint; data = json.load(sys.stdin); pprint(data);' | grep music | awk -F\' '{print $2 "," $6}'`
#cat "$JSON_FILE" | python -c 'import sys,json; from pprint import pprint; data = json.load(sys.stdin); pprint(data);'
#cat "$JSON_FILE" | python -c 'import sys,json; from pprint import pprint; data = json.load(sys.stdin); pprint(data);' | grep music


for ENTRY in `cat "$JSON_FILE" | python -c 'import sys,json; from pprint import pprint; data = json.load(sys.stdin); pprint(data);' | grep music | awk -F\' '{print $2 "," $6}'`
do
  echo "Processing $ENTRY..."
  echo $ENTRY | cut -d, -f1 
  FILENAME=`echo $ENTRY | cut -d, -f1`
  FILEHASH=`echo $ENTRY | cut -d, -f2`

  #Locate the file in the assets directory structure
  FULLPATH_HASHFILE=`find "$MINECRAFT_ASSETS_DIR" -name $FILEHASH`

  #Copy the file

  mkdir -p  $OUTPUT_DIR/`echo $FILENAME | sed -E 's/\/[a-z0-9_]+\..+//'`
  cp "$FULLPATH_HASHFILE" "$OUTPUT_DIR/$FILENAME"

done

1. Update the variables (i.e. YOURUSERNAMEHERE and YOURJSON) with your correct directory paths.
2. If you want all sounds, replace "grep music" with "grep sounds".
3. Hit esc to quit edit mode, then type ":wq" to save and quit the script.
4. Start a new line and run the script just saved by typing and hitting enter: "bash minecraft-music-extractor.sh".

## 
If you play the game before 1.7.2, the sound directory is located as follows:

- Windows:%AppData%\.minecraft\assetsor%AppData%\.minecraft\assets\virtual\legacy
- macOS:~/Library/Application Support/minecraft/assets
- Linux:~/.minecraft/assets

If you have played both the old and new versions, then both the old and new directories will exist in the game files. The old directory is only used for pre-1.7 versions.

### Legacy sub-folders
In .minecraft\assets\virtual\legacy\sounds, there are 13 sub folders:

- ambient: Ambiance and rain/thunder
- damage: Sounds of the player taking damage
- dig: Breaking blocks
- fire: Fire sounds
- firework: Fireworks sound effects
- liquids: Sounds made by liquids such as water and lava
- minecart: Sounds created by moving minecarts
- mob: Mob sounds
- music: Background music by C418
- random: Various sound effects from eating to explosions
- records: Music on the record discs found
- step: Footsteps
- tile: Pistons

## Warning
If you edit, add, or remove sounds directly in the sound directory, executing the launcher and then launching Minecraft while connected to the Internet will automatically re-download and revert any changes you've made to the sound directory, deleting your work. This applies for both the new and old sound directories. Disconnecting from the Internet before launching the game will not revert the files, but this is not recommended. The best method to safely store custom sounds is to create your own resource pack.

## Video tutorials
Minecraft Tutorial: Locate the Minecraft Sound Directory and Convert Audio Files (Old sound directory only)




