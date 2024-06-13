### Allay duplication
An allay duplicating.
If an allay is given an amethyst shard while it is dancing due to a nearby jukebox playing any music disc, it splits into two allays (itself and a new allay) and the amethyst shard is consumed. After duplication, both allays have a five minute cooldown before being able to duplicate again. Allays do not have a baby form.

### Teleportation

  

This feature is exclusive to  Bedrock Edition. 


When a player teleports through a nether portal, the player's allay teleports with them, even if it does not enter the portal.

When a player teleports through an end portal, the allay teleports to the End only if a player gives the allay an item before teleporting and must be nearby the player as they teleport.

Allays holding an item follow the player through a portal if they are 21 blocks horizontally to the player or if they are within 22 blocks vertically of the player's legs. Allays do not travel through portals regardless of how close they are if they are tethered to a fence with a lead.


## Data values
### ID
Java Edition:

| Name  | Identifier | Entity tags          | Translation key          |
|-------|------------|----------------------|--------------------------|
| Allay | `allay`    | `fall_damage_immune` | `entity.minecraft.allay` |

Bedrock Edition:

| Name  | Identifier | Numeric ID | Translation key     |
|-------|------------|------------|---------------------|
| Allay | `allay`    | `134`      | `entity.allay.name` |

### Entity data
Allays have entity data associated with them that contain various properties.

Java Edition:

Main article: Entity format
- Entity data
	- 
	- Tags common to all entities
	- 
	- Tags common to all mobs
	- CanDuplicate: 1 or 0 (true/false) – true if the allay can duplicate. This is set tofalsewhen the allay duplicates, andtruewhenDuplicationCooldownreaches 0.
	- DuplicationCooldown: The allay's duplication cooldown in ticks. This is set to 6000 game ticks (5 minutes) when the allay duplicates.
	- Inventory: List of items the allay has picked up. This list can contain at most one compound tag. The item given by the player to the allay is stored in itsHandItems[0]tag, not here.
		- 
		- Tags common to all items
	- listener: The vibration event listener of this allay.
		- distance: Nonnegative integer.
		- event: Optional.
			- distance: Nonnegative integer.
			- game_event: A resource location of the game event.
			- pos: Three doubles representing the X, Y, and Z coordinates.
			- projectile_owner: Optional. The projectile owner'sUUID. The 128-bit UUID is stored as four 32-bit integers, ordered from most to least significant.
			- source: Optional. The source entity'sUUID. The 128-bit UUID is stored as four 32-bit integers, ordered from most to least significant.
		- event_delay: Nonnegative integer.
		- event_distance: Nonnegative integer.
		- range: Nonnegative integer.
		- source: Position source.
			- type: A resource location of the position source type.
			- For typeblock
				- pos: X, Y, and Z coordinates.
			- For typeentity
				- source_entity: The entity'sUUID. The 128-bit UUID is stored as four 32-bit integers, ordered from most to least significant.
				- y_offset:

Bedrock Edition:

SeeBedrock Edition level format/Entity format.

