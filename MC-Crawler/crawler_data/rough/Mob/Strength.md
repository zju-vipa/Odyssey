# Strength
Strength is a status effect which increases attack power.

## Contents
- 1 Effect
- 2 Causes
- 3 Brewing
- 4 Immune mobs
- 5 Data values
	- 5.1 ID
- 6 Advancements
- 7 History
- 8 References

## Effect
Increases melee damage by 3 × level in Java Edition. Negative levels decrease melee damage, with attacks being ignored entirely if damage would be 0 or lower.

In Bedrock Edition, melee damage under the Strength effect can be found through the equation BaseDamage×1.3level+1.3level−10.3, where BaseDamage is the default damage of whatever weapon or tool is used to attack.[1] Example for an iron sword:

- Normal: 7
- Level 1: 10.1× 5.05
- Level 2: 14.13× 7.065

## Causes
| Cause                                  | Potency | Length      | Notes                                                                                                  |
|----------------------------------------|---------|-------------|--------------------------------------------------------------------------------------------------------|
| Potion of Strength                     | I       | 3:00        |                                                                                                        |
| Potion of Strength(extended)           | I       | 8:00        |                                                                                                        |
| Potion of StrengthII                   | II      | 1:30        |                                                                                                        |
| Splash Potion of Strength              | I       | 3:00        |                                                                                                        |
| Splash Potion of Strength (extended)   | I       | 8:00        |                                                                                                        |
| Splash Potion of StrengthII            | II      | 1:30        |                                                                                                        |
| Lingering Potion of Strength           | I       | 0:45        | Potion cloud lasts 30 seconds at most                                                                  |
| Lingering Potion of Strength(extended) | I       | 2:00        | Potion cloud lasts 30 seconds at most                                                                  |
| Lingering Potion of StrengthII         | II      | 0:23        | Potion cloud lasts 30 seconds at most                                                                  |
| Arrow of Strength                      | I       | 0:23        |                                                                                                        |
| Arrow of Strength(extended)            | I       | 1:00        |                                                                                                        |
| Arrow of StrengthII                    | II      | 0:12        |                                                                                                        |
| Beacon                                 | I       | 0:05 – 0:17 | Replenishes when within range, level 3 only                                                            |
| Beacon                                 | II      | 0:17        | Replenishes when within range, level 4 only                                                            |
| Being azombie villager                 | I       | 2:00 – 5:00 | When being cured and the difficulty is Normal. Time is always equivalent to the total conversion time. |
| Being azombie villager                 | II      | 2:00 – 5:00 | When being cured and the difficulty is Hard. Time is always equivalent to the total conversion time.   |
| Spawning within the world              | I       | ∞           | Only applies to somespiders on Hard difficulty.[note 1]‌[JE  only]                                     |

1. ↑The chance for a spider to have an effect is (10×clamped regional difficulty)%, and the chance for Strength is 20% of that.

## Brewing
| Potion                  | Reagent, Base | Extended                           | Enhanced                | Effects                                                                                                 |
|-------------------------|---------------|------------------------------------|-------------------------|---------------------------------------------------------------------------------------------------------|
| <br/>Potion of Strength |               | <br/>Potion of Strength (extended) | <br/>Potion of Strength | Strength<br/>Increases melee attack damage by 3.Enhanced:Strength IIIncreases melee attack damage by 6. |

## Immune mobs
Withers and ender dragons are immune to Strength. While not immune, any mobs that cannot attack are unaffected by Strength.

## Data values
### ID
This section is about the effect IDs.  For the IDs on potions, see Potion § Item data.  For for the IDs on tipped arrows, see Arrow § Metadata.
Java Edition:

| Name     | Identifier | Numeric ID | Translation key             |
|----------|------------|------------|-----------------------------|
| Strength | `strength` | `5`        | `effect.minecraft.strength` |

Bedrock Edition:

| Name     | Identifier | Numeric ID | Translation key      |
|----------|------------|------------|----------------------|
| Strength | `strength` | `5`        | `potion.damageBoost` |

