# Configured surface builder
Surface builders control how the surface of the terrain is shaped and what blocks it is generated with. Configured surface builders are stored as JSON files within a data pack in the path data/<namespace>/worldgen/configured_surface_builder. They are used in world generation.

## JSON format
- 
	- type:[needs testing]The type of surface builder to use, must be one of"default","mountain","shattered_savanna","gravelly_mountain","giant_tree_taiga","swamp","badlands","wooded_badlands","eroded_badlands","frozen_ocean","nether","nether_forest","soul_sand_valley","basalt_deltas", or"nope". These choices change the generation of patterns of surface materials, and in the case of "frozen_ocean" and "eroded_badlands", add generated icebergs and buttes, respectively. For example, the mixed patterns of stone in mountains and the striped terracotta of mesas are coded for through these options.
	- config: Configuration for the surface builder.
		- top_material:[needs testing]The block to use for the topmost layer of the terrain.
			- Name: The namespaced id of the block to use.
			- Properties: Block states
				- state: A block state key and its value.
		- under_material:[needs testing]The block to use directly under the topmost layer of the terrain.
			- Name: The namespaced id of the block to use.
			- Properties: Block states
				- state: A block state key and its value.
		- underwater_material:[needs testing]The block to use under bodies of water.
			- Name: The namespaced id of the block to use.
			- Properties: Block states
				- state: A block state key and its value.

