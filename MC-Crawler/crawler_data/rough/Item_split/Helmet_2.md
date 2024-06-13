### Armor trimming
It is possible to upgrade armor with trims. This requires a smithing template, a helmet, and an ingot or crystal (iron ingot, copper ingot, gold ingot, netherite ingot, emerald, redstone dust, lapis lazuli, amethyst shard, nether quartz, or diamond).

These trims have no effect on the gameplay or strength of the armor. 

| Ingredients                                   | Smithing recipe |
|-----------------------------------------------|-----------------|
| Any Armor Trim +Any Helmet +Any Ingot/Crystal | Upgrade Gear    |

### Smelting usage
| Name                          | Ingredients                                                         | Smelting recipe |
|-------------------------------|---------------------------------------------------------------------|-----------------|
| Iron Nuggetor<br/>Gold Nugget | Iron Helmetor<br/>Chainmail Helmetor<br/>Golden Helmet+<br/>Anyfuel | 0.1             |

### Piglins
Piglins are attracted to golden helmets and pick them up, examining them for 6 to 8 seconds. Piglins can wear other helmets but are not attracted to them. They prefer stronger helmets over weaker helmets, with one exception: They always prefer golden helmets, throwing out stronger helmets in favor of gold helmets. Enchanted helmets are preferred over unenchanted helmets.

## Data values
### ID
Java Edition:

| Name             | Identifier         | Form | Item tags                 | Translation key                   |
|------------------|--------------------|------|---------------------------|-----------------------------------|
| Leather Cap      | `leather_helmet`   | Item | `freeze_immune_wearables` | `item.minecraft.leather_helmet`   |
| Chainmail Helmet | `chainmail_helmet` | Item | None                      | `item.minecraft.chainmail_helmet` |
| Iron Helmet      | `iron_helmet`      | Item | None                      | `item.minecraft.iron_helmet`      |
| Diamond Helmet   | `diamond_helmet`   | Item | None                      | `item.minecraft.diamond_helmet`   |
| Golden Helmet    | `golden_helmet`    | Item | None                      | `item.minecraft.golden_helmet`    |
| Netherite Helmet | `netherite_helmet` | Item | None                      | `item.minecraft.netherite_helmet` |

Bedrock Edition:

| Name             | Identifier         | Numeric ID | Form | Translation key              |
|------------------|--------------------|------------|------|------------------------------|
| Leather Cap      | `leather_helmet`   | `335`      | Item | `item.leather_helmet.name`   |
| Chainmail Helmet | `chainmail_helmet` | `339`      | Item | `item.chainmail_helmet.name` |
| Iron Helmet      | `iron_helmet`      | `343`      | Item | `item.iron_helmet.name`      |
| Diamond Helmet   | `diamond_helmet`   | `347`      | Item | `item.diamond_helmet.name`   |
| Golden Helmet    | `golden_helmet`    | `351`      | Item | `item.golden_helmet.name`    |
| Netherite Helmet | `netherite_helmet` | `609`      | Item | `item.netherite_helmet.name` |

### Item data
When leather caps are dyed, it has the following NBT:

- tag: Parent tag.
	- display: Display properties.
		- color: The color of the leather armor. The tooltip displays "Dyed" if advanced tooltips are disabled, otherwise it displays the hexadecimal color value. Color codes are calculated from the Red, Green and Blue components using this formula:Red<<16 + Green<<8 + Blue[1]


