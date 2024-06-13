# Stone Bricks
Stone bricks is a block found in various structures. It has three other variants, mossy stone bricks, cracked stone bricks, and chiseled stone bricks.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Infested blocks
	- 1.3 Natural generation
	- 1.4 Chest loot
	- 1.5 Crafting
	- 1.6 Stonecutting
- 2 Usage
	- 2.1 Crafting ingredient
	- 2.2 Smelting
	- 2.3 Stonecutting
	- 2.4 Note Blocks
	- 2.5 Silverfish
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 Trivia
- 8 Gallery
	- 8.1 Screenshots
- 9 See also
- 10 References

## Obtaining
### Breaking
Stone bricks can be mined using any pickaxe. If mined without a pickaxe, they drop nothing.

| Block     | Stone Bricks          |
|-----------|-----------------------|
| Hardness  | 1.5                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 7.5                   |
| Wooden    | 1.15                  |
| Stone     | 0.6                   |
| Iron      | 0.4                   |
| Diamond   | 0.3                   |
| Netherite | 0.25                  |
| Golden    | 0.2                   |


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


### Infested blocks
Stone bricks can also be obtained by mining their respective infested blocks with Silk Touch.

### Natural generation
Regular stone bricks generate as part of strongholds, making up most of the walls, ceilings, and floors. They can also generate as part of ocean ruins and ruined portals. Igloo basements are lined with stone bricks. Stone bricks can also spawn in trail ruins.

### Chest loot
| Item         | Structure | Container     | Quantity | Chance                         |
|--------------|-----------|---------------|----------|--------------------------------|
|              |           |               |          | Java EditionandBedrock Edition |
| Stone Bricks | Village   | Mason's chest | 1        | 37.7%                          |

### Crafting
| Ingredients | Crafting recipe | Description |
|-------------|-----------------|-------------|
| Stone       | 4               |             |

### Stonecutting
| Ingredients | Cutting recipe | Description |
|-------------|----------------|-------------|
| Stone       |                |             |

## Usage
As stone bricks offer no real advantage over stone or cobblestone, their main use is for decoration.

### Crafting ingredient
| Name               | Ingredients             | Crafting recipe |
|--------------------|-------------------------|-----------------|
| Mossy Stone Bricks | Stone Bricks+Vines      |                 |
| Mossy Stone Bricks | Stone Bricks+Moss Block |                 |
| Stone Brick Slab   | Stone Bricks            | 6               |
| Stone Brick Stairs | Stone Bricks            | 4               |
| Stone Brick Wall   | Stone Bricks            | 6               |

### Smelting
| Name                 | Ingredients          | Smelting recipe |
|----------------------|----------------------|-----------------|
| Cracked Stone Bricks | Stone Bricks+Anyfuel | 0.1             |

### Stonecutting
| Name                                                                     | Ingredients        | Cutting recipe | Description              |
|--------------------------------------------------------------------------|--------------------|----------------|--------------------------|
| Stone Brick SlaborStone Brick StairsorStone Brick Wall                   | Stone Bricks       | 2              |                          |
| Chiseled Stone Bricks                                                    | Stone Bricks       |                | ‌[Java Edition  only][1] |
| Mossy Stone Brick SlaborMossy Stone Brick StairsorMossy Stone Brick Wall | Mossy Stone Bricks | 2              |                          |

### Note Blocks
Stone bricks can be placed under note blocks to produce "bass drum" sounds.

### Silverfish
Silverfish have the ability to enter and hide in stone bricks, creating an infested block of the corresponding type.

## Data values
### ID
Java Edition:

| Name         | Identifier   | Form         | Block tags   | Item tags    | Translation key              |
|--------------|--------------|--------------|--------------|--------------|------------------------------|
| Stone Bricks | stone_bricks | Block & Item | stone_bricks | stone_bricks | block.minecraft.stone_bricks |

Bedrock Edition:

| Name         | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key                                         |
|--------------|------------|------------|----------------------------|----------------|---------------------------------------------------------|
| Stone Bricks | stonebrick | 98         | Block & Giveable Item[i 2] | Identical[i 3] | tile.stonebrick.default.nametile.stonebrick.smooth.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


### Block states
See also: Block states

Bedrock Edition

| Name             | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                                |
|------------------|---------------|---------------|----------------|-------------------------|------------------------------------------------------------|
| stone_brick_type | 0x10x20x4     | default       | default        | 0                       | Stone Bricks                                               |
|                  |               |               | mossy          | 1                       | Mossy Stone Bricks                                         |
|                  |               |               | cracked        | 2                       | Cracked Stone Bricks                                       |
|                  |               |               | chiseled       | 3                       | Chiseled Stone Bricks                                      |
|                  |               |               | smooth         | 4                       | Smooth Stone Bricks (unused, same texture as regular ones) |



## See also
- Infested Block

