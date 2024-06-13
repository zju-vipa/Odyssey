#### Redstone circuits
An arrow can activate a wooden button, wooden pressure plate, a tripwire, or a target. An arrow continues to power these blocks until it is removed, either due to despawning, or being picked up. Target blocks emit a redstone pulse for one second, as opposed to the static depressed state of the other switches. Non-wooden switches are not affected by arrows.

## Data values
### ID
Java Edition:

| Name  | Identifier | Form | Item tags | Translation key        |
|-------|------------|------|-----------|------------------------|
| Arrow | `arrow`    | Item | `arrows`  | `item.minecraft.arrow` |

| Name  | Identifier | Entity tags                       | Translation key          |
|-------|------------|-----------------------------------|--------------------------|
| Arrow | `arrow`    | `arrows`<br/>`impact_projectiles` | `entity.minecraft.arrow` |

Bedrock Edition:

| Name  | Identifier | Numeric ID | Form | Item tags         | Translation key   |
|-------|------------|------------|------|-------------------|-------------------|
| Arrow | `arrow`    | `301`      | Item | `minecraft:arrow` | `item.arrow.name` |

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
#### Normal and tipped arrows
Arrows have entity data that define various properties of the entity.

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

