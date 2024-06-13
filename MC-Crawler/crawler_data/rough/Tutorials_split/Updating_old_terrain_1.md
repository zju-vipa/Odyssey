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

