# Deepslate Bricks
Deepslate bricks are the brick version of deepslate.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
- 2 Usage
	- 2.1 Crafting ingredient
	- 2.2 Stonecutting
	- 2.3 Smelting
- 3 Sounds
- 4 Data values
	- 4.1 ID
- 5 History
- 6 Issues

## Obtaining
### Breaking
Deepslate bricks can be obtained only by mining them with any pickaxe. When mined using any other tool, they drop nothing.

| Block     | Deepslate Bricks      |
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

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Natural generation
Deepslate bricks generate naturally in ancient cities.

### Crafting
| Ingredients        | Crafting recipe |
|--------------------|-----------------|
| Polished Deepslate | 4               |

## Usage
### Crafting ingredient
| Name                   | Ingredients      | Crafting recipe |
|------------------------|------------------|-----------------|
| Deepslate Brick Slab   | Deepslate Bricks | 6               |
| Deepslate Brick Stairs | Deepslate Bricks | 4               |
| Deepslate Brick Wall   | Deepslate Bricks | 6               |
| Deepslate Tiles        | Deepslate Bricks | 4               |

### Stonecutting
| Name                   | Ingredients      | Cutting recipe |
|------------------------|------------------|----------------|
| Deepslate Brick Slab   | Deepslate Bricks | 2              |
| Deepslate Brick Stairs | Deepslate Bricks |                |
| Deepslate Brick Wall   | Deepslate Bricks |                |
| Deepslate Tiles        | Deepslate Bricks |                |
| Deepslate Tile Slab    | Deepslate Bricks | 2              |
| Deepslate Tile Stairs  | Deepslate Bricks |                |
| Deepslate Tile Wall    | Deepslate Bricks |                |

### Smelting
| Name                     | Ingredients                   | Smelting recipe |
|--------------------------|-------------------------------|-----------------|
| Cracked Deepslate Bricks | Deepslate Bricks+<br/>Anyfuel | 0.1             |

## Data values
### ID
Java Edition:

| Name             | Identifier         | Form         | Translation key                    |
|------------------|--------------------|--------------|------------------------------------|
| Deepslate Bricks | `deepslate_bricks` | Block & Item | `block.minecraft.deepslate_bricks` |

Bedrock Edition:

| Name             | Identifier         | Numeric ID | Form                       | Item ID[i 1]   | Translation key              |
|------------------|--------------------|------------|----------------------------|----------------|------------------------------|
| Deepslate Bricks | `deepslate_bricks` | `646`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.deepslate_bricks.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.


