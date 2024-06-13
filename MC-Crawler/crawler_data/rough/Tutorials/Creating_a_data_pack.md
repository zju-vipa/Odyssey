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

#### Description
The text following "description" can be any string or a raw JSON text. It will show up when you hover over your data pack in the output from /datapack list and in the data pack UI when creating a world. In pack.mcmeta, it is possible to use the § symbol (see Minecraft Formatting codes) in the description of pack.mcmeta and the data pack name.

### Testing your pack
Once you have created your pack.mcmeta, try testing it out in-game! Open the world or, if you are already in the world, type /reload, then type /datapack list. It should list two entries. One of the two should appear as [file/(your data pack's name) (world)], where your data pack's folder name goes at (your data pack's name). When you hover over your data pack's entry, you should see the description of your data pack as you have written in  description of your pack.mcmeta.

When your pack shows up, you are ready to move on.

#### Troubleshooting
If you don't see your pack in the list, make sure your pack.mcmeta file is correct and saved. Look for any missing curly brackets {}, commas ,, colons :, quotation marks "", or square brackets []. Remember that for each open brace, quotation, or square bracket, you must have a closing bracket, quotation, or square brackets. If you still don't see your pack, make sure it's in the right folder.

## Adding content to your pack
### Naming
See also: Resource location

Make a folder called data in your data pack folder, where you have placed the pack.mcmeta file in. In this data folder you have to create one or more folders which will act as your namespaces.

Entries in data packs have resource locations in a fashion of namespace:path. The corresponding file would be located at data/namespace/(data_type)/path.(suffix). Note that / characters in the path will be translated into directory separators.

A few examples:

- anitem tagof IDdummy:foo_proof/barwould be located atdata/dummy/tags/item/foo_proof/bar.json
- afunctionof IDfoo:handler/bar_callwould be located atdata/foo/functions/handler/bar_call.mcfunction

#### Legal characters
Namespaces, paths and other folder and file names in the data pack should only contain the following symbols:

- 0123456789Numbers
- abcdefghijklmnopqrstuvwxyzLowercase letters
- _Underscore
- -Hyphen/minus
- /Forward Slash/Directory separator (Can't be used in namespace)
- .Period

The preferred naming convention is lower_case_with_underscores, called lower snake case.

#### Namespace
Most objects in the game use namespaced resource locations to prevent potential content conflicts or unintentional overrides.

For example, if two data packs add two new minigame mechanisms to Minecraft and both have a function named start. Without namespaces, these two functions would clash and the minigames would be broken. But if they have different namespaces of minigame_one and minigame_two, the functions would become minigame_one:start and minigame_two:start, which no longer conflict.

Most of the time when Minecraft requires an ID, such as for /function, you should provide the namespace in addition to the path. If you don't specify the namespace, it will fallback to minecraft. 

Make sure to always use your own namespace for anything new that you add, and only use other namespaces if you're explicitly overriding something else, or, in the case of tags, appending to something else.

For example, Minecraft uses the minecraft namespace, which means that this namespace should only be used when the data pack needs to overwrite existing Minecraft data or to add its entries to vanilla tags.

### Functions
Main article: Function (Java Edition)
See also: Tutorials/Command blocks and functions

Functions are a set of commands that can be run in order.

To add functions, first create a folder named functions inside the namespace folder. Then, create a file named (function_name).mcfunction in this folder or in any of its subfolders. This will be your function file. Your function will be named in the game as (namespace):(name) or (namespace):(subfolder1)/(subfolder2)/.../(name) when the function file is located in a subfolder.

### Loot tables
Main article: Loot table
Loot tables will tell Minecraft what should be dropped when a mob dies or what should be generated inside containers, like chests, when opened for the first time, they can also be called by the /loot command.

To add loot tables, first create a folder named loot_tables inside the namespace folder. Then, create a file named (loot_table_name).json in this folder or in any of its subfolders. This will be your loot table file. Your loot table will be named in the game as (namespace):(name) or (namespace):(subfolder1)/(subfolder2)/.../(name) if the file is located in a subfolder. All the vanilla loot tables are in the minecraft namespace.

Here is an example of a cow's loot table, it can be used as a reference:

{
  "type": "minecraft:entity",
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 0,
                "max": 2,
                "type": "minecraft:uniform"
              }
            },
            {
              "function": "minecraft:looting_enchant",
              "count": {
                "min": 0,
                "max": 1
              }
            }
          ],
          "name": "minecraft:leather"
        }
      ]
    },
    {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "functions": [
            {
              "function": "minecraft:set_count",
              "count": {
                "min": 1,
                "max": 3,
                "type": "minecraft:uniform"
              }
            },
            {
              "function": "minecraft:furnace_smelt",
              "conditions": [
                {
                  "condition": "minecraft:entity_properties",
                  "predicate": {
                    "flags": {
                      "is_on_fire": true
                    }
                  },
                  "entity": "this"
                }
              ]
            },
            {
              "function": "minecraft:looting_enchant",
              "count": {
                "min": 0,
                "max": 1
              }
            }
          ],
          "name": "minecraft:beef"
        }
      ]
    }
  ]
}

### Structures
Structures can be used with structure blocks and jigsaw blocks and/or can overwrite how certain vanilla structures look in Minecraft. It is saved in an NBT format. You can create an NBT file by using a structure block or by exporting a build using a third party program such as MCEdit.

To add structures to a data pack, first create a folder named structures inside the namespace folder. Then, put your structure file in this folder or in any of its subfolders. Your structure will be named in the game as (namespace):(name) or (namespace):(subfolder1)/(subfolder2)/.../(name) if the file is located in a subfolder.

### World generation
Main article: Custom world generation
Custom world generation allows your pack to change how the world generates. This is particularly useful in conjunction with custom worlds.

To change world generation, first create a folder named worldgen inside the namespace folder. Then, put your noise_settings file in this folder or in any of its subfolders. Your changes will be named in the game as (namespace):(name) or (namespace):(subfolder1)/(subfolder2)/.../(name) if the file is located in a subfolder.

### Advancements
Main article: Advancements
Advancements can be completed by players and give various rewards.

To add advancements, first create a folder named advancements inside the namespace folder. Then, create a file named (advancement_name).json (You can't put spaces in the file name. Use lowercase letters in the file name). in this folder or in any of its subfolders. This will be your advancement file. Your advancement will be named in the game as (namespace):(name) or (namespace):(subfolder1)/(subfolder2)/.../(name) if the file is located in a subfolder.

### Recipes
Main article: Recipe
Recipes are used to let players craft items.

To add recipes, first create a folder named recipes inside the namespace folder. Then, create a file named (recipe_name).json in this folder or in any of its subfolders. This will be your recipe file. Your recipe will be named in the game as (namespace):(name) or (namespace):(subfolder1)/(subfolder2)/.../(name) if the file is located in a subfolder.

#### Shaped crafting
See also: Recipe § minecraft:crafting_shaped

The first common type of crafting is shaped crafting.

{
  "type": "minecraft:crafting_shaped",
  "pattern": [
    "123",
    "231",
    "312"
  ],
  "key": {
    "1": {
      "item": "Resource location of the item"
    },
    "2": {
      "item": "Resource location of the item"
    },
    "3": {
      "item": "Resource location of the item"
    }
  },
  "result": {
    "item": "Resource location of the item",
    "count": Number of items produced
  }
}

This is a rough example of a shaped crafting recipe, as specified by the crafting_shaped type. pattern is a list used to specify the shape of the crafting recipe. It contains a maximum of 3 strings, each string standing for one row in the crafting grid. These strings then contain a maximum of 3 single characters next to each other, each character standing for one spot in the crafting grid. You don't need all 3 strings, nor do you need to have 3 characters in each string. But each string should contain the same amount of characters. You can use spaces to indicate empty spots.

key is a compound used to specify what item should be used for which character in pattern. This can either be specified using item followed by an item ID or tag followed by an item data pack tag.

The result compound speaks for itself, it specified what the resulting item should be. count is used to specify how many of the item should be given.

This is the original recipe for a piston (can be used as a reference):

{
  "type": "crafting_shaped",
  "pattern": [
    "TTT",
    "#X#",
    "#R#"
  ],
  "key": {
    "R": {
      "item": "minecraft:redstone"
    },
    "#": {
      "item": "minecraft:cobblestone"
    },
    "T": {
      "tag": "minecraft:planks"
    },
    "X": {
      "item": "minecraft:iron_ingot"
    }
  },
  "result": {
    "item": "minecraft:piston"
  }
}

#### Shapeless crafting
See also: Recipe § minecraft:crafting_shapeless

There's another common type of recipes, a shapeless recipe. The list with multiple items allows alternatives for the given slot such as Oak Plank and Birch Plank.

{
  "type": "crafting_shapeless",
  "ingredients": [
    {
      "item": "<item ID>"
    },
    {
      "item": "<item ID>"
    },
    [
      {
        "item": "<item ID>"
      },
      {
        "item": "<item ID>"
      }
    ]
  ],
  "result": {
    "item": "<item ID>",
    "count": 5
  }
}

As specified by the crafting_shapeless type, this is a recipe without a pattern. The ingredients can be put in the crafting grid in any shape or form. In the example, there's a list inside the ingredients compound. This means any of the items in this list can be used.

This is the original recipe for Fire Charge (can be used as a reference):

{
  "type": "crafting_shapeless",
  "ingredients": [
    {
      "item": "minecraft:gunpowder"
    },
    {
      "item": "minecraft:blaze_powder"
    },
    [
      {
        "item": "minecraft:coal"
      },
      {
        "item": "minecraft:charcoal"
      }
    ]
  ],
  "result": {
    "item": "minecraft:fire_charge",
    "count": 3
  }
}

It is also possible to create new smelting recipes.

{
  "type": "smelting",
  "ingredient": {
    "item": "<item ID>"
  },
  "result": "<item ID>",
  "experience": 0.35,
  "cookingtime": 200
}

This is a rough example of a smelting recipe. "ingredient" is used to specify the item you are going to smelt. "result" is going to specify the result. In "experience", you are able to choose the amount of xp gained for smelting, and in "cookingtime" the amount of time that it will take for the item to smelt, which in this case is 10 seconds (200 ticks = 10 seconds).

This is the default smelting recipe for a diamond ore:

{
  "type": "smelting",
  "ingredient": {
    "item": "minecraft:diamond_ore"
  },
  "result": "minecraft:diamond",
  "experience": 1,
  "cookingtime": 200
}

### Tags
Main article: tag
Tags are used to group blocks, items, entities, or functions together. Additionally, the minecraft:tick function tag is used to run functions every tick and the minecraft:load function tag is used to run functions every time the world is (re)loaded.

To add tags, first create a folder named tags inside the namespace folder. Inside this folder, create folders named blocks, items and functions. Then, create a file named (tag_name).json in one of these folders or in any of their subfolders. This will be your tag file. Your tag will be named in the game as (namespace):(name) or (namespace):(subfolder1)/(subfolder2)/.../(name) if the file is located in a subfolder.

### Predicates
Main article: Predicate
Predicates are technical JSON files that represent the conditions for loot tables, /execute if predicate command, or predicate target selector argument.

To add predicates, first create a folder named predicates inside the namespace folder. Then, create a file named (predicate_name).json (You can't put spaces in the file name. Use lowercase letters in the file name). in this folder or in any of its subfolders. This will be your predicate file. Your predicate will be named in the game as (namespace):(name) or (namespace):(subfolder1)/(subfolder2)/.../(name) if the file is located in a subfolder.

### Dimensions
Main article: Custom dimension
Dimensions are JSON file used to specify all the dimensions a world contains.

To add dimensions, first create a folder named dimension inside the namespace folder. Then, create a file named (dimension_name).json (You can't put spaces in the file name. Use lowercase letters in the file name). in this folder. This will be your dimension file.

Custom dimensions can be accessed in game using /execute in (namespace):(dimension_name)

## Utilities

  


This list is incomplete; you can help by expanding it.


Many utilities have been created in order to make programming data packs easier. This is a reference list for utilities such as transpilers or syntax highlighting plugins. Please exercise caution when installing third-party programs onto your computer, as they are not actively monitored and may contain malware. 

| Name             | Hosting | Description                                                                                                                 | Link                                                        |
|------------------|---------|-----------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| Minecraft Script | GitHub  | A language based on JavaScript that can be compiled into a working data pack using a Node.js compiler.                      | https://mcscript.stevertus.com/                             |
| Minity           | GitHub  | Another scripting language that compiles into data packs using a Node.js compiler.                                          | https://github.com/minity-script/minity                     |
| TMS Transpiler   | GitHub  | A python tool that can assemble indented mcfunction code into valid files. Great if you don't want to learn a new language. | https://github.com/davidkowalk/advanced_minecraft_scripting |
| ObjD             | Pub     | A dart framework for creating data packs to minimize the repetitive work to be done.                                        | https://objd.stevertus.com/                                 |

Another option is to use a visual interface to create the framework or the content for your project.

| Name                             | Hosting                      | Description                                                              | Link                                                      |
|----------------------------------|------------------------------|--------------------------------------------------------------------------|-----------------------------------------------------------|
| Datapack Creator                 | Planet Minecraft             | An IDE for creating data packs with some useful tools                    | https://www.planetminecraft.com/mod/datapack-creator-ide/ |
| NBTData Pack Generator           | nbt-data.com                 | An online generator for a raw data pack framework without any functions. | https://www.nbt-data.com/datapack-generator               |
| Recipe Generator                 | thedestruc7i0n.ca            | An Online Generator to generate the JSON files required for crafting.    | https://crafting.thedestruc7i0n.ca/                       |
| Minecraft Tools Recipe Generator | minecraft.tools              | An Online Generator to generate the JSON files required for crafting.    | https://minecraft.tools/en/custom-crafting.php            |
| Minecraft Recipe Generator       | recipegeneratorminecraft.com | An Online Generator to create data packs for custom recipes.             | https://recipegeneratorminecraft.com                      |
| Misode's Data Pack Generator     | GitHub                       | JSON Generator for Minecraft Data Packs                                  | https://misode.github.io/                                 |
| MCStacker for MC 1.19            | mcstacker.net/               | A collection of command generators.                                      | https://mcstacker.net/                                    |
| Origin Creator                   | GitHub                       | A fully featured webtool for creating data packs.                        | https://www.mathgeniuszach.com/apps/origin-creator/       |
| MCreator                         | mcreator.net                 | A easy-to-use, fully featured graphical tool for creating data packs.    | https://mcreator.net/                                     |
| MCDatapacker                     | Github                       | An offline program to create and edit data packs                         | https://github.com/IoeCmcomc/MCDatapacker                 |

If you use a code editor, you may want to format your data pack files with syntax highlighting. Depending on your text editor extra steps may have to be taken to install it in your environment.

| IDE/Editor                     | Description                                                       | Link                                                                                  |
|--------------------------------|-------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| Visual Studio CodeSublime Text | Language grammars and syntax highlighting for mcfunction files.   | https://github.com/Arcensoth/language-mcfunction                                      |
| Notepad++                      | Syntax highlighting.                                              | https://pastebin.com/hbMiJ3YV                                                         |
| Visual Studio Code             | Heavy language features for JSON and mcfunction files.            | https://marketplace.visualstudio.com/items?itemName=SPGoding.datapack-language-server |
| IntelliJ IDEA                  | Allows connecting to an external IDE to do more optimized coding. | https://plugins.jetbrains.com/plugin/22587-minecraft-command-devkit                   |



