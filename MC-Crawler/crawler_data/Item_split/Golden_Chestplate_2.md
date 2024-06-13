### Armor trimming
It is possible to upgrade armor with trims. This requires a smithing template, a chestplate, and an ingot or crystal (iron ingot, copper ingot, gold ingot, netherite ingot, emerald, redstone dust, lapis lazuli, amethyst shard, nether quartz, or diamond).

These trims have no effect on the gameplay or strength of the armor. 

| Ingredients                                       | Smithing recipe |
|---------------------------------------------------|-----------------|
| Any Armor Trim +Any Chestplate +Any Ingot/Crystal | Upgrade Gear    |

### Smelting usage
| Name                     | Ingredients                                                      | Smelting recipe |
|--------------------------|------------------------------------------------------------------|-----------------|
| Iron NuggetorGold Nugget | Iron ChestplateorChainmail ChestplateorGolden Chestplate+Anyfuel | 0.1             |

### Piglins
Piglins are attracted to golden chestplates and pick them up, examining them for 6 to 8 seconds. Piglins can wear other chestplates but are not attracted to them. They prefer stronger chestplates over weaker chestplates, with one exception: They always prefer golden chestplates over all other chestplates, throwing out stronger chestplates to equip them. Enchanted chestplates are preferred over unenchanted chestplates.

## Data values
### ID
Java Edition:

| Name                 | Identifier           | Form | Item tags               | Translation key                     |
|----------------------|----------------------|------|-------------------------|-------------------------------------|
| Leather Tunic        | leather_chestplate   | Item | freeze_immune_wearables | item.minecraft.leather_chestplate   |
| Chainmail Chestplate | chainmail_chestplate | Item | None                    | item.minecraft.chainmail_chestplate |
| Iron Chestplate      | iron_chestplate      | Item | None                    | item.minecraft.iron_chestplate      |
| Diamond Chestplate   | diamond_chestplate   | Item | None                    | item.minecraft.diamond_chestplate   |
| Golden Chestplate    | golden_chestplate    | Item | None                    | item.minecraft.golden_chestplate    |
| Netherite Chestplate | netherite_chestplate | Item | None                    | item.minecraft.netherite_chestplate |

Bedrock Edition:

| Name                 | Identifier           | Numeric ID | Form | Translation key                |
|----------------------|----------------------|------------|------|--------------------------------|
| Leather Tunic        | leather_chestplate   | 336        | Item | item.leather_chestplate.name   |
| Chainmail Chestplate | chainmail_chestplate | 340        | Item | item.chainmail_chestplate.name |
| Iron Chestplate      | iron_chestplate      | 344        | Item | item.iron_chestplate.name      |
| Diamond Chestplate   | diamond_chestplate   | 348        | Item | item.diamond_chestplate.name   |
| Golden Chestplate    | golden_chestplate    | 352        | Item | item.golden_chestplate.name    |
| Netherite Chestplate | netherite_chestplate | 610        | Item | item.netherite_chestplate.name |

### Item data
When leather tunics are dyed, it has the following NBT:


 tag: Parent tag.
 display: Display properties.
 color: The color of the leather armor. The tooltip displays "Dyed" if advanced tooltips are disabled, otherwise it displays the hexadecimal color value. Color codes are calculated from the Red, Green and Blue components using this formula:Red<<16 + Green<<8 + Blue[2]


