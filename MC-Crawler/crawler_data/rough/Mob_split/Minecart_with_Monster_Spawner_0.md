# Minecart with Monster Spawner
Minecarts with monster spawners are a combination of both minecarts and monster spawner.

## Contents
- 1 Obtaining
- 2 Usage
- 3 Drops
- 4 Sounds
- 5 Data values
	- 5.1 ID
	- 5.2 Entity data
- 6 History
- 7 Issues
- 8 Gallery
- 9 References

## Obtaining
Minecarts with monster spawners cannot be obtained as an item in the inventory, and can only be produced using the /summon command or by using external tools.

## Usage
Main article: Monster Spawner
The monster spawner within behaves the same way as normal monster spawners, but the entity to be spawned cannot be set via using spawn eggs; the monster spawner's data can only be modified using commands or NBT edits. It has the same associated NBT tags as a normal monster spawner.[1]

More precisely, a minecart with monster spawner acts as a monster spawner block at the minecart's position. In other words, if the minecart with monster spawner moved within a block position, the range of spawn would not change, but if it moved 5 blocks east, the range of spawn would now be centered at the minecart with monster spawner's new position.

Spawner minecarts were used in some custom maps as a way to have redstone controlled monster spawners, however after the addition of the /summon and /setblock commands they were mostly rendered obsolete and are very rarely used today.

## Drops
When they are broken, minecarts with monster spawners drop 1 minecart. The monster spawner does not drop.

## Data values
### ID
| Entity                        | Identifier         | Translation key                     |
|-------------------------------|--------------------|-------------------------------------|
| Minecart with Monster Spawner | `spawner_minecart` | `entity.minecraft.spawner_minecart` |

### Entity data
See also: Entity format

Minecarts with monster spawners have entity data associated with them that contain various properties of the entity.

- Entity data
	- 
	- Tags common to all entities
	- 
	- Tags common to all minecarts
	- 
	- Tags common to monster spawner and minecart with monster spawner


