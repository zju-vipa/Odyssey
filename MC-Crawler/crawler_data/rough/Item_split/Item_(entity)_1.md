### Damage
Items cannot be attacked by players or mobs; attempting to do so simply hits through them. However, they take damage and disappear from environmental or block-based damage such as explosions, fire, lava, and contact with cacti. Items have essentially no health, so they are destroyed by the slightest damage, though if set on fire they may remain for a few seconds before disappearing. Nether stars are immune to explosions, and netherite-based items and tools are immune to fire and float on top of lava. Also, some blocks that normally damage mobs, such as magma blocks, campfires, sweet berry bushes, wither roses and powder snow, do not damage items.

### Despawning
Items despawn after 6000 game ticks (5 minutes) of being in a loaded, entity-ticking chunk; this is affected by the player's simulation distance. If two item stacks merge, the timer is set to the item that has more time remaining. The 5-minute timer is paused when the chunk is unloaded or no longer processing entities. In Bedrock Edition, nether stars do not despawn.

Items that fall into the void immediately despawn when they fall below world minumum height - 64 so Y=-128 in the Overworld, Y=-64 in the Nether and the End.

## Data values
### ID
Java Edition:

| Name | Identifier | Translation key         |
|------|------------|-------------------------|
| Item | `item`     | `entity.minecraft.item` |

Bedrock Edition:

| Name | Identifier | Numeric ID | Translation key    |
|------|------------|------------|--------------------|
| Item | `item`     | `64`       | `entity.item.name` |

### Entity data
See also: Chunk format

Dropped items have entity data associated with them that contain various properties of the entity.

Java Edition:

Main article: Entity format
- Entity data
	- 
	- Tags common to all entities
	- Age: The number of ticks the item has been "untouched". After 6000 ticks (5 minutes) the item is destroyed. If set to -32768, the Age does not increase, preventing the item from despawning automatically.
	- Health: The health of the item, which starts at 5. Items take damage from fire, lava, cacti and explosions. The item is destroyed when its health reaches 0.
	- Item: The inventory item, without the Slot tag.
		- 
		- Tags common to all items
	- Owner: If present, only the player with thisUUIDcan pick up the item. Used by thegive command(and can be set in a summon command) to prevent the wrong player from picking up the spawned item entity.
	- PickupDelay: The number of ticks the item cannot be picked up. Decreases by 1 per tick. If set to 32767, the PickupDelay does not decrease, preventing the item from being picked up.
	- Thrower: TheUUIDof the player who dropped the item. Not present if the item was not dropped by a player.

Bedrock Edition:

SeeBedrock Edition level format/Entity format.

