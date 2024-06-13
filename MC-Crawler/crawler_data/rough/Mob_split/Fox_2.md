### Trust
A trusting fox attacking the player
Breeding two adults with sweet berries or glow berries produces a kit that trusts the player. The baby fox trusts the player that bred it and does not flee from that player as it grows up; however, because baby foxes also follow nearby adult foxes, an adult running away from the player may cause the baby to do the same. 

Naturally spawned kits do not trust players. Foxes attack specific mobs that hurt a player they trust.

A lead can be useful during this time to keep the baby fox from fleeing until it has finished maturing to an adult itself, or the player can simply kill the adult foxes with a ranged weapon.

When attacking phantoms, foxes do not jump to attack.

In Bedrock Edition, foxes that trust the player attack any mob that harms their trusted player, including other players. In Java Edition, foxes attack only the sources of damage when their trusted player receives the damage from the following causes:[2]

- melee attacks from mobs except dolphins, iron golems, wolves, bees, polar bears, killer bunnies, slimes, magma cubes, hoglins or zoglins.[3]
- projectile damage from arrows, fireballs or wind charges.
- defensive damage from pufferfish.

Foxes do not retaliate against players who harm them, but they still attack players who damage players they trust.

Trusting foxes retreat from polar bears and wolves but not tamed wolves. A tamed wolf whose owner attacks a trusting fox also attacks the fox.

The player can summon a neutral fox in singleplayer with the command /execute summon fox run data modify entity @s Trusted append from entity @s UUID. Like other neutral mobs, foxes are passive in Peaceful difficulty.

## Data values
### ID
Java Edition:

| Name | Identifier | Entity tags                 | Translation key        |
|------|------------|-----------------------------|------------------------|
| Fox  | `fox`      | `powder_snow_walkable_mobs` | `entity.minecraft.fox` |

Bedrock Edition:

| Name | Identifier | Numeric ID | Translation key   |
|------|------------|------------|-------------------|
| Fox  | `fox`      | `121`      | `entity.fox.name` |

### Entity data
Foxes have entity data associated with them that contain various properties.

Java Edition:

Main article: Entity format
- Entity data
	- 
	- Additional fields for mobs that can breed
	- 
	- Tags common to all entities
	- 
	- Tags common to all mobs
	- Crouching: 1 or 0 (true/false) – Whether the fox is crouching.
	- Sitting: 1 or 0 (true/false) – Whether the fox is sitting.
	- Sleeping: 1 or 0 (true/false) – Whether the fox is sleeping.
	- Trusted: A list of players that the fox trusts. For a list with more than 2 elements, only the first and the last are considered.
		- : TheUUIDof each trusted player, stored as four ints.
	- Type: ID of the fox's type.


Fox Type
Main article: Fox/DV[edit]

Bedrock Edition:

SeeBedrock Edition level format/Entity format.

