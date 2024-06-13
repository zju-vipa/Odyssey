# Polished Blackstone Brick Slab
A polished blackstone brick slab is a polished blackstone bricks variant of a slab.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
	- 1.4 Stonecutting
- 2 Usage
	- 2.1 Note blocks
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 References

## Obtaining
### Breaking
Polished blackstone brick slabs can be mined using any pickaxe.

| Block     | Polished Blackstone Brick Slab |
|-----------|--------------------------------|
| Hardness  | 2                              |
| Tool      |                                |
|           | Breakingtime (sec)[A]          |
| Default   | 10                             |
| Wooden    | 1.5                            |
| Stone     | 0.75                           |
| Iron      | 0.5                            |
| Diamond   | 0.4                            |
| Netherite | 0.35                           |
| Golden    | 0.25                           |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Natural generation
Polished blackstone brick slabs generate as part of ruined portals in the Nether.

### Crafting
| Ingredients                | Crafting recipe |
|----------------------------|-----------------|
| Polished Blackstone Bricks | 6               |

### Stonecutting
| Ingredients                                                           | Cutting recipe |
|-----------------------------------------------------------------------|----------------|
| Blackstoneor<br/>Polished Blackstoneor<br/>Polished Blackstone Bricks | 2              |

## Usage
For information about the placement mechanics of all slabs, see Slab § Usage.

### Note blocks
Polished blackstone brick slabs can be placed under note blocks to produce "bass drum" sounds.

## Data values
### ID
Java Edition:

| Name                           | Identifier                       | Form         | Block tags                     | Item tags | Translation key                                  |
|--------------------------------|----------------------------------|--------------|--------------------------------|-----------|--------------------------------------------------|
| Polished Blackstone Brick Slab | `polished_blackstone_brick_slab` | Block & Item | `slabs`<br/>`mineable/pickaxe` | `slabs`   | `block.minecraft.polished_blackstone_brick_slab` |

Bedrock Edition:

| Name                                  | Identifier                              | Numeric ID | Form                         | Item ID[i 1]   | Translation key                            |
|---------------------------------------|-----------------------------------------|------------|------------------------------|----------------|--------------------------------------------|
| Polished Blackstone Brick Double Slab | `polished_blackstone_brick_double_slab` | `540`      | Block & Ungiveable Item[i 2] | Identical[i 3] | —                                          |
| Polished Blackstone Brick Slab        | `polished_blackstone_brick_slab`        | `539`      | Block & Giveable Item[i 4]   | Identical[i 3] | `tile.polished_blackstone_brick_slab.name` |

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



