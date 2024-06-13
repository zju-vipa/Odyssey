# Tutorials/Adding custom trims
This tutorial explains how to create a data pack and resource pack that adds custom trim materials or patterns. It assumes you already know how to create a data pack.

## Contents
- 1 Custom trim patterns
	- 1.1 Trim pattern
	- 1.2 Item tag
	- 1.3 Recipe
	- 1.4 Translation
	- 1.5 Atlas
	- 1.6 Textures
- 2 Custom trim materials
	- 2.1 Trim material
	- 2.2 Item tag
	- 2.3 Translation
	- 2.4 Atlases
	- 2.5 Color palette texture
	- 2.6 Item models
- 3 Custom trimmable items
	- 3.1 Item tag
	- 3.2 Item models
	- 3.3 Atlas
	- 3.4 Mask texture
- 4 See also
- 5 References

## Custom trim patterns
A smithing recipe showing a custom "Stripes" trim pattern
This example adds a new "Stripes" pattern that works with all the vanilla armor types and colors.

### Trim pattern
Let's start with the central file in the trim_pattern folder in the data pack.





Changes to this file won't be applied when running /reload[1]. Always leave and reopen the world to apply the new changes!


data/example/trim_pattern/stripes.json
{
  "asset_id": "example:stripes",
  "description": {
    "translate": "trim_pattern.example.stripes"
  },
  "template_item": "minecraft:stick"
}

- The root object
	- asset_id: A resource location which will be used in the resource pack.
	- description: AJSON text componentused for the tooltip on items.
	- template_item: Theitemrepresenting this pattern.
	- decal: Optional, defaults to false. If true, the pattern texture will be masked based on the underlying armor.

### Item tag
The stick needs to be added to the #minecraft:trim_templates item tag. This item tag is not referenced in a recipe, but is used in the game internally making the template usable in the smithing recipes.

data/minecraft/tags/items/trim_templates.json
{
  "values": [
    "minecraft:stick"
  ]
}

### Recipe
The next piece in the data pack is the smithing recipe. For the full JSON format, see Recipe § smithing_trim.

data/example/recipes/stripes_armor_trim.json
{
  "type": "minecraft:smithing_trim",
  "addition": {
    "tag": "minecraft:trim_materials"
  },
  "base": {
    "tag": "minecraft:trimmable_armor"
  },
  "template": {
    "item": "minecraft:stick"
  }
}

### Translation
Moving on to the resource pack, the first step is to create the translation that we referenced in the trim pattern's  description field.

assets/example/lang/en_us.json
{
  "trim_pattern.example.stripes": "Stripes Armor Trim"
}

### Atlas
And now for the complicated bit: adding the texture permutations for the different colors and armor types. This is done by appending the minecraft:armor_trims atlas file.

assets/minecraft/atlases/armor_trims.json
{
  "sources": [
    {
      "type": "minecraft:paletted_permutations",
      "textures": [
        "example:trims/models/armor/stripes",
        "example:trims/models/armor/stripes_leggings"
      ],
      "palette_key": "trims/color_palettes/trim_palette",
      "permutations": {
        "quartz": "trims/color_palettes/quartz",
        "iron": "trims/color_palettes/iron",
        "gold": "trims/color_palettes/gold",
        "diamond": "trims/color_palettes/diamond",
        "netherite": "trims/color_palettes/netherite",
        "redstone": "trims/color_palettes/redstone",
        "copper": "trims/color_palettes/copper",
        "emerald": "trims/color_palettes/emerald",
        "lapis": "trims/color_palettes/lapis",
        "amethyst": "trims/color_palettes/amethyst"
      }
    }
  ]
}

- 
	- textures: A list of grayscale trim pattern textures that we want to generate permutations of with the colors defined below.
	- palette_key: The same trim palette key as vanilla. The grayscale color palette key to use when mapping the colors fromtexturesto the colors inpermutations.
	- permutations: The same color palettes as vanilla. A map of the trim material'sasset_name(see below) to its color palette.

For the full JSON format, see Resource_pack § Atlases

### Textures
The textures referenced in the atlas  textures field should be grayscale images, using the same colors as the texture in  palette_key. The textures for this example can be downloaded here:

- assets/example/trims/models/armor/stripes.png
- assets/example/trims/models/armor/stripes_leggings.png

## Custom trim materials
A smithing recipe showing a custom "Ender" trim material
This second example adds a new "Ender" material that works with all the vanilla armor types and colors.

### Trim material
Let's start with the trim_material.





Changes to this file won't be applied when running /reload[1]. Always leave and reopen the world to apply the new changes!


data/example/trim_material/ender.json
{
  "asset_name": "ender",
  "description": {
    "color": "#258474",
    "translate": "trim_material.example.ender"
  },
  "ingredient": "minecraft:ender_pearl",
  "item_model_index": 0.85
}

- The root object
	- asset_name: A string which will be used in the resource pack.
	- description: AJSON text componentused for the tooltip on items. The color#258474is used here.
	- ingredient: Theitemrepresenting this material.
	- item_model_index: A value between 0 and 1, used in theitem models(see below).
	- override_armor_materials: Optional. Map of armor material to override color palette.

### Item tag
The ender pearl needs to be added to the #minecraft:trim_materials item tag. This makes the material usable in the smithing recipes.

data/minecraft/tags/items/trim_materials.json
{
  "values": [
    "minecraft:ender_pearl"
  ]
}

### Translation
Moving on to the resource pack, the first step is to create the translation that we referenced in the trim material's  description field.

assets/example/lang/en_us.json
{
  "trim_material.example.ender": "Ender Material"
}

### Atlases
For trim materials, two atlas files need to be modified: one for the armor entity rendering and one for the inventory item models.

assets/minecraft/atlases/armor_trims.json
{
  "sources": [
    {
      "type": "paletted_permutations",
      "textures": [
        "trims/models/armor/coast",
        "trims/models/armor/coast_leggings",
        "trims/models/armor/sentry",
        "trims/models/armor/sentry_leggings",
        "trims/models/armor/dune",
        "trims/models/armor/dune_leggings",
        "trims/models/armor/wild",
        "trims/models/armor/wild_leggings",
        "trims/models/armor/ward",
        "trims/models/armor/ward_leggings",
        "trims/models/armor/eye",
        "trims/models/armor/eye_leggings",
        "trims/models/armor/vex",
        "trims/models/armor/vex_leggings",
        "trims/models/armor/tide",
        "trims/models/armor/tide_leggings",
        "trims/models/armor/snout",
        "trims/models/armor/snout_leggings",
        "trims/models/armor/rib",
        "trims/models/armor/rib_leggings",
        "trims/models/armor/spire",
        "trims/models/armor/spire_leggings"
      ],
      "palette_key": "trims/color_palettes/trim_palette",
      "permutations": {
        "ender": "example:trims/color_palettes/ender"
      }
    }
  ]
}

assets/minecraft/atlases/blocks.json
{
  "sources": [
    {
      "type": "paletted_permutations",
      "textures": [
        "trims/items/leggings_trim",
        "trims/items/chestplate_trim",
        "trims/items/helmet_trim",
        "trims/items/boots_trim"
      ],
      "palette_key": "trims/color_palettes/trim_palette",
      "permutations": {
        "ender": "example:trims/color_palettes/ender"
      }
    }
  ]
}

- 
	- textures: The same list of textures as vanilla.
	- palette_key: The same trim palette key as vanilla. The grayscale color palette key to use when mapping the colors fromtexturesto the colors inpermutations.
	- permutations: The custom materials that we want to add permutations for. The keyendershould match theasset_namefrom the data pack.

### Color palette texture
Scaled up color palette for the "ender" trim material
These atlas files reference a color palette texture which needs to be created. Since the vanilla palette key is used, the image has a width of 8 and a height of 1.

The textures for this example can be downloaded here:

- assets/example/textures/trims/color_palettes/ender.png

### Item models
The most time consuming step is to add the item model predicate to all the possible items. In this example it is only added for the iron chestplate.

assets/minecraft/models/item/iron_chestplate.json
{
  "parent": "minecraft:item/generated",
  "overrides": [
    {
      "model": "minecraft:item/iron_chestplate_quartz_trim",
      "predicate": {
        "trim_type": 0.1
      }
    },
    {
      "model": "minecraft:item/iron_chestplate_netherite_trim",
      "predicate": {
        "trim_type": 0.3
      }
    },
    {
      "model": "minecraft:item/iron_chestplate_redstone_trim",
      "predicate": {
        "trim_type": 0.4
      }
    },
    {
      "model": "minecraft:item/iron_chestplate_copper_trim",
      "predicate": {
        "trim_type": 0.5
      }
    },
    {
      "model": "minecraft:item/iron_chestplate_gold_trim",
      "predicate": {
        "trim_type": 0.6
      }
    },
    {
      "model": "minecraft:item/iron_chestplate_emerald_trim",
      "predicate": {
        "trim_type": 0.7
      }
    },
    {
      "model": "minecraft:item/iron_chestplate_diamond_trim",
      "predicate": {
        "trim_type": 0.8
      }
    },
    {
      "model": "example:item/iron_chestplate_ender_trim",
      "predicate": {
        "trim_type": 0.85
      }
    },
    {
      "model": "minecraft:item/iron_chestplate_lapis_trim",
      "predicate": {
        "trim_type": 0.9
      }
    },
    {
      "model": "minecraft:item/iron_chestplate_amethyst_trim",
      "predicate": {
        "trim_type": 1.0
      }
    }
  ],
  "textures": {
    "layer0": "minecraft:item/iron_chestplate"
  }
}

The majority of this file is the same as the vanilla iron_chestplate model, only the highlighted region is added. The order is important here!

This references another item model file, which needs to be created.

assets/example/models/item/iron_chestplate_ender_trim.json
{
  "parent": "minecraft:item/generated",
  "textures": {
    "layer0": "minecraft:item/iron_chestplate",
    "layer1": "minecraft:trims/items/chestplate_trim_ender"
  }
}

This item model references the trims/items/chestplate_trim_ender sprite that was generated in the blocks.json atlas.

Because the override for all the other armor types hasn't been added, they will default to the previous trim_type, in this case 0.8, which is diamond. To prevent this, the steps in this section need to be taken for each item in the #minecraft:trimmable_armor item tag.

## Custom trimmable items
A smithing recipe of an axe added as a trimmable item
This example adds the iron_axe as a trimmable item. Since this is not an armor item, we only need to worry about the item model. The trim pattern used will have no effect on the texture, only the trim material can be used in the model overrides.

### Item tag
The only change in the data pack is adding the item to the #minecraft:trimmable_armor item tag.

data/minecraft/tags/items/trimmable_armor.json
{
  "values": [
    "minecraft:iron_axe"
  ]
}

### Item models
Moving to the resource pack by customizing the iron axe item model. This step is similar to the items models when adding a custom material, but this time all overrides need to be added.

assets/minecraft/models/item/iron_axe.json
{
  "parent": "minecraft:item/handheld",
  "overrides": [
    {
      "model": "example:item/iron_axe_quartz_trim",
      "predicate": {
        "trim_type": 0.1
      }
    },
    {
      "model": "example:item/iron_axe_netherite_trim",
      "predicate": {
        "trim_type": 0.3
      }
    },
    {
      "model": "example:item/iron_axe_redstone_trim",
      "predicate": {
        "trim_type": 0.4
      }
    },
    {
      "model": "example:item/iron_axe_copper_trim",
      "predicate": {
        "trim_type": 0.5
      }
    },
    {
      "model": "example:item/iron_axe_gold_trim",
      "predicate": {
        "trim_type": 0.6
      }
    },
    {
      "model": "example:item/iron_axe_emerald_trim",
      "predicate": {
        "trim_type": 0.7
      }
    },
    {
      "model": "example:item/iron_axe_diamond_trim",
      "predicate": {
        "trim_type": 0.8
      }
    },
    {
      "model": "example:item/iron_axe_lapis_trim",
      "predicate": {
        "trim_type": 0.9
      }
    },
    {
      "model": "example:item/iron_axe_amethyst_trim",
      "predicate": {
        "trim_type": 1.0
      }
    }
  ],
  "textures": {
    "layer0": "minecraft:item/iron_axe"
  }
}

The above file references custom item models for each material.





The following file needs to be created for each of the 10 listed materials.


assets/example/models/item/iron_axe_amethyst_trim.json
{
  "parent": "minecraft:item/handheld",
  "textures": {
    "layer0": "minecraft:item/iron_axe",
    "layer1": "example:trims/items/axe_trim_amethyst"
  }
}

### Atlas
The above model files reference an axe_trim_amethyst texture. This texture does not exist, it needs to be generated by the paletted_permutations sprite source in the blocks.json atlas.

assets/minecraft/atlases/blocks.json
{
  "sources": [
    {
      "type": "paletted_permutations",
      "textures": [
        "example:trims/items/axe_trim"
      ],
      "palette_key": "trims/color_palettes/trim_palette",
      "permutations": {
        "quartz": "trims/color_palettes/quartz",
        "iron": "trims/color_palettes/iron",
        "gold": "trims/color_palettes/gold",
        "diamond": "trims/color_palettes/diamond",
        "netherite": "trims/color_palettes/netherite",
        "redstone": "trims/color_palettes/redstone",
        "copper": "trims/color_palettes/copper",
        "emerald": "trims/color_palettes/emerald",
        "lapis": "trims/color_palettes/lapis",
        "amethyst": "trims/color_palettes/amethyst"
      }
    }
  ]
}

### Mask texture
The atlas references the axe_trim texture, which is a mask for which pixels to color with the color palette.

The texture for this example can be downloaded here:

- assets/example/textures/trims/items/axe_trim.png

