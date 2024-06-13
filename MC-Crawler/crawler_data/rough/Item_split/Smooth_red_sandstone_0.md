# Smooth Red Sandstone
Smooth red sandstone is a variant of red sandstone, obtained by smelting.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Smelting
- 2 Usage
	- 2.1 Crafting ingredient
	- 2.2 Stonecutting
	- 2.3 Note blocks
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
	- 5.1 Data history
- 6 Issues
- 7 References
- 8 External links

## Obtaining
### Breaking
Smooth red sandstone can be mined with any pickaxe. If mined without a pickaxe, the block drops nothing.

| Block     | Smooth Red Sandstone  |
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

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Smelting
| Ingredients                | Smelting recipe |
|----------------------------|-----------------|
| Red Sandstone+<br/>Anyfuel | 0.1             |

## Usage
Unlike red sand, smooth red sandstone is never affected by gravity.

### Crafting ingredient
| Name                        | Ingredients          | Crafting recipe |
|-----------------------------|----------------------|-----------------|
| Smooth Red Sandstone Slab   | Smooth Red Sandstone | 6               |
| Smooth Red Sandstone Stairs | Smooth Red Sandstone | 4               |

### Stonecutting
| Ingredients          | Cutting recipe |
|----------------------|----------------|
| Smooth Red Sandstone | 2              |

### Note blocks
Smooth red sandstone can be placed under note blocks to produce "bass drum" sounds.

## Data values
### ID
Java Edition:

| Name                 | Identifier             | Form         | Translation key                        |
|----------------------|------------------------|--------------|----------------------------------------|
| Smooth Red Sandstone | `smooth_red_sandstone` | Block & Item | `block.minecraft.smooth_red_sandstone` |

Bedrock Edition:

| Name                 | Identifier      | Numeric ID | Form                       | Item ID[i 1]   | Translation key                  |
|----------------------|-----------------|------------|----------------------------|----------------|----------------------------------|
| Smooth Red Sandstone | `red_sandstone` | `179`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.red_sandstone.smooth.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

In Bedrock Edition, smooth red sandstone use the following block states:

Bedrock Edition:

| Name            | Metadata Bits   | Default value | Allowed values | Values forMetadata Bits | Description        |
|-----------------|-----------------|---------------|----------------|-------------------------|--------------------|
| sand_stone_type | `0x1`<br/>`0x2` | `default`     | `default`      | `0`                     | Sandstone          |
|                 |                 |               | `heiroglyphs`  | `1`                     | Chiseled Sandstone |
|                 |                 |               | `cut`          | `2`                     | Cut Sandstone      |
|                 |                 |               | `smooth`       | `3`                     | Smooth Sandstone   |




