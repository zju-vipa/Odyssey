# Block of Stripped Bamboo
A block of stripped bamboo is a variant of the block of bamboo made by using an axe on a block of bamboo.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Post-generation
		- 1.2.1 Stripping
- 2 Usage
	- 2.1 Crafting ingredient
	- 2.2 Fuel
	- 2.3 Note blocks
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 Gallery
	- 7.1 Screenshots
	- 7.2 In other media
- 8 References
- 9 External links

## Obtaining
### Breaking
Blocks of stripped bamboo can be broken by hand, but using an axe speeds up the process.

| Block     | Block of Stripped Bamboo |
|-----------|--------------------------|
| Hardness  | 2                        |
| Tool      |                          |
|           | Breakingtime (sec)[A]    |
| Default   | 3                        |
| Wooden    | 1.5                      |
| Stone     | 0.75                     |
| Iron      | 0.5                      |
| Diamond   | 0.4                      |
| Netherite | 0.35                     |
| Golden    | 0.25                     |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Post-generation
#### Stripping
Using an axe on a block of bamboo turns it into a block of stripped bamboo.

## Usage
### Crafting ingredient
| Name                | Ingredients                         | Crafting recipe |
|---------------------|-------------------------------------|-----------------|
| Bamboo Hanging Sign | Chain+<br/>Block of Stripped Bamboo | 6               |
| Bamboo Planks       | Block of Stripped Bamboo            | 2               |

### Fuel
Blocks of stripped bamboo can be used as fuel in furnaces, smelting 1.5 items per block.

Unlike logs, blocks of bamboo cannot be smelted into charcoal.[1]

### Note blocks
Blocks of stripped bamboo can be placed under note blocks to produce "bass" sounds.

## Data values
### ID
Java Edition:

| Name                     | Identifier              | Form         | Block tags                         | Item tags       | Translation key                         |
|--------------------------|-------------------------|--------------|------------------------------------|-----------------|-----------------------------------------|
| Block of Stripped Bamboo | `stripped_bamboo_block` | Block & Item | `mineable/axe`<br/>`bamboo_blocks` | `bamboo_blocks` | `block.minecraft.stripped_bamboo_block` |

Bedrock Edition:

| Name                     | Identifier              | Numeric ID | Form                       | Item ID[i 1]   | Translation key                   |
|--------------------------|-------------------------|------------|----------------------------|----------------|-----------------------------------|
| Block of Stripped Bamboo | `stripped_bamboo_block` | `-528`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.stripped_bamboo_block.name` |

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



