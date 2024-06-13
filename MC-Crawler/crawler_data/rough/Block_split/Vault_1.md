## Data values
### ID
Java Edition:

| Name  | Identifier | Form         | Translation key         |
|-------|------------|--------------|-------------------------|
| Vault | `vault`    | Block & Item | `block.minecraft.vault` |

| Name         | Identifier |
|--------------|------------|
| Block entity | `vault`    |

Bedrock Edition:

| Name  | Identifier | Numeric ID | Form                       | Item ID[i 1]   | Translation key   |
|-------|------------|------------|----------------------------|----------------|-------------------|
| Vault | `vault`    | `-314`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.vault.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

| Name         | Savegame ID |
|--------------|-------------|
| Block entity | `Vault`     |

### Block states
See also: Block states

Java Edition:

| Name        | Default value | Allowed values                            | Description                                                                                                             |
|-------------|---------------|-------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| facing      | `north`       | `east`<br/>`north`<br/>`south`<br/>`west` | The direction the vault's face is facing.<br/>The opposite from the direction the player faces while placing the vault. |
| ominous     | `false`       | `false`<br/>`true`                        | Controls whether this vault is anominous vault.                                                                         |
| vault_state | `inactive`    | `active`                                  | When a player who has not used the vault is nearby.                                                                     |
|             |               | `ejecting`                                | While ejecting reward.                                                                                                  |
|             |               | `inactive`                                | When no players who have not used the vault are nearby.                                                                 |
|             |               | `unlocking`                               | Prior to reward ejection.                                                                                               |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values                            | Values forMetadata Bits | Description                                                                                                             |
|------------------------------|---------------|---------------|-------------------------------------------|-------------------------|-------------------------------------------------------------------------------------------------------------------------|
| minecraft:cardinal_direction | Not Supported | `south`       | `east`<br/>`north`<br/>`south`<br/>`west` | `Unsupported`           | The direction the vault's face is facing.<br/>The opposite from the direction the player faces while placing the vault. |
| ominous                      | Not Supported | `false`       | `false`<br/>`true`                        | `Unsupported`           | Controls whether this vault is anominous vault.                                                                         |
| vault_state                  | Not Supported | `inactive`    | `active`                                  | `Unsupported`           | When a player who has not used the vault is nearby.                                                                     |
|                              |               |               | `ejecting`                                | `Unsupported`           | While ejecting reward.                                                                                                  |
|                              |               |               | `inactive`                                | `Unsupported`           | When no players who have not used the vault are nearby.                                                                 |
|                              |               |               | `unlocking`                               | `Unsupported`           | Prior to reward ejection.                                                                                               |



### Block data
A vault has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format

- Block entity data
	- 
	- Tags common to all block entities
	- config: Configuration data that does not automatically change. All fields are optional.
		- loot_table: A resource location to theloot tablethat is ejected when unlocking the vault. Defaults to"minecraft:chests/trial_chambers/reward".
		- override_loot_table_to_display: A resource location to the loot table that is used to display items in the vault. If not present, the game uses theloot_tablefield.
		- activation_range: The range in blocks when the vault should activate. Defaults to 4.
		- deactivation_range: The range in blocks when the vault should deactivate. Defaults to 4.5.
		- key_item: The key item that is used to check for valid keys. Defaults to"minecraft:trial_key".
			- 
			- Tags common to all items
	- server_data: Data that is only stored on the server.
		- rewarded_players: A set of player UUIDs that have already received their rewards from this vault.
		- state_updating_resumes_at: The game time when the vault processes block state changes, such as changing fromunlockingtoejectingafter a delay.
		- items_to_eject: List of item stacks that have been rolled by the loot table and are waiting to be ejected.
			- : An item stack
				- 
				- Tags common to all items
		- total_ejections_needed: The total amount of item stacks that need to be ejected.
	- shared_data: Data that is synced between the server and client.
		- display_item: The item that is currently being displayed.
		- connected_players: A set of player UUIDs that are within range of the vault.
		- connected_particles_range: The range in blocks when the vault emits particles.

Bedrock Edition:

SeeBedrock Edition level format/Block entity format.

