# Underwater Torch
An underwater torch is a non-solid block that emits light underwater.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Crafting
- 2 Usage
	- 2.1 Placement
	- 2.2 Light
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 Gallery
	- 7.1 Renders
- 8 Trivia
- 9 See also

## Obtaining
### Breaking
Unlike a normal torch, an underwater torch does not break if water occupies its space.

Like normal torches, an underwater torch breaks instantly and drops itself when broken using anything. The tool does not lose durability when breaking the underwater torch.

Underwater torches are also broken if pushed by a piston.

### Crafting
| Ingredients          | Crafting recipe |
|----------------------|-----------------|
| Magnesium+<br/>Torch |                 |

As with any torch, an underwater torch can be crafted with coal or charcoal. The player can also use a torch from the creative menu.[verify]

## Usage
An underwater torch can be used exactly like a normal torch, only it can be underwater.

- Underwater torches can be placed on the top or the sides of most solid blocks, although some requiresneaking(seeplacementfor exceptions). Being non-solid, an underwater torch has no collision box.
- Gravity-affected blocks likesandandgraveldo not fall if the block below them has an underwater torch on it, and they break if they fall onto an underwater torch.

### Placement
In general, underwater torches can be placed only on solid, opaque, and full blocks; exceptions are listed below.

| Block name       | Underwater torch placeable |
|------------------|----------------------------|
| Slab             | Top of top-half slabs      |
| Fence            | Top only                   |
| Cobblestone Wall | Top only                   |
| Glass            | Yes                        |
| Stained Glass    | Yes                        |
| Hopper           | Top only                   |
| Snow             | Top of 8-layer thick snow  |
| Soul Sand        | Yes                        |
| Piston           | Yes                        |
| Monster Spawner  | Yes                        |

### Light
Underwater torches emit a light level of 14. Underwater torches also melt snow layers and ice within 2 blocks (taxicab distance).

## Data values
### ID
| Name             | Identifier         | Numeric ID | Form                       | Item ID[i 1]   | Translation key              |
|------------------|--------------------|------------|----------------------------|----------------|------------------------------|
| Underwater Torch | `underwater_torch` | `239`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.underwater_torch.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block states

| Name                   | Metadata Bits             | Default value | Allowed values                                      | Values forMetadata Bits             | Description                                                                                                                                  |
|------------------------|---------------------------|---------------|-----------------------------------------------------|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| torch_facing_direction | `0x1`<br/>`0x2`<br/>`0x4` | `west`        | `west`<br/>`east`<br/>`north`<br/>`south`<br/>`top` | `1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | The face of the block that the torch is attached to. If the torch is a wall torch, the top of the torch faces opposite to this direction.[1] |
|                        |                           |               | `unknown`                                           | `0`                                 | Unused                                                                                                                                       |




