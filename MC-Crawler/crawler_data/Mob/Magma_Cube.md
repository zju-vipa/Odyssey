# Magma Cube
A magma cube is a hostile mob found in the Nether. A magma cube behaves similarly to a slime, but is fireproof, jumps higher and less often, and deals more damage.

## Contents
- 1 Spawning
	- 1.1 Nether Wastes
	- 1.2 Nether Fortresses
	- 1.3 Basalt Deltas
	- 1.4 Spawners
- 2 Drops
	- 2.1 On death
- 3 Behavior
	- 3.1 Combat
- 4 Sounds
- 5 Data values
	- 5.1 ID
	- 5.2 Entity data
- 6 Achievements
- 7 Advancements
- 8 History
- 9 Issues
- 10 Trivia
- 11 Gallery
	- 11.1 Screenshots
	- 11.2 In other media
- 12 References
- 13 External links

## Spawning
See also: Spawn § Spawn cycle

Magma cubes spawn in areas of the Nether at all light levels. The space they spawn in must be clear of solid obstructions and liquids. Due to being inherently fireproof, magma cubes can spawn on magma blocks. 

Only sizes 1, 2 and 4 (NBT Size tag values 0, 1 and 3 respectively) spawn naturally. With use of /summon, magma cubes can potentially range from size 1 to 127 (NBT Size tag 0–126).[verify]

This large magma cube attempts to spawn on the basalt, but because there is a piece of iron bar intersecting its hitbox, it is unable to spawn. This check is performed before the size of the magma cube is determined, meaning no magma cubes can spawn at that location.
A magma cube needs roughly a 3×2.1×3 free space to spawn. The area in which they spawn must be clear of solid or liquid obstructions. When a magma cube attempts to spawn, the game checks for the space requirement of a large magma cube, and the size is determined later. Therefore, since large magma cubes are slightly taller than 2 blocks, no magma cubes, regardless of size, are able to spawn at all in 2-block-high areas. Also, since large magma cubes are slightly wider than 2 blocks, and mobs spawn at the center of a block, having any block within the 3×2.1×3 area, even as thin as a glass pane, can prevent a magma cube of any size from spawning.

Magma cubes' size is affected by regional difficulty: chances range from 33% for each size at the low difficulty to 16% small, 33% medium, and 50% big with higher difficulty.

### Nether Wastes
Magma cubes spawn uncommonly in Nether wastes in groups of 1 to 4.

### Nether Fortresses
Magma cubes spawn commonly in Nether fortresses in groups of 4.

### Basalt Deltas
Magma cubes spawn commonly in basalt deltas, in groups of 2 to 5.

### Spawners
Magma cube monster spawners generate in the treasure room of bastions.

## Drops
### On death
| Item |                       | Roll Chance | Quantity (Roll Chance) |           |            |              |
|------|-----------------------|-------------|------------------------|-----------|------------|--------------|
|      |                       |             | Default                | Looting I | Looting II | Looting III  |
|      | Magma Cream           | 1[d 1]      | 1 (25%)                | 1–2 (40%) | 1–3 (50%)  | 1–4 (57.14%) |
|      | Pearlescent Froglight | 100%[d 2]   | 1                      | 1         | 1          | 1            |
|      | Verdant Froglight     | 100%[d 3]   | 1                      | 1         | 1          | 1            |
|      | Ochre Froglight       | 100%[d 4]   | 1                      | 1         | 1          | 1            |


↑ From large and medium magma cubes only.

↑ From small magma cubes only when killed by a warm frog.

↑ From small magma cubes only when killed by a cold frog

↑ From small magma cubes only when killed by a temperate frog


- Large magma cube:4 experience and 2-4 medium magma cubes
- Medium magma cube:2 experience and 2-4 small magma cubes
- Small magma cube:1 experience

## Behavior
Magma cube jumping.
A magma cube seeks out any player or an iron golem within a spherical distance of 16 blocks. If it finds no enemy, it changes direction every 40 to 100 ticks (2 to 5 seconds) and jumps forward every 40 to 120 ticks (2 to 6 seconds). If it finds a target, the delay before jumping is 1⁄3 as long (13 to 40 ticks), and the magma cube changes direction directly toward the target before jumping.

Magma cubes cannot be hurt by fall damage or burning, and are not slowed down by lava. They can swim upward in lava and leap above its surface. 

Their jump height depends on their size (6 high for large). Their forward speed is twice that of most other mobs. They always make a distinct sound upon jumping up and landing, but no idle sounds.

When a magma cube is killed, it splits into 2-4 smaller magma cubes. Tiny magma cubes disappear when killed, like other mobs.

They can swim in water and attempt to stay on the surface. Like slimes, magma cubes starts taking drowning damage if submerged in water for 15 seconds, splitting into smaller cubes if possible.

Magma cubes take extra damage from powder snow, taking 5 every two seconds, unlike 1 for other mobs.

Unlike most mobs, magma cubes have no pathfinding ability, meaning that they do not avoid falling off cliffs and cannot go around walls, even when chasing a player. This behavior is shared by slimes.

When they are in lava, they hover and try to move to nearby land.

### Combat
See also: Tutorials/Combat § Magma Cubes

Magma cubes attack by jumping and attempting to land on the player, and cause damage when touched anywhere. As their jump rate is random, magma cubes can be hard to fight.

The health of a magma cube is its size squared; the attack strength is its size + 2, and the armor points are its size tripled.

A magma cube jumps a distance of approximately its length times 1.5 and a height equivalent to its size in blocks. This means that a large magma cube jumps 4 blocks in height and moves significantly quicker than a small magma cube, which jumps 2 blocks in height; while a tiny magma cube moves slowly and jumps 1 block in height.

Magma cubes continuously damage all players and iron golems‌[JE  only] they collide with (although damage immunity reduces the actual damage to 1 attack every half second), unlike other mobs that damage only those targets they specifically attack.[1] This means that a large magma cube deals 12 × 6 of damage per second on normal difficulty. Unlike slimes, tiny magma cubes can deal damage to the player.

## Data values
### ID
Java Edition:

| Name       | Identifier | Entity tags                                                              | Translation key             |
|------------|------------|--------------------------------------------------------------------------|-----------------------------|
| Magma Cube | magma_cube | fall_damage_immunefreeze_hurts_extra_typesfrog_foodnon_controlling_rider | entity.minecraft.magma_cube |

Bedrock Edition:

| Name       | Identifier | Numeric ID | Translation key        |
|------------|------------|------------|------------------------|
| Magma Cube | magma_cube | 42         | entity.magma_cube.name |

### Entity data
Magma cubes have entity data associated with them that contains various properties.

Java Edition:

Main article: Entity format

 Entity data
Tags common to all entities
Tags common to all mobs
 Size: The size of the magma cube. Note that this value is zero-based, so 0 is the smallest magma cube, 1 is the next larger, etc. The sizes that spawn naturally are 0, 1, and 3.
 wasOnGround: 1 or 0 (true/false) - true if the magma cube is touching the ground.

Bedrock Edition:

See Bedrock Edition level format/Entity format.
