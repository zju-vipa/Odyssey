# Light Weighted Pressure Plate
A light weighted pressure plate is a type of pressure plate that, like the heavy weighted pressure plate, outputs a variable redstone signal strength based on the number of entities present on the plate.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Chest loot
	- 1.3 Crafting
- 2 Usage
	- 2.1 Placement
	- 2.2 Redstone component
		- 2.2.1 Activation
	- 2.3 Behavior
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 Advancements
- 6 History
- 7 Issues
- 8 See also
- 9 References

## Obtaining
### Breaking
A light weighted pressure plate drops itself if a piston extends or pushes a block into its location, or if a block under the pressure plate is moved or destroyed.

| Block     | Light Weighted Pressure Plate |
|-----------|-------------------------------|
| Hardness  | 0.5                           |
| Tool      |                               |
|           | Breakingtime (sec)[A]         |
| Default   | 2.5                           |
| Wooden    | 0.4                           |
| Stone     | 0.2                           |
| Iron      | 0.15                          |
| Diamond   | 0.1                           |
| Netherite | 0.1                           |
| Golden    | 0.1                           |


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


### Chest loot
| Item                          | Structure     | Container | Quantity | Chance                         |
|-------------------------------|---------------|-----------|----------|--------------------------------|
|                               |               |           |          | Java EditionandBedrock Edition |
| Light Weighted Pressure Plate | Ruined Portal | Chest     | 1        | 7.3%                           |

### Crafting
| Ingredients | Crafting recipe |
|-------------|-----------------|
| Gold Ingot  |                 |

## Usage
| Signal strength | Entity count |
|-----------------|--------------|
| 0               | 0            |
| 1               | 1            |
| 2               | 2            |
| 3               | 3            |
| 4               | 4            |
| 5               | 5            |
| 6               | 6            |
| 7               | 7            |
| 8               | 8            |
| 9               | 9            |
| 10              | 10           |
| 11              | 11           |
| 12              | 12           |
| 13              | 13           |
| 14              | 14           |
| 15              | 15+          |

### Placement
Main article: Pressure Plate § Placement
A light weighted pressure plate can only be placed on the top of other blocks with either a full solid block face, a solid center, or a solid rim.

### Redstone component
See also: Redstone circuit

A light weighted pressure plate detects all entities on top of it, outputting a redstone signal strength of 1 for every entity present, up to the maximum of 15 signal strength with 15 or more entities.

#### Activation
Main article: Pressure Plate § Activation
While active, a light weighted pressure plate weakly powers itself, and strongly powers the block it is placed on.

The power level output varies depending on the number of entities colliding with the pressure plate.

The signal strength from a weighted pressure plate does not vary with the type of entity. 15 mobs will produce the same signal strength as 15 different items. Note the light weighted presser plate counts entities, not quantity of items, generally leading to one entity count per stack of items. For more information see  item entity behavior.

### Behavior
A light weighted pressure plate is a non-solid block, allowing entities to freely pass through it.

The visual height of a pressure plate is 1⁄16 of a block when inactive and 1⁄32 of a block when active.

Fluids flow around a light weighted pressure plate without affecting it.

## Data values
### ID
Java Edition:

| Name                          | Identifier                    | Form         | Block tags                        | Translation key                               |
|-------------------------------|-------------------------------|--------------|-----------------------------------|-----------------------------------------------|
| Light Weighted Pressure Plate | Light_weighted_pressure_plate | Block & Item | pressure_plateswall_post_override | block.minecraft.Light_weighted_pressure_plate |

Bedrock Edition:

| Name                          | Identifier                    | Numeric ID | Form                       | Item ID[i 1]   | Translation key                         |
|-------------------------------|-------------------------------|------------|----------------------------|----------------|-----------------------------------------|
| Light Weighted Pressure Plate | Light_weighted_pressure_plate | 148        | Block & Giveable Item[i 2] | Identical[i 3] | tile.Light_weighted_pressure_plate.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


### Block states
Main article: Pressure Plate § Block states
## See also
Heavy Weighted Pressure Plate


