# Quartz Pillar
A quartz pillar (in Java Edition) or pillar quartz block (in Bedrock Edition) is a variant of the block of quartz, obtained through crafting.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Crafting
	- 1.3 Stonecutting
	- 1.4 Trading
- 2 Usage
	- 2.1 Crafting ingredient
	- 2.2 Note Blocks
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 Gallery
	- 7.1 Screenshots
- 8 References

## Obtaining
### Breaking
Quartz pillars can be mined using any pickaxe. If mined without a pickaxe, it drops nothing.

| Block     | Quartz Pillar         |
|-----------|-----------------------|
| Hardness  | 0.8                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 4                     |
| Wooden    | 0.6                   |
| Stone     | 0.3                   |
| Iron      | 0.2                   |
| Diamond   | 0.15                  |
| Netherite | 0.15                  |
| Golden    | 0.1                   |


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


### Crafting
| Ingredients     | Crafting recipe |
|-----------------|-----------------|
| Block of Quartz | 2               |

### Stonecutting
| Ingredients     | Cutting recipe |
|-----------------|----------------|
| Block of Quartz |                |

### Trading
Master-level mason villagers sell a quartz pillar for an emerald.

## Usage
Quartz pillars can be rotated sideways.

### Crafting ingredient
| Name          | Ingredients   | Crafting recipe | Description           |
|---------------|---------------|-----------------|-----------------------|
| Quartz Slab   | Quartz Pillar | 6               | ‌[Java Edition  only] |
| Quartz Stairs | Quartz Pillar | 4               | ‌[Java Edition  only] |

### Note Blocks
Quartz pillars can be placed under note blocks to produce "bass drum" sounds.

## Data values
### ID
Java Edition:

| Name          | Identifier    | Form         | Block tags       | Translation key               |
|---------------|---------------|--------------|------------------|-------------------------------|
| Quartz Pillar | quartz_pillar | Block & Item | mineable/pickaxe | block.minecraft.quartz_pillar |

Bedrock Edition:

| Name                | Identifier   | Numeric ID | Form                       | Item ID[i 1]   | Translation key              |
|---------------------|--------------|------------|----------------------------|----------------|------------------------------|
| Pillar Quartz Block | quartz_block | 155        | Block & Giveable Item[i 2] | Identical[i 3] | tile.quartz_block.lines.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


### Block states
See also: Block states

Java Edition:

| Name | Default value | Allowed values | Description                                |
|------|---------------|----------------|--------------------------------------------|
| axis | y             | x              | The quartz pillar is oriented east–west.   |
|      |               | y              | The quartz pillar is oriented vertically.  |
|      |               | z              | The quartz pillar is oriented north–south. |

Bedrock Edition:

| Name        | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                      |
|-------------|---------------|---------------|----------------|-------------------------|--------------------------------------------------|
| chisel_type | 0x10x2        | default       | default        | 0                       | Block of Quartz                                  |
|             |               |               | chiseled       | 1                       | Chiseled Quartz Block                            |
|             |               |               | lines          | 2                       | Pillar Quartz Block                              |
|             |               |               | smooth         | 3                       | Smooth Quartz Block                              |
| pillar_axis | 0x40x8        | y             | x              | 1                       | The pillar quartz block is oriented east–west.   |
|             |               |               | y              | 0                       | The pillar quartz block is oriented vertically.  |
|             |               |               | z              | 2                       | The pillar quartz block is oriented north–south. |


