# Chiseled Sandstone
Chiseled sandstone is a decorative variant of sandstone, crafted from sandstone slabs.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
	- 1.4 Stonecutting
- 2 Usage
	- 2.1 Crafting ingredient
	- 2.2 Note blocks
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 Trivia
- 8 References

## Obtaining
### Breaking
Chiseled sandstone can be mined with any pickaxe. If mined without a pickaxe, the block drops nothing.

| Block     | Chiseled Sandstone    |
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

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Natural generation
Chiseled sandstone generates in desert pyramids. Additionally, chiseled sandstone can also generate in warm underwater ruins.

### Crafting
| Ingredients    | Crafting recipe |
|----------------|-----------------|
| Sandstone Slab |                 |

### Stonecutting
| Ingredients | Cutting recipe |
|-------------|----------------|
| Sandstone   |                |

## Usage
Unlike sand, chiseled sandstone is never affected by gravity.

### Crafting ingredient
| Name           | Ingredients        | Crafting recipe |
|----------------|--------------------|-----------------|
| Sandstone Slab | Chiseled Sandstone | 6               |

### Note blocks
Chiseled sandstone can be placed under note blocks to produce "bass drum" sounds.

## Data values
### ID
Java Edition:

| Name               | Identifier           | Form         | Translation key                      |
|--------------------|----------------------|--------------|--------------------------------------|
| Chiseled Sandstone | `chiseled_sandstone` | Block & Item | `block.minecraft.chiseled_sandstone` |

Bedrock Edition:

| Name               | Identifier  | Numeric ID | Form                       | Item ID[i 1]   | Translation key                |
|--------------------|-------------|------------|----------------------------|----------------|--------------------------------|
| Chiseled Sandstone | `sandstone` | `24`       | Block & Giveable Item[i 2] | Identical[i 3] | `tile.sandstone.chiseled.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

In Bedrock Edition, chiseled sandstone use the following block states:

Bedrock Edition:

| Name            | Metadata Bits   | Default value | Allowed values | Values forMetadata Bits | Description        |
|-----------------|-----------------|---------------|----------------|-------------------------|--------------------|
| sand_stone_type | `0x1`<br/>`0x2` | `default`     | `default`      | `0`                     | Sandstone          |
|                 |                 |               | `heiroglyphs`  | `1`                     | Chiseled Sandstone |
|                 |                 |               | `cut`          | `2`                     | Cut Sandstone      |
|                 |                 |               | `smooth`       | `3`                     | Smooth Sandstone   |



