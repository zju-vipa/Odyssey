# Zombie Head
A zombie head is a block modeled after the head of a zombie.

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
	- 8.2 In other media
- 9 References

## Obtaining
### Breaking
A zombie head can be mined using any item,[1] and drops itself when broken.

| Block    | Zombie Head         |
|----------|---------------------|
| Hardness | 1                   |
|          | Breakingtime (secs) |
| Default  | 1.5                 |

If a zombie head is pushed by a piston or comes in contact with water or lava, it breaks off as an item.

When destroyed by an explosion, the zombie head always drops as an item.

### Mob loot
Zombie heads are always dropped by a zombie if it dies due to a charged creeper's explosion. In Bedrock Edition, if multiple mobs are killed by the same charged creeper, all of them drop their heads, however in Java Edition only one mob selected at random drops its head.[2]

| Source | Roll Chance | Quantity (Roll Chance) |           |            |             |
|--------|-------------|------------------------|-----------|------------|-------------|
|        |             | Default                | Looting I | Looting II | Looting III |
| Zombie | 100%[d 1]   | 1                      | 1         | 1          | 1           |

1. ↑Only dropped when killed by a charged creeper.

## Usage
### Decoration
Zombie heads can be oriented in 16 different directions on top of a block, and 4 directions on the sides of blocks, similar to signs. They can be placed on top of, or beside each other by shift clicking.

### Wearing
See also:  § Renders

The player can wear zombie heads, similarly to pumpkins or helmets. This overlays the second layer of the player's skin.

#### Disguise
Wearing a zombie head reduces the detection range for zombies to 50% of the normal range. This is similar to (and stacks with) the reductions in detection range from sneaking and from the Invisibility status effect.

In Bedrock Edition, wearing a zombie head makes the player invisible to other players on a locator map.

### Dispensers
A dispenser can equip a zombie head on a player, mob, or armor stand with an empty helmet slot, within the block the dispenser is facing.

### Crafting ingredient
| Ingredients                             | Crafting recipe |
|-----------------------------------------|-----------------|
| Zombie head +<br/>Gunpowder+<br/>AnyDye |                 |

### Enchantments
Zombie heads can receive the following enchantments, but only through an anvil.

| Name               | Max level | Method |
|--------------------|-----------|--------|
| Curse of Binding   | I         | Anvil  |
| Curse of Vanishing | I         | Anvil  |

### Note blocks
Placing a zombie head above a note block causes the note block to play the zombie's ambient sound when activated.

The block below the note block does not affect the mob sound it creates.

## Data values
### ID
Java Edition:

| Name             | Identifier         | Form         | Translation key                    |
|------------------|--------------------|--------------|------------------------------------|
| Zombie Head      | `zombie_head`      | Block & Item | `block.minecraft.zombie_head`      |
| Zombie Wall Head | `zombie_wall_head` | Block        | `block.minecraft.zombie_wall_head` |

| Name         | Identifier |
|--------------|------------|
| Block entity | `skull`    |

Bedrock Edition:

| Zombie Head | Identifier | Numeric ID | Form                         | Item ID[i 1] | Translation key          |
|-------------|------------|------------|------------------------------|--------------|--------------------------|
| Block       | `skull`    | `144`      | Block & Ungiveable Item[i 2] | `item.skull` | —                        |
| Item        | `skull`    | `516`      | Item                         | —            | `item.skull.zombie.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Unavailable with /give command

| Name         | Savegame ID |
|--------------|-------------|
| Block entity | `Skull`     |

### Metadata
See also: Data values

In Bedrock Edition, zomie heads use the following data values:
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



