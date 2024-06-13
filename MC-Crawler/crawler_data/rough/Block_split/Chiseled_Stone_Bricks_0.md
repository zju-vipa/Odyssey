# Chiseled Stone Bricks
Chiseled stone bricks are a variant of stone bricks, crafted from stone brick slabs.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Infested blocks
	- 1.3 Natural generation
	- 1.4 Crafting
	- 1.5 Stonecutting
	- 1.6 Trading
- 2 Usage
	- 2.1 Crafting ingredient
	- 2.2 Note blocks
	- 2.3 Silverfish
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
Chiseled stone bricks can be mined using any pickaxe. If mined without a pickaxe, they drop nothing.

| Block     | Chiseled Stone Bricks |
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
Chiseled stone bricks can also be obtained by mining its respective infested block with Silk Touch.

### Natural generation
Chiseled stone bricks can generate as part of ocean ruins and ruined portals. In addition, three chiseled stone bricks generate as part of each jungle temple. 

### Crafting
| Ingredients      | Crafting recipe |
|------------------|-----------------|
| Stone Brick Slab |                 |

### Stonecutting
| Name                                     | Ingredients  | Cutting recipe | Description              |
|------------------------------------------|--------------|----------------|--------------------------|
| Stone Bricksor<br/>Chiseled Stone Bricks | Stone        |                |                          |
| Chiseled Stone Bricks                    | Stone Bricks |                | ‌[Java Edition  only][1] |

### Trading
Apprentice-level stone mason villagers sell 4 chiseled stone bricks for one emerald as part of their trades.‌[Java Edition  only]

Apprentice-level stone mason villagers have a 25% (1⁄4) chance to sell 4 chiseled stone bricks for one emerald as part of their trades.‌[Bedrock Edition  only]

## Usage
As stone bricks offer no real advantage over stone or cobblestone, their main use is for decoration.

### Crafting ingredient
| Name      | Ingredients                                | Crafting recipe |
|-----------|--------------------------------------------|-----------------|
| Lodestone | Chiseled Stone Bricks+<br/>Netherite Ingot |                 |

### Note blocks
Chiseled stone bricks can be placed under note blocks to produce "bass drum" sounds.

### Silverfish
Silverfish have the ability to enter and hide in chiseled stone bricks, creating an infested block of the corresponding type.

## Data values
### ID
Java Edition:

| Name                  | Identifier              | Form         | Block tags     | Item tags      | Translation key                         |
|-----------------------|-------------------------|--------------|----------------|----------------|-----------------------------------------|
| Chiseled Stone Bricks | `chiseled_stone_bricks` | Block & Item | `stone_bricks` | `stone_bricks` | `block.minecraft.chiseled_stone_bricks` |

Bedrock Edition:

| Name                  | Identifier   | Numeric ID | Form                       | Item ID[i 1]   | Translation key                 |
|-----------------------|--------------|------------|----------------------------|----------------|---------------------------------|
| Chiseled Stone Bricks | `stonebrick` | `98`       | Block & Giveable Item[i 2] | Identical[i 3] | `tile.stonebrick.chiseled.name` |

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




