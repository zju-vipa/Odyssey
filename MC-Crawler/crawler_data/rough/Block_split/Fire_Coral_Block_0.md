# Coral Block
A coral block is a solid block that comes in five variants: tube, brain, bubble, fire, and horn.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Trading
- 2 Usage
	- 2.1 Placement
	- 2.2 Sea pickle farm blocks
	- 2.3 Note Blocks
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 Trivia
- 8 Gallery
	- 8.1 Screenshots
	- 8.2 Development images
- 9 References
- 10 External links

## Obtaining
### Breaking
Coral blocks can be obtained only with a pickaxe enchanted with Silk Touch; if mined with a pickaxe not enchanted with Silk Touch, they drop the respective dead coral block.

| Block     | Coral Block           |
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

### Natural generation
Coral blocks naturally generate in coral reef structures, which can be found in warm oceans.

### Trading
Coral blocks can be bought from wandering traders for 3 emeralds each.

## Usage


North



































East



































South



































West



































Example




































Schematic of valid block placements for coral blockswith water around. Several ways are shown where thearrangement would cause coral blocks to stay aliveor die.


Coral blocks can be used for building or as decoration blocks.

### Placement
In order for a coral block to stay alive, at least one of the six directly adjacent blocks must be water or a waterlogged block. If placed outside of water, it transforms into its respective dead coral block after 3 to 4.95 seconds‌[Java Edition  only] or 2.25 seconds‌[Bedrock Edition  only] — a grayscale version of the coral block. A coral block still dies if the game rule randomTickSpeed is set to 0.[1] Once a coral block dies, it is not possible to turn a dead coral block into a live coral block.

In Bedrock Edition, coral blocks do not die if they are surrounded by any non-air blocks.[2]

### Sea pickle farm blocks
If sea pickles are planted on live coral blocks, using bone meal on the sea pickles increases the number of sea pickles and creates more sea pickles on nearby coral blocks. Specifically, they can spread to the original sea pickle's level or one level below, out to a horizontal taxicab distance of 2. This only works on living coral blocks, not dead coral blocks.

### Note Blocks
All types of coral blocks can be placed under note blocks to produce "bass drum" sounds.

## Data values
### ID
Java Edition:

| Name               | Identifier           | Form         | Block tags                            | Translation key                      |
|--------------------|----------------------|--------------|---------------------------------------|--------------------------------------|
| Tube Coral Block   | `tube_coral_block`   | Block & Item | `coral_blocks`<br/>`mineable/pickaxe` | `block.minecraft.tube_coral_block`   |
| Brain Coral Block  | `brain_coral_block`  | Block & Item | `coral_blocks`<br/>`mineable/pickaxe` | `block.minecraft.brain_coral_block`  |
| Bubble Coral Block | `bubble_coral_block` | Block & Item | `coral_blocks`<br/>`mineable/pickaxe` | `block.minecraft.bubble_coral_block` |
| Fire Coral Block   | `fire_coral_block`   | Block & Item | `coral_blocks`<br/>`mineable/pickaxe` | `block.minecraft.fire_coral_block`   |
| Horn Coral Block   | `horn_coral_block`   | Block & Item | `coral_blocks`<br/>`mineable/pickaxe` | `block.minecraft.horn_coral_block`   |

Bedrock Edition:

| Name               | Identifier                                 | Alias ID          | Numeric ID | Form                       | Item ID[i 1]   | Translation key                                                                                                                                                     |
|--------------------|--------------------------------------------|-------------------|------------|----------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Coral Blocks       | `coral_block‌[until BE 1.21.0]`            | None              | `-132`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.coral_block.blue.name`<br/>`tile.coral_block.pink.name`<br/>`tile.coral_block.purple.name`<br/>`tile.coral_block.red.name`<br/>`tile.coral_block.yellow.name` |
| Tube Coral Block   | `tube_coral_block‌[upcoming: BE 1.21.0]`   | `coral_block / 0` | `-132`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.coral_block.blue.name`                                                                                                                                        |
| Brain Coral Block  | `brain_coral_block‌[upcoming: BE 1.21.0]`  | `coral_block / 1` | `-849`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.coral_block.pink.name`                                                                                                                                        |
| Bubble Coral Block | `bubble_coral_block‌[upcoming: BE 1.21.0]` | `coral_block / 2` | `-850`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.coral_block.purple.name`                                                                                                                                      |
| Fire Coral Block   | `fire_coral_block‌[upcoming: BE 1.21.0]`   | `coral_block / 3` | `-851`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.coral_block.red.name`                                                                                                                                         |
| Horn Coral Block   | `horn_coral_block‌[upcoming: BE 1.21.0]`   | `coral_block / 4` | `-852`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.coral_block.yellow.name`                                                                                                                                      |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑ a b c d e fAvailable with /give command.
3. ↑ a b c d e fThe block's direct item form has the same id as the block.

### Block states
See also: Block states

Bedrock Edition:

| Name        | Metadata Bits             | Default value | Allowed values     | Values forMetadata Bits | Description                              |
|-------------|---------------------------|---------------|--------------------|-------------------------|------------------------------------------|
| coral_color | `0x1`<br/>`0x2`<br/>`0x4` | `blue`        | `blue`             | `0`                     | Tube Coral Block                         |
|             |                           |               | `pink`             | `1`                     | Brain Coral Block                        |
|             |                           |               | `purple`           | `2`                     | Bubble Coral Block                       |
|             |                           |               | `red`              | `3`                     | Fire Coral Block                         |
|             |                           |               | `yellow`           | `4`                     | Horn Coral Block                         |
| dead_bit    | `0x8`                     | `false`       | `false`<br/>`true` | `0`<br/>`1`             | Whether or not this coral block is dead. |




