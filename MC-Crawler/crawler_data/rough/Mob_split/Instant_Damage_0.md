# Instant Damage
Instant Damage is an instant status effect that decreases health for players and living mobs and heals the undead.

## Contents
- 1 Effect
- 2 Causes
- 3 Brewing
- 4 Immune mobs
- 5 Data values
	- 5.1 ID
- 6 History
- 7 Issues

## Effect
Instant Damage inflicts magic damage of 3 × 2level. Undead mobs (including the wither) are healed as if with Instant Health instead. Death is reported as "<player> was killed by magic". When applied using a lingering potion, damage is inflicted every second. As this is magic damage, it can be decreased only via Resistance and Protection.‌[Java Edition  only]

## Causes
| Cause                         | Potency | Damage                       | Heals undead                | Length  | Notes                                     |
|-------------------------------|---------|------------------------------|-----------------------------|---------|-------------------------------------------|
| Potion of Harming             | I       | 6                            |                             | Instant |                                           |
| Potion of HarmingII           | II      | 12× 6                        |                             | Instant |                                           |
| Splash Potion of Harming      | I       | 6                            | 4                           | Instant | Witchesthrow this potion at their target. |
| Splash Potion of HarmingII    | II      | 12× 6                        | 8                           | Instant |                                           |
| Lingering Potion of Harming   | I       | 3per second<br/>15× 7.5total | 2per second<br/>10total     | 0:05    |                                           |
| Lingering Potion of HarmingII | II      | 6per second<br/>30× 15total  | 4per second<br/>20× 10total | 0:05    | Dragon fireballscause this much harm.     |
| Arrow of Harming              | I       | 6                            | 4                           | Instant |                                           |
| Arrow of HarmingII            | II      | 12× 6                        | 8                           | Instant |                                           |

## Brewing
| Potion                 | Reagent, Base | Extended | Enhanced               | Effects                                                                                     |
|------------------------|---------------|----------|------------------------|---------------------------------------------------------------------------------------------|
| <br/>Potion of Harming |               | -        | <br/>Potion of Harming | Instant Damage<br/>Damages 6per potion.Enhanced:Instant Damage IIDamages 12 × 6 per potion. |

| Potion                 | Reagent, Base | Extended | Enhanced               | Effects                                                                                     |
|------------------------|---------------|----------|------------------------|---------------------------------------------------------------------------------------------|
| <br/>Potion of Harming |               | -        | <br/>Potion of Harming | Instant Damage<br/>Damages 6per potion.Enhanced:Instant Damage IIDamages 12 × 6 per potion. |

## Immune mobs
- Witchesare 85% resistant to Instant Damage.
- Endermenare immune to Instant Damage from splash potions and tipped arrows, but not fromcommandsor lingering potions.
- Ender dragonis immune to Instant Damage, if it isn't player-based damage, e.g. potions shot from adispenser.

## Data values
### ID
This section is about the effect IDs.  For the IDs on potions, see Potion § Item data.  For for the IDs on tipped arrows, see Arrow § Metadata.
Java Edition:

| Name           | Identifier       | Numeric ID | Translation key                   |
|----------------|------------------|------------|-----------------------------------|
| Instant Damage | `instant_damage` | `7`        | `effect.minecraft.instant_damage` |

Bedrock Edition:

| Name           | Identifier       | Numeric ID | Translation key |
|----------------|------------------|------------|-----------------|
| Instant Damage | `instant_damage` | `7`        | `potion.harm`   |


