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


↑ Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.


### Crafting
| Ingredients                 | Crafting recipe |
|-----------------------------|-----------------|
| Amethyst Shard+Sculk Sensor |                 |

## Usage
The calibrated sculk sensor is different from the basic sculk sensor in multiple ways:

- It can detect vibrations within adistanceof 16 blocks, instead of 8.
- It has a cooldown of 1 second instead of 2.
- It can be filtered (see below) to only react to some sounds.

### Filtering
When a redstone signal powers a calibrated sculk sensor on its crystalized side, the sensor will be filtered to only respond to vibrations that match the strength of that signal. Every vibration in the game has a frequency associated with it, and every vibration frequency directly matches a specific redstone signal strength. So, for example, a vibration with a frequency of 5 matches the redstone signal with a strength of 5.

| Redstone |        | Sounds with that frequency                                                                                              |
|----------|--------|-------------------------------------------------------------------------------------------------------------------------|
|          | Signal | Wire                                                                                                                    |
| 1        |        | Walking(notsneaking),climbing,jumping,swimming,crawling.                                                                |
| 2        |        | Landingon any solid block (i.e. stone, a slime block, or a honey block) or in any liquid (water, lava, or powder snow). |
| 3        |        | Using an item (casting a fishing pole, throwing a snowball, drinking a potion, drinking milk, etc.).                    |
| 4        |        | Aplayergliding with anelytraor amobperforming auniqueaction (e.g. a ravager roaring, a wolf shaking, etc.).             |
| 5        |        | Dismounting a mob or equipping a piece of gear.                                                                         |
| 6        |        | Mounting a mob or interacting with a mob (e.g. trading with a villager, etc).                                           |
| 7        |        | A mob or player takingdamage.                                                                                           |
| 8        |        | Eating afooditem.                                                                                                       |
| 9        |        | A block 'deactivating' (e.g. closing a door or chest, a pressed button becoming unpressed, etc.).                       |
| 10       |        | A block 'activating' (e.g. opening a door or chest, pressing a button being pressed, etc.).                             |
| 11       |        | A block changing (e.g. adding food to campfire, etc.).                                                                  |
| 12       |        | A non-woolblock being destroyed.                                                                                        |
| 13       |        | A non-wool block being placed.                                                                                          |
| 14       |        | A mob or playerteleportingor spawning.                                                                                  |
| 15       |        | A mob or player dying, or anexplosionhappening.                                                                         |



