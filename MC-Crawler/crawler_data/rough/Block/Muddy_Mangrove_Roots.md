# Muddy Mangrove Roots
Muddy mangrove roots are a decorative variant of mangrove roots with dirt-like properties.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Crafting
	- 1.4 Post-generation
- 2 Usage
	- 2.1 Farming
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues

## Obtaining
### Breaking
Muddy mangrove roots can be broken by hand, but using a shovel speeds up the process. Muddy mangrove roots drop themselves when broken with any tool.

| Block     | Muddy mangrove roots  |
|-----------|-----------------------|
| Hardness  | 0.7                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 1.05                  |
| Wooden    | 0.55                  |
| Stone     | 0.3                   |
| Iron      | 0.2                   |
| Diamond   | 0.15                  |
| Netherite | 0.15                  |
| Golden    | 0.1                   |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Natural generation
Muddy mangrove roots naturally generate in mangrove swamps where mud blocks intersect with normal mangrove roots at the bottom of mangrove trees.


### Crafting
| Ingredients             | Crafting recipe |
|-------------------------|-----------------|
| Mud+<br/>Mangrove Roots |                 |

### Post-generation
When a mangrove propagule grows into a tree, if the tree roots intersect with nearby mud blocks, those mud blocks are converted into muddy mangrove roots.

## Usage
Muddy mangrove roots are primarily used as decoration. They are orientable and can be rotated on any axis, facing perpendicular to whichever side of a block they are placed on.

### Farming
Muddy mangrove roots have the ability to grow saplings, sugar cane, sweet berries, and bamboo, which can be planted directly on them under appropriate conditions. Saplings convert muddy mangrove roots into dirt when grown,‌[Bedrock Edition  only] and azalea trees grown on muddy mangrove roots convert them into rooted dirt.

## Data values
### ID
Java Edition:

| Name                 | Identifier             | Form         | Block tags                                                 | Translation key                        |
|----------------------|------------------------|--------------|------------------------------------------------------------|----------------------------------------|
| Muddy Mangrove Roots | `muddy_mangrove_roots` | Block & Item | `dirt`<br/>`mineable/shovel`<br/>`#sniffer_diggable_block` | `block.minecraft.muddy_mangrove_roots` |

Bedrock Edition:

| Name                 | Identifier             | Numeric ID | Form                       | Item ID[i 1]   | Translation key                  |
|----------------------|------------------------|------------|----------------------------|----------------|----------------------------------|
| Muddy Mangrove Roots | `muddy_mangrove_roots` | `-483`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.muddy_mangrove_roots.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

Java Edition:

| Name | Default value | Allowed values | Description                                       |
|------|---------------|----------------|---------------------------------------------------|
| axis | `y`           | `x`            | The muddy mangrove roots is oriented east–west.   |
|      |               | `y`            | The muddy mangrove roots is oriented vertically.  |
|      |               | `z`            | The muddy mangrove roots is oriented north–south. |

Bedrock Edition:

| Name        | Metadata Bits   | Default value | Allowed values | Values forMetadata Bits | Description                                       |
|-------------|-----------------|---------------|----------------|-------------------------|---------------------------------------------------|
| pillar_axis | `0x1`<br/>`0x2` | `y`           | `x`            | `1`                     | The muddy mangrove roots is oriented east–west.   |
|             |                 |               | `y`            | `0`                     | The muddy mangrove roots is oriented vertically.  |
|             |                 |               | `z`            | `2`                     | The muddy mangrove roots is oriented north–south. |

