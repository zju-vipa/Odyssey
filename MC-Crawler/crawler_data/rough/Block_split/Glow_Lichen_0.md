# Glow Lichen
A glow lichen is a non-solid, light-emitting block. It can generate, or be placed, on any side of a solid block.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Post-generation
- 2 Usage
	- 2.1 Light
	- 2.2 Placement
	- 2.3 Composting
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 Trivia
- 8 Gallery
	- 8.1 Renders
	- 8.2 Screenshots
- 9 References

## Obtaining
See also: Tutorials/Glow lichen farming

### Breaking
Glow lichen can be destroyed with anything, most efficiently with an axe. However, using shears is the only way to obtain glow lichen. Enchanting shears with Efficiency II allows for instant mining.

| Block     | Glow Lichen           |
|-----------|-----------------------|
| Hardness  | 0.2                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 0.3                   |
| Wooden    | 0.15                  |
| Stone     | 0.1                   |
| Iron      | 0.05                  |
| Diamond   | 0.05                  |
| Netherite | 0.05                  |
| Golden    | 0.05                  |
| Shears    | 0.3                   |
| Sword     | 0.2                   |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Natural generation
Glow lichen generates naturally in the interior of caves (at any height) on the surface of stone, andesite, diorite, granite, calcite, tuff, deepslate, and dripstone blocks that are exposed to air or water sources.[more information needed] It can be found underwater, but cannot generate in the deep dark biome.


### Post-generation
Using bone meal causes glow lichen to spread to a random adjacent block if possible, otherwise the bone meal is not consumed. By fertilizing one lichen with bone meal, it is possible to cover the sides and the top of an adjacent block, but not the back. Otherwise, glow lichen does not spread naturally.

## Usage
### Light
Glow lichen emits a light level of 7.

### Placement
Multiple glow lichens can be placed in the area of one solid block, such as covering three sides of a corner. When such glow lichens are mined, all glow lichens occupying the same block are also mined. Mining with shears causes all glow lichens in the block to drop.

Glow lichens cannot be broken by flowing water or lava,[1][2] similar to signs. Therefore, they may be used to control the flow of these fluids.

### Composting
Placing a glow lichen into a composter has a 50% chance of raising the compost level by 1.

## Data values
### ID
| Name        | Identifier    | Form         | Translation key               |
|-------------|---------------|--------------|-------------------------------|
| Glow Lichen | `glow_lichen` | Block & Item | `block.minecraft.glow_lichen` |

Bedrock Edition:

| Name        | Identifier    | Numeric ID | Form                       | Item ID[i 1]   | Translation key         |
|-------------|---------------|------------|----------------------------|----------------|-------------------------|
| Glow Lichen | `glow_lichen` | `666`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.glow_lichen.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
See also: Block state

Java Edition:

| Name        | Default value | Allowed values     | Description                                                         |
|-------------|---------------|--------------------|---------------------------------------------------------------------|
| down        | `false`       | `false`<br/>`true` | When true, a glow lichen texture is displayed on the bottom.        |
| east        | `false`       | `false`<br/>`true` | When true, a glow lichen texture is displayed on the east.          |
| north       | `false`       | `false`<br/>`true` | When true, a glow lichen texture is displayed on the north.         |
| south       | `false`       | `false`<br/>`true` | When true, a glow lichen texture is displayed on the south.         |
| up          | `false`       | `false`<br/>`true` | When true, a glow lichen texture is displayed on the top.           |
| waterlogged | `false`       | `false`<br/>`true` | Whether or not there's water in the same place as this glow lichen. |
| west        | `false`       | `false`<br/>`true` | When true, a glow lichen texture is displayed on the west.          |

Bedrock Edition:

| Name                      | Metadata Bits                                             | Default value | Allowed values | Values forMetadata Bits | Description                                                                                                                                                                                        |
|---------------------------|-----------------------------------------------------------|---------------|----------------|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| multi_face_direction_bits | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8`<br/>`0x10`<br/>`0x20` | `0`           | `0 to 63`      | `0 to 63`               | The directions the glow lichen exists. Each bit determines one direction:0x1: Down<br/>0x2: Up<br/>0x4: South<br/>0x8: West<br/>0x10: North<br/>0x20: East<br/>0 is unused and it behaves like 63. |


