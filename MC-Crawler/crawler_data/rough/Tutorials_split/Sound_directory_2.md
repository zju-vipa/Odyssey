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





