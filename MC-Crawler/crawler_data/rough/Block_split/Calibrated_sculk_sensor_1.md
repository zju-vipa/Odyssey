## Data values
### ID
Java Edition:

| Name                    | Identifier                | Form         | Translation key                           |
|-------------------------|---------------------------|--------------|-------------------------------------------|
| Calibrated Sculk Sensor | `calibrated_sculk_sensor` | Block & Item | `block.minecraft.calibrated_sculk_sensor` |

| Name         | Identifier                |
|--------------|---------------------------|
| Block entity | `calibrated_sculk_sensor` |

Bedrock Edition:

| Name                    | Identifier                | Numeric ID | Form                       | Item ID[i 1]   | Translation key                     |
|-------------------------|---------------------------|------------|----------------------------|----------------|-------------------------------------|
| Calibrated Sculk Sensor | `calibrated_sculk_sensor` | `-580`     | Block & Giveable Item[i 2] | Identical[i 3] | `tile.calibrated_sculk_sensor.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

| Name         | Savegame ID             |
|--------------|-------------------------|
| Block entity | `CalibratedSculkSensor` |

### Block states
See also: Block states

Java Edition:

| Name               | Default value | Allowed values                                                                                                                    | Description                                                                                                                                                         |
|--------------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| facing             | `north`       | `east`<br/>`north`<br/>`south`<br/>`west`                                                                                         | The direction the calibrated sculk sensor's amethystinputis facing.<br/>The opposite from the direction the player faces while placing the calibrated sculk sensor. |
| power              | `0`           | `0`<br/>`1`<br/>`2`<br/>`3`<br/>`4`<br/>`5`<br/>`6`<br/>`7`<br/>`8`<br/>`9`<br/>`10`<br/>`11`<br/>`12`<br/>`13`<br/>`14`<br/>`15` | The calibrated sculk sensor's current power level.                                                                                                                  |
| sculk_sensor_phase | `inactive`    | `active`<br/>`cooldown`<br/>`inactive`                                                                                            | Whether or not the calibrated sculk sensor is active.[more information needed]                                                                                      |
| waterlogged        | `false`       | `false`<br/>`true`                                                                                                                | Whether or not there's water in the same place as this calibrated sculk sensor.                                                                                     |

Bedrock Edition:

| Name                         | Metadata Bits | Default value | Allowed values                            | Values forMetadata Bits | Description                                                                                                                                                         |
|------------------------------|---------------|---------------|-------------------------------------------|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| minecraft:cardinal_direction | Not Supported | `south`       | `east`<br/>`north`<br/>`south`<br/>`west` | `Unsupported`           | The direction the calibrated sculk sensor's amethystinputis facing.<br/>The opposite from the direction the player faces while placing the calibrated sculk sensor. |
| sculk_sensor_phase           | Not Supported | `0`           | `0`<br/>`1`<br/>`2`                       | `Unsupported`           | The calibrated sculk sensor phase.[more information needed]                                                                                                         |

### Block data
A calibrated sculk sensor has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format

- : Block entity data.
	- 
	- Tags common to all block entities
	- last_vibration_frequency: The frequency of the last vibration.
	- listener: The vibration event listener for this sculk shrieker, sculk sensor, or calibrated sculk sensor.
		- event: Only exists if there is an incoming vibration.
			- distance: The distance between this vibration's source and the block.
			- game_event: Theresource locationof the vibration event that caused the current incoming vibration.
			- pos: The coordinates of the source of this vibration.
				- : X coordinate.
				- : Y coordinate.
				- : Z coordinate.
			- projectile_owner: If the vibration was caused by a projectile, this is theUUIDof the entity that launched the projectile. Does not exist if vibration was not caused by a projectile.
			- source: TheUUIDof the entity that caused the vibration. Does not exist if vibration was not caused by an entity.
		- event_delay: How many ticks remain until triggered by the vibration. Set to 0 if there is no incoming vibration
		- selector: The data of the vibration selector.[more information needed]
			- tick: The game time when the vibration occurs, or -1 if there is no vibration to choose from.[more information needed]
			- event: Candidate game event, with the same structure as theeventtag above.[more information needed]

Bedrock Edition:

SeeBedrock Edition level format/Block entity format.

