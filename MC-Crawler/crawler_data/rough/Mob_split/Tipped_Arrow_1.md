#### No-effect tipped arrows
In Java Edition, it is possible to craft tipped arrows using lingering water bottles as well as Awkward, Thick, and Mundane lingering potions. If crafted with a water bottle, the arrow is called an arrow of Splashing. If crafted with Mundane, Awkward, or Thick potions, it is called a tipped arrow.[2] Tipped arrows crafted from different potions do not stack, as resultant tipped arrows all have different potion tags.

In Bedrock Edition, all four kinds as well as the long mundane tipped arrow aren't obtainable either in Creative, by cauldrons, by crafting, or by commands.

All four kinds generate blue particles in flight and upon landing, but otherwise behave like regular arrows. In particular, arrow of Splashing has no effect on fire and campfires and when shot from a bow with the Flame enchantment, can light candles, campfires and TNT just like regular arrows on fire. 

| Icon | Name               |
|------|--------------------|
|      | Arrow of Splashing |
|      | Tipped Arrow       |

#### Uncraftable tipped arrows
In Java Edition, the uncraftable tipped arrow is a tipped arrow with no effect that is unobtainable in regular gameplay. It is available in two variants that don't stack together:

- /give @s minecraft:tipped_arrow{Potion:"minecraft:empty"}- arrow assigned an effect placeholder "empty"
- /give @s minecraft:tipped_arrow- arrow not assigned any effect.

The uncraftable arrow doesn't differ from regular arrows in behavior when used as a projectile.

| Icon | Name                     |
|------|--------------------------|
|      | Uncraftable Tipped Arrow |

## Data values
### ID
Java Edition:

| Name         | Identifier     | Form | Item tags | Translation key                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|--------------|----------------|------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Tipped Arrow | `tipped_arrow` | Item | `arrows`  | `item.minecraft.tipped_arrow`<br/>`item.minecraft.tipped_arrow.effect.empty`<br/>`item.minecraft.tipped_arrow.effect.water`<br/>`item.minecraft.tipped_arrow.effect.mundane`<br/>`item.minecraft.tipped_arrow.effect.thick`<br/>`item.minecraft.tipped_arrow.effect.awkward`<br/>`item.minecraft.tipped_arrow.effect.night_vision`<br/>`item.minecraft.tipped_arrow.effect.invisibility`<br/>`item.minecraft.tipped_arrow.effect.leaping`<br/>`item.minecraft.tipped_arrow.effect.fire_resistance`<br/>`item.minecraft.tipped_arrow.effect.swiftness`<br/>`item.minecraft.tipped_arrow.effect.slowness`<br/>`item.minecraft.tipped_arrow.effect.water_breathing`<br/>`item.minecraft.tipped_arrow.effect.healing`<br/>`item.minecraft.tipped_arrow.effect.harming`<br/>`item.minecraft.tipped_arrow.effect.poison`<br/>`item.minecraft.tipped_arrow.effect.regeneration`<br/>`item.minecraft.tipped_arrow.effect.strength`<br/>`item.minecraft.tipped_arrow.effect.weakness`<br/>`item.minecraft.tipped_arrow.effect.levitation`<br/>`item.minecraft.tipped_arrow.effect.luck`<br/>`item.minecraft.tipped_arrow.effect.turtle_master`<br/>`item.minecraft.tipped_arrow.effect.slow_falling` |

| Name  | Identifier | Entity tags                       | Translation key          |
|-------|------------|-----------------------------------|--------------------------|
| Arrow | `arrow`    | `arrows`<br/>`impact_projectiles` | `entity.minecraft.arrow` |

Bedrock Edition:

| Name         | Identifier | Numeric ID | Form | Item tags         | Translation key                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|--------------|------------|------------|------|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Tipped Arrow | `arrow`    | `301`      | Item | `minecraft:arrow` | `item.tipped_arrow.name`<br/>`tipped_arrow.effect.water`<br/>`tipped_arrow.effect.mundane`<br/>`tipped_arrow.effect.thick`<br/>`tipped_arrow.effect.awkward`<br/>`tipped_arrow.effect.nightVision`<br/>`tipped_arrow.effect.invisibility`<br/>`tipped_arrow.effect.jump`<br/>`tipped_arrow.effect.fireResistance`<br/>`tipped_arrow.effect.moveSpeed`<br/>`tipped_arrow.effect.moveSlowdown`<br/>`tipped_arrow.effect.waterBreathing`<br/>`tipped_arrow.effect.heal`<br/>`tipped_arrow.effect.harm`<br/>`tipped_arrow.effect.poison`<br/>`tipped_arrow.effect.regeneration`<br/>`tipped_arrow.effect.damageBoost`<br/>`tipped_arrow.effect.weakness`<br/>`tipped_arrow.effect.wither`<br/>`tipped_arrow.effect.turtleMaster`<br/>`tipped_arrow.effect.slowFalling` |

| Name  | Identifier | Numeric ID | Translation key     |
|-------|------------|------------|---------------------|
| Arrow | `arrow`    | `80`       | `entity.arrow.name` |

### Metadata
In Bedrock Edition, arrows use the following item data values:

| Arrow                      | Regular | Extended | Enhanced(Level II) |
|----------------------------|---------|----------|--------------------|
| Arrow                      | 0       | N/A      | N/A                |
| Arrow of Splashing         | 1       | N/A      | N/A                |
| Tipped Arrow (Mundane)     | 2       | 3        | N/A                |
| Tipped Arrow (Thick)       | 4       | N/A      | N/A                |
| Tipped Arrow (Awkward)     | 5       | N/A      | N/A                |
| Arrow of Night Vision      | 6       | 7        | N/A                |
| Arrow of Invisibility      | 8       | 9        | N/A                |
| Arrow of Leaping           | 10      | 11       | 12                 |
| Arrow of Fire Resistance   | 13      | 14       | N/A                |
| Arrow of Swiftness         | 15      | 16       | 17                 |
| Arrow of Slowness          | 18      | 19       | 43                 |
| Arrow of Water Breathing   | 20      | 21       | N/A                |
| Arrow of Healing           | 22      | N/A      | 23                 |
| Arrow of Harming           | 24      | N/A      | 25                 |
| Arrow of Poison            | 26      | 27       | 28                 |
| Arrow of Regeneration      | 29      | 30       | 31                 |
| Arrow of Strength          | 32      | 33       | 34                 |
| Arrow of Weakness          | 35      | 36       | N/A                |
| Arrow of Decay             | 37      | N/A      | N/A                |
| Arrow of the Turtle Master | 38      | 39       | 40                 |
| Arrow of Slow Falling      | 41      | 42       | N/A                |

### Entity data
Tipped arrows have entity data that define various properties of the entity.

Java Edition:

Main article: Entity format
- Entity data
	- 
	- Tags common to all arrows
	- 
	- Tags common to all entities
	- 
	- Tags common to all projectiles
	- Note: An arrow entity is a tipped arrow if it has either thePotionorCustomPotionEffectstag.
	- 
	- Tags common to all potion effects
	- Color: Used by the arrow entity, for displaying the custom potion color of a fired arrow item that had aCustomPotionColortag.  The numeric color code are calculated from the Red, Green and Blue components using this formula:Red<<16 + Green<<8 + Blue. For positive values larger than 0x00FFFFFF, the top byte is ignored. All negative values remove the particles.

Bedrock Edition:

SeeBedrock Edition level format/Entity format.

