# Shulker
A shulker is a box-shaped hostile mob found in end cities. It hides in its shell to protect itself and blend in with its surroundings, and attacks by shooting homing bullets that inflict Levitation. It is the only source of shulker shells, which are used to craft shulker boxes.

## Contents
- 1 Spawning
	- 1.1 Natural generation
	- 1.2 Post-generation
- 2 Drops
	- 2.1 On death
- 3 Behavior
	- 3.1 Shulker bullet
	- 3.2 Coloring
- 4 Transportation
- 5 Sounds
	- 5.1 Shulker
	- 5.2 Shulker bullet
- 6 Data values
	- 6.1 ID
	- 6.2 Entity data
- 7 Achievements
- 8 Advancements
- 9 History
- 10 Issues
- 11 Trivia
- 12 Gallery
	- 12.1 Renders
		- 12.1.1 Open
		- 12.1.2 Closed
	- 12.2 Screenshots
	- 12.3 In other media
- 13 References
- 14 External links

## Spawning
### Natural generation
Shulkers spawn during the generation of end cities, which are located on the outer islands of the End. They usually spawn on the walls of the city and on end ships. They do not despawn naturally, even in Peaceful difficulty.

### Post-generation
There is a chance for a new shulker of the same color to spawn when a shulker is hit with a shulker bullet (including one of its own).

The following conditions need to be met:

- When the shulker gets hit and then has less than half its health remaining, there is a 25% chance for it to attempt teleportation without spawning a new shulker instead of checking the conditions below.
- The hit shulker must have its lid open.
- The hit shulker needs to find somewhere to teleport. For this, it takes a random block in a 17×17×17 cuboid centered on the shulker and then checks if the block has a valid face to teleport to. If not it proceeds to try this up to 4 more times. If no valid face is found, the attempt fails.
- Each other shulker within 8 blocks of the hit shulker decreases the odds of success by 20%. When five or more other shulkers are nearby, no shulkers spawn, but the hit shulker still teleports.

If the attempt succeeds a new shulker spawns where the old shulker was before it teleported.

## Drops
### On death
| Item |                   | Roll Chance | Quantity (Roll Chance) |            |            |             |
|------|-------------------|-------------|------------------------|------------|------------|-------------|
|      |                   |             | Default                | Looting I  | Looting II | Looting III |
|      | Shulker Shell(JE) | 50%–68.75%  | 1 (50%)                | 1 (56.25%) | 1 (62.5%)  | 1 (68.75%)  |
|      | Shulker Shell(BE) | 100%        | 0–1                    | 0–2        | 0–3        | 0–4         |

Shulkers also drop 5 when killed by a player or a tamed wolf.

## Behavior





The shell of the mob looks similar to a purpur block, blending in to its natural surroundings. Inside the shell of the mob is a small yellow head with two eyes. Spawning shulkers with other colors can be done using the /summon command, as detailed below.

Shulkers generally remain stationary, attached to an adjacent block with a full face.[1] However, if the block the shulker occupies becomes something other than air or the shulker finds itself not adjacent to any full face, or the shell cannot fully open (due to solid blocks or entities such as boats or other shulkers), it attempts to teleport (5 attempts per tick) to an air block within a 17×17×17 cube centered on the shulker where the shulker can attach to a full face and open. If it finds no valid position to teleport onto it does not move.

Shulkers evaluate the collision box of scaffolding based on their current position,[2] which can result in the shulker teleporting to a position only to find it invalid and teleport again.

Shulkers occasionally open their shell for 1–3 seconds. When a target comes within about 16 blocks, it opens fully and shoots guided projectiles that follow the shulker's target, called shulker bullets, moving only along the X, Y, or Z axes and leaving trails of white particles. The projectiles can be destroyed by attacking them or blocked with a shield. If the projectile hits an entity, it does 4 damage and inflicts the Levitation status effect for 10 seconds, this status effect has no effect underwater[3]‌[Java Edition  only], or while riding a mob. The shulker continues firing every 1–5.5 seconds while the target remains in range. If the shulker's target dies with projectiles still in flight, they fall to the ground.

Shulkers can attack each other, in which case they shoot fully guided bullets at each other, but are unaffected by Levitation when hit. The normal teleportation habits apply during these battles, and is likely to result in the duplication of more shulkers.

When its shell is closed, a shulker has 20 ( × 10) armor points and deflects arrows. When the shell opens, it loses this natural armor and takes damage as normal. When at less than half health, a shulker has a 25% chance of teleporting (as described above) after taking damage. When a shulker is attacked, other shulkers in the area target the attacker as well.

Shulkers don't take burning damage from lava or fire. They drown in water, but try to teleport away when water or lava flows into the block they occupy.

In Peaceful difficulty, shulkers exist within the world, but do not attack,[4] like piglins and hoglins in Bedrock Edition.

Shulkers are treated differently than true blocks. For example, mobs are unable to pathfind around[5] or jump over them,[6] and falling on them from a height does not produce particles.[7] Their spawn egg also does not destroy blocks such as grass.[8]

In Bedrock Edition, they apply Levitation II instead of I.

Gravity-affected blocks break when falling onto a shulker.

