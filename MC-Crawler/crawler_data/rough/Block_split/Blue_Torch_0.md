# Colored Torch
Colored torches are torches colored by metal chlorides, available in blue, red, purple, and green.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Crafting
- 2 Usage
	- 2.1 Light
	- 2.2 Placement
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Metadata
	- 4.3 Block states
- 5 History
- 6 Trivia
- 7 Gallery
	- 7.1 Renders
- 8 See also

## Obtaining
### Breaking
Colored torches break instantly and drop itself when broken using anything. The tool does not take any damage.
Colored torches are also broken if pushed by a piston.

### Crafting
| Ingredients                                                                                         | Crafting recipe | Description                                                                                                                                                       |
|-----------------------------------------------------------------------------------------------------|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Cerium Chlorideor<br/>Mercuric Chlorideor<br/>Potassium Chlorideor<br/>Tungsten Chloride+<br/>Torch |                 | Cerium Chloride: Blue<br/>Mercuric Chloride: Red<br/>Potassium Chloride: Purple<br/>Tungsten Chloride: Green<br/>‌[Bedrock Edition and Minecraft Education  only] |

## Usage
Torches can be placed on the top or the sides of most solid blocks, although some require sneaking (see placement for exceptions). Being non-solid, torches have no collision box.

Gravity-affected blocks like sand and gravel do not fall if the block below them has a torch on it and break when falling onto a torch.

### Light
Torches emit a light level of 14. Torches also melt snow layers within 2 blocks and ice within 3 blocks (taxicab distance). Colored torches emit normal light, not colored light, and therefore the coloring is purely aesthetic.

### Placement
In general, torches can be placed only on solid, opaque, full blocks; exceptions are listed below.

| Block name       | Torch placeable           |
|------------------|---------------------------|
| Slab             | Top of top-half slabs     |
| Fence            | Top only                  |
| Cobblestone Wall | Top only                  |
| Glass            | Yes                       |
| Stained Glass    | Yes                       |
| Hopper           | Top only                  |
| Snow             | Top of 8-layer thick snow |
| Soul Sand        | Yes                       |
| Piston           | Yes                       |
| Monster Spawner  | Yes                       |

## Data values
### ID
| Name                  | Identifier         | Numeric ID | Form                       | Item ID[i 1]   | Translation key                                                     |
|-----------------------|--------------------|------------|----------------------------|----------------|---------------------------------------------------------------------|
| Red and green torch   | `colored_torch_rg` | `202`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.colored_torch.red.name`<br/>`tile.colored_torch.green.name`   |
| Blue and purple torch | `colored_torch_bp` | `204`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.colored_torch.blue.name`<br/>`tile.colored_torch.purple.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑ a bAvailable with /give command.
3. ↑ a bThe block's direct item form has the same id as the block.

### Metadata
Colored torches have the following data values:
Colored torch (red/green)

|  | DV | Description |
|--|----|-------------|
|  | 0  | Red Torch   |
|  | 1  | Green Torch |

Colored torch (blue/purple)

|  | DV | Description  |
|--|----|--------------|
|  | 0  | Blue Torch   |
|  | 1  | Purple Torch |

### Block states
See also: Block states

| Name                   | Default value | Allowed values                                                    | Description                                                                                        |
|------------------------|---------------|-------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| color_bit              | `0`           | `0`<br/>`1`                                                       | What color the torch is.<br/>For`rg`0 is red and 1 is green.<br/>For`bp`0 is blue and 1 is purple. |
| torch_facing_direction | `top`         | `east`<br/>`north`<br/>`south`<br/>`top`<br/>`unknown`<br/>`west` | The direction the top of the torch is facing.                                                      |




