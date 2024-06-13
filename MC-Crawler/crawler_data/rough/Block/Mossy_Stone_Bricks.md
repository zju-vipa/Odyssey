# Mossy Stone Bricks
Mossy stone bricks are variant of stone bricks.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Infested blocks
	- 1.3 Natural generation
	- 1.4 Crafting
- 2 Usage
	- 2.1 Crafting ingredient
	- 2.2 Stonecutting
	- 2.3 Note Blocks
	- 2.4 Silverfish
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 Gallery
	- 7.1 Screenshots
- 8 See also
- 9 References

## Obtaining
### Breaking
Mossy stone bricks can be mined using any pickaxe. If mined without a pickaxe, they drop nothing.

| Block     | Mossy Stone Bricks    |
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

### Infested blocks
Mossy stone bricks can also be obtained by mining its respective infested block with Silk Touch.

### Natural generation
Mossy stone bricks generate as part of strongholds, making up some of the walls, ceilings, and floors. They can also generate as part of ocean ruins and ruined portals.

### Crafting
| Name               | Ingredients                  | Crafting recipe |
|--------------------|------------------------------|-----------------|
| Mossy Stone Bricks | Stone Bricks+<br/>Vines      |                 |
| Mossy Stone Bricks | Stone Bricks+<br/>Moss Block |                 |

## Usage
As mossy stone bricks offer no real advantage over stone or cobblestone, their main use is for decoration.

### Crafting ingredient
| Name                     | Ingredients        | Crafting recipe |
|--------------------------|--------------------|-----------------|
| Mossy Stone Brick Slab   | Mossy Stone Bricks | 6               |
| Mossy Stone Brick Stairs | Mossy Stone Bricks | 4               |
| Mossy Stone Brick Wall   | Mossy Stone Bricks | 6               |

### Stonecutting
| Ingredients        | Cutting recipe |
|--------------------|----------------|
| Mossy Stone Bricks | 2              |

### Note Blocks
Mossy stone bricks can be placed under note blocks to produce "bass drum" sounds.

### Silverfish
Silverfish have the ability to enter and hide in mossy stone bricks, creating an infested block of the corresponding type.

## Data values
### ID
Java Edition:

| Name               | Identifier           | Form         | Block tags     | Item tags      | Translation key                      |
|--------------------|----------------------|--------------|----------------|----------------|--------------------------------------|
| Mossy Stone Bricks | `mossy_stone_bricks` | Block & Item | `stone_bricks` | `stone_bricks` | `block.minecraft.mossy_stone_bricks` |

Bedrock Edition:

| Name               | Identifier   | Numeric ID | Form                       | Item ID[i 1]   | Translation key              |
|--------------------|--------------|------------|----------------------------|----------------|------------------------------|
| Mossy Stone Bricks | `stonebrick` | `98`       | Block & Giveable Item[i 2] | Identical[i 3] | `tile.stonebrick.mossy.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

Bedrock Edition

| Name             | Metadata Bits             | Default value | Allowed values | Values forMetadata Bits | Description                                                |
|------------------|---------------------------|---------------|----------------|-------------------------|------------------------------------------------------------|
| stone_brick_type | `0x1`<br/>`0x2`<br/>`0x4` | `default`     | `default`      | `0`                     | Stone Bricks                                               |
|                  |                           |               | `mossy`        | `1`                     | Mossy Stone Bricks                                         |
|                  |                           |               | `cracked`      | `2`                     | Cracked Stone Bricks                                       |
|                  |                           |               | `chiseled`     | `3`                     | Chiseled Stone Bricks                                      |
|                  |                           |               | `smooth`       | `4`                     | Smooth Stone Bricks (unused, same texture as regular ones) |



