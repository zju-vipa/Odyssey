### Armor trimming
It is possible to upgrade armor with trims. This requires a smithing template, a pair of boots, and an ingot or crystal (iron ingot, copper ingot, gold ingot, netherite ingot, emerald, redstone dust, lapis lazuli, amethyst shard, nether quartz, or diamond).

These trims have no effect on the gameplay or strength of the armor. 

| Ingredients                                  | Smithing recipe |
|----------------------------------------------|-----------------|
| Any Armor Trim +Any Boots +Any Ingot/Crystal | Upgrade Gear    |

### Smelting usage
| Name                          | Ingredients                                                      | Smelting recipe |
|-------------------------------|------------------------------------------------------------------|-----------------|
| Iron Nuggetor<br/>Gold Nugget | Iron Bootsor<br/>Chainmail Bootsor<br/>Golden Boots+<br/>Anyfuel | 0.1             |

### Piglins
Piglins are attracted to golden boots and pick them up, examining them for 6 to 8 seconds. Other boots do not attract piglins but can be worn by them. They prefer stronger boots over weaker boots, with one major exception: They always prefer golden boots over all other boots, throwing out stronger boots to equip them. Enchanted boots are preferred over unenchanted boots.

### Powder snow
Leather boots can be used to safely cross powder snow without sinking in it. The block behaves similar to scaffolding, allowing the player to sink in by pressing crouch and move up by pressing jump. The boots also prevent the wearer from taking freezing damage.

## Data values
### ID
Java Edition:

| Name            | Identifier        | Form | Item tags                 | Translation key                  |
|-----------------|-------------------|------|---------------------------|----------------------------------|
| Leather Boots   | `leather_boots`   | Item | `freeze_immune_wearables` | `item.minecraft.leather_boots`   |
| Chainmail Boots | `chainmail_boots` | Item | None                      | `item.minecraft.chainmail_boots` |
| Iron Boots      | `iron_boots`      | Item | None                      | `item.minecraft.iron_boots`      |
| Diamond Boots   | `diamond_boots`   | Item | None                      | `item.minecraft.diamond_boots`   |
| Golden Boots    | `golden_boots`    | Item | None                      | `item.minecraft.golden_boots`    |
| Netherite Boots | `netherite_boots` | Item | None                      | `item.minecraft.netherite_boots` |

Bedrock Edition:

| Name            | Identifier        | Numeric ID | Form | Translation key             |
|-----------------|-------------------|------------|------|-----------------------------|
| Leather Boots   | `leather_boots`   | `338`      | Item | `item.leather_boots.name`   |
| Chainmail Boots | `chainmail_boots` | `342`      | Item | `item.chainmail_boots.name` |
| Iron Boots      | `iron_boots`      | `346`      | Item | `item.iron_boots.name`      |
| Diamond Boots   | `diamond_boots`   | `350`      | Item | `item.diamond_boots.name`   |
| Golden Boots    | `golden_boots`    | `354`      | Item | `item.golden_boots.name`    |
| Netherite Boots | `netherite_boots` | `612`      | Item | `item.netherite_boots.name` |

### Item data
When leather boots are dyed, it has the following NBT:

- tag: Parent tag.
	- display: Display properties.
		- color: The color of the leather armor. The tooltip displays "Dyed" if advanced tooltips are disabled, otherwise it displays the hexadecimal color value. Color codes are calculated from the Red, Green and Blue components using this formula:Red<<16 + Green<<8 + Blue[1]


