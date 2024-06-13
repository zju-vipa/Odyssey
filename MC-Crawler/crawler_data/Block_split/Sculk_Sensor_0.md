# Sculk Sensor
The sculk sensor is a block in the sculk family. It detects vibrations caused by actions and events in a radius around it and emits a redstone signal, and, if it was triggered by a player, also activates nearby sculk shriekers. Players can sneak to avoid making vibrations and wool can be used to occlude and block them.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Natural generation
	- 1.3 Chest loot
	- 1.4 Post-generation
- 2 Usage
	- 2.1 Crafting ingredient
	- 2.2 Light
	- 2.3 Vibration detection
	- 2.4 Redstone emission
		- 2.4.1 Vibration frequencies
		- 2.4.2 Vibration resonance
		- 2.4.3 Things which are not detected
	- 2.5 Piston interactivity
- 3 Sounds
	- 3.1 Generic
	- 3.2 Unique
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
	- 4.3 Block data
- 5 Achievements
- 6 Advancements
- 7 History
- 8 Issues
- 9 Trivia
- 10 Gallery
	- 10.1 Screenshots
	- 10.2 Development images
- 11 References
- 12 External links

## Obtaining
### Breaking
Sculk sensors can be mined with any tool enchanted with Silk Touch, but hoes are the quickest. If mined with a non-Silk Touch tool, they drop 5 experience instead.

| Block     | Sculk Sensor          |
|-----------|-----------------------|
| Hardness  | 1.5                   |
| Tool      |                       |
|           | Breakingtime (sec)[A] |
| Default   | 2.25                  |
| Wooden    | 1.15                  |
| Stone     | 0.6                   |
| Iron      | 0.4                   |
| Diamond   | 0.3                   |
| Netherite | 0.25                  |
| Golden    | 0.2                   |


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


### Natural generation
Sculk sensors generate within the deep dark biome and ancient cities.


### Chest loot
| Item         | Structure    | Container | Quantity | Chance                         |
|--------------|--------------|-----------|----------|--------------------------------|
|              |              |           |          | Java EditionandBedrock Edition |
| Sculk Sensor | Ancient City | Chest     | 1–3      | 23.2%                          |

### Post-generation
A sculk catalyst has a 9% chance of generating a sculk sensor on top of a sculk block.

## Usage
### Crafting ingredient
Sculk sensors can be used to craft calibrated sculk sensors.

| Name                    | Ingredients                 | Crafting recipe |
|-------------------------|-----------------------------|-----------------|
| Calibrated Sculk Sensor | Amethyst Shard+Sculk Sensor |                 |

### Light
A sculk sensor has a light level of 1. When active, it changes to a lighter block state without a change to the light level.

### Vibration detection
The sculk sensor vibration particle.
Sculk sensors detect vibrations in an 8 block spherical radius around it. Vibrations are caused by various events, such as a player and mobs walking, placing or breaking blocks, gliding with elytra, items falling on the ground, a piston extending or a wet wolf shaking itself off. While sneaking, a player is not detected. Walking, falling, dropping items, or shooting a projectile all trigger the sensor.

When a vibration is made within the range of a sculk sensor, a signal travels from the vibration source to the sensor at a speed of one block per game tick (20 blocks per second). When the signal arrives, the sensor is activated for 30 game ticks (1.5 seconds). The sensor cannot detect any other vibrations while activated or while a signal is traveling to it.

Sculk sensors have a cooldown period of 10 game ticks (0.5 seconds) after being placed or after deactivating. During this cooldown period, they cannot detect vibrations. This prevents a sensor from reactivating when a contraption it is powering (such as a piston) becomes unpowered.

Sculk sensors don't detect vibrations from other sculk sources or the warden in Java Edition.

Wool and carpets have a special interaction with sculk sensors. If a wool block is placed between a sensor and a vibration source, the sensor is not able to detect the placed wool nor vibrations behind it. Specifically, if the ray joining the cube centers of the sensor block and the vibration source passes through any wool blocks, the noise is muffled. If the ray passes diagonally through the edge between two blocks, either one or the other block may muffle it but not both. Sculk sensors are not able to detect footsteps or dropped items on wool blocks or carpet, and they are also unable to detect dropped items of wool and carpets.

Sculk sensors pass on the vibrations made by players to sculk shriekers within 8 blocks of the sensor. For example, an item dropped by a player triggers the shrieker, but an item dropped by a dispenser or from a broken block does not; a player flying around with elytra triggers the shrieker, but a bat flying around does not. Alarms can be blocked by wool placed in between the sensor and shrieker, similar to how wool can block vibrations from reaching the sensor itself.

