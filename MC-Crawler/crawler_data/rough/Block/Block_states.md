# Block states
Block states (also known as block properties)[1] are extra pieces of data that further define a block, such as how it appears or behaves.

In Bedrock Edition, there are also aux values (also known as Metadata) to define a block. Aux values are in the format of binary flags, which basically match the block states one-to-one. And they are accessible in decimal number in commands. However, aux values are intended to be deprecated, and newly added blocks or block states no longer support aux values.

In Java Edition, there are also fluid states, that further define a fluid as to how it behaves.

## Contents
- 1 List of block states
	- 1.1 Anvils
	- 1.2 Amethyst Buds and Amethyst Cluster
	- 1.3 Bamboo
	- 1.4 Banners
	- 1.5 Barrel
	- 1.6 Basalt and Polished Basalt
	- 1.7 Beds
	- 1.8 Bedrock
	- 1.9 Beehive and Bee Nest
	- 1.10 Beetroots
	- 1.11 Bell
	- 1.12 Big Dripleaf
	- 1.13 Blast Furnace
	- 1.14 Block of Bamboo and Block of Stripped Bamboo
	- 1.15 Bone Block
	- 1.16 Border
	- 1.17 Brewing Stand
	- 1.18 Bubble Column
	- 1.19 Buttons
	- 1.20 Cactus
	- 1.21 Cake
	- 1.22 Campfire
	- 1.23 Candles
	- 1.24 Carrots
	- 1.25 Cauldron
	- 1.26 Cave Vines
	- 1.27 Chain
	- 1.28 Chemistry Table
	- 1.29 Chests
		- 1.29.1 Chest and Trapped Chest
		- 1.29.2 Ender Chest
	- 1.30 Chiseled Bookshelf
	- 1.31 Chorus Flower
	- 1.32 Chorus Plant
	- 1.33 Cocoa
	- 1.34 Command Blocks
	- 1.35 Composter
	- 1.36 Conduit
	- 1.37 Coral
	- 1.38 Coral Block
	- 1.39 Coral Fan
	- 1.40 Daylight Detector
	- 1.41 Deepslate
	- 1.42 Dirt
	- 1.43 Dispenser and Dropper
	- 1.44 Doors
	- 1.45 End Portal Frame
	- 1.46 End Rod
	- 1.47 Farmland
	- 1.48 Fences
	- 1.49 Fence Gates
	- 1.50 Fire
	- 1.51 Flowers
	- 1.52 Flower Pot
	- 1.53 Froglight
	- 1.54 Frosted Ice
	- 1.55 Furnace
	- 1.56 Glass Panes
	- 1.57 Glazed Terracotta
	- 1.58 Glow Lichen
	- 1.59 Grass Block, Mycelium, and Podzol
	- 1.60 Grindstone
	- 1.61 Hay Bale
	- 1.62 Hopper
	- 1.63 Infested Block
	- 1.64 Iron Bars
	- 1.65 Item Frame and Glow Item Frame
	- 1.66 Jigsaw Block
	- 1.67 Jack o'Lantern
	- 1.68 Jukebox
	- 1.69 Kelp
	- 1.70 Ladder
	- 1.71 Lantern and Soul Lantern
	- 1.72 Lava
	- 1.73 Leaves
	- 1.74 Lectern
	- 1.75 Lever
	- 1.76 Light Block
	- 1.77 Lightning Rod
	- 1.78 Logs
	- 1.79 Loom
	- 1.80 Mangrove Roots
	- 1.81 Melon Stem
	- 1.82 Mob heads
	- 1.83 Muddy Mangrove Roots
	- 1.84 Mushroom Blocks
	- 1.85 Nether Wart
	- 1.86 Nether Portal
	- 1.87 Note Block
	- 1.88 Observer
	- 1.89 Pink Petals
	- 1.90 Pistons
		- 1.90.1 Moving piston
		- 1.90.2 Piston head
	- 1.91 Potatoes
	- 1.92 Pointed Dripstone
	- 1.93 Pressure Plates
	- 1.94 Prismarine
	- 1.95 Pumpkin and Carved Pumpkin
		- 1.95.1 Pumpkin Stem
	- 1.96 Purpur and Quartz Pillar
	- 1.97 Rails
		- 1.97.1 Rail
		- 1.97.2 Activator Rail, Detector Rail, and Powered Rail
	- 1.98 Redstone Comparator
	- 1.99 Redstone Dust
	- 1.100 Redstone Lamp
	- 1.101 Redstone Ore
	- 1.102 Redstone Repeater
	- 1.103 Redstone Torch
	- 1.104 Respawn Anchor
	- 1.105 Sand and Red Sand
	- 1.106 Sandstone and Red Sandstone
	- 1.107 Saplings
	- 1.108 Scaffolding
	- 1.109 Sculk Catalyst
	- 1.110 Sculk Sensor
	- 1.111 Sculk Shrieker
	- 1.112 Sculk Vein
	- 1.113 Sea Pickle
	- 1.114 Shulker Boxes
	- 1.115 Sign
	- 1.116 Slabs
	- 1.117 Small Dripleaf
	- 1.118 Smoker
	- 1.119 Snow
	- 1.120 Sponge
	- 1.121 Stairs
	- 1.122 Stone Bricks
	- 1.123 Stonecutter
	- 1.124 Structure Block
	- 1.125 Structure Void
	- 1.126 Sugar Cane
	- 1.127 Sweet Berry Bush
	- 1.128 Tall Grass and Large Fern
	- 1.129 Tall Seagrass
	- 1.130 Target
	- 1.131 TNT
	- 1.132 Torch and Soul Torch
	- 1.133 Trapdoors
	- 1.134 Tripwire
	- 1.135 Tripwire Hook
	- 1.136 Turtle Egg
	- 1.137 Twisting Vines
	- 1.138 Underwater Torch
	- 1.139 Vines
	- 1.140 Walls
	- 1.141 Water
	- 1.142 Weeping Vines
	- 1.143 Wheat crop
	- 1.144 Wood
- 2 List of fluid states
	- 2.1 Water
	- 2.2 Lava
- 3 History

## List of block states
### Anvils
Java Edition:

| Name   | Default value | Allowed values                            | Description                                                                                                                                                                                                                                                                   |
|--------|---------------|-------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | An anvil pointing north or south is aligned with its long dimension pointing north–south.<br/>An anvil pointing east or west is aligned with its long dimension pointing east–west.<br/>This value is 90° clockwise from the direction a player faces while placing an anvil. |

Bedrock Edition:

| Name                         | Metadata Bits   | Default value | Allowed values                            | Values forMetadata Bits | Description                                                                                                                                                                                                                                                                   |
|------------------------------|-----------------|---------------|-------------------------------------------|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| damage                       | `0x4`<br/>`0x8` | `undamaged`   | `broken`                                  | `3`                     | Broken Anvil (inaccessible and unused, uses anvil base texture)                                                                                                                                                                                                               |
|                              |                 |               | `slightly_damaged`                        | `1`                     | Slightly Damaged Anvil.                                                                                                                                                                                                                                                       |
|                              |                 |               | `undamaged`                               | `0`                     | Anvil.                                                                                                                                                                                                                                                                        |
|                              |                 |               | `very_damaged`                            | `2`                     | Very Damaged Anvil.                                                                                                                                                                                                                                                           |
| minecraft:cardinal_direction | Not Supported   | `south`       | `east`<br/>`north`<br/>`south`<br/>`west` | `Unsupported`           | An anvil pointing north or south is aligned with its long dimension pointing north–south.<br/>An anvil pointing east or west is aligned with its long dimension pointing east–west.<br/>This value is 90° clockwise from the direction a player faces while placing an anvil. |



### Amethyst Buds and Amethyst Cluster
Java Edition:

| Name        | Default value | Allowed values                                                | Description                                                        |
|-------------|---------------|---------------------------------------------------------------|--------------------------------------------------------------------|
| facing      | `up`          | `down`<br/>`east`<br/>`north`<br/>`south`<br/>`up`<br/>`west` | The direction the amethyst is facing, determined by its anchoring. |
| waterlogged | `false`       | `true`<br/>`false`                                            | Whether or not the amethyst is located inside ofwater.             |

Bedrock Edition:

| Name                 | Metadata Bits | Default value | Allowed values                                                | Values forMetadata Bits | Description                                                        |
|----------------------|---------------|---------------|---------------------------------------------------------------|-------------------------|--------------------------------------------------------------------|
| minecraft:block_face | Not Supported | `up`          | `down`<br/>`east`<br/>`north`<br/>`south`<br/>`up`<br/>`west` | `Unsupported`           | The direction the amethyst is facing, determined by its anchoring. |



### Bamboo
Java Edition:
Bamboo

| Name   | Default value | Allowed values                 | Description                                                                                                |
|--------|---------------|--------------------------------|------------------------------------------------------------------------------------------------------------|
| age    | `0`           | `0`<br/>`1`                    | The age of the bamboo, if this is 1 the bamboo appears thicker.                                            |
| leaves | `none`        | `large`<br/>`none`<br/>`small` | The size of the leaves on this bamboo block.                                                               |
| stage  | `0`           | `0`<br/>`1`                    | The stage is incremented at random intervals.<br/>At stage 1, bamboo may try to grow more bamboo above it. |

Bedrock Edition:
Bamboo:

| Name                   | Metadata Bits   | Default value | Allowed values                                    | Values forMetadata Bits | Description                                                                                               |
|------------------------|-----------------|---------------|---------------------------------------------------|-------------------------|-----------------------------------------------------------------------------------------------------------|
| age_bit                | `0x8`           | `false`       | `false`<br/>`true`                                | `0`<br/>`1`             | The stage is incremented at random intervals.<br/>When true, bamboo may try to grow more bamboo above it. |
| bamboo_leaf_size       | `0x2`<br/>`0x4` | `no_leaves`   | `no_leaves`<br/>`small_leaves`<br/>`large_leaves` | `0`<br/>`1`<br/>`2`     | The size of the leaves on this bamboo block.                                                              |
| bamboo_stalk_thickness | `0x1`           | `thin`        | `thin`<br/>`thick`                                | `0`<br/>`1`             | The thickness of the bamboo, if this is thick the bamboo appears thicker.                                 |

Bamboo Sapling:

| Name         | Metadata Bits | Default value | Allowed values                                                          | Values forMetadata Bits | Description                           |
|--------------|---------------|---------------|-------------------------------------------------------------------------|-------------------------|---------------------------------------|
| age_bit      | `0x1`         | `false`       | `false`<br/>`true`                                                      | `0`<br/>`1`             | Specifies the sapling's growth stage. |
| sapling_type | Not Supported | `oak`         | `acacia`<br/>`birch`<br/>`dark_oak`<br/>`jungle`<br/>`oak`<br/>`spruce` | `Unsupported`           | Unused.                               |



### Banners
Java Edition:
Floor

| Name     | Default value | Allowed values | Description                          |
|----------|---------------|----------------|--------------------------------------|
| rotation | `0`           | `0`            | The block is facing south.           |
|          |               | `1`            | The block is facing south-southwest. |
|          |               | `2`            | The block is facing southwest.       |
|          |               | `3`            | The block is facing west-southwest.  |
|          |               | `4`            | The block is facing west.            |
|          |               | `5`            | The block is facing west-northwest.  |
|          |               | `6`            | The block is facing northwest.       |
|          |               | `7`            | The block is facing north-northwest. |
|          |               | `8`            | The block is facing north.           |
|          |               | `9`            | The block is facing north-northeast. |
|          |               | `10`           | The block is facing northeast.       |
|          |               | `11`           | The block is facing east-northeast.  |
|          |               | `12`           | The block is facing east.            |
|          |               | `13`           | The block is facing east-southeast.  |
|          |               | `14`           | The block is facing southeast.       |
|          |               | `15`           | The block is facing south-southeast. |

Wall

| Name   | Default value | Allowed values                            | Description                                                                                                                                                                    |
|--------|---------------|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the block is facing. For example, a block facing east is attached to a block to its west.<br/>Opposite from the direction a player faces when placing the block. |

Bedrock Edition:

** Standing **
| Name                  | Metadata Bits                       | Default value | Allowed values | Values forMetadata Bits | Description                          |
|-----------------------|-------------------------------------|---------------|----------------|-------------------------|--------------------------------------|
| ground_sign_direction | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8` | `0`           | `0`            | `0`                     | The block is facing south.           |
|                       |                                     |               | `1`            | `1`                     | The block is facing south-southwest. |
|                       |                                     |               | `2`            | `2`                     | The block is facing southwest.       |
|                       |                                     |               | `3`            | `3`                     | The block is facing west-southwest.  |
|                       |                                     |               | `4`            | `4`                     | The block is facing west.            |
|                       |                                     |               | `5`            | `5`                     | The block is facing west-northwest.  |
|                       |                                     |               | `6`            | `6`                     | The block is facing northwest.       |
|                       |                                     |               | `7`            | `7`                     | The block is facing north-northwest. |
|                       |                                     |               | `8`            | `8`                     | The block is facing north.           |
|                       |                                     |               | `9`            | `9`                     | The block is facing north-northeast. |
|                       |                                     |               | `10`           | `10`                    | The block is facing northeast.       |
|                       |                                     |               | `11`           | `11`                    | The block is facing east-northeast.  |
|                       |                                     |               | `12`           | `12`                    | The block is facing east.            |
|                       |                                     |               | `13`           | `13`                    | The block is facing east-southeast.  |
|                       |                                     |               | `14`           | `14`                    | The block is facing southeast.       |
|                       |                                     |               | `15`           | `15`                    | The block is facing south-southeast. |

** Wall **
| Name             | Metadata Bits             | Default value | Allowed values              | Values forMetadata Bits     | Description                                                                                                                                               |
|------------------|---------------------------|---------------|-----------------------------|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing_direction | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `2`<br/>`3`<br/>`4`<br/>`5` | `2`<br/>`3`<br/>`4`<br/>`5` | The direction the block is facing. For example, a block facing east is attached to a block to its west.2: north<br/>3: south<br/>4: west<br/>5: east<br/> |
|                  |                           |               | `0`<br/>`1`                 | `0`<br/>`1`                 | Unused                                                                                                                                                    |

### Barrel
Java Edition:

| Name   | Default value | Allowed values                                                | Description                                                                                       |
|--------|---------------|---------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| facing | `north`       | `down`<br/>`east`<br/>`north`<br/>`south`<br/>`up`<br/>`west` | The direction the barrel is facing.                                                               |
| open   | `false`       | `false`<br/>`true`                                            | Whether the barrel is currently being looked at by a player; changes the texture on the top face. |

Bedrock Edition:

| Name             | Metadata Bits             | Default value | Allowed values                              | Values forMetadata Bits                     | Description                                                                                                                                                                               |
|------------------|---------------------------|---------------|---------------------------------------------|---------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing_direction | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | The direction the barrel is facing.0:Down facing barrel<br/>1:Up facing barrel<br/>2:East facing barrel<br/>3:West facing barrel<br/>4:South facing barrel<br/>5:North facing barrel<br/> |
| open_bit         | `0x8`                     | `0`           | `0`<br/>`1`                                 | `0`<br/>`1`                                 | Whether the barrel is currently being looked at by a player; changes the texture on the top face.                                                                                         |



### Basalt and Polished Basalt
Java Edition:

| Name | Default value | Allowed values | Description                         |
|------|---------------|----------------|-------------------------------------|
| axis | `y`           | `x`            | The basalt is oriented east–west.   |
|      |               | `y`            | The basalt is oriented vertically.  |
|      |               | `z`            | The basalt is oriented north–south. |

Bedrock Edition:

| Name        | Metadata Bits   | Default value | Allowed values | Values forMetadata Bits | Description                         |
|-------------|-----------------|---------------|----------------|-------------------------|-------------------------------------|
| pillar_axis | `0x1`<br/>`0x2` | `y`           | `x`            | `1`                     | The basalt is oriented east–west.   |
|             |                 |               | `y`            | `0`                     | The basalt is oriented vertically.  |
|             |                 |               | `z`            | `2`                     | The basalt is oriented north–south. |



### Beds
Java Edition:

| Name     | Default value | Allowed values                            | Description                                                                                                  |
|----------|---------------|-------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| facing   | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the head of the bed is pointing.<br/>The same direction the player faces when placing the bed. |
| occupied | `false`       | `false`<br/>`true`                        | True when a player or villager is using the bed.                                                             |
| part     | `foot`        | `foot`<br/>`head`                         | The half of the bed in the current block.                                                                    |

Bedrock Edition:

| Name           | Metadata Bits   | Default value | Allowed values              | Values forMetadata Bits     | Description                                                                                                                                  |
|----------------|-----------------|---------------|-----------------------------|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| direction      | `0x1`<br/>`0x2` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3` | `0`<br/>`1`<br/>`2`<br/>`3` | The direction the head of the bed is pointing.0:Head facing South<br/>1:Head facing West<br/>2:Head facing North<br/>3:Head facing East<br/> |
| head_piece_bit | `0x8`           | `true`        | `false`<br/>`true`          | `0`<br/>`1`                 | If the current block is the head part.                                                                                                       |
| occupied_bit   | `0x4`           | `false`       | `false`<br/>`true`          | `0`<br/>`1`                 | True when a player or villager is using the bed.                                                                                             |



### Bedrock
Bedrock Edition:

| Name           | Metadata Bits | Default value | Allowed values     | Values forMetadata Bits | Description                                      |
|----------------|---------------|---------------|--------------------|-------------------------|--------------------------------------------------|
| infiniburn_bit | `0x1`         | `false`       | `false`<br/>`true` | `0`<br/>`1`             | Specifies if this bedrock can burn indefinitely. |



### Beehive and Bee Nest
Java Edition:

| Name        | Default value | Allowed values                              | Description                                                                                                                                                     |
|-------------|---------------|---------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing      | `north`       | `east`<br/>`north`<br/>`south`<br/>`west`   | The opposite from the direction the player faces while placing the block.                                                                                       |
| honey_level | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | Every pollinated bee that leaves the hive after working increases the honey level by one. When at level 5, honey can be bottled or honeycombs can be harvested. |

Bedrock Edition:

| Name        | Metadata Bits | Default value | Allowed values                              | Values forMetadata Bits | Description                                                                                                                                                     |
|-------------|---------------|---------------|---------------------------------------------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| direction   | Not Supported | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`                 | `Unsupported`           | The direction the block faces.0: south<br/>1: west<br/>2: north<br/>3: east<br/>                                                                                |
| honey_level | Not Supported | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | `Unsupported`           | Every pollinated bee that leaves the hive after working increases the honey level by one. When at level 5, honey can be bottled or honeycombs can be harvested. |



### Beetroots
Java Edition:

| Name | Default value | Allowed values | Description  |
|------|---------------|----------------|--------------|
| age  | `0`           | `0`            |              |
|      |               | `1`            |              |
|      |               | `2`            |              |
|      |               | `3`            | Fully grown. |

Bedrock Edition:

| Name   | Metadata Bits             | Default value | Allowed values      | Values forMetadata Bits | Description  |
|--------|---------------------------|---------------|---------------------|-------------------------|--------------|
| growth | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`<br/>`1`         | `0`<br/>`1`             |              |
|        |                           |               | `2`<br/>`3`         | `2`<br/>`3`             |              |
|        |                           |               | `4`<br/>`5`<br/>`6` | `4`<br/>`5`<br/>`6`     |              |
|        |                           |               | `7`                 | `7`                     | Fully grown. |



### Bell
Java Edition:

| Name       | Default value | Allowed values                                            | Description                                                                                             |
|------------|---------------|-----------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| attachment | `floor`       | `ceiling`<br/>`double_wall`<br/>`floor`<br/>`single_wall` | What the bell is attached to.                                                                           |
| facing     | `north`       | `east`<br/>`north`<br/>`south`<br/>`west`                 | The direction the bell is facing.<br/>Opposite from the direction the player faces when placing a bell. |
| powered    | `false`       | `true`<br/>`false`                                        | Whether the bell is attached to a power source, such as a redstone torch.                               |

Bedrock Edition:

| Name       | Metadata Bits   | Default value | Allowed values                                     | Values forMetadata Bits     | Description                                                                                                                                                                                            |
|------------|-----------------|---------------|----------------------------------------------------|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| attachment | `0x4`<br/>`0x8` | `standing`    | `standing`<br/>`hanging`<br/>`side`<br/>`multiple` | `0`<br/>`1`<br/>`2`<br/>`3` | What the bell is attached to.                                                                                                                                                                          |
| direction  | `0x1`<br/>`0x2` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`                        | `0`<br/>`1`<br/>`2`<br/>`3` | The direction the bell is facing. Opposite from the direction a player faces when placing the block.0: South facing bell<br/>1: West facing bell<br/>2: North facing bell<br/>3: East facing bell<br/> |
| toggle_bit | `0x10`          | `false`       | `false`<br/>`true`                                 | `0`<br/>`1`                 | Each time the bell is rung, this value toggles between true and false.                                                                                                                                 |



### Big Dripleaf
Java Edition:
Leaf:

| Name        | Default value | Allowed values                                 | Description                                                                                                                    |
|-------------|---------------|------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| facing      | `north`       | `east`<br/>`north`<br/>`south`<br/>`west`      | The direction the big dripleaf is facing.<br/>The opposite from the direction the player faces while placing the big dripleaf. |
| tilt        | `none`        | `full`<br/>`none`<br/>`partial`<br/>`unstable` | How far this big dripleaf is tilted.                                                                                           |
| waterlogged | `false`       | `false`<br/>`true`                             | Whether there is water in the same place as this big dripleaf.                                                                 |

Stem:

| Name        | Default value | Allowed values                            | Description                                                         |
|-------------|---------------|-------------------------------------------|---------------------------------------------------------------------|
| facing      | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the big dripleaf stem is facing.                      |
| waterlogged | `false`       | `false`<br/>`true`                        | Whether there is water in the same place as this big dripleaf stem. |


Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values                                           | Values forMetadata Bits | Description                                                                                                                    |
|------------------------------|---------------|---------------|----------------------------------------------------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| big_dripleaf_head            | Not Supported | `1`           | `0`<br/>`1`                                              | `Unsupported`           | Whether this is the leaf part or the stem part of big dripleaf.                                                                |
| big_dripleaf_tilt            | Not Supported | `none`        | `none`<br/>`unstable`<br/>`partial_tilt`<br/>`full_tilt` | `Unsupported`           | How far this big dripleaf is tilted.                                                                                           |
| minecraft:cardinal_direction | Not Supported | `south`       | `east`<br/>`north`<br/>`south`<br/>`west`                | `Unsupported`           | The direction the big dripleaf is facing.<br/>The opposite from the direction the player faces while placing the big dripleaf. |



### Blast Furnace
Java Edition:

| Name   | Default value | Allowed values                            | Description                                                                                                                            |
|--------|---------------|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| facing | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the blast furnace's opening faces.<br/>The opposite from the direction the player faces while placing the blast furnace. |
| lit    | `false`       | `false`<br/>`true`                        | If the blast furnace is lit.                                                                                                           |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values                            | Values forMetadata Bits | Description                                                                                                                            |
|------------------------------|---------------|---------------|-------------------------------------------|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| minecraft:cardinal_direction | Not Supported | `south`       | `east`<br/>`north`<br/>`south`<br/>`west` | `Unsupported`           | The direction the blast furnace's opening faces.<br/>The opposite from the direction the player faces while placing the blast furnace. |



### Block of Bamboo and Block of Stripped Bamboo
Java Edition:

| Name | Default value | Allowed values | Description                        |
|------|---------------|----------------|------------------------------------|
| axis | `y`           | `x`            | The block is oriented east–west.   |
|      |               | `y`            | The block is oriented vertically.  |
|      |               | `z`            | The block is oriented north–south. |

Bedrock Edition:

| Name        | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                        |
|-------------|---------------|---------------|----------------|-------------------------|------------------------------------|
| pillar_axis | Not Supported | `y`           | `x`            | `Unsupported`           | The block is oriented east-west.   |
|             |               |               | `y`            | `Unsupported`           | The block is oriented vertically.  |
|             |               |               | `z`            | `Unsupported`           | The block is oriented north-south. |



### Bone Block
Java Edition:

| Name | Default value | Allowed values | Description                             |
|------|---------------|----------------|-----------------------------------------|
| axis | `y`           | `x`            | The bone block is oriented east–west.   |
|      |               | `y`            | The bone block is oriented vertically.  |
|      |               | `z`            | The bone block is oriented north–south. |

Bedrock Edition:

| Name        | Metadata Bits   | Default value | Allowed values              | Values forMetadata Bits     | Description                                |
|-------------|-----------------|---------------|-----------------------------|-----------------------------|--------------------------------------------|
| pillar_axis | `0x4`<br/>`0x8` | `y`           | `y`<br/>`x`<br/>`z`         | `0`<br/>`1`<br/>`2`         | The axis along which the block is oriented |
| deprecated  | `0x1`<br/>`0x2` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3` | `0`<br/>`1`<br/>`2`<br/>`3` | Unused, has no effect in game.             |



### Border
Bedrock Edition and Minecraft Education:

| Name                       | Metadata Bits | Default value | Allowed values                | Values forMetadata Bits | Description                                             |
|----------------------------|---------------|---------------|-------------------------------|-------------------------|---------------------------------------------------------|
| wall_connection_type_east  | Not Supported | `none`        | `none`<br/>`short`<br/>`tall` | `Unsupported`           | How the wall extends from the center post to the east.  |
| wall_connection_type_north | Not Supported | `none`        | `none`<br/>`short`<br/>`tall` | `Unsupported`           | How the wall extends from the center post to the north. |
| wall_connection_type_south | Not Supported | `none`        | `none`<br/>`short`<br/>`tall` | `Unsupported`           | How the wall extends from the center post to the south. |
| wall_connection_type_west  | Not Supported | `none`        | `none`<br/>`short`<br/>`tall` | `Unsupported`           | How the wall extends from the center post to the west.  |
| wall_post_bit              | Not Supported | `true`        | `false`<br/>`true`            | `Unsupported`           | Whether or not the wall has a center post.              |



### Brewing Stand
Java Edition:

| Name         | Default value | Allowed values     | Description                      |
|--------------|---------------|--------------------|----------------------------------|
| has_bottle_0 | `false`       | `false`<br/>`true` | True when a bottle is in slot 1. |
| has_bottle_1 | `false`       | `false`<br/>`true` | True when a bottle is in slot 2. |
| has_bottle_2 | `false`       | `false`<br/>`true` | True when a bottle is in slot 3. |

Bedrock Edition:

| Name                     | Metadata Bits | Default value | Allowed values     | Values forMetadata Bits | Description                      |
|--------------------------|---------------|---------------|--------------------|-------------------------|----------------------------------|
| brewing_stand_slot_a_bit | `0x1`         | `false`       | `false`<br/>`true` | `0`<br/>`1`             | True when a bottle is in slot 1. |
| brewing_stand_slot_b_bit | `0x2`         | `false`       | `false`<br/>`true` | `0`<br/>`1`             | True when a bottle is in slot 2. |
| brewing_stand_slot_c_bit | `0x4`         | `false`       | `false`<br/>`true` | `0`<br/>`1`             | True when a bottle is in slot 3. |



### Bubble Column
Java Edition:

| Name | Default value | Allowed values     | Description                                                  |
|------|---------------|--------------------|--------------------------------------------------------------|
| drag | `true`        | `false`<br/>`true` | Determines whether the bubble column is upward or whirlpool. |

Bedrock Edition:

| Name      | Metadata Bits | Default value | Allowed values     | Values forMetadata Bits | Description                                                  |
|-----------|---------------|---------------|--------------------|-------------------------|--------------------------------------------------------------|
| drag_down | `0x1`         | `false`       | `false`<br/>`true` | `0`<br/>`1`             | Determines whether the bubble column is upward or whirlpool. |



### Buttons
Java Edition:

| Name    | Default value | Allowed values                            | Description                                                                                                                      |
|---------|---------------|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| face    | `wall`        | `ceiling`<br/>`floor`<br/>`wall`          | The face of the block it's placed on.<br/>Floor is on top of a block, ceiling is on the bottom, and wall is on one of its sides. |
| facing  | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction it's facing.<br/>Opposite to the direction the player is facing if placed on the side of a block.                  |
| powered | `false`       | `false`<br/>`true`                        | If true, the button is currently activated.                                                                                      |

Bedrock Edition:

| Name               | Metadata Bits             | Default value | Allowed values                              | Values forMetadata Bits                     | Description                                                                                                                                                                                                                                                                 |
|--------------------|---------------------------|---------------|---------------------------------------------|---------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| button_pressed_bit | `0x8`                     | `false`       | `false`<br/>`true`                          | `0`<br/>`1`                                 | If the button is currently activated.                                                                                                                                                                                                                                       |
| facing_direction   | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | The direction it's facing.0: Button on block bottom facing down<br/>1: Button on block top facing up<br/>2: Button on block side facing north<br/>3: Button on block side facing south<br/>4: Button on block side facing west<br/>5: Button on block side facing east<br/> |



### Cactus
Java Edition

| Name | Default value | Allowed values                                                                                                                    | Description                                                                                                                                                                                                        |
|------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| age  | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | A freshly-planted cactus – and a cactus that has just grown cactus above it – each have an age of 0.<br/>The age is incremented at random intervals.<br/>At age 15, a cactus may try to grow more cactus above it. |

Bedrock Edition

| Name | Metadata Bits                       | Default value | Allowed values                                                                                                                    | Values forMetadata Bits                                                                                                           | Description                                                                                                                                                                                                        |
|------|-------------------------------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| age  | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | A freshly-planted cactus – and a cactus that has just grown cactus above it – each have an age of 0.<br/>The age is incremented at random intervals.<br/>At age 15, a cactus may try to grow more cactus above it. |



### Cake
Java Edition
Cakes:

| Name  | Default value | Allowed values                                      | Description                          |
|-------|---------------|-----------------------------------------------------|--------------------------------------|
| bites | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6` | Number of bites taken from the cake. |

Candle cakes:

| Name | Default value | Allowed values     | Description                            |
|------|---------------|--------------------|----------------------------------------|
| lit  | `false`       | `false`<br/>`true` | Whether the candle on the cake is lit. |

Bedrock Edition
Cakes:

| Name         | Metadata Bits             | Default value | Allowed values                                      | Values forMetadata Bits                             | Description                          |
|--------------|---------------------------|---------------|-----------------------------------------------------|-----------------------------------------------------|--------------------------------------|
| bite_counter | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6` | Number of bites taken from the cake. |

Candle cakes:

| Name | Metadata Bits | Default value | Allowed values     | Values forMetadata Bits | Description                            |
|------|---------------|---------------|--------------------|-------------------------|----------------------------------------|
| lit  | `0x1`         | `false`       | `false`<br/>`true` | `0`<br/>`1`             | Whether the candle on the cake is lit. |



### Campfire
Java Edition:

| Name        | Default value | Allowed values                            | Description                                                                                                            |
|-------------|---------------|-------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| facing      | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the campfire is facing.<br/>The opposite from the direction the player faces while placing the campfire. |
| lit         | `true`        | `false`<br/>`true`                        | Whether the campfire is lit.                                                                                           |
| signal_fire | `false`       | `false`<br/>`true`                        | Whether the campfire has ahay balebelow it.                                                                            |
| waterlogged | `false`       | `false`<br/>`true`                        | Whether or not there's water in the same place as this campfire.                                                       |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values                            | Values forMetadata Bits | Description                                                                                                            |
|------------------------------|---------------|---------------|-------------------------------------------|-------------------------|------------------------------------------------------------------------------------------------------------------------|
| extinguished                 | `0x4`         | `false`       | `false`<br/>`true`                        | `0`<br/>`1`             | Whether the campfire is put out.                                                                                       |
| minecraft:cardinal_direction | Not Supported | `south`       | `east`<br/>`north`<br/>`south`<br/>`west` | `Unsupported`           | The direction the campfire is facing.<br/>The opposite from the direction the player faces while placing the campfire. |



### Candles
Java Edition:

| Name        | Default value | Allowed values              | Description                                                      |
|-------------|---------------|-----------------------------|------------------------------------------------------------------|
| candles     | `1`           | `1`<br/>`2`<br/>`3`<br/>`4` | Number of candles.                                               |
| lit         | `false`       | `false`<br/>`true`          | Whether or not these candles are lit.                            |
| waterlogged | `false`       | `false`<br/>`true`          | Whether or not there's water in the same place as these candles. |

Bedrock Edition:

| Name    | Metadata Bits   | Default value | Allowed values              | Values forMetadata Bits     | Description                              |
|---------|-----------------|---------------|-----------------------------|-----------------------------|------------------------------------------|
| candles | `0x1`<br/>`0x2` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3` | `0`<br/>`1`<br/>`2`<br/>`3` | Number of candles, starting from 1 to 4. |
| lit     | `0x4`           | `false`       | `false`<br/>`true`          | `0`<br/>`1`                 | Whether or not these candles are lit.    |

### Carrots
Java Edition:

| Name | Default value | Allowed values      | Description  |
|------|---------------|---------------------|--------------|
| age  | `0`           | `0`<br/>`1`         |              |
|      |               | `2`<br/>`3`         |              |
|      |               | `4`<br/>`5`<br/>`6` |              |
|      |               | `7`                 | Fully grown. |

Bedrock Edition:

| Name   | Metadata Bits             | Default value | Allowed values      | Values forMetadata Bits | Description  |
|--------|---------------------------|---------------|---------------------|-------------------------|--------------|
| growth | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`<br/>`1`         | `0`<br/>`1`             |              |
|        |                           |               | `2`<br/>`3`         | `2`<br/>`3`             |              |
|        |                           |               | `4`<br/>`5`<br/>`6` | `4`<br/>`5`<br/>`6`     |              |
|        |                           |               | `7`                 | `7`                     | Fully grown. |



### Cauldron
Java Edition:
Water cauldron and powder snow cauldron:

| Name  | Default value | Allowed values              | Description                                       |
|-------|---------------|-----------------------------|---------------------------------------------------|
| level | `0`           | `0`<br/>`1`<br/>`2`<br/>`3` | Fullness of a cauldron, 0 is empty and 3 is full. |

Bedrock Edition:

| Name            | Metadata Bits             | Default value | Allowed values                                      | Values forMetadata Bits                             | Description                                       |
|-----------------|---------------------------|---------------|-----------------------------------------------------|-----------------------------------------------------|---------------------------------------------------|
| fill_level      | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6` | Fullness of a cauldron, 0 is empty and 6 is full. |
| cauldron_liquid | `0x8`                     | `water`       | `water`                                             | `0`                                                 | The cauldron contains water.                      |
|                 |                           |               | `lava`                                              | `1`                                                 | The cauldron contains lava.                       |
|                 |                           |               | `powder_snow`                                       | `Unsupported [sic]`                                 | The cauldron contains powder snow.                |



### Cave Vines
Java Edition:
Cave Vines:

| Name    | Default value | Allowed values                                                                                                                                                                                                              | Description                         |
|---------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------|
| berries | `false`       | `false`<br/>`true`                                                                                                                                                                                                          | Whether this cave vine has berries. |
| age     | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15`<br/>`16`<br/>`17`<br/>`18`<br/>`19`<br/>`20`<br/>`21`<br/>`22`<br/>`23`<br/>`24`<br/>`25` | How old this cave vine is.          |

Cave Vines Plant:

| Name    | Default value | Allowed values     | Description                         |
|---------|---------------|--------------------|-------------------------------------|
| berries | `false`       | `false`<br/>`true` | Whether this cave vine has berries. |

Bedrock Edition:
Cave Vines, Cave Vines Body With Berries, Cave Vines Head With Berries:

| Name              | Metadata Bits | Default value | Allowed values                                                                                                                                                                                                              | Values forMetadata Bits | Description                |
|-------------------|---------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|----------------------------|
| growing_plant_age | Not Supported | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15`<br/>`16`<br/>`17`<br/>`18`<br/>`19`<br/>`20`<br/>`21`<br/>`22`<br/>`23`<br/>`24`<br/>`25` | `Unsupported`           | How old this cave vine is. |



### Chain
Java Edition:

| Name        | Default value | Allowed values     | Description                                                   |
|-------------|---------------|--------------------|---------------------------------------------------------------|
| axis        | `y`           | `x`                | The chain is oriented east–west.                              |
|             |               | `y`                | The chain is oriented vertically.                             |
|             |               | `z`                | The chain is oriented north–south.                            |
| waterlogged | `false`       | `false`<br/>`true` | Whether or not there's water in the same place as this chain. |

Bedrock Edition:

| Name        | Metadata Bits   | Default value | Allowed values | Values forMetadata Bits | Description                        |
|-------------|-----------------|---------------|----------------|-------------------------|------------------------------------|
| pillar_axis | `0x1`<br/>`0x2` | `y`           | `x`            | `1`                     | The chain is oriented east–west.   |
|             |                 |               | `y`            | `0`                     | The chain is oriented vertically.  |
|             |                 |               | `z`            | `2`                     | The chain is oriented north–south. |



### Chemistry Table
| Name                 | Metadata Bits   | Default value      | Allowed values              | Values forMetadata Bits     | Description                                                                           |
|----------------------|-----------------|--------------------|-----------------------------|-----------------------------|---------------------------------------------------------------------------------------|
| chemistry_table_type | `0x1`<br/>`0x2` | `compound_creator` | `compound_creator`          | `0`                         | Compound Creator                                                                      |
|                      |                 |                    | `element_constructor`       | `2`                         | Element Constructor                                                                   |
|                      |                 |                    | `lab_table`                 | `3`                         | Lab Table                                                                             |
|                      |                 |                    | `material_reducer`          | `1`                         | Material Reducer                                                                      |
| direction            | `0x4`<br/>`0x8` | `0`                | `0`<br/>`1`<br/>`2`<br/>`3` | `0`<br/>`1`<br/>`2`<br/>`3` | The direction the block's front is.0: north<br/>1: east<br/>2: south<br/>3: west<br/> |



### Chests
#### Chest and Trapped Chest
Java Edition:

| Name        | Default value | Allowed values                            | Description                                                                                                       |
|-------------|---------------|-------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| facing      | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the chest's latch is on.<br/>The opposite from the direction the player faces when placing a chest. |
| type        | `single`      | `left`<br/>`right`<br/>`single`           | The direction the chest has a connection with.                                                                    |
| waterlogged | `false`       | `false`<br/>`true`                        | Whether or not there's water in the same place as this chest.                                                     |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values                            | Values forMetadata Bits | Description                                                                                                       |
|------------------------------|---------------|---------------|-------------------------------------------|-------------------------|-------------------------------------------------------------------------------------------------------------------|
| minecraft:cardinal_direction | Not Supported | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | `Unsupported`           | The direction the chest's latch is on.<br/>The opposite from the direction the player faces when placing a chest. |



#### Ender Chest
Java Edition:

| Name        | Default value | Allowed values                            | Description                                                                                                                    |
|-------------|---------------|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| facing      | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the ender chest's latch is on.<br/>The opposite from the direction the player faces when placing an ender chest. |
| waterlogged | `false`       | `false`<br/>`true`                        | Whether or not there's water in the same place as this ender chest.                                                            |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values                            | Values forMetadata Bits | Description                                                                                                                    |
|------------------------------|---------------|---------------|-------------------------------------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| minecraft:cardinal_direction | Not Supported | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | `Unsupported`           | The direction the ender chest's latch is on.<br/>The opposite from the direction the player faces when placing an ender chest. |



### Chiseled Bookshelf
Java Edition:

| Name            | Default value | Allowed values                            | Description                                                                                              |
|-----------------|---------------|-------------------------------------------|----------------------------------------------------------------------------------------------------------|
| facing          | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the bookshelf is facing.<br/>Opposite from the direction the player faces when placing it. |
| slot_0_occupied | `false`       | `true`<br/>`false`                        | Whether there is a book in the upper-left slot.                                                          |
| slot_1_occupied | `false`       | `true`<br/>`false`                        | Whether there is a book in the upper-middle slot.                                                        |
| slot_2_occupied | `false`       | `true`<br/>`false`                        | Whether there is a book in the upper-right slot.                                                         |
| slot_3_occupied | `false`       | `true`<br/>`false`                        | Whether there is a book in the lower-left slot.                                                          |
| slot_4_occupied | `false`       | `true`<br/>`false`                        | Whether there is a book in the lower-middle slot.                                                        |
| slot_5_occupied | `false`       | `true`<br/>`false`                        | Whether there is a book in the lower-right slot.                                                         |

Bedrock Edition:

| Name         | Metadata Bits | Default value | Allowed values              | Values forMetadata Bits | Description                                                                                                                                                                            |
|--------------|---------------|---------------|-----------------------------|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| books_stored | Not Supported | `0`           | `0 — 63`                    | `Unsupported`           | The confguration of the books in the bookshelf.                                                                                                                                        |
| direction    | Not Supported | `0`           | `0`<br/>`1`<br/>`2`<br/>`3` | `Unsupported`           | The direction the bookshelf is facing.<br/>Opposite from the direction the player faces when placing it.0: facing South<br/>1: facing West<br/>2: facing North<br/>3: facing East<br/> |

### Chorus Flower
Java Edition

| Name | Default value | Allowed values                      | Description                                                                                                                                                                   |
|------|---------------|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| age  | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4` | A freshly planted chorus flower starts at age 0. The age is incremented when a chorus flower turns horizontally and/or generates additional chorus flowers on the same plant. |
|      |               | `5`                                 | At age 5, the chorus flower does not grow further. A chorus flower can become age 5 at any time.                                                                              |

Bedrock Edition

| Name | Metadata Bits             | Default value | Allowed values                                                                    | Values forMetadata Bits             | Description                                                                                                                                                                   |
|------|---------------------------|---------------|-----------------------------------------------------------------------------------|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| age  | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`                                               | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4` | A freshly planted chorus flower starts at age 0. The age is incremented when a chorus flower turns horizontally and/or generates additional chorus flowers on the same plant. |
|      |                           |               | `5`                                                                               | `5`                                 | At age 5, the chorus flower does not grow further. A chorus flower can become age 5 at any time.                                                                              |
|      |                           |               | `6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | `Unsupported`                       | Unused                                                                                                                                                                        |



### Chorus Plant
Java Edition:

| Name  | Default value | Allowed values     | Description                                                                       |
|-------|---------------|--------------------|-----------------------------------------------------------------------------------|
| down  | `false`       | `false`<br/>`true` | When true, the plant extends out from the center of the plant-block down.         |
| east  | `false`       | `false`<br/>`true` | When true, the plant extends out from the center of the plant-block to the east.  |
| north | `false`       | `false`<br/>`true` | When true, the plant extends out from the center of the plant-block to the north. |
| south | `false`       | `false`<br/>`true` | When true, the plant extends out from the center of the plant-block to the south. |
| up    | `false`       | `false`<br/>`true` | When true, the plant extends out from the center of the plant-block up.           |
| west  | `false`       | `false`<br/>`true` | When true, the plant extends out from the center of the plant-block to the west.  |



### Cocoa
Java Edition:

| Name   | Default value | Allowed values                            | Description                                                                                              |
|--------|---------------|-------------------------------------------|----------------------------------------------------------------------------------------------------------|
| age    | `0`           | `0`<br/>`1`<br/>`2`                       | The stage of the pod's growth, 2 is fully grown.                                                         |
| facing | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction from the cocoa bean to the log.<br/>The direction the player faces when placing the cocoa. |

Bedrock Edition:

| Name      | Metadata Bits   | Default value | Allowed values                                                                                            | Values forMetadata Bits     | Description                                                                                                                                                     |
|-----------|-----------------|---------------|-----------------------------------------------------------------------------------------------------------|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| age       | `0x4`<br/>`0x8` | `0`           | `0`<br/>`1`<br/>`2`                                                                                       | `0`<br/>`1`<br/>`2`         | The stage of the pod's growth, 2 is fully grown.                                                                                                                |
|           |                 |               | `3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | `Unsupported`               | Unused                                                                                                                                                          |
| direction | `0x1`<br/>`0x2` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`                                                                               | `0`<br/>`1`<br/>`2`<br/>`3` | The direction from the cocoa bean to the log.0: Attached to the south<br/>1: Attached to the east<br/>2: Attached to the north<br/>3: Attached to the west<br/> |



### Command Blocks
Java Edition:

| Name        | Default value | Allowed values                                                | Description                                       |
|-------------|---------------|---------------------------------------------------------------|---------------------------------------------------|
| conditional | `false`       | `false`<br/>`true`                                            | True if the command block is in conditional mode. |
| facing      | `north`       | `down`<br/>`east`<br/>`north`<br/>`south`<br/>`up`<br/>`west` | The direction the command block is pointing.      |

Bedrock Edition:

| Name             | Metadata Bits             | Default value | Allowed values                              | Values forMetadata Bits                     | Description                                                                                                                                                    |
|------------------|---------------------------|---------------|---------------------------------------------|---------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| conditional_bit  | `0x8`                     | `false`       | `false`<br/>`true`                          | `0`<br/>`1`                                 | True if the command block is in conditional mode.                                                                                                              |
| facing_direction | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | The direction the command block is pointing.0: facing down<br/>1: facing up<br/>2: facing north<br/>3: facing south<br/>4: facing west<br/>5: facing east<br/> |



### Composter
Java Edition:

| Name  | Default value | Allowed values                                                      | Description                                                            |
|-------|---------------|---------------------------------------------------------------------|------------------------------------------------------------------------|
| level | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8` | When at level 8, bone meal is able to be collected from the composter. |

Bedrock Edition:

| Name                 | Metadata Bits                       | Default value | Allowed values                                                      | Values forMetadata Bits                                             | Description                                                            |
|----------------------|-------------------------------------|---------------|---------------------------------------------------------------------|---------------------------------------------------------------------|------------------------------------------------------------------------|
| composter_fill_level | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8` | When at level 8, bone meal is able to be collected from the composter. |



### Conduit
Java Edition:

| Name        | Default value | Allowed values     | Description                                                     |
|-------------|---------------|--------------------|-----------------------------------------------------------------|
| waterlogged | `true`        | `false`<br/>`true` | Whether or not there's water in the same place as this conduit. |

### Coral
Java Edition:

| Name        | Default value | Allowed values     | Description                                                   |
|-------------|---------------|--------------------|---------------------------------------------------------------|
| waterlogged | `true`        | `false`<br/>`true` | Whether or not there's water in the same place as this coral. |



### Coral Block
Bedrock Edition:

| Name        | Metadata Bits             | Default value | Allowed values     | Values forMetadata Bits | Description                              |
|-------------|---------------------------|---------------|--------------------|-------------------------|------------------------------------------|
| coral_color | `0x1`<br/>`0x2`<br/>`0x4` | `blue`        | `blue`             | `0`                     | Tube Coral Block                         |
|             |                           |               | `pink`             | `1`                     | Brain Coral Block                        |
|             |                           |               | `purple`           | `2`                     | Bubble Coral Block                       |
|             |                           |               | `red`              | `3`                     | Fire Coral Block                         |
|             |                           |               | `yellow`           | `4`                     | Horn Coral Block                         |
| dead_bit    | `0x8`                     | `false`       | `false`<br/>`true` | `0`<br/>`1`             | Whether or not this coral block is dead. |



### Coral Fan
Java Edition
Floor:

| Name        | Default value | Allowed values     | Description                                                       |
|-------------|---------------|--------------------|-------------------------------------------------------------------|
| waterlogged | `true`        | `false`<br/>`true` | Whether or not there's water in the same place as this coral fan. |

Wall:

| Name        | Default value | Allowed values                            | Description                                                                                                                                                    |
|-------------|---------------|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing      | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction in which the coral fan juts out from the block it is attached to.<br/>For example, a coral fan facing north is attached to a block to its south. |
| waterlogged | `true`        | `false`<br/>`true`                        | Whether or not there's water in the same place as this coral fan.                                                                                              |

Bedrock Edition
Floor:

| Name                | Metadata Bits             | Default value | Allowed values | Values forMetadata Bits | Description                                                  |
|---------------------|---------------------------|---------------|----------------|-------------------------|--------------------------------------------------------------|
| coral_color         | `0x1`<br/>`0x2`<br/>`0x4` | `blue`        | `blue`         | `0`                     | Tube Coral Fan                                               |
|                     |                           |               | `pink`         | `1`                     | Brain Coral Fan                                              |
|                     |                           |               | `purple`       | `2`                     | Bubble Coral Fan                                             |
|                     |                           |               | `red`          | `3`                     | Fire Coral Fan                                               |
|                     |                           |               | `yellow`       | `4`                     | Horn Coral Fan                                               |
| coral_fan_direction | `0x8`                     | `0`           | `0`<br/>`1`    | `0`<br/>`1`             | The direction the coral is facing. East-west or north-south. |

Wall:

| Name                | Metadata Bits   | Default value | Allowed values              | Values forMetadata Bits     | Description                                                                                                                                                                    |
|---------------------|-----------------|---------------|-----------------------------|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| coral_hang_type_bit | `0x1`           | `false`       | `false`<br/>`true`          | `0`<br/>`1`                 | Which coral it is; depends on the ID.<br/>For`hang`false means tube and true means brain.<br/>For`hang2`false means bubble and true means fire.<br/>For`hang3`false mean horn. |
| coral_direction     | `0x4`<br/>`0x8` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3` | `0`<br/>`1`<br/>`2`<br/>`3` | The direction the top of the fan is facing.0: west<br/>1: east<br/>2: north<br/>3: south<br/>                                                                                  |
| dead_bit            | `0x2`           | `false`       | `false`<br/>`true`          | `0`<br/>`1`                 | Whether or not this coral is dead.                                                                                                                                             |



### Daylight Detector
Java Edition:

| Name     | Default value | Allowed values                                                                                                                    | Description                                                       |
|----------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| inverted | `false`       | `false`<br/>`true`                                                                                                                | If true, the daylight detector is inverted.                       |
| power    | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | The current redstone power level produced by the daylight sensor. |

Bedrock Edition:

| Name            | Metadata Bits                       | Default value | Allowed values                                                                                                                    | Values forMetadata Bits                                                                                                           | Description                                                       |
|-----------------|-------------------------------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| redstone_signal | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | The current redstone power level produced by the daylight sensor. |



### Deepslate
Java Edition:

| Name | Default value | Allowed values | Description                            |
|------|---------------|----------------|----------------------------------------|
| axis | `y`           | `x`            | The deepslate is oriented east–west.   |
|      |               | `y`            | The deepslate is oriented vertically.  |
|      |               | `z`            | The deepslate is oriented north–south. |

Bedrock Edition:

| Name        | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                            |
|-------------|---------------|---------------|----------------|-------------------------|----------------------------------------|
| pillar_axis | Not Supported | `y`           | `x`            | `Unsupported`           | The deepslate is oriented east–west.   |
|             |               |               | `y`            | `Unsupported`           | The deepslate is oriented vertically.  |
|             |               |               | `z`            | `Unsupported`           | The deepslate is oriented north–south. |



### Dirt
Bedrock Edition:

| Name      | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description |
|-----------|---------------|---------------|----------------|-------------------------|-------------|
| dirt_type | `0x1`         | `normal`      | `normal`       | `0`                     | Dirt        |
|           |               |               | `coarse`       | `1`                     | Coarse Dirt |



### Dispenser and Dropper
Java Edition:

| Name      | Default value | Allowed values                                                | Description                                                                                                                        |
|-----------|---------------|---------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| facing    | `north`       | `down`<br/>`east`<br/>`north`<br/>`south`<br/>`up`<br/>`west` | The direction in which contents are shot or dropped.<br/>The opposite from the direction the player faces while placing the block. |
| triggered | `false`       | `false`<br/>`true`                                            | True if this block is activated.                                                                                                   |

Bedrock Edition:

| Name             | Metadata Bits             | Default value | Allowed values                                              | Values forMetadata Bits                                     | Description                                                                                                                                                            |
|------------------|---------------------------|---------------|-------------------------------------------------------------|-------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing_direction | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7` | The direction in which contents are shot or dropped.0: facing down<br/>1: facing up<br/>2: facing north<br/>3: facing south<br/>4: facing west<br/>5: facing east<br/> |
| triggered_bit    | `0x8`                     | `false`       | `false`<br/>`true`                                          | `0`<br/>`1`                                                 | True if this block is activated.                                                                                                                                       |



### Doors
Java Edition:

| Name    | Default value | Allowed values                            | Description                                                                                                                                                                                  |
|---------|---------------|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing  | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the door's "inside" is facing.<br/>The direction the player faces while placing the door.<br/>For example, a door facing east occupies the west part of its block when closed. |
| half    | `lower`       | `lower`<br/>`upper`                       | Identifies which part of the door the block is.                                                                                                                                              |
| hinge   | `left`        | `left`<br/>`right`                        | Identifies the side the hinge is on (when facing the same direction as the door's inside).                                                                                                   |
| open    | `false`       | `false`<br/>`true`                        | True if the door is currently open.                                                                                                                                                          |
| powered | `false`       | `false`<br/>`true`                        | True if the door is currently powered by redstone.                                                                                                                                           |

Bedrock Edition:
Lower Door Block:

| Name            | Metadata Bits   | Default value | Allowed values              | Values forMetadata Bits     | Description                                                                                                                                                                                                                                                                |
|-----------------|-----------------|---------------|-----------------------------|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| direction       | `0x1`<br/>`0x2` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3` | `0`<br/>`1`<br/>`2`<br/>`3` | The direction the door's "inside" is facing.<br/>The direction the player faces while placing the door.<br/>For example, a door facing east occupies the west part of its block when closed.0: Facing east<br/>1: Facing south<br/>2: Facing west<br/>3: Facing north<br/> |
| door_hinge_bit  | `— [sic]`       | `false`       | `false`<br/>`true`          | `0`<br/>`0 [sic]`           | Identifies the side the hinge is on (when facing the same direction as the door's inside). false if hinge is on the left (the default), true if on the right.<br/>Lower door block has the same aux value when it is opened and closed.                                    |
| open_bit        | `0x4`           | `false`       | `false`<br/>`true`          | `0`<br/>`1`                 | True if the door is currently open.                                                                                                                                                                                                                                        |
| upper_block_bit | `0x8`           | `false`       | `false`<br/>`true`          | `0`<br/>`1`                 | Always false for the lower part of a door.                                                                                                                                                                                                                                 |

Upper Door Block:

| Name            | Metadata Bits | Default value | Allowed values              | Values forMetadata Bits           | Description                                                                                                                                                                                                                                                                                                                                |
|-----------------|---------------|---------------|-----------------------------|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| direction       | `— [sic]`     | `0`           | `0`<br/>`1`<br/>`2`<br/>`3` | `0`<br/>`0`<br/>`0`<br/>`0 [sic]` | The direction the door's "inside" is facing.<br/>The direction the player faces while placing the door.<br/>For example, a door facing east occupies the west part of its block when closed.0: Facing east<br/>1: Facing south<br/>2: Facing west<br/>3: Facing north<br/>Upper door block has the same aux value no matter what it faces. |
| door_hinge_bit  | `— [sic]`     | `false`       | `false`<br/>`true`          | `0`<br/>`Unsupported`             | Identifies the side the hinge is on (when facing the same direction as the door's inside). false if hinge is on the left (the default), true if on the right.<br/>Upper door block doesn't support aux value when its hinge is on theright.                                                                                                |
| open_bit        | `— [sic]`     | `false`       | `false`<br/>`true`          | `0`<br/>`0 [sic]`                 | True if the door is currently open.<br/>Lower door block has the same aux value when it is opened and closed.                                                                                                                                                                                                                              |
| upper_block_bit | `0x8`         | `false`       | `false`<br/>`true`          | `0`<br/>`1`                       | Always true for the upper part of a door.                                                                                                                                                                                                                                                                                                  |

### End Portal Frame
Java Edition:

| Name   | Default value | Allowed values                            | Description                                                                                                                                                                                                                                                        |
|--------|---------------|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| eye    | `false`       | `false`<br/>`true`                        | If true, the portal frame block contains aneye of ender.                                                                                                                                                                                                           |
| facing | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction of the end portal frame block.<br/>The opposite from the direction the player faces while placing the block.<br/>In order to activate a portal, all 12 blocks must be facing inward;<br/>for example, the northern three blocks must all face south. |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values                            | Values forMetadata Bits | Description                                                                                                                                                                                                                                                        |
|------------------------------|---------------|---------------|-------------------------------------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| end_portal_eye_bit           | `0x4`         | `false`       | `false`<br/>`true`                        | `0`<br/>`1`             | If the portal frame block contains aneye of ender.                                                                                                                                                                                                                 |
| minecraft:cardinal_direction | Not Supported | `south`       | `east`<br/>`north`<br/>`south`<br/>`west` | `Unsupported`           | The direction of the end portal frame block.<br/>The opposite from the direction the player faces while placing the block.<br/>In order to activate a portal, all 12 blocks must be facing inward;<br/>for example, the northern three blocks must all face south. |



### End Rod
Java Edition:

| Name   | Default value | Allowed values                                                | Description                                                                                                                                                                                                         |
|--------|---------------|---------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing | `up`          | `down`<br/>`east`<br/>`north`<br/>`south`<br/>`up`<br/>`west` | The direction to the end rod, from the block it is attached to; also the direction the white end points.<br/>Opposite from the direction the player faces when placing an end rod, and opposite from the wider end. |

Bedrock Edition:

| Name             | Metadata Bits             | Default value | Allowed values                              | Values forMetadata Bits                     | Description                                                                                                                                                                                                                |
|------------------|---------------------------|---------------|---------------------------------------------|---------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing_direction | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | The direction to the end rod, from the block it is attached to; also the direction the white end points.0: Facing down<br/>1: Facing up<br/>2: Facing north<br/>3: Facing south<br/>4: Facing west<br/>5: Facing east<br/> |



### Farmland
Java Edition:

| Name     | Default value | Allowed values                                              | Description                                                                                                                                                                                               |
|----------|---------------|-------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| moisture | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7` | Increasing levels of wetness. The wetness value counts down to 0 while the farmland does not have access to water. The wet texture is used only on level 7. Newly hydrated farmland jumps from 0 to 7.[2] |

Bedrock Edition:

| Name               | Metadata Bits             | Default value | Allowed values                                              | Values forMetadata Bits                                     | Description                                                                                                                                                                                            |
|--------------------|---------------------------|---------------|-------------------------------------------------------------|-------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| moisturized_amount | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7` | Increasing levels of wetness. The wetness value counts down to 0 while the farmland does not have access to water. The wet texture is used only on level 7. Newly hydrated farmland jumps from 0 to 7. |



### Fences
Java Edition:

| Name        | Default value | Allowed values     | Description                                                     |
|-------------|---------------|--------------------|-----------------------------------------------------------------|
| east        | `false`       | `false`<br/>`true` | When true, the fence extends from the center post to the east.  |
| north       | `false`       | `false`<br/>`true` | When true, the fence extends from the center post to the north. |
| south       | `false`       | `false`<br/>`true` | When true, the fence extends from the center post to the south. |
| waterlogged | `false`       | `false`<br/>`true` | Whether or not there's water in the same place as this fence.   |
| west        | `false`       | `false`<br/>`true` | When true, the fence extends from the center post to the west.  |

### Fence Gates
Java Edition:

| Name    | Default value | Allowed values                            | Description                                                                                                                                                                            |
|---------|---------------|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing  | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | For an open gate, the direction the gates swing open.<br/>For a closed gate, the direction the player was facing when the gate was placed, or the last direction the gates have swung. |
| in_wall | `false`       | `false`<br/>`true`                        | If true, the gate is lowered by three pixels, to accommodate attaching more cleanly withwalls.                                                                                         |
| open    | `false`       | `false`<br/>`true`                        | If true, the gate is opened.                                                                                                                                                           |
| powered | `false`       | `false`<br/>`true`                        | If true, the gate is receiving redstone power.                                                                                                                                         |

Bedrock Edition:

| Name        | Metadata Bits   | Default value | Allowed values              | Values forMetadata Bits     | Description                                                                                                                                                                                                                                                                                                    |
|-------------|-----------------|---------------|-----------------------------|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| direction   | `0x1`<br/>`0x2` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3` | `0`<br/>`1`<br/>`2`<br/>`3` | The direction the gate is facing0: Facing south<br/>1: Facing west<br/>2: Facing north<br/>3: Facing east<br/>For an open gate, it's the direction the gates swing open.<br/>For a closed gate, it's the direction the player was facing when the gate was placed, or the last direction the gates have swung. |
| in_wall_bit | `0x8`           | `false`       | `false`<br/>`true`          | `0`<br/>`1`                 | If the gate is lowered by three pixels, to accommodate attaching more cleanly withwalls.                                                                                                                                                                                                                       |
| open_bit    | `0x4`           | `false`       | `false`<br/>`true`          | `0`<br/>`1`                 | If the gate is opened.                                                                                                                                                                                                                                                                                         |

### Fire
Java Edition:
Fire:

| Name  | Default value | Allowed values                                                                                                                    | Description                                                                                                                                             |
|-------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| age   | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | $Newly placed fire has an age of 0, and has a\frac{1}{3}$chance of incrementing with eachblock tick.<br/>This factor affects how the fire extinguishes. |
| east  | `false`       | `false`<br/>`true`                                                                                                                | When true, fire texture shows on that face of the block to the east; false if there's a block below this fire.                                          |
| north | `false`       | `false`<br/>`true`                                                                                                                | When true, fire texture shows on that face of the block to the north; false if there's a block below this fire.                                         |
| south | `false`       | `false`<br/>`true`                                                                                                                | When true, fire texture shows on that face of the block to the south; false if there's a block below this fire.                                         |
| up    | `false`       | `false`<br/>`true`                                                                                                                | When true, fire texture shows on that face of the block above; false if there's a block below this fire.                                                |
| west  | `false`       | `false`<br/>`true`                                                                                                                | When true, fire texture shows on that face of the block to the west; false if there's a block below this fire.                                          |

Bedrock Edition:
Fire and Soul Fire:

| Name | Metadata Bits                       | Default value | Allowed values                                                                                                                    | Values forMetadata Bits                                                                                                           | Description                                                                           |
|------|-------------------------------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| age  | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | Newly placed fire has an age of 0.<br/>This factor affects how the fire extinguishes. |



### Flowers
Java Edition:
Sunflower, lilac, rose bush, peony, and pitcher plant

| Name | Default value | Allowed values      | Description                                    |
|------|---------------|---------------------|------------------------------------------------|
| half | `lower`       | `lower`<br/>`upper` | The half of the plant contained in this block. |

Bedrock Edition:
All small flowers except dandelion, wither rose, and torchflower

| Name        | Metadata Bits                       | Default value | Allowed values       | Values forMetadata Bits | Description        |
|-------------|-------------------------------------|---------------|----------------------|-------------------------|--------------------|
| flower_type | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8` | `poppy`       | `poppy`              | `0`                     | Poppy              |
|             |                                     |               | `orchid`             | `1`                     | Blue Orchid        |
|             |                                     |               | `allium`             | `2`                     | Allium             |
|             |                                     |               | `houstonia`          | `3`                     | Azure Bluet        |
|             |                                     |               | `tulip_red`          | `4`                     | Red Tulip          |
|             |                                     |               | `tulip_orange`       | `5`                     | Orange Tulip       |
|             |                                     |               | `tulip_white`        | `6`                     | White Tulip        |
|             |                                     |               | `tulip_pink`         | `7`                     | Pink Tulip         |
|             |                                     |               | `oxeye`              | `8`                     | Oxeye Daisy        |
|             |                                     |               | `cornflower`         | `9`                     | Cornflower         |
|             |                                     |               | `lily_of_the_valley` | `10`                    | Lily of the Valley |

Sunflower, lilac, rose bush, and peony

| Name              | Metadata Bits             | Default value | Allowed values     | Values forMetadata Bits | Description                                               |
|-------------------|---------------------------|---------------|--------------------|-------------------------|-----------------------------------------------------------|
| double_plant_type | `0x1`<br/>`0x2`<br/>`0x4` | `sunflower`   | `sunflower`        | `0`                     | Sunflower                                                 |
|                   |                           |               | `syringa`          | `1`                     | Lilac                                                     |
|                   |                           |               | `grass`            | `2`                     | Double Tallgrass                                          |
|                   |                           |               | `fern`             | `3`                     | Large Fern                                                |
|                   |                           |               | `rose`             | `4`                     | Rose Bush                                                 |
|                   |                           |               | `paeonia`          | `5`                     | Peony                                                     |
| upper_block_bit   | `0x8`                     | `false`       | `false`<br/>`true` | `0`<br/>`1`             | If it is the upper half of the plant. For items, it is 0. |

Pitcher plant

| Name            | Metadata Bits | Default value | Allowed values     | Values forMetadata Bits | Description                           |
|-----------------|---------------|---------------|--------------------|-------------------------|---------------------------------------|
| upper_block_bit | Not Supported | `false`       | `false`<br/>`true` | `Unsupported`           | If it is the upper half of the plant. |



### Flower Pot
Bedrock Edition:

| Name       | Metadata Bits | Default value | Allowed values     | Values forMetadata Bits | Description                                                       |
|------------|---------------|---------------|--------------------|-------------------------|-------------------------------------------------------------------|
| update_bit | `0x1`         | `false`       | `false`<br/>`true` | `0`<br/>`1`             | false: Empty flower pot.<br/>true: Flower pot with contents.<br/> |



### Froglight
Java Edition:

| Name | Default value | Allowed values | Description                            |
|------|---------------|----------------|----------------------------------------|
| axis | `y`           | `x`            | The froglight is oriented east–west.   |
|      |               | `y`            | The froglight is oriented vertically.  |
|      |               | `z`            | The froglight is oriented north–south. |

Bedrock Edition:

| Name        | Metadata Bits   | Default value | Allowed values | Values forMetadata Bits | Description                            |
|-------------|-----------------|---------------|----------------|-------------------------|----------------------------------------|
| pillar_axis | `0x1`<br/>`0x2` | `y`           | `x`            | `1`                     | The froglight is oriented east–west.   |
|             |                 |               | `y`            | `0`                     | The froglight is oriented vertically.  |
|             |                 |               | `z`            | `2`                     | The froglight is oriented north–south. |



### Frosted Ice
Java Edition：

| Name | Default value | Allowed values      | Description                |
|------|---------------|---------------------|----------------------------|
| age  | `0`           | `0`                 | Freshly generated ice.     |
|      |               | `1`<br/>`2`<br/>`3` | Ice with spreading cracks. |

Bedrock Edition：

| Name | Metadata Bits   | Default value | Allowed values                                                                                    | Values forMetadata Bits | Description                |
|------|-----------------|---------------|---------------------------------------------------------------------------------------------------|-------------------------|----------------------------|
| age  | `0x1`<br/>`0x2` | `0`           | `0`                                                                                               | `0`                     | Freshly generated ice.     |
|      |                 |               | `1`<br/>`2`<br/>`3`                                                                               | `1`<br/>`2`<br/>`3`     | Ice with spreading cracks. |
|      |                 |               | `4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | `Unsupported`           | Unused                     |



### Furnace
Java Edition:

| Name   | Default value | Allowed values                            | Description                                                                                                                |
|--------|---------------|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| facing | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the furnace's opening faces.<br/>The opposite from the direction the player faces while placing the furnace. |
| lit    | `false`       | `false`<br/>`true`                        | If the furnace is lit.                                                                                                     |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values                            | Values forMetadata Bits | Description                                                                                                                |
|------------------------------|---------------|---------------|-------------------------------------------|-------------------------|----------------------------------------------------------------------------------------------------------------------------|
| minecraft:cardinal_direction | Not Supported | `south`       | `east`<br/>`north`<br/>`south`<br/>`west` | `Unsupported`           | The direction the furnace's opening faces.<br/>The opposite from the direction the player faces while placing the furnace. |



### Glass Panes
Java Edition:

| Name        | Default value | Allowed values     | Description                                                          |
|-------------|---------------|--------------------|----------------------------------------------------------------------|
| east        | `false`       | `false`<br/>`true` | When true, the glass pane extends from the center post to the east.  |
| north       | `false`       | `false`<br/>`true` | When true, the glass pane extends from the center post to the north. |
| south       | `false`       | `false`<br/>`true` | When true, the glass pane extends from the center post to the south. |
| waterlogged | `false`       | `false`<br/>`true` | Whether or not there's water in the same place as this glass pane.   |
| west        | `false`       | `false`<br/>`true` | When true, the glass pane extends from the center post to the west.  |



### Glazed Terracotta
Java Edition:

| Name   | Default value | Allowed values                            | Description                                                               |
|--------|---------------|-------------------------------------------|---------------------------------------------------------------------------|
| facing | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The opposite from the direction the player faces while placing the block. |

Bedrock Edition:

| Name             | Metadata Bits             | Default value | Allowed values              | Values forMetadata Bits     | Description                                                                                                                                             |
|------------------|---------------------------|---------------|-----------------------------|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing_direction | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `2`<br/>`3`<br/>`4`<br/>`5` | `2`<br/>`3`<br/>`4`<br/>`5` | The direction the block faces.<br/>Opposite from the direction a player faces when placing the block.2: North<br/>3: South<br/>4: West<br/>5: East<br/> |
|                  |                           |               | `0`<br/>`1`                 | `0`<br/>`1`                 | Unused                                                                                                                                                  |



### Glow Lichen
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

### 
Java Edition:

| Name  | Default value | Allowed values     | Description                                                                                                      |
|-------|---------------|--------------------|------------------------------------------------------------------------------------------------------------------|
| snowy | `false`       | `false`<br/>`true` | If true, the block uses a snowy side and top texture.<br/>In-game, this is true when asnow blockorsnowis on top. |

### Grindstone
Java Edition:

| Name   | Default value | Allowed values                            | Description                                                                                                                                 |
|--------|---------------|-------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| face   | `wall`        | `ceiling`<br/>`floor`<br/>`wall`          | What the grindstone is attached to.                                                                                                         |
| facing | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the grindstone is facing.<br/>Opposite from the direction the player faces when placing a grindstone on the floor or ceiling. |

Bedrock Edition:

| Name       | Metadata Bits   | Default value | Allowed values                                     | Values forMetadata Bits     | Description                                                                                                                                                                              |
|------------|-----------------|---------------|----------------------------------------------------|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| attachment | `0x4`<br/>`0x8` | `standing`    | `standing`<br/>`hanging`<br/>`side`<br/>`multiple` | `0`<br/>`1`<br/>`2`<br/>`3` | What the grindstone is attached to.                                                                                                                                                      |
| direction  | `0x1`<br/>`0x2` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`                        | `0`<br/>`1`<br/>`2`<br/>`3` | The direction the grindstone is facing. Opposite from the direction a player faces when placing the block.0: South facing<br/>1: West facing<br/>2: North facing<br/>3: East facing<br/> |



### Hay Bale
Java Edition:

| Name | Default value | Allowed values | Description                            |
|------|---------------|----------------|----------------------------------------|
| axis | `y`           | `x`            | The hay block is oriented east–west.   |
|      |               | `y`            | The hay block is oriented vertically.  |
|      |               | `z`            | The hay block is oriented north–south. |

Bedrock Edition:

| Name        | Metadata Bits   | Default value | Allowed values              | Values forMetadata Bits     | Description                                |
|-------------|-----------------|---------------|-----------------------------|-----------------------------|--------------------------------------------|
| pillar_axis | `0x4`<br/>`0x8` | `y`           | `x`<br/>`y`<br/>`z`         | `1`<br/>`0`<br/>`2`         | The axis along which the block is oriented |
| deprecated  | `0x1`<br/>`0x2` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3` | `0`<br/>`1`<br/>`2`<br/>`3` | Unused, has no effect in game.             |



### Hopper
Java Edition:

| Name    | Default value | Allowed values                                       | Description                                                                                                                              |
|---------|---------------|------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| enabled | `true`        | `false`<br/>`true`                                   | True if hopper can move items to and from its inventory.<br/>When the hopper is being powered by redstone current, this is set to false. |
| facing  | `down`        | `down`<br/>`east`<br/>`north`<br/>`south`<br/>`west` | The direction the hopper's output points.<br/>The hopper pushes items into containers in this direction only.                            |

Bedrock Edition:

| Name             | Metadata Bits             | Default value | Allowed values                      | Values forMetadata Bits             | Description                                                                                                                                                                                                                                                       |
|------------------|---------------------------|---------------|-------------------------------------|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing_direction | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4` | The direction the hopper's output points.<br/>The hopper pushes items into containers in this direction only.0: Output facing down<br/>1: (unused)<br/>2: Output facing north<br/>3: Output facing south<br/>4: Output facing west<br/>5: Output facing east<br/> |
| toggle_bit       | `0x8`                     | `false`       | `false`<br/>`true`                  | `0`<br/>`1`                         | 1 if hopper cannot move items to and from its inventory.<br/>When the hopper is being powered by redstone current, this is set to true.                                                                                                                           |



### Infested Block
Bedrock Edition:
Infested Deepslate:

| Name        | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                            |
|-------------|---------------|---------------|----------------|-------------------------|----------------------------------------|
| pillar_axis | Not Supported | `y`           | `x`            | `Unsupported`           | The deepslate is oriented east–west.   |
|             |               |               | `y`            | `Unsupported`           | The deepslate is oriented vertically.  |
|             |               |               | `z`            | `Unsupported`           | The deepslate is oriented north–south. |

Others:

| Name                   | Metadata Bits             | Default value | Allowed values         | Values forMetadata Bits | Description                   |
|------------------------|---------------------------|---------------|------------------------|-------------------------|-------------------------------|
| monster_egg_stone_type | `0x1`<br/>`0x2`<br/>`0x4` | `stone`       | `stone`                | `0`                     | Infested Stone                |
|                        |                           |               | `cobblestone`          | `1`                     | Infested Cobblestone          |
|                        |                           |               | `stone_brick`          | `2`                     | Infested Stone Brick          |
|                        |                           |               | `mossy_stone_brick`    | `3`                     | Infested Mossy Stone Brick    |
|                        |                           |               | `cracked_stone_brick`  | `4`                     | Infested Cracked Stone Brick  |
|                        |                           |               | `chiseled_stone_brick` | `5`                     | Infested Chiseled Stone Brick |



### Iron Bars
Java Edition:

| Name        | Default value | Allowed values     | Description                                                        |
|-------------|---------------|--------------------|--------------------------------------------------------------------|
| east        | `false`       | `false`<br/>`true` | When true, the iron bars extend from the center post to the east.  |
| north       | `false`       | `false`<br/>`true` | When true, the iron bars extend from the center post to the north. |
| south       | `false`       | `false`<br/>`true` | When true, the iron bars extend from the center post to the south. |
| waterlogged | `false`       | `false`<br/>`true` | Whether or not there's water in the same place as these iron bars. |
| west        | `false`       | `false`<br/>`true` | When true, the iron bars extend from the center post to the west.  |

### Item Frame and Glow Item Frame
Bedrock Edition
Item Frame:

| Name                 | Metadata Bits   | Default value | Allowed values     | Values forMetadata Bits | Description                         |
|----------------------|-----------------|---------------|--------------------|-------------------------|-------------------------------------|
| facing_direction     | `0x1`<br/>`0x2` | `0`           | `5`                | `0`                     | East facing item frame              |
|                      |                 |               | `4`                | `1`                     | West facing item frame              |
|                      |                 |               | `3`                | `2`                     | South facing item frame             |
|                      |                 |               | `2`                | `3`                     | North facing item frame             |
|                      |                 |               | `1`                | `Unsupported`           | Up facing item frame                |
|                      |                 |               | `0`                | `Unsupported`           | Down facing item frame              |
| item_frame_map_bit   | `0x4`           | `false`       | `false`<br/>`true` | `0`<br/>`1`             | If this item frame contains a map.  |
| item_frame_photo_bit | Not Supported   | `false`       | `false`<br/>`true` | `Unsupported`           | If this item frame contains aphoto. |

Glow Item Frame:

| Name                 | Metadata Bits | Default value | Allowed values     | Values forMetadata Bits | Description                         |
|----------------------|---------------|---------------|--------------------|-------------------------|-------------------------------------|
| facing_direction     | Not Supported | `0`           | `5`                | `Unsupported`           | East facing item frame              |
|                      |               |               | `4`                | `Unsupported`           | West facing item frame              |
|                      |               |               | `3`                | `Unsupported`           | South facing item frame             |
|                      |               |               | `2`                | `Unsupported`           | North facing item frame             |
|                      |               |               | `1`                | `Unsupported`           | Up facing item frame                |
|                      |               |               | `0`                | `Unsupported`           | Down facing item frame              |
| item_frame_map_bit   | Not Supported | `false`       | `false`<br/>`true` | `Unsupported`           | If this item frame contains a map.  |
| item_frame_photo_bit | Not Supported | `false`       | `false`<br/>`true` | `Unsupported`           | If this item frame contains aphoto. |



### Jigsaw Block
Java Edition:

| Name        | Default value | Allowed values                                                                                                                                                                    | Description                               |
|-------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| orientation | `north_up`    | `down_east`<br/>`down_north`<br/>`down_south`<br/>`down_west`<br/>`east_up`<br/>`north_up`<br/>`south_up`<br/>`up_east`<br/>`up_north`<br/>`up_south`<br/>`up_west`<br/>`west_up` | The direction the jigsaw block is facing. |

Bedrock Edition:

| Name             | Metadata Bits | Default value | Allowed values                              | Values forMetadata Bits | Description                               |
|------------------|---------------|---------------|---------------------------------------------|-------------------------|-------------------------------------------|
| facing_direction | Not Supported | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | `Unsupported`           | The direction the jigsaw block is facing. |
| rotation         | Not Supported | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`                 | `Unsupported`           | The rotation around the axis.             |



### 
Java Edition:

| Name   | Default value | Allowed values                            | Description                                                                                                                                      |
|--------|---------------|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| facing | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the jack o'lantern's carved face is facing.<br/>The opposite from the direction the player faces while placing the jack o'lantern. |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values                            | Values forMetadata Bits | Description                                                                                                                                      |
|------------------------------|---------------|---------------|-------------------------------------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| minecraft:cardinal_direction | Not Supported | `south`       | `east`<br/>`north`<br/>`south`<br/>`west` | `Unsupported`           | The direction the jack o'lantern's carved face is facing.<br/>The opposite from the direction the player faces while placing the jack o'lantern. |



### Jukebox
Java Edition:

| Name       | Default value | Allowed values     | Description                                 |
|------------|---------------|--------------------|---------------------------------------------|
| has_record | `false`       | `false`<br/>`true` | True when the jukebox contains amusic disc. |



### Kelp
Java Edition:
Top kelp block:

| Name | Default value | Allowed values                                                                                                                                                                                                              | Description                                                                                                                                                                                                 |
|------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| age  | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15`<br/>`16`<br/>`17`<br/>`18`<br/>`19`<br/>`20`<br/>`21`<br/>`22`<br/>`23`<br/>`24`<br/>`25` | A freshly planted kelp starts with a random age between 0 and 24.<br/>Below age 25, a kelp may try go grow more kelp above it with the same age value incremented by one.<br/>Kelp stops growing at age 25. |

Bedrock Edition:

| Name     | Metadata Bits                       | Default value | Allowed values                                                                                                                    | Values forMetadata Bits                                                                                                           | Description                                                                                |
|----------|-------------------------------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| kelp_age | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | The age of the kelp. The kelp renders as a non-top piece if there's another kelp above it. |
|          |                                     |               | `16`<br/>`17`<br/>`18`<br/>`19`<br/>`20`<br/>`21`<br/>`22`<br/>`23`<br/>`24`<br/>`25`                                             | `Unsupported`                                                                                                                     | Unused                                                                                     |



### Ladder
Java Edition:

| Name        | Default value | Allowed values                            | Description                                                            |
|-------------|---------------|-------------------------------------------|------------------------------------------------------------------------|
| facing      | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction from the block the ladder is attached to, to the ladder. |
| waterlogged | `false`       | `false`<br/>`true`                        | Whether or not there's water in the same place as this ladder.         |

Bedrock Edition:

| Name             | Metadata Bits             | Default value | Allowed values              | Values forMetadata Bits     | Description                                                                                                                                                                      |
|------------------|---------------------------|---------------|-----------------------------|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing_direction | `0x1`<br/>`0x2`<br/>`0x4` | `2`           | `2`<br/>`3`<br/>`4`<br/>`5` | `2`<br/>`3`<br/>`4`<br/>`5` | The direction from the block the ladder is attached to, to the ladder.2: Ladder facing north<br/>3: Ladder facing south<br/>4: Ladder facing west<br/>5: Ladder facing east<br/> |
|                  |                           |               | `0`<br/>`1`                 | `0`<br/>`1`                 | Unused                                                                                                                                                                           |

### Lantern and Soul Lantern
Java Edition:

| Name        | Default value | Allowed values     | Description                                                     |
|-------------|---------------|--------------------|-----------------------------------------------------------------|
| hanging     | `false`       | `false`<br/>`true` | If the lantern is hanging from a block.                         |
| waterlogged | `false`       | `false`<br/>`true` | Whether or not there's water in the same place as this lantern. |

Bedrock Edition:

| Name    | Metadata Bits | Default value | Allowed values     | Values forMetadata Bits | Description                             |
|---------|---------------|---------------|--------------------|-------------------------|-----------------------------------------|
| hanging | `0x1`         | `false`       | `false`<br/>`true` | `0`<br/>`1`             | If the lantern is hanging from a block. |



### Lava
Java Edition:

| Name  | Default value | Allowed values                                                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| level | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | If bit 0x8 is set, this fluid is "falling" and spreads only downward. At this level, the lower bits are essentially ignored, since this block is then at its highest fluid level. This level is equal to the falling lava above, equal to 8 plus the level of the non-falling lava above it.The lower three bits are the fluid block's level. 0 is the highest fluid level (not necessarily filling the block - this depends on the neighboring fluid blocks above each upper corner of the block). Data values increase as the fluid level of the block drops: 1 is the next highest, 2 lower, on through 7, the lowest fluid level. Along a line on a flat plane, lava drops one level per meter in the Nether and two everywhere else. So inthe EndandOverworld, only 2, 4 and 6 are used. |

Bedrock Edition:
Lava and flowing lava

| Name         | Metadata Bits                       | Default value | Allowed values                                                                                                                    | Values forMetadata Bits                                                                                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|--------------|-------------------------------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| liquid_depth | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | If bit 0x8 is set, this fluid is "falling" and spreads only downward. At this level, the lower bits are essentially ignored, since this block is then at its highest fluid level. This level is equal to the falling lava above, equal to 8 plus the level of the non-falling lava above it.The lower three bits are the fluid block's level. 0 is the highest fluid level (not necessarily filling the block - this depends on the neighboring fluid blocks above each upper corner of the block). Data values increase as the fluid level of the block drops: 1 is the next highest, 2 lower, on through 7, the lowest fluid level. Along a line on a flat plane, lava drops one level per meter in the Nether and two everywhere else. So inthe EndandOverworld, only 2, 4 and 6 are used. |



### Leaves
Java Edition:

| Name        | Default value | Allowed values                                      | Description                                                                                    |
|-------------|---------------|-----------------------------------------------------|------------------------------------------------------------------------------------------------|
| distance    | `7`           | `1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7` | How far away this block is from the nearest log or wood, intaxicab distance.                   |
| persistent  | `false`       | `false`<br/>`true`                                  | If the block persists regardless of having no wood nearby.<br/>`true`for player-placed leaves. |
| waterlogged | `false`       | `false`<br/>`true`                                  | Whether or not there's water in the same place as this leaves.                                 |

Bedrock Edition:

| Name           | Metadata Bits | Default value | Allowed values     | Values forMetadata Bits | Description                                                |
|----------------|---------------|---------------|--------------------|-------------------------|------------------------------------------------------------|
| persistent_bit | Not Supported | `false`       | `false`<br/>`true` | `Unsupported`           | If the block persists regardless of having no wood nearby. |
| update_bit     | Not Supported | `false`       | `false`<br/>`true` | `Unsupported`           | If the block checks for nearby wood and decays.            |



### Lectern
Java Edition:

| Name     | Default value | Allowed values                            | Description                                                                                                          |
|----------|---------------|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| facing   | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the lectern is facing.<br/>The opposite from the direction the player faces while placing the lectern. |
| has_book | `false`       | `false`<br/>`true`                        | If the lectern currently has a book.                                                                                 |
| powered  | `false`       | `false`<br/>`true`                        | If the lectern is currently outputting a redstone signal.                                                            |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values                            | Values forMetadata Bits | Description                                                                                                          |
|------------------------------|---------------|---------------|-------------------------------------------|-------------------------|----------------------------------------------------------------------------------------------------------------------|
| minecraft:cardinal_direction | Not Supported | `south`       | `east`<br/>`north`<br/>`south`<br/>`west` | `Unsupported`           | The direction the lectern is facing.<br/>The opposite from the direction the player faces while placing the lectern. |
| powered_bit                  | `0x4`         | `false`       | `false`<br/>`true`                        | `0`<br/>`1`             | If the lectern is currently outputting a redstone signal.                                                            |



### Lever
Java Edition:

| Name    | Default value | Allowed values                            | Description                                                                                                                           |
|---------|---------------|-------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| face    | `wall`        | `ceiling`<br/>`floor`<br/>`wall`          | The face of the block the lever placed on.<br/>Floor is on top of a block, ceiling is on the bottom, and wall is on one of its sides. |
| facing  | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the lever is facing.<br/>Opposite to the direction the player is facing if placed on the side of a block.               |
| powered | `false`       | `false`<br/>`true`                        | If true, the lever is currently activated.                                                                                            |

Bedrock Edition:

| Name            | Metadata Bits             | Default value    | Allowed values     | Values forMetadata Bits | Description                                  |
|-----------------|---------------------------|------------------|--------------------|-------------------------|----------------------------------------------|
| open_bit        | `0x8`                     | `false`          | `false`<br/>`true` | `0`<br/>`1`             | If the lever is currently activated.         |
| lever_direction | `0x1`<br/>`0x2`<br/>`0x4` | `down_east_west` | `down_east_west`   | `0`                     | Lever on block bottom points east when off   |
|                 |                           |                  | `east`             | `1`                     | Lever on block side facing east              |
|                 |                           |                  | `west`             | `2`                     | Lever on block side facing west              |
|                 |                           |                  | `south`            | `3`                     | Lever on block side facing south             |
|                 |                           |                  | `north`            | `4`                     | Lever on block side facing north             |
|                 |                           |                  | `up_north_south`   | `5`                     | Lever on block top points south when off.    |
|                 |                           |                  | `up_east_west`     | `6`                     | Lever on block top points east when off.     |
|                 |                           |                  | `down_north_south` | `7`                     | Lever on block bottom points south when off. |



### Light Block
Java Edition:

| Name        | Default value | Allowed values                                                                                                                    | Description                                                         |
|-------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| waterlogged | `false`       | `true`<br/>`false`                                                                                                                | Whether or not there's water in the same place as this light block. |
| level       | `15`          | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | The amount of light this block outputs.                             |

Bedrock Edition:

| Name              | Metadata Bits                       | Default value | Allowed values                                                                                                                    | Values forMetadata Bits                                                                                                           | Description                             |
|-------------------|-------------------------------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| block_light_level | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | The amount of light this block outputs. |



### Lightning Rod
Java Edition:

| Name        | Default value | Allowed values                                                | Description                                                                  |
|-------------|---------------|---------------------------------------------------------------|------------------------------------------------------------------------------|
| facing      | `up`          | `up`<br/>`down`<br/>`north`<br/>`south`<br/>`east`<br/>`west` | The direction that the lightning rod is facing, determined by its anchoring. |
| powered     | `false`       | `false`<br/>`true`                                            | Whether or not the lightning rod is powered.                                 |
| waterlogged | `false`       | `false`<br/>`true`                                            | Whether or not there's water in the same place as this lightning rod.        |

Bedrock Edition:

| Name             | Metadata Bits | Default value | Allowed values                              | Values forMetadata Bits | Description                                                                                                    |
|------------------|---------------|---------------|---------------------------------------------|-------------------------|----------------------------------------------------------------------------------------------------------------|
| facing_direction | Not Supported | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | `Unsupported`           | The direction the lightning rod faces.0: Down<br/>1: Up<br/>2: North<br/>3: South<br/>4: West<br/>5: East<br/> |



### Logs
Java Edition:

| Name | Default value | Allowed values | Description                              |
|------|---------------|----------------|------------------------------------------|
| axis | `y`           | `x`            | The log or stem is oriented east–west.   |
|      |               | `y`            | The log or stem is oriented vertically.  |
|      |               | `z`            | The log or stem is oriented north–south. |

Bedrock Edition:

| Name        | Metadata Bits   | Default value | Allowed values | Values forMetadata Bits | Description                      |
|-------------|-----------------|---------------|----------------|-------------------------|----------------------------------|
| pillar_axis | `0x1`<br/>`0x2` | `y`           | `y`            | `0`                     | The log is oriented vertically.  |
|             |                 |               | `x`            | `1`                     | The log is oriented east–west.   |
|             |                 |               | `z`            | `2`                     | The log is oriented north–south. |



### Loom
Java Edition:

| Name   | Default value | Allowed values                            | Description                                                                                             |
|--------|---------------|-------------------------------------------|---------------------------------------------------------------------------------------------------------|
| facing | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the loom is facing.<br/>Opposite from the direction the player faces when placing a loom. |

Bedrock Edition:

| Name      | Metadata Bits   | Default value | Allowed values              | Values forMetadata Bits     | Description                                                                                                                         |
|-----------|-----------------|---------------|-----------------------------|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| direction | `0x1`<br/>`0x2` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3` | `0`<br/>`1`<br/>`2`<br/>`3` | The direction the loom is facing.0: South facing loom<br/>1: West facing loom<br/>2: North facing loom<br/>3: East facing loom<br/> |



### Mangrove Roots
Java Edition:

| Name        | Default value | Allowed values     | Description                                                            |
|-------------|---------------|--------------------|------------------------------------------------------------------------|
| waterlogged | `false`       | `false`<br/>`true` | Whether or not there's water in the same place as this mangrove roots. |



### Melon Stem
Java Edition:
Growing

| Name | Default value | Allowed values                              | Description                                       |
|------|---------------|---------------------------------------------|---------------------------------------------------|
| age  | `0`           | `0`                                         | A newly planted stem.                             |
|      |               | `1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6` | Intermediate growth stages of the stem.           |
|      |               | `7`                                         | A fully mature stem, capable of producing melons. |

Attached

| Name   | Default value | Allowed values                            | Description                               |
|--------|---------------|-------------------------------------------|-------------------------------------------|
| facing | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction from the stem to the melon. |

Bedrock Edition:

| Name             | Metadata Bits             | Default value | Allowed values                              | Values forMetadata Bits                     | Description                                       |
|------------------|---------------------------|---------------|---------------------------------------------|---------------------------------------------|---------------------------------------------------|
| growth           | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`                                         | `0`                                         | A newly planted stem.                             |
|                  |                           |               | `1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6` | `1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6` | Intermediate growth stages of the stem.           |
|                  |                           |               | `7`                                         | `7`                                         | A fully mature stem, capable of producing melons. |
| facing_direction | Not Supported             | `0`           | `0`<br/>`1`                                 | `Unsupported`                               | Unused                                            |
|                  |                           |               | `2`                                         | `Unsupported`                               | Stem pointing north.                              |
|                  |                           |               | `3`                                         | `Unsupported`                               | Stem pointing south.                              |
|                  |                           |               | `4`                                         | `Unsupported`                               | Stem pointing west.                               |
|                  |                           |               | `5`                                         | `Unsupported`                               | Stem pointing east.                               |



### Mob heads
Java Edition:
Floor

| Name     | Default value | Allowed values | Description                            |
|----------|---------------|----------------|----------------------------------------|
| powered  | `false`       | `true`         | The block receives a redstone signal.  |
|          |               | `false`        | The block receives no redstone signal. |
| rotation | `0`           | `0`            | The block is facing south.             |
|          |               | `1`            | The block is facing south-southwest.   |
|          |               | `2`            | The block is facing southwest.         |
|          |               | `3`            | The block is facing west-southwest.    |
|          |               | `4`            | The block is facing west.              |
|          |               | `5`            | The block is facing west-northwest.    |
|          |               | `6`            | The block is facing northwest.         |
|          |               | `7`            | The block is facing north-northwest.   |
|          |               | `8`            | The block is facing north.             |
|          |               | `9`            | The block is facing north-northeast.   |
|          |               | `10`           | The block is facing northeast.         |
|          |               | `11`           | The block is facing east-northeast.    |
|          |               | `12`           | The block is facing east.              |
|          |               | `13`           | The block is facing east-southeast.    |
|          |               | `14`           | The block is facing southeast.         |
|          |               | `15`           | The block is facing south-southeast.   |

Wall

| Name    | Default value | Allowed values                            | Description                                                                                           |
|---------|---------------|-------------------------------------------|-------------------------------------------------------------------------------------------------------|
| powered | `false`       | `true`                                    | The block receives a redstone signal.                                                                 |
|         |               | `false`                                   | The block receives no redstone signal.                                                                |
| facing  | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the head is facing.<br/>Opposite from the direction a player is facing when placing it. |

Bedrock Edition:

| Name             | Metadata Bits             | Default value | Allowed values | Values forMetadata Bits | Description                                          |
|------------------|---------------------------|---------------|----------------|-------------------------|------------------------------------------------------|
| facing_direction | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `1`            | `1`                     | On the floor (rotation is stored in the tile entity) |
|                  |                           |               | `2`            | `2`                     | On a wall, facing north                              |
|                  |                           |               | `3`            | `3`                     | On a wall, facing south                              |
|                  |                           |               | `4`            | `4`                     | On a wall, facing east                               |
|                  |                           |               | `5`            | `5`                     | On a wall, facing west                               |
|                  |                           |               | `0`            | `0`                     | Unused                                               |



### Muddy Mangrove Roots
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

### Mushroom Blocks
Java Edition:

| Name  | Default value | Allowed values     | Description                                                                                         |
|-------|---------------|--------------------|-----------------------------------------------------------------------------------------------------|
| east  | `true`        | `false`<br/>`true` | /If true, the east face has the cap/stem texture.<br/>If false, it has the pores texture instead.   |
| down  | `true`        | `false`<br/>`true` | /If true, the bottom face has the cap/stem texture.<br/>If false, it has the pores texture instead. |
| north | `true`        | `false`<br/>`true` | /If true, the north face has the cap/stem texture.<br/>If false, it has the pores texture instead.  |
| south | `true`        | `false`<br/>`true` | /If true, the south face has the cap/stem texture.<br/>If false, it has the pores texture instead.  |
| up    | `true`        | `false`<br/>`true` | /If true, the top face has the cap/stem texture.<br/>If false, it has the pores texture instead.    |
| west  | `true`        | `false`<br/>`true` | /If true, the west face has the cap/stem texture.<br/>If false, it has the pores texture instead.   |

Bedrock Edition:

| Name               | Metadata Bits                       | Default value | Allowed values         | Values forMetadata Bits | Description                                                                                         |
|--------------------|-------------------------------------|---------------|------------------------|-------------------------|-----------------------------------------------------------------------------------------------------|
| huge_mushroom_bits | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8` | `0`           | `0`                    | `0`                     | All six faces have the pores texture.                                                               |
|                    |                                     |               | `1`                    | `1`                     | Cap texture on top, west and north; pores on other sides.                                           |
|                    |                                     |               | `2`                    | `2`                     | Cap texture on top and north; pores on other sides.                                                 |
|                    |                                     |               | `3`                    | `3`                     | Cap texture on top, north and east; pores on other sides.                                           |
|                    |                                     |               | `4`                    | `4`                     | Cap texture on top and west; pores on other sides.                                                  |
|                    |                                     |               | `5`                    | `5`                     | Cap texture on top; pores on other sides.                                                           |
|                    |                                     |               | `6`                    | `6`                     | Cap texture on top and east; pores on other sides.                                                  |
|                    |                                     |               | `7`                    | `7`                     | Cap texture on top, south and west; pores on other sides.                                           |
|                    |                                     |               | `8`                    | `8`                     | Cap texture on top and south; pores on other sides.                                                 |
|                    |                                     |               | `9`                    | `9`                     | Cap texture on top, east and south; pores on other sides.                                           |
|                    |                                     |               | `10`                   | `10`                    | The four side faces have the stem texture,<br/>and the top and bottom faces have the pores texture. |
|                    |                                     |               | `11`<br/>`12`<br/>`13` | `11`<br/>`12`<br/>`13`  | All six faces have the pores texture.                                                               |
|                    |                                     |               | `14`                   | `14`                    | All six faces have the cap texture.                                                                 |
|                    |                                     |               | `15`                   | `15`                    | All six faces have the stem texture.                                                                |



### Nether Wart
| Name | Default value | Allowed values | Description  |
|------|---------------|----------------|--------------|
| age  | `0`           | `0`            |              |
|      |               | `1`<br/>`2`    |              |
|      |               | `3`            | Fully grown. |

Bedrock Edition:

| Name | Metadata Bits   | Default value | Allowed values                                                                                    | Values forMetadata Bits | Description  |
|------|-----------------|---------------|---------------------------------------------------------------------------------------------------|-------------------------|--------------|
| age  | `0x1`<br/>`0x2` | `0`           | `0`                                                                                               | `0`                     |              |
|      |                 |               | `1`<br/>`2`                                                                                       | `1`<br/>`2`             |              |
|      |                 |               | `3`                                                                                               | `3`                     | Fully grown. |
|      |                 |               | `4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | `Unsupported`           | Unused       |



### Nether Portal
Java Edition:

| Name | Default value | Allowed values | Description                              |
|------|---------------|----------------|------------------------------------------|
| axis | `x`           | `x`            | The portal's long edge runs east–west.   |
|      |               | `z`            | The portal's long edge runs north–south. |

Bedrock Edition:

| Name        | Metadata Bits   | Default value | Allowed values | Values forMetadata Bits | Description                                                                                                                               |
|-------------|-----------------|---------------|----------------|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| portal_axis | `0x1`<br/>`0x2` | `unknown`     | `unknown`      | `0`                     | If placed with this state, the portal's long edge runs north–south. If set to it, its direction will be tied to that of adjacent portals. |
|             |                 |               | `x`            | `1`                     | The portal's long edge runs east–west.                                                                                                    |
|             |                 |               | `z`            | `2`                     | The portal's long edge runs north–south.                                                                                                  |



### Note Block
Java Edition:

| Name       | Default value | Allowed values                                                                                                                                                                                                                                                                                                            | Description                                    |
|------------|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| instrument | `harp`        | `banjo`<br/>`basedrum`<br/>`bass`<br/>`bell`<br/>`bit`<br/>`chime`<br/>`cow_bell`<br/>`creeper`<br/>`custom_head`<br/>`didgeridoo`<br/>`dragon`<br/>`flute`<br/>`guitar`<br/>`harp`<br/>`hat`<br/>`iron_xylophone`<br/>`piglin`<br/>`pling`<br/>`skeleton`<br/>`snare`<br/>`wither_skeleton`<br/>`xylophone`<br/>`zombie` | The instrument of the note block.              |
| note       | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15`<br/>`16`<br/>`17`<br/>`18`<br/>`19`<br/>`20`<br/>`21`<br/>`22`<br/>`23`<br/>`24`                                                                                                        | The pitch of the note block                    |
| powered    | `false`       | `false`<br/>`true`                                                                                                                                                                                                                                                                                                        | True if the note block is currently activated. |



### Observer
Java Edition:

| Name    | Default value | Allowed values                                                | Description                                                                                          |
|---------|---------------|---------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| facing  | `south`       | `down`<br/>`east`<br/>`north`<br/>`south`<br/>`up`<br/>`west` | The direction the observer is observing. The same direction the player faces when placing the block. |
| powered | `false`       | `false`<br/>`true`                                            | True while the observer is observing a change and emitting a pulse.                                  |

Bedrock Edition:

| Name                       | Metadata Bits | Default value | Allowed values                                                | Values forMetadata Bits | Description                                                                                          |
|----------------------------|---------------|---------------|---------------------------------------------------------------|-------------------------|------------------------------------------------------------------------------------------------------|
| minecraft:facing_direction | Not Supported | `down`        | `down`<br/>`east`<br/>`north`<br/>`south`<br/>`up`<br/>`west` | `Unsupported`           | The direction the observer is observing. The same direction the player faces when placing the block. |
| powered_bit                | `0x8`         | `false`       | `false`<br/>`true`                                            | `0`<br/>`1`             | True while the observer is observing a change and emitting a pulse.                                  |



### Pink Petals
Java Edition:

| Name          | Default value | Allowed values                            | Description                                                                                                                   |
|---------------|---------------|-------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| facing        | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the pink petals are facing.<br/>The opposite from the direction the player faces while placing the pink petals. |
| flower_amount | `1`           | `1`<br/>`2`<br/>`3`<br/>`4`               | The amount of pink petals in the block.                                                                                       |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values                                              | Values forMetadata Bits | Description                                                                                                                   |
|------------------------------|---------------|---------------|-------------------------------------------------------------|-------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| growth                       | Not Supported | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7` | `Unsupported`           | The amount of pink petals in the block. A value greater than 3 can only be obtained via commands.                             |
| minecraft:cardinal_direction | Not Supported | `south`       | `east`<br/>`north`<br/>`south`<br/>`west`                   | `Unsupported`           | The direction the pink petals are facing.<br/>The opposite from the direction the player faces while placing the pink petals. |



### Pistons
Java Edition:

| Name     | Default value | Allowed values                                                | Description                                                                                                               |
|----------|---------------|---------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| extended | `false`       | `false`<br/>`true`                                            | If true, the piston is extended.                                                                                          |
| facing   | `north`       | `down`<br/>`east`<br/>`north`<br/>`south`<br/>`up`<br/>`west` | The direction the piston head is pointing.<br/>The opposite from the direction the player faces while placing the piston. |

Bedrock Edition:

| Name             | Metadata Bits             | Default value | Allowed values                              | Values forMetadata Bits                     | Description                                                                                                                                             |
|------------------|---------------------------|---------------|---------------------------------------------|---------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing_direction | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | The direction the piston is pointing.0: facing down<br/>1: facing up<br/>2: facing south<br/>3: facing north<br/>4: facing east<br/>5: facing west<br/> |

#### Moving piston
Java Edition:

| Name   | Default value | Allowed values                                                | Description                                            |
|--------|---------------|---------------------------------------------------------------|--------------------------------------------------------|
| facing | `north`       | `down`<br/>`east`<br/>`north`<br/>`south`<br/>`up`<br/>`west` | The direction the block is being pushed by the piston. |
| type   | `normal`      | `normal`<br/>`sticky`                                         | What piston base this has.                             |



#### Piston head
Java Edition:

| Name   | Default value | Allowed values                                                | Description                                                 |
|--------|---------------|---------------------------------------------------------------|-------------------------------------------------------------|
| facing | `north`       | `down`<br/>`east`<br/>`north`<br/>`south`<br/>`up`<br/>`west` | The direction the piston head is pointing.                  |
| short  | `false`       | `false`<br/>`true`                                            | If true, the piston arm is shorter than usual, by 4 pixels. |
| type   | `normal`      | `normal`<br/>`sticky`                                         | The type of piston head.                                    |

Bedrock Edition:
Piston Head:

| Name             | Metadata Bits             | Default value | Allowed values                              | Values forMetadata Bits                     | Description                                                                                                                                                  |
|------------------|---------------------------|---------------|---------------------------------------------|---------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing_direction | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | The direction the piston head is pointing.0: facing up<br/>1: facing down<br/>2: facing south<br/>3: facing north<br/>4: facing east<br/>5: facing west<br/> |

Sticky Piston Head:

| Name             | Metadata Bits | Default value | Allowed values                              | Values forMetadata Bits | Description                                                                                                                                                  |
|------------------|---------------|---------------|---------------------------------------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing_direction | Not Supported | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | `Unsupported`           | The direction the piston head is pointing.0: facing up<br/>1: facing down<br/>2: facing south<br/>3: facing north<br/>4: facing east<br/>5: facing west<br/> |



### Potatoes
Java Edition:

| Name | Default value | Allowed values      | Description  |
|------|---------------|---------------------|--------------|
| age  | `0`           | `0`<br/>`1`         |              |
|      |               | `2`<br/>`3`         |              |
|      |               | `4`<br/>`5`<br/>`6` |              |
|      |               | `7`                 | Fully grown. |

Bedrock Edition:

| Name   | Metadata Bits             | Default value | Allowed values      | Values forMetadata Bits | Description  |
|--------|---------------------------|---------------|---------------------|-------------------------|--------------|
| growth | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`<br/>`1`         | `0`<br/>`1`             |              |
|        |                           |               | `2`<br/>`3`         | `2`<br/>`3`             |              |
|        |                           |               | `4`<br/>`5`<br/>`6` | `4`<br/>`5`<br/>`6`     |              |
|        |                           |               | `7`                 | `7`                     | Fully grown. |



### Pointed Dripstone
Java Edition:

| Name               | Default value | Allowed values     | Description                                                               |
|--------------------|---------------|--------------------|---------------------------------------------------------------------------|
| thickness          | `tip`         | `tip_merge`        |                                                                           |
|                    |               | `tip`              |                                                                           |
|                    |               | `frustum`          |                                                                           |
|                    |               | `middle`           |                                                                           |
|                    |               | `base`             |                                                                           |
| vertical_direction | `up`          | `up`<br/>`down`    | The direction of the pointed dripstone.                                   |
| waterlogged        | `false`       | `true`<br/>`false` | Whether or not there's water in the same place as this pointed dripstone. |

Bedrock Edition:

| Name                | Metadata Bits | Default value | Allowed values     | Values forMetadata Bits | Description                                            |
|---------------------|---------------|---------------|--------------------|-------------------------|--------------------------------------------------------|
| dripstone_thickness | Not Supported | `tip`         | `merge`            | `Unsupported`           |                                                        |
|                     |               |               | `tip`              | `Unsupported`           |                                                        |
|                     |               |               | `frustum`          | `Unsupported`           |                                                        |
|                     |               |               | `middle`           | `Unsupported`           |                                                        |
|                     |               |               | `base`             | `Unsupported`           |                                                        |
| hanging             | Not Supported | `true`        | `false`<br/>`true` | `Unsupported`           | Whether or not the pointed dripstone is pointing down. |



### Pressure Plates
Java Edition:

** Stone and wooden pressure plates **
| Name    | Default value | Allowed values     | Description                                           |
|---------|---------------|--------------------|-------------------------------------------------------|
| powered | `false`       | `false`<br/>`true` | True if pressure plate is depressed, providing power. |

** Weighted pressure plates **
| Name  | Default value | Allowed values                                                                                                                    | Description                                                                                 |
|-------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| power | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | Specifies the redstone power level currently being produced by the weighted pressure plate. |

Bedrock Edition:

** Stone and wooden pressure plates **
| Name            | Metadata Bits | Default value | Allowed values                                                                                                    | Values forMetadata Bits | Description                                      |
|-----------------|---------------|---------------|-------------------------------------------------------------------------------------------------------------------|-------------------------|--------------------------------------------------|
| redstone_signal | `0x1`         | `0`           | `0`<br/>`1`                                                                                                       | `0`<br/>`1`             | Specifies whether the pressure plate is pressed. |
|                 |               |               | `2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | `Unsupported`           | Unused                                           |

** Weighted pressure plates **
| Name            | Metadata Bits                       | Default value | Allowed values                                                                                                                    | Values forMetadata Bits                                                                                                           | Description                                                                        |
|-----------------|-------------------------------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| redstone_signal | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | Specifies the redstone power level currently being produced by the pressure plate. |

### Prismarine
Bedrock Edition:

| Name                  | Metadata Bits   | Default value | Allowed values | Values forMetadata Bits | Description       |
|-----------------------|-----------------|---------------|----------------|-------------------------|-------------------|
| prismarine_block_type | `0x1`<br/>`0x2` | `default`     | `bricks`       | `2`                     | Prismarine Bricks |
|                       |                 |               | `dark`         | `1`                     | Dark Prismarine   |
|                       |                 |               | `default`      | `0`                     | Prismarine        |



### Pumpkin and Carved Pumpkin
Java Edition:
Carved pumpkin:

| Name   | Default value | Allowed values                            | Description                                                                                                                        |
|--------|---------------|-------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| facing | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the pumpkin's carved face is facing.<br/>The opposite from the direction the player faces while placing the pumpkin. |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values                            | Values forMetadata Bits | Description                                                                                                                                                                            |
|------------------------------|---------------|---------------|-------------------------------------------|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| minecraft:cardinal_direction | Not Supported | `south`       | `east`<br/>`north`<br/>`south`<br/>`west` | `Unsupported`           | The direction the pumpkin and carved pumpkin are facing.<br/>The opposite from the direction the player faces while placing the pumpkins. Though it doesn't affect the pumpkin at all. |



#### Pumpkin Stem
Java Edition:
Growing

| Name | Default value | Allowed values                              | Description                                         |
|------|---------------|---------------------------------------------|-----------------------------------------------------|
| age  | `0`           | `0`                                         | A newly planted stem.                               |
|      |               | `1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6` | Intermediate growth stages of the stem.             |
|      |               | `7`                                         | A fully mature stem, capable of producing pumpkins. |

Attached

| Name   | Default value | Allowed values                            | Description                                 |
|--------|---------------|-------------------------------------------|---------------------------------------------|
| facing | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction from the stem to the pumpkin. |

Bedrock Edition:

| Name             | Metadata Bits             | Default value | Allowed values                              | Values forMetadata Bits                     | Description                                         |
|------------------|---------------------------|---------------|---------------------------------------------|---------------------------------------------|-----------------------------------------------------|
| growth           | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`                                         | `0`                                         | A newly planted stem.                               |
|                  |                           |               | `1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6` | `1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6` | Intermediate growth stages of the stem.             |
|                  |                           |               | `7`                                         | `7`                                         | A fully mature stem, capable of producing pumpkins. |
| facing_direction | Not Supported             | `0`           | `0`<br/>`1`                                 | `Unsupported`                               | Unused                                              |
|                  |                           |               | `2`                                         | `Unsupported`                               | Stem pointing north.                                |
|                  |                           |               | `3`                                         | `Unsupported`                               | Stem pointing south.                                |
|                  |                           |               | `4`                                         | `Unsupported`                               | Stem pointing west.                                 |
|                  |                           |               | `5`                                         | `Unsupported`                               | Stem pointing east.                                 |



### Purpur and Quartz Pillar
Bedrock Edition:

| Name        | Metadata Bits   | Default value | Allowed values | Values forMetadata Bits | Description                               |
|-------------|-----------------|---------------|----------------|-------------------------|-------------------------------------------|
| chisel_type | `0x1`<br/>`0x2` | `default`     | `default`      | `0`                     | Purpur Block                              |
|             |                 |               | `chiseled`     | `1`                     | Chiseled Purpur(Unused)                   |
|             |                 |               | `lines`        | `2`                     | Purpur Pillar                             |
|             |                 |               | `smooth`       | `3`                     | Smooth Purpur(Unused)                     |
| pillar_axis | `0x4`<br/>`0x8` | `y`           | `x`            | `1`                     | The purpur block is oriented east–west.   |
|             |                 |               | `y`            | `0`                     | The purpur block is oriented vertically.  |
|             |                 |               | `z`            | `2`                     | The purpur block is oriented north–south. |



### Rails
#### Rail
Java Edition:

| Name        | Default value | Allowed values                                                                                    | Description                                                                                                                                            |
|-------------|---------------|---------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| shape       | `north_south` | `east_west`<br/>`north_east`<br/>`north_south`<br/>`north_west`<br/>`south_east`<br/>`south_west` | The two directions a rail connects to.<br/>For example, a`south_east`rail is a curved rail that connects to the south and to the east.                 |
|             |               | `ascending_east`<br/>`ascending_north`<br/>`ascending_south`<br/>`ascending_west`                 | A rail that ascendstowardthe direction noted.<br/>For example, an`ascending_west`rail is a straight rail that goes upward from the easttowardthe west. |
| waterlogged | `false`       | `true`<br/>`false`                                                                                | Whether or not there's water in the same place as this rail.                                                                                           |

Bedrock Edition:

| Name           | Metadata Bits                       | Default value | Allowed values | Values forMetadata Bits | Description                                      |
|----------------|-------------------------------------|---------------|----------------|-------------------------|--------------------------------------------------|
| rail_direction | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8` | `0`           | `0`            | `0`                     | Straight rail connecting to the north and south. |
|                |                                     |               | `1`            | `1`                     | Straight rail connecting to the east and west.   |
|                |                                     |               | `2`            | `2`                     | Sloped rail ascending to the east.               |
|                |                                     |               | `3`            | `3`                     | Sloped rail ascending to the west.               |
|                |                                     |               | `4`            | `4`                     | Sloped rail ascending to the north.              |
|                |                                     |               | `5`            | `5`                     | Sloped rail ascending to the south.              |
|                |                                     |               | `6`            | `6`                     | Curved rail connecting to the south and east.    |
|                |                                     |               | `7`            | `7`                     | Curved rail connecting to the south and west.    |
|                |                                     |               | `8`            | `8`                     | Curved rail connecting to the north and west.    |
|                |                                     |               | `9`            | `9`                     | Curved rail connecting to the north and east.    |

#### 
Java Edition:

| Name        | Default value | Allowed values                                                                    | Description                                                                                                                                            |
|-------------|---------------|-----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| powered     | `false`       | `false`<br/>`true`                                                                | True if rail is activated.                                                                                                                             |
| shape       | `north_south` | `east_west`<br/>`north_south`                                                     | Specifies the rail's orientation.                                                                                                                      |
|             |               | `ascending_east`<br/>`ascending_north`<br/>`ascending_south`<br/>`ascending_west` | A rail that ascendstowardthe direction noted.<br/>For example, an`ascending_west`rail is a straight rail that goes upward from the easttowardthe west. |
| waterlogged | `false`       | `false`<br/>`true`                                                                | Whether or not there's water in the same place as this rail.                                                                                           |

Bedrock Edition:

| Name           | Metadata Bits             | Default value | Allowed values              | Values forMetadata Bits | Description                         |
|----------------|---------------------------|---------------|-----------------------------|-------------------------|-------------------------------------|
| rail_data_bit  | `0x8`                     | `false`       | `false`<br/>`true`          | `0`<br/>`1`             | True if rail is activated.          |
| rail_direction | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`                         | `0`                     | flat track going north-south        |
|                |                           |               | `1`                         | `1`                     | flat track going east-west          |
|                |                           |               | `2`                         | `2`                     | sloped track ascending to the east  |
|                |                           |               | `3`                         | `3`                     | sloped track ascending to the west  |
|                |                           |               | `4`                         | `4`                     | sloped track ascending to the north |
|                |                           |               | `5`                         | `5`                     | sloped track ascending to the south |
|                |                           |               | `6`<br/>`7`<br/>`8`<br/>`9` | `Unsupported`           | Unused                              |

### Redstone Comparator
Java Edition:

| Name    | Default value | Allowed values                            | Description                                                                                                                                               |
|---------|---------------|-------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing  | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction from theoutputside to theinputside of the comparator,<br/>or the opposite from the direction the player faces while placing the comparator. |
| mode    | `compare`     | `compare`<br/>`subtract`                  | Specifies the current mode of the redstone comparator.                                                                                                    |
| powered | `false`       | `false`<br/>`true`                        | True if the redstone comparator is being powered.                                                                                                         |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values                            | Values forMetadata Bits | Description                                                                                                                                               |
|------------------------------|---------------|---------------|-------------------------------------------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| minecraft:cardinal_direction | Not Supported | `south`       | `east`<br/>`north`<br/>`south`<br/>`west` | `Unsupported`           | The direction from theoutputside to theinputside of the comparator,<br/>or the opposite from the direction the player faces while placing the comparator. |
| output_lit_bit               | `0x8`         | `false`       | `false`<br/>`true`                        | `0`<br/>`1`             | True if the redstone comparator is being powered.                                                                                                         |
| output_subtract_bit          | `0x4`         | `false`       | `false`<br/>`true`                        | `0`<br/>`1`             | Specifies the current mode of the redstone comparator.                                                                                                    |



### Redstone Dust
Java Edition:

| Name  | Default value | Allowed values                                                                                                                    | Description                                                           |
|-------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| east  | `none`        | `none`<br/>`side`<br/>`up`                                                                                                        | The way redstone dust connects to the east, side can also mean down.  |
| north | `none`        | `none`<br/>`side`<br/>`up`                                                                                                        | The way redstone dust connects to the north, side can also mean down. |
| power | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | The redstone dust's current power level.                              |
| south | `none`        | `none`<br/>`side`<br/>`up`                                                                                                        | The way redstone dust connects to the south, side can also mean down. |
| west  | `none`        | `none`<br/>`side`<br/>`up`                                                                                                        | The way redstone dust connects to the west, side can also mean down.  |

Bedrock Edition:

| Name            | Metadata Bits                       | Default value | Allowed values                                                                                                                    | Values forMetadata Bits                                                                                                           | Description                              |
|-----------------|-------------------------------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|------------------------------------------|
| redstone_signal | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | The redstone dust's current power level. |



### Redstone Lamp
Java Edition:

| Name | Default value | Allowed values     | Description                  |
|------|---------------|--------------------|------------------------------|
| lit  | `false`       | `false`<br/>`true` | If the redstone lamp is lit. |



### Redstone Ore
Java Edition:

| Name | Default value | Allowed values     | Description                 |
|------|---------------|--------------------|-----------------------------|
| lit  | `false`       | `false`<br/>`true` | If the redstone ore is lit. |



### Redstone Repeater
Java Edition:

| Name    | Default value | Allowed values                            | Description                                                                                                                                      |
|---------|---------------|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| delay   | `1`           | `1`<br/>`2`<br/>`3`<br/>`4`               | The redstone repeater's delay in redstone ticks.                                                                                                 |
| facing  | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction from theoutputside to theinputside of a repeater.<br/>The opposite from the direction the player faces while placing the repeater. |
| locked  | `false`       | `false`<br/>`true`                        | True if the repeater is currently locked.                                                                                                        |
| powered | `false`       | `false`<br/>`true`                        | If the redstone repeater is lit.                                                                                                                 |

Bedrock Edition:

| Name                         | Metadata Bits   | Default value | Allowed values                            | Values forMetadata Bits     | Description                                                                                                                                      |
|------------------------------|-----------------|---------------|-------------------------------------------|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| minecraft:cardinal_direction | Not Supported   | `south`       | `east`<br/>`north`<br/>`south`<br/>`west` | `Unsupported`               | The direction from theoutputside to theinputside of a repeater.<br/>The opposite from the direction the player faces while placing the repeater. |
| repeater_delay               | `0x4`<br/>`0x8` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`               | `0`<br/>`1`<br/>`2`<br/>`3` | The redstone repeater's delay in redstone ticks minus 1.                                                                                         |



### Redstone Torch
Java Edition:
Floor:

| Name | Default value | Allowed values     | Description          |
|------|---------------|--------------------|----------------------|
| lit  | `true`        | `false`<br/>`true` | If the torch is lit. |

Wall:

| Name   | Default value | Allowed values                            | Description                                   |
|--------|---------------|-------------------------------------------|-----------------------------------------------|
| facing | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the top of the torch is facing. |
| lit    | `true`        | `false`<br/>`true`                        | If the torch is lit.                          |

Bedrock Edition:

| Name                   | Metadata Bits             | Default value | Allowed values                                      | Values forMetadata Bits             | Description                                                                                                                                  |
|------------------------|---------------------------|---------------|-----------------------------------------------------|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| torch_facing_direction | `0x1`<br/>`0x2`<br/>`0x4` | `west`        | `west`<br/>`east`<br/>`north`<br/>`south`<br/>`top` | `1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | The face of the block that the torch is attached to. If the torch is a wall torch, the top of the torch faces opposite to this direction.[3] |
|                        |                           |               | `unknown`                                           | `0`                                 | Unused                                                                                                                                       |

### Respawn Anchor
Java Edition:

| Name    | Default value | Allowed values                      | Description                                   |
|---------|---------------|-------------------------------------|-----------------------------------------------|
| charges | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4` | How many charges the Respawn Anchor has left. |

Bedrock Edition:

| Name                  | Metadata Bits             | Default value | Allowed values                      | Values forMetadata Bits             | Description                                   |
|-----------------------|---------------------------|---------------|-------------------------------------|-------------------------------------|-----------------------------------------------|
| respawn_anchor_charge | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4` | How many charges the Respawn Anchor has left. |



### Sand and Red Sand
Bedrock Edition:

| Name      | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description |
|-----------|---------------|---------------|----------------|-------------------------|-------------|
| sand_type | `0x1`         | `normal`      | `normal`       | `0`                     | Sand        |
|           |               |               | `red`          | `1`                     | Red Sand    |



### Sandstone and Red Sandstone
Bedrock Edition:

| Name            | Metadata Bits   | Default value | Allowed values | Values forMetadata Bits | Description        |
|-----------------|-----------------|---------------|----------------|-------------------------|--------------------|
| sand_stone_type | `0x1`<br/>`0x2` | `default`     | `default`      | `0`                     | Sandstone          |
|                 |                 |               | `heiroglyphs`  | `1`                     | Chiseled Sandstone |
|                 |                 |               | `cut`          | `2`                     | Cut Sandstone      |
|                 |                 |               | `smooth`       | `3`                     | Smooth Sandstone   |



### Saplings
Java Edition:

** Sapling **
| Name  | Default value | Allowed values | Description                           |
|-------|---------------|----------------|---------------------------------------|
| stage | `0`           | `0`<br/>`1`    | Specifies the sapling's growth stage. |

Bedrock Edition:

| Name         | Metadata Bits             | Default value | Allowed values     | Values forMetadata Bits | Description                           |
|--------------|---------------------------|---------------|--------------------|-------------------------|---------------------------------------|
| age_bit      | `0x8`                     | `false`       | `false`<br/>`true` | `0`<br/>`1`             | Specifies the sapling's growth stage. |
| sapling_type | `0x1`<br/>`0x2`<br/>`0x4` | `oak`         | `acacia`           | `4`                     | Acacia Sapling                        |
|              |                           |               | `birch`            | `2`                     | Birch Sapling                         |
|              |                           |               | `dark_oak`         | `5`                     | Dark Oak Sapling                      |
|              |                           |               | `jungle`           | `3`                     | Jungle Sapling                        |
|              |                           |               | `oak`              | `0`                     | Oak Sapling                           |
|              |                           |               | `spruce`           | `1`                     | Spruce Sapling                        |



### Scaffolding
Java Edition:

| Name        | Default value | Allowed values                                              | Description                                                                                         |
|-------------|---------------|-------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| bottom      | `false`       | `false`<br/>`true`                                          | If this scaffolding is floating.                                                                    |
| distance    | `7`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7` | The distance from a center scaffolding horizontally. If it is 7, it becomes a falling block entity. |
| waterlogged | `false`       | `false`<br/>`true`                                          | Whether or not there's water in the same place as this scaffolding.                                 |

Bedrock Edition:

| Name            | Metadata Bits             | Default value | Allowed values                                              | Values forMetadata Bits                                     | Description                                                                                         |
|-----------------|---------------------------|---------------|-------------------------------------------------------------|-------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| stability       | `0x2`<br/>`0x4`<br/>`0x8` | `7`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7` | The distance from a center scaffolding horizontally. If it is 7, it becomes a falling block entity. |
| stability_check | `0x1`                     | `false`       | `false`<br/>`true`                                          | `0`<br/>`1`                                                 | If a scaffolding block has been checked for stability.[more information needed]                     |

### Sculk Catalyst
Java Edition:

| Name  | Default value | Allowed values     | Description                                                        |
|-------|---------------|--------------------|--------------------------------------------------------------------|
| bloom | `false`       | `false`<br/>`true` | Whether the sculk catalyst is actively spreading the sculk or not. |

Bedrock Edition:

| Name  | Default value | Allowed values | Description                                                        |
|-------|---------------|----------------|--------------------------------------------------------------------|
| bloom | `0`           | `0`<br/>`1`    | Whether the sculk catalyst is actively spreading the sculk or not. |



### Sculk Sensor
Java Edition:

| Name               | Default value | Allowed values                                                                                                                    | Description                                                          |
|--------------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| power              | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | The sculk sensor's current power level.                              |
| sculk_sensor_phase | `inactive`    | `active`<br/>`cooldown`<br/>`inactive`                                                                                            | Whether or not the sculk sensor is active.[more information needed]  |
| waterlogged        | `false`       | `false`<br/>`true`                                                                                                                | Whether or not there's water in the same place as this sculk sensor. |

Bedrock Edition:

| Name               | Metadata Bits | Default value | Allowed values      | Values forMetadata Bits | Description                                      |
|--------------------|---------------|---------------|---------------------|-------------------------|--------------------------------------------------|
| sculk_sensor_phase | Not Supported | `0`           | `0`<br/>`1`<br/>`2` | `Unsupported`           | The sculk sensor phase.[more information needed] |



### Sculk Shrieker
Java Edition:

| Name        | Default value | Allowed values     | Description                                                            |
|-------------|---------------|--------------------|------------------------------------------------------------------------|
| can_summon  | `false`       | `false`<br/>`true` | If true, the sculk shrieker can summon thewarden.                      |
| shrieking   | `false`       | `false`<br/>`true` | Whether the sculk shrieker is shrieking or not.                        |
| waterlogged | `false`       | `false`<br/>`true` | Whether or not there's water in the same place as this sculk shrieker. |

Bedrock Edition:

| Name       | Metadata Bits | Default value | Allowed values     | Values forMetadata Bits | Description                                       |
|------------|---------------|---------------|--------------------|-------------------------|---------------------------------------------------|
| active     | Not Supported | `0`           | `0`<br/>`1`        | `Unsupported`           | Whether the sculk shrieker is shrieking or not.   |
| can_summon | Not Supported | `false`       | `true`<br/>`false` | `Unsupported`           | If true, the sculk shrieker can summon thewarden. |



### Sculk Vein
Java Edition:

| Name        | Default value | Allowed values     | Description                                                        |
|-------------|---------------|--------------------|--------------------------------------------------------------------|
| down        | `false`       | `false`<br/>`true` | When true, a sculk vein texture is displayed on the bottom.        |
| east        | `false`       | `false`<br/>`true` | When true, a sculk vein texture is displayed on the east.          |
| north       | `false`       | `false`<br/>`true` | When true, a sculk vein texture is displayed on the north.         |
| south       | `false`       | `false`<br/>`true` | When true, a sculk vein texture is displayed on the south.         |
| up          | `false`       | `false`<br/>`true` | When true, a sculk vein texture is displayed on the top.           |
| waterlogged | `false`       | `false`<br/>`true` | Whether or not there's water in the same place as this sculk vein. |
| west        | `false`       | `false`<br/>`true` | When true, a sculk vein texture is displayed on the west.          |

Bedrock Edition:

| Name                      | Metadata Bits                                             | Default value | Allowed values | Values forMetadata Bits | Description                                                                                                                                                                                       |
|---------------------------|-----------------------------------------------------------|---------------|----------------|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| multi_face_direction_bits | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8`<br/>`0x10`<br/>`0x20` | `0`           | `0 to 63`      | `0 to 63`               | The directions the sculk vein exists. Each bit determines one direction:0x1: Down<br/>0x2: Up<br/>0x4: North<br/>0x8: South<br/>0x10: West<br/>0x20: East<br/>0 is unused and it behaves like 63. |



### Sea Pickle
Java Edition:

| Name        | Default value | Allowed values              | Description                                                      |
|-------------|---------------|-----------------------------|------------------------------------------------------------------|
| pickles     | `1`           | `1`<br/>`2`<br/>`3`<br/>`4` | Number of pickles.                                               |
| waterlogged | `true`        | `false`<br/>`true`          | Whether or not there's water in the same place as these pickles. |

Bedrock Edition:

| Name          | Metadata Bits   | Default value | Allowed values              | Values forMetadata Bits     | Description                                                  |
|---------------|-----------------|---------------|-----------------------------|-----------------------------|--------------------------------------------------------------|
| cluster_count | `0x1`<br/>`0x2` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3` | `0`<br/>`1`<br/>`2`<br/>`3` | Number of additional pickles.                                |
| dead_bit      | `0x4`           | `false`       | `false`<br/>`true`          | `0`<br/>`1`                 | True if there's no water in the same place as these pickles. |

### Shulker Boxes
Java Edition:

| Name   | Default value | Allowed values                                                | Description                                                                                                                    |
|--------|---------------|---------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| facing | `up`          | `down`<br/>`east`<br/>`north`<br/>`south`<br/>`up`<br/>`west` | The direction the shulker box is pointing.<br/>The opposite from the direction the player faces while placing the shulker box. |



### Sign
Java Edition:

** Standing **
| Name        | Default value | Allowed values     | Description                                                  |
|-------------|---------------|--------------------|--------------------------------------------------------------|
| rotation    | `0`           | `0`                | The block is facing south.                                   |
|             |               | `1`                | The block is facing south-southwest.                         |
|             |               | `2`                | The block is facing southwest.                               |
|             |               | `3`                | The block is facing west-southwest.                          |
|             |               | `4`                | The block is facing west.                                    |
|             |               | `5`                | The block is facing west-northwest.                          |
|             |               | `6`                | The block is facing northwest.                               |
|             |               | `7`                | The block is facing north-northwest.                         |
|             |               | `8`                | The block is facing north.                                   |
|             |               | `9`                | The block is facing north-northeast.                         |
|             |               | `10`               | The block is facing northeast.                               |
|             |               | `11`               | The block is facing east-northeast.                          |
|             |               | `12`               | The block is facing east.                                    |
|             |               | `13`               | The block is facing east-southeast.                          |
|             |               | `14`               | The block is facing southeast.                               |
|             |               | `15`               | The block is facing south-southeast.                         |
| waterlogged | `false`       | `false`<br/>`true` | Whether or not there's water in the same place as this sign. |

** Wall **
| Name        | Default value | Allowed values                            | Description                                                                                                                                                                    |
|-------------|---------------|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing      | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the block is facing. For example, a block facing east is attached to a block to its west.<br/>Opposite from the direction a player faces when placing the block. |
| waterlogged | `false`       | `false`<br/>`true`                        | Whether or not there's water in the same place as this sign.                                                                                                                   |

Bedrock Edition:

** Standing **
| Name                  | Metadata Bits                       | Default value | Allowed values | Values forMetadata Bits | Description                          |
|-----------------------|-------------------------------------|---------------|----------------|-------------------------|--------------------------------------|
| ground_sign_direction | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8` | `0`           | `0`            | `0`                     | The block is facing south.           |
|                       |                                     |               | `1`            | `1`                     | The block is facing south-southwest. |
|                       |                                     |               | `2`            | `2`                     | The block is facing southwest.       |
|                       |                                     |               | `3`            | `3`                     | The block is facing west-southwest.  |
|                       |                                     |               | `4`            | `4`                     | The block is facing west.            |
|                       |                                     |               | `5`            | `5`                     | The block is facing west-northwest.  |
|                       |                                     |               | `6`            | `6`                     | The block is facing northwest.       |
|                       |                                     |               | `7`            | `7`                     | The block is facing north-northwest. |
|                       |                                     |               | `8`            | `8`                     | The block is facing north.           |
|                       |                                     |               | `9`            | `9`                     | The block is facing north-northeast. |
|                       |                                     |               | `10`           | `10`                    | The block is facing northeast.       |
|                       |                                     |               | `11`           | `11`                    | The block is facing east-northeast.  |
|                       |                                     |               | `12`           | `12`                    | The block is facing east.            |
|                       |                                     |               | `13`           | `13`                    | The block is facing east-southeast.  |
|                       |                                     |               | `14`           | `14`                    | The block is facing southeast.       |
|                       |                                     |               | `15`           | `15`                    | The block is facing south-southeast. |

** Wall **
| Name             | Metadata Bits             | Default value | Allowed values              | Values forMetadata Bits     | Description                                                                                                                                               |
|------------------|---------------------------|---------------|-----------------------------|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing_direction | `0x1`<br/>`0x2`<br/>`0x4` | `2`           | `2`<br/>`3`<br/>`4`<br/>`5` | `2`<br/>`3`<br/>`4`<br/>`5` | The direction the block is facing. For example, a block facing east is attached to a block to its west.2: north<br/>3: south<br/>4: west<br/>5: east<br/> |
|                  |                           |               | `0`<br/>`1`                 | `0`<br/>`1`                 | Unused                                                                                                                                                    |



### Slabs
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



### Small Dripleaf
Java Edition:

| Name        | Default value | Allowed values                            | Description                                                                                                                        |
|-------------|---------------|-------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| facing      | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the small dripleaf is facing.<br/>The opposite from the direction the player faces while placing the small dripleaf. |
| half        | `lower`       | `lower`<br/>`upper`                       | What half of the small dripleaf this block is.                                                                                     |
| waterlogged | `false`       | `false`<br/>`true`                        | Whether or not there's water in the same place as this small dripleaf.                                                             |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values                            | Values forMetadata Bits | Description                                                                                                                        |
|------------------------------|---------------|---------------|-------------------------------------------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| minecraft:cardinal_direction | Not Supported | `south`       | `east`<br/>`north`<br/>`south`<br/>`west` | `Unsupported`           | The direction the small dripleaf is facing.<br/>The opposite from the direction the player faces while placing the small dripleaf. |
| upper_block_bit              | Not Supported | `true`        | `false`<br/>`true`                        | `Unsupported`           | What half of the small dripleaf this block is.                                                                                     |



### Smoker
Java Edition:

| Name   | Default value | Allowed values                            | Description                                                                                                              |
|--------|---------------|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| facing | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the smoker's opening faces.<br/>The opposite from the direction the player faces while placing the smoker. |
| lit    | `false`       | `false`<br/>`true`                        | If the smoker is lit.                                                                                                    |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values                            | Values forMetadata Bits | Description                                                                                                              |
|------------------------------|---------------|---------------|-------------------------------------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------|
| minecraft:cardinal_direction | Not Supported | `south`       | `east`<br/>`north`<br/>`south`<br/>`west` | `Unsupported`           | The direction the smoker's opening faces.<br/>The opposite from the direction the player faces while placing the smoker. |



### Snow
Java Edition:

| Name   | Default value | Allowed values                                              | Description                                                                                                                                          |
|--------|---------------|-------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| layers | `1`           | `1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8` | The number of layers thick.<br/>Each layer adds two pixels to the block height, and each layer after the first adds two pixels to the collision box. |

Bedrock Edition:

| Name        | Metadata Bits             | Default value | Allowed values                                              | Values forMetadata Bits                                     | Description                                           |
|-------------|---------------------------|---------------|-------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------|
| height      | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7` | The number of layers in addition to the bottom layer. |
| covered_bit | `0x8`                     | `false`       | `true`<br/>`false`                                          | `0`<br/>`1`                                                 | True if the snow is covering a plant.                 |



### Sponge
Bedrock Edition:

| Name        | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description |
|-------------|---------------|---------------|----------------|-------------------------|-------------|
| sponge_type | `0x1`         | `dry`         | `dry`          | `0`                     | Sponge      |
|             |               |               | `wet`          | `1`                     | Wet Sponge  |



### Stairs
Java Edition:

| Name        | Default value | Allowed values                                                                   | Description                                                                                                                                                                                                                                                                                                                        |
|-------------|---------------|----------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing      | `north`       | `east`<br/>`north`<br/>`south`<br/>`west`                                        | The direction the stairs' full-block side faces.<br/>When placed in-game by a player, this matches the direction the player faces.                                                                                                                                                                                                 |
| half        | `bottom`      | `bottom`<br/>`top`                                                               | Top if the stairs are upside-down.                                                                                                                                                                                                                                                                                                 |
| shape       | `straight`    | `inner_left`<br/>`inner_right`<br/>`outer_left`<br/>`outer_right`<br/>`straight` | "straight" is the default stairs shape.<br/>"inner" is an "inside corner" stair shape, with two full-block and two stair-shaped side faces.<br/>"outer" is an "outside corner" stair shape, with two stair-shaped and two half-block side faces.<br/>"left" and "right" specify in which direction is the higher part of the step. |
| waterlogged | `false`       | `false`<br/>`true`                                                               | Whether or not there's water in the same place as these stairs.                                                                                                                                                                                                                                                                    |

Bedrock Edition:

| Name             | Metadata Bits   | Default value | Allowed values              | Values forMetadata Bits     | Description                                                                                        |
|------------------|-----------------|---------------|-----------------------------|-----------------------------|----------------------------------------------------------------------------------------------------|
| upside_down_bit  | `0x4`           | `false`       | `false`<br/>`true`          | `0`<br/>`1`                 | True if the stairs are upside-down.                                                                |
| weirdo_direction | `0x1`<br/>`0x2` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3` | `0`<br/>`1`<br/>`2`<br/>`3` | The direction the stairs' full-block side faces.0: East<br/>1: West<br/>2: South<br/>3: North<br/> |

### Stone Bricks
Bedrock Edition

| Name             | Metadata Bits             | Default value | Allowed values | Values forMetadata Bits | Description                                                |
|------------------|---------------------------|---------------|----------------|-------------------------|------------------------------------------------------------|
| stone_brick_type | `0x1`<br/>`0x2`<br/>`0x4` | `default`     | `default`      | `0`                     | Stone Bricks                                               |
|                  |                           |               | `mossy`        | `1`                     | Mossy Stone Bricks                                         |
|                  |                           |               | `cracked`      | `2`                     | Cracked Stone Bricks                                       |
|                  |                           |               | `chiseled`     | `3`                     | Chiseled Stone Bricks                                      |
|                  |                           |               | `smooth`       | `4`                     | Smooth Stone Bricks (unused, same texture as regular ones) |



### Stonecutter
Java Edition:

| Name   | Default value | Allowed values                            | Description                                                                                                               |
|--------|---------------|-------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| facing | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the stonecutter is facing.<br/>The opposite from the direction the player faces when placing a stonecutter. |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values                            | Values forMetadata Bits | Description                                                                                                               |
|------------------------------|---------------|---------------|-------------------------------------------|-------------------------|---------------------------------------------------------------------------------------------------------------------------|
| minecraft:cardinal_direction | Not Supported | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | `Unsupported`           | The direction the stonecutter is facing.<br/>The opposite from the direction the player faces when placing a stonecutter. |



### Structure Block
Java Edition:

| Name | Default value | Allowed values | Description            |
|------|---------------|----------------|------------------------|
| mode | `data`        | `corner`       | Corner Structure Block |
|      |               | `data`         | Data Structure Block   |
|      |               | `load`         | Load Structure Block   |
|      |               | `save`         | Save Structure Block   |

Bedrock Edition:

| Name                 | Metadata Bits             | Default value | Allowed values | Values forMetadata Bits | Description               |
|----------------------|---------------------------|---------------|----------------|-------------------------|---------------------------|
| structure_block_type | `0x1`<br/>`0x2`<br/>`0x4` | `data`        | `corner`       | `3`                     | Corner Structure Block    |
|                      |                           |               | `data`         | `0`                     | Data Structure Block      |
|                      |                           |               | `export`       | `5`                     | Export Structure Block    |
|                      |                           |               | `invalid`      | `4`                     | Inventory Structure Block |
|                      |                           |               | `load`         | `2`                     | Load Structure Block      |
|                      |                           |               | `save`         | `1`                     | Save Structure Block      |



### Structure Void
Bedrock Edition:

| Name                | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description    |
|---------------------|---------------|---------------|----------------|-------------------------|----------------|
| structure_void_type | `0x1`         | `void`        | `air`          | `1`                     | Structure Air  |
|                     |               |               | `void`         | `0`                     | Structure Void |



### Sugar Cane
Java Edition:

| Name | Default value | Allowed values                                                                                                                    | Description                                                                                                                                                                                              |
|------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| age  | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | A freshly planted cane – and a cane that has just grown cane above it – each have an age of 0.<br/>The age is incremented at random intervals.<br/>At age 15, a cane may try to grow more cane above it. |

Bedrock Edition:

| Name | Metadata Bits                       | Default value | Allowed values                                                                                                                    | Values forMetadata Bits                                                                                                           | Description                                                                                                                                                                                              |
|------|-------------------------------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| age  | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | A freshly planted cane – and a cane that has just grown cane above it – each have an age of 0.<br/>The age is incremented at random intervals.<br/>At age 15, a cane may try to grow more cane above it. |



### Sweet Berry Bush
Java Edition:

| Name | Default value | Allowed values | Description                                                                  |
|------|---------------|----------------|------------------------------------------------------------------------------|
| age  | `0`           | `0`            | Young plant                                                                  |
|      |               | `1`            | No berries                                                                   |
|      |               | `2`            | Some berries,usingthe bush gives 1–2sweet berriesand sets the age back to 1. |
|      |               | `3`            | Full berries,usingthe bush gives 2–3sweet berriesand sets the age back to 1. |

Bedrock Edition:

| Name   | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                                                     |
|--------|---------------|---------------|----------------|-------------------------|---------------------------------------------------------------------------------|
| growth | `0x1`         | `0`           | `0`            | `0`                     | Young plant                                                                     |
|        |               |               | `1`            | `1`                     | No berries                                                                      |
|        |               |               | `2`            | `2`                     | Some berries,usingthe bush gives 1–2sweet berriesand sets the growth back to 2. |
|        |               |               | `3`            | `3`                     | Full berries,usingthe bush gives 2–3sweet berriesand sets the growth back to 2. |



### Tall Grass and Large Fern
Bedrock Edition:

| Name            | Metadata Bits   | Default value | Allowed values | Values forMetadata Bits | Description                                                                                         |
|-----------------|-----------------|---------------|----------------|-------------------------|-----------------------------------------------------------------------------------------------------|
| tall_grass_type | `0x1`<br/>`0x2` | `default`     | `default`      | `0`                     | Fern(Unused variant which looks identical to grass, but turns into alarge fernwhenbone mealis used) |
|                 |                 |               | `tall`         | `1`                     | Grass                                                                                               |
|                 |                 |               | `fern`         | `2`                     | Fern                                                                                                |
|                 |                 |               | `snow`         | `3`                     | Fern (looks identical to actual fern, but turns intodouble tallgrasswhenbone mealis used)           |

### Tall Seagrass
Java Edition:
Tall

| Name | Default value | Allowed values      | Description                                    |
|------|---------------|---------------------|------------------------------------------------|
| half | `lower`       | `lower`<br/>`upper` | The half of the plant contained in this block. |

Bedrock Edition:

| Name           | Metadata Bits   | Default value | Allowed values | Values forMetadata Bits | Description                               |
|----------------|-----------------|---------------|----------------|-------------------------|-------------------------------------------|
| sea_grass_type | `0x1`<br/>`0x2` | `default`     | `default`      | `0`                     | This is seagrass.                         |
|                |                 |               | `double_bot`   | `1`                     | This is the bottom half of tall seagrass. |
|                |                 |               | `double_top`   | `2`                     | This is the top half of tall seagrass.    |

### Target
Java Edition:

| Name  | Default value | Allowed values                                                                                                                    | Description                          |
|-------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|
| power | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | Redstone power output of the target. |



### TNT
Java Edition:

| Name     | Default value | Allowed values | Description                                                                   |
|----------|---------------|----------------|-------------------------------------------------------------------------------|
| unstable | `false`       | `false`        | Hittingthe TNT block breaks it, dropping it as an item that can be picked up. |
|          |               | `true`         | Hittingthe TNT block causes it to ignite and then explode.                    |

Bedrock Edition:

| Name                 | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                                                   |
|----------------------|---------------|---------------|----------------|-------------------------|-------------------------------------------------------------------------------|
| allow_underwater_bit | `0x2`         | `false`       | `false`        | `0`                     | This is normal TNT.                                                           |
|                      |               |               | `true`         | `1`                     | This is Underwater TNT.                                                       |
| explode_bit          | `0x1`         | `false`       | `false`        | `0`                     | Hittingthe TNT block breaks it, dropping it as an item that can be picked up. |
|                      |               |               | `true`         | `1`                     | Hittingthe TNT block causes it to ignite and then explode.                    |



### Torch and Soul Torch
Java Edition:
Wall

| Name   | Default value | Allowed values                            | Description                                   |
|--------|---------------|-------------------------------------------|-----------------------------------------------|
| facing | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the top of the torch is facing. |

Bedrock Edition:

| Name                   | Metadata Bits             | Default value | Allowed values                                      | Values forMetadata Bits             | Description                                                                                                                                  |
|------------------------|---------------------------|---------------|-----------------------------------------------------|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| torch_facing_direction | `0x1`<br/>`0x2`<br/>`0x4` | `west`        | `west`<br/>`east`<br/>`north`<br/>`south`<br/>`top` | `1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | The face of the block that the torch is attached to. If the torch is a wall torch, the top of the torch faces opposite to this direction.[4] |
|                        |                           |               | `unknown`                                           | `0`                                 | Unused                                                                                                                                       |



### Trapdoors
Java Edition:

| Name        | Default value | Allowed values                            | Description                                                                                      |
|-------------|---------------|-------------------------------------------|--------------------------------------------------------------------------------------------------|
| facing      | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the trapdoor swings open.<br/>The opposite from the side its hinge is attached to. |
| half        | `bottom`      | `bottom`<br/>`top`                        | Whether the trapdoor occupies the top or bottom part of a block.                                 |
| open        | `false`       | `false`<br/>`true`                        | True if the trapdoor is currently open (may differ from`powered`).                               |
| powered     | `false`       | `false`<br/>`true`                        | True if the trapdoor is currently powered (may differ from`open`).                               |
| waterlogged | `false`       | `false`<br/>`true`                        | Whether or not there's water in the same place as this trapdoor.                                 |

Bedrock Edition:

| Name            | Metadata Bits   | Default value | Allowed values              | Values forMetadata Bits     | Description                                                                                                                                                                                                             |
|-----------------|-----------------|---------------|-----------------------------|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| direction       | `0x1`<br/>`0x2` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3` | `0`<br/>`1`<br/>`2`<br/>`3` | The direction the trapdoor is facing.0: Trapdoor on the west side of a block<br/>1: Trapdoor on the east side of a block<br/>2: Trapdoor on the north side of a block<br/>3: Trapdoor on the south side of a block<br/> |
| open_bit        | `0x8`           | `false`       | `false`<br/>`true`          | `0`<br/>`1`                 | True if the trapdoor is currently open.                                                                                                                                                                                 |
| upside_down_bit | `0x4`           | `false`       | `false`<br/>`true`          | `0`<br/>`1`                 | Whether the trapdoor occupies the top or bottom part of a block.                                                                                                                                                        |

### Tripwire
Java Edition:

| Name     | Default value | Allowed values     | Description                                                                     |
|----------|---------------|--------------------|---------------------------------------------------------------------------------|
| attached | `false`       | `false`<br/>`true` | True if the tripwire is connected to a valid tripwire circuit.                  |
| disarmed | `false`       | `false`<br/>`true` | True if the tripwire is disarmed, that is, broken usingshears.                  |
| east     | `false`       | `false`<br/>`true` | True if the tripwire connects to other tripwire or tripwire hooks to the east.  |
| north    | `false`       | `false`<br/>`true` | True if the tripwire connects to other tripwire or tripwire hooks to the north. |
| powered  | `false`       | `false`<br/>`true` | True if the tripwire is active.                                                 |
| south    | `false`       | `false`<br/>`true` | True if the tripwire connects to other tripwire or tripwire hooks to the south. |
| west     | `false`       | `false`<br/>`true` | True if the tripwire connects to other tripwire or tripwire hooks to the west.  |

Bedrock Edition:

| Name          | Metadata Bits | Default value | Allowed values     | Values forMetadata Bits | Description                                                                                      |
|---------------|---------------|---------------|--------------------|-------------------------|--------------------------------------------------------------------------------------------------|
| attached_bit  | `0x4`         | `false`       | `false`<br/>`true` | `0`<br/>`1`             | True if the tripwire is connected to a valid tripwire circuit.                                   |
| disarmed_bit  | `0x8`         | `false`       | `false`<br/>`true` | `0`<br/>`1`             | True if the tripwire is disarmed, that is, broken usingshears.                                   |
| powered_bit   | `0x1`         | `false`       | `false`<br/>`true` | `0`<br/>`1`             | True if the tripwire is active.                                                                  |
| suspended_bit | `0x2`         | `true`        | `false`<br/>`true` | `0`<br/>`1`             | True if the tripwire hasn't connected to a valid tripwire circuit. (makeshitboxlarger when true) |



### Tripwire Hook
Java Edition:

| Name     | Default value | Allowed values                            | Description                                                                                                                                                            |
|----------|---------------|-------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| attached | `false`       | `false`<br/>`true`                        | True if the tripwire hook is connected to a valid tripwire circuit.                                                                                                    |
| facing   | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction in which the tripwire hook juts out from the block it is attached to.<br/>For example, a tripwire hook facing north is attached to a block to its south. |
| powered  | `false`       | `false`<br/>`true`                        | True if the tripwire hook is active.                                                                                                                                   |

Bedrock Edition:

| Name         | Metadata Bits   | Default value | Allowed values              | Values forMetadata Bits     | Description                                                                                                                                                                                                                                                                       |
|--------------|-----------------|---------------|-----------------------------|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| attached_bit | `0x4`           | `false`       | `false`<br/>`true`          | `0`<br/>`1`                 | True if the tripwire hook is connected to a valid tripwire circuit.                                                                                                                                                                                                               |
| direction    | `0x1`<br/>`0x2` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3` | `0`<br/>`1`<br/>`2`<br/>`3` | The direction in which the tripwire hook juts out from the block it is attached to.0: Tripwire hook on block side facing south<br/>1: Tripwire hook on block side facing west<br/>2: Tripwire hook on block side facing north<br/>3: Tripwire hook on block side facing east<br/> |
| powered_bit  | `0x8`           | `false`       | `false`<br/>`true`          | `0`<br/>`1`                 | True if the tripwire hook is active.                                                                                                                                                                                                                                              |



### Turtle Egg
Java Edition:

| Name  | Default value | Allowed values              | Description                                                                          |
|-------|---------------|-----------------------------|--------------------------------------------------------------------------------------|
| eggs  | `1`           | `1`<br/>`2`<br/>`3`<br/>`4` | Number of eggs.                                                                      |
| hatch | `0`           | `0`<br/>`1`<br/>`2`         | Determines how close an egg is to hatching; starts at 0 and is randomly incremented. |

Bedrock Edition:

| Name             | Metadata Bits   | Default value | Allowed values                                         | Values forMetadata Bits     | Description                                                                                  |
|------------------|-----------------|---------------|--------------------------------------------------------|-----------------------------|----------------------------------------------------------------------------------------------|
| turtle_egg_count | `0x1`<br/>`0x2` | `one_egg`     | `one_egg`<br/>`two_egg`<br/>`three_egg`<br/>`four_egg` | `0`<br/>`1`<br/>`2`<br/>`3` | Number of eggs.                                                                              |
| cracked_state    | `0x4`<br/>`0x8` | `no_cracks`   | `no_cracks`<br/>`cracked`<br/>`max_cracked`            | `0`<br/>`1`<br/>`2`         | Determines how close an egg is to hatching; starts at no cracks and is randomly incremented. |



### Twisting Vines
Java Edition
Twisting Vines:

| Name | Default value | Allowed values                                                                                                                                                                                                              | Description                                         |
|------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| age  | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15`<br/>`16`<br/>`17`<br/>`18`<br/>`19`<br/>`20`<br/>`21`<br/>`22`<br/>`23`<br/>`24`<br/>`25` | Increments for every block the twisting vine grows. |

Bedrock Edition

| Name               | Metadata Bits                                  | Default value | Allowed values                                                                                                                                                                                                              | Values forMetadata Bits                                                                                                                                                                                                     | Description                                         |
|--------------------|------------------------------------------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| twisting_vines_age | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8`<br/>`0x10` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15`<br/>`16`<br/>`17`<br/>`18`<br/>`19`<br/>`20`<br/>`21`<br/>`22`<br/>`23`<br/>`24`<br/>`25` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15`<br/>`16`<br/>`17`<br/>`18`<br/>`19`<br/>`20`<br/>`21`<br/>`22`<br/>`23`<br/>`24`<br/>`25` | Increments for every block the twisting vine grows. |



### Underwater Torch
| Name                   | Metadata Bits             | Default value | Allowed values                                      | Values forMetadata Bits             | Description                                                                                                                                  |
|------------------------|---------------------------|---------------|-----------------------------------------------------|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| torch_facing_direction | `0x1`<br/>`0x2`<br/>`0x4` | `west`        | `west`<br/>`east`<br/>`north`<br/>`south`<br/>`top` | `1`<br/>`2`<br/>`3`<br/>`4`<br/>`5` | The face of the block that the torch is attached to. If the torch is a wall torch, the top of the torch faces opposite to this direction.[5] |
|                        |                           |               | `unknown`                                           | `0`                                 | Unused                                                                                                                                       |



### Vines
Java Edition:

| Name  | Default value | Allowed values     | Description                                          |
|-------|---------------|--------------------|------------------------------------------------------|
| east  | `false`       | `false`<br/>`true` | When true, a vine texture is displayed on the east.  |
| north | `false`       | `false`<br/>`true` | When true, a vine texture is displayed on the north. |
| south | `false`       | `false`<br/>`true` | When true, a vine texture is displayed on the south. |
| up    | `false`       | `false`<br/>`true` | When true, a vine texture is displayed on the top.   |
| west  | `false`       | `false`<br/>`true` | When true, a vine texture is displayed on the west.  |

Bedrock Edition:

| Name                | Metadata Bits                       | Default value | Allowed values                                                                                                                    | Values forMetadata Bits                                                                                                           | Description                                                                                                                                                                                                                                                                            |
|---------------------|-------------------------------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| vine_direction_bits | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | The directions the vine exists, excluding up. Each bit determines one direction:0x1: Vines at the south<br/>0x2: Vines at the west<br/>0x4: Vines at the north<br/>0x8: Vines at the east<br/>Note: Vines gain the ceiling vines if there's a block above, block state doesn't change. |



### Walls
Java Edition

| Name        | Default value | Allowed values              | Description                                                  |
|-------------|---------------|-----------------------------|--------------------------------------------------------------|
| east        | `none`        | `low`<br/>`none`<br/>`tall` | How the wall extends from the center post to the east.       |
| north       | `none`        | `low`<br/>`none`<br/>`tall` | How the wall extends from the center post to the north.      |
| south       | `none`        | `low`<br/>`none`<br/>`tall` | How the wall extends from the center post to the south.      |
| up          | `true`        | `false`<br/>`true`          | When true, the wall has a center post.                       |
| waterlogged | `false`       | `false`<br/>`true`          | Whether or not there's water in the same place as this wall. |
| west        | `none`        | `low`<br/>`none`<br/>`tall` | How the wall extends from the center post to the west.       |

Bedrock Edition
Non-blackstone and deepslate wall:

| Name                       | Metadata Bits                       | Default value | Allowed values                                                                                                                                                                                                                                        | Values forMetadata Bits                                                                                         | Description                                                            |
|----------------------------|-------------------------------------|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| wall_block_type            | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8` | `cobblestone` | `cobblestone`<br/>`mossy_cobblestone`<br/>`granite`<br/>`diorite`<br/>`andesite`<br/>`sandstone`<br/>`brick`<br/>`stone_brick`<br/>`mossy_stone_brick`<br/>`nether_brick`<br/>`end_brick`<br/>`prismarine`<br/>`red_sandstone`<br/>`red_nether_brick` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13` | The type of wall; for example,`stone_brick`denotes a stone brick wall. |
| wall_connection_type_east  | Not Supported                       | `none`        | `none`<br/>`short`<br/>`tall`                                                                                                                                                                                                                         | `Unsupported`                                                                                                   | How the wall extends from the center post to the east.                 |
| wall_connection_type_north | Not Supported                       | `none`        | `none`<br/>`short`<br/>`tall`                                                                                                                                                                                                                         | `Unsupported`                                                                                                   | How the wall extends from the center post to the north.                |
| wall_connection_type_south | Not Supported                       | `none`        | `none`<br/>`short`<br/>`tall`                                                                                                                                                                                                                         | `Unsupported`                                                                                                   | How the wall extends from the center post to the south.                |
| wall_connection_type_west  | Not Supported                       | `none`        | `none`<br/>`short`<br/>`tall`                                                                                                                                                                                                                         | `Unsupported`                                                                                                   | How the wall extends from the center post to the west.                 |
| wall_post_bit              | Not Supported                       | `true`        | `false`<br/>`true`                                                                                                                                                                                                                                    | `Unsupported`                                                                                                   | Whether or not the wall has a center post.                             |

Blackstone and deepslate wall:

| Name                       | Metadata Bits | Default value | Allowed values                | Values forMetadata Bits | Description                                             |
|----------------------------|---------------|---------------|-------------------------------|-------------------------|---------------------------------------------------------|
| wall_connection_type_east  | Not Supported | `none`        | `none`<br/>`short`<br/>`tall` | `Unsupported`           | How the wall extends from the center post to the east.  |
| wall_connection_type_north | Not Supported | `none`        | `none`<br/>`short`<br/>`tall` | `Unsupported`           | How the wall extends from the center post to the north. |
| wall_connection_type_south | Not Supported | `none`        | `none`<br/>`short`<br/>`tall` | `Unsupported`           | How the wall extends from the center post to the south. |
| wall_connection_type_west  | Not Supported | `none`        | `none`<br/>`short`<br/>`tall` | `Unsupported`           | How the wall extends from the center post to the west.  |
| wall_post_bit              | Not Supported | `true`        | `false`<br/>`true`            | `Unsupported`           | Whether or not the wall has a center post.              |

### Water
Java Edition:

| Name  | Default value | Allowed values                                                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| level | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | If bit 0x8 is set, this fluid is "falling" and spreads only downward. At this level, the lower bits are essentially ignored, since this block is then at its highest fluid level. This level is equal to the falling water above, equal to 8 plus the level of the non-falling water above it.The lower three bits are the fluid block's level. 0 is the highest fluid level (not necessarily filling the block - this depends on the neighboring fluid blocks above each upper corner of the block). Data values increase as the fluid level of the block drops: 1 is the next highest, 2 lower, on through 7, the lowest fluid level. Along a line on a flat plane, water drops one level per meter. |

Bedrock Edition:
Water and flowing water

| Name         | Metadata Bits                       | Default value | Allowed values                                                                                                                    | Values forMetadata Bits                                                                                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|--------------|-------------------------------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| liquid_depth | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | If bit 0x8 is set, this fluid is "falling" and spreads only downward. At this level, the lower bits are essentially ignored, since this block is then at its highest fluid level. This level is equal to the falling water above, equal to 8 plus the level of the non-falling water above it.The lower three bits are the fluid block's level. 0 is the highest fluid level (not necessarily filling the block - this depends on the neighboring fluid blocks above each upper corner of the block). Data values increase as the fluid level of the block drops: 1 is the next highest, 2 lower, on through 7, the lowest fluid level. Along a line on a flat plane, water drops one level per meter. |



### Weeping Vines
Java Edition
Weeping Vines:

| Name | Default value | Allowed values                                                                                                                                                                                                              | Description                                        |
|------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| age  | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15`<br/>`16`<br/>`17`<br/>`18`<br/>`19`<br/>`20`<br/>`21`<br/>`22`<br/>`23`<br/>`24`<br/>`25` | Increments for every block the weeping vine grows. |

Bedrock Edition

| Name              | Metadata Bits                                  | Default value | Allowed values                                                                                                                                                                                                              | Values forMetadata Bits                                                                                                                                                                                                     | Description                                        |
|-------------------|------------------------------------------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| weeping_vines_age | `0x1`<br/>`0x2`<br/>`0x4`<br/>`0x8`<br/>`0x10` | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15`<br/>`16`<br/>`17`<br/>`18`<br/>`19`<br/>`20`<br/>`21`<br/>`22`<br/>`23`<br/>`24`<br/>`25` | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15`<br/>`16`<br/>`17`<br/>`18`<br/>`19`<br/>`20`<br/>`21`<br/>`22`<br/>`23`<br/>`24`<br/>`25` | Increments for every block the weeping vine grows. |



### Wheat crop
Java Edition:

| Name | Default value | Allowed values | Description  |
|------|---------------|----------------|--------------|
| age  | `0`           | `0`            |              |
|      |               | `1`            |              |
|      |               | `2`            |              |
|      |               | `3`            |              |
|      |               | `4`            |              |
|      |               | `5`            |              |
|      |               | `6`            |              |
|      |               | `7`            | Fully grown. |

Bedrock Edition:

| Name   | Metadata Bits             | Default value | Allowed values | Values forMetadata Bits | Description  |
|--------|---------------------------|---------------|----------------|-------------------------|--------------|
| growth | `0x1`<br/>`0x2`<br/>`0x4` | `0`           | `0`            | `0`                     |              |
|        |                           |               | `1`            | `1`                     |              |
|        |                           |               | `2`            | `2`                     |              |
|        |                           |               | `3`            | `3`                     |              |
|        |                           |               | `4`            | `4`                     |              |
|        |                           |               | `5`            | `5`                     |              |
|        |                           |               | `6`            | `6`                     |              |
|        |                           |               | `7`            | `7`                     | Fully grown. |



### Wood
Java Edition:

| Name | Default value | Allowed values | Description                                 |
|------|---------------|----------------|---------------------------------------------|
| axis | `y`           | `x`            | The wood or hyphae is oriented east–west.   |
|      |               | `y`            | The wood or hyphae is oriented vertically.  |
|      |               | `z`            | The wood or hyphae is oriented north–south. |

Bedrock Edition:

| Name        | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                 |
|-------------|---------------|---------------|----------------|-------------------------|---------------------------------------------|
| pillar_axis | Not Supported | `y`           | `x`            | `Unsupported`           | The wood or hyphae is oriented east–west.   |
|             |               |               | `y`            | `Unsupported`           | The wood or hyphae is oriented vertically.  |
|             |               |               | `z`            | `Unsupported`           | The wood or hyphae is oriented north–south. |



## List of fluid states
### Water
Java Edition:
Water

| Name    | Default value | Allowed values     | Description   |
|---------|---------------|--------------------|---------------|
| falling | `false`       | `true`<br/>`false` | Always false. |

Flowing water

| Name    | Default value | Allowed values                                              | Description                                                 |
|---------|---------------|-------------------------------------------------------------|-------------------------------------------------------------|
| falling | `false`       | `true`<br/>`false`                                          | True for falling water, false for water with a block below. |
| level   | `1`           | `1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8` | Height of the water, 8 when the water is falling.           |

### Lava
Java Edition:
Lava

| Name    | Default value | Allowed values     | Description   |
|---------|---------------|--------------------|---------------|
| falling | `false`       | `true`<br/>`false` | Always false. |

Flowing lava

| Name    | Default value | Allowed values                                              | Description                                               |
|---------|---------------|-------------------------------------------------------------|-----------------------------------------------------------|
| falling | `false`       | `false`<br/>`true`                                          | True for falling lava, false for lava with a block below. |
| level   | `1`           | `1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8` | Height of the lava, 8 when the lava is falling.           |

