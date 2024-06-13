# Tutorials/Updating old terrain
From time to time, Minecraft world generation is changed to introduce new features. Some of these changes are terrain-breaking (like Java Edition 1.8), while others keep the terrain roughly the same in terms of altitude. In either case, you may want to clear out chunks of your old world, so that the new world-gen kicks in to give you the exciting stuff. This tutorial explains how to delete chunks in an older world for them to regenerate in a newer version, so that you won't need to travel thousands of blocks into unexplored terrain to see the new terrains if the player has a huge world. This action is commonly known as chunk resetting.

## Contents
- 1 Non-breaking update
	- 1.1 Using MCA Selector (any Java)
	- 1.2 Using MCEdit (1.7.2-1.12.2)
	- 1.3 Using the tools
		- 1.3.1 Preparation
		- 1.3.2 Protecting regions of your world
			- 1.3.2.1 Example
		- 1.3.3 Running the selection
- 2 Breaking change
	- 2.1 Splicing by Y
- 3 Gallery
- 4 References

## Non-breaking update
An example for a non-breaking update is Java Edition 1.13. This version vastly changes the world generation of oceans, swamps and rivers by adding features like shipwrecks, coral reefs, and seagrass. However, the new terrain generation doesn't affect the biome type or terrain altitude (with a few exceptions, as u/bdm68 pointed out.)[1]

In the case of 1.13, we want to remove all chunks with an ocean, river, or swamp biome so that they regerate with the new features in 1.13. Since the biome types and altitude didn't change in 1.13, the regenerated chunks will seamlessly blend into the existing landscape, but they will generate with the new underwater features.

### 
MCA selector is a tool to do chunk-level operations on a Minecraft world, and that also includes deleting and filtering. It has a filter interface for you to check for coordinate, block type, biomes, as well as for chunks of a certain data version. It works on any version of Java Edition.


You can follow these steps to reduce world file size or delete chunks without accidentally removing any important part of the world:

- Open your world in MCA Selector
- Click on "Tools" -> "Filter chunks"
- Replace the linexPos <= 100 AND xPos >= -100 AND zPos <= 100 AND zPos >= -100withInhabitedTime = "0",press Enter then click "OK"
- Now the generated chunks that no player has ever been near are selected. You can delete them by hover at "Selection" -> Delete selected chunks -> OK

### 
MCEdit has a plugin to select chunks by biome so that we can delete them. It is also possible to protect regions of your world, in case you need to preserve existing builds in those biomes.[2] As this method depends on MCEdit, it only works for worlds opened in Java Edition 1.7.2 to 1.12.2. If you have opened the world in 1.13, you need to retrieve the older save from the backups folder.

The plugin inspects each chunk of your world, and decides for each chunk whether it can be deleted. In Minecraft, a single chunk can contain different biomes. For example, along the shore of an ocean, a lot of chunks will contain ocean biomes as well as beach biomes. Sometimes it is not obvious how these cases should be handled, so the plugin can be used in one of two modes:

- Aggressivemode deletes chunks that contain any of the selected biomes. For example, if you decide to delete all river biomes in aggressive mode, the plugin will delete a chunk as soon as it contains a single block of river biome, no matter which other biomes are present in that chunk.
- Cautiousmode only deletes chunks that contain nothing but the selected biomes. For example, if you tell the plugin to delete ocean and beach biomes, then it will only delete chunks in which each block is part of an ocean biome or a beach biome. If there is a single block in that chunk that is neither in an ocean nor in a beach biome, then it won't delete that chunk.

Here is an example to illustrate the difference:


There are four biomes present here: plains (green), beaches (yellow), rivers (light blue), and oceans (dark blue). If you were to delete all rivers, beaches, and oceans with the plugin, then all purple striped chunks would be deleted no matter which mode you use. But in aggressive mode, also the red striped chunks would be deleted.

In general, aggressive mode will lead to better results, especially if you want to regenerate river biomes. However, you may need to protect more regions of your world.

To protect regions of your world, you will need to modify the plugin by writing some Python code. Guides are provided so don't be worried.

The whole process may take a couple of hours.

### Using the tools
#### Preparation
1. Make a backup of your world.
2. Test your backup to make sure that it works. Be aware that your world may be corrupted, so don't just skip steps 1 and 2.
3. Prepare your tool.
	- Download and installMCEdit. The recommended version isMCEdit 2.0.0 beta 12. The download link is for Windows and Mac.
		- Download the biome deleter pluginhereand extract it. You will find two files; a copy of this tutorial, as well as the plugin in a file called 'biome_deleter.py'.
		- Install the plugin by copying it into the plugin folder.
			- On Windows, you will find a folder next to the MCEdit 2 exe called 'MCEdit 2 Files'. The 'plugins' folder is inside that folder.
			- On macOS, the plugins folder is '~/Documents/MCEdit 2 Files/plugins'. You might need to create that folder if it doesn't exist.
	- Download and install MCA selector.
4. Decide which biomes you want to delete. The following biomes are largely affected by the new terrain generation:
	- Ocean(ID 0)
	- Swamp(ID 6)
	- River(ID 7)
	- Frozen Ocean(ID 10)
	- Mushroom Fields(ID 15)
	- Beach(ID 16)
	- Deep Ocean(ID 24)
	- Stone Shore(ID 25)
	- Snowy Beach(ID 26)

#### Protecting regions of your world
Once you decided which biomes you want to delete, make a (mental) list of things you built in those biomes, or near the edges of those biomes. Depending on the mode you use, the plugin may delete chunks even if they contain biomes that you did not want to delete.

If you haven't built anything in those biomes that you want to keep, skip to the next section. Otherwise, this section will teach you how you can modify the plugin to protect those builds.

A screenshot explaining parts of the MCEdit user interface.
1. Open your world in MCEdit. Here is a simple guide for MCEdit:
	- MCEdit has three camera modes. A sideways camera that looks likeTerraria, an overview camera that shows the world from the top, as well as a full 3-D camera. You can switch between them using the three buttons labeled2D,Over, and3D. For this tutorial, we'll be using the overview camera.
	- Press and hold the right mouse button to move around.
	- The toolbar is on the left-hand side of the window. For this tutorial, we'll only be using theSelecttool.
	- Using the chunk selector, you can select chunks by dragging a box with the left mouse button.
	- The status bar at the bottom of the window shows a lot of useful information about whatever you're pointing at with your mouse cursor. In particular, it shows the block coordinates, chunk coordinates, and the biome.You will be using the chunk coordinates to define protected regions.
2. Open the plugin ('biome_deleter.py') in a text editor (e.g. Notepad on Windows, or TextEdit on macOS). Scroll down until you found a big headline saying 'Protected Regions' (line 200).
3. For each region that you want to protect, do the following:
	1. Using the overview camera, find the region that you want to protect.
	2. Using the chunk selection tool, select the region that you want to protect.
	3. Find thechunk coordinatesof the upper left and lower right chunk of the selected region. The status bar in MCEdit shows, from left to right, the x, y, and z coordinate of the chunk. So, when you see 'chunk (1, 0, -9)', then 1 is the x coordinate, 0 is the y coordinate, and -9 is the z coordinate of that chunk.
	4. In your text editor, find the area dedicated to your protected regions, and add a new line there.
	5. Type 'chunk_region(x1, z1, x2, z2),' (note the comma at the end there), but replace x1 and z1 by the x and z coordinate of the upper left chunk, and replace x2 and z2 by the x and z coordinate of the lower right chunk.
	6. Add spaces at the beginning of that new line until the 'c' in 'chunk_region' is right underneath the '#' signs in the lines above.
4. Save the modified plugin.

The idea is similar with MCA selector, but only a top view is provided. You may want to go into the game (in a backup) so that you can use the x-z coordinates from within. Alternatively, it suffices in most cases to check for a 64×64 radius from a crafting table (Palette), the quintessential marker for player activity.

##### Example
There are two regions that you want to protect.

- The first one is your base. The box of chunks that encloses your base has chunk (-1, 0, 4) in its upper left corner, and chunk (3, 0, 12) in its lower right corner. So, we write 'chunk_region(-1, 4, 3, 12),' to define this region.
- The second one is a mob farm in the middle of the ocean. The entire farm fits into a single chunk, namely chunk (33, 0, 15). In this case, the upper left and lower right "corner" are the same chunk, so we write 'chunk_region(33, 15, 33, 15),'.

This is what the modified section of the plugin would look like:

# Protected Regions
# Any chunk region in this list will not be deleted.
protected_regions = [
   # Use spaces to indent your lines so far that the 'c' in
   # 'chunk_region' is right under the # characters.
   # ----------- Add your protected regions below this line -----------
   chunk_region(-1, 4, 3, 12),
   chunk_region(33, 15, 33, 15),
   # ----------- Add your protected regions above this line -----------
]

If you're having trouble with this section, feel free to message the creator on Reddit. Be sure to include the modified part of the plugin in your comment. If MCEdit shows an error message, include the content of the error message, too.

In MCA selector, no code modification is needed. You simply need to roll the protected bits into the query parameter. For the above, you would do:

(Original filter) AND (NOT((xPos >= -1 AND xPos <= 3 AND zPos >= 4 AND zPos <= 12) OR (xPos == 33 AND zPos == 15))

#### Running the selection
For MCEdit: 

1. The biome deleter plugin should now be listed in thePluginsmenu.
2. Open the biome deleter plugin. It is listed asBiome deleterin thePluginsmenu.
3. Pick eitherAggressiveorCautiousmode (see above for the differences).
4. Decide whether you want to run the plugin on the entire dimension, or just on the currently selected chunks.
5. Select the biomes that you want to delete.
6. Click OK to start the plugin.This may take hoursdepending on the size of your world, and the computer you're using. MCEdit may appear unresponsive in the process, but you should see a message in MCEdit's console window every now and then that reports how many chunks have been marked for deletion. Once the plugin finishes, MCEdit will be responsive again. You should also see a message in the console window that reports how many chunks have been marked for deletion in total.
7. Now save the modified world. Again this may take a very long time, depending on the number of changed chunks.

For MCA Selector:

1. Open MCA Selector. Open the world you want to act on.
2. Go to theToolsmenu and clickFilter.
3. With some sort of reference, type in the filter expression you want to use. For example, with the ocean biome example, you should be looking for a Group of Biome selections connected by OR, and the whole Group should be connected with a set of coordinate filters with AND to rule out your area.
	- Example: (waiting for textual mode)
4. After you click "Ok", the selection will run. Check for the selected areas in the window and if you spot anything you built, unselect the area with a right-click.
5. Press "delete" or "backspace" on your keyboard. Say "yes" to the question. Now you are good to go.

At this point, your world is ready to be opened in 1.13. Take a few minutes to check your world to verify that everything went well.

## Breaking change
It is much harder to find a smooth transition among breaking-change versions. A tool called mcmerge (Java 1.7 -> 1.8-1.12) can help by adding rivers around the transition, but you have to do some preparations on the old map before using it. If you don't want the preparation, bestofboth (Java 1.7 -> 1.8-1.12) simply looks for cliffs and fill them all in.

### Splicing by Y
The changes introduced in Java Edition 1.18 additionally adds the use case of splicing the old and new worlds by Y value, so that an older map receives additional underground space. This can be done by pasting the 16x16x16 sections in from a new world of the same seed. MCA Selector allows for dealing with sections in this way.[3]

In normal situations, JE 1.18+ is able to make the terrain blend where new and old chunks connect in the 0~256 Y range, so that the change is not quite "breaking". There will be a disconnect in terms of bedrock height, making it possible to mine into the void at these boundaries.

