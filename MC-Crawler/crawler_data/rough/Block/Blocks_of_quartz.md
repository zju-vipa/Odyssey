# Block of Quartz
A block of quartz is a mineral block used for decoration. It can be turned into a chiseled quartz block, quartz pillar[a], quartz bricks, or smooth quartz.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
	- 1.4 Trading
- 2 Usage
	- 2.1 Crafting ingredient
	- 2.2 Stonecutting
	- 2.3 Smelting ingredient
	- 2.4 Note blocks
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 Trivia
- 8 Gallery
	- 8.1 Screenshots
- 9 Notes
- 10 References
- 11 External links

## Obtaining
### Breaking
Blocks of quartz can be mined using any pickaxe. If mined without a pickaxe, it drops nothing.

| Block     | Block of Quartz       |
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
Four quartz blocks generate naturally as part of each bridge bastion remnant.

### Crafting
| Ingredients   | Crafting recipe |
|---------------|-----------------|
| Nether Quartz |                 |

### Trading
Master-level mason villagers sell a quartz block for an emerald.

## Usage
Quartz blocks cannot be used to store nether quartz because they cannot be crafted back into it, unlike blocks made from other ores.[1]

### Crafting ingredient
| Name          | Ingredients     | Crafting recipe | Description              |
|---------------|-----------------|-----------------|--------------------------|
| Quartz Bricks | Block of Quartz | 4               |                          |
| Quartz Pillar | Block of Quartz | 2               |                          |
| Quartz Slab   | Block of Quartz | 6               | ‌[Java Edition  only]    |
| Quartz Slab   | Block of Quartz | 6               | ‌[Bedrock Edition  only] |
| Quartz Stairs | Block of Quartz | 4               | ‌[Bedrock Edition  only] |
| Quartz Stairs | Block of Quartz | 4               | ‌[Java Edition  only]    |

### Stonecutting
| Ingredients     | Cutting recipe |
|-----------------|----------------|
| Block of Quartz | 2              |

### Smelting ingredient
| Name                | Ingredients                  | Smelting recipe |
|---------------------|------------------------------|-----------------|
| Smooth Quartz Block | Block of Quartz+<br/>Anyfuel | 0.1             |

### Note blocks
Blocks of quartz can be placed under note blocks to produce "bass drum" sounds.

## Data values
### ID
Java Edition:

| Name            | Identifier     | Form         | Block tags         | Translation key                |
|-----------------|----------------|--------------|--------------------|--------------------------------|
| Block of Quartz | `quartz_block` | Block & Item | `mineable/pickaxe` | `block.minecraft.quartz_block` |

Bedrock Edition:

| Name            | Identifier     | Numeric ID | Form                       | Item ID[i 1]   | Translation key                  |
|-----------------|----------------|------------|----------------------------|----------------|----------------------------------|
| Block of Quartz | `quartz_block` | `155`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.quartz_block.default.name` |

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
1. ↑Known as quartz pillar in Java Edition and pillar quartz block in Bedrock Edition.

