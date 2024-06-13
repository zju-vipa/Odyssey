# Heavy Weighted Pressure Plate
A heavy weighted pressure plate is a type of pressure plate that, like the light weighted pressure plate, outputs a variable redstone signal strength based on the number of entities present on the plate.

A heavy weighted pressure plate outputs one redstone signal strength for every 10 entities present.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Crafting
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
- 5 History
- 6 Issues
- 7 References

## Obtaining
### Breaking
A heavy weighted pressure plate drops itself if a piston extends or pushes a block into its location, or if a block under the pressure plate is moved or destroyed.

| Block     | Heavy Weighted Pressure Plate |
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

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Crafting
| Ingredients | Crafting recipe |
|-------------|-----------------|
| Iron Ingot  |                 |

## Usage
| Signal strength | Entity count |
|-----------------|--------------|
| 0               | 0            |
| 1               | 1–10         |
| 2               | 11–20        |
| 3               | 21–30        |
| 4               | 31–40        |
| 5               | 41–50        |
| 6               | 51–60        |
| 7               | 61–70        |
| 8               | 71–80        |
| 9               | 81–90        |
| 10              | 91–100       |
| 11              | 101–110      |
| 12              | 111–120      |
| 13              | 121–130      |
| 14              | 131–140      |
| 15              | 141+         |

### Placement
Main article: Pressure Plate § Placement
A heavy weighted pressure plate can only be placed on the top of other blocks with either a full solid block face, a solid center, or a solid rim.

### Redstone component
See also: Redstone circuit

A heavy weighted pressure plate detects all entities on top of it, outputting a redstone signal strength of 1 for every 10 entities present, starting at 1.

#### Activation
Main article: Pressure Plate § Activation
While active, a heavy weighted pressure plate weakly powers itself, and strongly powers the block it is placed on.

The power level output varies depending on the number of entities colliding with the pressure plate.

The signal strength from a weighted pressure plate does not vary with the type of entity. 15 mobs will produce the same signal strength as 15 different items. Note the heavy weighted presser plate counts entities, not quantity of items, generally leading to one entity count per stack of items. For more information see  item entity behavior.

### Behavior
A heavy weighted pressure plate is a non-solid block, allowing entities to freely pass through it.

The visual height of a pressure plate is 1⁄16 of a block when inactive and 1⁄32 of a block when active.

Fluids flow around a heavy weighted pressure plate without affecting it.

## Data values
### ID
Java Edition:

| Name                          | Identifier                      | Form         | Block tags                                 | Translation key                                 |
|-------------------------------|---------------------------------|--------------|--------------------------------------------|-------------------------------------------------|
| Heavy Weighted Pressure Plate | `heavy_weighted_pressure_plate` | Block & Item | `pressure_plates`<br/>`wall_post_override` | `block.minecraft.heavy_weighted_pressure_plate` |

Bedrock Edition:

| Name                          | Identifier                      | Numeric ID | Form                       | Item ID[i 1]   | Translation key                           |
|-------------------------------|---------------------------------|------------|----------------------------|----------------|-------------------------------------------|
| Heavy Weighted Pressure Plate | `heavy_weighted_pressure_plate` | `148`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.heavy_weighted_pressure_plate.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
Main article: Pressure Plate § Block states

