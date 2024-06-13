### Taming
Adult mules can be tamed: with an empty hand, mount the mule repeatedly; when it no longer bucks the player and shows hearts, it is tamed. It is necessary to tame a mule in order to give it equipment or ride it for any length of time. 

Taming depends on the mule's "temper". Mules begin with a temper of 0 out of 100. When a player is riding the mule, a random number between 0 and 99 is chosen. The mule becomes tame if this number is less than the temper, otherwise, the temper is increased by 5 and the player is bucked off. Temper can also be increased by feeding the mule.

While riding an untamed mule, a galloping sound is audible, more or less rapid to give a general idea of the mule's speed. It is unknown whether there is any indication of jump height before taming.

Like all tamed animals, a death message is displayed to their owner if they are killed.‌[Bedrock Edition  only]

### Breeding
Like their real-life counterparts, mules in Minecraft cannot produce offspring. The only way to produce a mule (other than using a spawn egg) is to cross-breed a horse with a donkey.

### Food
Feeding a mule food can alter its behavior, cause it to grow (if it is not yet an adult; foals normally take 20 minutes to fully mature if not fed), and/or restore its health. The table below lists the effects of the various foods mules eat.

To feed a mule, hold a valid food item and press use on the mule. If the food is invalid, the player simply mounts the mule. Mules can be fed only when feeding would have an effect, similar to other animals.

| Food          | Heals  | Speeds growth by | Increases temper | Notes                                           |
|---------------|--------|------------------|------------------|-------------------------------------------------|
| Sugar         | 1      | 30 sec           | +3               |                                                 |
| Wheat         | 2      | 20 sec           | +3               |                                                 |
| Apple         | 3      | 1 min            | +3               |                                                 |
| Golden carrot | 4      | 1 min            | +5               |                                                 |
| Golden apple  | 10     | 4 min            | +10              |                                                 |
| Hay bale      | 20× 10 | 3 min            | N/A              | Hay bales cannot be fed to untamed adult mules. |

## Statistics
See also: Tutorials/Horses

Mules have three "equine stats" that vary from mule to mule: health, (maximum) movement speed, and jump strength. These stats are created once the mule is born or spawned, and are not affected by food.

### Spawned values
When spawned in any way except breeding – for instance, using commands or using spawn eggs – mules are assigned their stats within certain ranges, specific according to their horse type.

#### Health
A mule's health ranges from 15–30, but tends toward the average of 22–23. Displayed hearts are health, divided by two, rounded down. A mule with a non-even number of health points (15, 17, 19, etc.) does not show the last half-heart. If the mule has lost one fewer health point than the inflicted damage and did not regenerate, it has an odd number of health points, otherwise, it has an even number of health points.

#### Movement speed
Spawned mules' speed is always 0.175; the player's normal walking speed is 0.1. The speed listed does not include any status effect that affects the speed of a horse or a player. Bred mules have speed based on their parent's speeds, like all other horse breeding.

See transportation to compare the speeds of various transportation methods.

#### Jump strength
Spawned mules' jump strength is usually 0.5, which is enough to clear 1 9⁄16 blocks. Other jump strengths can be found in bred mules, depending on the statistics of the parents (as explained later).

### Bred values
When breeding a horse and a donkey, the foal's stats are determined by a variation of the average of both parents' stats, randomly determined as horses' stats are.

## Data values
### ID
Java Edition:

| Name | Identifier | Entity tags            | Translation key         |
|------|------------|------------------------|-------------------------|
| Mule | `mule`     | `dismounts_underwater` | `entity.minecraft.mule` |

Bedrock Edition:

| Name | Identifier | Numeric ID | Translation key    |
|------|------------|------------|--------------------|
| Mule | `mule`     | `25`       | `entity.mule.name` |

### Entity data
Mules have entity data associated with them that contain various properties.

Java Edition:

Main article: Entity format
- Entity data
	- 
	- Additional fields for mobs that can breed
	- 
	- Tags common to all entities
	- 
	- Tags common to all mobs
	- 
	- Tags common to all horses
	- 
	- ChestedHorse: 1 or 0 (true/false) - true if the horse has chests. A chested horse that is not a donkey or a mule crashes the game.
	- Items: List of items. Exists only if ChestedHorse is true.
		- An item, including the Slot tag. Slots are numbered 2 to 16 for donkeys and mules, and none exist for all other horses.
			- 
			- Tags common to all items

Bedrock Edition:

SeeBedrock Edition level format/Entity format.

