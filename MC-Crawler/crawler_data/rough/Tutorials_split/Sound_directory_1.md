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

