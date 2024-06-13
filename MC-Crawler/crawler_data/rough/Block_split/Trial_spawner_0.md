# Trial Spawner
A trial spawner is a type of spawner found only within trial chambers. It spawns mobs in waves, which increase in number the more Survival/Adventure mode players are nearby. When all of its spawned mobs are defeated, it ejects a combination of consumable items and/or trial keys, then goes inactive for 30 minutes. It cannot be obtained as an item or moved by a piston. A trial spawner converts into an ominous trial spawner during an ominous trial.

## Contents
- 1 Obtaining
	- 1.1 Natural generation
	- 1.2 Breaking
- 2 Usage
	- 2.1 Activation
	- 2.2 Mob spawning
		- 2.2.1 Spawning values
	- 2.3 Completion
		- 2.3.1 Cooldown
	- 2.4 Custom trial spawners
	- 2.5 Loot
	- 2.6 Ominous trial
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
	- 4.3 Block data
- 5 Video
- 6 History
- 7 Issues
- 8 Trivia
- 9 Gallery
	- 9.1 Renders
	- 9.2 Development images

## Obtaining
Trial spawners cannot be obtained in Survival, even with Silk Touch, and can not be moved with a piston.

### Natural generation
Trial spawners generate naturally in every chamber and every corridor of trial chambers, except for the entrance chamber.

### Breaking
A trial spawner can be broken but it does not drop itself as an item and takes an extended duration of time to break. It can only be obtained via the Creative inventory, the /give command, or by using pick block.

Due to their high blast resistance, trial spawners are immune to explosions, but can still be destroyed by the wither's block-breaking attack and blue wither skulls.

| Block    | Trial Spawner       |
|----------|---------------------|
| Hardness | 50                  |
|          | Breakingtime (secs) |
| Default  | 250                 |

## Usage
A trial spawner summons a limited number of mobs, scaled based on the number of nearby players. When these mobs are defeated, the spawner drops a reward for each player and enters a cooldown period.

### Activation
The trial spawner has a required player range of 14 blocks. Any player in Survival or Adventure mode activates the spawner if the distance between the player's center and the spawner's center becomes less than the required player range. Once activated, the spawner begins summoning copies of the mob set in it.

Trial spawners do not activate in Peaceful difficulty, or if the gamerule doMobSpawning is false, even if set to an entity capable of spawning in Peaceful.

When a trial spawner first activates, it shoots spark-like particles up into the air. While active, it emits smoke and flame particles around itself and any entities it summons.

The light level around a trial spawner does not affect how it summons entities.

### Mob spawning
A breeze and two skeletons spawning from a trial spawner.
See also: Trial Chambers § Trial spawners

When a player enters the trial spawner's range, the spawner attempts to spawn 1 mob every 40 game ticks (2 seconds). With 1 player, it does not spawn a mob if there are already 2 mobs from the spawner that are still alive. It will spawn a total of 6 mobs before ejecting loot and going into cooldown. The number of living mobs required to prevent further mob spawning is called the simultaneous mob count. The number of mobs spawned before going into cooldown is the total mob count. These numbers are summarized in § Spawning values.

This duration of time between each mob being spawned is the spawn interval. If the spawner can't spawn a mob, it waits for the duration of the spawn interval and tries again. Once the number of living mobs spawned by the spawner has reached the simultaneous mob count, it stops trying to spawn mobs. Mobs spawned by the spawner do not naturally despawn, but the spawner does not detect or count living mobs from unloaded chunks. Therefore, moving mobs into unloaded chunks causes them to build up and the spawner to continue spawning more. 

A trial spawner also stops spawning mobs if the number of living mobs spawned by it reached the total mob count. The spawner doesn't need to detect these mobs being alive, and therefore still counts them if they are in unloaded chunks. The spawner detects the death of the mobs only for the total mob count, and it always detects the death of the mobs even if it is not in a loaded chunk.

Both the simultaneous mob count and the total mob count increase if another player comes within the spawner's range. For each additional player present, the simultaneous mob count increases by 1, and the total mob count increases by 2. For example, with 2 players, 8 mobs spawn in total with 3 at once, and with 3 players, 10 mobs spawn in total with 4 at once.

If a player leaves the detection range of a trial spawner, these values do not scale back down.

The values described above are the default values used when trial spawners are placed manually. Naturally generated spawners in trial chambers use different values. Additionally, these numbers can be configured by modifying the block's NBT data.

Naturally generating trial spawners in trial chambers use different values for the spawn interval, the total mob count, and the simultaneous mob count. The quantity that the last 2 values change by with additional players is also different for different types of spawners. All naturally generated spawners attempt to spawn mobs every 20 game ticks (1 second), or every 160 game ticks (8 seconds) for the slow versions of the spawners. Additionally, naturally generated breeze spawners allow 1 breeze to exist at once (+0.5 for each additional player present) and stop after spawning 2 mobs (+1 for each additional player present). Baby zombie spawners allow 2 baby zombies to exist at once (+0.5 for each additional player present) and stop after spawning 6 mobs (+2 for each additional player present). All other spawners generated in trial chambers use the default value of 6 total mobs, plus 2 for each additional player present, and 3 simultaneous mobs, plus 2 for each additional player present. This is summarized in § Spawning values.

