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

