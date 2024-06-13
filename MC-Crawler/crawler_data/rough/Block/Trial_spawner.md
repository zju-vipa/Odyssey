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

#### Spawning values
| Type                                                | Spawn interval             | Total mobs (base) | Total mobs added per player | Simultaneous mobs (base) | Simultaneous mobs added per player |
|-----------------------------------------------------|----------------------------|-------------------|-----------------------------|--------------------------|------------------------------------|
| Default values                                      | 40 game ticks (2 seconds)  | 6                 | 2                           | 2                        | 1                                  |
| Breeze                                              | 20 game ticks (1 second)   | 2                 | 1                           | 1                        | 0.5                                |
| Baby zombie                                         | 20 game ticks (1 second)   | Default           | Default                     | Default                  | 0.5                                |
| All others in trial chambers                        | 20 game ticks (1 second)   | Default           | Default                     | 3                        | 0.5                                |
| All others (slow versions)[more information needed] | 160 game ticks (8 seconds) | Default           | Default                     | 4                        | 2                                  |

Mobs spawn in positions that have a line of sight to the spawner, in a 4-block spherical radius. This is different from the monster spawner, which has a larger, rectangular spawning box. Otherwise, the standard mob spawning rules apply (mobs cannot collide with blocks, guardians and elder guardians spawn only in water, etc.)

### Completion
All mobs spawned by the trial spawner must be defeated before the trial spawner can drop loot. A mob is considered defeated when is either killed or transformed into another entity (excepting the transformation of creepers into charged creepers; the charged creeper must be defeated before completion of the trial spawner).

If a mob spawns more mobs upon death, only the initial mob must be defeated in order to complete the spawner (i.e. slimes and magma cubes).

#### Cooldown
Upon completion, the trial spawner enters a cooldown state for 30 minutes (36000 game ticks) before it can be activated again.

### Custom trial spawners
Using a spawn egg on a trial spawner sets the trial spawner's type to that egg's entity.

Trial spawners placed by players have the same loot data as those found in trial chambers.

### Loot
When all mobs have been killed, the spawner waits 40 ticks (2 seconds). Then, every 30 ticks (1.5 seconds), it ejects random items from the loot table. It does this for every detected player. It has a 50% chance of picking the trial key, in which case it drops for all players. The other 50% of the time it drops one of the other items for each player.
In Java Edition, each trial spawner contains 1 item stack,  with the following distribution: 

| Item                   | Stack Size  [A] | Weight   [B]    | Chance   [C] | Avg.per spawner   [D] | Avg. # spawnersto defeat   [E] |
|------------------------|-----------------|-----------------|--------------|-----------------------|--------------------------------|
| Trial Key              | 1               | $\frac{13}{26}$ | 50.0%        | 0.500                 | 2.0                            |
| Glow Berries           | 2–10            | $\frac{3}{26}$  | 11.5%        | 0.692                 | 8.7                            |
| Emerald                | 1–6             | $\frac{3}{26}$  | 11.5%        | 0.404                 | 8.7                            |
| Baked Potato           | 1–3             | $\frac{3}{26}$  | 11.5%        | 0.231                 | 8.7                            |
| Golden Carrot          | 1–3             | $\frac{1}{26}$  | 3.8%         | 0.077                 | 26.0                           |
| Ender Pearl            | 1               | $\frac{1}{26}$  | 3.8%         | 0.038                 | 26.0                           |
| Potion of Regeneration | 1               | $\frac{1}{26}$  | 3.8%         | 0.038                 | 26.0                           |
| Potion of Strength     | 1               | $\frac{1}{26}$  | 3.8%         | 0.038                 | 26.0                           |



↑ The size of stacks (or for unstackable items, number) of this item on any given roll.

↑ The weight of this item relative to other items in the pool.

↑ The odds of finding any of this item in a single chest.

↑ The number of items expected per chest, averaged over a large number of chests.

↑ The average number of chests the player should expect to search to find any of this item.



### Ominous trial
Main article: Ominous Trial Spawner
A player with Bad Omen that is within the activation range of a trial spawner is given the Trial Omen effect, starting an ominous trial. During an ominous trial, trial spawners near a player with Trial Omen are converted into ominous trial spawners. When a trial spawner becomes ominous, all of its existing mobs are despawned. If the spawner was on cooldown and was not ominous before going on cooldown, the cooldown is skipped when becoming ominous.

## Data values
### ID
Java Edition:

| Name          | Identifier      | Form         | Translation key                 |
|---------------|-----------------|--------------|---------------------------------|
| Trial Spawner | `trial_spawner` | Block & Item | `block.minecraft.trial_spawner` |

| Name         | Identifier      |
|--------------|-----------------|
| Block entity | `trial_spawner` |

Bedrock Edition:

| Name          | Identifier      | Numeric ID | Form                       | Item ID[i 1]   | Translation key           |
|---------------|-----------------|------------|----------------------------|----------------|---------------------------|
| Trial Spawner | `trial_spawner` | `-315`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.trial_spawner.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

| Name         | Savegame ID    |
|--------------|----------------|
| Block entity | `TrialSpawner` |

### Block states
See also: Block states

Java Edition:

| Name                | Default value | Allowed values                | Description                                                     |
|---------------------|---------------|-------------------------------|-----------------------------------------------------------------|
| ominous             | `false`       | `false`<br/>`true`            | Controls whether this trial spawner is anominous trial spawner. |
| trial_spawner_state | `inactive`    | `active`                      | When the spawner is active.                                     |
|                     |               | `cooldown`                    | When the spawner is on cooldown.                                |
|                     |               | `ejecting_reward`             | While ejecting reward.                                          |
|                     |               | `inactive`                    | When no mob is set.                                             |
|                     |               | `waiting_for_players`         | When no players are nearby, not on cooldown, and a mob is set.  |
|                     |               | `waiting_for_reward_ejection` | Prior to reward ejection.                                       |

Bedrock Edition:

| Name                | Metadata Bits | Default value | Allowed values     | Values forMetadata Bits | Description                                                     |
|---------------------|---------------|---------------|--------------------|-------------------------|-----------------------------------------------------------------|
| ominous             | Not Supported | `false`       | `false`<br/>`true` | `Unsupported`           | Controls whether this trial spawner is anominous trial spawner. |
| trial_spawner_state | Not Supported | `0`           | `0`                | `Unsupported`           | When no mob is set.                                             |
|                     |               |               | `1`                | `Unsupported`           | When no players are nearby, not on cooldown, and a mob is set.  |
|                     |               |               | `2`                | `Unsupported`           | When the spawner is active.                                     |
|                     |               |               | `3`                | `Unsupported`           | Prior to reward ejection.                                       |
|                     |               |               | `4`                | `Unsupported`           | While ejecting reward.                                          |
|                     |               |               | `5`                | `Unsupported`           | When the spawner is on cooldown.                                |



### Block data
A trial spawner has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format

- Block entity data
	- 
	- Tags common to all block entities
	- required_player_range: Between 1 and 128. Defaults to 14. — Maximum distance in blocks for players to join the battle.
	- target_cooldown_length: Defaults to 36000. — Time in ticks of the cooldown period. Includes the time spend dispensing the reward.
	- normal_config: Optional, see configuration for defaults. — The configuration to use when not ominous.
		- 
		- Trial Spawner Configuration
	- ominous_config: Optional, defaults tonormal_config. When individual entries are omitted, they also default to their setting innormal_config. — The configuration to use when ominous.
		- 
		- Trial Spawner Configuration
	- registered_players: A set of player UUIDs. — All the players that have joined the battle. The length of this array determines the amount of mobs and amount of reward.
		- : A UUID.
	- current_mobs: A set of mob UUIDs. — The mobs that were spawned by this spawner and are still alive.
		- : A UUID.
	- cooldown_ends_at: Gametime in ticks when the cooldown ends. 0 if not currently in cooldown.
	- next_mob_spawns_at: Gametime in ticks when the next spawn attempt happens. 0 if not currently active.
	- total_mobs_spawned: The total amount of mobs that have already been spawned in this cycle. 0 if not currently active.
	- spawn_data: The next mob to attempt to spawn. Selected fromspawn_potentialsafter the last attempt. Determines the mob displayed in the spawner.
		- 
		- Spawn Data
	- ejecting_loot_table: A resource location to theloot tablethat is given as reward. Unset if not currently giving rewards. Selected fromloot_tables_to_ejectafter all mobs are defeated.

Bedrock Edition:

SeeBedrock Edition level format/Block entity format.
