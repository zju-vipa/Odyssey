### Food
Feeding a horse food can alter its behavior, cause it to grow (if it is not yet an adult; foals normally take 20 minutes to fully mature if not fed), and/or restore its health. The table below lists the effects of the various foods horses can take.

In Bedrock Edition, the health of foals cannot be restored by feeding.

In Java Edition, feeding tamed horses in full health has no sound effect and movements.[4][5] In Bedrock Edition, while temper is at max value, untamed horses can be fed any food except hay bale.

To feed a horse, hold a valid food item and press use on the horse.

| Food          | Heals  | Speeds growth by   | Increases temper | Notes                                                                 |
|---------------|--------|--------------------|------------------|-----------------------------------------------------------------------|
| Sugar         | 1      | 30 sec (600 ticks) | +3               |                                                                       |
| Wheat         | 2      | 20 sec (400 ticks) | +3               |                                                                       |
| Apple         | 3      | 1 min (1200 ticks) | +3               |                                                                       |
| Golden carrot | 4      | 1 min (1200 ticks) | +5               | Activateslove modein tamed horses.                                    |
| Golden apple  | 10     | 4 min (4800 ticks) | +10              | Activateslove modein tamed horses. Enchanted golden apples also work. |
| Hay bale      | 20× 10 | 3 min (3600 ticks) | N/A              | InBedrock Edition, adult horse in full health cannot be fed.          |

## Statistics
See also: Tutorials/Horses

All horses have three "equine stats" that vary from horse to horse: health, (maximum) movement speed, and jump height. These stats are created once the horse is born or spawned, and are not affected by food.

### Spawned values
When spawned in any way except breeding – for instance, using commands, spawning naturally, spawning as part of a skeleton trap, or using spawn eggs – horses are assigned their stats within certain ranges.

#### Health
Horse's health points range from 15 × 7.5 to 30 × 15, with an average of 22.5 × 11.25. A horse with an odd number of health points does not show the last half-heart.

#### Movement speed
Horse's movement speed ranges from 0.1125–0.3375 in internal units, with an average of 0.225. For reference, the player's normal walking speed is 0.1. The speed listed does not include any status effect that affects the speed of the horse or the player.

The conversion factor between internal units and blocks/sec is roughly 43.17. However, horses instead travel at just shy of 42.16 blocks/sec times their internal attribute, putting the best horse's maximum speed at 14.23 blocks/second, and the average horse's speed at about 9.49 blocks/sec.

- Minimum: 4.74 blocks/sec.
- Player speed (walking): 4.317 blocks/sec.
- Player speed (sprinting): 5.612 blocks/sec.

See also transportation methods to compare the speeds of various transportation methods.

#### Jump strength
Horse's jump strength ranges from 0.4–1.0, with an average of 0.7.

A jump strength of 0.5 is enough to clear 1 9⁄16 blocks, while 1.0 is enough to clear 5 1⁄4 blocks.

### Bred values
When breeding two horses, or a horse and a donkey, the foal's stats are determined by averaging both parent's stats and adding a random variation to it.[more information needed]

The variant of the child has an 11% chance to be a random base color, and a 20% chance to have random markings. Otherwise, it chooses the values from one of its parents.

## Data values
### ID
Java Edition:

| Name  | Identifier | Entity tags            | Translation key          |
|-------|------------|------------------------|--------------------------|
| Horse | `horse`    | `dismounts_underwater` | `entity.minecraft.horse` |

Bedrock Edition:

| Name  | Identifier | Numeric ID | Translation key     |
|-------|------------|------------|---------------------|
| Horse | `horse`    | `23`       | `entity.horse.name` |

### Entity data
Horses have entity data associated with them that contain various properties.

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
	- ArmorItem: The armor of this horse. Ignored if the item is not one of thehorse armors.‌[until JE 1.20.5]
		- 
		- Tags common to all items
	- Variant: The variant of the horse. Determines colors. Stored asbaseColor | (markings << 8). Unused values lead to white horses.


Horse Variant
Main article: Horse/DV[edit]

Bedrock Edition:

SeeBedrock Edition level format/Entity format.

