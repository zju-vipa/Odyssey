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



