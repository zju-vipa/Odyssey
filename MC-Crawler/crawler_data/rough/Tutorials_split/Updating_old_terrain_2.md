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


