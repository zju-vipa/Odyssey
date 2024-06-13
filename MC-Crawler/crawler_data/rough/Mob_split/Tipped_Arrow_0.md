# Tipped Arrow
A tipped arrow is a variant of the regular arrow that can apply status effects to players and mobs.

## Contents
- 1 Obtaining
	- 1.1 Picking up arrows
	- 1.2 Mob loot
	- 1.3 Crafting
	- 1.4 Trading
	- 1.5 Villager gifts
	- 1.6 Cauldrons
- 2 Usage
	- 2.1 Special properties
		- 2.1.1 No-effect tipped arrows
		- 2.1.2 Uncraftable tipped arrows
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Metadata
	- 4.3 Entity data
- 5 Advancements
- 6 History
- 7 Issues
- 8 Gallery
	- 8.1 Renders
		- 8.1.1 Tipped arrow
	- 8.2 Screenshots
- 9 References

## Obtaining
### Picking up arrows
Main article: Arrow § Picking up arrows
Similarly to regular arrows, players can pick up tipped arrows that have been shot by dispensers, or other players in Survival or Adventure mode. Unlike regular arrows, tipped arrows shot by an Infinity-enchanted bow can be picked up, as they are not affected by the enchantment.

### Mob loot
Strays have a 50% chance of dropping 1 arrow of Slowness when killed by a player. Each level of Looting increases the chance of this drop by 50% of the previous chance. This results in a maximum of 93.75% with Looting III.

| Source | Roll Chance     | Quantity (Roll Chance) |           |            |             |
|--------|-----------------|------------------------|-----------|------------|-------------|
|        |                 | Default                | Looting I | Looting II | Looting III |
| Stray  | 50%–93.75%[d 1] | 1 (50%)                | 1 (75%)   | 1 (87.5%)  | 1 (93.75%)  |

1. ↑Only dropped when kill credit is given to the player

Bogged have a 50% chance of dropping 1 arrow of Poison when killed by a player.‌[upcoming: JE 1.21 & BE 1.21] Each level of Looting increases the chance of this drop by 50% of the previous chance. This results in a maximum of 93.75% with Looting III.

| Source | Roll Chance     | Quantity (Roll Chance) |           |            |             |
|--------|-----------------|------------------------|-----------|------------|-------------|
|        |                 | Default                | Looting I | Looting II | Looting III |
| Bogged | 50%–93.75%[d 1] | 1 (50%)                | 1 (75%)   | 1 (87.5%)  | 1 (93.75%)  |

1. ↑Only dropped when kill credit is given to the player

### Crafting
| Ingredients                         | Crafting recipe           |
|-------------------------------------|---------------------------|
| Arrow+<br/>MatchingLingering Potion | 8888888888888888888888888 |

### Trading
In Bedrock Edition, master-level fletcher villagers have a 1⁄2 chance to sell 5 tipped arrows for 2 emeralds and 5 arrows. In Java Edition, they have a 2⁄3 chance to sell 5 tipped arrows for 2 emeralds and 5 arrows. Trades in Java Edition can be the base effect, level II, or extended; in Bedrock Edition, only the arrow of decay is level II.

- Arrow ofFire Resistance
- Arrow ofHarming
- Arrow ofHealing
- Arrow ofInvisibility
- Arrow ofLeaping
- Arrow ofNight Vision
- Arrow ofPoison
- Arrow ofRegeneration
- Arrow ofSlowness
- Arrow ofStrength
- Arrow ofSwiftness
- Arrow of theTurtle Master
- Arrow ofWater Breathing
- Arrow ofWeakness
- Arrow ofSlow Falling‌[Java Edition  only]
- Arrow ofDecay‌[Bedrock Edition  only]
- Arrow ofInfested‌[upcoming: JE 1.21 & BE 1.21]
- Arrow ofOozing‌[upcoming: JE 1.21 & BE 1.21]
- Arrow ofWeaving‌[upcoming: JE 1.21 & BE 1.21]
- Arrow ofWind Charged‌[upcoming: JE 1.21 & BE 1.21]

The list above includes every potion effect except for Slow Falling in Bedrock Edition and Luck in Java Edition. Trading is the only legitimate way to obtain arrows of Decay in Survival mode.

### Villager gifts
In Java Edition, any tipped arrow (except for Luck) can be obtained as a reward item from fletcher villagers when the player has the Hero of the Village status effect.

### Cauldrons
Main article: Cauldron § Holding potions
In Bedrock Edition, tipped arrows can also be obtained by using arrows on cauldrons that contain potions. The number of tipped arrows created depends on the amount of potion inside a cauldron, which is measured in levels equivalent to 1⁄6 of its maximum capacity, or half of what a bottle can hold. For every quantity of up to 16 arrows tipped, the amount of potion remaining is reduced by 1 level. However, any potion in the bottom half of a cauldron is only counted as a single level for the purposes of tipping arrows. This means that a maximum of 64 arrows can be tipped from a full cauldron, either at once or in parts. This is more efficient than using lingering potions, as up to 21.33 arrows can be tipped per potion.

## Usage
Main article: Arrow § Common properties
Tipped arrows share many of the same characteristics as regular arrows as projectiles.

### Special properties
See also:  § Crafting

Tipped arrows are arrows that imbue a potion effect when hitting a mob or player. The duration of the effect is 1⁄8 that of the corresponding potion, if applicable, and is not affected by the power of the arrow. The status effect is the same as the regular power effect for the potion. If a bow is enchanted with Infinity, tipped arrows are still consumed. 

The types of arrows are:

- Arrow of Regeneration
- Arrow of Swiftness
- Arrow of Fire Resistance
- Arrow of Healing
- Arrow of Night Vision
- Arrow of Strength
- Arrow of Leaping
- Arrow of Invisibility
- Arrow of Poison
- Arrow of Weakness
- Arrow of Slowness
- Arrow of Harming
- Arrow of Water Breathing
- Arrow of Luck‌[JE  only]
- Arrow of Decay‌[BE  only]
- Arrow of the Turtle Master
- Arrow of Slow Falling
- Arrow of Oozing‌[upcoming: JE 1.21 & BE 1.21.0]
- Arrow of Wind Charging‌[upcoming: JE 1.21 & BE 1.21.0]
- Arrow of Weaving‌[upcoming: JE 1.21 & BE 1.21.0]
- Arrow of Infestation‌[upcoming: JE 1.21 & BE 1.21.0]

Arrows of Harming (and arrows of Healing when used against undead mobs) do not add a static amount of damage to the arrow.[1] Instead, the arrow's damage is first calculated, then checked to see if it is below 12 × 6. If the arrow's damage is less than 12, the Harming effect of the arrow makes up the difference, to ensure the arrow does exactly 12 × 6. Therefore, an unenchanted bow cannot deal more than 12 damage using Harming (or Healing) arrows, as it can deal a maximum of 11 × 5.5 damage on level ground. However, if the arrow would deal more than 12 damage, the harming effect is entirely neutralized. This means that bows enchanted with Power I through Power III has a chance to not utilize the arrow at full charge, and any Power level above III never utilizes arrows of Harming effectively at full charge when against unarmored mobs/players. 

