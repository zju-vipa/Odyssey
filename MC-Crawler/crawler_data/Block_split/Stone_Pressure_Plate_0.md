# Stone Pressure Plate
A stone pressure plate is a stone variant of the pressure plate that can detect only players and mobs.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
- 2 Usage
	- 2.1 Crafting ingredient
	- 2.2 Placement
	- 2.3 Redstone component
		- 2.3.1 Activation
	- 2.4 Behavior
	- 2.5 Note blocks
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
A stone pressure plate can be obtained only by using a pickaxe.

| Block     | Stone Pressure Plate  |
|-----------|-----------------------|
| Hardness  | 0.5                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 2.5                   |
| Wooden    | 0.4                   |
| Stone     | 0.2                   |
| Iron      | 0.15                  |
| Diamond   | 0.1                   |
| Netherite | 0.1                   |
| Golden    | 0.1                   |


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


### Natural generation
One stone pressure plate is generated naturally in each desert pyramid. Stone pressure plate also generate as part of ancient cities.

### Crafting
| Ingredients | Crafting recipe |
|-------------|-----------------|
| Stone       |                 |

## Usage
See also: Pressure Plate § Usage

A stone pressure plate has equivalent functionality as a polished blackstone pressure plate, except for the additional functionality as a crafting ingredient.

### Crafting ingredient
| Name          | Ingredients                                   | Crafting recipe |
|---------------|-----------------------------------------------|-----------------|
| Detector Rail | Iron Ingot+Stone Pressure Plate+Redstone Dust | 6               |

### Placement
Main article: Pressure Plate § Placement
A stone pressure plate can only be placed on the top of other blocks with either a full solid block face, a solid center, or a solid rim.

### Redstone component
See also: Redstone circuit

A stone pressure plate can be used to detect entities on top of it (players, mobs, items, etc.).

#### Activation
Main article: Pressure Plate § Activation
A stone pressure plate is activated only by mobs, players and armor stands, unlike wooden pressure plates.

Once activated, a pressure plate checks if entities are still present at regular intervals. Stone pressure plates check every 10 redstone ticks, starting 10 redstone ticks after activation, so they deactivate up to 10 redstone ticks (20 game ticks or 1 second, barring lag) after no entities are on top of them.

Stone pressure plates are activated by minecarts only if the minecart contains a mob or player.

### Behavior
For stone pressure plates, the power level is always 15. 

### Note blocks
Stone pressure plates can be placed under note blocks to produce "bass drum" sounds.

## Data values
### ID
Java Edition:

| Name                 | Identifier           | Form         | Block tags                                             | Item tags | Translation key                      |
|----------------------|----------------------|--------------|--------------------------------------------------------|-----------|--------------------------------------|
| Stone Pressure Plate | stone_pressure_plate | Block & Item | pressure_platesstone_pressure_plateswall_post_override | None      | block.minecraft.stone_pressure_plate |

Bedrock Edition:

| Name                 | Identifier           | Numeric ID | Form                       | Item ID[i 1]   | Translation key                |
|----------------------|----------------------|------------|----------------------------|----------------|--------------------------------|
| Stone Pressure Plate | stone_pressure_plate | 70         | Block & Giveable Item[i 2] | Identical[i 3] | tile.stone_pressure_plate.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


### Block states
See also: Block states

Java Edition:

Stone and wooden pressure plates
| Name    | Default value | Allowed values | Description                                           |
|---------|---------------|----------------|-------------------------------------------------------|
| powered | false         | falsetrue      | True if pressure plate is depressed, providing power. |

Weighted pressure plates
| Name  | Default value | Allowed values         | Description                                                                                 |
|-------|---------------|------------------------|---------------------------------------------------------------------------------------------|
| power | 0             | 0123456789101112131415 | Specifies the redstone power level currently being produced by the weighted pressure plate. |

Bedrock Edition:

Stone and wooden pressure plates
| Name            | Metadata Bits | Default value | Allowed values       | Values forMetadata Bits | Description                                      |
|-----------------|---------------|---------------|----------------------|-------------------------|--------------------------------------------------|
| redstone_signal | 0x1           | 0             | 01                   | 01                      | Specifies whether the pressure plate is pressed. |
|                 |               |               | 23456789101112131415 | Unsupported             | Unused                                           |

Weighted pressure plates
| Name            | Metadata Bits | Default value | Allowed values         | Values forMetadata Bits | Description                                                                        |
|-----------------|---------------|---------------|------------------------|-------------------------|------------------------------------------------------------------------------------|
| redstone_signal | 0x10x20x40x8  | 0             | 0123456789101112131415 | 0123456789101112131415  | Specifies the redstone power level currently being produced by the pressure plate. |


