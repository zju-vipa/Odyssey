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

