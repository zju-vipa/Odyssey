# Coral Fan
Coral fans are non-solid blocks that come in 5 variants: tube, brain, bubble, fire, and horn.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Post-generation
		- 1.3.1 Bone meal
	- 1.4 Wall Coral Fans
- 2 Usage
	- 2.1 Placement
		- 2.1.1 Water
	- 2.2 Pushing with pistons
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
	- 5.1 Asset history
- 6 Issues
- 7 Gallery
	- 7.1 Screenshots
- 8 References

## Obtaining
### Breaking
Coral fans can be mined instantly but can be obtained only when mined with a Silk Touch enchanted tool. Breaking coral fans without Silk Touch destroys the coral fan.

| Block    | Coral Fan           |
|----------|---------------------|
| Hardness | 0                   |
|          | Breakingtime (secs) |
| Default  | 0.05                |

### Natural generation
Coral fans naturally generate in coral reef structures.


### Post-generation
#### Bone meal
When bone meal is used in warm ocean biomes, it has a chance of generating coral fans (this does not work in Bedrock Edition, due to MCPE-171383).

### Wall Coral Fans
Wall coral fans cannot be obtained through vanilla means. In Java Edition, they are completely unobtainable, but in Bedrock Edition, they can be obtained through add-ons or inventory editing, though the item form is badly glitched to the point of being completely nameless.

## Usage
Coral fans can be used for building or as decoration blocks.

### Placement
All coral fans can be placed on the four sides and the top surface of blocks; they cannot be placed on the bottom surface.

#### Water
In order for coral fans to stay alive, they must be placed in water. In Java Edition, coral fans can also be placed outside of water as long as one of the blocks surrounding it contains water. If placed outside of water, they transform into their respective dead coral fan immediately‌[Bedrock Edition  only] or after 3 to 4.95 seconds‌[Java Edition  only]. Once a coral fan dies, it is not possible to turn a dead coral fan back into a live coral fan.

### Pushing with pistons
Live coral fans cannot be pushed by pistons (attempting to do so results in the coral fan breaking).

## Data values
### ID
Java Edition:

| Name                  | Identifier            | Form         | Block tags                      | Translation key                       |
|-----------------------|-----------------------|--------------|---------------------------------|---------------------------------------|
| Tube Coral Fan        | tube_coral_fan        | Block & Item | coralsunderwater_bonemeals      | block.minecraft.tube_coral_fan        |
| Brain Coral Fan       | brain_coral_fan       | Block & Item | coralsunderwater_bonemeals      | block.minecraft.brain_coral_fan       |
| Bubble Coral Fan      | bubble_coral_fan      | Block & Item | coralsunderwater_bonemeals      | block.minecraft.bubble_coral_fan      |
| Fire Coral Fan        | fire_coral_fan        | Block & Item | coralsunderwater_bonemeals      | block.minecraft.fire_coral_fan        |
| Horn Coral Fan        | horn_coral_fan        | Block & Item | coralsunderwater_bonemeals      | block.minecraft.horn_coral_fan        |
| Tube Coral Wall Fan   | tube_coral_wall_fan   | Block        | underwater_bonemealswall_corals | block.minecraft.tube_coral_wall_fan   |
| Brain Coral Wall Fan  | brain_coral_wall_fan  | Block        | underwater_bonemealswall_corals | block.minecraft.brain_coral_wall_fan  |
| Bubble Coral Wall Fan | bubble_coral_wall_fan | Block        | underwater_bonemealswall_corals | block.minecraft.bubble_coral_wall_fan |
| Fire Coral Wall Fan   | fire_coral_wall_fan   | Block        | underwater_bonemealswall_corals | block.minecraft.fire_coral_wall_fan   |
| Horn Coral Wall Fan   | horn_coral_wall_fan   | Block        | underwater_bonemealswall_corals | block.minecraft.horn_coral_wall_fan   |

Bedrock Edition:

| Name                            | Identifier                              | Alias ID      | Numeric ID | Form                         | Item ID[i 1]   | Translation key                                                                                                                                 |
|---------------------------------|-----------------------------------------|---------------|------------|------------------------------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Coral Fan                       | coral_fan‌[until BE 1.20.80]            | None          | -133       | Block & Giveable Item[i 2]   | Identical[i 3] | tile.coral_fan.blue_fan.nametile.coral_fan.pink_fan.nametile.coral_fan.purple_fan.nametile.coral_fan.red_fan.nametile.coral_fan.yellow_fan.name |
| Tube Coral Fan                  | tube_coral_fan‌[upcoming: BE 1.20.80]   | coral_fan / 0 | -133       | Block & Giveable Item[i 2]   | Identical[i 3] | tile.coral_fan.blue_fan.name                                                                                                                    |
| Brain Coral Fan                 | brain_coral_fan‌[upcoming: BE 1.20.80]  | coral_fan / 1 | -840       | Block & Giveable Item[i 2]   | Identical[i 3] | tile.coral_fan.pink_fan.name                                                                                                                    |
| Bubble Coral Fan                | bubble_coral_fan‌[upcoming: BE 1.20.80] | coral_fan / 2 | -841       | Block & Giveable Item[i 2]   | Identical[i 3] | tile.coral_fan.purple_fan.name                                                                                                                  |
| Fire Coral Fan                  | fire_coral_fan‌[upcoming: BE 1.20.80]   | coral_fan / 3 | -842       | Block & Giveable Item[i 2]   | Identical[i 3] | tile.coral_fan.red_fan.name                                                                                                                     |
| Horn Coral Fan                  | horn_coral_fan‌[upcoming: BE 1.20.80]   | coral_fan / 4 | -843       | Block & Giveable Item[i 2]   | Identical[i 3] | tile.coral_fan.yellow_fan.name                                                                                                                  |
| Coral Wall Fan(tube and brain)  | coral_fan_hang                          | None          | 390        | Block & Ungiveable Item[i 4] | Identical[i 3] | —                                                                                                                                               |
| Coral Wall Fan(bubble and fire) | coral_fan_hang2                         | None          | 391        | Block & Ungiveable Item[i 4] | Identical[i 3] | —                                                                                                                                               |
| Coral Wall Fan(horn)            | coral_fan_hang3                         | None          | 392        | Block & Ungiveable Item[i 4] | Identical[i 3] | —                                                                                                                                               |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ a b c d e f Available with /give command.

↑ a b c d e f g h i The block's direct item form has the same id as the block.

↑ a b c Unavailable with /give command


### Block states
See also: Block states

Java Edition
Floor:

| Name        | Default value | Allowed values | Description                                                       |
|-------------|---------------|----------------|-------------------------------------------------------------------|
| waterlogged | true          | falsetrue      | Whether or not there's water in the same place as this coral fan. |

Wall:

| Name        | Default value | Allowed values     | Description                                                                                                                                               |
|-------------|---------------|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing      | north         | eastnorthsouthwest | The direction in which the coral fan juts out from the block it is attached to.For example, a coral fan facing north is attached to a block to its south. |
| waterlogged | true          | falsetrue          | Whether or not there's water in the same place as this coral fan.                                                                                         |

Bedrock Edition
Floor:

| Name                | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                                  |
|---------------------|---------------|---------------|----------------|-------------------------|--------------------------------------------------------------|
| coral_color         | 0x10x20x4     | blue          | blue           | 0                       | Tube Coral Fan                                               |
|                     |               |               | pink           | 1                       | Brain Coral Fan                                              |
|                     |               |               | purple         | 2                       | Bubble Coral Fan                                             |
|                     |               |               | red            | 3                       | Fire Coral Fan                                               |
|                     |               |               | yellow         | 4                       | Horn Coral Fan                                               |
| coral_fan_direction | 0x8           | 0             | 01             | 01                      | The direction the coral is facing. East-west or north-south. |

Wall:

| Name                | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                                                                                                                               |
|---------------------|---------------|---------------|----------------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| coral_hang_type_bit | 0x1           | false         | falsetrue      | 01                      | Which coral it is; depends on the ID.Forhangfalse means tube and true means brain.Forhang2false means bubble and true means fire.Forhang3false mean horn. |
| coral_direction     | 0x40x8        | 0             | 0123           | 0123                    | The direction the top of the fan is facing.0: west 1: east 2: north 3: south                                                                              |
| dead_bit            | 0x2           | false         | falsetrue      | 01                      | Whether or not this coral is dead.                                                                                                                        |



