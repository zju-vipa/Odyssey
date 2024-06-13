# Resource location
Resource locations[1] (also known as namespaced IDs, namespaced identifiers, resource identifiers,[2] or namespaced strings[3]) are a way to declare and specify game objects in Minecraft, which can identify built-in and user-defined objects without potential ambiguity or conflicts.

## Contents
- 1 Introduction
	- 1.1 Legal characters
		- 1.1.1 Java Edition
		- 1.1.2 Bedrock Edition
	- 1.2 Conversion to string
	- 1.3 Conversion from string
- 2 Usage
	- 2.1 Java Edition
		- 2.1.1 Registries and registry objects
		- 2.1.2 Pack contents
			- 2.1.2.1 Locating contents in packs
			- 2.1.2.2 Registered pack contents
		- 2.1.3 Other contents
	- 2.2 Bedrock Edition
		- 2.2.1 Build-in contents
		- 2.2.2 Registried add-on entries
		- 2.2.3 Others
- 3 Namespaces
	- 3.1 minecraft namespace
	- 3.2 Custom namespace
	- 3.3 Other built-in namespaces
- 4 History
- 5 See also
- 6 References
- 7 External links

## Introduction
Resource locations are used as plain strings to reference blocks, items, entity types, and various other objects in vanilla Minecraft.

A valid resource location has a format of namespace:path, where only certain characters can be used.

### Legal characters
#### Java Edition
The namespace and the path of a resource location should only contain the following symbols:

- 0123456789Numbers
- abcdefghijklmnopqrstuvwxyzLowercase letters
- _Underscore
- -Hyphen/minus
- .Dot

The following characters are illegal in the namespace, but acceptable in the path:

- /Forward slash (directory separator)

The preferred naming convention for either namespace or path is snake_case.

#### Bedrock Edition
The namespace and the path of an namespaced ID can contain all symbols with the exception of slashes and colons.

The following characters are illegal in the namespace, but acceptable in the path of loot tables and functions.

- /Forward slash (directory separator)

The preferred naming convention for either namespace or path is snake_case.

### Conversion to string
A resource location would be converted to a string by appending its namespace with a : (colon) and its path.

Examples:

| Namespace       | Path                      | String representation                   |
|-----------------|---------------------------|-----------------------------------------|
| `minecraft`     | `diamond`                 | `minecraft:diamond`                     |
| `foo`           | `bar.baz`                 | `foo:bar.baz`                           |
| `minecraftwiki` | `commands/minecraft_wiki` | `minecraftwiki:commands/minecraft_wiki` |

### Conversion from string
Unlike that, resource locations can always be converted to strings; some strings cannot be converted to resource locations.

A few restrictions:

- The string can have at most one:(colon) character
- The rest of the string must fulfill the requirement forlegal characters

When the : is present, the part of the string before the : becomes the namespace, and that after the : becomes the path.

In Java Edition, and in some cases in Bedrock Edition, when the : is absent, minecraft becomes the namespace and the whole string becomes the path.

It is recommended to always include a : in the string format of resource locations.

** Examples **
| String                   | Resolved namespace                                                | Resolved path                                                                            | What the game converts it back to                                                                    |
|--------------------------|-------------------------------------------------------------------|------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| `bar:code`               | `bar`                                                             | `code`                                                                                   | `bar:code`                                                                                           |
| `minecraft:zombie`       | `minecraft`                                                       | `zombie`                                                                                 | `minecraft:zombie`                                                                                   |
| `diamond`                | `minecraft`‌[Java Edition  only]<br/>None‌[Bedrock Edition  only] | `diamond`                                                                                | `minecraft:diamond`‌[Java Edition  only]<br/>`diamond`‌[Bedrock Edition  only]                       |
| `foo/bar:coal`           | Invalid character`/`                                              |                                                                                          |                                                                                                      |
| `minecraft/villager`     | `minecraft`‌[Java Edition  only]<br/>None‌[Bedrock Edition  only] | `minecraft/villager`                                                                     | `minecraft:minecraft/villager`‌[Java Edition  only]<br/>`minecraft/villager`‌[Bedrock Edition  only] |
| `mypack_recipe`          | `minecraft`‌[Java Edition  only]<br/>None‌[Bedrock Edition  only] | `mypack_recipe`                                                                          | `minecraft:mypack_recipe`‌[Java Edition  only]<br/>`mypack_recipe`‌[Bedrock Edition  only]           |
| `mymap:schrödingers_var` | `mymap`                                                           | Invalid character`ö`‌[Java Edition  only]<br/>`schrödingers_var`‌[Bedrock Edition  only] | `mymap:schrödingers_var`‌[Bedrock Edition  only]                                                     |
| `custom_pack:Capital`    | `custom_pack`                                                     | Invalid character`C`‌[Java Edition  only]<br/>`Capital`‌[Bedrock Edition  only]          | `custom_pack:Capital`‌[Bedrock Edition  only]                                                        |

## Usage
Here list all places that use resource locations: 

### Java Edition
In Java Edition, resource locations act mainly as main keys of objects in registries, or file paths of contents in packs. Besides, some customizable or hardcoded contents also use resource locations.

#### Registries and registry objects
Each registry and each object in registries has a resource location to represent it.

There's a root registry with resource location of minecraft:root. Other registries are registered into the root registry as its entries.

The following is the list of registries and their resource locations:

** Root Registry：minecraft:root **
- Attribute:minecraft:attribute
- Block:minecraft:block
- Block entity type:minecraft:block_entity_type
- Chunk status:minecraft:chunk_status
- Command argument type:minecraft:command_argument_type
- Dimension and Level stem:minecraft:dimension
- Dimension type:minecraft:dimension_type
- Enchantment:minecraft:enchantment
- Entity type:minecraft:entity_type
- Fluid:minecraft:fluid
- Game event:minecraft:game_event
- Position source type (used by game events):minecraft:position_source_type
- Item:minecraft:item
- Menu type:minecraft:menu
- Mob effect:minecraft:mob_effect
- Particle type:minecraft:particle_type
- Potion:minecraft:potion
- Recipe serializer:minecraft:recipe_serializer
- Recipe type:minecraft:recipe_type
- Sound event:minecraft:sound_event
- Statistics type:minecraft:stat_type
- Custom Statistics:minecraft:custom_stat
- Entity data registries
	- Entity schedule activity:minecraft:activity
	- Entity memory module type:minecraft:memory_module_type
	- Entity schedule:minecraft:schedule
	- Entity AI sensor type:minecraft:sensor_type
	- Painting motive:minecraft:motive
	- Villager profession:minecraft:villager_profession
	- Villager type:minecraft:villager_type
	- Poi type:minecraft:point_of_interest_type
- Loot table serializer registries:
	- Loot condition type:minecraft:loot_condition_type
	- Loot function type:minecraft:loot_function_type
	- Loot nbt provider type:minecraft:loot_nbt_provider_type
	- Loot number provider type:minecraft:loot_number_provider_type
	- Loot pool entry type:minecraft:loot_pool_entry_type
	- Loot score provider type:minecraft:loot_score_provider_type
- Json file value provider registries:
	- Float provider type:minecraft:float_provider_type
	- Int provider type:minecraft:int_provider_type
	- Height provider type:minecraft:height_provider_type
- World generator registries:
	- Block predicate type:minecraft:block_predicate_type
	- Structure featrue rule test type:minecraft:rule_test
	- Structure featrue position rule test type:minecraft:pos_rule_test
	- World carver:minecraft:worldgen/carver
	- Configured world carver:minecraft:worldgen/configured_carver
	- Feature:minecraft:worldgen/feature
	- Configured feature:minecraft:worldgen/configured_feature
	- Structure set:minecraft:worldgen/structure_set
	- Structure processor type:minecraft:worldgen/structure_processor
	- Structure processor list:minecraft:worldgen/processor_list
	- Structure pool element type:minecraft:worldgen/structure_pool_element
	- Structure template pool:minecraft:worldgen/template_pool
	- Structure piece type:minecraft:worldgen/structure_piece
	- Structure feature:minecraft:worldgen/structure_type
	- Configured structure feature:minecraft:worldgen/structure
	- Structure placement type:minecraft:worldgen/structure_placement
	- Placement modifier type:minecraft:worldgen/placement_modifier_type
	- Placed feature:minecraft:worldgen/placed_feature
	- Biome:minecraft:worldgen/biome
	- Biome source:minecraft:worldgen/biome_source
	- Normal noise:minecraft:worldgen/noise
	- Noise generator settings:minecraft:worldgen/noise_settings
	- Density function:minecraft:worldgen/density_function
	- Density function type:minecraft:worldgen/density_function_type
	- World preset:minecraft:worldgen/world_preset
	- Flat world generator preset:minecraft:worldgen/flat_level_generator_preset
	- Chunk generator:minecraft:worldgen/chunk_generator
	- Surface condition source:minecraft:worldgen/material_condition
	- Surface rule source:minecraft:worldgen/material_rule
	- Block state provider type:minecraft:worldgen/block_state_provider_type
	- Foliage placer type:minecraft:worldgen/foliage_placer_type
	- Trunk placer type:minecraft:worldgen/trunk_placer_type
	- Tree decorator type:minecraft:worldgen/tree_decorator_type
	- Feature size type:minecraft:worldgen/feature_size_type

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

## Namespaces
|  | “ | This isn't a new concept, but I thought I should reiterate what a "namespace" is. Most things in the game has a namespace, so that if we add something and a mod (or map, or whatever) adds something, they're both different somethings. Whenever you're asked to name something, for example a loot table, you're expected to also provide what namespace that thing comes from. If you don't specify the namespace, we default to minecraft. This means that something and minecraft:something are the same thing. | „ |
|--|---|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|
|  |   | — Dinnerbone on namespaces[4]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |   |

A namespace is a domain for content. It is to prevent potential content conflicts or unintentional overrides of objects of the same name.

For example, two data packs add two minigame mechanisms to Minecraft; both have a function named start. Without namespaces, these two functions would clash and the minigames would be broken. When they have different namespaces of minigame_one and minigame_two, the functions would become minigame_one:start and minigame_two:start, which no longer conflict.

### minecraft namespace
Minecraft reserves the minecraft namespace. When a namespace is not specified, a resource location falls back to minecraft‌[Java Edition  only]. As a result, the minecraft namespace should only be used by content creators when the content needs to overwrite or modify existing Minecraft data, such as adding a function to the minecraft:load function tag.

### Custom namespace
The namespace should be distinct for different projects or content creations (e.g. a data pack, a resource pack, a mod, backing data/resource packs for a custom map, etc.)

To prevent potential clashes, the namespace should be as specific as possible.

- Avoidalphabet soups. For example, a project named "nuclear craft" should not use the namespacenc, as this is too ambiguous.
- Avoid words that are too vague.battle_royalewould not be informative to look up as well, butplayer_name_battle_royalewould be much better.

In either case, these poorly chosen namespaces reduce the exposure of a project and bring difficulties for debugging when there are multiple content creations applied to the game.

### Other built-in namespaces

  

This feature is exclusive to  Java Edition. 


The vanilla Minecraft resource pack declares Realms-oriented language files in the realms namespace (located at assets/realms/lang/.json) and game-related language files in the minecraft namespace, even though translation keys are not resource locations. The realms jar itself also declares its en_us.json language file and its various textures in the realms namespace.

In the IDs of command argument types, a brigadier namespace also appears for command argument types that are native to Brigadier.

