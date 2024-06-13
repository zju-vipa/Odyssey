# Slab
A slab is a half-height version of its respective block. 

## Contents
- 1 Variants
- 2 Obtaining
	- 2.1 Crafting
	- 2.2 Stonecutting
- 3 Usage
	- 3.1 Placement
	- 3.2 Behavior
- 4 Block states
- 5 History
	- 5.1 Data history
	- 5.2 Double slab "items"
		- 5.2.1 Appearances
			- 5.2.1.1 Smooth Stone Double Slab
		- 5.2.2 Names
- 6 Issues
- 7 Trivia
- 8 References

## Variants
There are 56 (59‌[upcoming: JE 1.21 & BE 1.21.0]) variants of slabs:

- Wooden Slab
	- Oak Slab
	- Spruce Slab
	- Birch Slab
	- Jungle Slab
	- Acacia Slab
	- Dark Oak Slab
	- Mangrove Slab
	- Cherry Slab
	- Bamboo Slab
	- Crimson Slab
	- Warped Slab
- Bamboo Mosaic Slab
- Stone Slab
- Cobblestone Slab
- Mossy Cobblestone Slab
- Smooth Stone Slab
- Stone Brick Slab
- Mossy Stone Brick Slab
- Granite Slab
- Polished Granite Slab
- Diorite Slab
- Polished Diorite Slab
- Andesite Slab
- Polished Andesite Slab
- Cobbled Deepslate Slab
- Polished Deepslate Slab
- Deepslate Brick Slab
- Deepslate Tile Slab
- Tuff Slab‌[upcoming: JE 1.21 & BE 1.21.0]
- Polished Tuff Slab‌[upcoming: JE 1.21 & BE 1.21.0]
- Tuff Brick Slab‌[upcoming: JE 1.21 & BE 1.21.0]
- Brick Slab
- Mud Brick Slab
- Sandstone Slab
- Smooth Sandstone Slab
- Cut Sandstone Slab
- Red Sandstone Slab
- Smooth Red Sandstone Slab
- Cut Red Sandstone Slab
- Prismarine Slab
- Prismarine Brick Slab
- Dark Prismarine Slab
- Nether Brick Slab
- Red Nether Brick Slab
- Blackstone Slab
- Polished Blackstone Slab
- Polished Blackstone Brick Slab
- End Stone Brick Slab
- Purpur Slab
- Quartz Slab
- Smooth Quartz Slab
- Cut Copper Slab
	- Unoxidized Cut Copper Slab(Waxed)
	- Exposed Cut Copper Slab(Waxed)
	- Weathered Cut Copper Slab(Waxed)
	- Oxidized Cut Copper Slab(Waxed)

## Obtaining
### Crafting
All slabs have the same crafting recipe format, with one block resulting in two slabs each.

| Ingredients                                                                                            | Crafting recipe                                             |
|--------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| Planks,Bamboo Mosaic,<br/>stone blocks, brick blocks,<br/>Quartz Block,Smooth Quartz,<br/>orCut Copper | 66666666666666666666666666666666666666666666666666666666666 |

### Stonecutting
All slabs except wooden slabs and bamboo mosaic slabs can be obtained by stonecutting, at the same rate as with crafting.

| Ingredients                                                                | Cutting recipe                                      |
|----------------------------------------------------------------------------|-----------------------------------------------------|
| Stone block, brick block,<br/>Quartz Block,Smooth Quartz,<br/>orCut Copper | 222222222222222222222222222222222222222222222222222 |

## Usage
### Placement
Slabs can occupy either the top half or the bottom half of a block, or both:

- Placing a slab on top of ablockor on the side of a block in the lower half of the side surface creates a bottom slab.
- Placing a slab on the underside of a block or on the top half of the side surface creates a top slab.
- Placing a top and bottom slab of the same type in the same block creates a double slab block.
- It is impossible to place two different kinds of slabs in the same block.

Slabs cannot be oriented vertically.

### Behavior
An example of how top slabs can make redstone travel compactly "up stairs".
Slabs do not block a vertical redstone connection as it is a transparent block.
A player sneaking under a slab.
In Bedrock Edition a single slab (top or bottom) is transparent to light and diffuses sky light, while a double slab is opaque. The empty half of a slab block is also transparent to mobs, unlike other transparent blocks such as fences and glass, which players can see through but mobs cannot.

A bottom placed on top of a hopper is transparent to items; the items fall through the bottom slab into the hopper. Without a hopper attached below, a bottom slab behaves as a solid surface.

Falling block entities (like sand, gravel, and concrete powder) turn into their dropped form if they land on a bottom slab, as when they fall on a torch.

Mobs see a slab as a full block when pathfinding. They can spawn on top slabs and double slabs, but not on bottom slabs. This can be used to prevent mob spawning in certain areas, such as mob farms.

Generally, the top face of top slabs, the bottom face of bottom slabs, and all faces of double slabs are handled as solid blocks. Due to this, blocks that require a solid surface for placement can be placed on these faces.

Double slabs are handled as a single block instead of two different slabs; as such, breaking one destroys the whole block and drop two slabs, as opposed to breaking only one slab within the block. "Double slabs" that are not aligned to the grid (i.e. a bottom slab on top of a top slab) are handled as separate blocks and are broken individually.

Redstone dust placed on a top slab receives signals from redstone dust one block lower and adjacent, but cannot transmit signals down to that block.

Due to the way blast rays propagate from an explosion, bottom slabs provide extremely effective absorption to explosions directly on top of them. In some cases, only the slab is destroyed from a TNT explosion directly on top of it. Explosions from end crystals and creepers are also weakened.

Sneaking reduces the player's hitbox height to 1.5 blocks, allowing the player to fit through such a gap (for example, walking over a bottom slab with one block of air above it, or in a two block high tunnel with an upper slab on the ceiling). A player cannot walk from a block of soul sand directly up to a bottom slab without jumping – this applies not just to soul sand, but to any block 7⁄8 of a block high or shorter, because the maximum step height of the player is 0.6 of a block. The player can walk off a bottom slab while sneaking, because the sneaking prevents falling only when the distance is higher than one half block.

If a single slab is placed in a water source block, or water is placed onto a single slab using a water bucket, the empty half of that slab's block is waterlogged. If a slab is placed in flowing water, a pocket of air is created in the unfilled half of the block. If the player's head is in this pocket, the player can breathe and see as clearly as from an air block. In Java Edition, if a single slab is placed in between two water sources or waterlogged blocks, the slab becomes waterlogged.

A minecart on powered rails is not repelled by a slab, although it is repelled by a slab with a minecart on top.

## Block states
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



