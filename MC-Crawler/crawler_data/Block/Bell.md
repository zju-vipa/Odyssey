# Bell
A bell is a transparent, animated block entity that produces a sound when used. Unlike most utility blocks, bells cannot be crafted.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Chest loot
	- 1.4 Trading
- 2 Usage
	- 2.1 Claiming
	- 2.2 Raid
		- 2.2.1 Glowing effect
	- 2.3 Piglins
	- 2.4 Redstone component
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
	- 4.3 Block data
- 5 Achievements
- 6 Advancements
- 7 History
- 8 Issues
- 9 Trivia
- 10 Gallery
	- 10.1 Renders
	- 10.2 Screenshots
- 11 References

## Obtaining
### Breaking
A bell can be mined by hand or with any tool, but using a pickaxe is fastest.

| Block     | Bell                  |
|-----------|-----------------------|
| Hardness  | 5                     |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 25                    |
| Wooden    | 3.75                  |
| Stone     | 1.9                   |
| Iron      | 1.25                  |
| Diamond   | 0.95                  |
| Netherite | 0.85                  |
| Golden    | 0.65                  |


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


### Natural generation
Bells can generate naturally in all village variants, usually near the center of the village in the meeting point.

### Chest loot
| Item | Structure     | Container | Quantity | Chance                         |
|------|---------------|-----------|----------|--------------------------------|
|      |               |           |          | Java EditionandBedrock Edition |
| Bell | Ruined Portal | Chest     | 1        | 1.5%                           |

### Trading
In Java Edition, apprentice-level armorer villagers have a 50% chance to sell a bell for 36 emeralds. Apprentice-level toolsmith and weaponsmith villagers always offer to sell a bell for 36 emeralds.

In Bedrock Edition, apprentice-level armorer villagers have a 1⁄3 chance to sell a bell for 36 emeralds. Apprentice-level toolsmith villagers sell bells for 36 emeralds. Journeyman-level weaponsmith villagers sell bells for 36 emeralds.

## Usage
Bells can be anchored to the side of blocks, ceilings, and floors and drop as an item if the sustain block is broken or moved by a piston. They can also be attatched to trapdoors but break if the trapdoor is opened.

When the use control is pressed while looking at the side of a bell, it produces a sound as well as a "swaying" animation. A bell can also be rung using a redstone signal, by any projectile, or by dropping an item on it.

If the player rings the bell while villagers are sleeping, all of the villagers wake up. Bells can be rung by players only from certain angles (villagers are not subject to this restriction); trying from an incorrect angle does not cause the bell to ring.

Villagers ring the bell only during raids.

### Claiming
A villager can detect a bell within 48 blocks euclidean distance horizontally and 6 block vertically (either up or down) from the base of his hitbox and can claim it if he gets within 6 blocks taxicab distance of it and there is a valid path that can lead them to be in the block right besides the bell. Baby villagers do not claim nor ring a bell.   

When villagers spawn (either naturally or by commands) and have not already claimed a bed or workstation will automatically claim any bell 6 blocks from them, even if they can't reach it. Also, when a bell is placed within 48 blocks from the pillow of a claimed bed and there is a valid path a villager can walk through, the bell gets automatically claimed in the afternoon (between 9000t and 12000t), which is displayed by green particles appearing above the bell. This does not work with claimed workstations.  

Claimed bells are POIs and determine the position of a village center among claimed beds and workstations.

When a player subject to the bad omen effect enters a village with a bell, the claiming mechanisms are forced no matter the time. So if the bell is close enough either from a villager or from a claimed bed it becomes part of the village.

A claimed bell defines a gathering site of a village and villagers pathfind close to it in the afternoon. If the bell is broken, anger particles appear above the village leader's head. 

If a player rings a bell, the villagers run to their houses even if there is no raid. They can activate a bell even through blocks but only if it was previously claimed and at least 2 blocks (also diagonal) from the base of their hitbox.

### Raid
See also: Tutorials/Defeating a village raid

When the bell is rung, villagers within a distance of 32 blocks run into their houses immediately.

When a raid's first wave appears, in Java Edition, at least one villager rushes to ring the bell in the center of the village (if they are close enough) to warn the other villagers of an incoming raid before going into their house. In Bedrock Edition, bells in the corresponding village ring automatically at the start of a raid, warning villagers to return to their houses.

#### Glowing effect
Additionally, in Java Edition, if a bell is rung and there is a raid mob within a 32 block spherical range, the Glowing effect is applied to all raid mobs within 48 blocks, and  particles appear. It produces a resonating sound once this process is complete. The raid mobs don't have to be actively participating in a raid to receive the Glowing effect: the effect applies to illagers in woodland mansions, or witches that naturally spawns in the Overworld.

### Piglins
Piglins admire bells as golden items. However, breaking a bell does not aggravate them.[1]

### Redstone component
In Bedrock Edition, observers can detect when a bell is rung. Observers do not emit a signal when the bell stops ringing or becomes unpowered.

## Data values
### ID
Java Edition:

| Name | Identifier | Form         | Item tags    | Translation key      |
|------|------------|--------------|--------------|----------------------|
| Bell | bell       | Block & Item | piglin_loved | block.minecraft.bell |

| Name         | Identifier |
|--------------|------------|
| Block entity | bell       |

Bedrock Edition:

| Name | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key |
|------|------------|------------|----------------------------|----------------|-----------------|
| Bell | bell       | 461        | Block & Giveable Item[i 2] | Identical[i 3] | tile.bell.name  |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


| Name         | Savegame ID |
|--------------|-------------|
| Block entity | Bell        |

### Block states
See also: Block states

Java Edition:

| Name       | Default value | Allowed values                     | Description                                                                                        |
|------------|---------------|------------------------------------|----------------------------------------------------------------------------------------------------|
| attachment | floor         | ceilingdouble_wallfloorsingle_wall | What the bell is attached to.                                                                      |
| facing     | north         | eastnorthsouthwest                 | The direction the bell is facing.Opposite from the direction the player faces when placing a bell. |
| powered    | false         | truefalse                          | Whether the bell is attached to a power source, such as a redstone torch.                          |

Bedrock Edition:

| Name       | Metadata Bits | Default value | Allowed values              | Values forMetadata Bits | Description                                                                                                                                                                           |
|------------|---------------|---------------|-----------------------------|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| attachment | 0x40x8        | standing      | standinghangingsidemultiple | 0123                    | What the bell is attached to.                                                                                                                                                         |
| direction  | 0x10x2        | 0             | 0123                        | 0123                    | The direction the bell is facing. Opposite from the direction a player faces when placing the block.0: South facing bell 1: West facing bell 2: North facing bell 3: East facing bell |
| toggle_bit | 0x10          | false         | falsetrue                   | 01                      | Each time the bell is rung, this value toggles between true and false.                                                                                                                |



### Block data
A bell has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format


 Block entity data
Tags common to all block entities

Bedrock Edition:

See Bedrock Edition level format/Block entity format.
