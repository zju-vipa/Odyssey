# Wither (effect)
Wither is a status effect that inflicts damage over time. It acts similarly to Poison, save for the fact that it acts slower, can do so against the undead, and can kill.

## Contents
- 1 Mechanic
- 2 Effect
- 3 Causes
- 4 Immune mobs
- 5 Data values
	- 5.1 ID
- 6 Advancements
- 7 History
- 8 Issues
- 9 Trivia
- 10 References

## Mechanic
Wither is an effect that keeps damaging the player as it continues. Unlike Poison, it can affect undead mobs, deals less damage per second, and can kill. It is usually difficult for the player to see how much health they have left, as it turns the player's health bar black.

## Effect
An animation of HP when it receives a "Wither" status for 5 seconds (level 2).
The amount of damage inflicted to the affected entity is shown in the table below:

| Level      | Ticks per | per second |
|------------|-----------|------------|
| 1          | 40        | 0.5× 0.25  |
| 2          | 20        | 1          |
| 3          | 10        | 2          |
| 4[note 1]  | 5         | 4          |
| 5[note 1]  | 2         | 10         |
| 6+[note 1] | 1         | 20× 10     |


↑ a b c Due to damage immunity, the effective rate is 10 ticks ( × 1 per second) at levels 4 and up.


The player's hearts turn black ( on Survival mode or  on Hardcore‌[Java Edition  only] mode), making it more difficult, but still possible, for the player to see their health. Death is reported as "<player> withered away".
Amplifiers outside the range 0–31 (corresponding to levels 1–32) use modulo 32.

## Causes
| Cause                     | Potency | Length                                          | Lifetime damage                                  | Notes                                                                                |
|---------------------------|---------|-------------------------------------------------|--------------------------------------------------|--------------------------------------------------------------------------------------|
| Potion of Decay           | II      | 0:40                                            | 40× 20                                           | ‌[Bedrock Edition  only][more information needed]                                    |
| Splash Potion of Decay    | II      | 0:30                                            | 30× 15                                           | ‌[Bedrock Edition  only][more information needed]                                    |
| Lingering Potion of Decay | II      | 0:10                                            | 10                                               | ‌[Bedrock Edition  only][more information needed]                                    |
| Arrow of Decay            | II      | 0:05                                            | 5                                                | ‌[Bedrock Edition  only]                                                             |
| Wither                    | II      | 0:10 (normal difficulty) 0:40 (hard difficulty) | 10 (normal difficulty) 40 × 20 (hard difficulty) | When wither skulls make a direct hit on the target. Normal and Hard difficulty only. |
| Wither Skeleton           | I       | 0:10                                            | 5                                                | Melee attack only.                                                                   |
| Wither Rose               | I       | 0:02[note 1]                                    | 1                                                | Only when in range (within the block)                                                |
| Suspicious Stew           | I       | 0:08                                            | 4                                                | Must be made withWither Rose                                                         |


↑ In Java Edition the effect is being refreshed every tick, causing it to apply damage at the same rate. Effectively this causes 1 () damage every 10 ticks (instead of every 2 seconds) to living entities due to damage immunity while the entity touches the block.


## Immune mobs
Wither skeletons, withers and ender dragons are immune to Wither, while witches are 85% resistant to damage from Wither.

## Data values
### ID
This section is about the effect IDs.  For the IDs on potions, see Potion § Item data.  For for the IDs on tipped arrows, see Arrow § Metadata.
Java Edition:

| Name   | Identifier | Numeric ID | Translation key         |
|--------|------------|------------|-------------------------|
| Wither | wither     | 20         | effect.minecraft.wither |

Bedrock Edition:

| Name   | Identifier | Numeric ID | Translation key |
|--------|------------|------------|-----------------|
| Wither | wither     | 20         | potion.wither   |

