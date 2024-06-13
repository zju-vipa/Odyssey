# Wither Skeleton Skull
A wither skeleton skull is a block modeled after the head of a wither skeleton, essential in the spawning of withers.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Mob loot
- 2 Usage
	- 2.1 Decoration
	- 2.2 Wearing
		- 2.2.1 Disguise
	- 2.3 Withers
	- 2.4 Dispensers
	- 2.5 Crafting ingredient
	- 2.6 Enchantments
	- 2.7 Note blocks
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Metadata
	- 4.3 Block states
- 5 Achievements
- 6 Advancements
- 7 History
- 8 Issues
- 9 Trivia
- 10 Gallery
- 11 References

## Obtaining
### Breaking
A wither skeleton skull can be mined using any item,[1] and drops itself when broken.

| Block    | Wither Skeleton Skull |
|----------|-----------------------|
| Hardness | 1                     |
|          | Breakingtime (secs)   |
| Default  | 1.5                   |

If a wither skeleton skull is pushed by a piston or comes in contact with water or lava, it breaks off as an item.

When destroyed by an explosion, the wither skeleton skull always drops as an item.

### Mob loot
A wither skeleton has a 2.5% chance of dropping a wither skeleton skull when killed by a player or a tamed wolf. The chance is increased by 1% per level of Looting, for a maximum of 5.5% with Looting III. In Bedrock Edition, the chance is increased by 2% per level of Looting, for a maximum of 8.5% with Looting III.

A wither skeleton skull is always dropped by a wither skeleton if it dies due to a charged creeper's explosion. In Bedrock Edition, if multiple mobs are killed by the same charged creeper, all of them drop their heads,[2] however in Java Edition only one mob selected at random drops its head.[3]

| Source              | Roll Chance    | Quantity (Roll Chance) |           |            |             |
|---------------------|----------------|------------------------|-----------|------------|-------------|
|                     |                | Default                | Looting I | Looting II | Looting III |
| Wither Skeleton(JE) | 2.5%–5.5%[d 1] | 1 (2.5%)               | 1 (3.5%)  | 1 (4.5%)   | 1 (5.5%)    |
| Wither Skeleton(BE) | 2.5%–8.5%[d 1] | 1 (2.5%)               | 1 (4.5%)  | 1 (6.5%)   | 1 (8.5%)    |
| Wither Skeleton     | 100%[d 2]      | 1                      | 1         | 1          | 1           |


↑ a b Only dropped when kill credit is given to the player

↑ Only when killed by a charged creeper. In Java Edition, only one skull or head drops per charged creeper explosion, even if multiple mobs are killed by it.


## Usage
### Decoration
Wither skeleton skulls can be oriented in 16 different directions on top of a block, and 4 directions on the sides of blocks, similar to signs. They can be placed on top of, or beside each other by shift clicking.

### Wearing
See also:  § Gallery

The player can wear wither skeleton skulls, similarly to pumpkins or helmets. This overlays the second layer of the player's skin.

#### Disguise
Unlike some other heads and skulls, wearing a wither skeleton skull does not reduce the detection range for wither skeletons.

In Bedrock Edition, wearing a wither skeleton skull makes the player invisible to other players on a locator map.

### Withers



















Wither build configuration


Withers can be spawned by placing soul sand or soul soil in a T shape, and putting 3 wither skeleton skulls on top of the T. The T can be horizontal or vertical. The last block placed must be one of the three wither skeleton skulls. A dispenser can also create a wither, by placing the final wither skeleton skull onto soul sand directly in front of and below it.

### Dispensers
A dispenser can equip a wither skeleton skull on a player, mob, or armor stand with an empty helmet slot, within the block the dispenser is facing.

Dispensers can also complete the construction of a wither.

### Crafting ingredient
| Name                 | Ingredients                            | Crafting recipe |
|----------------------|----------------------------------------|-----------------|
| Banner Pattern Skull | Paper+Wither Skeleton Skull            |                 |
| Firework Star        | Wither Skeleton Skull+Gunpowder+AnyDye |                 |

### Enchantments
Wither skeleton skulls can receive the following enchantments, but only through an anvil.

| Name               | Max level | Method |
|--------------------|-----------|--------|
| Curse of Binding   | I         | Anvil  |
| Curse of Vanishing | I         | Anvil  |

### Note blocks
Placing a wither skeleton skull above a note block causes the note block to play the wither skeleton's ambient sound when activated.

The block below the note block does not affect the mob sound it creates.

## Data values
### ID
Java Edition:

| Name                       | Identifier                 | Form         | Translation key                            |
|----------------------------|----------------------------|--------------|--------------------------------------------|
| Wither Skeleton Skull      | wither_skeleton_skull      | Block & Item | block.minecraft.wither_skeleton_skull      |
| Wither Skeleton Wall Skull | wither_skeleton_wall_skull | Block        | block.minecraft.wither_skeleton_wall_skull |

| Name         | Identifier |
|--------------|------------|
| Block entity | skull      |

Bedrock Edition:

| Wither Skeleton Skull | Identifier | Numeric ID | Form                         | Item ID[i 1] | Translation key        |
|-----------------------|------------|------------|------------------------------|--------------|------------------------|
| Block                 | skull      | 144        | Block & Ungiveable Item[i 2] | item.skull   | —                      |
| Item                  | skull      | 516        | Item                         | —            | item.skull.wither.name |


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



