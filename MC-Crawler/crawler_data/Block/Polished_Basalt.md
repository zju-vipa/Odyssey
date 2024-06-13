# Polished Basalt
Polished basalt is the polished version of basalt and can be found as part of ancient cities and bastion remnants.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
	- 1.4 Stonecutting
- 2 Usage
	- 2.1 Note blocks
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 References

## Obtaining
### Breaking
Polished basalt drops as an item if mined by any pickaxe. If mined by any other tool, it drops nothing.

| Block     | Polished Basalt       |
|-----------|-----------------------|
| Hardness  | 1.25                  |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 6.25                  |
| Wooden    | 0.95                  |
| Stone     | 0.5                   |
| Iron      | 0.35                  |
| Diamond   | 0.25                  |
| Netherite | 0.25                  |
| Golden    | 0.2                   |


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


### Natural generation
Polished basalt can be found naturally as part of bastion remnants and ancient cities.

### Crafting
| Name            | Ingredients | Crafting recipe |
|-----------------|-------------|-----------------|
| Polished Basalt | Basalt      | 4               |

### Stonecutting
| Name            | Ingredients | Cutting recipe |
|-----------------|-------------|----------------|
| Polished Basalt | Basalt      |                |

## Usage
Polished basalt points perpendicular to whatever block face they are placed on.

### Note blocks
Polished basalt can be placed under note blocks to produce "bass drum" sound.

## Data values
### ID
Java Edition:

| Name            | Identifier      | Form         | Block tags       | Translation key                 |
|-----------------|-----------------|--------------|------------------|---------------------------------|
| Polished Basalt | polished_basalt | Block & Item | mineable/pickaxe | block.minecraft.polished_basalt |

Bedrock Edition:

| Name            | Identifier      | Numeric ID | Form                       | Item ID[i 1]   | Translation key           |
|-----------------|-----------------|------------|----------------------------|----------------|---------------------------|
| Polished Basalt | polished_basalt | 490        | Block & Giveable Item[i 2] | Identical[i 3] | tile.polished_basalt.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


### Block states
See also: Block states

Java Edition:

| Name | Default value | Allowed values | Description                         |
|------|---------------|----------------|-------------------------------------|
| axis | y             | x              | The basalt is oriented east–west.   |
|      |               | y              | The basalt is oriented vertically.  |
|      |               | z              | The basalt is oriented north–south. |

Bedrock Edition:

| Name        | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                         |
|-------------|---------------|---------------|----------------|-------------------------|-------------------------------------|
| pillar_axis | 0x10x2        | y             | x              | 1                       | The basalt is oriented east–west.   |
|             |               |               | y              | 0                       | The basalt is oriented vertically.  |
|             |               |               | z              | 2                       | The basalt is oriented north–south. |



