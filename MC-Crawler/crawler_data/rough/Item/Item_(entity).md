# Item (entity)
Items are "dropped" blocks or items (non-block resources) that appear in the world, rather than being in the inventory of a player or block entity; they are a type of entity.

## Contents
- 1 Appearance
- 2 Behavior
	- 2.1 Damage
	- 2.2 Despawning
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Entity data
- 5 History
- 6 Trivia
- 7 Gallery
- 8 See also
- 9 References

## Appearance
3D dropped items, both blocks and strict items.
Items have two possible appearances, generally corresponding to whether the item appears as a 3D or 2D shape in a player's inventory screens. 3D items appear as their 3D shape, miniaturized to about 1⁄4 scale, while 2D items appear as 1⁄2 scale with all the pixels extruded into a cube. Both types slowly rotate and bob up and down; this is merely a visual effect, the item itself does not actually rotate or bob up and down.

Item entities that represent a stack of more than one item appear as several items stuck together. Stacks of 1 appear as one item, 2-16 as two items, 17–32 as three, 33-48 as four, and 49+ as five.

The rotation rate of the item is approximately 2.87675 degrees per tick, or 57.595 degrees per second.

## Behavior
Item entities come from many sources. Some common ones are:

- The death of amoborplayer.
- Ablockthat is mined by a player, destroyed by anexplosion, or washed away bywater.
- An inventory item tossed by pressing the drop item key (defaultQon PC,on Xbox,/on Nintendo Switch,on PlayStation) or dragging a stack outside of an inventory window.
	- In the mobile versions ofBedrock Edition, items in the hotbar can be dropped by pressing on the item's slot. The entire stack is dropped.
- A container (other than anender chestor ashulker box) that is destroyed while holding items inside.

The player may be thought of as having an "item pickup" box that surrounds their hitbox. This pickup box extends 1 additional block to the horizontal sides, and 0.5 additional blocks up and down. Any item whose hitbox intersects with the pickup box can be picked up. The pickup box is inclusive on the horizontal sides (for distance less than or equal to 1), and exclusive on the vertical sides (distance less than 0.5). When the player's hitbox size changes, such as when crouching or sleeping, the pickup box size changes with it.

Once an item entity's hitbox overlaps with the player's pickup box, it can transfer its items. As many items as can fit in the player inventory, excluding the armor slots and the off-hand slot, are transferred. If any item is transferred, a "plopping" sound is played. If all items are transferred, the items appear to move into the center of the player. The item entity never physically moves, however, which means it can appear to go through lava and blocks in its path. This can happen through blocks that are thinner than a full block, but also through the shared edge of two full blocks. Unlike experience orbs, multiple item entities can be picked up simultaneously. Dropped items have a delay of 10 ticks (half a second) between appearing and being able to be picked up, or 40 ticks (2 seconds) if thrown by a player, dolphin, or fox.

When two stackable items of the same type come within 3/4 of a block of each other, they merge into a single stack if the resulting stack size does not exceed that item's maximum stack size.

Items do not collide with other entities (except boats) and are only moved or stopped by blocks.

Like other entities, items can be pushed by flowing water and bubble columns, pushed by a piston, launched by a moving slime block, stuck to a honey block, or caught in a cobweb. Items move at faster speeds if ice is placed under the flowing water. When in still water, items float slowly up to the surface.

In Java Edition, items can be reared by fishing rods, costing 3 durability.

If an item is within a solid block, then it flies out one of the unobstructed sides, or out of the top of the block if surrounded by solid blocks on all sides. It does this even if the space below is unoccupied; therefore, it is possible to recover an item dropped by breaking a hole in a floor by quickly placing another block there.

Items visually disappear when the player is about 16 blocks away from them, and reappear when they get closer. In Java Edition, this distance can be adjusted by the "Entity Distance" slider in video settings.

Unlike most entities, items cannot be spectated in Spectator mode without use of the /spectate command.

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
