# Creeper Head
A creeper head is a block modeled after the head of a creeper.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Mob loot
- 2 Usage
	- 2.1 Decoration
	- 2.2 Wearing
		- 2.2.1 Disguise
	- 2.3 Dispensers
	- 2.4 Crafting ingredient
	- 2.5 Enchantments
	- 2.6 Note blocks
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Metadata
	- 4.3 Block states
- 5 Achievements
- 6 History
- 7 Issues
- 8 Gallery
	- 8.1 Renders
- 9 References

## Obtaining
### Breaking
A creeper head can be mined using any item,[1] and drops itself when broken.

| Block    | Creeper Head        |
|----------|---------------------|
| Hardness | 1                   |
|          | Breakingtime (secs) |
| Default  | 1.5                 |

If a creeper head is pushed by a piston or comes in contact with water or lava, it breaks off as an item.

When destroyed by an explosion, the creeper head always drops as an item.

### Mob loot
Creeper heads are always dropped by a creeper if it dies due to a charged creeper's explosion. In Bedrock Edition, if multiple mobs are killed by the same charged creeper, all of them drop their heads, however in Java Edition only one mob selected at random drops its head.[2]

| Source  | Roll Chance | Quantity (Roll Chance) |           |            |             |
|---------|-------------|------------------------|-----------|------------|-------------|
|         |             | Default                | Looting I | Looting II | Looting III |
| Creeper | 100%[d 1]   | 1                      | 1         | 1          | 1           |


↑ Only dropped when killed by a charged creeper.


## Usage
### Decoration
Creeper heads can be oriented in 16 different directions on top of a block, and 4 directions on the sides of blocks, similar to signs. They can be placed on top of, or beside each other by shift clicking.

### Wearing
See also:  § Renders

The player can wear creeper heads, similarly to pumpkins or helmets. This overlays the second layer of the player's skin.

#### Disguise
Wearing a creeper head reduces the detection range for creepers to 50% of the normal range. This is similar to (and stacks with) the reductions in detection range from sneaking and from the Invisibility status effect.

In Bedrock Edition, wearing a creeper head makes the player invisible to other players on a locator map.

### Dispensers
A dispenser can equip a creeper head on a player, mob, or armor stand with an empty helmet slot, within the block the dispenser is facing.

### Crafting ingredient
| Name                   | Ingredients                    | Crafting recipe |
|------------------------|--------------------------------|-----------------|
| Banner Pattern Creeper | Paper+Creeper Head             |                 |
| Firework Star          | Creeper head +Gunpowder+AnyDye |                 |

### Enchantments
Creeper heads can receive the following enchantments, but only through an anvil.

| Name               | Max level | Method |
|--------------------|-----------|--------|
| Curse of Binding   | I         | Anvil  |
| Curse of Vanishing | I         | Anvil  |

### Note blocks
Placing a creeper head above a note block causes the note block to play the creeper's primed (hissing) sound when activated. This is unlike other mob heads, as creepers don't make ambient sounds.

The block below the note block does not affect the mob sound it creates.

## Data values
### ID
Java Edition:

| Name              | Identifier        | Form         | Translation key                   |
|-------------------|-------------------|--------------|-----------------------------------|
| Creeper Head      | creeper_head      | Block & Item | block.minecraft.creeper_head      |
| Creeper Wall Head | creeper_wall_head | Block        | block.minecraft.creeper_wall_head |

| Name         | Identifier |
|--------------|------------|
| Block entity | skull      |

Bedrock Edition:

| Creeper Head | Identifier | Numeric ID | Form                         | Item ID[i 1] | Translation key         |
|--------------|------------|------------|------------------------------|--------------|-------------------------|
| Block        | skull      | 144        | Block & Ungiveable Item[i 2] | item.skull   | —                       |
| Item         | skull      | 516        | Item                         | —            | item.skull.creeper.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Unavailable with /give command


| Name         | Savegame ID |
|--------------|-------------|
| Block entity | Skull       |

### Metadata
See also: Data values

In Bedrock Edition, mob heads use the following data values:
For the item and for the tile entity, data values determine the skull type:

|  | DV | Description           |
|--|----|-----------------------|
|  | 0  | Skeleton Skull        |
|  | 1  | Wither Skeleton Skull |
|  | 2  | Zombie Head           |
|  | 3  | Head                  |
|  | 4  | Creeper Head          |
|  | 5  | Dragon Head           |

### Block states
See also: Block states

Java Edition:
Floor

| Name     | Default value | Allowed values | Description                          |
|----------|---------------|----------------|--------------------------------------|
| rotation | 0             | 0              | The block is facing south.           |
|          |               | 1              | The block is facing south-southwest. |
|          |               | 2              | The block is facing southwest.       |
|          |               | 3              | The block is facing west-southwest.  |
|          |               | 4              | The block is facing west.            |
|          |               | 5              | The block is facing west-northwest.  |
|          |               | 6              | The block is facing northwest.       |
|          |               | 7              | The block is facing north-northwest. |
|          |               | 8              | The block is facing north.           |
|          |               | 9              | The block is facing north-northeast. |
|          |               | 10             | The block is facing northeast.       |
|          |               | 11             | The block is facing east-northeast.  |
|          |               | 12             | The block is facing east.            |
|          |               | 13             | The block is facing east-southeast.  |
|          |               | 14             | The block is facing southeast.       |
|          |               | 15             | The block is facing south-southeast. |

Wall

| Name   | Default value | Allowed values     | Description                                                                                      |
|--------|---------------|--------------------|--------------------------------------------------------------------------------------------------|
| facing | north         | eastnorthsouthwest | The direction the head is facing.Opposite from the direction a player is facing when placing it. |

Bedrock Edition:

| Name             | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                          |
|------------------|---------------|---------------|----------------|-------------------------|------------------------------------------------------|
| facing_direction | 0x10x20x4     | 0             | 1              | 1                       | On the floor (rotation is stored in the tile entity) |
|                  |               |               | 2              | 2                       | On a wall, facing north                              |
|                  |               |               | 3              | 3                       | On a wall, facing south                              |
|                  |               |               | 4              | 4                       | On a wall, facing east                               |
|                  |               |               | 5              | 5                       | On a wall, facing west                               |
|                  |               |               | 0              | 0                       | Unused                                               |



