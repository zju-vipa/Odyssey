#### Bedrock Edition
The slime chunk algorithm in Bedrock Edition is different from in Java Edition. The algorithm doesn't depend on the world seed, thus the chunks that slimes can naturally spawn in inhabit the same coordinates for every world.[2]

### Trial spawners
‌In Java Edition 1.21 and Bedrock Edition 1.21.0‌[upcoming], slimes have a chance to be selected as a "melee" mob for trial spawners in trial chambers[more information needed].

### Potions
In the 24w13a snapshot, the oozing potion was added. Using the splash potion on a mob will make it spawn two slimes at death. [more information needed]

## Drops
### On death
From a single large slime, a player can expect an experience and slimeball yield of 12-28 and 0-32, respectively. However, average loot yield from a single large slime is usually around 19 experience and 9 slimeballs.

#### Large slimes
- Spawns 2-4 medium slimes on death
- 4 when killed by the player

#### Medium slimes
- Spawns 2-4 small slimes on death
- 2 when killed by the player

#### Small slimes
| Item |           | Roll Chance | Quantity (Roll Chance) |           |            |             |
|------|-----------|-------------|------------------------|-----------|------------|-------------|
|      |           |             | Default                | Looting I | Looting II | Looting III |
|      | Slimeball | 100%[d 1]   | 0–2                    | 0–3       | 0–4        | 0–5         |
|      | Slimeball | 100%[d 2]   | 1                      | 1         | 1          | 1           |


↑ When not killed by a frog

↑ When killed by a frog


1 when killed by the player

## Behavior
A slime jumping.
Slimes move by hopping, which they do every 10 to 30 ticks (1⁄2 to 1 1⁄2 seconds), and can swim in water and climb ladders and scaffolding. Unlike other mobs, slimes continue moving when no players are nearby. Their exact routine is as follows:

The slime searches for a player (or, failing that, an iron golem) within 16 blocks (spherical) distance.

- If no target is found, the slime waits 10 to 30 ticks (1⁄2to 11⁄2seconds) between jumps, and changes direction randomly every 40 to 100 ticks (2 to 5 seconds).
- If a target is found, the delay before jumping is1⁄3as long (3 to 10 ticks), and the slime's direction is set directly toward the target before jumping.

Unlike most mobs, slimes do not pathfind toward their target, always approaching their target in a straight line, without avoiding environmental hazards such as lava, cactus or dangerous falls. This means they can easily get stuck in corners or behind walls, not knowing how to circumvent them. This behavior is shared by magma cubes.

A slime's maximum health is equal to its size squared, and its dimensions are 0.51 blocks times its size in each dimension. When a slime attacks, it deals damage equal to its size, except for size 0 (smallest) slimes, which do no damage, and do not prevent sleeping. Because small slimes still have a hostile AI, they continuously attack the player.

A slime's jump distance also depends on its size; a slime jumps a distance slightly farther than its length. When landing, a number (8 times the slime's size) of slime particles appear. Regardless of size, slimes always jump 1 block high.

When a slime larger than 0 dies, it spawns 2-4 new slimes equivalent to its size divided by 2, rounding down. A slime that was named with a name tag produces smaller slimes with the same name when it dies.

Slimes continuously damage all players, snow golems‌[Bedrock Edition  only] and iron golems they collide with (although damage immunity reduces the actual damage to 1 attack every half second), unlike other mobs that damage only those targets they specifically attack.[3]

Slimes in water attempt to swim to the surface if possible. If forced to stay submerged, they eventually drown, splitting into smaller slimes that drown and finally drop slimeballs.

Slimes are immune to Oozing.‌[upcoming: JE 1.21 & BE 1.21.0]

## Data values
### ID
Java Edition:

| Name  | Identifier | Entity tags                                             | Translation key        |
|-------|------------|---------------------------------------------------------|------------------------|
| Slime | slime      | frog_foodno_anger_from_wind_chargenon_controlling_rider | entity.minecraft.slime |

Bedrock Edition:

| Name  | Identifier | Numeric ID | Translation key   |
|-------|------------|------------|-------------------|
| Slime | slime      | 37         | entity.slime.name |

### Entity data
Slimes have entity data associated with them that contains various properties.

Java Edition:

Main article: Entity format

 Entity data
Tags common to all entities
Tags common to all mobs
 Size: The size of the slime. Note that this value is zero-based, so 0 is the smallest slime, 1 is the next larger, etc. The sizes that spawn naturally are 0, 1, and 3. Values that are greater than 126 get clamped to 126.
 wasOnGround: 1 or 0 (true/false) - true if the slime is touching the ground.

Bedrock Edition:

See Bedrock Edition level format/Entity format.
## See also
- Magma Cube– A similar mob that spawns only in the Nether and drops magma cream
- Tropical Slime- A variant found inMinecraft Dungeonsand inMinecraft Earth


