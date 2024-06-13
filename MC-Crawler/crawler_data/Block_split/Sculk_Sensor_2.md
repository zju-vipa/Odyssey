#### Things which are not detected
The following occurrences, despite presumably causing physical motion, do not produce vibrations and therefore cannot be detected: 

- Blocks destroyed by a fluid flowing into their space[1]
- Several blocks being destroyed due to their supporting block being removed:[2]
	- Rails
	- Powered rails
	- Detector rails
	- Activator rails
	- Redstone wire
	- Redstone repeaters
	- Redstone comparators
- Several cases where adispenserfails to perform an action:[3]
	- Flint and steel not creating fire
	- Bone meal not growing something
	- Heads and carved pumpkins, if not equipped on something or placed
	- Shulker boxes, if not placed
	- Shears, if there's nothing to shear
	- Glowstone, if it doesn't charge a respawn anchor
- Inserting aneye of enderinto anend portal frame[4][5]
- Eyes of ender breaking[6]
- Silverfishentering blocks[7]
- Waterandlavaflowing into existing spaces, or drying up[8]
- Changing the mode of aredstone comparator[9]
- Changing the delay on aredstone repeater[10]
- Changing the shape of a single unit ofredstone wire[11]
- Fireextinguished by rain[12]

The following cases have been confirmed to be intentional: 

- Axolotlsbeing bred via tropical fish buckets[13]
- Moss blocksreplacing existing blocks[14]

### Piston interactivity
Sculk sensors are immovable. Pistons cannot push them, and sticky pistons cannot push or pull them. Slime blocks and honey blocks do not stick to sculk sensors and have no effect whether the slime block or honey block is being pushed or pulled.

## Data values
### ID
Java Edition:

| Name         | Identifier   | Form         | Translation key              |
|--------------|--------------|--------------|------------------------------|
| Sculk Sensor | sculk_sensor | Block & Item | block.minecraft.sculk_sensor |

| Name         | Identifier   |
|--------------|--------------|
| Block entity | sculk_sensor |

Bedrock Edition:

| Name         | Identifier   | Numeric ID | Form                       | Item ID[i 1]   | Translation key        |
|--------------|--------------|------------|----------------------------|----------------|------------------------|
| Sculk Sensor | sculk_sensor | 562        | Block & Giveable Item[i 2] | Identical[i 3] | tile.sculk_sensor.name |


↑ ID of block's direct item form, which is used in savegame files and addons.

↑ Available with /give command.

↑ The block's direct item form has the same id as the block.


| Name         | Savegame ID |
|--------------|-------------|
| Block entity | SculkSensor |

### Block states
See also: Block states

Java Edition:

| Name               | Default value | Allowed values         | Description                                                          |
|--------------------|---------------|------------------------|----------------------------------------------------------------------|
| power              | 0             | 0123456789101112131415 | The sculk sensor's current power level.                              |
| sculk_sensor_phase | inactive      | activecooldowninactive | Whether or not the sculk sensor is active.[more information needed]  |
| waterlogged        | false         | falsetrue              | Whether or not there's water in the same place as this sculk sensor. |

Bedrock Edition:

| Name               | Metadata Bits | Default value | Allowed values | Values forMetadata Bits | Description                                      |
|--------------------|---------------|---------------|----------------|-------------------------|--------------------------------------------------|
| sculk_sensor_phase | Not Supported | 0             | 012            | Unsupported             | The sculk sensor phase.[more information needed] |



### Block data
A sculk sensor has a block entity associated with it that holds additional data about the block.

Java Edition:

See also: Block entity format


: Block entity data.
Tags common to all block entities
 last_vibration_frequency: The frequency of the last vibration.
 listener: The vibration event listener for this sculk shrieker, sculk sensor, or calibrated sculk sensor.
 event: Only exists if there is an incoming vibration.
 distance: The distance between this vibration's source and the block.
 game_event: The resource location of the vibration event that caused the current incoming vibration.
 pos: The coordinates of the source of this vibration.
: X coordinate.
: Y coordinate.
: Z coordinate.
 projectile_owner: If the vibration was caused by a projectile, this is the UUID of the entity that launched the projectile. Does not exist if vibration was not caused by a projectile.
 source: The UUID of the entity that caused the vibration. Does not exist if vibration was not caused by an entity.
 event_delay: How many ticks remain until triggered by the vibration. Set to 0 if there is no incoming vibration
 selector: The data of the vibration selector.[more information needed]
 tick: The game time when the vibration occurs, or -1 if there is no vibration to choose from.[more information needed]
 event: Candidate game event, with the same structure as the  event tag above.[more information needed]

Bedrock Edition:

See Bedrock Edition level format/Block entity format.

