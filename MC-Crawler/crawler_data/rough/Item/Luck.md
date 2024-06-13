# Luck
Luck is a status effect that makes it more likely to receive better loot from certain loot tables, contrary to Bad Luck.

## Contents
- 1 Effect
- 2 Causes
- 3 Immune mobs
- 4 Data values
	- 4.1 ID
- 5 History
- 6 Issues
- 7 Trivia
- 8 References

## Effect
Adds 1 × level to attribute generic.luck, making loot table entries with a high quality score more likely, and entries with negative quality less likely. It also increases the chances of bonus_rolls occurring. Currently, only fishing uses quality. The new weight of each entry is floor(base_weight + quality * generic.luck). Negative levels decrease luck.

Using a fishing rod enchanted with Luck of the Sea increases a player's luck while fishing equivalent to the generic.luck attribute, but doesn't actually grant the Luck status effect or increase the player's attribute.

## Causes
| Cause                          | Potency | Length |
|--------------------------------|---------|--------|
| Potion of Luck[tn 1]           | I       | 5:00   |
| Splash Potion of Luck[tn 1]    | I       | 5:00   |
| Lingering Potion of Luck[tn 1] | I       | 1:15   |
| Arrow of Luck                  | I       | 0:37   |

1. ↑ a b cPotions of Luck are unobtainable in Survival without using cheats.

## Immune mobs
While no mobs, except bosses, are immune to Luck, only players are actually affected.

## Data values
### ID
This section is about the effect IDs.  For the IDs on potions, see Potion § Item data.  For for the IDs on tipped arrows, see Arrow § Metadata.
| Name | Identifier | Numeric ID | Translation key         |
|------|------------|------------|-------------------------|
| Luck | `luck`     | `26`       | `effect.minecraft.luck` |

