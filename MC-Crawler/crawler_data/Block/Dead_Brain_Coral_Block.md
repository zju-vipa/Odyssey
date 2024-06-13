# Dead Coral Block
A dead coral block is a dead variant of a coral block. These blocks are always grey. There are five variants total: tube, brain, bubble, fire, and horn.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Post-generation
- 2 Usage
	- 2.1 Note blocks
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues
- 7 Gallery
	- 7.1 Screenshots
- 8 References

## Obtaining
### Breaking
Dead coral blocks can be obtained with any type of pickaxe. They can also be obtained by mining the respective live variant of coral blocks without Silk Touch.

| Block     | Dead Coral Block      |
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


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


### Natural generation
Dead coral block variants‌[Bedrock Edition  only] naturally generate in coral reef structures, which can be found in warm oceans. In Java Edition, dead coral blocks do not generate naturally.

### Post-generation
If a live coral block is placed outside of water, it transforms into its respective dead coral block after a few seconds — a grayscale version of the coral block. A coral block still dies if the game rule randomTickSpeed is set to 0.[1]

## Usage
Dead coral blocks can be used for building or as decoration blocks. Unlike live coral blocks, dead coral blocks cannot be used for farming sea pickles. It is not possible to turn a dead coral block back into a live coral block.

### Note blocks
All types of dead coral blocks can be placed under note blocks to produce "bass drum" sounds.

## Data values
### ID
Java Edition:

| Name                    | Identifier              | Form         | Translation key                         |
|-------------------------|-------------------------|--------------|-----------------------------------------|
| Dead Tube Coral Block   | dead_tube_coral_block   | Block & Item | block.minecraft.dead_tube_coral_block   |
| Dead Brain Coral Block  | dead_brain_coral_block  | Block & Item | block.minecraft.dead_brain_coral_block  |
| Dead Bubble Coral Block | dead_bubble_coral_block | Block & Item | block.minecraft.dead_bubble_coral_block |
| Dead Fire Coral Block   | dead_fire_coral_block   | Block & Item | block.minecraft.dead_fire_coral_block   |
| Dead Horn Coral Block   | dead_horn_coral_block   | Block & Item | block.minecraft.dead_horn_coral_block   |

Bedrock Edition:

| Name                    | Identifier                                    | Alias ID         | Numeric ID | Form                       | Item ID[i 1]   | Translation key                                                                                                                                                |
|-------------------------|-----------------------------------------------|------------------|------------|----------------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Dead Coral Blocks       | coral_block‌[until BE 1.21.0]                 | None             | -132       | Block & Giveable Item[i 2] | Identical[i 3] | tile.coral_block.blue_dead.nametile.coral_block.pink_dead.nametile.coral_block.purple_dead.nametile.coral_block.red_dead.nametile.coral_block.yellow_dead.name |
| Dead Tube Coral Block   | dead_tube_coral_block‌[upcoming: BE 1.21.0]   | coral_block / 8  | -853       | Block & Giveable Item[i 2] | Identical[i 3] | tile.coral_block.blue_dead.name                                                                                                                                |
| Dead Brain Coral Block  | dead_brain_coral_block‌[upcoming: BE 1.21.0]  | coral_block / 9  | -854       | Block & Giveable Item[i 2] | Identical[i 3] | tile.coral_block.pink_dead.name                                                                                                                                |
| Dead Bubble Coral Block | dead_bubble_coral_block‌[upcoming: BE 1.21.0] | coral_block / 10 | -855       | Block & Giveable Item[i 2] | Identical[i 3] | tile.coral_block.purple_dead.name                                                                                                                              |
| Dead Fire Coral Block   | dead_fire_coral_block‌[upcoming: BE 1.21.0]   | coral_block / 11 | -856       | Block & Giveable Item[i 2] | Identical[i 3] | tile.coral_block.red_dead.name                                                                                                                                 |
| Dead Horn Coral Block   | dead_horn_coral_block‌[upcoming: BE 1.21.0]   | coral_block / 12 | -857       | Block & Giveable Item[i 2] | Identical[i 3] | tile.coral_block.yellow_dead.name                                                                                                                              |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ a b c d e f Available with /give command.

↑ a b c d e f The block's direct item form has the same id as the block.


### Block states
See also: Block states

Bedrock Edition:

| Name        | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                              |
|-------------|---------------|---------------|----------------|-------------------------|------------------------------------------|
| coral_color | 0x10x20x4     | blue          | blue           | 0                       | Tube Coral Block                         |
|             |               |               | pink           | 1                       | Brain Coral Block                        |
|             |               |               | purple         | 2                       | Bubble Coral Block                       |
|             |               |               | red            | 3                       | Fire Coral Block                         |
|             |               |               | yellow         | 4                       | Horn Coral Block                         |
| dead_bit    | 0x8           | false         | falsetrue      | 01                      | Whether or not this coral block is dead. |



