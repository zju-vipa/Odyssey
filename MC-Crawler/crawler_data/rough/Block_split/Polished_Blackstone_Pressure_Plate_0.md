# Polished Blackstone Pressure Plate
A polished blackstone pressure plate is a polished blackstone variant of the pressure plate that can detect only players and mobs.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Crafting
- 2 Usage
	- 2.1 Placement
	- 2.2 Redstone component
		- 2.2.1 Activation
	- 2.3 Behavior
	- 2.4 Note blocks
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Trivia
- 7 Issues
- 8 References

## Obtaining
### Breaking
A polished blackstone pressure plate can be obtained only by using a pickaxe.

| Block     | Polished Blackstone Pressure Plate |
|-----------|------------------------------------|
| Hardness  | 0.5                                |
| Tool      |                                    |
|           | Breakingtime (sec)[A]              |
| Default   | 2.5                                |
| Wooden    | 0.4                                |
| Stone     | 0.2                                |
| Iron      | 0.15                               |
| Diamond   | 0.1                                |
| Netherite | 0.1                                |
| Golden    | 0.1                                |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Crafting
| Ingredients         | Crafting recipe |
|---------------------|-----------------|
| Polished Blackstone |                 |

## Usage
See also: Pressure Plate § Usage

A polished blackstone pressure plate has equivalent functionality as a stone pressure plate, except for the lack of functionality as a crafting ingredient.

### Placement
Main article: Pressure Plate § Placement
A polished blackstone pressure plate can only be placed on the top of other blocks with either a full solid block face, a solid center, or a solid rim.

### Redstone component
See also: Redstone circuit

A polished blackstone pressure plate can be used to detect entities on top of it (mobs, players and armor stands).

#### Activation
Main article: Pressure Plate § Activation
A polished blackstone pressure plate is activated only by mobs, players and armor stands, unlike wooden pressure plates.

Once activated, a pressure plate checks if entities are still present at regular intervals. Polished blackstone pressure plates check every 10 redstone ticks, starting 10 redstone ticks after activation, so they deactivate up to 10 redstone ticks (20 game ticks or 1 second, barring lag) after no entities are on top of them.

Polished blackstone pressure plates are activated by minecarts only if the minecart contains a mob or player.

### Behavior
For polished blackstone pressure plates, the power level is always 15. 

### Note blocks
Polished blackstone pressure plates can be placed under note blocks to produce "bass drum" sounds.

## Data values
### ID
Java Edition:

| Name                               | Identifier                           | Form         | Block tags                                                             | Item tags | Translation key                                      |
|------------------------------------|--------------------------------------|--------------|------------------------------------------------------------------------|-----------|------------------------------------------------------|
| Polished Blackstone Pressure Plate | `polished_blackstone_pressure_plate` | Block & Item | `pressure_plates`<br/>`stone_pressure_plates`<br/>`wall_post_override` | None      | `block.minecraft.polished_blackstone_pressure_plate` |

Bedrock Edition:

| Name                               | Identifier                           | Numeric ID | Form                       | Item ID[i 1]   | Translation key                                |
|------------------------------------|--------------------------------------|------------|----------------------------|----------------|------------------------------------------------|
| Polished Blackstone Pressure Plate | `polished_blackstone_pressure_plate` | `550`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.polished_blackstone_pressure_plate.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

Java Edition:

** Stone and wooden pressure plates **
| Name    | Default value | Allowed values     | Description                                           |
|---------|---------------|--------------------|-------------------------------------------------------|
| powered | `false`       | `false`<br/>`true` | True if pressure plate is depressed, providing power. |

** Weighted pressure plates **
| Name  | Default value | Allowed values                                                                                                                    | Description                                                                                 |
|-------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| power | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | Specifies the redstone power level currently being produced by the weighted pressure plate. |

Bedrock Edition:

** Stone and wooden pressure plates **
| Name            | Metadata Bits | Default value | Allowed values                                                                                                    | Values forMetadata Bits | Description                                      |
|-----------------|---------------|---------------|-------------------------------------------------------------------------------------------------------------------|-------------------------|--------------------------------------------------|
| redstone_signal | `0x1`         | `0`           | `0`<br/>`1`                                                                                                       | `0`<br/>`1`             | Specifies whether the pressure plate is pressed. |
|                 |               |               | `2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | `Unsupported`           | Unused                                           |

** Weighted pressure plates **
| Name            | Metadata Bits                       | Default value | Allowed values                                                                                                                    | Values forMetadata Bits                                                                                                           | Description                                                                        |
|-----------------|-------------------------------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| redstone_signal | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | Specifies the redstone power level currently being produced by the pressure plate. |


