# Purpur Pillar
Purpur pillars are decorative blocks that are naturally generated in end cities and end ships.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
	- 1.4 Stonecutting
- 2 Usage
	- 2.1 Crafting ingredient
	- 2.2 Note Blocks
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 Gallery
- 8 External links

## Obtaining
### Breaking
Purpur pillars can be mined using any pickaxe. If mined without a pickaxe, it drops nothing.

| Block     | Purpur Pillar         |
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

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Natural generation
Purpur pillars can be found naturally as part of the structure of end cities and end ships.

### Crafting
| Ingredients | Crafting recipe |
|-------------|-----------------|
| Purpur Slab |                 |

### Stonecutting
| Name          | Ingredients  | Cutting recipe |
|---------------|--------------|----------------|
| Purpur Pillar | Purpur Block |                |

## Usage
Purpur pillars are primarily decorative blocks, similar to other brick-type blocks. Purpur pillar blocks can be placed sideways, similar to logs or quartz pillar blocks.

### Crafting ingredient
Purpur pillars can be used to craft purpur slabs in Java Edition, but not Bedrock Edition. 

| Name          | Ingredients   | Crafting recipe | Description           |
|---------------|---------------|-----------------|-----------------------|
| Purpur Slab   | Purpur Pillar | 6               | ‌[Java Edition  only] |
| Purpur Stairs | Purpur Pillar | 4               |                       |

### Note Blocks
Purpur pillar can be placed under note blocks to produce "bass drum" sound.

## Data values
### ID
Java Edition:

| Name          | Identifier      | Form         | Block tags         | Translation key                 |
|---------------|-----------------|--------------|--------------------|---------------------------------|
| Purpur Pillar | `purpur_pillar` | Block & Item | `mineable/pickaxe` | `block.minecraft.purpur_pillar` |

Bedrock Edition:

| Name          | Identifier     | Numeric ID | Form                       | Item ID[i 1]   | Translation key                |
|---------------|----------------|------------|----------------------------|----------------|--------------------------------|
| Purpur Pillar | `purpur_block` | `201`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.purpur_block.lines.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

Java Edition:

| Name | Default value | Allowed values | Description                                |
|------|---------------|----------------|--------------------------------------------|
| axis | `y`           | `x`            | The purpur pillar is oriented east–west.   |
|      |               | `y`            | The purpur pillar is oriented vertically.  |
|      |               | `z`            | The purpur pillar is oriented north–south. |

Bedrock Edition:

| Name        | Metadata Bits   | Default value | Allowed values | Values forMetadata Bits | Description                                |
|-------------|-----------------|---------------|----------------|-------------------------|--------------------------------------------|
| chisel_type | `0x1`<br/>`0x2` | `default`     | `default`      | `0`                     | Purpur Block                               |
|             |                 |               | `chiseled`     | `1`                     | Chiseled Purpur(Unused)                    |
|             |                 |               | `lines`        | `2`                     | Purpur Pillar                              |
|             |                 |               | `smooth`       | `3`                     | Smooth Purpur(Unused)                      |
| pillar_axis | `0x4`<br/>`0x8` | `y`           | `x`            | `1`                     | The purpur pillar is oriented east–west.   |
|             |                 |               | `y`            | `0`                     | The purpur pillar is oriented vertically.  |
|             |                 |               | `z`            | `2`                     | The purpur pillar is oriented north–south. |



