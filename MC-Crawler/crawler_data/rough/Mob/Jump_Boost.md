# Jump Boost
Jump Boost is a status effect that temporarily increases the jump height of the player.

## Contents
- 1 Mechanics
- 2 Causes
- 3 Brewing
- 4 Unaffected mobs
- 5 Notes
- 6 Data values
	- 6.1 ID
- 7 Advancements
- 8 History
- 9 Issues
- 10 Trivia
- 11 Gallery
- 12 References

## Mechanics
Jump Boost allows the player to jump higher than the normal 1.2522 blocks. Each level adds 50% to the base jump height. It also reduces fall damage by 1 each level. 

Arbitrary levels can be set via commands. In Java Edition, negative levels decrease jump height and increase fall damage (which also causes the player to start taking damage from short falls that would normally do no damage); extreme negative levels eliminates all jumping ability and causes damage even when stepping off a slab.

## Causes
| Cause                                 | Potency | Length                              | Notes                                                                                                      |
|---------------------------------------|---------|-------------------------------------|------------------------------------------------------------------------------------------------------------|
| Potion of Leaping                     | I       | 3:00                                | $Increases jump height to 1\frac{13}{16}$blocks.                                                           |
| Potion of Leaping(extended)           | I       | 8:00                                | $Increases jump height to 1\frac{13}{16}$blocks, but for a longer duration.                                |
| Potion of LeapingII                   | II      | 1:30                                | $Increases jump height to 2\frac{1}{2}$blocks.                                                             |
| Splash Potion of Leaping              | I       | 3:00‌[JE  only]<br/>2:15‌[BE  only] | $Increases jump height to 1\frac{13}{16}$blocks.                                                           |
| Splash Potion of Leaping(extended)    | I       | 8:00‌[JE  only]<br/>6:00‌[BE  only] | $Increases jump height to 1\frac{13}{16}$blocks, but for a longer duration.                                |
| Splash Potion of LeapingII            | II      | 1:30‌[JE  only]<br/>1:07‌[BE  only] | $Increases jump height to 2\frac{1}{2}$blocks.                                                             |
| Lingering Potion of Leaping           | I       | 0:45                                | $Moving into the particle cloud increases jump height to 1\frac{13}{16}$blocks.                            |
| Lingering Potion of Leaping(extended) | I       | 2:00                                | $Moving into the particle cloud increases jump height to 1\frac{13}{16}$blocks, but for a longer duration. |
| Lingering Potion of LeapingII         | II      | 0:22                                | $Moving into the particle cloud increases jump height to 2\frac{1}{2}$blocks.                              |
| Arrow of Leaping                      | I       | 0:22                                | $Getting hit by the arrow increases jump height to 1\frac{13}{16}$blocks.                                  |
| Arrow of Leaping(extended)            | I       | 1:00                                | $Getting hit by the arrow increases jump height to 1\frac{13}{16}$blocks, but for a longer duration.       |
| Arrow of LeapingII                    | II      | 0:11                                | $Getting hit by the arrow increases jump height to 2\frac{1}{2}$blocks.                                    |
| Beaconset to Jump Boost               | I       | 0:05 – 0:17                         | Replenishes when in range.                                                                                 |
| Beaconset to Jump Boost II            | II      | 0:17                                | Replenishes when in range. Requires beacon pyramid level 4.                                                |
| Suspicious Stew                       | I       | 0:06                                | Must be made with aCornflower.                                                                             |
| Suspicious Stew                       | I       | 0:08                                | Tradedfrom expert farmervillagers.                                                                         |
| Suspicious Stew                       | I       | 0:07-0:10                           | Found inshipwrecksupply chests andDesert WellSuspicious Sand.                                              |

## Brewing
| Potion                 | Reagent, base | Extended                          | Enhanced                  | Effects                                                                                                     |
|------------------------|---------------|-----------------------------------|---------------------------|-------------------------------------------------------------------------------------------------------------|
| <br/>Potion of Leaping |               | <br/>Potion of Leaping (extended) | <br/>Potion of Leaping II | $Increases jump height to 1\frac{13}{16}$blocks.Enhanced:Jump Boost IIIncreases jump height to 21⁄2 blocks. |

## Unaffected mobs
Shulkers, withers, and the ender dragon are unaffected by Jump Boost.

## Notes
- InJava Edition, when at maximum level, jumping is not changed, but aplayertakes 256× 128less falldamage.
- At level 15, the increased height exceeds the maximum possible damage reduction, resulting in fall damage upon landing.
- At level 33, a player jumping on the spot is killed by fall damage upon landing, receiving thedeath message"<player> fell from a high place".
- InJava Edition, starting at level 128 and up, the player can no longer jump because of integer overflow.‌[until JE 1.20.5]
- At high enough levels (achievable only with commands), the player may jump hundreds of blocks high, enough to exceed Y=319. At level 127 it is possible to jump 374 blocks up.
- The actual max height the player can reach with any given level of Jump Boost can be approximated using this quadratic function0.0308354x^2 + 0.744631x + 1.836131wherexis the amplifier.

## Data values
### ID
This section is about the effect IDs.  For the IDs on potions, see Potion § Item data.  For for the IDs on tipped arrows, see Arrow § Metadata.
Java Edition:

| Name       | Identifier   | Numeric ID | Translation key               |
|------------|--------------|------------|-------------------------------|
| Jump Boost | `jump_boost` | `8`        | `effect.minecraft.jump_boost` |

Bedrock Edition:

| Name       | Identifier   | Numeric ID | Translation key |
|------------|--------------|------------|-----------------|
| Jump Boost | `jump_boost` | `8`        | `potion.jump`   |

