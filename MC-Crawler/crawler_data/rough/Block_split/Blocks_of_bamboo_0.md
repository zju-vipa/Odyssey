# Block of Bamboo
The block of bamboo is a log-like block made of bamboo.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Crafting
- 2 Usage
	- 2.1 Crafting ingredient
	- 2.2 Stripping
	- 2.3 Fuel
	- 2.4 Note blocks
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 Gallery
	- 7.1 Concept artwork
- 8 References
- 9 External links

## Obtaining
### Breaking
They can be broken by hand, but using an axe speeds up the process.

| Block     | Block of Bamboo       |
|-----------|-----------------------|
| Hardness  | 2                     |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 3                     |
| Wooden    | 1.5                   |
| Stone     | 0.75                  |
| Iron      | 0.5                   |
| Diamond   | 0.4                   |
| Netherite | 0.35                  |
| Golden    | 0.25                  |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Crafting
| Ingredients | Crafting recipe | Description                           |
|-------------|-----------------|---------------------------------------|
| Bamboo      |                 | Cannot be crafted back into 9 bamboo. |

## Usage
### Crafting ingredient
| Name          | Ingredients     | Crafting recipe |
|---------------|-----------------|-----------------|
| Bamboo Planks | Block of Bamboo | 2               |

### Stripping
Using an axe on a block of bamboo turns it into a block of stripped bamboo.

### Fuel
Blocks of bamboo can be used as a fuel in furnaces, smelting 1.5 items per block.

The efficiency of using bamboo as fuel depends on how it is crafted. 9 bamboo can smelt 2.25 items, whereas a block can smelt only 1.5 items. However, the block can be crafted into 2 bamboo planks, which together can smelt 3 items.

Unlike logs, blocks of bamboo cannot be smelted into charcoal.[1]

### Note blocks
Block of bamboo can be placed under note blocks to produce "bass" sounds.

## Data values
### ID
Java Edition:

| Name            | Identifier     | Form         | Block tags                         | Item tags       | Translation key                |
|-----------------|----------------|--------------|------------------------------------|-----------------|--------------------------------|
| Block of Bamboo | `bamboo_block` | Block & Item | `mineable/axe`<br/>`bamboo_blocks` | `bamboo_blocks` | `block.minecraft.bamboo_block` |

Bedrock Edition:

| Name            | Identifier     | Numeric ID | Form                       | Item ID[i 1]   | Translation key          |
|-----------------|----------------|------------|----------------------------|----------------|--------------------------|
| Block of Bamboo | `bamboo_block` | `-527`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.bamboo_block.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

Java Edition:

| Name | Default value | Allowed values | Description                        |
|------|---------------|----------------|------------------------------------|
| axis | `y`           | `x`            | The block is oriented east–west.   |
|      |               | `y`            | The block is oriented vertically.  |
|      |               | `z`            | The block is oriented north–south. |

Bedrock Edition:

| Name        | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                        |
|-------------|---------------|---------------|----------------|-------------------------|------------------------------------|
| pillar_axis | Not Supported | `y`           | `x`            | `Unsupported`           | The block is oriented east-west.   |
|             |               |               | `y`            | `Unsupported`           | The block is oriented vertically.  |
|             |               |               | `z`            | `Unsupported`           | The block is oriented north-south. |




