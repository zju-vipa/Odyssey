### Suspense
Wardens keep track of how angry they are at each suspect as a number from 0 to 150. When a warden notices a vibration, it adds anger to the player or mob that caused the vibration. It adds 10 anger if the vibration was from a projectile or 35 anger for other vibrations. However, if two projectiles from the same player/mob are heard by the warden within five seconds, it instead adds the full 35 anger toward that player/mob. Wardens do not add anger toward a mob/player if the projectile was shot from more than 30 blocks away, although the projectile does count toward the counter of two projectiles. Anger decays at a rate of 1 per second and immediately clears if the targeted player switches to Creative or Spectator modes, the target or warden leaves the dimension, or if the target dies.

A warden adds 35 anger toward any mob that directly touches it. This effect has a 1-second cooldown.

When it finishes sniffing, a warden adds 35 anger to the nearest mob or player within 6 blocks horizontally and 20 blocks vertically, a cylindrical volume centered on the warden.

Once a warden reaches 80 anger with a target, it roars for 4.2 seconds, adds another 20 anger, and pursues the target. In this angered state, the warden chases the target normally despite being blind. A warden also enters its hostile state and adds 100 anger if directly attacked by a mob. If the attacking player or mob is within 5 blocks, it skips its roaring animation altogether and immediately gives chase.

A warden is biased toward player vibrations, attacks, and contact - even if a warden is angrier at another mob, it still attacks the player first as long as they have angered the warden as well. This is not true of any other mob.[4]

After 60 seconds of being "calm" and not detecting any vibrations or sniffing any mobs, a warden burrows back into the ground and despawns. If the warden is floating on a liquid, it instead immediately despawns without any burrowing animation. During its emerging/burrowing animation, a warden cannot detect any vibrations, and can take damage only from /kill, though it can still be pushed by entities, pistons, or liquids. Named wardens do not dig or despawn.

### Attacks
A warden's melee attack has a cooldown of 0.9 seconds and disables shields for 5 seconds, dealing 16 × 8 to 45 × 22.5 health points depending on the difficulty.

The warden's sonic boom attack on a chicken
If a warden cannot reach its target, it switches to its ranged attack: a sonic boom. It does so when the following are true:

- It has been 10 seconds since the warden detected the target
- It has been 5 seconds since the warden last used a melee or ranged attack
- The target is within 15 blocks horizontally and 20 blocks vertically of the warden.

The sonic boom aims directly at the target, making it impossible to dodge, passing through blocks and other mobs without damaging them. A warden takes 1.7 seconds to charge and unleashes the attack, which instantly hits the target as long as the target is within attack range. The attack takes an additional 1.3 seconds to cool down before the warden can use melee attacks again for a total of 3 seconds. The sonic boom is visible via green-blue particles that are projected out of the warden's chest. This attack bypasses armor, breeze armor, enchantments, horse armor, shields, shulker shells, wither armor, and wolf armor without making them lose durability. Only the Resistance status effect can reduce this attack's damage.


## Data values
### ID
Java Edition:

| Name   | Identifier | Translation key           |
|--------|------------|---------------------------|
| Warden | `warden`   | `entity.minecraft.warden` |

Bedrock Edition:

| Name   | Identifier | Numeric ID | Translation key      |
|--------|------------|------------|----------------------|
| Warden | `warden`   | `131`      | `entity.warden.name` |

### Entity data
Wardens have entity data associated with them that contains various properties.

Java Edition:

Main article: Entity format
- Entity data
	- 
	- Tags common to all entities
	- 
	- Tags common to all mobs
	- anger: Anger management of the warden.
		- suspects: List of suspects that have angered the warden.
			- A suspect.
				- angerThe level of anger. It has a maximum value of 150 and decreases by 1 every second.
				- uuid: TheUUIDof the entity that is associated with the anger, stored as four ints.

Bedrock Edition:

SeeBedrock Edition level format/Entity format.

