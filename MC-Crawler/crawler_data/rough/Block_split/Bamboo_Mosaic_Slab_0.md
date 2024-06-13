# Bamboo Mosaic Slab
A bamboo mosaic slab is a bamboo mosaic variant of a slab.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Crafting
- 2 Usage
	- 2.1 Fuel
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 References

## Obtaining
### Breaking
Bamboo mosaic slabs can be broken with anything, but axes are fastest.

| Block     | Bamboo Mosaic Slab    |
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
| Ingredients   | Crafting recipe |
|---------------|-----------------|
| Bamboo Mosaic | 6               |

## Usage
For information about the placement mechanics of all slabs, see Slab § Usage.

### Fuel
Bamboo mosaic slabs can be used as fuel in furnaces, smelting 0.75 items per slab in Java Edition, and 1.5 items per slab in Bedrock Edition.[1]

## Data values
### ID
Java Edition:

| Name               | Identifier           | Form         | Block tags                 | Item tags | Translation key                      |
|--------------------|----------------------|--------------|----------------------------|-----------|--------------------------------------|
| Bamboo Mosaic Slab | `bamboo_mosaic_slab` | Block & Item | `slabs`<br/>`mineable/axe` | `slabs`   | `block.minecraft.bamboo_mosaic_slab` |

Bedrock Edition:

| Name                      | Identifier                  | Numeric ID | Form                         | Item ID[i 1]   | Translation key                |
|---------------------------|-----------------------------|------------|------------------------------|----------------|--------------------------------|
| Bamboo Mosaic Double Slab | `bamboo_mosaic_double_slab` | `-525`     | Block & Ungiveable Item[i 2] | Identical[i 3] | —                              |
| Bamboo Mosaic Slab        | `bamboo_mosaic_slab`        | `-524`     | Block & Giveable Item[i 4]   | Identical[i 3] | `tile.bamboo_mosaic_slab.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Unavailable with /give command
3. ↑ a bThe block's direct item form has the same id as the block.
4. ↑Available with /give command.

### Block states
See also: Block states

Java Edition:

| Name        | Default value | Allowed values     | Description                                                  |
|-------------|---------------|--------------------|--------------------------------------------------------------|
| type        | `bottom`      | `bottom`<br/>`top` | Where the slab is within its block.                          |
|             |               | `double`           | The block is a double slab.                                  |
| waterlogged | `false`       | `false`<br/>`true` | Whether or not there's water in the same place as this slab. |

Bedrock Edition:

| Name                    | Metadata Bits | Default value | Allowed values     | Values forMetadata Bits | Description                         |
|-------------------------|---------------|---------------|--------------------|-------------------------|-------------------------------------|
| minecraft:vertical_half | Not Supported | `bottom`      | `bottom`<br/>`top` | `Unsupported`           | Where the slab is within its block. |




