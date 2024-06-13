## Behavior
The skeleton horse is an undead mob that is initially defensive when it spawns and triggers a skeleton trap horse if the player gets too close, but once the skeleton rider is defeated, the skeleton horse becomes completely passive. Skeleton horses behave like normal horses, roaming idly and occasionally stopping to rear, swish their tails, or lower their heads as though eating the grass. Unlike sheep, the eating animation does not actually cause any grass to be consumed. Skeleton horses can breathe in water.

Unlike other passive mobs, skeleton horses slowly regenerate health evident by their health bar while the player rides it. This is the same case for normal horses.

Skeleton horses cannot be bred, however, in Java Edition, skeleton horses can be fed while being ridden by the skeleton, the valid food items are the same as for the normal horse: sugar, wheat, normal/gold/enchanted apples, golden carrots, and hay bales. 

Being an undead mob, they are: 

- damaged by the status effectInstant Healthand healed by the status effectInstant Damage.
- unaffected by the status effectsRegenerationandPoison.
- ignored by thewither.
- affected by theSmiteenchantment.
- a threat toarmadillos, causing them to hide in their shell.‌[upcoming: JE 1.20.5 & BE 1.20.80]

Other notes:

- The skeleton wears an iron helmet, unless it randomly spawned with some other headgear.
- The skeleton's bow and helmet are enchanted as if on anenchanting tableat level 5–22. The exact level depends onregional difficulty; on Easy it is always a level-5 enchantment.
- The skeleton trap horse and the skeleton horse in a jockey are always adult. InBedrock Edition, the skeleton trap horse is not an adult nor a baby, though it looks like an adult.
	- Baby skeleton horses can be spawned with aspawn egg. Baby skeleton horses cannot grow up normally InBedrock Edition.
- The skeleton in a naturally spawned skeleton horseman jockey does not despawn.
- A trap horse may spawn in areas that a regular horse may not, such as the middle of an ocean.
- A trap horse can trigger normally in clear weather (and often a player encounters a trap horse after the thunderstorm has cleared).
- The skeleton drops more experience orbs.
- The skeleton does not shoot any mob that attacks the skeleton horse.
- InBedrock Edition, skeleton horses are killed by theconduitlike any regular hostile mob, despite being tamed.[3]

### Taming
In Bedrock Edition, the skeleton horse is always tamed. In Java Edition, a skeleton trap horse becomes tamed when struck by lightning. The other three skeleton horses are tamed when they are spawned.

In Java Edition, with the use of commands, a skeleton horse can be tamed in the same way as a regular horse, granting the Best Friends Forever advancement:/ride @s mount @e[type=minecraft:skeleton_horse,limit=1]. A tamed skeleton horse can also be summoned using /summon minecraft:skeleton_horse ~ ~ ~ {Tame:1b}.

## Statistics
See also: Tutorials/Horses

All horses have three "equine stats" that vary from horse to horse: health, maximum movement speed, and jump strength. These stats are created once the horse is born or spawned, and are not affected by food.

### Spawned values
When spawned in any way except breeding – for instance, using commands, spawning naturally, spawning as part of a skeleton trap, or using spawn eggs – horses are assigned their stats within certain ranges, specific according to their horse type.

#### Health
A skeleton horse's health is always 15. Displayed hearts are health, divided by two, rounded down. A horse with an odd number of health points (15, 17, 19, etc.) does not show the last half-heart. If the horse has lost one health point lower than the inflicted damage and did not regenerate, it has an odd number of health points, otherwise, it has an even number of health points.

#### Movement speed
Skeleton horse's speed is always 0.2;
the player's normal walking speed is 0.1. The speed listed does not include any status effect that affects the speed of a horse or a player.

See transportation to compare the speeds of various transportation methods.

#### Jump strength
Jump strength ranges from 0.4–1.0, averaging 0.7.

A jump strength of 0.5 is enough to clear 1 19⁄32 blocks, while 1.0 is enough to clear 5 9⁄32 blocks.

The jump strengths required to clear several block heights are:

| Jump Strength | Blocks                      |
|---------------|-----------------------------|
| 0.967         | 5.00                        |
| 0.848         | 4.00                        |
| 0.716         | 3.00                        |
| 0.565         | 2.00                        |
| 0.431         | 1.25 (player's jump height) |

## Data values
### ID
Java Edition:

| Name           | Identifier       | Entity tags                                                                                                                                | Translation key                   |
|----------------|------------------|--------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| Skeleton Horse | `skeleton_horse` | `can_breathe_under_water`<br/>`ignores_poison_and_regen`<br/>`inverted_healing_and_harm`<br/>`skeletons`<br/>`undead`<br/>`wither_friends` | `entity.minecraft.skeleton_horse` |

Bedrock Edition:

| Name           | Identifier       | Numeric ID | Translation key              |
|----------------|------------------|------------|------------------------------|
| Skeleton Horse | `skeleton_horse` | `26`       | `entity.skeleton_horse.name` |

### Entity data
Skeleton horses have entity data associated with them that contain various properties.

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
	- SkeletonTrap: 1 or 0 (true/false) - true if the horse is a trappedskeleton horse. Does not affect horse type.
	- SkeletonTrapTime: Incremented each tick when SkeletonTrap is set to 1. The horse automatically despawns when it reaches 18000 (15 minutes).

Bedrock Edition:

SeeBedrock Edition level format/Entity format.

