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

| Source | Roll Chance | Quantity (Roll Chance) |           |            |             |
|--------|-------------|------------------------|-----------|------------|-------------|
|        |             | Default                | Looting I | Looting II | Looting III |
| Stray  | 1[d 1]      | 1 (50%)                | 1 (75%)   | 1 (87.5%)  | 1 (93.75%)  |


↑ Only dropped when kill credit is given to the player


Bogged have a 50% chance of dropping 1 arrow of Poison when killed by a player.‌[upcoming: JE 1.21 & BE 1.21] Each level of Looting increases the chance of this drop by 50% of the previous chance. This results in a maximum of 93.75% with Looting III.

| Source | Roll Chance | Quantity (Roll Chance) |           |            |             |
|--------|-------------|------------------------|-----------|------------|-------------|
|        |             | Default                | Looting I | Looting II | Looting III |
| Bogged | 1[d 1]      | 1 (50%)                | 1 (75%)   | 1 (87.5%)  | 1 (93.75%)  |


↑ Only dropped when kill credit is given to the player


### Crafting
| Ingredients                    | Crafting recipe           |
|--------------------------------|---------------------------|
| Arrow+MatchingLingering Potion | 8888888888888888888888888 |

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


Arrow of Regeneration
Arrow of Swiftness
Arrow of Fire Resistance
Arrow of Healing
Arrow of Night Vision
Arrow of Strength
Arrow of Leaping
Arrow of Invisibility
Arrow of Poison
Arrow of Weakness
Arrow of Slowness
Arrow of Harming
Arrow of Water Breathing
Arrow of Luck‌[JE  only]
Arrow of Decay‌[BE  only]
Arrow of the Turtle Master
Arrow of Slow Falling
Arrow of Oozing‌[upcoming: JE 1.21 & BE 1.21.0]
Arrow of Wind Charging‌[upcoming: JE 1.21 & BE 1.21.0]
Arrow of Weaving‌[upcoming: JE 1.21 & BE 1.21.0]
Arrow of Infestation‌[upcoming: JE 1.21 & BE 1.21.0]

Arrows of Harming (and arrows of Healing when used against undead mobs) do not add a static amount of damage to the arrow.[1] Instead, the arrow's damage is first calculated, then checked to see if it is below 12 × 6. If the arrow's damage is less than 12, the Harming effect of the arrow makes up the difference, to ensure the arrow does exactly 12 × 6. Therefore, an unenchanted bow cannot deal more than 12 damage using Harming (or Healing) arrows, as it can deal a maximum of 11 × 5.5 damage on level ground. However, if the arrow would deal more than 12 damage, the harming effect is entirely neutralized. This means that bows enchanted with Power I through Power III has a chance to not utilize the arrow at full charge, and any Power level above III never utilizes arrows of Harming effectively at full charge when against unarmored mobs/players. 

#### No-effect tipped arrows
In Java Edition, it is possible to craft tipped arrows using lingering water bottles as well as Awkward, Thick, and Mundane lingering potions. If crafted with a water bottle, the arrow is called an arrow of Splashing. If crafted with Mundane, Awkward, or Thick potions, it is called a tipped arrow.[2] Tipped arrows crafted from different potions do not stack, as resultant tipped arrows all have different potion tags.

In Bedrock Edition, all four kinds as well as the long mundane tipped arrow aren't obtainable either in Creative, by cauldrons, by crafting, or by commands.

All four kinds generate blue particles in flight and upon landing, but otherwise behave like regular arrows. In particular, arrow of Splashing has no effect on fire and campfires and when shot from a bow with the Flame enchantment, can light candles, campfires and TNT just like regular arrows on fire. 

| Icon | Name               |
|------|--------------------|
|      | Arrow of Splashing |
|      | Tipped Arrow       |

#### Uncraftable tipped arrows
In Java Edition, the uncraftable tipped arrow is a tipped arrow with no effect that is unobtainable in regular gameplay. It is available in two variants that don't stack together:

- /give @s minecraft:tipped_arrow{Potion:"minecraft:empty"}- arrow assigned an effect placeholder "empty"
- /give @s minecraft:tipped_arrow- arrow not assigned any effect.

The uncraftable arrow doesn't differ from regular arrows in behavior when used as a projectile.

| Icon | Name                     |
|------|--------------------------|
|      | Uncraftable Tipped Arrow |

## Data values
### ID
Java Edition:

| Name         | Identifier   | Form | Item tags | Translation key                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|--------------|--------------|------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Tipped Arrow | tipped_arrow | Item | arrows    | item.minecraft.tipped_arrowitem.minecraft.tipped_arrow.effect.emptyitem.minecraft.tipped_arrow.effect.wateritem.minecraft.tipped_arrow.effect.mundaneitem.minecraft.tipped_arrow.effect.thickitem.minecraft.tipped_arrow.effect.awkwarditem.minecraft.tipped_arrow.effect.night_visionitem.minecraft.tipped_arrow.effect.invisibilityitem.minecraft.tipped_arrow.effect.leapingitem.minecraft.tipped_arrow.effect.fire_resistanceitem.minecraft.tipped_arrow.effect.swiftnessitem.minecraft.tipped_arrow.effect.slownessitem.minecraft.tipped_arrow.effect.water_breathingitem.minecraft.tipped_arrow.effect.healingitem.minecraft.tipped_arrow.effect.harmingitem.minecraft.tipped_arrow.effect.poisonitem.minecraft.tipped_arrow.effect.regenerationitem.minecraft.tipped_arrow.effect.strengthitem.minecraft.tipped_arrow.effect.weaknessitem.minecraft.tipped_arrow.effect.levitationitem.minecraft.tipped_arrow.effect.luckitem.minecraft.tipped_arrow.effect.turtle_masteritem.minecraft.tipped_arrow.effect.slow_falling |

| Name  | Identifier | Entity tags              | Translation key        |
|-------|------------|--------------------------|------------------------|
| Arrow | arrow      | arrowsimpact_projectiles | entity.minecraft.arrow |

Bedrock Edition:

| Name         | Identifier | Numeric ID | Form | Item tags       | Translation key                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|--------------|------------|------------|------|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Tipped Arrow | arrow      | 301        | Item | minecraft:arrow | item.tipped_arrow.nametipped_arrow.effect.watertipped_arrow.effect.mundanetipped_arrow.effect.thicktipped_arrow.effect.awkwardtipped_arrow.effect.nightVisiontipped_arrow.effect.invisibilitytipped_arrow.effect.jumptipped_arrow.effect.fireResistancetipped_arrow.effect.moveSpeedtipped_arrow.effect.moveSlowdowntipped_arrow.effect.waterBreathingtipped_arrow.effect.healtipped_arrow.effect.harmtipped_arrow.effect.poisontipped_arrow.effect.regenerationtipped_arrow.effect.damageBoosttipped_arrow.effect.weaknesstipped_arrow.effect.withertipped_arrow.effect.turtleMastertipped_arrow.effect.slowFalling |

| Name  | Identifier | Numeric ID | Translation key   |
|-------|------------|------------|-------------------|
| Arrow | arrow      | 80         | entity.arrow.name |

### Metadata
In Bedrock Edition, arrows use the following item data values:

| Arrow                      | Regular | Extended | Enhanced(Level II) |
|----------------------------|---------|----------|--------------------|
| Arrow                      | 0       | N/A      | N/A                |
| Arrow of Splashing         | 1       | N/A      | N/A                |
| Tipped Arrow (Mundane)     | 2       | 3        | N/A                |
| Tipped Arrow (Thick)       | 4       | N/A      | N/A                |
| Tipped Arrow (Awkward)     | 5       | N/A      | N/A                |
| Arrow of Night Vision      | 6       | 7        | N/A                |
| Arrow of Invisibility      | 8       | 9        | N/A                |
| Arrow of Leaping           | 10      | 11       | 12                 |
| Arrow of Fire Resistance   | 13      | 14       | N/A                |
| Arrow of Swiftness         | 15      | 16       | 17                 |
| Arrow of Slowness          | 18      | 19       | 43                 |
| Arrow of Water Breathing   | 20      | 21       | N/A                |
| Arrow of Healing           | 22      | N/A      | 23                 |
| Arrow of Harming           | 24      | N/A      | 25                 |
| Arrow of Poison            | 26      | 27       | 28                 |
| Arrow of Regeneration      | 29      | 30       | 31                 |
| Arrow of Strength          | 32      | 33       | 34                 |
| Arrow of Weakness          | 35      | 36       | N/A                |
| Arrow of Decay             | 37      | N/A      | N/A                |
| Arrow of the Turtle Master | 38      | 39       | 40                 |
| Arrow of Slow Falling      | 41      | 42       | N/A                |

### Entity data
Tipped arrows have entity data that define various properties of the entity.

Java Edition:

Main article: Entity format

 Entity data
Tags common to all arrows
Tags common to all entities
Tags common to all projectiles
Note: An arrow entity is a tipped arrow if it has either the Potion or CustomPotionEffects tag.
Tags common to all potion effects
 Color: Used by the arrow entity, for displaying the custom potion color of a fired arrow item that had a CustomPotionColor tag.  The numeric color code are calculated from the Red, Green and Blue components using this formula: Red<<16 + Green<<8 + Blue. For positive values larger than 0x00FFFFFF, the top byte is ignored. All negative values remove the particles.

Bedrock Edition:

See Bedrock Edition level format/Entity format.
