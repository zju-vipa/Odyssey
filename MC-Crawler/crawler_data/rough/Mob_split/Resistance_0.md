# Resistance
Resistance is a status effect that reduces incoming damage.

## Contents
- 1 Effect
- 2 Causes
- 3 Immune mobs
- 4 Notes
- 5 Data values
	- 5.1 ID
- 6 Advancements
- 7 History
- 8 Issues

## Effect
Resistance reduces incoming damage by 20% × level from all sources except for starvation, the void, and explosions with extreme power values (negative values (128 to 255 (mod 256) or -128 to -1 (mod 256)) stored in an NBT, see entity format) such as creepers and ghast fireballs.

Resistance is applied only to the remaining damage after all other damage reductions (armor and enchantments), but before rounding down to a whole number. This means any equipped armor pieces still loses the usual amount of durability, even at level 5+ where the potion effect grants complete immunity to most sources.

## Causes
| Cause                                           | Potency | Length                              | Notes                                                       |
|-------------------------------------------------|---------|-------------------------------------|-------------------------------------------------------------|
| Beaconset to Resistance                         | I       | 0:08 – 0:17                         | Replenishes when in range. Requires beacon pyramid level 2. |
| Beaconset to Resistance II                      | II      | 0:17                                | Replenishes when in range. Requires beacon pyramid level 4. |
| Enchanted Golden Apple                          | I       | 5:00                                |                                                             |
| Potion of the Turtle Master                     | III     | 0:20                                |                                                             |
| Potion of the Turtle Master(extended)           | III     | 0:40                                |                                                             |
| Potion of the Turtle MasterII                   | IV      | 0:20                                |                                                             |
| Splash Potion of the Turtle Master              | III     | 0:20‌[JE  only]<br/>0:15‌[BE  only] |                                                             |
| Splash Potion of the Turtle Master(extended)    | III     | 0:40‌[JE  only]<br/>0:30‌[BE  only] |                                                             |
| Splash Potion of the Turtle MasterII            | IV      | 0:20‌[JE  only]<br/>0:15‌[BE  only] |                                                             |
| Lingering Potion of the Turtle Master           | III     | 0:05                                |                                                             |
| Lingering Potion of the Turtle Master(extended) | III     | 0:10                                |                                                             |
| Lingering Potion of the Turtle MasterII         | IV      | 0:05                                |                                                             |
| Arrow of the Turtle Master                      | III     | 0:02                                |                                                             |
| Arrow of the Turtle Master(extended)            | III     | 0:05                                |                                                             |
| Arrow of the Turtle MasterII                    | IV      | 0:02                                |                                                             |

## Immune mobs
Withers and ender dragons are immune to Resistance; it grants no benefit to them.

## Notes
- Level 5+ gives the player or mob full immunity to alldamage, with the exceptions mentioned earlier.

## Data values
### ID
This section is about the effect IDs.  For the IDs on potions, see Potion § Item data.  For for the IDs on tipped arrows, see Arrow § Metadata.
Java Edition:

| Name       | Identifier   | Numeric ID | Translation key               |
|------------|--------------|------------|-------------------------------|
| Resistance | `resistance` | `11`       | `effect.minecraft.resistance` |

Bedrock Edition:

| Name       | Identifier   | Numeric ID | Translation key     |
|------------|--------------|------------|---------------------|
| Resistance | `resistance` | `11`       | `potion.resistance` |


