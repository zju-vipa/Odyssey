# Deepslate Brick Slab
A deepslate brick slab is a deepslate brick variant of a slab.

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
Deepslate brick slabs can be mined using any pickaxe.

| Block     | Deepslate Brick Slab  |
|-----------|-----------------------|
| Hardness  | 3.5                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 17.5                  |
| Wooden    | 2.65                  |
| Stone     | 1.35                  |
| Iron      | 0.9                   |
| Diamond   | 0.7                   |
| Netherite | 0.6                   |
| Golden    | 0.45                  |


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


### Natural generation
Deepslate brick slabs generate as part of ancient cities.

### Crafting
| Ingredients      | Crafting recipe |
|------------------|-----------------|
| Deepslate Bricks | 6               |

### Stonecutting
| Ingredients                                             | Cutting recipe |
|---------------------------------------------------------|----------------|
| Cobbled DeepslateorPolished DeepslateorDeepslate Bricks | 2              |

## Usage
For information about the placement mechanics of all slabs, see Slab § Usage.

### Note blocks
Deepslate brick slabs can be placed under note blocks to produce "bass drum" sounds.

## Data values
### ID
Java Edition:

| Name                 | Identifier           | Form         | Block tags            | Item tags | Translation key                      |
|----------------------|----------------------|--------------|-----------------------|-----------|--------------------------------------|
| Deepslate Brick Slab | deepslate_brick_slab | Block & Item | slabsmineable/pickaxe | slabs     | block.minecraft.deepslate_brick_slab |

Bedrock Edition:

| Name                        | Identifier                  | Numeric ID | Form                         | Item ID[i 1]   | Translation key                       |
|-----------------------------|-----------------------------|------------|------------------------------|----------------|---------------------------------------|
| Deepslate Brick Double Slab | deepslate_brick_double_slab | 654        | Block & Ungiveable Item[i 2] | Identical[i 3] | tile.deepslate_brick_double_slab.name |
| Deepslate Brick Slab        | deepslate_brick_slab        | 647        | Block & Giveable Item[i 4]   | Identical[i 3] | tile.deepslate_brick_slab.name        |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Unavailable with /give command

↑ a b The block's direct item form has the same id as the block.

↑ Available with /give command.


### Block states
See also: Block states

Java Edition:

| Name        | Default value | Allowed values | Description                                                  |
|-------------|---------------|----------------|--------------------------------------------------------------|
| type        | bottom        | bottomtop      | Where the slab is within its block.                          |
|             |               | double         | The block is a double slab.                                  |
| waterlogged | false         | falsetrue      | Whether or not there's water in the same place as this slab. |

Bedrock Edition:

| Name                    | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                         |
|-------------------------|---------------|---------------|----------------|-------------------------|-------------------------------------|
| minecraft:vertical_half | Not Supported | bottom        | bottomtop      | Unsupported             | Where the slab is within its block. |




