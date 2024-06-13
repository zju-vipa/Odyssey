# Falling Block
A falling block is the entity form of a block that appears when a gravity-affected block loses its support.

## Contents
- 1 Spawning
- 2 Behavior
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Entity data
- 5 History
- 6 See also
- 7 References

## Spawning
Falling blocks naturally spawn where gravity-affected blocks lose their base of support. These blocks include:

- Anvil
- Concrete Powder
- Dragon Egg
- Gravel
- Pointed Dripstone
- Red Sand
- Sand
- Scaffolding
- Snow layer‌[Bedrock Edition  only]
- Suspicious Sand
- Suspicious Gravel
- Any other block by using cheats. Falling block entities can be spawned through/summon. By tweaking theBlockStateNBT tag, it is possible to summon any block as a falling block entity.

Although it has the same appearance as its corresponding block and is also affected by gravity, a primed TNT is a different kind of entity.

## Behavior
A falling block continues falling until it lands on another block with a solid top surface. If it lands with the bottom center of its hitbox in a replaceable block (grass, water, vines, air, etc.), and the block below can support it (i.e. not a replaceable block), then the falling block returns to its block state. Otherwise, it breaks and drops as an item.

Like most other entities, falling blocks are affected by explosions and bubble columns, can be launched by a moving slime block, can be pushed by pistons, can be slowed down by cobwebs, and can slide down the side of a honey block. However, they do not bounce on a stationary slime block and can neither be pushed nor slowed down by water or lava.

Falling blocks pass through most entities without colliding with them, although projectiles such as arrows bounce off them. They do not have health, cannot be attacked and do not take damage. They are also immune to all status effects.

By default, a falling block that has existed for more than 600 ticks (30 seconds) destroys itself and drops as an item. This can be changed by modifying the entity's Time NBT value. Suspicious sand and suspicious gravel also drop themselves after falling for more than 30 seconds,[1] making this the only way to obtain suspicious blocks in Survival.

Commands such as /data‌[Java Edition  only] can change the moving and facing directions of a falling block, although there are no in-game mechanics that can alter a falling block's facing direction. They can be removed with the /kill command.

Some falling blocks, like anvils and pointed dripstone, deal damage to players and mobs in the same block space where they land. The damage is dealt only on landing, and is not dealt to players and mobs that collide with them in mid-air. A falling block that deals damage can be summoned if its HurtEntities tag is set to true. The amount of damage dealt per block fallen can be customized via the FallHurtAmount tag, and the maximum damage dealt can be customized via the FallHurtMax tag.

## Data values
### ID
Java Edition:

| Name          | Identifier      | Translation key                  |
|---------------|-----------------|----------------------------------|
| Falling Block | `falling_block` | `entity.minecraft.falling_block` |

Bedrock Edition:

| Name          | Identifier      | Numeric ID | Translation key             |
|---------------|-----------------|------------|-----------------------------|
| Falling Block | `falling_block` | `66`       | `entity.falling_block.name` |

### Entity data
Java Edition:

Main article: Entity format
- Dynamic block entity data
	- 
		- 
		- Tags common to all entities
	- BlockState: The falling block represented by this entity.
		- Name: Theresource locationof the block.
		- Properties: Optional. Theblock statesof the block.
			- Name: The block state name and its value.
	- CancelDrop: 1 or 0 (true/false) - true if the block should be destroyed instead of placed after landing on a solid block. When true, the block is not dropped as an item, even if theDropItemtag is set to true. However, if the entity is deleted due to itsTimevalue being too high, this tag is ignored and an item is dropped depending on theDropItemtag.CancelDropdefaults to 1 for fallingsuspicious sandandsuspicious gravel, and 0 for the other vanilla falling blocks and any summoned falling block.
	- DropItem: 1 or 0 (true/false) – true if the block should drop as an item when it breaks. Any block that does not have an item formwith the same ID as the blockdoes not drop even if this is set.
	- FallHurtAmount: Multiplied by theFallDistanceto calculate the amount of damage to inflict. By default this value is 2for anvils, and 6for pointed dripstone.
	- FallHurtMax: The maximum hit points of damage to inflict on entities that intersect this falling block. For vanilla falling blocks, always 40× 20.
	- HurtEntities: 1 or 0 (true/false) – true if the block should hurt entities it falls on. Defaults to 1 foranvilsandpointed dripstoneand to 0 for the other vanilla falling blocks and any summoned falling block.
	- TileEntityData: Optional. The tags of the block entity for this block.
	- Time: The number of ticks the entity has existed. WhenTimegoes above 600, or above 100 while the block is at Y=-64 or is outside building height, the entity is deleted.

Bedrock Edition:

SeeBedrock Edition level format/Entity format.

