# Tutorials/Custom maps
Custom maps are maps created by other players who can then upload the files online to share. You can then download these maps and play them. Note that this is not a list of maps; this just has suggestions of how to play and use maps. You can find a list of maps on other websites.

## Contents
- 1 Importing maps
- 2 Map types
	- 2.1 Puzzle
	- 2.2 Action
	- 2.3 PVP
	- 2.4 Parkour
	- 2.5 Creative
	- 2.6 Adventure
	- 2.7 Horror
- 3 Sharing maps
- 4 Compressing maps
	- 4.1 Removing player data
	- 4.2 Removing automatically generated files
	- 4.3 Minifying JSON files
	- 4.4 Compressing resources
	- 4.5 Removing region files
- 5 See also
- 6 References

## Importing maps
Before you can import a map, you will need to download one. There are many websites online for this purpose.

** Java Edition **
Once you have downloaded the map, it should be in .zip format. Extract and copy the compressed folder. Next, start the Minecraft Launcher and click Launch Options on the top right corner. Select your profile and click Open Game Dir. The .minecraft folder should appear. Finally, paste the copied map folder into the saves folder and start Minecraft. The world should have appeared in your worlds list.

Java Edition, Simpler Map Transfer

After the map is downloaded, take the .zip file, and copy it. Now, go to the "Type here to search" area on the taskbar. Type Run, and write %appdata%. After You Find The .minecraft  folder, go to the "saves" folder, and paste the world

** Bedrock Edition **
Once you have downloaded the map, it should be in a .mcworld or folder format. 

To import the .mcworld format on Windows 10, you should be able to double click the file to open it in Minecraft, the world will be automatically imported.

To import the .mcworld format on a mobile device, you should be able to click a share/open in button or double tap it to open the file in Minecraft, the world will be automatically imported.

To import the map as folder format for all OS, you will have to drag the world folder manually to Minecraft/games/com.mojang/minecraftWorlds/ folder.

## Map types
Playing the maps is the most fun part. Custom maps often have objectives and sometimes a storyline. They can be great fun and there are many types. Here are a few of the types, as well as some tips to completing them.

### Puzzle
A fork shown in a Minecraft maze made of sandstone.
These are obstacle courses involving puzzles to complete. They might have a scoring system, such as chests hidden with gold. The more you collect, the higher your score. Here are some obstacles you may see:

- RedstonePuzzles. These will give you some redstone components, such as arepeateror two and someredstone dust, and ask you to rewire a door or something to open. Check the relative redstone sections on them in this wiki to find some tips on how to make the most of what you have.
- Mazes. Wander around narrow paths aimlessly until you see a door. Mazes can be very fun to play. At each fork, it may help to mark chosen paths with a torch to track where you have been.

### Action
Generally, these maps involve fighting and survival skills.

- Survival Maps. Like regular Minecraftsurvival, but with a twist. You may be in theclouds, have limited resources/space, etc.
- CTM maps. Short for "Complete the Monument", these maps are known to be very difficult. The goal is to complete a "Victory Monument", where you have to fill it up withwool, records, or some other type of items. These maps have many traps along the way.
- Arena Maps. These maps have stages and in each stage, you must fight a wave ofmobsin order to progress.

### PVP
These maps are for Player vs. Player. They are great if you get tired of fighting the same in-game mobs, since the AI can be very predictable.

- Race For Wool maps. This is when teams of four go into a lane and try to complete a monument there. They include dungeons and crossfire from the other lanes. This is a type of CTM.
- Capture The Wool maps. This is where people rush to the opponent's base and attempt to steal wool from a fleecy box (wool chest). They then have to return to their base. Can be played in small or large groups.
- Destroy the Monument/Core maps. Self-explanatory. Usually only played in large groups, sometimes up to 50v50.

### Parkour
A short parkour course, with Blocks over a pit of lava with a chest at the end. The player is expected to jump across the blocks and get to the chest for a reward.
Parkour means to jump over blocks. They are usually organized in stages. There are several kinds of jumps, ranging from corner jumps, S-jumps, and ladder jumps. These maps are a test of agility and timing.

### Creative
These are maps with no real goal in mind. They often have stunning scenery or mechanics. The website Planet Minecraft is filled with these. They can sometimes have a purpose, like as a map for a server.

### Adventure
Complete a long and winding storyline. Often has lots of content. Sometimes puzzle, sometimes action, sometimes parkour. You cannot break any blocks in these maps, unless specifically told or allowed otherwise.

### Horror
Generally an Adventure map with jumpscares and a dark/ambiguous storyline. Ghosts, past memories, death, and locked-in are common themes.

## Sharing maps
** Java Edition **
For importing a map, you will first need to open the minecraft saves folder. This can be found by opening the launcher, clicking Launch Options, and clicking Open Game Dir. Once you are in the .minecraft folder, navigate to the saves folder and find the world you want to share. To make it easier to send to others, you will probably want to compress the folder into a zip file.

Optionally, you can also go to a site such as MediaFire or CurseForge and find their uploads screen. Paste the file in and follow the instructions. The Internet can now see your creation!

** Bedrock Edition **
Exporting a map is easiest on Windows 10. In Windows 10, open Minecraft and click edit on the world you wish to share. Scroll to the bottom and click the "Export World" button and choose a location to save the .mcworld file to.

On mobile, you will first need to locate the Minecraft folder. In iOS, you can access this in the “Files” app in the "On My iPhone” or “On My iPad” or “On My iPod” category. Once in the Minecraft folder, you will need to go to "Minecraft/games/com.mojang/minecraftWorlds/" In this folder, you can find all of your Minecraft worlds in folders with randomized names. It may be helpful to sort the folders by date modified.

Once you have found the desired world, you can verify its name by opening the "levelname" file contained inside. If you compress the contents of the folder (not the folder itself) and rename it to have a .mcworld extension rather than .zip, it should be easy to share and open in Minecraft.

Please note that you can also not compress the map and change the extension to .mcworld and just share the world as a folder. But to import the map as folder format you will have to drag the world folder manually to Minecraft/games/com.mojang/minecraftWorlds/ folder.

## Compressing maps
Large maps files can get very big, however there are ways to combat this by reducing the total file size. Keep in mind that every map will have a file size, larger maps much more so. It is impossible to get a map below 1kb, but some can be as little as 200kb. Note that this information is written for Java Edition and may not be the same for Bedrock Edition.

### Removing player data
A lot of maps don't require prior knowledge of the player playing it before it is loaded for the first time, and most of the time the final release has no reason to keep old player data generated by the developer(s). If your map doesn't require any playerdata, such as someone's advancements, position, inventory, or otherwise player-specific data, you can remove the "advancements", "playerdata", and "stats" folders found in the root of the map folder. If your map has custom advancements, do not delete those. Only delete the advancements folder inside the root of the map. (.minecraft/saves/Map_Name/advancements, not .minecraft/saves/Map_Name/datapacks/Maps_Datapack/data/namespace/advancements)

### Removing automatically generated files
Both session.lock and level.dat_old are files that are not needed to be packed along with the map file. You can safely delete both these files, since they will be regenerated once the map is loaded. You can also remove the "poi" folder, but this will incur a slightly longer loading time. The "poi" folder will be regenerated on map load.

### Minifying JSON files
JSON is meant to be read both with and without newlines. We can remove all newlines that are part of the JSON file (be sure not to remove any "\n" inside strings!) to reduce its file size. You can also remove spaces between JSON values. Minifying JSON files doesn't save that much space since they are made of text. However, over a large number of files, the space saved could add up.


For example, the JSON:
[
  "",
  {
    "text": "To do list: ",
    "color": "blue",
    "underlined": true
  }
]

can be shorted to:
[{"text":"To do list:","color": "blue","underlined":true}]

Here, we remove the spaces and newlines between the "text", "color", and "underlined" values. Note that spaces inside the "text" string were not removed. The useless "", at the start was also removed as it serves no purpose. Some generators erroneously add that. The trailing space at the end was removed; however this might not always be wanted. Be careful when editing "text" strings. If your resource pack has a custom language file, you can compress that as well.

### Compressing resources
If you are using a resource pack, the textures and sounds can add a hefty amount to the package size. Compressing them or making sure they do not have unnecessary high resolution can help lighten the load.

** Compressing textures **
A lot of textures can become very large without the benefit of improved quality. Some textures could be as large at 2048×2048 (almost 4K UHD) even if the player will never notice much difference. At most, textures should be 256×256 and they should not need to exceed this. Usually, textures can safely be in resolutions of 16×16, 32×32, or 64×64. Either way, try not to exceed 256×256, as this level of details is not easily be seen by the player. After finding an acceptable resolution, try using image compressors. These can sometimes reduce your file size by up to 90%, but may come at the cost of a loss of color depth (24-bit colors to 16-bit). This reduces the file size because there are not as many colors to store, but vibrant textures may become more "grainy", or "static-ey". If you still think there is data that can be shaved off, try removing all EXIF data from the image. Note that this will remove any copyright notes the image has (if any are present), and you may have to manually add credit (you should always give credit manually, but this is a legal matter).

** Compressing .ogg sounds **
Ogg Vorbis is meant to reduce filesize,[1] but sometimes just the format isn't enough. You can also reduce the bitrate of the audio or reduce amplitude and manually increase it with /playsound. You can also try mixing the track down to mono, meaning the audio will have 1 track, instead of 2. This can result in quality reduction if not done carefully. It is recommended to mix small sounds down to mono, as players won't have enough time to distinguish the stereo version from its mono counterpart.

### Removing region files
This is not recommended for most users as it can delete parts of your map. Be sure to make a backup before attempting this; you never know if something might go wrong.

Before you start, it is recommended to read up on chunks and region files. As a summary, chunks are 16×16 regions of a world, and region files are a 32×32 chunks. There are 1024 chunks, or 262144 blocks, in a region file.

Use Dinnerbone's Chunk Coordinate Finder and input coordinates of a block in every chunk in intervals of 16. For example, find the chunk file at chunk number 0, 0 and then at chunk number 0, 32. Make sure to find the blocks in positive and negative chunks, too. Once you have a full list of chunks that you want to keep, make a backup of your current world.  Once you've made your backup, delete any chunk files that are not in your list. For example, if your list contains the regions:

- 0, 0,
- 0, 1,
- 0, -1,
- 3, 4,

you would not delete r.0.0.mca, r.0.1.mca, r.0.-1.mca, and r.3.4.mca. Delete all other files that do not match. This will remove any regions that are unused which can greatly reduce the map's total file size.

