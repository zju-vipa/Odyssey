# Monster Spawner
A monster spawner is a type of spawner found in a variety of structures. It contains a miniature mob, and constantly spawns instances of that mob as long as a player is nearby and, if applicable for the mob it spawns, if there are valid dark areas nearby. It cannot be obtained as an item in survival mode or moved by a piston, and it only drops experience orbs when broken.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
- 2 Usage
	- 2.1 Mechanics
		- 2.1.1 Spawning requirements
	- 2.2 Disabling
	- 2.3 Custom monster spawners
	- 2.4 Note blocks
	- 2.5 Piston interactivity
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block data
- 5 Video
- 6 History
- 7 Issues
- 8 Trivia
- 9 Gallery
	- 9.1 Renders
		- 9.1.1 Spawner
		- 9.1.2 Structure
	- 9.2 Screenshots
- 10 See also
- 11 Notes
- 12 References
- 13 External links

## Obtaining
Monster spawners cannot be obtained in Survival, even with Silk Touch.

A monster spawner can be obtained in Creative mode by taking it from Creative inventory, by using the /give command, or by using pick block. It is initially empty and inert, but can be configured to spawn a desired mob by using a spawn egg on the placed block.

A /setblock, /clone or /fill command can also be used to obtain a monster spawner.

### Breaking
If broken with a pickaxe, a monster spawner drops 15-43 experience. When mined with anything else, it drops nothing.

| Block     | Monster Spawner       |
|-----------|-----------------------|
| Hardness  | 5                     |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 25                    |
| Wooden    | 3.75                  |
| Stone     | 1.9                   |
| Iron      | 1.25                  |
| Diamond   | 0.95                  |
| Netherite | 0.85                  |
| Golden    | 0.65                  |


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


### Natural generation
Monster spawners can generate naturally in the following places:

Monster room
One in the center of the monster room spawning one of the following mobs with the indicated frequency: zombie (50%), skeleton (25%), or spider (25%).
Mineshaft
Any number of cave spider monster spawners, densely surrounded by cobwebs, scattered throughout.
Woodland Mansions
Optionally one spider monster spawner, densely surrounded by cobwebs, in a rarely generated secret room on the 2nd or 3rd floor. It is sometimes visible through the windows from outside.
Stronghold
One silverfish monster spawner in the end portal room.
Nether fortress
One or two blaze monster spawners on fenced platforms with full-block "stairs" leading up to them. Normally two are generated per fortress, but there can be fewer.
Bastion remnant
One magma cube monster spawner hanging from a chain underneath a bridge in treasure rooms.
## Usage
The monster spawner spawns mobs in an (at most) 9×3×9 volume (see § Mechanics) around it when the player is within 16 blocks. Suitable spawning locations for the block's mob type are provided in or around the spawning volume. The monster spawner attempts to spawn four mobs around it, then waits from 10 to 39.95 seconds before attempting to spawn more.

In Peaceful difficulty, monster spawners still activate but do not spawn monsters in Bedrock Edition. In Java Edition, zombified piglins, magma cubes, and ghasts do not spawn at all and other hostile mobs disappear immediately after spawning.

Monster spawners are transparent, but they behave like leaves in that they diffuse sky light coming from directly above. 

In Bedrock Edition, they have a hitbox slightly smaller than a full block, and therefore, one can walk on the edge of a supporting full block directly below the monster spawner.

### Mechanics
A monster spawner activates when a player (that's not in Spectator mode) comes within a spherical radius of 16 blocks from the center point of the block; i.e. 15.5 blocks from the monster spawner itself. The player's presence is determined by coordinates at their foot level, meaning that a player standing exactly 15.5 blocks below the spawner won't activate it, even though their head is in range. In Java Edition an active monster spawner attempts to spawn mobs within a 4-block horizontal and 1-block vertical range; that is, in a 9×3×9 volume centered on the monster spawner. In Bedrock Edition, the horizontal spawning range is 4 blocks taxicab distance, creating spawning volume extending 4 blocks in each cardinal horizontal direction from the sides of the monster spawner; its horizontal cross-section is therefore diamond-shaped. Mobs can spawn anywhere in this range that is suitable, with mobs more likely to spawn closer to the monster spawner than farther away.

While mobs are spawned at fractional x and z-coordinates (i.e. not aligned to blocks), they are spawned at an integer y-coordinate. Horizontally, a mob can spawn with its center point anywhere within range, but vertically, mobs spawn with their legs at either the same layer as the monster spawner block, one block above it, or one block below it.  (Note that when there are other blocks slightly intersecting the mob's hitbox, they can sometimes glitch further away - often up - but this does not make it a true spawning point.)

The monster spawner attempts to spawn 4 mobs at randomly chosen points within the spawning volume, then waits anywhere from 200 to 799 ticks (10 to 39.95 seconds) before spawning again. As it waits, the mob model inside the block spins faster and faster. Except for the normal solid-block spawning requirement, all the remaining ones must be met (not in a solid block, correct light level, etc.), so the monster spawner often produces fewer than 4 mobs. When it does spawn, it emits a "poof", and more flame particles temporarily appear around it. If the monster spawner fails to spawn any mobs because it did not pick any suitable locations, it repeats this process every tick until it succeeds. It only starts the next wait cycle after successfully spawning at least one mob.

If 6 or more mobs of the monster spawner's type have their hitbox intersecting a 9×9×9 volume centered on the monster spawner block in Java Edition or a 16×10×16 volume centered on the lower northwest corner of the monster spawner block in Bedrock Edition, the monster spawner "poofs" without creating any mobs and then waits for the next cycle. [needs testing in Bedrock Edition] This is checked before each of the four spawn attempts.

