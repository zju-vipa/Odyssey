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


