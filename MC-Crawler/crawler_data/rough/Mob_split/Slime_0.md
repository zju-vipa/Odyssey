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

