# Calibrated Sculk Sensor
A calibrated sculk sensor is a craftable variant of sculk sensor. Similarly to its counterpart it detects vibrations, but with twice the range, and can detect multiple vibrations in quicker succession. It outputs a signal on all sides except for its input, which can receive power to make the sensor only listen to specific vibrations, depending on the input signal strength.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Crafting
- 2 Usage
	- 2.1 Filtering
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
	- 4.3 Block data
- 5 History
- 6 Gallery
- 7 Issues
- 8 References

## Obtaining
### Breaking
Calibrated sculk sensors can be broken with any tool, but can be broken faster with a hoe. They drop experience when broken. When broken by an item that is enchanted with Silk Touch, a calibrated sculk sensor drops itself.

| Block     | Calibrated Sculk Sensor |
|-----------|-------------------------|
| Hardness  | 1.5                     |
| Tool      |                         |
|           | Breakingtime (sec)[A]   |
| Default   | 2.25                    |
| Wooden    | 1.15                    |
| Stone     | 0.6                     |
| Iron      | 0.4                     |
| Diamond   | 0.3                     |
| Netherite | 0.25                    |
| Golden    | 0.2                     |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Crafting
| Ingredients                      | Crafting recipe |
|----------------------------------|-----------------|
| Amethyst Shard+<br/>Sculk Sensor |                 |

## Usage
The calibrated sculk sensor is different from the basic sculk sensor in multiple ways:

- It can detect vibrations within adistanceof 16 blocks, instead of 8.
- It has a cooldown of 1 second instead of 2.
- It can be filtered (see below) to only react to some sounds.

### Filtering
When a redstone signal powers a calibrated sculk sensor on its crystalized side, the sensor will be filtered to only respond to vibrations that match the strength of that signal. Every vibration in the game has a frequency associated with it, and every vibration frequency directly matches a specific redstone signal strength. So, for example, a vibration with a frequency of 5 matches the redstone signal with a strength of 5.

| Redstone |      | Sounds with that frequency                                                                                              |
|----------|------|-------------------------------------------------------------------------------------------------------------------------|
| Signal   | Wire |                                                                                                                         |
| 1        |      | Walking(notsneaking),climbing,jumping,swimming,crawling.                                                                |
| 2        |      | Landingon any solid block (i.e. stone, a slime block, or a honey block) or in any liquid (water, lava, or powder snow). |
| 3        |      | Using an item (casting a fishing pole, throwing a snowball, drinking a potion, drinking milk, etc.).                    |
| 4        |      | Aplayergliding with anelytraor amobperforming auniqueaction (e.g. a ravager roaring, a wolf shaking, etc.).             |
| 5        |      | Dismounting a mob or equipping a piece of gear.                                                                         |
| 6        |      | Mounting a mob or interacting with a mob (e.g. trading with a villager, etc).                                           |
| 7        |      | A mob or player takingdamage.                                                                                           |
| 8        |      | Eating afooditem.                                                                                                       |
| 9        |      | A block 'deactivating' (e.g. closing a door or chest, a pressed button becoming unpressed, etc.).                       |
| 10       |      | A block 'activating' (e.g. opening a door or chest, pressing a button being pressed, etc.).                             |
| 11       |      | A block changing (e.g. adding food to campfire, etc.).                                                                  |
| 12       |      | A non-woolblock being destroyed.                                                                                        |
| 13       |      | A non-wool block being placed.                                                                                          |
| 14       |      | A mob or playerteleportingor spawning.                                                                                  |
| 15       |      | A mob or player dying, or anexplosionhappening.                                                                         |



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
