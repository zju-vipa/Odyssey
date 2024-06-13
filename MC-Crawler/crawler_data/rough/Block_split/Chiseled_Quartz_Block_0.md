# Chiseled Quartz Block
A chiseled quartz block, is a variant of the block of quartz, obtained by crafting from quartz slabs.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Crafting
	- 1.3 Stonecutting
- 2 Usage
	- 2.1 Crafting ingredient
	- 2.2 Note blocks
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 Notes
- 8 References

## Obtaining
### Breaking
Chiseled quartz blocks can be mined using any pickaxe. If mined without a pickaxe, it drops nothing.

| Block     | Chiseled Quartz Block |
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

### Crafting
| Ingredients | Crafting recipe |
|-------------|-----------------|
| Quartz Slab |                 |

### Stonecutting
| Ingredients     | Cutting recipe |
|-----------------|----------------|
| Block of Quartz |                |

## Usage
### Crafting ingredient
| Name          | Ingredients           | Crafting recipe | Description           |
|---------------|-----------------------|-----------------|-----------------------|
| Quartz Slab   | Chiseled Quartz Block | 6               | ‌[Java Edition  only] |
| Quartz Stairs | Chiseled Quartz Block | 4               | ‌[Java Edition  only] |

### Note blocks
Chiseled quartz blocks can be placed under note blocks to produce "bass drum" sounds.

## Data values
### ID
Java Edition:

| Name                  | Identifier              | Form         | Block tags         | Translation key                         |
|-----------------------|-------------------------|--------------|--------------------|-----------------------------------------|
| Chiseled Quartz Block | `chiseled_quartz_block` | Block & Item | `mineable/pickaxe` | `block.minecraft.chiseled_quartz_block` |

Bedrock Edition:

| Name                  | Identifier     | Numeric ID | Form                       | Item ID[i 1]   | Translation key                   |
|-----------------------|----------------|------------|----------------------------|----------------|-----------------------------------|
| Chiseled Quartz Block | `quartz_block` | `155`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.quartz_block.chiseled.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

Bedrock Edition:

| Name        | Metadata Bits   | Default value | Allowed values | Values forMetadata Bits | Description                               |
|-------------|-----------------|---------------|----------------|-------------------------|-------------------------------------------|
| chisel_type | `0x1`<br/>`0x2` | `default`     | `default`      | `0`                     | Block of Quartz                           |
|             |                 |               | `chiseled`     | `1`                     | Chiseled Quartz Block                     |
|             |                 |               | `lines`        | `2`                     | Pillar Quartz Block                       |
|             |                 |               | `smooth`       | `3`                     | Smooth Quartz Block                       |
| pillar_axis | `0x4`<br/>`0x8` | `y`           | `x`            | `1`                     | The quartz block is oriented east–west.   |
|             |                 |               | `y`            | `0`                     | The quartz block is oriented vertically.  |
|             |                 |               | `z`            | `2`                     | The quartz block is oriented north–south. |

## Notes



