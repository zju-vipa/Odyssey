# Red Sandstone
Red sandstone is a variant of regular sandstone. Red sandstone comes in the three other variants, them being cut red sandstone, chiseled red sandstone, and smooth red sandstone.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
- 2 Usage
	- 2.1 Crafting ingredient
	- 2.2 Stonecutting
	- 2.3 Smelting
	- 2.4 Note blocks
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 Video
- 6 History
	- 6.1 Data history
- 7 Issues
- 8 Gallery
	- 8.1 Screenshots
- 9 References

## Obtaining
### Breaking
Red Sandstone can be mined with any pickaxe. If mined without a pickaxe, the block drops nothing.

| Block     | Red Sandstone         |
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
Red sandstone generates at noise cave entrances in badlands biomes.

If a village generates some buildings inside of a badlands biome, any floating platform surrounding village buildings generate with red sandstone below red sand.

No naturally generated structures are made of red sandstone.


### Crafting
| Ingredients | Crafting recipe |
|-------------|-----------------|
| Red Sand    |                 |

## Usage
Unlike red sand, red sandstone is never affected by gravity.

### Crafting ingredient
| Name                 | Ingredients   | Crafting recipe |
|----------------------|---------------|-----------------|
| Cut Red Sandstone    | Red Sandstone | 4               |
| Red Sandstone Slab   | Red Sandstone | 6               |
| Red Sandstone Stairs | Red Sandstone | 4               |
| Red Sandstone Wall   | Red Sandstone | 6               |

### Stonecutting
| Ingredients   | Cutting recipe |
|---------------|----------------|
| Red Sandstone | 22             |

### Smelting
| Ingredients                | Smelting recipe |
|----------------------------|-----------------|
| Red Sandstone+<br/>Anyfuel | 0.1             |

### Note blocks
Red sandstone can be placed under note blocks to produce "bass drum" sounds.

## Data values
### ID
Java Edition:

| Name          | Identifier      | Form         | Translation key                 |
|---------------|-----------------|--------------|---------------------------------|
| Red Sandstone | `red_sandstone` | Block & Item | `block.minecraft.red_sandstone` |

Bedrock Edition:

| Name          | Identifier      | Numeric ID | Form                       | Item ID[i 1]   | Translation key                   |
|---------------|-----------------|------------|----------------------------|----------------|-----------------------------------|
| Red Sandstone | `red_sandstone` | `179`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.red_sandstone.default.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

In Bedrock Edition, sandstone and red sandstone use the following block states:

Bedrock Edition:

| Name            | Metadata Bits   | Default value | Allowed values | Values forMetadata Bits | Description        |
|-----------------|-----------------|---------------|----------------|-------------------------|--------------------|
| sand_stone_type | `0x1`<br/>`0x2` | `default`     | `default`      | `0`                     | Sandstone          |
|                 |                 |               | `heiroglyphs`  | `1`                     | Chiseled Sandstone |
|                 |                 |               | `cut`          | `2`                     | Cut Sandstone      |
|                 |                 |               | `smooth`       | `3`                     | Smooth Sandstone   |




