# Data pack
The data pack system provides a way for players to further customize their Minecraft experience. Data packs can be used to override or add new advancements, dimensions, functions, loot tables, predicates, item modifiers, recipes, structures, tags, damage types, world generation settings, and biomes without any code modification.

## Contents
- 1 Usage
- 2 Contents
	- 2.1 Folder structure
	- 2.2 pack.mcmeta
		- 2.2.1 Pack format
	- 2.3 data
- 3 History
- 4 Issues
- 5 Gallery
- 6 See also
- 7 External links

## Usage
Data packs can be placed in the .minecraft/saves/(world)/datapacks folder of a world. Each data pack is either a sub-folder or a .zip file within the datapacks folder. After it is in the folder, a data pack is enabled for that world when the world is reloaded or loaded.

Data packs load their data based on the load order. This order can be seen and altered by using the /datapack command and is stored in the level.dat file.

The player can also select data packs at the world creation screen by clicking the Data Packs button and dragging-and-dropping their data pack folders/zip-files there. This is similar to the resource pack selection screen, and allows the player to enable data packs before the world is generated, and easily customize the load order too.

## Contents
### Folder structure
Data packs use the following folder structure:

- (data pack name)
	- pack.mcmeta
	- pack.png
	- data
		- (namespace)advancements
(advancement).json
functions
(function).mcfunction
item_modifiers
(item_modifier).json
loot_tables
(loot_table).json
predicates
(predicate).json
recipes
(recipe).json
structures
(structure).nbt
chat_type
(chat type).json
damage_type
(damage type).json
tags 
blocks
(tag).json
entity_types
(tag).json
fluids
(tag).json
functions
(tag).json
game_events
(tag).json
items
(tag).json
(registry name)
(tag).json
dimension
(dimension).json
dimension_type
(dimension type).json
worldgen 
biome
(biome).json
configured_carver
(carver).json
configured_feature
(feature).json
density_function
(density_function).json
noise
(noise).json
noise_settings
(noise_settings).json
placed_feature
(placed_feature).json
processor_list
(block_processor).json
structure
(structure).json
structure_set
(structure_set).json
template_pool
(jigsaw_pool).json
world_preset
(preset).json
flat_level_generator_preset
(flat_level_generator_preset).json
			- advancements
				- (advancement).json
			- functions
				- (function).mcfunction
			- item_modifiers
				- (item_modifier).json
			- loot_tables
				- (loot_table).json
			- predicates
				- (predicate).json
			- recipes
				- (recipe).json
			- structures
				- (structure).nbt
			- chat_type
				- (chat type).json
			- damage_type
				- (damage type).json
			- tagsblocks
(tag).json
entity_types
(tag).json
fluids
(tag).json
functions
(tag).json
game_events
(tag).json
items
(tag).json
(registry name)
(tag).json
				- blocks
					- (tag).json
				- entity_types
					- (tag).json
				- fluids
					- (tag).json
				- functions
					- (tag).json
				- game_events
					- (tag).json
				- items
					- (tag).json
				- (registry name)
					- (tag).json
			- dimension
				- (dimension).json
			- dimension_type
				- (dimension type).json
			- worldgenbiome
(biome).json
configured_carver
(carver).json
configured_feature
(feature).json
density_function
(density_function).json
noise
(noise).json
noise_settings
(noise_settings).json
placed_feature
(placed_feature).json
processor_list
(block_processor).json
structure
(structure).json
structure_set
(structure_set).json
template_pool
(jigsaw_pool).json
world_preset
(preset).json
flat_level_generator_preset
(flat_level_generator_preset).json
				- biome
					- (biome).json
				- configured_carver
					- (carver).json
				- configured_feature
					- (feature).json
				- density_function
					- (density_function).json
				- noise
					- (noise).json
				- noise_settings
					- (noise_settings).json
				- placed_feature
					- (placed_feature).json
				- processor_list
					- (block_processor).json
				- structure
					- (structure).json
				- structure_set
					- (structure_set).json
				- template_pool
					- (jigsaw_pool).json
				- world_preset
					- (preset).json
				- flat_level_generator_preset
					- (flat_level_generator_preset).json

More than one directory for different namespaces may exist under the data directory.

### pack.mcmeta
A data pack is identified by Minecraft based on the presence of the pack.mcmeta file in the root directory of the data pack, which contains data in JSON format.

- The root object.
	- pack: Holds the data pack information.
		- description: AJSON textthat appears when hovering over the data pack's name in the list given by the/datapack listcommand, or when viewing the pack in the Create World screen.
		- pack_format: Pack version. If this number does not match the current required number, the data pack displays a warning and requires additional confirmation to load the pack. See§ Pack formatfor a full list of pack format numbers.
		- supported_formats: (Optional) Describes a range for pack formats that this pack supports.  Examples:16,[16,17],{"min_inclusive": 16, "max_inclusive": 17}
	- filter: (Optional) Section for filtering out files from data packs applied below this one. Any file that matches one of the patterns insideblockis treated as if it was not present in the pack at all.
		- block: List of patterns
			- 
				- namespace: Aregular expressionfor the namespace of files to be filtered out. If unspecified, it applies to every namespace.
				- path: Aregular expressionfor the paths of files to be filtered out. If unspecified, it applies to every file.
	- overlays: (Optional) Section for specifying the overlays, which are sub-packs applied over the "normal" contents of a pack. Their directories have their own assets and data directories, and are placed in the pack's root directory.
		- entries: List of overlays. The order is important, as the first in the list is applied first.
			- 
				- formats: Describes a range for pack formats when this overlay should be active.  Examples:16,[16,17],{"min_inclusive": 16, "max_inclusive": 17}
				- directory: The directory to overlay for the respective versions (allowed characters:a-z,0-9,_and-).

pack.mcmeta, as used by the "vanilla" data pack in 1.20.4, as found in the client and official server jars:

pack.mcmeta
{
    "pack": {
        "description": "The default data for Minecraft",
        "pack_format": 26
    }
}

#### Pack format
For the full list of pack formats in all versions, see Pack format § List of data pack formats.

| Value | Releases          | Significant/Breaking Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-------|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `4`   | 1.13–1.14.4       | Added the initial pack format version of 4.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `5`   | 1.15–1.16.1       | Addedpredicates.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `6`   | 1.16.2–1.16.5     | Added experimental support forcustom world generation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `7`   | 1.17–1.17.1       | The`/replaceitem`command was replaced with`/item`. The`set_damage`loot function now require a validtypefield.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `8`   | 1.18–1.18.1       | Loot tables now require atypefield. Removed length limits for scoreboards, score holders and team names.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `9`   | 1.18.2            | The`/locate`command now takes a configured structure as its first parameter rather than a structure type, so many grouped structures now require a structure type tag. E.g.`/locate village`is now`/locate #village`.                                                                                                                                                                                                                                                                                                                                                         |
| `10`  | 1.19–1.19.3       | Data packs can now have afiltersection in`pack.mcmeta`. Merged`/locatebiome`with`/locate`, changing its syntax.                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `12`  | 1.19.4            | Addeddamage types. Removed all boolean flags in damage predicates, instead damage type tags can now be tested for. Biome fieldprecipitationchanged tohas_precipitation.                                                                                                                                                                                                                                                                                                                                                                                                       |
| `15`  | 1.20–1.20.1       | Changed sign NBT. E.g.`Text1`is now`front_text.messages[0]`. All fields in`placed_block`,`item_used_on_block`, and`allay_drop_item_on_block`advancement triggers have been collapsed to a single location field. Renamed the`alternative`predicate to`any_of`.                                                                                                                                                                                                                                                                                                                |
| `18`  | 1.20.2            | Addedfunction macros. Effects now use namespaced IDs rather than numeric values in NBT. E.g.`1`is now`minecraft:speed`.                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `26`  | 1.20.3–1.20.4     | Text componentsare parsed more strictly. Renamed`grass`block and item to`short_grass`. Addedscoreboarddisplay names and number formats.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `41`  | 1.20.5‌[upcoming] | Renamed the`sweeping`enchantmentto`sweeping_edge`. Changed the behavior of the`item_used_on_block`advancement trigger. Replaced some behavior of amplifiers above 127 withattributes. Unstructured NBT data attached item stacks has been replaced with structured components. Removed`durability`,`potions`,`nbt`, and`enchantments`fields in item predicates. Recipe output can now specify components. Int and float providers used in worldgen definitions are no longer wrapped in an extra`value`field next to`type`. Added new item sub-predicates and loot functions. |

### data
See also: Resource location § Namespaces

This folder contains all the data under one or multiple namespaces. It can contain advancements, chat_type, damage_type, dimension, dimension_type, functions, item_modifiers, loot_tables, predicates, recipes, structures, tags, and/or worldgen folders. The worldgen folder can contain biome, configured_carver, configured_feature, density_function, flat_level_generator_preset, noise, noise_settings, placed_feature, processor_list, structure, structure_set, template_pool and world_preset folders.

The dimension, dimension_type and worldgen folders are currently experimental features.

Each advancement, function, loot table, predicate, structure, recipe and tag file can be placed directly in their respective folder but sub-folders are also allowed.

