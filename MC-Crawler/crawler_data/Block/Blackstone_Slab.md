# Blackstone Slab
A blackstone slab is a blackstone variant of a slab.

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
Blackstone slabs can be mined using any pickaxe.

| Block     | Blackstone Slab       |
|-----------|-----------------------|
| Hardness  | 2                     |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 10                    |
| Wooden    | 1.5                   |
| Stone     | 0.75                  |
| Iron      | 0.5                   |
| Diamond   | 0.4                   |
| Netherite | 0.35                  |
| Golden    | 0.25                  |


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


### Natural generation
Blackstone slabs generate as part of bastion remnants.

### Crafting
| Ingredients | Crafting recipe |
|-------------|-----------------|
| Blackstone  | 6               |

### Stonecutting
| Ingredients | Cutting recipe |
|-------------|----------------|
| Blackstone  | 2              |

## Usage
For information about the placement mechanics of all slabs, see Slab § Usage.

### Note blocks
Blackstone slabs can be placed under note blocks to produce "bass drum" sounds.

## Data values
### ID
Java Edition:

| Name            | Identifier      | Form         | Block tags            | Item tags | Translation key                 |
|-----------------|-----------------|--------------|-----------------------|-----------|---------------------------------|
| Blackstone Slab | blackstone_slab | Block & Item | slabsmineable/pickaxe | slabs     | block.minecraft.blackstone_slab |

Bedrock Edition:

| Name                   | Identifier             | Numeric ID | Form                         | Item ID[i 1]   | Translation key           |
|------------------------|------------------------|------------|------------------------------|----------------|---------------------------|
| Blackstone Double Slab | blackstone_double_slab | 538        | Block & Ungiveable Item[i 2] | Identical[i 3] | —                         |
| Blackstone Slab        | blackstone_slab        | 537        | Block & Giveable Item[i 4]   | Identical[i 3] | tile.blackstone_slab.name |


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



