# Big
Big is an effect that makes entities bigger. Entity size (both visual size and its hitbox) is multiplied by level+1. Mob drops are also multiplied: there are (level+1)3 rolls performed on a mob under this effect. This means, for example, that evoker with Big I always drops 8 totems of undying, calculated from (1+1)3, as there is a 100% chance to drop the totem on each roll. This evoker also drops anywhere from 0 to 8 emeralds, most likely 4, as there is a 50% chance to drop an emerald on each roll.

It is the counterpart to Small.

## Contents
- 1 Entities affected
- 2 Causes
- 3 Data values
	- 3.1 ID
- 4 History
- 5 Issues

## Entities affected
| Entity/Entities                | Is affected?                   |
|--------------------------------|--------------------------------|
| Players                        | Yes                            |
| Mobs                           | Yes (exceptbosses)             |
| Armor Stands                   | Yes, but only through`/effect` |
| Item FramesandGlow Item Frames | No                             |
| Items                          | No                             |
| BoatsandBoats with Chests      | No                             |
| Minecarts                      | No                             |

## Causes
| Cause                             | Potency | Length   | Notes                                                          |
|-----------------------------------|---------|----------|----------------------------------------------------------------|
| Potion of Big                     | I       | 3:00     | Size of the entity is doubled. Mob drops are multiplied by 8.  |
| Potion of Big(extended)           | I       | 8:00     | Size of the entity is doubled. Mob drops are multiplied by 8.  |
| Potion of BigII                   | II      | 1:30     | Size of the entity is tripled. Mob drops are multiplied by 27. |
| Splash Potion of Big              | I       | 3:00     | Size of the entity is doubled. Mob drops are multiplied by 8.  |
| Splash Potion of Big(extended)    | I       | 8:00     | Size of the entity is doubled. Mob drops are multiplied by 8.  |
| Splash Potion of BigII            | II      | 1:30     | Size of the entity is tripled. Mob drops are multiplied by 27. |
| Lingering Potion of Big           | I       | 0:45     | Size of the entity is doubled. Mob drops are multiplied by 8.  |
| Lingering Potion of Big(extended) | I       | 2:00     | Size of the entity is doubled. Mob drops are multiplied by 8.  |
| Lingering Potion of BigII         | II      | 0:22     | Size of the entity is tripled. Mob drops are multiplied by 27. |
| Arrow of Big                      | I       | 0:45     | Size of the entity is doubled. Mob drops are multiplied by 8.  |
| Arrow of Big(extended)            | I       | 2:00     | Size of the entity is doubled. Mob drops are multiplied by 8.  |
| Arrow of BigII                    | II      | 0:22     | Size of the entity is tripled. Mob drops are multiplied by 27. |
| Voting for`perma_effect`          | ?       | Infinity | If enabled, all players have the specified effect infinitely.  |

## Data values
### ID
This section is about the effect IDs.  For the IDs on potions, see Potion § Item data.  For for the IDs on tipped arrows, see Arrow § Metadata.
| Name | Identifier | Numeric ID | Translation key        |
|------|------------|------------|------------------------|
| Big  | `big`      | `34`       | `effect.minecraft.big` |

