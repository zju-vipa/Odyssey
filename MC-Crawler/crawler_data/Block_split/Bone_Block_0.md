# Bone Block
Bone blocks are storage blocks equivalent to nine pieces of bone meal. 

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Chest loot
	- 1.4 Crafting
- 2 Usage
	- 2.1 Crafting ingredient
	- 2.2 Note blocks
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 Gallery
	- 7.1 Screenshots
- 8 External links

## Obtaining
### Breaking
Bone blocks can be mined using any pickaxe. If mined without a pickaxe, they drop nothing.

| Block     | Bone Block            |
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
Bone blocks are generated naturally as part of fossil structures found in desert and swamp biomes. They also generate as part of nether fossils in soul sand valley biomes.


### Chest loot
| Item       | Structure       | Container     | Quantity | Chance                         |
|------------|-----------------|---------------|----------|--------------------------------|
|            |                 |               |          | Java EditionandBedrock Edition |
| Bone Block | Bastion Remnant | Generic chest | 3–6      | 24.4%                          |

### Crafting
| Ingredients | Crafting recipe |
|-------------|-----------------|
| Bone Meal   |                 |

## Usage
Bone blocks are decorative blocks, and can also be used as compact storage for bone meal.

### Crafting ingredient
| Name      | Ingredients | Crafting recipe |
|-----------|-------------|-----------------|
| Bone Meal | Bone Block  | 9               |

### Note blocks
Bone blocks can be placed under note blocks to produce xylophone sounds.

## Data values
### ID
Java Edition:

| Name       | Identifier | Form         | Translation key            |
|------------|------------|--------------|----------------------------|
| Bone Block | bone_block | Block & Item | block.minecraft.bone_block |

Bedrock Edition:

| Name       | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key      |
|------------|------------|------------|----------------------------|----------------|----------------------|
| Bone Block | bone_block | 216        | Block & Giveable Item[i 2] | Identical[i 3] | tile.bone_block.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


### Block states
See also: Block states

Java Edition:

| Name | Default value | Allowed values | Description                             |
|------|---------------|----------------|-----------------------------------------|
| axis | y             | x              | The bone block is oriented east–west.   |
|      |               | y              | The bone block is oriented vertically.  |
|      |               | z              | The bone block is oriented north–south. |

Bedrock Edition:

| Name        | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                |
|-------------|---------------|---------------|----------------|-------------------------|--------------------------------------------|
| pillar_axis | 0x40x8        | y             | yxz            | 012                     | The axis along which the block is oriented |
| deprecated  | 0x10x2        | 0             | 0123           | 0123                    | Unused, has no effect in game.             |




