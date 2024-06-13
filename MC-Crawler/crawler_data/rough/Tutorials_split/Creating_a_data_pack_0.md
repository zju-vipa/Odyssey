# Tutorials/Creating a data pack
This tutorial shows how to create a data pack. Data packs can be used to add or modify functions, loot tables, structures, advancements, recipes, tags, dimensions, predicates and world generation.

## Contents
- 1 Setting up your data pack
	- 1.1 Finding the world directory
	- 1.2 Folder structure
	- 1.3 Creating a pack.mcmeta file
		- 1.3.1 Pack format
		- 1.3.2 Description
	- 1.4 Testing your pack
		- 1.4.1 Troubleshooting
- 2 Adding content to your pack
	- 2.1 Naming
		- 2.1.1 Legal characters
		- 2.1.2 Namespace
	- 2.2 Functions
	- 2.3 Loot tables
	- 2.4 Structures
	- 2.5 World generation
	- 2.6 Advancements
	- 2.7 Recipes
		- 2.7.1 Shaped crafting
		- 2.7.2 Shapeless crafting
	- 2.8 Tags
	- 2.9 Predicates
	- 2.10 Dimensions
- 3 Utilities
- 4 See also

## Setting up your data pack
To create a data pack, start by navigating to the datapacks folder of your world. The location of the folder varies depending on your operating system and the type of world:

### Finding the world directory
Main article: .minecraft
To create a data pack, you will need to find the datapacks folder of your world. The location of the world folder depends on your operating system and the type of world:

- In Singleplayer:
	- For Windows, it can be found in%APPDATA%\.minecraft\saves\(your world).
	- For macOS, find your user folder, then navigate toLibrary/Application Support/Minecraft/saves/(your world).
	- For Linux, it is at~/.minecraft/saves/(your world)

- In Multiplayer:
	- Find the root directory of your server (whereserver.propertiesis located), then navigate toworld.

Once you are in the datapacks folder, create a folder with a name of your choice. This will be your data pack's name. Enter the data pack folder.

### Folder structure
A data pack needs to follow a specific folder structure. Every content in your data pack has its own place.


Data packs use the following folder structure:


(datapack folder)
pack.mcmeta
pack.png
data
(namespace)
advancements
functions
item_modifiers
loot_tables
predicates
recipes
structures
chat_type
damage_type
tags
blocks
entity_types
fluids
functions
game_events
items
chat_type
damage_type
(registry name)
dimension
dimension_type
worldgen
biome
configured_carver
configured_feature
density_function
noise
noise_settings
placed_feature
processor_list
structure
structure_set
template_pool
world_preset
flat_level_generator_preset



### Creating a pack.mcmeta file
Instructions on how to enable file extensions on Windows 11
See also: Data pack § pack.mcmeta

To create this file, right click within your data pack folder and create a new text document. Name this file pack.mcmeta.

Note: Ensure the file extension is .mcmeta and not .txt when you rename it! In other words, remove your old file extension. You may be warned that changing a file name extension could make the file unusable. However, this actually indicates that you have renamed the pack.mcmeta file correctly.

If you can't see file extensions, you'll have to turn them on. For Windows 11, you can turn them on by open the "View" dropdown menu, then hover over the "Show" option, then turn on the "File name extensions" option. For Windows 10, you can turn them on by going to the View menu of the file explorer and checking the check box for file name extensions. For Windows beneath Windows 10, you can uncheck "hide extensions" in folder settings.

Open pack.mcmeta in your text editor and paste or type the following:

{
  "pack": {
    "pack_format": 26,
    "description": "This is a description of your data pack."
  }
}

Be sure to type the code exactly as shown above. Missing or extra quotation marks, colons, or brackets can prevent your data pack from working correctly.

#### Pack format
The value of "pack_format" tells Minecraft which version of the game your data pack is compatible with. The following list shows which versions each value is currently associated with: 

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

If you're making a data pack for a snapshot version, you can see all data pack formats here.

In data pack format 16 and higher, there is an optional supported_formats line that can be added.

- supported_formatsdescribes a range for pack formats that the pack supports, even when using the list format.
	- Examples:26,[18, 26],{"min_inclusive": 18, "max_inclusive": 26}
	- Ifsupported_formatsis present, it must contain the value declared inpack_format.
	- Since this information is ignored by older versions of the game, they will always see a "normal", single-version pack, without any extended compatibility.
	- The entire line would look something like"supported_formats": {"min_inclusive": 18, "max_inclusive": 26},.

