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

