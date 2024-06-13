# Slime
Slimes are bouncy, cube-shaped hostile mobs that spawn deep underground in particular chunks, or on the surface in swamp biomes. They attack by jumping at their targets, come in three sizes, and larger slimes can split into smaller ones on death.

## Contents
- 1 Spawning
	- 1.1 Swamps
	- 1.2 Slime chunks
		- 1.2.1 Java Edition
		- 1.2.2 Bedrock Edition
	- 1.3 Trial spawners
	- 1.4 Potions
- 2 Drops
	- 2.1 On death
		- 2.1.1 Large slimes
		- 2.1.2 Medium slimes
		- 2.1.3 Small slimes
- 3 Behavior
- 4 Sounds
- 5 Data values
	- 5.1 ID
	- 5.2 Entity data
- 6 Achievements
- 7 Advancements
- 8 Video
- 9 History
- 10 Issues
- 11 Trivia
- 12 Gallery
	- 12.1 Screenshots
	- 12.2 In other media
- 13 See also
- 14 References

## Spawning
See also: Tutorials/Slime farming

Slimes spawn in 3 sizes: small, medium, and big. Slimes have an NBT tag,  Size, which determines their size. Small medium and big slimes have their Size set to 0, 1, and 3 respectively. Using the /summon or /data commands, a slime can be given any Size in the range from 0 to 126 (inclusive).[verify]

A slime needs a space of 2.04×2.04×2.04 blocks to spawn, which must be clear of solid and liquid obstructions. When a slime attempts to spawn, the game checks for the space requirement. Therefore, small and medium slimes are not able to spawn in 2-block tall areas, even though it would normally be enough room other small mobs. Any block within the space, even a glass pane, can prevent slimes from spawning.

- Abuttonor any block without a collision hitbox can prevent a mob from spawning on the block below it, but doesn't count as an obstruction. This is because the game looks for a block with anairblock above it when trying to spawn a mob.
- InJava Editionthe space is centered on the top face of the block the slime spawns on.
	- The game doesn't have any blocks a hitbox that is contained in the 0.46-block wide region touching any of the 4 horizontal faces of the block. It should be noted that atrapdooris treated like a full-block when the game looks for space to spawn mobs. Therefore, the effective spawning space a slime needs is 3×2.1×3 blocks.
- InBedrock Edition, the space is centered in the northwest corner of a block. This means the effective spawning region is 2×2×2 blocks.[verify]

The random distribution of slime sizes is affected by regional difficulty: chances range from 33% for each size at the low difficulty to 16% small, 33% medium, and 50% big with higher difficulty.

### Swamps
Slimes can spawn in swamps and mangrove swamps, between the altitudes of Y=51 and Y=69 (inclusive) when the provided light level is 7 or less. They spawn most often on a full moon, and never on a new moon.

More precisely, the game checks two factors:

1. If the light level is equal to or less than a random integer (from 0 to 7)
2. If the fraction of the moon that is bright is greater than a random number (from 0 to 1)

If these conditions are met and the altitude is acceptable, there is a 50% chance of spawning a slime.

The light level requirement for slime spawning in swamps is different from that of most hostile mobs, which spawn only at light level 0.[1] This allows slimes in swamps to spawn in dimly-lit areas where most hostile mobs cannot, allowing swamp-based slime farms to be built.

### Slime chunks


Slimes spawn in the Overworld in slime chunks below the layer of Y=40, regardless of the lighting or weather conditions.

About 1⁄10 of all chunks are generated as slime chunks, but they are not determined randomly. An algorithm is used to determine whether each chunk is a slime chunk.

#### Java Edition
In Java Edition, slime chunks are determined pseudo-randomly by combining their chunk coordinates with the seed of the world.

This Java code can be used to print a message to the terminal indicating whether one specific chunk is a slime chunk.[verify]

import java.util.Random; 

public class CheckSlimechunk {
    
    public static void main(String args[])
    {
        // the seed from /seed as a 64bit long literal
        long seed = 12345L;
        int xPosition = 123;
        int zPosition = 456;
        
        Random rnd = new Random(
                seed +
                (int) (xPosition * xPosition * 0x4c1906) +
                (int) (xPosition * 0x5ac0db) +
                (int) (zPosition * zPosition) * 0x4307a7L +
                (int) (zPosition * 0x5f24f) ^ 0x3ad8025fL
        );
        
        System.out.println(rnd.nextInt(10) == 0);
    } 
}

The game combines the chunk coordinates and the world seed to make a specific RNG seed to generate a random integer between 0 and 9 (inclusive). If the random integer is 0, then the chunk is a slime chunk. World coordinates can be converted to chunk coordinates by dividing by 16 and then rounding down. The world coordinates and the chunk coordinates are both 32-bit integers (instances of int).

#### Bedrock Edition
The slime chunk algorithm in Bedrock Edition is different from in Java Edition. The algorithm doesn't depend on the world seed, thus the chunks that slimes can naturally spawn in inhabit the same coordinates for every world.[2]

### Trial spawners
‌In Java Edition 1.21 and Bedrock Edition 1.21.0‌[upcoming], slimes have a chance to be selected as a "melee" mob for trial spawners in trial chambers[more information needed].

### Potions
In the 24w13a snapshot, the oozing potion was added. Using the splash potion on a mob makes it spawn two slimes upon death. [more information needed]

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

1. ↑When not killed by a frog
2. ↑When killed by a frog

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

| Name  | Identifier | Entity tags                                                             | Translation key          |
|-------|------------|-------------------------------------------------------------------------|--------------------------|
| Slime | `slime`    | `frog_food`<br/>`no_anger_from_wind_charge`<br/>`non_controlling_rider` | `entity.minecraft.slime` |

Bedrock Edition:

| Name  | Identifier | Numeric ID | Translation key     |
|-------|------------|------------|---------------------|
| Slime | `slime`    | `37`       | `entity.slime.name` |

### Entity data
Slimes have entity data associated with them that contains various properties.

Java Edition:

Main article: Entity format
- Entity data
	- 
	- Tags common to all entities
	- 
	- Tags common to all mobs
	- Size: The size of the slime. Note that this value is zero-based, so 0 is the smallest slime, 1 is the next larger, etc. The sizes that spawn naturally are 0, 1, and 3. Values that are greater than 126 get clamped to 126.
	- wasOnGround: 1 or 0 (true/false) - true if the slime is touching the ground.

Bedrock Edition:

SeeBedrock Edition level format/Entity format.
