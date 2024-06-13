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

