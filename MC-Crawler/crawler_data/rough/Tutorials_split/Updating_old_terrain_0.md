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

