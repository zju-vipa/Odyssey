# Structure/JSON format
A structure is a large decoration, covering an area up to 256×256×256 block centered on the structure start. Structures often consist of multiple pieces that are fit together to form the overall structure. They are configured using JSON files within a data pack in the path data/<namespace>/worldgen/structure. To generate in a world, a structure needs to be part of at least one structure set.

## Contents
- 1 JSON format
- 2 Structure types
	- 2.1 Using Jigsaw Blocks
	- 2.2 Using structure templates
	- 2.3 Hardcoded structures
- 3 History
- 4 External links
- 5 Reference

## JSON format
- The root tag.
	- type: The ID of structure feature type.
	- biomes:biome(referenced byID), or biome#tagorlist (containingIDs) — Biomes that this structure is allowed to generate in.
	- step: The step where the structure generates. See also thefeaturesfield incustom biome. Structure features are generated prior to features in the same step. One ofraw_generation,lakes,local_modifications,underground_structures,surface_structures,strongholds,underground_ores,underground_decoration,fluid_springs,vegetal_decoration, andtop_layer_modification.
	- terrain_adaptation: (Optional, defaults tonone) The type of terrain adaptation used for the structure[needs testing].nonefor no adaptation,beard_thinis used bypillager outpostsandvillages,beard_boxis used byancient cities, andburyis used bystrongholds.
	- spawn_overrides: (Required, but can be empty. If this object doesn't contain a certain category, the category's spawn setting won't be overridden, and mobs are spawned based on biome.) Overrides the mobs that can spawn in this structure. Used for things like blaze and wither skeleton spawning in nether fortresses, and can also be used to block mobs from spawning like in ancient cities.
		- <mob category>: The key must be one ofmonster,creature,ambient,water_creature,underground_water_creature,water_ambient,misc, oraxolotls.
			- bounding_box：Can bepieceorfull. Iffull, overrides spawn setting inside the full bounding box of the structure. Ifpiece, only the bounding boxs of all structure pieces.
			- spawns：(Required, but can be empty. If empty, mobs in this category do not spawn.) A list of spawner data objects, one for each mob which should spawn in this structure.
				- : The spawner data for a single mob.
					- type: The namespaced entity id of the mob.
					- weight: How often this mob should spawn, higher values produce more spawns.
					- minCount: The minimum count of mobs to spawn in a pack. Must be greater than 0.
					- maxCount: The maximum count of mobs to spawn in a pack. Must be greater than 0. And must be not less thanminCount.
	- Additional fields depending on value oftype, seeStructure types.

## Structure types
Structures use different types. The structure types and their corresponding configuration are listed below:

### Using Jigsaw Blocks
Main article: Jigsaw structure
Jigsaw structures are using template pools and jigsaw blocks and allow full customization of structure generation using a datapack.


jigsaw



 Structure configuration
 type: jigsaw
Fields common to all structures
 start_pool: template pool (referenced by  ID or  inlined) — The template pool the structure starts from.
 size: Value between 0 and 20 (inclusive) — The depth of jigsaw structures to generate.
 start_height: If project_start_to_heightmap is unset, the structure will start at the value provided. Otherwise, the value acts as an offset from the heightmap.
Height provider
 project_start_to_heightmap: (optional) The heightmap the start height should project to. Can be WORLD_SURFACE_WG, WORLD_SURFACE, OCEAN_FLOOR_WG, OCEAN_FLOOR, MOTION_BLOCKING, or MOTION_BLOCKING_NO_LEAVES.
 start_jigsaw_name: (optional) The name of the jigsaw block the structure start attaches to.
 max_distance_from_center: The maximum 3D Chebyshev distance from the jigsaw pieces to the structure start. Value between 1 and 128 (inclusive) when  terrain_adaptation is "none", otherwise from 1 to 116 (inclusive).
 use_expansion_hack: Only used in villages.
 pool_aliases: (optional) used to rewire jigsaw pool connections by redirecting pool references on individual structure instances.
: pool alias



### Using structure templates
These structure types use specific structure templates, but they use hard-coded relative positioning between those structure templates instead of using jigsaw blocks.


end_city



 Structure configuration
 type: minecraft:end_city
Fields common to all structures




igloo



 Structure configuration
 type: minecraft:igloo
Fields common to all structures




nether_fossil



 Structure configuration
 type: minecraft:nether_fossil
Fields common to all structures
 start_height: The y-value where the structure starts.
Height provider




ocean_ruin



 Structure configuration
 type: minecraft:ocean_ruin
Fields common to all structures
 biome_temp: Either warm or cold. Determines which variant this structure uses.
 large_probability: The probability of this structure using the large variant buildings. Value between 0.0 and 1.0 (inclusive).
 cluster_probability: The probability of a cluster of ocean ruins generating, instead of just one. Value between 0.0 and 1.0 (inclusive).




ruined_portal



 Structure configuration
 type: minecraft:ruined_portal
Fields common to all structures
 setups: (Cannot be empty) A list of ruined portal setups to randomly choose one from it.
 weight: The weight this ruined portal setup is chosen.
 placement: Either on_land_surface, partly_buried, on_ocean_floor, in_mountain, underground, in_nether. Determines how the ruined portal is placed.
 air_pocket_probability: The probability that the ruined portal generates an air pocket around it. Value between 0.0 and 1.0 (inclusive).
 mossiness: Determines how mossy the ruined portal is, as an argument for minecraft:block_age processor. Value between 0.0 and 1.0 (inclusive).
 overgrown: Determines whether or not jungle leaves generate.
 vines: Determines whether or not vines generate on the ruined portal.
 can_be_cold: Determines whether or not lava and magma can be replaced with netherrack.
 replace_with_blackstone: Determines whether or not stone bricks in the ruined portal are replaced with their blackstone equivalents.




shipwreck



 Structure configuration
 type: minecraft:shipwreck
Fields common to all structures
 is_beached: (optional, defaults to false) Whether or not the shipwreck is beached.




woodland_mansion



 Structure configuration
 type: minecraft:woodland_mansion
Fields common to all structures



