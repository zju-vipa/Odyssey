# Warden
A warden is a powerful but evadable hostile mob summoned by sculk shriekers in the deep dark biome. It attacks by swinging its arms downward, dealing the highest melee damage of all mobs, or with its sonic boom attack which cannot be blocked by obstacles or armor. Wardens are completely blind and rely only on vibrations, smell, and touch to detect players and mobs to attack, and can therefore be evaded via sneaking, diversions (snowballs, arrows, etc.) and wool.

## Contents
- 1 Spawning
- 2 Drops
	- 2.1 On death
- 3 Behavior
	- 3.1 Idle
	- 3.2 Suspense
	- 3.3 Attacks
- 4 Sounds
- 5 Data values
	- 5.1 ID
	- 5.2 Entity data
- 6 Achievements
- 7 Advancements
- 8 Videos
	- 8.1 YouTube
	- 8.2 Other
- 9 History
- 10 Issues
- 11 Trivia
- 12 Gallery
	- 12.1 Renders
		- 12.1.1 Animations
	- 12.2 Screenshots
	- 12.3 Development media
	- 12.4 Concept artwork
	- 12.5 In other media
		- 12.5.1 Official media
		- 12.5.2 Merchandise
- 13 References
- 14 External links

## Spawning
A warden emerges from the ground after being summoned by sculk shriekers.
Wardens do not use standard mob spawning mechanics. They are instead spawned when a player in Survival or Adventure mode activates naturally generated sculk shriekers four times, if there isn't already another warden within 24 blocks. A warden spawns by emerging from the ground near the shrieker that summoned it, taking about 6.7 seconds to do so and being completely invulnerable until fully emerged. 

The warning count for sculk shriekers is specific to each player rather than each sculk shrieker. This means that the player can activate four different shriekers in different locations and a warden emerges after the fourth activation. The light level does not have an effect on warden spawning.

Up to 20 attempts are made to spawn a warden within an 11×13×11 cubic area, which is centered on the shrieker. During each attempt, the game picks a random column from the y axis, then the game picks the topmost block in that column with a top surface with full collision and the block above must have no collision (the spawning warden cannot collide with any existing entities or liquids; wardens must not have water inside their spawn block, where their feet go, but they can spawn with water in the second and third block. For example, a pressure plate with water flowing on top is still a valid location).

In Java Edition, warden spawning can be toggled on or off with the game rule doWardenSpawning.

## Drops
### On death
| Item |                | Roll Chance | Quantity (Roll Chance) |           |            |             |
|------|----------------|-------------|------------------------|-----------|------------|-------------|
|      |                |             | Default                | Looting I | Looting II | Looting III |
|      | Sculk Catalyst | 100%        | 1                      | 1         | 1          | 1           |

- 5experienceif killed by either a player or a tamedwolf.

## Behavior
A warden is blind and seeks out targets by sensing vibrations and by sniffing.
After spawning, wardens wander randomly around the world and move toward nearby vibrations originating from players, mobs and non-mob sources including projectiles and minecarts. A warden also periodically sniffs the area around it, allowing it to zero in on targets even if they don't create vibrations. As wardens sniff, pick up vibrations or are touched by other players or mobs, wardens become increasingly agitated.

### Idle
A warden can fit inside any space that is 1 block wide and 3 blocks tall, allowing it to chase players and mobs through small corridors.

Wardens are immune to damage from fire or lava and do not take knockback. They pursue through blocks that are usually avoided by other mobs, including rails[1], cacti, or magma blocks.

A warden, whether angered or not, gives 12 seconds of Darkness to all players within a 20 block radius of it every 6 seconds. The souls in its chest make a low heartbeat that occurs in tandem with the Darkness effect. The heartbeat speeds up as the warden becomes increasingly agitated.[2] A warden prefers to track down the most suspicious targets, rather than the ones closest to it.[3]

A warden listens to all vibrations within a 16 block radius, except those from other wardens, armor stands, dying mobs and players in Creative or Spectator mode. Like with sculk sensors, they cannot detect vibrations from a sneaking player that is moving, jumping, falling or shooting a projectile. A warden has a 2-second cooldown between detecting vibrations.

A warden is aware of all targetable entities within a 49×51×49 box around itself. If the warden has a targetable entity, is not investigating any disturbances, and is otherwise idle, it pathfinds toward the closest entity, prioritizing players over mobs. While pathfinding, the warden can begin a 'sniff' behavior and animation. This takes around 4.2 seconds and has a 5-10 seconds cooldown. A warden can still sniff out sneaking players, despite not being able to detect vibrations from them.

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
