# Poison
Poison is an effect that inflicts damage over time. It is similar to Wither, but it drains health faster and it cannot kill (it does, however, reduce the player's health all the way to 1 ()).

## Contents
- 1 Effect
- 2 Causes
- 3 Brewing
- 4 Immune mobs
- 5 Data values
	- 5.1 ID
- 6 Achievements
- 7 Advancements
- 8 History
- 9 Issues
- 10 Trivia
- 11 References

## Effect
The amount of damage inflicted to the affected entity is shown in the table below:

| Level      | Ticks per | per second |
|------------|-----------|------------|
| 1          | 25        | 0.8× 0.4   |
| 2          | 12        | 1.66× 0.83 |
| 3[note 1]  | 6         | 3.32× 1.66 |
| 4[note 1]  | 3         | 6.66× 3.33 |
| 5+[note 2] | 1         | 20× 10     |


↑ a b Due to damage immunity, the effective rate of damage is 12 ticks ( × 0.8 per second).

↑ Due to damage immunity, the effective rate of damage is 10 ticks ( × 1 per second).


The player's hearts turn yellow-green ()( on hardcore mode).

The damage stops when the affected entity is at 1 () health, but can resume if healing occurs and the affected entity is at more than 1 () health before the effect expires. 

Amplifiers outside the range 0–31 (corresponding to levels 1–32) are treated modulo 32 (as though reduced by 32 until they are within the range, or alternatively as the remainder from the division by 32, i.e. 33 or 65 is treated as 1).

The effect can be removed by drinking milk or honey. In  Minecraft Education and Bedrock Edition when education options are enabled, drinking antidote also removes poison.

## Causes
| Cause                                | Potency | Length                                         | Lifetime damage                            | Notes                                                                                                    |
|--------------------------------------|---------|------------------------------------------------|--------------------------------------------|----------------------------------------------------------------------------------------------------------|
| Potion of Poison                     | I       | 0:45                                           | 36× 18                                     |                                                                                                          |
| Potion of Poison(extended)           | I       | 1:30‌[JE  only]2:00‌[BE  only]                 | 72× 36‌[JE  only]96× 48‌[BE  only]         |                                                                                                          |
| Potion of PoisonII                   | II      | 0:21‌[JE  only]0:22‌[BE  only]                 | 35× 17.5‌[JE  only]36× 18‌[BE  only]       |                                                                                                          |
| Splash Potion of Poison              | I       | 0:45‌[JE  only]0:33‌[BE  only]                 | 36× 18‌[JE  only]26× 13‌[BE  only]         | Witchesthrow this splash potion if their target has 8or more health.                                     |
| Splash Potion of Poison(extended)    | I       | 1:30                                           | 72× 36                                     |                                                                                                          |
| Splash Potion of PoisonII            | II      | 0:21‌[JE  only]0:16‌[BE  only]                 | 35× 17.5‌[JE  only]26× 13‌[BE  only]       |                                                                                                          |
| Lingering Potion of Poison           | I       | 0:11                                           | 8                                          |                                                                                                          |
| Lingering Potion of Poison(extended) | I       | 0:22‌[JE  only]0:30‌[BE  only]                 | 17× 8.5‌[JE  only]24× 12‌[BE  only]        |                                                                                                          |
| Lingering Potion of PoisonII         | II      | 0:05                                           | 8                                          |                                                                                                          |
| Arrow of Poison                      | I       | 0:05                                           | 4                                          |                                                                                                          |
| Arrow of Poison(extended)            | I       | 0:11‌[JE  only]0:15‌[BE  only]                 | 8‌[JE  only]12× 6‌[BE  only]               |                                                                                                          |
| Arrow of PoisonII                    | II      | 0:02                                           | 3                                          |                                                                                                          |
| Cookie                               | I       | 0:45                                           | 36× 18                                     | Affects onlyparrots.‌[JE  only]Has no effect other than the particles as the parrot is killed instantly. |
| Poisonous Potato                     | I       | 0:05                                           | 4                                          | 60% chance.                                                                                              |
| Pufferfish                           | II      | 1:00                                           | 48× 24                                     |                                                                                                          |
| Suspicious Stew                      | I       | 0:12                                           | 9                                          | Must be crafted from aLily of the Valley.                                                                |
| Suspicious Stew                      | I       | 0:14                                           | 11× 5.5                                    | Tradedfrom expert farmervillagers.                                                                       |
| Spider Eye                           | I       | 0:05                                           | 2                                          | Dropped fromspidersand apply poison when eaten.                                                          |
| Cave Spider                          | I       | 0:07 (normal difficulty)0:15 (hard difficulty) | 5(normal difficulty)12× 6(hard difficulty) | Given when it attacks an entity.                                                                         |
| Pufferfish                           | I       | 0:03 (partially inflated)0:06 (fully inflated) | 2(partially inflated)4(fully inflated)     | Only when touched.                                                                                       |
| Bee                                  | I       | 0:10 (normal difficulty)0:18 (hard difficulty) | 8(normal difficulty)14× 7(hard difficulty) | Given when it attacks an entity.                                                                         |

## Brewing
| Potion           | Reagent, Base | Extended                    | Enhanced         | Effects                                                                                 |
|------------------|---------------|-----------------------------|------------------|-----------------------------------------------------------------------------------------|
| Potion of Poison |               | Potion of Poison (extended) | Potion of Poison | PoisonDamages by 1every 1.25 seconds.Enhanced: Poison IIDamages by 1 every 0.4 seconds. |

## Immune mobs
Cave spiders, ender dragons, undead mobs, spiders and witches in Bedrock Edition are unaffected by Poison. Witches are 85% resistant to damage from Poison in Java Edition.

## Data values
### ID
This section is about the effect IDs.  For the IDs on potions, see Potion § Item data.  For for the IDs on tipped arrows, see Arrow § Metadata.
Java Edition:

| Name   | Identifier | Numeric ID | Translation key         |
|--------|------------|------------|-------------------------|
| Poison | poison     | 19         | effect.minecraft.poison |

Bedrock Edition:

| Name   | Identifier | Numeric ID | Translation key |
|--------|------------|------------|-----------------|
| Poison | poison     | 19         | potion.poison   |

