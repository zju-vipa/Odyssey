# Torch
Torches are non-solid blocks that emit light.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Chest loot
	- 1.4 Crafting
	- 1.5 Post-generation
- 2 Usage
	- 2.1 Light
	- 2.2 Crafting ingredient
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 Gallery
	- 7.1 Renders
	- 7.2 Screenshots
	- 7.3 In other media
- 8 See also
- 9 References
- 10 External links

## Obtaining
### Breaking
Torches can be broken instantly using anything, and drop themselves as an item.

A torch is removed and drops itself as an item if:

- Its attachment block is moved, removed, or destroyed
- Waterorlavaflows into its space
- Apistonpushes it or moves a block into its space

### Natural generation
Torches can be found generated among the supports in a mineshaft's corridors, as part of village lamp posts and most houses, in various rooms in strongholds, in the basements of igloos, in woodland mansions, and atop pillager outposts. Torches also generate around bonus chests if each side has a block at the same height around it. In the End, four torches generate as part of the exit portal, around the second bedrock block from the top. Torches also generate in ancient cities.


### Chest loot
| Item  | Structure      | Container           | Quantity | Chance                         |
|-------|----------------|---------------------|----------|--------------------------------|
|       |                |                     |          | Java EditionandBedrock Edition |
| Torch | Mineshaft      | Chest               | 1–16     | 65.7%                          |
|       | Trial Chambers | Supply chest        | 3–6      | 20.4%                          |
|       |                | Corridor chest      | 3–6      | 19.6%                          |
|       | Village        | Savanna house chest | 1–2      | 11.3%                          |

### Crafting
| Ingredients                    | Crafting recipe |
|--------------------------------|-----------------|
| Coalor<br/>Charcoal+<br/>Stick | 4               |

### Post-generation
When the ender dragon dies or is re-summoned using end crystals, the four torches on the exit portal regenerate. If the original torches are still in position, they drop as items, and the new torches take their place.

## Usage
Torches in various positions on chiseled stone bricks.
Torches can be placed on the top or the sides of most solid blocks, although some blocks require sneaking. Being non-solid, torches have no collision box. More information about placement can be found at Opacity/Placement.

Gravity-affected blocks like sand and gravel will not start falling if the space immediately beneath is occupied by a torch. Falling blocks break if they fall onto a solid block with a torch above it. If there is an air block under the torch, the falling blocks fall through the torch onto the surface below.[1]

### Light
Torches give off a light level of 14. Torches also melt snow layers within 2 blocks and ice within 3 blocks (taxicab distance).

### Crafting ingredient
| Name                                                            | Ingredients                                                                                         | Crafting recipe | Description                                                                                                                                                       |
|-----------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Blue Torchor<br/>Red Torchor<br/>Purple Torchor<br/>Green Torch | Cerium Chlorideor<br/>Mercuric Chlorideor<br/>Potassium Chlorideor<br/>Tungsten Chloride+<br/>Torch |                 | Cerium Chloride: Blue<br/>Mercuric Chloride: Red<br/>Potassium Chloride: Purple<br/>Tungsten Chloride: Green<br/>‌[Bedrock Edition and Minecraft Education  only] |
| Jack o'Lantern                                                  | Carved Pumpkin+<br/>Torch                                                                           |                 |                                                                                                                                                                   |
| Lantern                                                         | Iron Nugget+<br/>Torch                                                                              |                 |                                                                                                                                                                   |
| Underwater Torch                                                | Magnesium+<br/>Torch                                                                                |                 | ‌[Bedrock Edition and Minecraft Education  only]                                                                                                                  |

## Data values
### ID
Java Edition:

| Name       | Identifier   | Form         | Block tags           | Item tags | Translation key              |
|------------|--------------|--------------|----------------------|-----------|------------------------------|
| Torch      | `torch`      | Block & Item | `wall_post_override` | None      | `block.minecraft.torch`      |
| Wall Torch | `wall_torch` | Block        | None                 | —         | `block.minecraft.wall_torch` |

Bedrock Edition:

| Name  | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key   |
|-------|------------|------------|----------------------------|----------------|-------------------|
| Torch | `torch`    | `50`       | Block & Giveable Item[i 2] | Identical[i 3] | `tile.torch.name` |

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




