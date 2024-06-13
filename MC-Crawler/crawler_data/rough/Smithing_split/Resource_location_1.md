#### Pack contents
Resource locations are also used to represent files' paths in data pack or resource pack.

** Data pack **
- Tags
- Advancements
- Recipes
- Predicates
- Loot tables
- Item modifier
- Functions
- Structure files
- Dimensions
- Dimension types
- World generator contents
	- Biomes
	- Configured carvers
	- Configured features
	- Configured structure features
	- Placed features
	- Structures
	- Structure sets
	- Processor lists
	- Template pools
	- Noise
	- Noise generator settings
	- Density functions
	- Flat level generator presets
	- World presets

** Resource pack **
- Block states
- Models
- Textures
- Sounds
- Fonts
- Font resource files
- Particles
- shaders

##### Locating contents in packs
Given objects from resource packs and data packs are files, the resource locations represent corresponding paths.

Though the locations vary by object type and the pack type the object type belongs to, there is a pattern to follow. In general, the location is in the fashion of pack_type/namespace/object_type/name.suffix, where all the / (forward slash) symbol (may be part of object_type or name) is replaced by operating system-dependent directory separator.

Given the type of content we want to locate, we can find out the corresponding pack_type, object_type, and suffix. Then, we can substitute in and find out the final file location of the content.


Examples




Resource location
Content Type
pack_type
object_type
suffix
Final Location


my_texture_pack:diamonds
Texture
assets
textures
png
assets/my_texture_pack/textures/diamonds.png


abc:run_game
Function
data
functions
mcfunction
data/abc/functions/run_game.mcfunction


block/torch(same as minecraft:block/torch)
Model
assets
models
json
assets/minecraft/models/block/torch.json


load(same as minecraft:load)
Function Tag
data
tags/functions
json
data/minecraft/tags/functions/load.json


rocket_pack:industry/start_of_story
Advancement
data
advancements
json
data/rocket_pack/advancements/industry/start_of_story.json


##### Registered pack contents
A registried pack content refers to pack content that is registered into a registry when the pack is loaded. For a registried pack content, its resource location works as both main key of registry entry and path of its resource file.


List of registered pack contents




Content Type
Registered into
Folder
Suffix


Dimensions
minecraft:dimension
data/namespace/dimension
json


Dimension types
minecraft:dimension_type
data/namespace/dimension_type
json


Configured carvers
minecraft:worldgen/configured_carver
data/namespace/worldgen/configured_carver
json


Configured features
minecraft:worldgen/configured_feature
data/namespace/worldgen/configured_feature
json


Configured structure features
minecraft:worldgen/structure
data/namespace/worldgen/structure
json


Structure sets
minecraft:worldgen/structure_set
data/namespace/worldgen/structure_set
json


Processor lists
minecraft:worldgen/processor_list
data/namespace/worldgen/processor_list
json


Template pools
minecraft:worldgen/template_pool
data/namespace/worldgen/template_pool
json


Placed features
minecraft:worldgen/placed_feature
data/namespace/worldgen/placed_feature
json


Biomes
minecraft:worldgen/biome
data/namespace/worldgen/biome
json


Noise
minecraft:worldgen/noise
data/namespace/worldgen/noise
json


Noise generator settings
minecraft:worldgen/noise_settings
data/namespace/worldgen/noise_settings
json


Density functions
minecraft:worldgen/density_function
data/namespace/worldgen/density_function
json


Flat level generator presets
minecraft:worldgen/flat_level_generator_preset
data/namespace/worldgen/flat_level_generator_preset
json


World presets
minecraft:worldgen/world_preset
data/namespace/worldgen/world_preset
json


#### Other contents
** Customizable contents **
- Boss bars
- Command storages

** Hardcoded contents **
- Cat types for predicates (e.g. textures/entity/cat/tabby.png, textures/entity/cat/jellie.png)
- Criteria triggers
- Item properties (i.e. item predicates in models. e.g. angle, custom_model_data)
- Loot context param sets (i.e. types of loot table. e.g. barter, generic)
- Unaccessible contents:
	- Suggestion providers for autocompletion of commands (e.g. summonable_entities, all_recipes)
	- Entity models
	- Loot context params (e.g. this_entity, origin, tool)


### Bedrock Edition
Unlike Java Edition, where there is a unified standard and handling methods of resource location, namespaced identifiers are usually treated as normal strings in Bedrock Edition. Moreover, namespaced identifiers are even not required in some cases (e.g. recipe's identifier). However, for content creators, it is recommended to always use namespaced identifiers no matter whether required or not.

The following is a list of all places that use namespaced identifiers: 

#### Build-in contents
- Vanilla blocks, items, entities, status effects, dimensions, biomes, structures, features, etc.
- Entity attributes
- Item components for commands
- Components for block, entity, etc. used in add-on files
- Json schemas for addons
- Gametest script enabled components

#### Registried add-on entries
A registried add-on entry refers to add-on content that is registered with an identifier which is declared in add-on files.

Here is a list of registried add-on entries whose identifiers can be namespaced.

** Behavior pack contents **
- Blocks
- Entities
- Items
- Spawn rules
- Biomes
- Features
- Feature rules
- Volumes
- Recipes
- Structures
- Gametests
- Diolog scenes
- Spawn groups

** Resource pack contents **
- Attachables
- Cameras
- Particle effects
- Fog settings

Some custom fields in add-on files can also be namespaced, such as custom block properties and entity component groups, which aren't listed here.

#### Others
- Structures saved with structure block

