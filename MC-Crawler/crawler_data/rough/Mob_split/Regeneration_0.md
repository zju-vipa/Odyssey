# Regeneration
Regeneration is a status effect that restores an entity's health over time.

## Contents
- 1 Effect
- 2 Causes
- 3 Brewing
- 4 Notes
- 5 Immune mobs
- 6 Data values
	- 6.1 ID
- 7 Advancements
- 8 History
- 9 Notes

## Effect
The amount of health healed over time is shown in the table below:

| Level | Ticks per | per second  |
|-------|-----------|-------------|
| 1     | 50        | 0.4× 0.2    |
| 2     | 25        | 0.8× 0.4    |
| 3     | 12        | 1.67× 0.835 |
| 4     | 6         | 3.33× 1.665 |
| 5     | 3         | 6.67× 3.335 |
| 6+    | 1         | 20× 10      |

Amplifiers outside the range 0–31 (corresponding to levels 1–32) are used modulo 32, making level 33 the same as level 1, etc.

## Causes
| Cause                                      | Potency                        | Length                              | Notes                                                                                                                                                  |
|--------------------------------------------|--------------------------------|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Potion of Regeneration                     | I                              | 0:45                                | 18× 9is regenerated.                                                                                                                                   |
| Potion of Regeneration(extended)           | I                              | 1:30‌[JE  only]<br/>2:00‌[BE  only] | 36× 18inJava Editionor 48× 24inBedrock Edition                                                                                                         |
| Potion of RegenerationII                   | II                             | 0:22                                | 17.6× 8.8                                                                                                                                              |
| Splash Potion of Regeneration              | I                              | 0:45‌[JE  only]<br/>0:33‌[BE  only] | 18× 9inJava Editionor 13.2× 6.6inBedrock Edition                                                                                                       |
| Splash Potion of Regeneration(extended)    | I                              | 1:30                                | 36× 18                                                                                                                                                 |
| Splash Potion of RegenerationII            | II                             | 0:22‌[JE  only]<br/>0:16‌[BE  only] | 17.6× 8.8inJava Editionor 12.8× 6.4inBedrock Edition                                                                                                   |
| Lingering Potion of Regeneration           | I                              | 0:11                                | The health regenerated depends how long the entity spent in the cloud.                                                                                 |
| Lingering Potion of Regeneration(extended) | I                              | 0:22‌[JE  only]<br/>0:30‌[BE  only] | The health regenerated depends how long the entity spent in the cloud.                                                                                 |
| Lingering Potion of RegenerationII         | II                             | 0:05                                | The health regenerated depends how long the entity spent in the cloud.                                                                                 |
| Arrow of Regeneration                      | I                              | 0:05                                | 2                                                                                                                                                      |
| Arrow of Regeneration(extended)            | I                              | 0:11‌[JE  only]<br/>0:15‌[BE  only] | 4.4× 2.2inJava Editionor 6inBedrock Edition                                                                                                            |
| Arrow of RegenerationII                    | II                             | 0:02                                | 1.6× 0.8                                                                                                                                               |
| Beaconset to Regeneration                  | I                              | 0:17                                | $Replenishes when in range. Requires beacon pyramid level 4. Due to a bug, beacon regeneration works at only\frac{5}{8}$the normal regeneration speed. |
| Suspicious Stew                            | I                              | 0:08‌[JE  only]<br/>0:06‌[BE  only] | Must be made withOxeye Daisy. Regenerates 3.2× 1.6inJava Editionor 2.4× 1.2inBedrock Edition                                                           |
| Golden Apple                               | II                             | 0:05                                | 4is regenerated.                                                                                                                                       |
| Enchanted Golden Apple                     | II‌[JE  only]<br/>V‌[BE  only] | 0:20‌[JE  only]<br/>0:30‌[BE  only] | 16× 8inJava Editionor 200× 100inBedrock Edition                                                                                                        |
| Totem of Undying                           | II                             | 0:45‌[JE  only]<br/>0:40‌[BE  only] | When being revived by it. Regenerates 36× 18inJava Editionor 32× 16inBedrock Edition.                                                                  |
| Spawning within the world                  | I                              | ∞                                   | Applies only tospiders on Hard difficulty.‌[JE  only]                                                                                                  |
| Unlockingtrades                            | I                              | 0:10                                | Applies only tovillagers. Regenerates 4                                                                                                                |
| Having lowhealth                           | I                              | 0:10                                | Applies only toAxolotls.                                                                                                                               |
| Killing a mob                              | I                              | +0:05 *Axolotls nearby              | When killing a mob that can be targeted by an axolotl while an axolotl is nearby                                                                       |

## Brewing
| Potion                      | Reagent, Base | Extended                               | Enhanced                    | Effects                                                                                                             |
|-----------------------------|---------------|----------------------------------------|-----------------------------|---------------------------------------------------------------------------------------------------------------------|
| <br/>Potion of Regeneration |               | <br/>Potion of Regeneration (extended) | <br/>Potion of Regeneration | Regeneration<br/>Restores health byevery 2.5 seconds.Enhanced:Regeneration IIRestores health by  every 1.2 seconds. |

## Notes
1. ↑MC-30946



## Immune mobs
Undead mobs and ender dragons are unaffected by Regeneration.

## Data values
### ID
This section is about the effect IDs.  For the IDs on potions, see Potion § Item data.  For for the IDs on tipped arrows, see Arrow § Metadata.
Java Edition:

| Name         | Identifier     | Numeric ID | Translation key                 |
|--------------|----------------|------------|---------------------------------|
| Regeneration | `regeneration` | `10`       | `effect.minecraft.regeneration` |

Bedrock Edition:

| Name         | Identifier     | Numeric ID | Translation key       |
|--------------|----------------|------------|-----------------------|
| Regeneration | `regeneration` | `10`       | `potion.regeneration` |

## Notes


| Java Edition only | Dolphin's Grace |
|-------------------|-----------------|

| Bedrock Edition only | Fatal Poison |
|----------------------|--------------|

| Java Edition only | Glowing |
|-------------------|---------|

| Java Edition only | Bad Luck Luck |
|-------------------|---------------|

| Java Edition only | Big Caring It's very slippery Sharing Small Sticky |
|-------------------|----------------------------------------------------|


