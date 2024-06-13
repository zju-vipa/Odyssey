# Polished Deepslate Slab
A polished deepslate slab is a polished deepslate variant of a slab.

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
Polished deepslate slabs can be mined using any pickaxe.

| Block     | Polished Deepslate Slab |
|-----------|-------------------------|
| Hardness  | 3.5                     |
| Tool      |                         |
|           | Breakingtime (sec)[A]   |
| Default   | 17.5                    |
| Wooden    | 2.65                    |
| Stone     | 1.35                    |
| Iron      | 0.9                     |
| Diamond   | 0.7                     |
| Netherite | 0.6                     |
| Golden    | 0.45                    |


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


### Natural generation
Polished deepslate slabs generate as part of ancient cities.

### Crafting
| Ingredients        | Crafting recipe |
|--------------------|-----------------|
| Polished Deepslate | 6               |

### Stonecutting
| Ingredients                           | Cutting recipe |
|---------------------------------------|----------------|
| Cobbled DeepslateorPolished Deepslate | 2              |

## Usage
For information about the placement mechanics of all slabs, see Slab § Usage.

### Note blocks
Polished deepslate slabs can be placed under note blocks to produce "bass drum" sounds.

## Data values
### ID
Java Edition:

| Name                    | Identifier              | Form         | Block tags            | Item tags | Translation key                         |
|-------------------------|-------------------------|--------------|-----------------------|-----------|-----------------------------------------|
| Polished Deepslate Slab | polished_deepslate_slab | Block & Item | slabsmineable/pickaxe | slabs     | block.minecraft.polished_deepslate_slab |

Bedrock Edition:

| Name                           | Identifier                     | Numeric ID | Form                         | Item ID[i 1]   | Translation key                          |
|--------------------------------|--------------------------------|------------|------------------------------|----------------|------------------------------------------|
| Polished Deepslate Double Slab | polished_deepslate_double_slab | 652        | Block & Ungiveable Item[i 2] | Identical[i 3] | tile.polished_deepslate_double_slab.name |
| Polished Deepslate Slab        | polished_deepslate_slab        | 639        | Block & Giveable Item[i 4]   | Identical[i 3] | tile.polished_deepslate_slab.name        |


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




