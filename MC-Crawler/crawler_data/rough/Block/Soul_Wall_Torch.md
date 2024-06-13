# Soul Torch
Soul torches are non-solid blocks that emit light. They are a variant of the torch crafted with the addition of soul soil or soul sand.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Chest loot
	- 1.3 Crafting
- 2 Usage
	- 2.1 Light
	- 2.2 Piglins
	- 2.3 Crafting ingredient
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 Gallery
	- 7.1 Renders
- 8 See also
- 9 References

## Obtaining
### Breaking
Soul torches can be broken instantly using anything, and drop themselves as an item.

A soul torch is removed and drops itself as an item if:

- Its attachment block is moved, removed, or destroyed
- Waterorlavaflows into its space
- Apistonpushes it or moves a block into its space

### Chest loot
| Item       | Structure    | Container | Quantity | Chance                         |
|------------|--------------|-----------|----------|--------------------------------|
|            |              |           |          | Java EditionandBedrock Edition |
| Soul Torch | Ancient City | Chest     | 1–15     | 35.9%                          |

### Crafting
| Ingredients                                                   | Crafting recipe |
|---------------------------------------------------------------|-----------------|
| Coalor<br/>Charcoal+<br/>Stick+<br/>Soul Soilor<br/>Soul Sand | 4               |

## Usage
Soul torches in various positions on chiseled stone bricks.
Soul torches can be placed on the top or the sides of most solid blocks, although some blocks require sneaking. Being non-solid, soul torches have no collision box. More information about placement can be found at Opacity/Placement.

Gravity-affected blocks like sand and gravel will not start falling if the space immediately beneath is occupied by a soul torch. Falling blocks break if they fall onto a solid block with a soul torch above it. If there is an air block under the soul torch, the falling blocks fall through the soul torch onto the surface below.[1]

### Light
Soul torches give off a light level of 10. Due to their lower light level, soul torches do not melt snow or ice.

### Piglins
Soul torches repel piglins.

### Crafting ingredient
| Name         | Ingredients                 | Crafting recipe |
|--------------|-----------------------------|-----------------|
| Soul Lantern | Iron Nugget+<br/>Soul Torch |                 |

## Data values
### ID
Java Edition:

| Name            | Identifier        | Form         | Block tags                                   | Item tags           | Translation key                   |
|-----------------|-------------------|--------------|----------------------------------------------|---------------------|-----------------------------------|
| Soul Torch      | `soul_torch`      | Block & Item | `piglin_repellents`<br/>`wall_post_override` | `piglin_repellents` | `block.minecraft.soul_torch`      |
| Soul Wall Torch | `soul_wall_torch` | Block        | `piglin_repellents`                          | —                   | `block.minecraft.soul_wall_torch` |

Bedrock Edition:

| Name       | Identifier   | Numeric ID | Form                       | Item ID[i 1]   | Translation key        |
|------------|--------------|------------|----------------------------|----------------|------------------------|
| Soul Torch | `soul_torch` | `523`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.soul_torch.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

Java Edition:
Wall

| Name   | Default value | Allowed values                            | Description                                   |
|--------|---------------|-------------------------------------------|-----------------------------------------------|
| facing | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the top of the torch is facing. |

Bedrock Edition:

| Name                   | Metadata Bits             | Default value | Allowed values                                      | Values forMetadata Bits             | Description                                                                                                                                  |
|------------------------|---------------------------|---------------|-----------------------------------------------------|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| torch_facing_direction | `0x1`<br/>`0x2`<br/>`0x4` | `west`        | `west`<br/>`east`<br/>`north`<br/>`south`<br/>`top` | `1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | The face of the block that the torch is attached to. If the torch is a wall torch, the top of the torch faces opposite to this direction.[2] |
|                        |                           |               | `unknown`                                           | `0`                                 | Unused                                                                                                                                       |



