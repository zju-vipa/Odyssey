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

