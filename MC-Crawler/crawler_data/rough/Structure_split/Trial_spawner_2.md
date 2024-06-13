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

