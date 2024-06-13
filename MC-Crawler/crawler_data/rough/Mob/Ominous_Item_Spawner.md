# Ominous Item Spawner
Ominous item spawners are entities that display an item for 3 to 6 seconds before dispensing it downwards.

## Contents
- 1 Behavior
- 2 Sounds
- 3 Data values
	- 3.1 ID
	- 3.2 Entity data
- 4 History
- 5 References

## Behavior
An ominous item spawner displays an item rotating in the air for a specified amount of time. When spawned by a ominous trial spawner, that time varies between 3 and 6 seconds. After that time, the item is dispensed downwards. If the item is a projectile, it is shot as an entity. Otherwise the item is dropped.

## Data values
### ID
Java Edition:

| Name                 | Identifier             | Translation key                         |
|----------------------|------------------------|-----------------------------------------|
| Ominous Item Spawner | `ominous_item_spawner` | `entity.minecraft.ominous_item_spawner` |

Bedrock Edition:

| Name                 | Identifier             | Numeric ID | Translation key |
|----------------------|------------------------|------------|-----------------|
| Ominous Item Spawner | `ominous_item_spawner` | `145`      | —               |

### Entity data
Ominous item spawners have entity data associated with them that contain various properties.

Java Edition:

Main article: Entity format
- Entity data
	- 
	- Tags common to all entities
	- item: The item to display and dispense.
		- 
		- Tags common to all items
	- spawn_item_after_ticks: Total time in ticks to display the item, before dispensing it. Currently not read from nbt.[1]

